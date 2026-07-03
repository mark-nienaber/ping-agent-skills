---
title: Configure direct Salesforce sign on using PingOne (SP-initiated login) plus SLO
description: You must first enable identity provider (IdP)-initiated sign-on.
component: configuration_guides
page_id: configuration_guides:salesforce:config_signon_slo_salesforce_p1
canonical_url: https://docs.pingidentity.com/configuration_guides/salesforce/config_signon_slo_salesforce_p1.html
revdate: May 15, 2024
section_ids:
  before-you-begin: Before you begin
  enable-pingone-authentication-in-salesforce: Enable PingOne authentication in Salesforce
  test-the-pingone-sp-initiated-sso-integration: Test the PingOne SP-initiated SSO integration
---

# Configure direct Salesforce sign on using PingOne (SP-initiated login) plus SLO

## Before you begin

* You must first enable identity provider (IdP)-initiated sign-on.

## Enable PingOne authentication in Salesforce

1. Sign on to your Salesforce domain as an administrator.

2. Click the **Gear** icon, then go to **Setup → Company Settings → My Domain**.

   ![Screen capture of the Salesforce Settings menu with the My Domain tab highlighted.](_images/icd1619220366566.png)

3. Make a note of your domain name, for example, `https://your-company.my.salesforce.com`

4. In the **Authentication Configuration** section, click **Edit**.

   ![Screen capture of the Salesforce Authentication Configuration page with the Edit button highlighted in red.](_images/kka1619220392349.png)

5. In the **Authentication Service** list, select **PingOne**. Click **Save**.

   ![Screen capture of the Salesforce Authentication Configuration fields with the Save button and the Authentication Service pingone check box highlighted in red](_images/uci1619220428580.png)

   |   |                                                                       |
   | - | --------------------------------------------------------------------- |
   |   | This entry was created as a result of the IdP-initiated sign-on task. |

   Configuration is complete.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Salesforce will now redirect to PingOne for authentication of all new sessions. You should also select the **Login Form** check box during the testing phase in case of authentication issues.Testers will be offered the option of the standard Salesforce login form or PingOne authentication.After you've successfully tested authentication, you can clear the **Login Form** check box so that authentication automatically defaults to PingOne. |

## Test the PingOne SP-initiated SSO integration

1. Go to your Salesforce domain.

   |   |                                                                                                                                                                                                                                                                 |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If the **Login Form** check box is still selected, the Salesforce sign-on screen still displays, and you're offered a choice of Salesforce sign on or PingOne sign, select PingOne.If you've cleared the **Login Form** check box, you're not offered a choice. |

2. When you are redirected to PingOne, enter your PingOne username and password.

   After successful authentication, you're redirected back to Salesforce.

   ![Screen capture of the Salesforce domain home page.](_images/isr1619220460753.png)
