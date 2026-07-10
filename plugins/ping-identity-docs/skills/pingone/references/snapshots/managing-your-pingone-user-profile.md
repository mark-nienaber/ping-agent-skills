---
title: "Administrators: Managing your PingOne environment"
description: Manage the MFA methods and change the password for your PingOne account from your profile page.
component: pingone
page_id: pingone:managing_your_pingone_user_profile:p1_signin
canonical_url: https://docs.pingidentity.com/pingone/managing_your_pingone_user_profile/p1_signin.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 18, 2024
section_ids:
  steps: Steps
  choose-from: Choose from:
  result: Result:
---

# Administrators: Managing your PingOne environment

You can manage the multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)* methods for your PingOne account, and change your password, if needed.

Each PingOne environment has three unique URLs:

| URL                        | Purpose                                                                                                                                  | Format                                                             |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| **Console URL**            | URL to sign on to the console for administrators of one or more environments, depending on the permissions defined for the admin's role. | https\://console.pingone.*\<geography>*/?env=*\<environmentID>*    |
| **Self-service Url**       | URL for PingOne end users to access self-service functionality, such as changing a password, pairing a device, or editing their profile. | https\://apps.pingone.*\<geography>*/*\<environmentID>*/myaccount/ |
| **Application Portal Url** | URL for end users to access their application portal.                                                                                    | https\://apps.pingone.*\<geography>*/*\<environmentID>*/myapps/    |

|   |                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can view these URLs from your PingOne account (**Settings > Environment Properties**). Make a note of them when you sign on for the first time. |

You can edit your profile, change your password, and manage your MFA *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)* methods. The appearance of your PingOne profile page is the same as the UI available to your end users, however, some of the options listed are not applicable to an administrator account, such as linked account consents.

## Steps

