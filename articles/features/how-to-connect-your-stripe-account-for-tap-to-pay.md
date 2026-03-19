---
intercom_article_id: "13688464"
title_en: "How to Connect Your Stripe Account for Tap to Pay"
state: "published"
collection: "Features"
collection_he: "פונקציות"
---

# How to Connect Your Stripe Account for Tap to Pay

## What is this key?

The Secret Key is a secure token that authorizes our application to communicate with Stripe.

- **Format:** It always begins with `sk_live_` followed by a string of random characters.
- **Purpose:** It acts as a bridge, allowing our app to send payment commands to your Stripe dashboard.

## Is it safe to share this key?

**Yes.** We understand that your financial security is paramount. Here is how we handle this connection:

- **Payment Processing Only:** We use this key strictly to **write** transaction data (i.e., to process a sale).
- **No Withdrawal Access:** Our system creates a "one-way" channel. We **cannot** withdraw funds from your bank account, access your banking credentials, or change your payout settings.
- **Secure Storage:** The key is encrypted in our system.

---

## Step-by-Step Guide: How to Retrieve Your Key

Follow these steps to locate the correct key in your Stripe Dashboard:

**1. Log in to Stripe** Go to [dashboard.stripe.com](https://dashboard.stripe.com/login) and sign in.

**2. Ensure you are in "Live Mode"** This is the most important step. We need your production key, not a test key.

- Look at the toggle switch in the top-right corner of the dashboard.
- Make sure **"Test Mode"** is turned **OFF** (the toggle should be grey, not orange).

**3. Go to the Developers Section** Click on the **"Developers"** button located in the top-right area of the dashboard.

**4. Open API Keys** In the secondary menu (usually on the left side or a tab bar), select **"API keys"**.

**5. Locate the "Secret key"**

- Look for the section labeled **Standard keys**.
- Find the row named **Secret key**.
- You will see a token hidden by asterisks (e.g., `sk_live_...`).

**6. Reveal and Copy**

- Click the **"Reveal live key"** button (Stripe may ask for your password or 2FA).
- **Verify:** Ensure the key starts with **`sk_live_`**.
- Click the key to copy it to your clipboard.

**7. Send to Support** Once you have copied the key, please email it directly to our support team to complete the setup:

- **Email:** [support@fundgen.ai](mailto:support@fundgen.ai)
- **Subject:** Stripe Key Integration - [Your Company Name]

Our team will securely link your account and notify you once Tap to Pay is active.

## Using Tap to Pay as an Ambassador

Once your campaign admin has connected the Stripe account, you can start accepting in-person contactless donations directly through the FundGen Ambassador App.

**Steps to process an in-person donation:**

1.  From the app, navigate to the contact's profile whom you wish to collect a donation from.
2.  Tap the **+** icon (Add Activity) and select **Log Donation**.
3.  Enter the donation amount and any relevant notes.
4.  Instead of just logging it, you will now see an option to **"Tap to Pay"** or **"Process with Tap to Pay"**. Tap this option.
5.  Follow the on-screen prompts to have the donor tap their contactless card or mobile wallet on your phone.
6.  Once the payment is successful, the donation will be immediately logged in the system under the contact's profile and count towards your goal.
7.  The contact's status will automatically update to "Donated".

**Benefits:**
*   **Instant Processing:** Donations are processed and recorded in real-time.
*   **Convenience:** Accept payments anywhere, anytime, without external card readers.
*   **Seamless Tracking:** All TTP donations are automatically linked to the contact and your personal fundraising goal.

---

# כיצד לחבר את חשבון ה-Stripe שלך לתשלום בנגיעה (Tap to Pay)

## מהו מפתח זה?

המפתח הסודי (Secret Key) הוא אסימון מאובטח המאפשר לאפליקציה שלנו לתקשר עם Stripe.

- **פורמט:** הוא תמיד מתחיל ב-`sk_live_` ואחריו מחרוזת של תווים אקראיים.
- **מטרה:** הוא משמש כגשר, המאפשר לאפליקציה שלנו לשלוח פקודות תשלום ללוח המחוונים של Stripe שלך.

## האם בטוח לשתף מפתח זה?

**כן.** אנו מבינים שהביטחון הפיננסי שלך הוא בעל חשיבות עליונה. כך אנו מטפלים בחיבור זה:

- **עיבוד תשלומים בלבד:** אנו משתמשים במפתח זה אך ורק כדי **לכתוב** נתוני עסקה (כלומר, לעבד מכירה).
- **ללא גישת משיכה:** המערכת שלנו יוצרת ערוץ "חד כיווני". אנו **איננו יכולים** למשוך כספים מחשבון הבנק שלך, לגשת לפרטי הבנק שלך, או לשנות את הגדרות התשלום שלך.
- **אחסון מאובטח:** המפתח מוצפן במערכת שלנו.

---

## מדריך שלב אחר שלב: כיצד לאחזר את המפתח שלך

בצע את השלבים הבאים כדי לאתר את המפתח הנכון בלוח המחוונים של Stripe שלך:

**1. היכנס ל-Stripe** עבור אל [dashboard.stripe.com](https://dashboard.stripe.com/login) והיכנס.

**2. ודא שאתה במצב "Live Mode"** זהו השלב החשוב ביותר. אנו זקוקים למפתח הייצור שלך, לא למפתח בדיקה.

- הסתכל על מתג ההפעלה/כיבוי בפינה הימנית העליונה של לוח המחוונים.
- ודא ש**"Test Mode"** כבוי (המתג צריך להיות אפור, לא כתום).

**3. עבור למקטע המפתחים** לחץ על כפתור **"Developers"** הממוקם באזור הימני העליון של לוח המחוונים.

**4. פתח מפתחות API** בתפריט המשני (בדרך כלל בצד שמאל או בסרגל כרטיסיות), בחר **"API keys"**.

**5. אתר את "המפתח הסודי"**

- חפש את המקטע שכותרתו **Standard keys**.
- מצא את השורה בשם **Secret key**.
- תראה אסימון מוסתר על ידי כוכביות (לדוגמה, `sk_live_...`).

**6. חשוף והעתק**

- לחץ על כפתור **"Reveal live key"** (Stripe עשויה לבקש את הסיסמה שלך או אימות דו-שלבי).
- **וודא:** ודא שהמפתח מתחיל ב-**`sk_live_`**.
- לחץ על המפתח כדי להעתיק אותו ללוח.

**7. שלח לתמיכה** לאחר שהעתקת את המפתח, אנא שלח אותו ישירות לצוות התמיכה שלנו כדי להשלים את ההגדרה:

- **דוא"ל:** [support@fundgen.ai](mailto:support@fundgen.ai)
- **נושא:** שילוב מפתח Stripe - [שם החברה שלך]

הצוות שלנו יקשר את חשבונך בצורה מאובטחת ויודיע לך ברגע שתשלום בנגיעה (Tap to Pay) יהיה פעיל.

## שימוש ב-Tap to Pay כשגריר

לאחר שמנהל הקמפיין שלכם חיבר את חשבון ה-Stripe, תוכלו להתחיל לקבל תרומות ללא מגע באופן אישי ישירות דרך אפליקציית FundGen Ambassador.

**שלבים לביצוע תרומה אישית:**

1.  באפליקציה, נווטו לפרופיל איש הקשר שממנו תרצו לגבות תרומה.
2.  לחצו על אייקון ה-**+** (הוסף פעילות) ובחרו **"תיעוד תרומה"**.
3.  הזינו את סכום התרומה וכל הערה רלוונטית.
4.  במקום רק לתעד את התרומה, כעת תראו אפשרות **"הקש לתשלום"** או **"בצע תשלום בנגיעה"**. לחצו על אפשרות זו.
5.  עקבו אחר ההנחיות שעל המסך כדי שהתורם יקיש את כרטיס האשראי ללא מגע או הארנק הדיגיטלי שלו על הטלפון שלכם.
6.  לאחר שהתשלום הושלם בהצלחה, התרומה תתועד באופן מיידי במערכת תחת פרופיל איש הקשר ותיספר ליעד שלכם.
7.  סטטוס איש הקשר יתעדכן אוטומטית ל"תרם".

**יתרונות:**
*   **עיבוד מיידי:** תרומות מעובדות ומתועדות בזמן אמת.
*   **נוחות:** קבלו תשלומים בכל מקום ובכל זמן, ללא צורך בקוראי כרטיסים חיצוניים.
*   **מעקב חלק:** כל התרומות שבוצעו באמצעות TTP מקושרות אוטומטית לאיש הקשר וליעד הגיוס האישי שלכם.