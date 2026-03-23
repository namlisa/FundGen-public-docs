```markdown
---
intercom_article_id: ""
title_en: "Sending WhatsApp Messages as an Ambassador (Admin Feature)"
title_he: "שליחת הודעות וואטסאפ בשם שגריר (תכונת מנהל)"
state: "published"
collection: "Campaign Management"
collection_he: "ניהול הקמפיין"
---

# Sending WhatsApp Messages as an Ambassador (Admin Feature)

Campaign administrators can now send personalized WhatsApp messages to contacts on behalf of specific ambassadors. This feature allows for centralized communication while maintaining the personal touch of the ambassador.

## Who is this for?

*   Campaign Managers
*   Team Leaders with Admin permissions

## Prerequisites

*   You must be logged in as a user with **Admin Permissions**.
*   The target ambassador's personal WhatsApp account must be connected to the campaign bot. Refer to [Connecting Ambassador WhatsApp Accounts to the Campaign Bot](articles/campaign-management/connecting-and-configuring-the-campaign-bot.md) for instructions.
*   The contact you wish to message must be assigned to the ambassador.

## Steps to Send a WhatsApp Message on Behalf of an Ambassador

1.  **Log in to the Admin Interface:**
    Access the FundGen admin interface via computer or mobile: [https://admin.givingl.ink/dashboard](https://admin.givingl.ink/dashboard)

2.  **Navigate to Ambassador Management:**
    *   In the main toolbar, select the **Contacts** menu.
    *   From the menu, select the **Manage Ambassadors** tab.

3.  **Select the Ambassador:**
    *   Find the ambassador whose behalf you want to send the message from.
    *   Click on their profile to view their details.

4.  **Access the "Send WhatsApp Message" Feature:**
    *   On the ambassador's profile page, locate and click the **"Send WhatsApp Message"** button.

5.  **Select a Contact:**
    *   A list of contacts assigned to this ambassador will appear.
    *   Select the specific contact you wish to send the message to.

6.  **Compose or Select a Message:**
    *   You can choose from existing [Message Templates](articles/campaign-management/smart-message-templates.md) or compose a custom message.
    *   Ensure any dynamic variables (like `##NAME##` or `##LINK##`) are correctly populated. The ambassador's personal donation link (`##LINK##`) will be automatically used.

7.  **Send the Message:**
    *   Review the message and click **"Send"**.
    *   The message will be sent using the selected ambassador's WhatsApp identity through the connected campaign bot.

## What the Ambassador Sees

*   The message will appear in the ambassador's activity feed as if they sent it themselves.
*   For internal visibility, the activity will be tagged with "Admin Sent". This tag is only visible to the ambassador in their activity log and does not appear to the recipient.

## Important Considerations

*   **Personalization:** Although sent by an admin, the message appears as if coming directly from the ambassador, maintaining a personal touch with the donor.
*   **Compliance:** This feature leverages the existing WhatsApp bot connection, ensuring messages are sent in compliance with WhatsApp's policies via connected personal accounts.
*   **Activity Logging:** All messages sent this way are logged against the ambassador's activity, contributing to their overall campaign statistics and XP, fostering accurate reporting.
---

# שליחת הודעות וואטסאפ בשם שגריר (תכונת מנהל)

מנהלי קמפיין יכולים כעת לשלוח הודעות וואטסאפ מותאמות אישית לאנשי קשר בשם שגרירים ספציפיים. תכונה זו מאפשרת תקשורת מרוכזת תוך שמירה על הנגיעה האישית של השגריר.

## למי מיועד המדריך?

*   מנהלי קמפיין
*   ראשי צוות בעלי הרשאות מנהל

## תנאים מקדימים

*   עליך להיות מחובר עם **משתמש בעל הרשאת ניהול**.
*   חשבון הוואטסאפ האישי של השגריר המיועד חייב להיות מחובר לבוט הקמפיין. עיין ב[חיבור חשבונות וואטסאפ של שגרירים לבוט הקמפיין](articles/campaign-management/connecting-and-configuring-the-campaign-bot.md) להוראות.
*   איש הקשר שאליו ברצונך לשלוח הודעה חייב להיות משויך לשגריר.

## שלבים לשליחת הודעת וואטסאפ בשם שגריר

1.  **התחבר לממשק הניהול:**
    יש להיכנס לממשק הניהול של FundGen באמצעות מחשב או נייד: [https://admin.givingl.ink/dashboard](https://admin.givingl.ink/dashboard)

2.  **נווט לניהול שגרירים:**
    *   בסרגל הכלים הראשי, בחר בתפריט **אנשי קשר**.
    *   מתוך התפריט, בחר בלשונית **ניהול שגרירים**.

3.  **בחר את השגריר:**
    *   אתר את השגריר שדרכו ברצונך לשלוח את ההודעה.
    *   לחץ על הפרופיל שלו כדי לצפות בפרטיו.

4.  **גש לתכונת "שלח הודעת וואטסאפ":**
    *   בעמוד הפרופיל של השגריר, אתר ולחץ על כפתור **"שלח הודעת וואטסאפ"**.

5.  **בחר איש קשר:**
    *   רשימת אנשי הקשר המשויכים לשגריר זה תופיע.
    *   בחר את איש הקשר הספציפי שאליו ברצונך לשלוח את ההודעה.

6.  **ערוך או בחר הודעה:**
    *   באפשרותך לבחור מבין [תבניות הודעות](articles/campaign-management/smart-message-templates.md) קיימות או לערוך הודעה מותאמת אישית.
    *   ודא שכל המשתנים הדינמיים (כמו `##NAME##` או `##LINK##`) מאוכלסים כהלכה. קישור התרומה האישי של השגריר (`##LINK##`) ישמש אוטומטית.

7.  **שלח את ההודעה:**
    *   עיין בהודעה ולחץ על **"שלח"**.
    *   ההודעה תישלח באמצעות זהות הוואטסאפ של השגריר הנבחר דרך בוט הקמפיין המחובר.

## מה השגריר רואה

*   ההודעה תופיע בפיד הפעילות של השגריר כאילו הוא שלח אותה בעצמו.
*   לצורך נראות פנימית, הפעילות תסומן כ-"נשלח על ידי מנהל". תג זה גלוי רק לשגריר ביומן הפעילות שלו ואינו מופיע לנמען.

## שיקולים חשובים

*   **התאמה אישית:** למרות שנשלחה על ידי מנהל מערכת, ההודעה נראית כאילו הגיעה ישירות מהשגריר, ושומרת על נגיעה אישית עם התורם.
*   **תאימות:** תכונה זו ממנפת את חיבור בוט הוואטסאפ הקיים, ומבטיחה שהודעות נשלחות בהתאם למדיניות וואטסאפ באמצעות חשבונות אישיים מחוברים.
*   **רישום פעילות:** כל ההודעות הנשלחות בדרך זו נרשמות כפעילות של השגריר, ותורמות לסטטיסטיקות הקמפיין הכוללות שלו ולנקודות ה-XP, מה שמבטיח דיווח מדויק.
```