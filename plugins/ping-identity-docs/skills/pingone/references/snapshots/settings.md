---
title: (Customer Only) Configuring WhatsApp as a sender
description: To use WhatsApp as a strong authentication (MFA) method, you'll need to add your WhatsApp business account as a sender.
component: pingone
page_id: pingone:settings:p1-using-a-custom-whatsapp-sender-account
canonical_url: https://docs.pingidentity.com/pingone/settings/p1-using-a-custom-whatsapp-sender-account.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  next-steps: Next steps
---

# (Customer Only) Configuring WhatsApp as a sender

To use [WhatsApp](../strong_authentication_mfa/p1-strong-auth_whatsapp.html) as a strong authentication (MFA) method, you'll need to add your WhatsApp business account as a sender.

## Before you begin

Before connecting your WhatsApp business account as a sender in PingOne, configure a WhatsApp business account in the Meta business and developer portals as follows:

1. If you don't have one already, create a WhatsApp business account.

2. Create a WhatsApp application that includes at least one sender number.

3. In the WhatsApp business account, create a **System User** with the **Admin** System user role.

4. Assign the **System User** to the WhatsApp application.

5. Generate an access token, and then add the following scopes to the access token:

   * `business_management`

   * `manage_app_solution`

   * `whatsapp_business_management`

   * `whatsapp_business_messaging`

6. Get the **App ID** and **App Secret**. You can find the **App ID** and **App Secret** in the Developer portal **App settings**.

7. In the WhatsApp business account, create one or more WhatsApp message templates. The message templates must be of category **Authenticator**. The message template can be used to send notifications in PingOne.

|   |                                                                             |
| - | --------------------------------------------------------------------------- |
|   | You can only add a single WhatsApp sender account to a PingOne environment. |

## Steps

To configure a custom WhatsApp sender:

1. Go to **Settings > Senders**.

2. In the **Sender Type** field, select **Messaging**, and then click **Next**.

3. In the **Provider Configuration** window, enter the following information, and then click **Verify**:

   * **WhatsApp for Business ID**: Enter your organization's WhatsApp business account ID.

   * **User Access Token**: Enter the user access token that was generated from your WhatsApp business account.

   * **App ID**: Enter the app ID of the relevant WhatsApp application.

   * **App Secret**: Enter the app secret for the WhatsApp application in the format `<appid|apptoken>`.

     ![Sender window. The Messaging tab shows the text To use your own sender account for WhatsApp messages, enter the relevant details and verify your account. Several fields are shown.](../strong_authentication_mfa/_images/p1-whatsapp-sender-messaging-tab.png)

     PingOne verifies the WhatsApp business account details and displays the available WhatsApp sender numbers.

     |   |                                                                                                          |
     | - | -------------------------------------------------------------------------------------------------------- |
     |   | Validation can take several minutes. Don't close the validation window until the validation is complete. |

     Result

     The WhatsApp account is saved.

     ## Next steps

     Learn more about the additional steps required to add WhatsApp as an authentication method in [(Customer Only) Configuring WhatsApp authentication](../strong_authentication_mfa/p1-strong-auth_whatsapp.html)
