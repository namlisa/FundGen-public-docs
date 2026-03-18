#!/usr/bin/env python3
"""
Sync Markdown articles in articles/ to Intercom Help Center.
- Reads frontmatter for intercom_article_id, title, state
- Splits file on --- separator into EN and HE sections
- Updates existing articles; creates new ones and writes back the ID
- Dry-run mode: --dry-run
"""

import os, re, sys, json, glob, argparse
import requests

API_KEY = os.environ.get("INTERCOM_API_KEY", "")
BASE = "https://api.intercom.io"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Accept": "application/json",
    "Content-Type": "application/json",
}

COLLECTION_IDS = {
    "Get Started": "17522117",
    "Campaign Management": "17521491",
    "Features": "17521176",
    "Collecting Donations": "17521373",
}

def md_to_html(md):
    """Minimal Markdown → HTML (enough for Intercom)."""
    lines = md.split('\n')
    html_lines = []
    in_list = False
    list_type = None

    def close_list():
        nonlocal in_list, list_type
        if in_list:
            html_lines.append(f'</{list_type}>')
            in_list = False
            list_type = None

    for line in lines:
        # Headings — always close any open list first
        m = re.match(r'^(#{1,4})\s+(.*)', line)
        if m:
            close_list()
            level = len(m.group(1))
            html_lines.append(f'<h{level}>{m.group(2)}</h{level}>')
            continue

        # HR
        if re.match(r'^---+$', line.strip()):
            close_list()
            html_lines.append('<hr/>')
            continue

        # List items — skip empty bullet lines (just "- " with no text)
        m = re.match(r'^(\s*)[-*]\s+(.*)', line)
        if m:
            item_text = m.group(2).strip()
            if not item_text:
                continue  # skip empty list items
            if not in_list or list_type != 'ul':
                if in_list:
                    close_list()
                html_lines.append('<ul>')
                in_list = True
                list_type = 'ul'
            html_lines.append(f'<li>{inline_md(item_text)}</li>')
            continue

        m = re.match(r'^(\s*)\d+\.\s+(.*)', line)
        if m:
            item_text = m.group(2).strip()
            if not item_text:
                continue  # skip empty ordered list items
            if not in_list or list_type != 'ol':
                if in_list:
                    html_lines.append(f'</{list_type}>')
                html_lines.append('<ol>')
                in_list = True
                list_type = 'ol'
            html_lines.append(f'<li>{inline_md(item_text)}</li>')
            continue

        # Close list if needed
        if in_list and line.strip() != '':
            html_lines.append(f'</{list_type}>')
            in_list = False

        if line.strip() == '':
            continue

        html_lines.append(f'<p>{inline_md(line)}</p>')

    if in_list:
        html_lines.append(f'</{list_type}>')

    return '\n'.join(html_lines)

def inline_md(text):
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Italic
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    # Links
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    # Inline code
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    return text

def parse_frontmatter(content):
    """Returns (frontmatter_dict, body_text)."""
    if not content.startswith('---'):
        return {}, content
    end = content.find('\n---\n', 4)
    if end == -1:
        return {}, content
    fm_text = content[4:end]
    body = content[end+5:]
    fm = {}
    for line in fm_text.split('\n'):
        m = re.match(r'^(\w+):\s*"?(.+?)"?\s*$', line)
        if m:
            fm[m.group(1)] = m.group(2)
    return fm, body

def split_body(body):
    """Split body into EN and HE sections on '\\n---\\n'."""
    # Find the --- separator that's NOT a frontmatter delimiter
    parts = re.split(r'\n---\n', body, maxsplit=1)
    if len(parts) == 1:
        return body.strip(), ''
    return parts[0].strip(), parts[1].strip()

def extract_title_and_body(section):
    """Pull the leading # heading out as title, rest as body."""
    lines = section.split('\n')
    title = ''
    body_lines = []
    found_title = False
    for line in lines:
        if not found_title and re.match(r'^#\s+', line):
            title = re.sub(r'^#+\s+', '', line).strip()
            found_title = True
        else:
            body_lines.append(line)
    return title, '\n'.join(body_lines).strip()

def sync_article(filepath, dry_run=False):
    with open(filepath) as f:
        content = f.read()

    fm, body = parse_frontmatter(content)
    article_id = fm.get('intercom_article_id', '').strip('"')
    state = fm.get('state', 'published').strip('"')
    collection = fm.get('collection', '').strip('"')
    collection_id = COLLECTION_IDS.get(collection)

    en_section, he_section = split_body(body)
    title_en, body_en = extract_title_and_body(en_section)
    title_he, body_he = extract_title_and_body(he_section)

    # Build translated_content
    translated = {}
    if title_en or body_en:
        translated['en'] = {
            'title': title_en,
            'body': md_to_html(body_en),
            'author_id': None,
        }
    if title_he or body_he:
        translated['he'] = {
            'title': title_he,
            'body': md_to_html(body_he),
            'author_id': None,
        }

    # Determine default locale & title
    default_locale = 'he' if title_he else 'en'
    default_title = title_he if default_locale == 'he' else title_en

    payload = {
        'title': default_title,
        'state': state,
        'default_locale': default_locale,
        'translated_content': translated,
    }
    if collection_id:
        payload['parent_id'] = int(collection_id)
        payload['parent_type'] = 'collection'

    if dry_run:
        action = 'UPDATE' if article_id else 'CREATE'
        print(f"  [{action}] {filepath}")
        print(f"    title_en={title_en!r}  title_he={title_he!r}  state={state}")
        return

    if article_id:
        # Update
        r = requests.put(f"{BASE}/articles/{article_id}", headers=HEADERS, json=payload)
        if r.status_code == 200:
            print(f"  ✅ Updated [{article_id}] {title_en or title_he}")
        else:
            print(f"  ❌ Update failed [{article_id}]: {r.status_code} {r.text[:200]}")
    else:
        # Create
        r = requests.post(f"{BASE}/articles", headers=HEADERS, json=payload)
        if r.status_code == 200:
            new_id = r.json()['id']
            print(f"  ✅ Created [{new_id}] {title_en or title_he}")
            # Write back the ID to the file
            new_content = content.replace(
                'intercom_article_id: ""',
                f'intercom_article_id: "{new_id}"'
            )
            if new_content == content:
                # Try adding it after ---
                new_content = content.replace(
                    '---\n',
                    f'---\nintercom_article_id: "{new_id}"\n',
                    1
                )
            with open(filepath, 'w') as f:
                f.write(new_content)
        else:
            print(f"  ❌ Create failed: {r.status_code} {r.text[:200]}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--file', help='Sync a single file')
    args = parser.parse_args()

    if not API_KEY and not args.dry_run:
        print("ERROR: INTERCOM_API_KEY environment variable not set")
        sys.exit(1)

    if args.file:
        files = [args.file]
    else:
        repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        files = glob.glob(f"{repo_root}/articles/**/*.md", recursive=True)

    mode = "DRY RUN" if args.dry_run else "LIVE"
    print(f"Syncing {len(files)} articles [{mode}]...")
    for f in sorted(files):
        sync_article(f, dry_run=args.dry_run)
    print("Done.")

if __name__ == '__main__':
    main()
