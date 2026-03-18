#!/usr/bin/env python3
"""
Called by the AI doc updater workflow.
1. Fetches PR diff + description from the app repo (namlisa/namlisa_app)
2. Reads all article markdown files
3. Asks Gemini Flash which articles need updating and what the changes should be
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

    diff = requests.get(
        f"https://api.github.com/repos/{APP_REPO}/pulls/{PR_NUMBER}",
        headers={**GH_HEADERS, "Accept": "application/vnd.github.v3.diff"},
    ).text

    # Truncate very large diffs
    if len(diff) > 20000:
        diff = diff[:20000] + "\n\n[diff truncated]"

    return {
        'title': pr.get('title', ''),
        'body': pr.get('body', '') or '',
        'diff': diff,
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
    model = genai.GenerativeModel("gemini-2.5-flash")

    full_articles = '\n\n'.join([
        f"=== {path} ===\n{content}"
        for path, content in articles.items()
    ])

    prompt = f"""You are a documentation assistant for the FundGen Ambassador App — a fundraising campaign management tool used by ambassadors in Hebrew and English.

A pull request was just merged into the app codebase. Your job is to identify which help center articles (if any) are now outdated or incomplete due to these changes, and propose specific edits.

PR Title: {pr_context['title']}

PR Description:
{pr_context['body']}

Code diff (truncated):
{pr_context['diff']}

Current help center articles:
{full_articles}

Rules:
- Articles are bilingual (Hebrew + English). Update BOTH language sections when a change is needed.
- Keep the YAML frontmatter exactly as-is (do not change intercom_article_id, state, collection, etc.)
- Write Hebrew naturally — not translated-sounding. Match the existing tone and style.
- Only include articles that genuinely need changes. Do not invent or pad.
- If nothing changed that affects docs, return an empty array.

Respond with a JSON array. Each element:
{{
  "file": "articles/folder/filename.md",
  "reason": "one-line explanation of why this article needs updating",
  "updated_content": "the complete new file content (including frontmatter)"
}}

Return only the JSON array, no other text.
"""

    response = model.generate_content(prompt)
    text = response.text.strip()

    # Extract JSON array from response
    m = re.search(r'\[.*\]', text, re.DOTALL)
    if not m:
        return []
    return json.loads(m.group(0))

def apply_changes(changes):
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for change in changes:
        filepath = os.path.join(repo_root, change['file'])
        if not os.path.exists(os.path.dirname(filepath)):
            print(f"  Skipping unknown path: {change['file']}")
            continue
        print(f"  Updating: {change['file']} — {change['reason']}")
        with open(filepath, 'w') as f:
            f.write(change['updated_content'])

def main():
    print(f"Processing PR #{PR_NUMBER} from {APP_REPO}...")
    pr_context = fetch_pr_context()
    print(f"  PR: {pr_context['title']}")

    articles = read_all_articles()
    print(f"  Articles: {len(articles)} files")

    changes = ask_gemini(pr_context, articles)
    print(f"  Gemini suggests {len(changes)} changes")

    if changes:
        apply_changes(changes)
        print("Done — changes applied.")
    else:
        print("Done — no changes needed.")

if __name__ == '__main__':
    main()
