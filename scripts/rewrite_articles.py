#!/usr/bin/env python3
"""
One-shot Gemini 2.5 Flash rewrite of all help center articles.

Fixes:
- Terminology: Global Leads → Potential Donors, Spoke → Contacted, No Answer → No reply to contact, etc.
- Per-article issues: broken links, copy-paste errors, outdated features, branding
- Rewrites Hebrew (primary) and English sections using current i18n strings as ground truth
- Preserves frontmatter, image/screenshot/video references unchanged
"""

import os, sys, glob, re, time
import google.generativeai as genai

GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '')
if not GEMINI_API_KEY:
    print("ERROR: GEMINI_API_KEY not set")
    sys.exit(1)

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash-preview-04-17")

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ──────────────────────────────────────────────
# Ground-truth terminology (from i18n + codebase)
# ──────────────────────────────────────────────

TERMINOLOGY = """
## Terminology mapping (OLD → CORRECT)

### English
- "Global Leads" → "Potential Donors"
- "Spoke" (as a contact status) → "Contacted"
- "No Answer" (as a contact status) → "No reply to contact"
- "Left Message" → "No reply to contact"  (same status, old label)
- "Conversation Script" / "Conversation Scripts" → "Call Scripts"
- "Smart Message Templates" → "Message Templates"
- "Ambassador App" (without "FundGen") → "FundGen Ambassador App"
- "Namlisa" (user-facing) → "FundGen" (platform) or "FundGen Ambassador App" (the app)
- "Admin Interface" URL: https://admin.givingl.ink/dashboard  (keep as-is, do not change)

### Hebrew
- "לידים גלובליים" → "תורמים פוטנציאליים"
- "אנשי קשר גלובליים" → "תורמים פוטנציאליים"
- "דיברתי" (status) → "יצרתי קשר"
- "לא ענה" (status) → "לא ענה לפנייה"
- "תסריט שיחה" / "תסריטי שיחה" → "תסריטי שיחה" (Call Scripts)
- "תבניות הודעה חכמות" → "תבניות הודעות" (Message Templates)
- "אפליקציית השגריר" → "אפליקציית FundGen Ambassador"
- "Namlisa" (user-facing) → "FundGen"

## Current contact status labels (from app i18n — use exactly)

English:
- Contacted
- No reply to contact
- Promised to donate
- Donated
- Not interested
- Wrong contact details
- Contact later
- Maybe donate in the future
- Donated by other
- Thanked

Hebrew:
- יצרתי קשר
- לא ענה לפנייה
- התחייב לתרום
- תרם
- לא מעוניין
- פרטי קשר שגויים
- ליצור קשר מאוחר יותר
- אולי יתרום בעתיד
- נתרם על ידי אחר
- נשלחה תודה

## Current scheduled message types (from app i18n — use exactly)

English: Donation Trigger, Campaign Milestone, Hot Streak, Goal Milestone,
First Donation, Recurring Highlight, Leaderboard, Donation Stats,
Morning Kickoff, Final Countdown

Hebrew: טריגר תרומה, אבן דרך לקמפיין, רצף חם, אבן דרך ליעד,
תרומה ראשונה, הדגשת תרומה חוזרת, לוח מובילים, סטטיסטיקת תרומות,
בוקר טוב, ספירה לאחור

## Notification categories (from app i18n)
English: Instant Notifications, Scheduled Summary Messages, Timed Notifications
Hebrew: התראות מיידיות, הודעות סיכום מתוזמנות, התראות בזמן קבוע

## Section navigation for "Call Scripts" feature
- Admin interface → Messages → Call Scripts  (EN)
- ממשק ניהול → הודעות → תסריטי שיחה  (HE)

## Section navigation for "Message Templates" feature
- Admin interface → Messages → Message Templates  (EN)
- ממשק ניהול → הודעות → תבניות הודעות  (HE)

## "Potential Donors" navigation
- Admin interface → Contacts → Potential Donors  (EN)
- ממשק ניהול → אנשי קשר → תורמים פוטנציאליים  (HE)
"""

