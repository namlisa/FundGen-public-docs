---
intercom_article_id: "14286238"
title_en: "Scheduling Calls to Ambassadors"
title_he: "תזמון שיחות לשגרירים"
state: "published"
collection: "Campaign Management"
collection_he: "ניהול הקמפיין"
---

# Scheduling Calls to Ambassadors

The 'Scheduled Calls' feature allows campaign administrators to set up automated reminders for ambassadors to make important phone calls. This is a powerful tool for coordinating outreach, reminding ambassadors about follow-ups, or prompting them to contact specific donors or potential leads at key moments.

This feature works by sending a pre-configured WhatsApp message to the designated ambassadors at a scheduled time, reminding them to perform a call.

## How it Works

1.  **Admin Schedules:** A campaign admin sets up a "Scheduled Call" message in the FundGen admin interface.
2.  **Bot Delivers Reminder:** At the scheduled time, the campaign bot (connected to WhatsApp) sends a reminder message to the selected ambassadors.
3.  **Ambassador Takes Action:** The ambassador receives the WhatsApp message, which prompts them to make the call.

## Setting Up a Scheduled Call

**Prerequisites:**
*   You must be logged in as a user with **Admin Permissions**.
*   The Campaign Bot must be connected to WhatsApp. (See: [Connecting and Configuring the Campaign Bot](articles/campaign-management/connecting-and-configuring-the-campaign-bot.md))

**Steps:**

