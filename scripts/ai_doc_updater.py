#!/usr/bin/env python3
"""
Called by the AI doc updater workflow.
1. Fetches PR diff + description from the app repo (namlisa/namlisa_app)
2. Reads all article markdown files
3. Asks Claude Haiku which articles need updating and what the changes should be
4. Applies the changes to the markdown files
"""

import os, sys, json, glob, subprocess
import requests
import anthropic

GH_TOKEN = os.environ['GH_TOKEN']
PR_NUMBER = os.environ['PR_NUMBER']
APP_REPO = os.environ.get('APP_REPO', 'namlisa/namlisa_app')
ANTHROPIC_API_KEY = os.environ['ANTHROPIC_API_KEY']

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

def ask_haiku(pr_context, articles):
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    article_list = '\n'.join([
        f"- {path}: {content[:100].replace(chr(10),' ')}..."
        for path, content in articles.items()
    ])

    full_articles = '\n\n'.join([
        f"=== {path} ===\n{content}"
        for path, content in articles.items()
    ])

    prompt = f"""You are a documentation assistant. A pull request was just merged into the FundGen Ambassador App codebase.

PR Title: {pr_context['title']}

PR Description:
{pr_context['body']}

Code diff (truncated):
{pr_context['diff']}

Below are all the current help center articles. Your job is to identify which articles (if any) are now outdated or incomplete due to the PR changes, and propose specific edits.

Current articles:
{full_articles}

Respond with a JSON array. Each element:
{{
  "file": "articles/folder/filename.md",
  "reason": "one-line explanation of why this article needs updating",
  "updated_content": "the complete new file content (including frontmatter)"
}}

Return an empty array [] if no articles need updating.
Only include articles that genuinely need changes — don't make up changes.
Keep the frontmatter intact. Only modify the Markdown body content.
"""

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=8192,
        messages=[{"role": "user", "content": prompt}],
    )

    text = response.content[0].text.strip()
    # Extract JSON from response
    m = __import__('re').search(r'\[.*\]', text, __import__('re').DOTALL)
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

    changes = ask_haiku(pr_context, articles)
    print(f"  Haiku suggests {len(changes)} changes")

    if changes:
        apply_changes(changes)
        print("Done — changes applied.")
    else:
        print("Done — no changes needed.")

if __name__ == '__main__':
    main()