# ──────────────────────────────────────────────
# Per-article issue notes (keyed by filename)
# ──────────────────────────────────────────────

ARTICLE_NOTES = {
    "our-recommended-method-for-campaign-success.md": """
- Replace all old status names with current ones from the terminology mapping above.
- Replace "Global Leads" / "לידים הגלובליים" with "Potential Donors" / "תורמים פוטנציאליים" everywhere.
- Remove empty bullet points and empty headings (lines that are just "## " with no text, or "- " with no text).
- The English section has several empty bullets and a heading "## " with no text — remove them.
- Keep the overall structure (4 steps + closing) intact.
""",
    "יצירת-חשבון.md": """
- Replace "Ambassador App" with "FundGen Ambassador App" everywhere in both languages.
- Replace "Namlisa" (user-facing) with "FundGen" or "FundGen Ambassador App" as appropriate.
""",
    "הורדת-האפליקציה.md": """
- Replace "Ambassador App" with "FundGen Ambassador App" everywhere in both languages.
- Replace "Namlisa" (user-facing) with "FundGen" or "FundGen Ambassador App" as appropriate.
""",
    "סקירה-לוח-בקרה-של-הקמפיין-דשבורד.md": """
- Verify section/feature names match the current admin sidebar. The main sections are:
  Contacts (אנשי קשר), Donations (תרומות), Messages (הודעות), Team (צוות), Settings (הגדרות).
- Update any outdated section names you encounter.
""",
    "מילון-מונחים.md": """
- Remove broken GitHub links in "מאמרים קשורים" at the bottom — delete that section entirely.
- Update the terminology table:
  - "לידים גלובליים" → "תורמים פוטנציאליים" with updated definition "אנשי קשר שמנהל הקמפיין העלה לבסיס הנתונים"
  - Remove "דיברתי" / "לא ענה" from the status table — replace with the full current status list
    from the terminology mapping above (all 10 statuses).
  - Add missing statuses: "פרטי קשר שגויים", "אולי יתרום בעתיד", "נתרם על ידי אחר", "נשלחה תודה".
- Update branding: "Namlisa" → "FundGen".
- Article is Hebrew-only (no EN section after ---) — keep it that way.
""",
    "scheduled-messages.md": """
- The article currently only describes 2 message types: Donation Trigger and Campaign Update.
  The app now has ~10 types. Rewrite the "Types of Scheduled Messages" section to cover all current types:
  Donation Trigger, Campaign Milestone, Hot Streak, Goal Milestone, First Donation,
  Recurring Highlight, Leaderboard, Donation Stats, Morning Kickoff, Final Countdown.
- For each type, give a one-sentence description (use the descriptions from the terminology mapping above).
- The three notification categories are: Instant Notifications, Scheduled Summary Messages, Timed Notifications.
  Mention this grouping where appropriate.
- Keep navigation steps intact but verify: Messages → Scheduled Messages (admin interface).
""",
    "connecting-and-configuring-the-campaign-bot.md": """
- Verify the alert/notification type names match the current app. Use terminology from the mapping above.
- Replace any "Namlisa" branding with "FundGen".
""",
    "team-leader-permissions-and-team-assignment.md": """
- There is a copy-paste error: a step about "campaign ambassadors list" appears to be repeated.
  Find and remove the duplicate step.
- Verify that icon descriptions match the current UI.
""",
    "granting-admin-permissions.md": """
- Fix broken Hebrew URL if it has a trailing dash (e.g., "https://admin.givingl.ink/dashboard-" → remove the dash).
- The article mentions "three icons" but only explains one. Either explain all three icons or
  rewrite to accurately describe what icons/buttons are shown.
""",
    "smart-message-templates.md": """
- Rename the article title (both EN and HE, and frontmatter title fields) to "Message Templates" / "תבניות הודעות".
- Update navigation path if it says something other than Messages → Message Templates.
- Replace "Smart Message Templates" / "תבניות הודעה חכמות" throughout with the new names.
""",
    "conversation-script.md": """
- Rename the article title (both EN and HE, and frontmatter title fields) to "Call Scripts" / "תסריטי שיחה".
- Update navigation path to Messages → Call Scripts.
- Replace "Conversation Script" / "תסריט שיחה" throughout with the new names.
""",
    "uploading-global-leads-lists.md": """
- Rename article title (EN and HE frontmatter) to "Uploading Potential Donors Lists" / "העלאת רשימות תורמים פוטנציאליים".
- Replace all occurrences of "Global Leads" / "לידים גלובליים" with "Potential Donors" / "תורמים פוטנציאליים".
- There is a copy-paste error in step 5 (the English section) — step 5 currently says
  "The page will display the list of campaign ambassadors" which is wrong context for this step.
  Step 5 should describe what the user sees after scrolling (the upload area/button), not the ambassador list.
  Rewrite step 5 to say something like: "The upload section will appear. Click the Document Upload icon."
- Fix similar inconsistency in the Hebrew step 5 if present.
""",
    "ניהול-הרשאות-משתמשים.md": """
- Fix typo: "ממק ניהול" → "ממשק ניהול".
- Verify the role hierarchy matches the app: Admin > Team Leader > Ambassador.
  If the article describes different roles, update accordingly.
""",
    "the-ignore-option-in-the-contacts-screen.md": """
- Clarify the distinction: the action button is called "Ignore" (התעלם), but the resulting
  list/filter label is "Hidden" (מוסתר). The article should explain both terms so users
  understand why they see "Hidden" in the UI after performing "Ignore".
""",
    "import-contacts-from-global-leads.md": """
- Rename article title (EN and HE frontmatter) to "Import Contacts from Potential Donors" /
  "ייבוא אנשי קשר מרשימת תורמים פוטנציאליים".
- Replace "Global Leads" / "לידים גלובליים" everywhere with "Potential Donors" / "תורמים פוטנציאליים".
""",
    "שימוש-בתבניות-הודעות.md": """
- Fix typo: "מתו האופציות" → "מתוך האופציות".
""",
    "ביצוע-שיחה-ותיעודה.md": """
- Replace old status names in the table with current ones from the terminology mapping.
- Verify the XP value for logging a call is still correct (check if article mentions a specific XP amount).
""",
    "עדכון-סטטוס-איש-קשר.md": """
- Verify column/field names match current UI. The status picker shows the contact statuses
  from the terminology mapping above — make sure the article lists them correctly.
""",
    "how-to-view-anonymous-donations-in-the-app.md": """
- Verify the tab name: check whether the article says "My Goal" tab — this should match
  the current i18n label (the tab in the app is "My Goal" / "היעד שלי").
""",
    "צפייה-בהתקדמות-התרומות-שלך.md": """
- Fix inconsistency: if the article uses "Your Goal" in one place and "My Goal" in another,
  standardize to "My Goal" / "היעד שלי" (matching app i18n).
""",
    "צפייה-בלוח-המובילים.md": """
- Verify the "Achievements" navigation item exists in the current app nav bar.
  If the article refers to a nav item called "Achievements" that no longer exists,
  update to the correct navigation path (the Leaderboard is accessed from the Me/profile section).
""",
}

