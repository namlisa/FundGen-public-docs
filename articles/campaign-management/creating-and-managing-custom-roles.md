---
intercom_article_id: ""
title_en: "Creating and Managing Custom Roles"
title_he: "יצירה וניהול תפקידים מותאמים אישית"
state: "published"
collection: "Campaign Management"
collection_he: "ניהול הקמפיין"
---

# Creating and Managing Custom Roles

FundGen's new Custom Roles feature provides campaign administrators with granular control over user access. Instead of broad 'Admin' or 'Team Leader' toggles, you can now define specific roles (e.g., 'Marketing Manager', 'Data Analyst') with precise `read`, `write`, or `no access` permissions for different modules within the FundGen admin interface.

## Why Use Custom Roles?

-   **Granular Control:** Assign exact permissions needed for each team member, minimizing security risks.
-   **Streamlined Workflows:** Ensure users only see and interact with the modules relevant to their responsibilities.
-   **Flexibility:** Adapt roles to your campaign's unique organizational structure.
-   **Scalability:** Easily manage permissions as your team grows or roles change.

## Prerequisites

- You must be logged in as a user with **Admin Permissions** or a custom role that grants `write` access to `User Role Management`.

## Step-by-Step: Creating a New Custom Role

1.  **Access the Admin Interface:** Log in to [https://admin.givingl.ink/dashboard](https://admin.givingl.ink/dashboard).
2.  **Navigate to Custom Roles:** In the main sidebar, go to **Settings** and click on **Custom Roles**.
3.  **Add a New Role:** Click the **'+ Add New Role'** button or a similar icon to create a new role.
4.  **Define Role Details:**
    *   **Role Name:** Enter a descriptive name (e.g., "Campaign Marketer", "Donor Relations Lead").
    *   **Description (Optional):** Add a brief explanation of the role's purpose.
5.  **Configure Granular Permissions:** You will see a list of modules or areas within the FundGen admin interface. For each module, select the appropriate access level:
    *   **No Access:** Users assigned this role cannot see or interact with this module.
    *   **Read Access:** Users can view information within this module but cannot make changes.
    *   **Write Access:** Users can view, create, edit, and delete information within this module.

    *Example Modules and Permissions:*

    | **Module**            | **Read Access** | **Write Access** | **No Access** |
    | :-------------------- | :-------------- | :--------------- | :------------ |
    | Campaign Settings     | ✅              | ✅               | ⬜            |
    | Ambassador Management | ✅              | ✅               | ⬜            |
    | Data Access & Reports | ✅              | ⬜               | ⬜            |
    | Communication Tools   | ✅              | ✅               | ⬜            |
    | User Role Management  | ✅              | ⬜               | ⬜            |

6.  **Save the Role:** After configuring all desired permissions, click **'Save Role'**.

## Managing Existing Custom Roles

From the **Custom Roles** screen, you can:

-   **Edit:** Click the 'Edit' icon (pencil) next to a role to modify its name, description, or permissions.
-   **Duplicate:** Create a copy of an existing role as a starting point for a new one.
-   **Delete:** Remove a custom role. Note that you cannot delete a role that is currently assigned to users. You must reassign users first.

Once your custom roles are defined, you can proceed to [Assign Custom Roles to Users](/articles/campaign-management/assigning-custom-roles-to-users).

---

# יצירה וניהול תפקידים מותאמים אישית

תכונת התפקידים המותאמים אישית החדשה של FundGen מעניקה למנהלי קמפיין שליטה מדויקת על גישת המשתמשים. במקום מתגים כלליים של 'מנהל מערכת' או 'ראש צוות', תוכלו כעת להגדיר תפקידים ספציפיים (לדוגמה: 'מנהל שיווק', 'אנליסט נתונים') עם הרשאות מדויקות של `קריאה`, `כתיבה`, או `ללא גישה` עבור מודולים שונים בתוך ממשק הניהול של FundGen.

## למה להשתמש בתפקידים מותאמים אישית?

-   **שליטה מדויקת:** הקצו הרשאות מדויקות הנדרשות לכל חבר צוות, תוך מזעור סיכוני אבטחה.
-   **זרימות עבודה יעילות:** ודאו שמשתמשים רואים ומתקשרים רק עם המודולים הרלוונטיים לתחומי האחריות שלהם.
-   **גמישות:** התאימו תפקידים למבנה הארגוני הייחודי של הקמפיין שלכם.
-   **סקלאביליות:** נהלו בקלות הרשאות ככל שהצוות שלכם גדל או שתפקידים משתנים.

## תנאים מקדימים

- עליך להיות מחובר כמשתמש עם **הרשאת מנהל** או תפקיד מותאם אישית המעניק גישת `כתיבה` ל`ניהול הרשאות משתמשים`.

## שלב אחר שלב: יצירת תפקיד מותאם אישית חדש

1.  **גישה לממשק הניהול:** היכנסו ל- [https://admin.givingl.ink/dashboard](https://admin.givingl.ink/dashboard).
2.  **ניווט לתפקידים מותאמים אישית:** בסרגל הצד הראשי, עבור אל **הגדרות** ולחץ על **תפקידים מותאמים אישית**.
3.  **הוספת תפקיד חדש:** לחץ על כפתור **'+ הוסף תפקיד חדש'** או על אייקון דומה כדי ליצור תפקיד חדש.
4.  **הגדרת פרטי התפקיד:**
    *   **שם תפקיד:** הזן שם תיאורי (לדוגמה: "משווק קמפיין", "מוביל קשרי תורמים").
    *   **תיאור (אופציונלי):** הוסף הסבר קצר על מטרת התפקיד.
5.  **הגדרת הרשאות מדויקות:** תראה רשימה של מודולים או אזורים בתוך ממשק הניהול של FundGen. עבור כל מודול, בחר את רמת הגישה המתאימה:
    *   **ללא גישה:** משתמשים שהוקצו להם תפקיד זה לא יוכלו לראות או לתקשר עם מודול זה.
    *   **גישת קריאה:** משתמשים יכולים לצפות במידע בתוך מודול זה אך אינם יכולים לבצע שינויים.
    *   **גישת כתיבה:** משתמשים יכולים לצפות, ליצור, לערוך ולמחוק מידע בתוך מודול זה.

    *דוגמאות למודולים והרשאות:*

    | **מודול**                | **גישת קריאה** | **גישת כתיבה** | **ללא גישה** |
    | :----------------------- | :-------------- | :-------------- | :------------ |
    | הגדרות קמפיין            | ✅              | ✅               | ⬜            |
    | ניהול שגרירים            | ✅              | ✅               | ⬜            |
    | גישה לנתונים ודוחות     | ✅              | ⬜               | ⬜            |
    | כלי תקשורת               | ✅              | ✅               | ⬜            |
    | ניהול הרשאות משתמשים | ✅              | ⬜               | ⬜            |

6.  **שמירת התפקיד:** לאחר הגדרת כל ההרשאות הרצויות, לחץ על **'שמור תפקיד'**.

## ניהול תפקידים מותאמים אישית קיימים

ממסך **תפקידים מותאמים אישית**, תוכלו:

-   **עריכה:** לחצו על אייקון 'ערוך' (עיפרון) ליד תפקיד כדי לשנות את שמו, תיאורו או הרשאותיו.
-   **שכפול:** צרו עותק של תפקיד קיים כנקודת התחלה עבור תפקיד חדש.
-   **מחיקה:** הסירו תפקיד מותאם אישית. שימו לב שלא ניתן למחוק תפקיד המוקצה כרגע למשתמשים. עליכם להקצות מחדש את המשתמשים תחילה.

לאחר שתפקידיכם המותאמים אישית מוגדרים, תוכלו להמשיך ל[הקצאת תפקידים מותאמים אישית למשתמשים](/articles/campaign-management/assigning-custom-roles-to-users).
