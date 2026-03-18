---
intercom_article_id: "13688464"
title_en: "How to Connect Your Stripe Account for Tap to Pay"
state: "published"
---

# How to Connect Your Stripe Account for Tap to Pay

## What is this key?

The Secret Key is a secure token that authorizes our application to communicate with Stripe.
- 

**Format:** It always begins with `sk_live_` followed by a string of random characters.
- 

**Purpose:** It acts as a bridge, allowing our app to send payment commands to your Stripe dashboard.

## Is it safe to share this key?

**Yes.** We understand that your financial security is paramount. Here is how we handle this connection:
- 

**Payment Processing Only:** We use this key strictly to **write** transaction data (i.e., to process a sale).
- 

**No Withdrawal Access:** Our system creates a "one-way" channel. We **cannot** withdraw funds from your bank account, access your banking credentials, or change your payout settings.
- 

**Secure Storage:** The key is encrypted in our system.

---

## Step-by-Step Guide: How to Retrieve Your Key

Follow these steps to locate the correct key in your Stripe Dashboard:

**1. Log in to Stripe** Go to [dashboard.stripe.com](https://dashboard.stripe.com/login) and sign in.

**2. Ensure you are in "Live Mode"** This is the most important step. We need your production key, not a test key.
- 

Look at the toggle switch in the top-right corner of the dashboard.
- 

Make sure **"Test Mode"** is turned **OFF** (the toggle should be grey, not orange).

**3. Go to the Developers Section** Click on the **"Developers"** button located in the top-right area of the dashboard.

**4. Open API Keys** In the secondary menu (usually on the left side or a tab bar), select **"API keys"**.

**5. Locate the "Secret key"**
- 

Look for the section labeled **Standard keys**.
- 

Find the row named **Secret key**.
- 

You will see a token hidden by asterisks (e.g., `sk_live_...`).

**6. Reveal and Copy**
- 

Click the **"Reveal live key"** button (Stripe may ask for your password or 2FA).
- 

**Verify:** Ensure the key starts with **`sk_live_`**.
- 

Click the key to copy it to your clipboard.

**7. Send to Support** Once you have copied the key, please email it directly to our support team to complete the setup:
- 

**Email:** [support@fundgen.ai](mailto:support@fundgen.ai)
- 

**Subject:** Stripe Key Integration - [Your Company Name]

Our team will securely link your account and notify you once Tap to Pay is active.