# ──────────────────────────────────────────────
# Prompt template
# ──────────────────────────────────────────────

SYSTEM_PROMPT = """You are a technical writer for FundGen Ambassador App (a fundraising campaign management mobile app).
Your task is to rewrite a help center article to fix outdated terminology, branding, and content issues.

CRITICAL RULES:
1. Preserve the YAML frontmatter block (between --- delimiters at the top) EXACTLY as-is,
   EXCEPT you may update title_en and title_he fields if the article notes say to rename the article.
2. Preserve ALL image references (![...](url)), screenshot references, and video links EXACTLY.
3. The article body has two sections separated by a line containing only "---":
   - First section: English content
   - Second section: Hebrew content (some articles are Hebrew-only, with no English section)
   Keep this structure. Rewrite both sections applying the fixes.
4. Hebrew is the PRIMARY language — the Hebrew section should be complete and well-written.
   The English section should also be complete and accurate.
5. Do NOT invent features, screens, or navigation paths that aren't mentioned in the current terminology.
6. Do NOT add commentary, notes, or explanations outside the article content.
7. Output ONLY the complete updated article content, starting with the --- frontmatter delimiter.
8. For "FundGen Ambassador App" in Hebrew, use "אפליקציית FundGen Ambassador".
9. URLs to the admin interface (https://admin.givingl.ink/dashboard) must be preserved exactly.
10. Keep Markdown formatting (headings, lists, bold, tables) intact and well-formed.
"""

