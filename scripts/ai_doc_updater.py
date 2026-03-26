#!/usr/bin/env python3
"""
Called by the AI doc updater workflow.
1. Fetches PR title + description from the app repo (namlisa/namlisa_app)
2. Reads all article markdown files
3. Asks Gemini Pro which articles need updating AND which new articles to create
4. Applies the changes to the markdown files
"""

import os, sys, json, glob, re
import requests
import google.generativeai as genai

GH_TOKEN = os.environ['GH_TOKEN']
PR_NUMBER = os.environ['PR_NUMBER']
APP_REPO = os.environ.get('APP_REPO', 'namlisa/namlisa_app')
GEMINI_API_KEY = os.environ['GEMINI_API_KEY']

GH_HEADERS = {
    "Authorization": f"Bearer {GH_TOKEN}",
    "Accept": "application/vnd.github+json",
}

def fetch_pr_context():
    pr = requests.get(
        f"https://api.github.com/repos/{APP_REPO}/pulls/{PR_NUMBER}",
        headers=GH_HEADERS,
    ).json()

    # Fetch the actual diff to give Gemini real data instead of just title/description
    diff_resp = requests.get(
        f"https://api.github.com/repos/{APP_REPO}/pulls/{PR_NUMBER}",
        headers={**GH_HEADERS, "Accept": "application/vnd.github.diff"},
    )
    diff_text = diff_resp.text if diff_resp.status_code == 200 else ''
    # Truncate very large diffs to avoid exceeding token limits
    if len(diff_text) > 30000:
        diff_text = diff_text[:30000] + '\n\n... (diff truncated at 30KB) ...'

    return {
        'title': pr.get('title', ''),
        'body': pr.get('body', '') or '',
        'diff': diff_text,
    }

def read_all_articles():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    files = glob.glob(f"{repo_root}/articles/**/*.md", recursive=True)
    articles = {}
    for f in sorted(files):
        rel = os.path.relpath(f, repo_root)
        with open(f) as fh:
            articles[rel] = fh.read()
    return articles