1.  **Access Scheduled Messages:**
    *   Log in to the FundGen admin interface: [https://admin.givingl.ink/dashboard](https://admin.givingl.ink/dashboard)
    *   In the main sidebar, navigate to the **Messages** category.
    *   Click on **Scheduled Messages**.

2.  **Add a New Scheduled Message:**
    *   Click the **➕ (Add)** button in the center of the screen.
    *   The "Add Scheduled Message" window will open.

3.  **Select "Scheduled Call" Type:**
    *   From the list of message types, select **"Scheduled Call (to Ambassadors)"**.

4.  **Configure Call Details:**
    *   **Message Content:** Write the WhatsApp message that the bot will send to ambassadors. This message should clearly instruct them on which call to make (e.g., "Reminder to call all contacts in 'Promised to Donate' status," or "Call Mrs. Goldstein regarding her pledge."). You can use dynamic variables if available (e.g., `##AMBASSADOR_NAME##`).
    *   **Target Audience:** Choose who will receive this call reminder:
        *   **All Ambassadors:** Sends the reminder to every active ambassador in the campaign.
        *   **Specific Teams:** Sends to all ambassadors belonging to selected teams.
        *   **Specific Ambassadors:** Allows you to manually select individual ambassadors.
    *   **Schedule:** Define when the reminder should be sent:
        *   **Date and Time:** Set a specific date and time for a one-time reminder.
        *   **Recurrence:** Configure the message to repeat daily, weekly, or on specific days of the week.
        *   **Operating Hours:** Set a time window within which the message can be sent on the scheduled days.

5.  **Save the Scheduled Call:**
    *   Review all settings.
    *   Click **Save** to activate the scheduled call reminder.

## Ambassador Experience

When a Scheduled Call reminder is active, ambassadors will receive a WhatsApp message from the connected campaign bot at the designated time. This message will contain the instructions set by the admin, prompting them to initiate the relevant call. Ambassadors should then log their call activity in the FundGen Ambassador App as usual.

---

# תזמון שיחות לשגרירים

תכונת 'שיחות מתוזמנות' מאפשרת למנהלי קמפיין להגדיר תזכורות אוטומטיות לשגרירים לבצע שיחות טלפון חשובות. זהו כלי עוצמתי לתיאום מאמצי פנייה, תזכורות לשגרירים לגבי מעקבים, או זימון אותם ליצור קשר עם תורמים ספציפיים או לידים פוטנציאליים ברגעים קריטיים.

תכונה זו פועלת על ידי שליחת הודעת וואטסאפ מוגדרת מראש לשגרירים הייעודיים בזמן מתוזמן, המזכירה להם לבצע שיחה.

## איך זה עובד

1.  **מנהל המערכת מתזמן:** מנהל קמפיין מגדיר הודעת "שיחה מתוזמנת" בממשק הניהול של FundGen.
2.  **הבוט שולח תזכורת:** בזמן המתוזמן, בוט הקמפיין (המחובר לוואטסאפ) שולח הודעת תזכורת לשגרירים הנבחרים.
3.  **השגריר פועל:** השגריר מקבל את הודעת הוואטסאפ, המנחה אותו לבצע את השיחה.

## הגדרת שיחה מתוזמנת

**תנאים מקדימים:**
*   עליך להיות מחובר עם **משתמש בעל הרשאת מנהל**.
*   בוט הקמפיין חייב להיות מחובר לוואטסאפ. (ראה: [חיבור והגדרת בוט לקבוצת קמפיין](articles/campaign-management/connecting-and-configuring-the-campaign-bot.md))

**שלבים:**

1.  **כניסה למסך הודעות מתוזמנות:**
    *   היכנס לממשק הניהול של FundGen: [https://admin.givingl.ink/dashboard](https://admin.givingl.ink/dashboard)
    *   בסרגל הכלים הראשי בצד ימין, נווט לקטגוריית **הודעות**.
    *   לחץ על **הודעות מתוזמנות**.

2.  **הוספת הודעה מתוזמנת חדשה:**
    *   במרכז המסך יש ללחוץ על כפתור **➕ (הוספה)**.
    *   תיפתח חלונית **"הוסף הודעה מתוזמנת"**.

3.  **בחר בסוג "שיחה מתוזמנת":**
    *   מתוך רשימת סוגי ההודעות, בחר ב**"שיחה מתוזמנת (לשגרירים)"**.

4.  **הגדר את פרטי השיחה:**
    *   **תוכן ההודעה:** כתוב את הודעת הוואטסאפ שהבוט ישלח לשגרירים. הודעה זו צריכה להנחות אותם בבירור איזו שיחה לבצע (לדוגמה: "תזכורת להתקשר לכל אנשי הקשר בסטטוס 'התחייבו לתרום'", או "התקשר לגברת גולדשטיין לגבי ההתחייבות שלה"). ניתן להשתמש במשתנים דינמיים אם זמינים (לדוגמה: `##AMBASSADOR_NAME##`).
    *   **קהל יעד:** בחר מי יקבל תזכורת שיחה זו:
        *   **כל השגרירים:** שולח את התזכורת לכל שגריר פעיל בקמפיין.
        *   **צוותים ספציפיים:** שולח לכל השגרירים השייכים לצוותים שנבחרו.
        *   **שגרירים ספציפיים:** מאפשר לבחור ידנית שגרירים בודדים.
    *   **תזמון:** הגדר מתי יש לשלוח את התזכורת:
        *   **תאריך ושעה:** קבע תאריך ושעה ספציפיים לתזכורת חד-פעמית.
        *   **חזרה:** הגדר את ההודעה לחזור על בסיס יומי, שבועי, או בימים ספציפיים בשבוע.
        *   **שעות פעילות:** קבע חלון זמן שבתוכו ניתן לשלוח את ההודעה בימים המתוזמנים.

5.  **שמור את השיחה המתוזמנת:**
    *   בדוק את כל ההגדרות.
    *   לחץ **שמור** כדי להפעיל את תזכורת השיחה המתוזמנת.

## חווית השגריר

כאשר תזכורת שיחה מתוזמנת פעילה, שגרירים יקבלו הודעת וואטסאפ מבוט הקמפיין המחובר בזמן הייעודי. הודעה זו תכלול את ההוראות שהוגדרו על ידי מנהל המערכת, ותנחה אותם ליזום את השיחה הרלוונטית. לאחר מכן, השגרירים צריכים לתעד את פעילות השיחה שלהם באפליקציית FundGen Ambassador כרגיל.