def build_prompt(filename, content, notes):
    return f"""
{SYSTEM_PROMPT}

## Current terminology and i18n ground truth:

{TERMINOLOGY}

## Per-article fixes for this specific article ({filename}):

{notes if notes else "Apply only the global terminology fixes. No specific structural changes needed for this article."}

## Article to rewrite:

{content}

Now output the complete rewritten article:
""".strip()


def parse_frontmatter(content):
    """Returns (frontmatter_text, body_text) where frontmatter_text includes the --- delimiters."""
    if not content.startswith('---'):
        return '', content
    end = content.find('\n---\n', 4)
    if end == -1:
        return '', content
    return content[:end+5], content[end+5:]


def rewrite_article(filepath):
    rel = os.path.relpath(filepath, REPO_ROOT)
    filename = os.path.basename(filepath)
    notes = ARTICLE_NOTES.get(filename, '')

    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()

    print(f"  → Rewriting: {rel}")

    prompt = build_prompt(filename, original, notes)

    try:
        response = model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                temperature=0.1,  # low temp = more deterministic, less hallucination
                max_output_tokens=8192,
            ),
        )
        result = response.text.strip()
    except Exception as e:
        print(f"    ERROR calling Gemini: {e}")
        return False

    # Strip any markdown code block wrapping Gemini may add
    if result.startswith('```'):
        result = re.sub(r'^```(?:markdown|md)?\n', '', result)
        result = re.sub(r'\n```$', '', result.rstrip())

    # Sanity check: result must start with --- (frontmatter preserved)
    if not result.startswith('---'):
        print(f"    WARNING: Output doesn't start with frontmatter delimiter — skipping {filename}")
        print(f"    Output starts with: {result[:100]!r}")
        return False

    # Verify frontmatter block is still present
    fm_orig, _ = parse_frontmatter(original)
    fm_new, _ = parse_frontmatter(result)
    if not fm_new:
        print(f"    WARNING: Frontmatter missing in output — skipping {filename}")
        return False

    # Preserve intercom_article_id from original (must never change)
    orig_id_match = re.search(r'intercom_article_id:\s*"?([^"\n]+)"?', fm_orig)
    new_id_match = re.search(r'intercom_article_id:\s*"?([^"\n]+)"?', fm_new)
    if orig_id_match and new_id_match and orig_id_match.group(1) != new_id_match.group(1):
        print(f"    WARNING: intercom_article_id changed — restoring original ID")
        result = result.replace(
            f'intercom_article_id: "{new_id_match.group(1)}"',
            f'intercom_article_id: "{orig_id_match.group(1)}"',
        )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(result + '\n')

    print(f"    ✅ Done ({len(result)} chars)")
    return True


def main():
    files = sorted(glob.glob(f"{REPO_ROOT}/articles/**/*.md", recursive=True))
    print(f"Found {len(files)} articles to rewrite.\n")

    success = 0
    failed = []

    for filepath in files:
        ok = rewrite_article(filepath)
        if ok:
            success += 1
        else:
            failed.append(os.path.relpath(filepath, REPO_ROOT))
        # Rate-limit: Gemini Flash has generous limits but be polite
        time.sleep(2)

    print(f"\n{'='*50}")
    print(f"Completed: {success}/{len(files)} articles rewritten successfully.")
    if failed:
        print(f"Failed ({len(failed)}):")
        for f in failed:
            print(f"  - {f}")
        sys.exit(1)


if __name__ == '__main__':
    main()
