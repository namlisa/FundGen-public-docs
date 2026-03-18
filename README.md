# FundGen Public Docs

This repo is the source of truth for all [FundGen Ambassador App](https://fundgen.ai) help center articles.

Articles live as Markdown files in `articles/`. Changes merged to `main` are automatically synced to Intercom.

## Structure

```
articles/
├── get-started/           # "התחילו כאן" — first steps for new ambassadors
├── campaign-management/   # "ניהול הקמפיין" — admin/campaign setup
├── features/              # "פונקציות" — feature-specific guides
├── collecting-donations/  # "איסוף תרומות" — donation tracking
└── uncategorized/         # articles not yet assigned to a collection
```

## Article Format

Each `.md` file has YAML frontmatter:

```yaml
---
intercom_article_id: "12345678"
title_en: "Article Title"
title_he: "כותרת המאמר"
state: "published"       # published | draft
collection: "Features"
collection_he: "פונקציות"
---

# Article Title

English content here...

---

# כותרת המאמר

תוכן בעברית כאן...
```

- **English content** goes first, under the EN title.
- **Hebrew content** goes after `---`, under the HE title.
- If an article has only one language, omit the other section.

## How to Edit

1. Edit the `.md` file directly on GitHub or in a PR
2. Merge to `main`
3. The `sync-to-intercom.yml` workflow fires automatically and updates the live article

## How to Add a New Article

1. Create a new `.md` file in the right folder
2. Leave `intercom_article_id` blank — the sync script will create the article in Intercom and write back the ID
3. Open a PR, merge to `main`

## Local Setup

```bash
pip install requests pyyaml
export INTERCOM_API_KEY="your_key"
python scripts/sync.py --dry-run    # preview changes
python scripts/sync.py              # apply changes
```
