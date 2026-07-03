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