* To access your admin self-service profile, sign on to the PingOne admin console, and in the **Avatar** menu select one of the following.

  ### Choose from:

  * [Profile](p1_manageprofile.html): Go to the **Profile** tab to update your contact details including phone number, email address, and physical address.

    |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
    | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | To enable single sign-on (SSO) *(tooltip: \<div class="paragraph">&#xA;\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>&#xA;\</div>)* to Support from the **My Support Cases** option on the **Avatar** menu, you must have a verified email address in your profile. Your profile must also include you **First Name** and **Last Name**. |

  * [My MFA methods](p1_managingauthenticationmethods.html): Go to the **Authentication** tab to add one or more authentication method to securely sign on to your account or app.

    |   |                                                                                                                                                                                                                                                                  |
    | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | Access to the PingOne admin console requires at least one registered MFA method. Supported methods include email, authenticator app (TOTP), and FIDO2. Learn more in [Configuring administrator security](../settings/p1_configure_administrator_security.html). |

  * [Change password](p1_changepassword.html): Go to the **Change Password** tab to change your own password.

    |   |                                                                                                                    |
    | - | ------------------------------------------------------------------------------------------------------------------ |
    |   | You can also access your profile using the self-service URL or from the **Avatar** menu in the application portal. |

    ### Result:

    Your profile opens, showing the following tabs.

  ![Screen shot of a sample user profile, showing the tabs available. This example shows the MFA tab, and the authentication methods paired with the account.](_images/hke1639053406051.png)

---

---
title: "Administrators: Verifying your own email address"
description: Administrators must verify their own email address in PingOne.
component: pingone
page_id: pingone:managing_your_pingone_user_profile:p1_verify_email_admins
canonical_url: https://docs.pingidentity.com/pingone/managing_your_pingone_user_profile/p1_verify_email_admins.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 6, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
  result-2: Result
---

# Administrators: Verifying your own email address

Administrators must verify their own email address in PingOne.

## About this task

As an administrator, you should verify your email address using the PingOne admin console, but you can also use the PingOne self-service application to verify your email address. See [End users: Verifying an email address](p1_verify_email_self.html).

To verify your email address with the admin console:

## Steps

1. In PingOne, in the **Verify Email Address** popup window, click **Verify**.

   ![A screenshot of the Verify Email Address popup.](_images/elt1682626873582.png)

   ### Result:

   PingOne sends a verification code to your email address.

2. Go to the email from PingOne, copy the eight-digit verification code, and paste it into the **Verification Code** field.

   |   |                                                                                                    |
   | - | -------------------------------------------------------------------------------------------------- |
   |   | If you didn't receive an email or need to resend the code for any reason, click **Request Again**. |

## Result

Under your contact information, your email appears as verified. If you change your email address in your profile, you must verify it again.

![A screenshot of an email address with a checkmark and Verified.](_images/pts1682626417150.png)

---

---
title: Changing your password
description: If you forget your password or want to change it, you can change it yourself from your PingOne profile.
component: pingone
page_id: pingone:managing_your_pingone_user_profile:p1_changepassword
canonical_url: https://docs.pingidentity.com/pingone/managing_your_pingone_user_profile/p1_changepassword.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 8, 2024
section_ids:
  before-you-begin: Before you begin
  steps: Steps
---

# Changing your password

If you forget your password or want to change it, you can change it yourself from your PingOne profile.

## Before you begin

To access your PingOne user profile, you'll need your PingOne environment URL and password.

|   |                                                                                               |
| - | --------------------------------------------------------------------------------------------- |
|   | You can also access yourPingOne user profile using the self-service URL for your environment. |

## Steps

1. [Go to your profile](p1_signinselfservice.html), click the **My Profile** tab, and then click **Change Password**.

2. Enter the following information:

   * **Current password**

   * **New password**

   * **Confirm new password**

3. Click **Save**.

---

---
title: Completing the administrator account registration
description: When you receive an email indicating that you were added as an administrator in PingOne, verify your email address and update your password to complete the registration process.
component: pingone
page_id: pingone:managing_your_pingone_user_profile:p1_complete_admin_registration_process
canonical_url: https://docs.pingidentity.com/pingone/managing_your_pingone_user_profile/p1_complete_admin_registration_process.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 12, 2025
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  choose-from: Choose from:
  result: Result:
  result-2: Result:
  result-3: Result
---

# Completing the administrator account registration

When you receive an email indicating that you were added as an administrator in PingOne, verify your email address and update your password to complete the registration process.

## Before you begin

You should have received the following information from the PingOne administrator who added you as an administrator:

* Your PingOne user name if it is different from your email address.

* The **Console Login URL** for the environment that you are being added to.

* (Optional) A temporary password.

## Steps

1. Go to the PingOne console using the URL you received from the administrator.

2. Enter your PingOne **Username**.

3. Update your **Password**.

   ### Choose from:

   * If you received a temporary password, enter it and create a new password when prompted.

   * Click **Forgot Password**, enter your PingOne username on the **Password Reset** window, and click **Submit**.

     An email containing a recovery code is sent to the email address associated with your PingOne user account. Paste the code where indicated on the **Enter New Password** window. Create a new password and click **Save**.

     ### Result:

   You are signed on to the PingOne administrator console.

4. On **Verify Email Address**, click **Verify**.

   ### Result:

   A new verification code is sent to your email address.

5. Paste the verification code where indicated and click **Confirm**.

## Result

Your administrator account registration is complete.

---

---
title: Editing your profile
description: Access your PingOne user profile to update your contact details and location information.
component: pingone
page_id: pingone:managing_your_pingone_user_profile:p1_manageprofile
canonical_url: https://docs.pingidentity.com/pingone/managing_your_pingone_user_profile/p1_manageprofile.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 8, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  result: Result:
---

# Editing your profile

Access your PingOne user profile to update your contact details and location information.

## Before you begin

To access your PingOne profile, you'll need your PingOne self-service portal URL and password.

## About this task

The out-of-the-box profile includes the user's basic contact and location information by default.

## Steps

1. [Go to your profile](p1_signinselfservice.html), click the **My Profile** tab, and then click **Edit Profile**.

2. Edit your details.

   The fields that appear are defined by your organization and might include:

   * **Contact** details: Your name, phone number, mobile number, and email address.

     |   |                                                                                                                                                                                                                                          |
     | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | Administrators only: To enable SSO to Support from the **My Support Cases** option on the **Avatar** menu, you must have a verified email address in your profile. Your profile must also include your **First Name** and **Last Name**. |

   * **Location**: Your physical location, including street name, city, state, and zip code.

3. Click **Save**.

   ### Result:

   The PingOne directory is updated with your changes.

---

---
title: "End users: Accessing your PingOne profile"
description: Access the PingOne self-service portal to update your personal information, change your password, add MFA, view your accounts and sessions, and manage consents.
component: pingone
page_id: pingone:managing_your_pingone_user_profile:p1_signinselfservice
canonical_url: https://docs.pingidentity.com/pingone/managing_your_pingone_user_profile/p1_signinselfservice.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 8, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  result: Result:
---

# End users: Accessing your PingOne profile

Access the PingOne self-service portal to update your personal information, change your password, add MFA, view your accounts and sessions, and manage consents.

|   |                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If you haven't received the URL for the self-service portal, contact the support team or Help Desk of the company that provides you with this service before proceeding. |

## About this task

This section is intended for PingOne administrators to understand the options available to your end users when they access their self-service profile. Options available vary according to your configuration needs. The PingOne self-service portal enables your end users to:

* Edit their own profile

* Change their own profile

* Add or modify the mutli-factor authentication (MFA) methods from those defined by the admin

* View external accounts linked to their PingOne profile

* View any agreements for which they have given consent

|   |                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | You should create and maintain separate PingOne environments for your administrators and your end users so that you can maintain MFA configurations, branding, and policies appropriate to each environment. |

## Steps

* Access your profile based on your use case:

  ### Choose from:

  * To access your profile using the self-service URL: In a web browser, enter the self-service URL you received from your organization.

  * For customer use cases: In your application, tap the relevant option.

  * For workforce use cases: From the application portal, in the **Avatar** menu, select **Devices**.

    ### Result:

    Your profile opens, showing the following tabs.

  ![A screenshot showing the Profile page.](_images/hke1639053406051.png)

  * [My profile](p1_manageprofile.html): Update your contact details including phone number, email address, and physical address.

  * [Authentication](p1_managingauthenticationmethods.html): Add one or more authentication method to securely sign on to your account or app.

  * [Change password](p1_changepassword.html): Change your password yourself.

  * [Accounts & sessions](p1_manage_accts_sessions.html): View and manage linked accounts and open sessions.

  * [Consents](p1_manage_consents.html): View any agreements to which you have consented.

---

---
title: "End users: Verifying an email address"
description: In certain situations, end users might be able to verify their own email address using the PingOne self-service application.
component: pingone
page_id: pingone:managing_your_pingone_user_profile:p1_verify_email_self
canonical_url: https://docs.pingidentity.com/pingone/managing_your_pingone_user_profile/p1_verify_email_self.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 8, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result
---

# End users: Verifying an email address

In certain situations, end users might be able to verify their own email address using the PingOne self-service application.

|   |                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If you haven't received the URL for the self-service portal, contact the support team or Help Desk of the company that provides you with this service before proceeding. |

## About this task

You might be required to verify your email address if you change your email address in your profile or if your administrator requires it.

To verify an email address as an end user:

## Steps

1. Sign on to the PingOne self-service application.

   Learn more in [End users: Accessing your PingOne profile](p1_signinselfservice.html).

2. Do one of the following:

   * If you have already received the verification email, then paste or enter the verification code.

   * If you haven't received the verification email, click **Verify** in the yellow banner. Go to your email application and locate the email from PingOne. Copy the verification code, then paste or enter the code in the self-service application.

     |   |                                                                                                                                                                                   |
     | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If you don't see the yellow banner, you don't need to verify your email address.If you didn't receive an email, or need to resend the code for any reason, click **Resend code**. |

3. Click **Verify**.

## Result

Under your contact information, your email shows as verified. If you change your email address in your profile, you must verify it again.

---

---
title: Managing accounts and sessions
description: View and manage accounts linked to your profile, and any open sessions.
component: pingone
page_id: pingone:managing_your_pingone_user_profile:p1_manage_accts_sessions
canonical_url: https://docs.pingidentity.com/pingone/managing_your_pingone_user_profile/p1_manage_accts_sessions.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 8, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  result: Result:
  result-2: Result:
  result-3: Result:
  choose-from: Choose from:
---

# Managing accounts and sessions

View and manage accounts linked to your profile, and any open sessions.

## Before you begin

Administrators can allow their users to sign on using one or more external account profiles, such as Amazon, Facebook, or GitHub. When a user signs on using an external account, the account is listed in their profile, in the **Linked Account** section of the **Accounts & Sessions** tab. Users can view and manage their accounts from this tab.

## About this task

You can view and manage:

* Linked accounts: The first time you sign on using a linked account, such as Facebook or LinkedIn, the account is linked to your profile.

* Sessions: Each time you sign on to your account or app, a new session is created. If you sign on using more than one device, you create multiple active sessions. Active sessions are displayed in the **Accounts & Sessions** tab and show details of the browser, device type, and the date and time at which the session started.

![Accounts & Sessions tab, showing a linked account, with the Unlink Accounts button, and several active sessions, with the Sign Off button next to each session. The option to sign off all sessions appears at the bottom of the list of active sessions.](_images/wkl1639661043073.png)

|   |                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingOne retains a maximum of 10 sessions per user, including expired sessions. The oldest session is dropped when the maximum of 10 sessions is reached. |

## Steps

1. [Go to your profile](p1_signinselfservice.html) and click the **Accounts & Sessions** tab.

   ### Result:

   You see any linked accounts and any open sessions.

2. To unlink an external account:

   1. In the row next to the account that you want to unlink, click **Unlink Account**.

      ### Result:

      A confirmation window opens.

   2. Click **Unlink**.

      ### Result:

   The account is removed.

3. To sign off an open session:

   ### Choose from:

   * Sign off a single session: Next to the relevant entry, click **Sign Off**.

   * Sign off all sessions: Click** Sign off all sessions**.

---

---
title: Managing authentication methods
description: From your PingOne user profile you can add, rename, or delete one or more authentication methods. You can also define your default authentication method.
component: pingone
page_id: pingone:managing_your_pingone_user_profile:p1_managingauthenticationmethods
canonical_url: https://docs.pingidentity.com/pingone/managing_your_pingone_user_profile/p1_managingauthenticationmethods.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 8, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  result: Result:
  result-2: Result:
---

# Managing authentication methods

From your PingOne user profile you can add, rename, or delete one or more authentication methods. You can also define your default authentication method.

## Before you begin

To enable users with more than one authentication method to define a default multi-factor authentication (MFA) method, you must enable the `User-selected default` option. See [Configuring MFA settings](../authentication/p1_configure_mfa_settings.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | A user might not be able to use their default device for various reasons, such as:- If a user tries to authenticate from a mobile device and device authorization is allowed, then the device authorization occurs.

- If a user has a FIDO device with an active session, this device is used to authenticate the user even if the user changes their default device.

- If policy rules disallow the default device. |

## About this task

You can add different devices, such as a security key or phone biometrics for authentication. You can also add multiple authentication methods that use the same physical device. For example, you could set up MFA using SMS, voice, FIDO2 biometrics, and an authenticator app on a single mobile device. The devices available are defined by your organization.

|   |                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------- |
|   | You should add at least two MFA methods. The methods listed are defined by your administrator, and might vary between environments. |

## Steps

1. [Go to your profile](p1_signinselfservice.html), click the **My Profile** tab, and then click the **Authentication** tab.

2. Click **Add Method**.

   ### Result:

   The **Select Method** window opens, listing the methods available for you to add. The options available are defined by your organization.

   ![Select method window showing a list of available authentication methods.](_images/ywd1639664454341.png)

3. Select the authentication method you want to add and follow the instructions to pair that authentication method:

   * **PingID mobile app**: Download and open PingID mobile app and then scan the QR code. Accept all permissions and authenticate to complete the pairing process.

   * **Authenticator app**: Use a third-party authenticator application, such as Google Authenticator. Open the authenticator application and scan the QR code or enter the passcode. Click **Next**. Enter the passcode from the authenticator application to complete pairing.

   * **PingID desktop app**: Download and install PingID desktop app. Open the app and enter the pairing key that's displayed in MyAccount to complete pairing.

   * **Text message**: Use a text message (SMS) with a one-time passcode (OTP) to authenticate. Enter the phone number and click **Next**. Enter the OTP you received to complete pairing.

   * **Voice**: Receive a voice call with an OTP to authenticate. Enter the phone number and click **Next**. Enter the OTP you received to complete pairing.

   * **Email**: Use an email message with an OTP to authenticate. Enter an email address and click **Next**. Enter the OTP you received to complete pairing.

   * **FIDO2 biometrics**: Use FIDO2 biometrics on compatible devices to authenticate. On your device, sign on or enter your password to complete pairing.

   * **Passkeys**: Select your account and click **Continue**, or click **Save another way** and follow the prompts to choose where you want to save your passkey.

   * **YubiKey**: Insert the Yubikey, tap it, and then click **Verify**.

   * **Hardware Token**: Enter the serial number of the hardware token, as it appears on the back of your token and follow the steps to authenticate and complete pairing.

     ### Result:

     The authentication method is listed on the **Authentication** tab in the **Your Authentication Methods** section. Repeat this step to add another authentication method, if required.

   ![Authentication tab showing a list of the authentication methods paired with a user's account.](_images/myaccountmethods.png)

4. After adding an authentication method, you can optionally do the following:

   | Option                              | Description                                                                                                                                                                                                                                                                                                                                                                                 |
   | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Set a default authentication method | If you added more than one MFA method, to define your default method, click the hamburger menu next to the relevant MFA method and then click **Set As Default**.&#xA;&#xA;The authentication methods available depend on your company policy, and other factors, such as the browser you're using, so your default authentication method might not always be available for authentication. |
   | Rename an authentication method     | Click the hamburger menu next to the authentication method you want to set as default, and then click **Edit Name**. Enter a meaningful name for the authentication method, and select the checkmark. Names of up to 100 characters are supported.                                                                                                                                          |
   | Remove an authentication method     | Click the hamburger menu next to the authentication method you want to remove, and then click **Remove**.&#xA;&#xA;Ensure that you leave at least one authentication method. If you remove all authentication methods, you might lock yourself out of the application.                                                                                                                      |

---

---
title: Managing consents
description: View or revoke any terms of service agreements that you consented to when accessing your account.
component: pingone
page_id: pingone:managing_your_pingone_user_profile:p1_manage_consents
canonical_url: https://docs.pingidentity.com/pingone/managing_your_pingone_user_profile/p1_manage_consents.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 10, 2023
section_ids:
  steps: Steps
  result: Result:
---

# Managing consents

View or revoke any terms of service agreements that you consented to when accessing your account.

On the **Consent** tab, you can view all the agreements that you've consented to. Agreements can include terms and conditions, as well as permissions for an application. For example, you might allow an application to access your profile or email address.

## Steps

1. Go to your profile. See [End users: Accessing your PingOne profile](p1_signinselfservice.html).

2. Click the **Consent** tab.

   ### Result:

   You see a list of all agreements for which you've given your consent.

3. Do one or more of the following:

   * To view details of the agreement, click the **Eye** icon (![dan1639660327115](_images/dan1639660327115.png)) next to an entry.

   * To revoke an agreement that you have already consented to, click the trash can icon. In the confirmation message, click **Revoke Access**.

---

---
title: Managing your PingOne user profile
description: The PingOne self-service portal enables administrators and end users to manage their profile without contacting customer service.
component: pingone
page_id: pingone:managing_your_pingone_user_profile:p1_self_service_start
canonical_url: https://docs.pingidentity.com/pingone/managing_your_pingone_user_profile/p1_self_service_start.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 9, 2023
---

# Managing your PingOne user profile

The PingOne self-service portal enables administrators and end users to manage their profile without contacting customer service.

|   |                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you're **not** a PingOne administrator and are encountering an issue while trying to verify your email address, please contact the support team or Help Desk of the company that provided you with this service. |

This section is intended to introduce the functions available for the out-of-the-box PingOne user profile page and is intended for the following audiences:

* PingOne administrators: Learn how to manage your own account.

* PingOne administrators managing PingOne end users: Understand how your users can make use of the self-service options and use this guide as a basis for creating a guide for your own end users.

![Screenshot showing the profile page](_images/hke1639053406051.png)

The options displayed in the PingOne user profile are identical for both administrators and end users, but they can be implemented differently to fit your use cases.

From the PingOne self-service page, users can:

* Update their profile

* Add or remove authentication methods

* Change their password

* View linked accounts, sessions, and consents

Administrators can view the same tabs on the profile page. Some options might not be relevant when managing their own account, such as linked profiles and consents.

|   |                                                                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | You should create and maintain separate PingOne environments for your administrators and your end users so that you can maintain multi-factor authentication (MFA) configurations, branding, and policies appropriate to each environment. |