def ask_gemini(pr_context, articles):
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-2.5-pro")

    full_articles = '\n\n'.join([
        f"=== {path} ===\n{content}"
        for path, content in articles.items()
    ])

    prompt = f"""You are the documentation author for the FundGen Ambassador App — a fundraising campaign management tool used by Jewish fundraising ambassadors. The help center is the primary support resource for ambassadors and campaign admins, available in Hebrew and English.

A pull request was just merged into the app codebase. Your job is to:

1. **Update existing articles** that are now outdated or incomplete due to these changes
2. **Create new articles** for significant new features, integrations, or user flows introduced in this PR that have NO existing documentation

---

PR Title: {pr_context['title']}

PR Description:
{pr_context['body']}

Actual code diff (this is the ground truth of what changed):
{pr_context['diff']}

Current help center articles (paths + full content):
{full_articles}

---

## RULES

### CRITICAL — accuracy over coverage:
- ONLY update or create documentation for features explicitly described in the PR title, description, and code diff above. Do NOT infer, guess, or extrapolate features beyond what is stated.
- The code diff is the GROUND TRUTH. If the diff shows a minor bug fix (e.g., fixing a URL parameter, null check, formatting), return an empty changes array. Do NOT invent new features or roles that don't appear in the diff.
- If the PR title/description describes a backend-only change (infrastructure, CI, refactoring, performance fixes, bug fixes with no behavior change), return an empty changes array. When in doubt, do nothing.
- NEVER invent UI elements, buttons, screens, menu items, roles, permissions, or workflows that aren't explicitly shown in the code diff. If the diff doesn't add a new role, don't document one.
- NEVER add features to unrelated articles. If the PR is about WhatsApp, don't touch donation or permission articles unless the PR description explicitly connects them.
- Doing nothing is always better than hallucinating. Most PRs will NOT need doc updates. Bug fix PRs almost NEVER need doc updates.

### For EXISTING articles:
- Update any article that is now outdated, incomplete, or missing steps due to the PR changes
- Keep the YAML frontmatter exactly as-is (never change intercom_article_id, state, collection, etc.)

### For NEW articles:
- If the PR introduces a significant new feature, integration, or user-facing flow with NO existing documentation, write a complete new article for it
- New article YAML frontmatter:
  - `intercom_article_id`: leave as empty string ""
  - `state`: "published" for shipped features, "draft" for incomplete/experimental
  - `collection` + `collection_he`: choose the best fit:
    - `"Get Started"` / `"התחילו כאן"` → onboarding, account setup, first steps
    - `"Campaign Management"` / `"ניהול הקמפיין"` → admin features, campaign config, permissions, team management
    - `"Features"` / `"פונקציות"` → specific features ambassadors use day-to-day
    - `"Collecting Donations"` / `"איסוף תרומות"` → donation tracking, leaderboards, progress
- File naming: lowercase, hyphens, `.md` (e.g., `connecting-whatsapp-account.md`)
- File path: `articles/<collection-folder>/<filename>.md`

### Language & tone:
- All articles must be bilingual: English first, then Hebrew after the `---` separator
- Write Hebrew naturally — conversational, not translated-sounding. Match the style of existing articles.
- Write for the end user (ambassador or campaign admin), not a developer

### Quality bar for new articles:
- Write complete, useful articles — not placeholders
- Include step-by-step instructions where relevant
- Mention prerequisites (e.g., "you'll need a WhatsApp Business account before starting")
- Cover the full user flow from start to finish
- If the feature has both an admin setup step AND an ambassador usage step, cover both

### When to do nothing:
- If the PR is a backend-only change with no user-visible impact, return an empty array
- If the PR only fixes a bug with no behavior change the user would notice, return an empty array

---

Respond with a JSON object with two keys:
{{
  "summary": "A 3-5 line summary for the commit message explaining WHAT documentation changed and WHY (based on the app PR). First line: what the app PR does. Remaining lines: what doc changes were made and the reasoning. Written for a human reviewer.",
  "changes": [
    {{
      "file": "articles/folder/filename.md",
      "is_new": true,
      "reason": "one-line explanation of why this article is being created or updated",
      "updated_content": "the complete file content including frontmatter"
    }}
  ]
}}

Set `"is_new": false` for updates to existing articles, `"is_new": true` for brand-new articles.

Return only the JSON object, no other text.
"""

    response = model.generate_content(prompt)
    text = response.text.strip()

    # Extract JSON object from response
    m = re.search(r'\{.*\}', text, re.DOTALL)
    if not m:
        return '', []
    result = json.loads(m.group(0), strict=False)
    return result.get('summary', ''), result.get('changes', [])

def apply_changes(changes):
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    known_dirs = ['articles/get-started', 'articles/campaign-management',
                  'articles/features', 'articles/collecting-donations', 'articles/uncategorized']
    for change in changes:
        filepath = os.path.join(repo_root, change['file'])
        dir_path = os.path.dirname(filepath)
        is_new = change.get('is_new', False)

        rel_dir = os.path.relpath(dir_path, repo_root)
        if rel_dir not in known_dirs:
            print(f"  Skipping unknown path: {change['file']}")
            continue

        action = "Creating" if is_new else "Updating"
        print(f"  {action}: {change['file']} — {change['reason']}")
        os.makedirs(dir_path, exist_ok=True)
        with open(filepath, 'w') as f:
            f.write(change['updated_content'])

def main():
    print(f"Processing PR #{PR_NUMBER} from {APP_REPO}...")
    pr_context = fetch_pr_context()
    print(f"  PR: {pr_context['title']}")

    articles = read_all_articles()
    print(f"  Articles: {len(articles)} files")

    summary, changes = ask_gemini(pr_context, articles)
    new_count = sum(1 for c in changes if c.get('is_new'))
    update_count = len(changes) - new_count
    print(f"  Gemini suggests {update_count} updates, {new_count} new articles")

    if changes:
        apply_changes(changes)
        # Write summary for the workflow to use in the commit message
        summary_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            '.commit-summary.txt'
        )
        with open(summary_path, 'w') as f:
            f.write(summary)
        print(f"  Commit summary written to .commit-summary.txt")
        print("Done — changes applied.")
    else:
        print("Done — no changes needed.")

if __name__ == '__main__':
    main()
