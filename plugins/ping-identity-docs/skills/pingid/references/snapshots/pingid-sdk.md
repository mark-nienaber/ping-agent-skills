---
title: Automatic synchronization of PingID SDK with a PingFederate user directory
description: The PingID SDK Connector synchronizes user identities and their profile attributes from a configured datastore within PingFederate to PingID SDK.
component: pingid
page_id: pingid:pingid_sdk:pid_automatic_syn_of_pid_sdk_with_pf
canonical_url: http://docs.pingidentity.com/pingid/pingid_sdk/pid_automatic_syn_of_pid_sdk_with_pf.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 23, 2024
section_ids:
  the-pingid-sdk-connector-flow: The PingID SDK Connector flow:
---

# Automatic synchronization of PingID SDK with a PingFederate user directory

The PingID SDK Connector synchronizes user identities and their profile attributes from a configured datastore within PingFederate to PingID SDK.

Ping Identity offers a catalog of connectors that provide provisioning capabilities to SaaS providers. The connectors act as a mediator to handle transactions safely and securely. The PingID SDK Connector offers profile management solutions to multiple directory types, such as LDAP, Active Directory (AD), and PingDirectory.

The PingID SDK Connector:

* Includes support for user life cycle management that lets you create, update, disable, and delete users

* Includes configuration options for workflow capabilities, such as the ability to disable updates

![Diagram illustrating the flow between Active Directory, PingFederate and the PingID SDK Connector, and PingOne.](_images/qzj1564021075991.png)

## The PingID SDK Connector flow:

1. PingFederate polls the user directory for any changes to user records at regular intervals, configurable in PingFederate.

2. Returned records are stored within PingFederate's intermediary database and marked as requiring an update in PingID SDK (PingOne).

3. The connector pulls the marked record from the intermediary database and performs the necessary operation (Create, Get, Update, Delete) against the PingID SDK record. These changes are reflected in the PingOne admin portal.

To download the PingID SDK for PingFederate connector, go to [PingID Server SaaS Connectors](https://www.pingidentity.com/en/resources/downloads/pingfederate.html).

For more information on configuring the PingID SDK for PingFederate connector, see [PingFederate PingID SDK Connector Guide](https://support.pingidentity.com/s/document-item?bundleId=integrations\&topicId=zyw1565632179137.html).

---

---
title: Configuring a new PingID SDK app
description: Create and configure a new PingID SDK application in the admin web portal.
component: pingid
page_id: pingid:pingid_sdk:pid_sdk_config_new_app
canonical_url: http://docs.pingidentity.com/pingid/pingid_sdk/pid_sdk_config_new_app.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 23, 2023
section_ids:
  steps: Steps
  choose-from: Choose from:
---

# Configuring a new PingID SDK app

Create and configure a new PingID SDK application in the admin web portal.

## Steps

1. In the admin portal, go to **Applications → PingID SDK Applications**. ![Screen capture illustrating the PingID SDK Applications tab in the administrator web portal.](_images/uay1564020819206.png)

   If there are applications already defined for your organization, they are listed on this page.

2. To open the **Add PingID SDK Application** wizard, click **[icon: plus, set=fa]Add Application**.

3. Configure the **Basic Properties** fields: ![Screen capture illustrating the Basic Properties section of the Add PingID SDK Application window.](_images/cjb1564021070062.png)

   1. In the **Application Name** field, enter the application name.

      |   |                                                                                                                                                                                                                                    |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | The **Application Name** field is required, and each name must be unique. If the name is in use, an error message appears and the **Next** button is disabled.Whitespaces are permitted, except for the first and last characters. |

   2. To enter the **Application ID** (UUID) of a shared application that is already registered in another PingOne tenant, click **Link to existing application**.

      |   |                                                                                                                                                                                                                                                             |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Any **Application ID** can appear only once in an organization's list of registered PingID SDK applications.A link icon appears next to a linked application, both in the original organization and in the organization referencing the **Application ID**. |

   3. Click **Next**.

4. Configure the **Connect to your application** fields:

   ### Choose from:

   * On iOS: You can upload and associate separate certificate files for the Sandbox and for Production.

   * On Android: Both of the connection details fields, **Sender ID** and **Server Key**, can either be left blank or must both be filled.

     \+ image::div1569483765690.png\[alt="Screen capture illustrating the Connect To Your Application section of the Add PingID SDK Application window.",role="border-no-padding"]

     1. Click **Next**.

5. Configure the **Configure PingID** fields: ![Screen capture illustrating the Configure PingID section of the Add PingID SDK Application window.](_images/gqt1564021072318.png)

   The **Configure PingID** section lets you:

   * Access the **Configuration Edit** window directly.

   * Simplify the configuration process by allowing you to copy the configurations of an existing application. This feature is only available after at least one application has been configured.

     |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
     | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | * When there are more than 5 applications, a **Search** field appears. Entering part of an application's name in the **Search** field immediately shortens the returned list of apps to entries that contain the input search string.

     * If you choose an already existing application configuration, all of its configurations automatically apply to the new application.

     * Any of the configuration settings can be changed.

     * Updating a configuration setting in either the original application or the newly created application does not have any impact on the other application's configuration. |

     1. From the **Configuration** list, select a configuration or predefined application to copy its configuration.

     2. To navigate directly to the app's **Integration** and **Configuration** tabs or to view or change the configuration settings, click **Save & Edit Configuration**.

   For more information, see [Updating a PingID SDK app's configuration](pid_sdk_update_app_configuration.html).

   1. To save the app's integration and configuration settings as defined with the wizard and return to the**PingID SDK Applications** list, click **Done**.

6. Go to **Applications → PingID SDK Applications**.

7. To enable or disable an application, from the list of applications, click the toggle to the right of your application. ![Screen capture illustrating the PingID SDK Applications tab with applications toggled on and off.](_images/uay1564020819206.png)

---

---
title: Configuring a Syniverse account for PingID SDK
description: Ensure that you have available your Syniverse account Access Token. You can copy it as required from the Syniverse dashboard. You should also have set up one or more origination phone numbers. The following procedure will guide you in configuring PingID SDK to use your Syniverse account.
component: pingid
page_id: pingid:pingid_sdk:pid_configuring_syniverse_account_for_sdk
canonical_url: http://docs.pingidentity.com/pingid/pingid_sdk/pid_configuring_syniverse_account_for_sdk.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 2, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring a Syniverse account for PingID SDK

## About this task

|   |                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | By default, PingID SDK uses Twilio for voice and SMS. By enabling your own Syniverse account, you are taking responsibility for despatching SMS and voice messages. |

Ensure that you have available your Syniverse account Access Token. You can copy it as required from the Syniverse dashboard. You should also have set up one or more origination phone numbers. The following procedure will guide you in configuring PingID SDK to use your Syniverse account.

To configure PingID SDK for a Syniverse account:

## Steps

1. Log in to the admin console.

2. Go to **Setup → PingID SDK**.

3. Under **SMS/Voice Sender**, choose **Custom**.

   The custom configuration settings appear.

   ![gzf1598337206054](_images/gzf1598337206054.png)

4. In the **SMS/Voice Sender** dropdown, select **Syniverse**.

   |   |                                                                                            |
   | - | ------------------------------------------------------------------------------------------ |
   |   | A custom Syniverse account applies across all PingID SDK applications of the organization. |

5. To configure your Syniverse account to work with PingID SDK:

   1. Copy the URL from the **Address** field.

   2. In your Syniverse account:

      1. In the **Delivery Configuration**, paste the URL that you copied from the PingID SDK **Address** field.

      2. Create 2 subscriptions: **SCG-Message** and **SCG-Voice-Calls**.

         See the Syniverse article [How to setup a Webhook for Receiving Messages and Notifications](https://sdcsupport.syniverse.com/hc/en-us/articles/360001528033-How-to-setup-a-Webhook-for-Receiving-Messages-and-Notifications) for more information.

         |   |                                                                                                                                                                                                                                                                           |
         | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
         |   | These Syniverse configurations are required in order that Ping Identity's dashboards and reports will reflect complete and accurate data. Ping Identity will not be able to troubleshoot SMS or voice events related to Syniverse if these configurations are incomplete. |

6. Copy/paste your Syniverse Access Token to the indicated field.

   |   |                                                                                                                                                                                                                                                                                                                        |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The system uses your access token to connect to your Syniverse account.Recommended: In your account in the Syniverse portal, define an application that is dedicated to PingID SDK traffic. Use this application for analyzing PingID SDK traffic throughput, and troubleshooting SMS or Voice message despatch cases. |

7. Click the **Verify Account** button. That validates the account to PingID SDK and populates the Origination Numbers list from your Syniverse account.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | * If the Access Token is incorrect, you will be shown this error message: ![ofh1597820713553](_images/ofh1597820713553.png)

   * If your Syniverse account is not fully configured a yellow exclamation mark appears next to the Access Token field. If you click on it, this message appears: ![eul1597825300926](_images/eul1597825300926.png)

   * If there are no originating phone numbers in the Syniverse account, it will not be validated to PingID SDK. |

   If the account was successfully verified, the display will change to show a list of originating numbers from Syniverse:

   ![itu1597828167369](_images/itu1597828167369.png)

8. Select at least one originating telephone number to use.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | * Syniverse allows you to define phone numbers for use with either voice or SMS.

   * Syniverse allows the use of sender IDs (in place of telephone numbers) for commercial use or to comply with regulations requiring SMSs to be sent as **transactional** and not **promotional**. When using the Ping Identity account, all originating numbers are defined as transactional with a senderID in Syniverse. To achieve the same functionality in a custom Syniverse account, you must configure it directly in Syniverse.

   * Sender IDs are displayed according to the Sender IDs sent in the API requests.

   * Short codes are supported only for the United States, and only for SMS messages. If only short codes are chosen, but the number is not a US number:

     * If the admin configures **FALLBACK SMS/VOICE SENDER** as **Ping Identity** or **Twilio**, the selected fallback account's phone numbers are used.

     * If the admin **Disables** the **FALLBACK SMS/VOICE SENDER** option, the SMS will not be sent. |

9. Enable **FALLBACK SMS/VOICE SENDER** as **Ping Identity** or **Twilio** to fall back to one of these alternatives if Syniverse becomes unavailable for reasons explained in the following Note.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | **Under fallback:**If PingID SDK receives an error during the message despatch process that the used number is invalid, it will retry using another configured Syniverse number. After attempting to despatch the message and receiving an error for all configured numbers, the fallback flow is triggered.- If there was no way originating the SMS or voice event with the tenant's own Syniverse account and admin defined a fallback, the event will be originated from the configured fallback account

   - The following errors will cause fallback:

     * All API errors (but not SMS delivery errors)

     * No origination number was found on the Syniverse account

   - If a transaction was charged to a specific account (Ping or custom), it does not imply that subsequent transactions will be charged to the same account. The account charged for each transaction is determined on an individual basis. Preference is always given to the custom account.

   - If you configured **FALLBACK SMS/VOICE SENDER** as **Ping Identity**, you will be billed at Ping Identity's rates and not at any preferential rates you have directly from Syniverse. In addition, Ping Identity originating numbers and setup parameters will be in force. |

   * **Ping Identity**:

     Use Ping Identity's SMS/Voice sender account in cases of fallback.

   * **Twilio**:

     ![mzs1598337933242](_images/mzs1598337933242.png)

   Enter the Twilio Account SID, Auth Token and select at least one Origination Number:

   1. Copy/paste the Twilio account SID to the indicated field.

      |   |                                                                                                                                     |
      | - | ----------------------------------------------------------------------------------------------------------------------------------- |
      |   | If the SID is shorter than 34 characters, you will be shown this error message:![dbq1564020510020](../_images/dbq1564020510020.png) |

   2. Copy/paste the Twilio Auth Token to the indicated field.

   3. Click the **Verify Account** button. That validates the account to PingID SDK and populates the Origination Numbers list from your Twilio account.

      |   |                                                                                                                                                                                                                                         |
      | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | * If the AUTH TOKEN is incorrect, you will be shown this error message:![zig1564020510564](../_images/zig1564020510564.png)

      * If there are no originating phone numbers in the Twilio account, it will not be validated to PingID SDK. |

      If the account was successfully verified, the display will change to show a list of originating numbers from Twilio:

      ![duo1598338758424](_images/duo1598338758424.png)

   4. Select at least one originating telephone number to use.

10. To save your settings, click **Save** at the bottom of the **Setup** window.

11. To complete the setup process, enter your legal consent:

    ![cei1597831478688](_images/cei1597831478688.png)

    |   |                                                                            |
    | - | -------------------------------------------------------------------------- |
    |   | You will only be asked for legal consent when entering a new Access Token. |

---

---
title: Configuring a Twilio account for PingID SDK
description: Configure PingID SDK for a Twilio account.
component: pingid
page_id: pingid:pingid_sdk:pid_configuring_twilio_account_pid_sdk
canonical_url: http://docs.pingidentity.com/pingid/pingid_sdk/pid_configuring_twilio_account_pid_sdk.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 29, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring a Twilio account for PingID SDK

Configure PingID SDK for a Twilio account.

## About this task

|   |                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingID SDK uses Twilio for voice and SMS. By enabling your own Twilio account, you are taking responsibility for despatching SMS and voice messages. |

Ensure that you have available your Twilio account SID and auth token. You can copy them as required from the Twilio dashboard. You should also have set up one or more origination phone numbers. The following procedure will guide you in configuring PingID SDK to use your Twilio account.

To configure PingID SDK for a Twilio account:

## Steps

1. Sign on to the admin console.

2. Go to **Setup → PingID SDK**.

3. Under **SMS/Voice Sender**, choose **Custom**.

   The custom configuration settings appear.

   ![A screen capture of the SMS/Voice Sender section with Custom and Twilio selected.](_images/suv1606990921552.png)

4. In the **SMS/Voice Sender** dropdown, select **Twilio**.

   |   |                                                                                         |
   | - | --------------------------------------------------------------------------------------- |
   |   | A custom Twilio account applies across all PingID SDK applications of the organization. |

5. Copy/paste the Twilio account SID to the indicated field.

   |   |                                                                                                                                                                                                                                           |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If the SID is shorter than 34 characters, you will be shown this error message:![A screen capture of the Account SID with the error message "Twilio account SID must be 34 characters long" displaying.](../_images/dbq1564020510020.png) |

6. Copy/paste the Twilio auth token to the indicated field.

7. Click the **Verify Account** button. That validates the account to PingID SDK and populates the **Origination Numbers** list from your Twilio account.

   |   |                                                                                                                                                                                                                                                                                                                               |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | * If the auth token is incorrect, you will be shown this error message:![A screen capture of Account SID with the error message "Error receiving account information" displaying.](../_images/zig1564020510564.png)* If there are no originating phone numbers in the Twilio account, it will not be validated to PingID SDK. |

   If the account was successfully verified, the display will change to show a list of originating numbers from Twilio:

   ![A screen capture of the SMS/Voice Sender section with a list of origination numbers showing.](_images/prw1606991396053.png)

8. Select at least one originating telephone number to use.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | * Twilio allows you to define phone numbers for use with either voice or SMS or both. PingID SDK uses the same number for both voice and SMS and will so relate to the Twilio defined numbers. Twilio numbers (excluding short codes) that are defined as voice only or SMS only are filtered out from the numbers list to avoid operational errors.

   * Twilio allows the use of sender IDs (in place of telephone numbers) for commercial use or to comply with regulations requiring SMSs to be sent as **transactional** and not **promotional**.When using the Ping Identity account, all originating numbers are defined as transactional with a sender ID in Twilio. To achieve the same functionality in a custom Twilio account, you must configure it directly in Twilio. **Sender IDs are displayed according to the sender IDs sent in the API requests. **Short codes are supported only for the United States, and only for SMS messages. If only short codes are chosen, but the number is not a United States number:* If the admin configures **FALLBACK SMS/VOICE SENDER** as **Ping Identity** or **Syniverse**, the selected fallback account's phone numbers are used.

   * If the admin **Disables** the **FALLBACK SMS/VOICE SENDER** option, the SMS will not be sent. |

9. Enable **FALLBACK SMS/VOICE SENDER** as **Ping Identity** or **Syniverse** to fall back to one of these alternatives if Twilio becomes unavailable for reasons explained in the following note.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | **Under fallback:**If PingID SDK receives an error during the message despatch process that the used number is invalid, it will retry using the fallback option.- If there was no way originating the SMS or voice event with tenant's own account, and admin defined a fallback to Syniverse or Ping Identity's account, the event will be originated from the fallback account.

   - The following errors will cause fallback:

     * All API errors (but not SMS delivery errors)

     * No origination number was found on the Twilio account

   - If a transaction was charged to a specific account (Ping or custom), it does not imply that subsequent transactions will be charged to the same account. The account charged for each transaction is determined on an individual basis. Preference is always given to the custom account.

   - If you configured **FALLBACK SMS/VOICE SENDER** as **Ping Identity**, you will be billed at Ping Identity's rates and not at any preferential rates you have directly from Twilio. In addition, Ping Identity originating numbers and setup parameters will be in force. |

   * **Ping Identity**:

     Use Ping Identity's SMS/voice sender account in cases of fallback.

   * **Syniverse**:

     Enter the Syniverse **Access Token** and select at least one **Origination Number**:

     ![A screen capture of the Fallback SMS/Voice Sender section with Syniverse selected and an address entered in the Address field.](_images/kco1606992288845.png)

     1. Copy/paste your Syniverse **Access Token** to the indicated field.

        |   |                                                                                                                                                                                                                                                                                                                        |
        | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        |   | The system uses your access token to connect to your Syniverse account.Recommended: In your account in the Syniverse portal, define an application that is dedicated to PingID SDK traffic. Use this application for analyzing PingID SDK traffic throughput, and troubleshooting SMS or voice message despatch cases. |

     2. Click the **Verify Account** button. That validates the account to PingID SDK and populates the **Origination Numbers** list from your Syniverse account.

        |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
        | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
        |   | * If the **Access Token** is incorrect, you will be shown this error message:![A screen capture of the Access Token with the error message "Invalid account information" displaying.](_images/ofh1597820713553.png)* If your Syniverse account is not fully configured a yellow exclamation mark appears next to the **Access Token** field. If you click on it, this message appears:![A screen capture of the Syniverse Not Configured warning message.](_images/eul1597825300926.png)* If there are no originating phone numbers in the Syniverse account, it will not be validated to PingID SDK.

        * To configure your Syniverse account to work with PingID SDK:

          1. Copy the URL from the **Address** field.

          2. In your Syniverse account:

             * In the **Delivery Configuration**, paste the URL that you copied from the PingID SDK **Address** field.

             * Create two subscriptions: **SCG-Message** and **SCG-Voice-Calls**.See [How to setup a Webhook for Receiving Messages and Notifications](https://sdcsupport.syniverse.com/hc/en-us/articles/360001528033-How-to-setup-a-Webhook-for-Receiving-Messages-and-Notifications) in the Syniverse Developer Community for more information.These Syniverse configurations are required in order that Ping Identity's dashboards and reports will reflect complete and accurate data. Ping Identity will not be able to troubleshoot SMS or voice events related to Syniverse if these configurations are incomplete. |

   If the account was successfully verified, the display will change to show a list of originating numbers from Syniverse:

   \+ image::itu1597828167369.png\[alt="A screen capture of the list of Organization Numbers.",role="border-no-padding"]

   1. Select at least one originating telephone number to use.

10. To save your settings, click **Save** at the bottom of the **Setup** window.

11. To complete the setup process, enter your legal consent:

    ![A screen capture of the Third-party Service Consent.](_images/cei1597831478688.png)

    |   |                                                                   |
    | - | ----------------------------------------------------------------- |
    |   | You will only be asked for legal consent when entering a new SID. |

---

---
title: Configuring the CIBA Authenticator for PingID SDK
description: Create and configure a Client-Initiated Backchannel Authentication (CIBA) Authenticator for PingID SDK.
component: pingid
page_id: pingid:pingid_sdk:pid_configuring_ciba_authenticator_pid_sdk
canonical_url: http://docs.pingidentity.com/pingid/pingid_sdk/pid_configuring_ciba_authenticator_pid_sdk.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 7, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  choose-from-2: Choose from:
  choose-from-3: Choose from:
---

# Configuring the CIBA Authenticator for PingID SDK

Create and configure a Client-Initiated Backchannel Authentication (CIBA) Authenticator for PingID SDK.

## About this task

This procedure describes the process of creating and configuring a Client Initiated Backchannel Authentication (CIBA) Authenticator for the purpose of authenticating users via an out-of-band authentication method.

Prerequisites:

* PingFederate 9.3+

* PingID SDK Package v1.10+ (comprising PingID SDK Integration Kit v1.7+ and PingID SDK Adapter for PingFederate v1.6+)

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | - The PingID SDK CIBA Authenticator supports mobile devices only.

- The PingID SDK CIBA Authenticator is part of the PingID SDK integration with PingFederate, but is not part of the PingID SDK Adapter for PingFederate.

- The CIBA configuration for PingID SDK assumes that a user has at least one mobile device.

- A push notification is sent to the user's primary device. If the user's primary device is not a mobile, the push notification is sent to their first enabled mobile device.

- If an authenticating device is bypassed or pushless, that device is ignored.

- The admin console UI menu labels presented in this topic are those used in PingFederate 9.3. These may differ slightly from other versions of PingFederate. |

## Steps

1. In the PingFederate admin console, select: **OAuth Server → CIBA → Authenticators**.

   ![juc1576769957520](_images/juc1576769957520.png)

2. Click **Create New Instance** to create a new authenticator, or click on an existing authenticator to edit it.

3. Enter the CIBA authenticator's initial instance definitions:

   1. **INSTANCE NAME**: Enter a descriptive name for this authenticator.

   2. **INSTANCE ID**: Enter a string which will be used as an ID for this authenticator. Spaces are not allowed.

   3. **TYPE**: Select **PingID SDK CIBA Authenticator** from the dropdown options.

4. Click **NEXT**.

   The CIBA authenticator's **Type** step is displayed.

   ![til1576770214220](_images/til1576770214220.png)

5. Enter the fields in the authenticator's **Type** step:

   1. **PINGID SDK PROPERTIES**: Upload the PingID SDK properties file from your PingOne admin console:

      * In the PingOne admin console, go to **Setup → PingID → CLIENT INTEGRATION → INTEGRATE WITH PINGID SDK → SETTINGS FILE**.

      * Click **Download**. You may want to provide the file with a more meaningful name.

   |   |                                                                                      |
   | - | ------------------------------------------------------------------------------------ |
   |   | The PingID SDK settings file should not be confused with the PingID properties file. |

   1. **APPLICATION ID**: Enter the application ID that was generated by PingID SDK in your application configuration:

      * In the PingOne admin console, go to **Applications → PingID SDK Applications**, and copy the **Application ID**.

   2. **HEARTBEAT TIMEOUT**: The duration in seconds that thePingID SDK CIBA Authenticator should wait for a heartbeat to verify PingID SDK services, before timing out (default 30 seconds).

6. Click **Show Advanced Fields**.

   The **Type** step's advanced fields are displayed.

   ![wri1576770917051](_images/wri1576770917051.png)

7. Enter the following advanced fields:

   1. **MESSAGES FILE**: The prefix of the name of the PingID SDK messages file.

      * The default is `pingid-sdk-messages`. This default value is applied even if this field is left empty.

      * Templates are located at `/server/default/conf/language-packs.`

      * The file prefix (for example `pingid-sdk-messages`) may be changed, but the suffix for the locale must be in the format "`_<locale>.properties`", for example: `pingid-sdk-messages_en.properties`.

      * The following parameters are required for the default values of the push message's title and body texts in the **DYNAMIC PUSH MESSAGE** and **DYNAMIC CLIENT CONTEXT** fields:

        * `pingid.sdk.ciba.authentication.push.title`: populates the `pushMessageTitle` parameter.

        * `pingid.sdk.ciba.authentication.push.body.start`: The default **DYNAMIC PUSH MESSAGE** template uses this key.

        * `pingid.sdk.ciba.authentication.push.body.user.binding.msg`: The default **DYNAMIC CLIENT CONTEXT** template uses this key.

          These parameters may be replaced, or removed.

   2. **DYNAMIC PUSH MESSAGE**: A velocity language template that PingID SDK uses to pass push authentication messages to the device. The template is used to populate the `pushMessageBody` parameter, using the following variables:

      * `OOBAuthRequestContext`: Refer to the PingFederate developer documentation <https://www.pingidentity.com/content/dam/developer/documentation/pingfederate/server-sdk/9.3/index.html?com/pingidentity/sdk/oobauth/class-use/OOBAuthRequestContext.html>.

      * `LanguagePackMessages`: Refer to the PingFederate developer documentation <https://www.pingidentity.com/content/dam/developer/documentation/pingfederate/server-sdk/9.3/index.html?com/pingidentity/sdk/locale/LanguagePackMessages.html>.

   3. **DYNAMIC CLIENT CONTEXT**: A velocity language template that PingID SDK uses to pass push authentication messages to the device. The template is used to populate the `clientContext` parameter, using the following variables:

      * `OOBAuthRequestContext`: Refer to the PingFederate developer documentation <https://www.pingidentity.com/content/dam/developer/documentation/pingfederate/server-sdk/9.3/index.html?com/pingidentity/sdk/oobauth/class-use/OOBAuthRequestContext.html>.

      * `LanguagePackMessages`: Refer to the PingFederate developer documentation <https://www.pingidentity.com/content/dam/developer/documentation/pingfederate/server-sdk/9.3/index.html?com/pingidentity/sdk/locale/LanguagePackMessages.html>.

      * `SimpleTitle`: String. The push message's title.

      * `SimpleBody`: String. The push message's body text.

      * `JsonHelp`: Jose4j JSONValue class. Refer to <https://javadoc.io/doc/org.bitbucket.b_c/jose4j/0.4.1/org/jose4j/json/internal/json_simple/JSONValue.html>.

8. Save the configuration.

9. **Optional:** Configure a dynamic notification push category or dynamic application ID.

   CIBA authenticators support dynamic notification push categories and dynamic application IDs, and their configurations are similar.

   * Dynamic notification push categories

     A CIBA authenticator can receive a notification push category as a dynamic attribute. This enables a single CIBA authenticator to work with multiple categories, and submit push notifications according to categories.

     |   |                                                                                                                                                                                                                                                                                         |
     | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | **Dynamic notification push category** configuration requires the following software versions:- PingFederate 9.3+

     - PingID SDK Package v1.13+ comprising:

       * PingID SDK Integration Kit v1.9+

       * PingID SDK Adapter for PingFederate v1.8+

       * PingID SDK CIBA Authenticator 1.1+ |

   * Dynamic application IDs

     A CIBA authenticator can receive an application ID as a dynamic attribute. This enables a single CIBA authenticator to work with multiple applications. The dynamic application ID overwrites the default application ID value (see APPLICATION ID configuration above). If the CIBA authenticator receives an invalid or non-existent application ID, an error is generated.

     |   |                                                                                                                                                                                                                                                                                    |
     | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | **Dynamic application ID** configuration requires the following software versions:- PingFederate 9.3+

     - PingID SDK Package v1.14.4+ comprising:

       * PingID SDK Integration Kit v1.11+

       * PingID SDK Adapter for PingFederate v1.8.1+

       * PingID SDK CIBA Authenticator 1.1.1+ |

10. In the PingFederate admin console, select: **OAuth Server → CIBA → Authenticators**.

11. In the authenticator's **Extended Contract** step, under **Extend the Contract**:

    ### Choose from:

    * To configure a dynamic notification push category, enter `pingIdSdkPushCategory`

    * To configure a dynamic application ID, enter `pingIdSdkApplicationId`

      Click **ADD**.

12. Click **SAVE**.

13. In the PingFederate admin console, select: **OAuth Server → CIBA Request Policies**.

14. Click **Add Policy**.

    For more information, see [Managing CIBA request policies](http://docs.pingidentity.com/pingfederate/12.3/administrators_reference_guide/help_cibapoliciesmanagementtasklet_cibapoliciesmanagementstate.html) and [Defining issuance criteria for identity hint contract](http://docs.pingidentity.com/pingfederate/12.3/administrators_reference_guide/help_requesthintcontractmappingtasklet_requesthintcontractissuancecriteriastate.html) in the PingFederate Administration Guide.

15. In the **Identity Hint Contract** step, under **Extend the Contract**:

    ### Choose from:

    * To configure a dynamic notification push category, enter `request.pingIdSdkPushCategory`

    * To configure a dynamic application ID, enter `request.pingIdSdkApplicationId`

    Click **ADD**.

16. Click **NEXT**.

    The CIBA policy's **Identity Hint Mapping** step is displayed.

17. Click **Manage Fulfillment**.

18. In the **Identity Hint Mapping** step:

    ### Choose from:

    * To configure a dynamic notification push category, select `Request` in the **Source** column of the `request.pingIdSdkPushCategory` contract.

    * To configure a dynamic application ID, select `Request` in the **Source** column of the `request.pingIdSdkApplicationId` contract.

    Click **ADD**.

19. Save the configuration.

---

---
title: Configuring the PingID SDK adapter for PingFederate
description: This procedure describes the process of creating and configuring a PingID SDK adapter for the purpose of providing pairing and authentication solutions integrated with PingFederate.
component: pingid
page_id: pingid:pingid_sdk:pid_configuring_sdk_adapter_for_pf
canonical_url: http://docs.pingidentity.com/pingid/pingid_sdk/pid_configuring_sdk_adapter_for_pf.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 7, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring the PingID SDK adapter for PingFederate

## About this task

This procedure describes the process of creating and configuring a PingID SDK adapter for the purpose of providing pairing and authentication solutions integrated with PingFederate.

Prerequisites:

* PingFederate 8.2+

* If your installation should support integration with the PingFederate Authentication API, the following minimum software versions are required:

  * PingFederate 9.3+

  * PingFederate PingID SDK IDP Adapter 1.7+

|   |                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The admin console UI menu labels in this document are those used in PingFederate 9.0. These may differ slightly from earlier versions of PingFederate. |

The creation and configuration of an adapter comprises three mandatory steps:

* [\[createConfigureSelector\]](#createConfigureSelector)

* [\[createConfigureAdapter\]](#createConfigureAdapter)

* [\[createConfigurePolicy\]](#createConfigurePolicy)

The following optional enhancements improve the user authentication experience:

* [\[optConfigProxy\]](#optConfigProxy) (requires PingFederate PingID SDK IDP Adapter 1.4+)

* [\[optHtmlFormQRbutton\]](#optHtmlFormQRbutton)

* [\[optCancelButton\]](#optCancelButton)

  |   |                                                                                                                                                                                         |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | * QR code based authentication requires PingFederate 9.2+ and PingFederate PingID SDK IDP Adapter 1.2+.

  * QR code based authentication is not supported for the PF Authentication API. |

## Steps

1. Create and configure a selector or tracked HTTP parameter:

   Create an instance of the PingID SDK Payload Handling Selector, which is required as a preprocessor to an authentication policy that uses the PingID SDK adapter.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | * **PingFederate 9.1.x and below**: Creation of a PingID SDK Payload Handling Selector is mandatory.

   * **PingFederate 9.2+**: Creation of a PingID SDK Payload Handling Selector is not required, only if the "`payload`" parameter has been added to PingFederate's Tracked HTTP Parameters (see <https://support.pingidentity.com/s/document-item?bundleId=pingfederate-92&topicId=adminGuide%2Fpf_t_defineAuthenticationPolicies.html>):

     ```
     *Identity Provider → AUTHENTICATION POLICIES → Policies → Tracked HTTP Parameters → Add*: [.codeph]``payload``
     ``` |

   1. In the PingFederate admin console, select: **Identity Provider → AUTHENTICATION POLICIES → Selectors**.

      ![ygg1564020794131](_images/ygg1564020794131.png)

      The **Manage Authentication Selector Instances** screen is displayed.

   2. Click **Create New Instance** to create a new selector, or click on an existing selector to edit it.

      ![mbs1564020795095](_images/mbs1564020795095.png)

      The selector's **Type** step is displayed.

   3. All fields in the **Type** step are mandatory:

      ![dif1564020796179](_images/dif1564020796179.png)

      * INSTANCE NAME

        Enter a descriptive name for this selector.

      * INSTANCE ID

        Enter a string which will be used as an ID for this selector. Spaces are not allowed.

      * TYPE

        Select PingID SDK Payload Handling Selector from the dropdown options.

   4. Click **NEXT**.

   5. Click **NEXT** in the **Authentication Selector** screen.

   6. Click **DONE** in the **Summary** screen, to return to the **Manage Authentication Selector Instances** screen.

   7. Click **SAVE** to persist changes.

2. Create and configure an adapter:

   1. In the PingFederate admin console, select: **Identity Provider → APPLICATION INTEGRATION → Adapters**.

      ![wsb1564020797025](_images/wsb1564020797025.png)

      The **Manage IdP Adapter Instances** screen is displayed.

   2. Click **Create New Instance** to create a new adapter, or click on an existing adapter to edit it.

      ![npn1564020798000](_images/npn1564020798000.png)

      The adapter's **Type** step is displayed.

   3. Enter the following fields in the **Type** step:

      ![cto1564020798953](_images/cto1564020798953.png)

      * INSTANCE NAME

        Enter a descriptive name for this adapter.

      * INSTANCE ID

        Enter a string which will be used as an ID for this adapter. Spaces are not allowed.

      * TYPE

        Select **PID SDK Adapter**from the dropdown options.

      * PARENT INSTANCE

        Leave this field with the default value: **None**.

   4. Click **NEXT** to continue to the **IdP Adapter** step.

      ![uqz1564020799948](_images/uqz1564020799948.png)

   5. Configure the following fields:

      * PINGID SDK PROPERTIES

        * Mandatory.

        * Upload the PingID SDK properties file from your PingOne admin console:

          * In the PingOne admin console, go to **Setup → PingID → CLIENT INTEGRATION → INTEGRATE WITH PINGID SDK → SETTINGS FILE**.

          * Click **Download**. You may want to provide the file with a more meaningful name.

          * If you use a proxy, note that the deprecated configuration of the `pingidsdk_proxy_url` entry in the PingID SDK properties file is still supported. Configuration of an entry in the PingFederate `run.properties` file (see [\[optConfigProxy\]](#optConfigProxy)), is the preferred configuration.

            |   |                                                                                                                                                                              |
            | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
            |   | If entries are defined in both the PingFederate `run.properties` and the PingID SDK properties files, the definition in the PingID SDK properties file will take precedence. |

            |   |                                                                                      |
            | - | ------------------------------------------------------------------------------------ |
            |   | The PingID SDK settings file should not be confused with the PingID properties file. |

      * APPLICATION ID

        * Mandatory.

        * Enter the application ID that was generated by PingID SDK in your application configuration:

          * In the PingOne admin console, go to **Applications → PingID SDK Applications**, and copy the **Application ID**.

            |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
            | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
            |   | * From PingFederate 8.4 and PingFederate PingID SDK IDP Adapter 1.2, multiple applications can be linked to a single PingID SDK adapter for PingFederate. This is achieved with dynamic parameters overriding the value of **Application ID**. Refer to [Dynamic parameters support](https://apidocs.pingidentity.com/pingid-sdk/guide/pf-adapter/pid_c_SDKforPFdynamicParameters/) in the PingID SDK developers guide for further details.

            * In earlier versions of PingFederate and the PingID SDK Adapter, each application requires its own separate PingID SDK adapter for PingFederate. |

      * DEVICE PAIRING

        * Choose how users will pair their first device when it's a mobile device:

          * **Automatic** (default).

      Once authorization of the adapter completes successfully, the automatic pairing process begins.

      * **Manual**.

        Once authorization of the adapter completes, the pairing process is not initiated. The pairing process is initiated separately. Depending on the **UNPAIRED USERS - MANUAL PAIRING**Bypass field configuration, the user will be allowed into the application or denied access.

        Refer to [User device pairing](https://apidocs.pingidentity.com/pingid-sdk/guide/overview/pid_c_SDKpairFirstDevice/) in the PingID SDK developer's documentation.

        * UNPAIRED USERS - MANUAL PAIRING

          * Relevant only when **Manual** pairing is selected:

          * Choose whether to allow users without a paired device to **Bypass Authentication** (default), or **Block User - Require Pairing** a device before continuing.

        * UNPAIRED USERS - WEB LOGIN

          Choose whether to allow users without a paired device to **Bypass Authentication** (default), or **Block User - Require Pairing** a device before continuing, when signing in from a web platform.

        * ADDITIONAL TRUSTED DEVICES

          When a user who already has a paired device, is pairing an additional device, choose whether to allow the user to approve pairing of the new device using a device in their existing trusted devices network and **Verify New Devices with Primary Device** (default), or to **Pair Each Device Individually**, without primary device verification.

        * MFA TIMEOUT

          The duration of the PingID SDK MFA session with the adapter in minutes, before it times out and users need to authenticate again. (Default: 10 minutes, maximum 30 minutes.)

        * USER VERIFICATION

          When the application setting **VERIFY DEVICES USING APPLE/ANDROID PUSH SERVICE** is enabled (in the PingOne admin console: **Applications → PingID SDK Applications → \[Application] → Configuration** ) and there is no approval for a silent push sent for extra verification, choose whether to **Regard as Success** or **Regard as Failure**.

          |   |                                                                                                                                                                     |
          | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
          |   | This configuration is relevant only to logins from mobile devices, and will be applied to pushless device scenarios, and events when the network is not accessible. |

        * AUTHENTICATION DURING ERRORS

          If there are network problems or the PingID SDK service is unreachable, choose whether to **Bypass users** (default) or **Block users** who attempt to authenticate.

        * HEARTBEAT TIMEOUT

          The duration in seconds that the PingID SDK adapter should wait for a heartbeat to verify PingID SDK services, before timing out (default 30 seconds).

   6. Click **Advanced fields**.

      The advanced fields are displayed.

      ![tki1569390722952](_images/tki1569390722952.png)

   7. Configure the following fields:

      * HTML TEMPLATE

        |   |                                                                         |
        | - | ----------------------------------------------------------------------- |
        |   | This field is relevant only when the PF Authentication API is not used. |

        * The name of the HTML template file whose screens are displayed to the user during the adapter authorization flow.

        * The default is `pingid.sdk.login.template.html`. This default value is applied even if this field is left empty.

        * Templates are located at `/server/default/conf/template`.

      * MESSAGE FILE

        * The prefix of the name of the PingID SDK messages file.

        * The default is `pingid-sdk-messages`. This default value is applied even if this field is left empty.

        * Templates are located at `/server/default/conf/language-packs.`

        * The file prefix (for example `pingid-sdk-messages`) may be changed, but the suffix for the locale must be in the format "`_<locale>.properties`", for example: `pingid-sdk-messages_en.properties`.

      * CHANGE DEVICE

        |   |                                                                         |
        | - | ----------------------------------------------------------------------- |
        |   | This field is relevant only when the PF Authentication API is not used. |

        * Choose whether the **CHANGE DEVICE** flow is allowed or denied.

          * **Allow** (default): Users will see the **CHANGE DEVICE** button on all relevant screens.

          * **Deny**: Users will not see the **CHANGE DEVICE** button, and will not have this option as part of their authentication flow.

      * SUCCESS SCREENS

        |   |                                                                         |
        | - | ----------------------------------------------------------------------- |
        |   | This field is relevant only when the PF Authentication API is not used. |

        * Choose whether to present the **SUCCESS SCREENS** as part of the authentication flow.

        * Default: **Show to Users**.

      * ERROR SCREENS

        |   |                                                                         |
        | - | ----------------------------------------------------------------------- |
        |   | This field is relevant only when the PF Authentication API is not used. |

        * Choose whether to present the **ERROR** screens as part of the authentication flow.

        * Default: **Show to Users**.

      * TIMEOUT SCREENS

        |   |                                                                         |
        | - | ----------------------------------------------------------------------- |
        |   | This field is relevant only when the PF Authentication API is not used. |

        * Choose whether to present the **TIMEOUT** screens as part of the authentication flow.

        * Default: **Show to Users**.

      * QR CODE BASED AUTHENTICATION

        |   |                                                                              |
        | - | ---------------------------------------------------------------------------- |
        |   | QR code based authentication is not supported for the PF Authentication API. |

        Choose whether to use QR code based authentication, and in which cases:

        * **Disable** (default).

        * **Conditionally enable**: The QR code is displayed only when the user is unknown.

        * **Always enable**: Allows QR code based authentication, whether the user is known or not.

        * **Default**: QR code based authentication is the default authentication method, and the QR code is presented by default to the user.

          |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
          | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
          |   | * The **Default** setting overrides the **DEVICES SELECTION** setting in the PingID SDK Applications Configuration in the PingOne admin web portal.

          * QR code based authentication is supported from PingFederate 9.0. Note that PingFederate PingID SDK IDP Adapter 1.2 will work on versions earlier than 9.0 only when **QR CODE BASED AUTHENTICATION** is set to **Disable**. Attempting to save **QR CODE BASED AUTHENTICATION** using a setting other than **Disable** on versions of PingFederate earlier than 9.0 will result in the error message. |

      * ROOTED/JAILBROKEN DEVICE

        * When an authentication device is identified as rooted or jailbroken:

          * **Allow**: Allow the authentication flow to continue.

          * **Block** (default): Deny the authentication request.

   8. Click **NEXT** to continue to the **Extended Contract**step.

      The contract fields are displayed. In addition to the `username` attribute, the **Core Contract** also displays the following attributes:

      * `pingid.sdk.status` holds information about the level of authentication through which the user was authenticated. For further information about this attribute, refer to [PingFederate access token - pingid.sdk.status attribute](https://apidocs.pingidentity.com/pingid-sdk/guide/pf-adapter/pid_c_SDKforPFpingidSdkStatus) in the PingID SDK developer guide.From PingFederate PingID SDK IDP Adapter 1.5, the following **Core Contract** attributes provide information about devices that are rooted or jailbroken:

      * `pingid.sdk.status.reason`: Possible value is "device\_rooted\_or\_jailbroken", which will appear only when the `pingid.sdk.status` has the value "pairing\_error" and the device is rooted.

      * `authenticating.device.rooted`: True or false.

      * `accessing.device.rooted`: True or false.You can add more attributes to the contract under Extend the Contract, per the example below.

        ![wgo1569393938969](_images/wgo1569393938969.png)

   9. Click **NEXT** to continue to the **Adapter Attributes** step.

      ![grt1564020803131](_images/grt1564020803131.png)

      Check the **Pseudonym** checkbox for the username attribute.

   10. Click **NEXT** through each of the subsequent steps.

   11. Click **DONE** in the **Summary** step to return to the **Manage IdP Adapter Instances** screen.

   12. Click **SAVE** to persist changes.

       |   |                                                                                                                                                                                                                                                                                                                                |
       | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
       |   | ```
       *Adapter session considerations*
       ```+ It is important to update the `<pf_install>/pingfederate/server/default/conf/size-limits.conf` file to adjust the session configuration to ensure that the PingID SDK adapter functions correctly.+ Note that the settings in `size-limits.conf` are global, affecting all adapters. |

3. **Create and configure a policy**:

   Create a policy in PingFederate, for the purpose of determining the authentication flow.

   The flexibility of PingFederate permits implementation of different policy models, and may vary according to organizational or application requirements.

   The following example describes a basic policy configuration for the PingID SDK adapter, highlighting mandatory settings. The example defines a 1st factor authentication method before the SDK adapter, from which the username must then be mapped to the SDK adapter.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | * The SDK selector or Tracked HTTP Parameter:

     * **PingFederate 9.1.x and below**: The PingID SDK Payload Handling Selector that was created earlier must be the first action in a policy actions chain.

     * **PingFederate 9.2+**: The PingID SDK Payload Handling Selector is not required, only if the "`payload`" parameter has been added to PingFederate's Tracked HTTP Parameters (see <https://support.pingidentity.com/s/document-item?bundleId=pingfederate-92&topicId=adminGuide/pf_t_defineAuthenticationPolicies.html>).

   * The SDK adapter created earlier must participate in the policy flow. |

   1. In the PingFederate administrative console, select: **Identity Provider → AUTHENTICATION POLICIES → Policies**.

      ![dvm1564020805121](_images/dvm1564020805121.png)

   The **Manage Authentication Policies** screen is displayed.

   1. Enter the following fields:

      ![osp1564020806585](_images/osp1564020806585.png)

      1. Check the **ENABLE IDP AUTHENTICATION POLICIES** checkbox.

      2. The SDK selector or Tracked HTTP Parameter:

         * **PingFederate 9.1.x and below**: The first **ACTION** in the policy chain **must** be mapped to the SDK selector created earlier:

           * Open the **ACTION** dropdown.

           * Click **IdP Adapters**.

           * Select the **SDK selector**.

           * The SDK selector has only one return status: **Success**.

             For the policy's following action, select **HTML Adapter** (or any other 1st factor adapter) from the **ACTION** dropdown.

         * **PingFederate 9.2+**: If the "`payload`" parameter has been added to PingFederate's Tracked HTTP Parameters (see <https://support.pingidentity.com/s/document-item?bundleId=pingfederate-92&topicId=adminGuide/pf_t_defineAuthenticationPolicies.html>):

           * Open the **ACTION** dropdown.

           * Click **HTML Adapter** (or any other 1st factor adapter).

           * Select the **HTML Adapter**.

      3. The **HTML Adapter** has two resulting states:

         * **Fail**:

           The action following **Fail** will be **Done**, meaning the policy flow ends at this point.

         * **Success**:

           Select the **SDK Adapter** for the action following **Success**.

      4. Map the username from the **HTML Adapter** (or any other 1st factor adapter) step in the policy flow to the **SDK Adapter**:

         * Click on **Options** below the SDK Adapter.

           The **Incoming User ID** screen opens.

           ![syn1564020807632](_images/syn1564020807632.png)

           * **Source**: Select **HTML Adapter**.

           * **Attribute**: Select **username**.

         * Click **Done** to return to the **Manage Authentication Policies** screen.

           ![ebq1564020808512](_images/ebq1564020808512.png)

      5. An Authentication Policy Contract should then be mapped into the target application (SP Connection, OAuth Grant Mapping, etc.) for which you want to provide SSO services.

         For example:

         ![cvp1564020810028](_images/cvp1564020810028.png)

      6. Click **Save**.

4. (Optional) **Configure proxy settings**:

   Define an entry in the PingFederate `run.properties` file, as described in the PingFederate admin guide (see [Configuring forward proxy server settings](http://docs.pingidentity.com/pingfederate/12.3/administrators_reference_guide/pf_configure_forward_proxy_server_settings.html)).

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The native PingFederate method for defining a proxy is the preferred option. The following deprecated method is still supported:1) Manually add a `pingidsdk_proxy_url` entry to your PingID SDK properties file:

      ```
      pingidsdk_proxy_url=<your proxy address>
      ```

   2) Do not change the `pingidsdk_url` entry.If entries are defined in both the PingFederate `run.properties` and the PingID SDK properties files, the definition in the PingID SDK properties file will take precedence. |

5. (Optional) **HTML Form Adapter QR code button - passwordless login**:

   |   |                                                                                                                                                                                         |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | * QR code based authentication requires PingFederate 9.2+ and PingFederate PingID SDK IDP Adapter 1.2+.

   * QR code based authentication is not supported for the PF Authentication API. |

   QR code based authentication is an alternative method, which offers secure, passwordless authentication. QR code based authentication can effectively eliminate the need for first factor authentication. This method combines the strength of a strong secure authentication measure, with a streamlined user experience.

   The following image presents the user HTML Form Adapter access screen. Once configured, the user can either use the traditional username and password sign on at the left, or select the **Sign on with QR code** button on the right. **Sign on with QR code** generates a QR code image which the user can scan with a trusted mobile device, thus achieving rapid secure passwordless authentication.

   ![qof1564020811460](_images/qof1564020811460.png)

   1. Refer to [Enabling third-party identity providers without registration](http://docs.pingidentity.com/pingfederate/12.3/administrators_reference_guide/pf_enabling_thirdparty_identity_providers_without_registration.html) in the PingFederate documentation, specifically the following steps:

      1. Make a note of which authentication policy contract is currently being used in your policy.

      2. Create a local identity profile.

         |   |                                                                                                                                                         |
         | - | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
         |   | When creating the local identity profile, you must add "`QR Code`" as an **Authentication Source**.+ ![piu1564020812124](_images/piu1564020812124.png)+ |

      3. Configure the HTML Form Adapter instance for customer identities.

   2. Navigate to **Identity Provider → Authentication Policies → Policies**.

      ![dvm1564020805121](_images/dvm1564020805121.png)

   3. In the **Authentication Policies** page, edit your PingID SDK authentication policy.

   4. Below the HTML Form Adapter, expand the policy tree and select **Rules**.

      ![qww1564020812711](_images/qww1564020812711.png)

   5. In the **Rules** popup, fill in the following values:

      | Field            | Value           |
      | ---------------- | --------------- |
      | `Attribute Name` | `policy.action` |
      | `Condition`      | `equal to`      |
      | `Value`          | `QR Code`       |
      | `Result`         | `QR Code`       |

      ![tcu1564020813241](_images/tcu1564020813241.png)

   6. Click **Done**.

   7. Below the **HTML Form Adapter** branch, the **QR CODE** policy result is displayed, in addition to the FAIL and SUCCESS branches.

      ![hbj1564020813988](_images/hbj1564020813988.png)

   8. In the **QR Code** result, select the **SDK Adapter**, and finish building the flow according to the steps in the [\[createConfigurePolicy\]](#createConfigurePolicy) section.

      The final result should appear similar to the following image:

      ![vaq1564020814649](_images/vaq1564020814649.png)

6. (Optional) **Add a CANCEL button to the QR code based authentication flows**:

   |   |                                                                                                                                                                                         |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | * QR code based authentication requires PingFederate 9.2+ and PingFederate PingID SDK IDP Adapter 1.2+.

   * QR code based authentication is not supported for the PF Authentication API. |

   There may be scenarios where an organization wants to allow users of QR code based authentication to cancel an authentication request. This can be achieved by configuring a CANCEL button in the QR based authentication flow, and defining its functionality in the authentication policy. By default, the CANCEL button is not enabled.

   1. **Configure a CANCEL Button in the HTML template**:

      1. Open the HTML template file `<PingFederate installation folder>/pingfederate-<version>/pingfederate/server/default/conf/template/pingid.sdk.login.template.html`in a text editor.

      2. Scroll down to the **QR Code section**. You'll see the following commented out lines, where you can add a CANCEL button in the QR image page, deep link page and loading page:

         ```
         <!-- uncomment the following line if you "cancel" is supported -->
         <!-- <a class="button" onclick="cancelQRCode(this)"href="javascript:void(0);">$messages.getMessage("pingid.sdk.authenticating.button.qrcode.cancel")</a>-->
         ```

      3. To add a CANCEL button to the page, uncomment the second line (containing the \<a> tags).

   2. **Add a CANCEL function in the authentication policy**:

      1. In the PingFederate admin console, navigate to **Identity Provider → Authentication Policies → Policies**.

   ![dvm1564020805121](_images/dvm1564020805121.png)

   1. In the **Authentication Policies** page, edit your PingID SDK authentication policy.

   2. Below the SDK Adapter, expand the policy tree and select **Rules**.

      ![qgr1564020815242](_images/qgr1564020815242.png)

   3. In the **Rules** popup, fill in the following values:

      | Field            | Value                                         |
      | ---------------- | --------------------------------------------- |
      | `Attribute Name` | `policy.action`                               |
      | `Condition`      | `equal to`                                    |
      | `Value`          | `canceled`                                    |
      | `Result`         | `Fallback` (You may choose a different name.) |

      ![gut1564020815785](_images/gut1564020815785.png)

   4. Click **Done**.

   5. Below the **SDK Adapter** branch, the **FALLBACK** policy result is displayed, in addition to the FAIL and SUCCESS branches.

      ![psm1564020816420](_images/psm1564020816420.png)

   6. To configure it as a restart flow action, select **Restart**.

      |   |                                                                                               |
      | - | --------------------------------------------------------------------------------------------- |
      |   | You can also choose different actions. For example, redirect the user to a different adapter. |

   7. Click **Done**.

   8. Click **Save**.

   9. (Optional): If you want to change the action's default value ("canceled") to a different value:

      * Go to the following line in the HTML template:

        ```
        <form id="cancelQRCodeForm" name="cancelQRCodeForm"
                  action="$resumePath?cancel=1&action=canceled" method="post">
                  <input type="hidden" name="csrfToken" id="csrfToken" value="$csrfToken"
                  encode="false"/>
        </form>
        ```

      * Change `&action=canceled` to `&action=<your value>`. Make sure that this new value is identical to the "`Value`" field in the **Authentication Policies → Rules** popup.

      * Click **Done**.

      * Click **Save**.

---

---
title: Distributing the PingID SDK settings file and application ID
description: Distribute the PingID SDK settings file and application ID to integrate the component into the application code.
component: pingid
page_id: pingid:pingid_sdk:pid_sdk_distribute_settings_file
canonical_url: http://docs.pingidentity.com/pingid/pingid_sdk/pid_sdk_distribute_settings_file.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 23, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
---

# Distributing the PingID SDK settings file and application ID

Distribute the PingID SDK settings file and application ID to integrate the component into the application code.

## About this task

Application developers require the following resources in order to integrate the PingID SDK component into their application code:

* PingID SDK settings file

* Application ID

Administrators download the PingID SDK settings file and access the application ID in the administrative web portal for distribution to the application developers.

## Steps

1. In the admin web portal, go to **Setup → PingID SDK → Integrate with PingID SDK → Settings File → Download**. ![Screen capture illustrating the Settings File Download for integrating PingID SDK with your application.](_images/xxn1617868406363.png)

2. From the PingOne web portal, go to **Applications → PingID SDK Applications**.

   ### Result:

   The **Application ID** displays below the application's name.

   ![Screen capture illustrating the PingID SDK application IDs.](_images/uay1564020819206.png)

---

---
title: Enabling or disabling a PingID SDK app
description: Enable or disable a PingID SDK application.
component: pingid
page_id: pingid:pingid_sdk:pid_sdk_enable_disable_app
canonical_url: http://docs.pingidentity.com/pingid/pingid_sdk/pid_sdk_enable_disable_app.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 23, 2023
section_ids:
  steps: Steps
---

# Enabling or disabling a PingID SDK app

Enable or disable a PingID SDK application.

## Steps

1. In the admin web portal, go to **Applications → PingID SDK Applications**.

2. To enable or disable the desired application, click the toggle button to the right of your app. ![Screen capture illustrating the PingID SDK Applications tab.](_images/uay1564020819206.png)

---

---
title: Installing the PingID SDK Integration Kit for PingFederate
description: Install the PingID SDK integration kit for single sign-on (SSO) with PingFederate.
component: pingid
page_id: pingid:pingid_sdk:pid_installing_pid_sdk_i_for_pf
canonical_url: http://docs.pingidentity.com/pingid/pingid_sdk/pid_installing_pid_sdk_i_for_pf.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 27, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
---

# Installing the PingID SDK Integration Kit for PingFederate

Install the PingID SDK integration kit for single sign-on (SSO) with PingFederate.

## Before you begin

Your organization is using PingID SDK as an authentication solution for federated SSO with PingFederate.

PingID SDK integration kit requirements:

* Register for the PingID Enterprise service on PingOne.

* Configure the PingID service and download the PingID SDK properties file. For more information, see [Distributing the PingID SDK settings file and application ID](pid_sdk_distribute_settings_file.html).

* PingFederate 8.2 or later.

  |   |                                                                                                                                                                                                                |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If your installation should support integration with the PingFederate Authentication API, the following minimum software versions are required:- PingFederate 9.3+

  - PingID SDK adapter 1.7+ for PingFederate |

* Network access to a PingFederate installation.

* Open ports:

  * 443 (in external firewall)

  * 1812 (in internal firewall)

* Administrator permissions on PingFederate.

## About this task

The PingID SDK integration kit is part of the PingID SDK package. Download the full PingID SDK package, including the PingID SDK integration kit from <https://www.pingidentity.com/en/resources/downloads/pingid.html>.

## Steps

1. Extract the integration kit package.

   |   |                                                                                                                                                                                                                                                                                   |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The integration kit includes the following directories:- `dist`: The PingID SDK adapter for SSO using PingFederate, the PingID SDK selector, the default HTML sign-on template, and language support.

   - `legal`: Legal details, attributions, copyrights, patents, and licenses. |

2. On the PingFederate host, stop the PingFederate server if it is running.

3. Remove any previous PingID SDK integration kit version files in the `<pingfederate-installation>/server/default/deploy` directory.

4. Copy the following files from the `<PingID SDK Integration Kit>/dist` directory to the `<pingfederate-installation>/server/default/deploy` directory:

   * `pf-pingid-sdk-idp-adapter-<version>.jar`

   * `pf.plugin.pingid-sdk-idp-selector-<version>.jar`

   * `pingid-sdk-web.war`

5. Copy `pingid.sdk.login.template.html` to `<pingfederate-installation>/server/default/conf/template`.

6. Copy `pingid-sdk-messages_en.properties` to `<pingfederate-installation>/server/default/conf/language-packs`.

7. If `<pingfederate-installation>/server/default/lib/pf-authn-api-<version>.jar` is older than the `pf-authn-api-<version>.jar` in the PingID SDK Integration Kit, replace it with the `pf-authn-api-<version>.jar` from the PingID SDK Integration Kit.

8. If you want to use the PingFederate Authentication API, merge the contents of the `authn-api-messages.properties` file from the PingID SDK Integration Kit into the `<pingfederate-installation>/server/default/conf/language-packs/authn-api-messages.properties` file.

9. Restart the PingFederate server.

10. If PingFederate is deployed on clustered servers, repeat these steps for all PingFederate nodes.

---

---
title: Managing a Syniverse account for PingID SDK
description: Managing an account includes:
component: pingid
page_id: pingid:pingid_sdk:pid_managing_syniverse_account_pid_sdk
canonical_url: http://docs.pingidentity.com/pingid/pingid_sdk/pid_managing_syniverse_account_pid_sdk.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 2, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Managing a Syniverse account for PingID SDK

## About this task

Managing an account includes:

* Changing active originating numbers and fallback setting (as in [Configuring a Syniverse account for PingID SDK](pid_configuring_syniverse_account_for_sdk.html))

* Changing to another account

* Deleting the custom account

To manage a custom Syniverse account:

## Steps

1. Log in to the admin console.

2. Go to **Setup → PingID SDK**.

The **SYNIVERSE ACCOUNT** configuration is displayed.

1. Select at least one originating telephone number to use.

2. You may change the Fallback settings.

3. To switch to a different account, click **Change Account**. You will be offered the configuration window for a new account. Proceed as in [Configuring a Syniverse account for PingID SDK](pid_configuring_syniverse_account_for_sdk.html).

4. To delete the active custom account, click the **Ping Identity** radio button.

5. To save your settings, click **Save** at the bottom of the **Setup** window.

---

---
title: Managing a Twilio account for PingID SDK
description: Manage a custom Twilio account.
component: pingid
page_id: pingid:pingid_sdk:pid_managing_twilio_account_for_sdk
canonical_url: http://docs.pingidentity.com/pingid/pingid_sdk/pid_managing_twilio_account_for_sdk.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 25, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
  result-2: Result:
---

# Managing a Twilio account for PingID SDK

Manage a custom Twilio account.

## About this task

Managing an account includes:

* Changing active originating numbers and fallback setting, as in [Configuring a Twilio account for PingID SDK](pid_configuring_twilio_account_pid_sdk.html)

* Changing to another account

* Deleting the custom account

## Steps

1. In the PingID admin portal, go to **Setup → PingID SDK**.

   ### Result:

   The **Twilio Account** configuration displays.

   ![A screen capture of PingID showing the Twilio account configuration.](../_images/smd1564020513309.png)

2. Select at least one originating telephone number to use.

3. To change the fallback settings, in the **Fallback To Default Account** section, click the desired setting.

4. To switch to a different account, click **Change Account**.

   ### Result:

   The configuration window for a new account appears.

5. To delete the active custom account, click **Ping Identity**.

6. Click **Save**.

---

---
title: PingID Admin Activity Report fields for PingID SDK
description: The PingID Admin Activity Report produces output with the following default and optional fields.
component: pingid
page_id: pingid:pingid_sdk:pid_admin_activity_report_fields_sdk
canonical_url: http://docs.pingidentity.com/pingid/pingid_sdk/pid_admin_activity_report_fields_sdk.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 2, 2024
---

# PingID Admin Activity Report fields for PingID SDK

The PingID Admin Activity Report produces output with the following default and optional fields.

Customize the report output by adding optional field columns, removing default fields, and changing default runtime parameters. Find more information in [Run a custom report](http://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_run_custom_report.html).

| Field name        | Description                                                                                                                  | Default/Optional |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **Timestamp**     | The date and time when the admin action event occurred, according to the current time zone.                                  | Default          |
| **Admin**         | The email address, username, or LDAP name assigned to the administrator who performed the action.                            | Default          |
| **Admin Type**    | The type of administrator. This will be "user" unless the action was performed by a Ping Identity employee.                  | Default          |
| **Action**        | The type of resource and the action of the event. Possible values:- `account updated`

- `report updated`

- `user updated`  | Default          |
| **Resource Name** | The name of the resource on which the action was performed.                                                                  | Default          |
| **Resource Type** | The type of resource on which the action was performed. Possible values:- `account`

- `report`

- `user`                    | Default          |
| **Message**       | Detailed information regarding the action event, including the resource type, resource name, and nature of the admin action. | Default          |
| **Admin Id**      | The unique identifier assigned by PingOne to the administrator.                                                              | Optional         |
| **Browser Agent** | The browser name and version used for PingOne SSO.                                                                           | Optional         |
| **IP Address**    | The IP address of the host used to initiate the event.                                                                       | Optional         |
| **Resource Id**   | The unique identifier assigned by PingOne to the resource.                                                                   | Optional         |
| **Status**        | The status of the action. Possible values:- `SUCCESS`

- `FAILURE`                                                           | Optional         |

---

---
title: PingID SDK
description: PingID SDK enables you to provide your customers with advanced multi-factor authentication (MFA) functionality that balances security and convenience.
component: pingid
page_id: pingid:pingid_sdk:pid_sdk
canonical_url: http://docs.pingidentity.com/pingid/pingid_sdk/pid_sdk.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 10, 2023
section_ids:
  pingid-sdk-settings: PingID SDK settings
  system-settings: System settings
  application-settings: Application settings
---

# PingID SDK

PingID SDK enables you to provide your customers with advanced multi-factor authentication (MFA) functionality that balances security and convenience.

|   |                                                                                                                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Because PingID SDK is no longer actively supported and will be deprecated, you should migrate to [PingOne MFA](https://www.pingidentity.com/en/platform/capabilities/multi-factor-authentication/pingone-mfa.html). For more information on migrating to PingOne MFA, contact your Ping account executive or customer success manager. |

To send your consumers branded, customizable push notifications, you can embed the PingID mobile SDK into new or existing iOS or Android applications. As an alternative authentication factor, you can also use SMS, voice, and email notifications with customized content and a one-time passcode (OTP). QR code-based authentication is available as a passwordless authentication option. These methods allow your organization to provide MFA without introducing unnecessary friction or forcing your consumers to download a separate MFA application. For more information, see [Introduction to PingID SDK](https://apidocs.pingidentity.com/pingid-sdk/guide/overview/pid_c_SDKintroduction/).

PingOne hosts the PingID services and provides the web administrative portal for PingID SDK application and user management. Register for a PingOne account at <https://admin.pingone.com/web-portal/register>.

## PingID SDK settings

### System settings

System settings apply system-wide to all tenants and all applications and are not configurable.

| System parameter                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Value (not configurable)                   | Relevant error or status                                                        |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------ | ------------------------------------------------------------------------------- |
| `Authentication session lifetime` | The period during which application logic can check the status of an authentication. In cases where users didn't receive a push notification or they use an offline device, they can complete the authentication.                                                                                                                                                                                                                                                                                                        | 30 minutes                                 | Top level error code: `NOT_FOUND`                                               |
| `Push notification timeout`       | The time a new authentication notification request has to reach a user's mobile device before timeout occurs. There might be a difference between the response of iOS and Android platforms when an app moves the push notification payload to the mobile SDK. The push notification period is included in the `Online session timeout` period.Factors such as specific implementations and platform limitations might also impact the time it takes for an app to move the push notification payload to the mobile SDK. | 20 seconds                                 | `status`: `TIMEOUT`                                                             |
| `Online session timeout`          | The total amount of time a new authentication request has before timing out. The difference between the `Push notification timeout` and `Online session timeout` indicates the amount of time the user has to respond upon receiving an authentication request before timeout occurs.                                                                                                                                                                                                                                    | 40 seconds                                 | `status`: `TIMEOUT`                                                             |
| `Silent push timeout`             | The extension of time for approval of a trusted device when `VERIFY DEVICES USING APPLE/ANDROID PUSH SERVICE` is set to **Enable**.                                                                                                                                                                                                                                                                                                                                                                                      | 7 seconds                                  | N/A                                                                             |
| `SMS lifetime limit`              | The time for the counters of the `DAILY USED SMS LIMIT` and `DAILY UNUSED SMS LIMIT` to accumulate the count of authentication requests per user, per application.The daily counters are reset every night at midnight UTC.                                                                                                                                                                                                                                                                                              | 1 calendar day                             | N/A                                                                             |
| `SMS pairing limit`               | The maximum number of pairing SMS messages permitted per account.                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Full license: unlimited Trial license: 100 | Top level error code: `REQUEST_FAILED`Detailed error code: `SMS_QUOTA_EXCEEDED` |

### Application settings

Application settings are configurable settings per application in the admin portal. For configuration instructions and default settings, see [Updating a PingID SDK app's configuration](pid_sdk_update_app_configuration.html).

|   |                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------- |
|   | Some of the application configurations are restricted or not configurable for tenants with trial licenses. |

---

---
title: PingID SDK application management
description: PingIDK SDK administrators can configure, update, enable, disable, and distribute settings for the application.
component: pingid
page_id: pingid:pingid_sdk:pid_sdk_application_management
canonical_url: http://docs.pingidentity.com/pingid/pingid_sdk/pid_sdk_application_management.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 30, 2024
---

# PingID SDK application management

PingIDK SDK administrators can configure, update, enable, disable, and distribute settings for the application.

PingID SDK enables developers of mobile apps on iOS or Android to include advanced multi-factor authentication (MFA) functionality that is on-brand and customizable within their mobile applications. This allows organizations to preserve their brand experience rather than force customers to download a separate MFA application.

As part of the integration of a the PingID SDK component into a customer's mobile application, the PingID SDK account administrator should create an application entry in the PingOne account.

During this process, an application ID will be generated. This application ID is used by the customer server and the customer mobile application for identification of the customer mobile application in PingID SDK.

The administrator's role in a PingID SDK application's lifecycle comprises the following activities:

* [Configuring a new PingID SDK app](pid_sdk_config_new_app.html)

  Creation of an entry for a new PingID SDK application in the admin portal with a basic default configuration.

* [Updating a PingID SDK app's configuration](pid_sdk_update_app_configuration.html)

  Configuration of an existing PingID SDK application's settings, applying changes to the default configuration, and other updates to the application's configuration, as might be required during the app's lifecycle.

* [Enabling or disabling a PingID SDK app](pid_sdk_enable_disable_app.html)

  Configuration of a PingID SDK application's enabled or disabled state.

* [Distributing the PingID SDK settings file and application ID](pid_sdk_distribute_settings_file.html)

  Retrieval of resources required for distribution to developers, in order for them to integrate the PingID SDK component into their mobile application code.

---

---
title: Running the PingID SDK Admin Activity Report
description: Run the PingID SDK Admin Activity Report from the admin portal.
component: pingid
page_id: pingid:pingid_sdk:pid_running_sdk_admin_activity_report
canonical_url: http://docs.pingidentity.com/pingid/pingid_sdk/pid_running_sdk_admin_activity_report.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 27, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
  result-2: Result:
  result-3: Result:
  pingid-admin-activity-report-fields-for-pingid-sdk: PingID Admin Activity Report fields for PingID SDK
---

# Running the PingID SDK Admin Activity Report

Run the PingID SDK Admin Activity Report from the admin portal.

## About this task

The PingID SDK admin activity report outputs detailed information regarding admin-related activity during the past week.

## Steps

1. From the admin portal, go to **Dashboard → Reporting → Reports**.

   ### Result:

   A list of pre-defined reports display.

2. Next to **PingID SDK Admin Activity of the last 7 Days**, click **Run**.

   ### Result:

   The report output is presented. For a detailed description of the report output fields, see [PingID Admin Activity Report fields for PingID SDK](pid_admin_activity_report_fields_sdk.html).

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | * You can customize the report output by adding optional field columns, removing default fields, and changing default runtime parameters, according to the steps in the generic PingOne [Run a custom report](http://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_run_custom_report.html) procedure.

   * You can stream PingID event information to Splunk or other third-party products. You can view and analyze this information when you subscribe to PingID audit events through the PingOne subscription facility. For more information, see [Subscriptions](http://docs.pingidentity.com/pingoneforenterprise/pingone_sso_for_saas_apps/p14saas_subscriptions.html) in the PingOne Admin Guide. |

3. To download the report in `.csv` format, click **Export**.

   ### Result:

   The report is saved in your browser's default downloads folder. The export process can take several minutes to complete, depending on the size of the report.

## PingID Admin Activity Report fields for PingID SDK

The PingID Admin Activity Report produces output with the following default and optional fields.

Customize the report output by adding optional field columns, removing default fields, and changing default runtime parameters. Find more information in [Run a custom report](http://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_run_custom_report.html).

| Field name        | Description                                                                                                                  | Default/Optional |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **Timestamp**     | The date and time when the admin action event occurred, according to the current time zone.                                  | Default          |
| **Admin**         | The email address, username, or LDAP name assigned to the administrator who performed the action.                            | Default          |
| **Admin Type**    | The type of administrator. This will be "user" unless the action was performed by a Ping Identity employee.                  | Default          |
| **Action**        | The type of resource and the action of the event. Possible values:- `account updated`

- `report updated`

- `user updated`  | Default          |
| **Resource Name** | The name of the resource on which the action was performed.                                                                  | Default          |
| **Resource Type** | The type of resource on which the action was performed. Possible values:- `account`

- `report`

- `user`                    | Default          |
| **Message**       | Detailed information regarding the action event, including the resource type, resource name, and nature of the admin action. | Default          |
| **Admin Id**      | The unique identifier assigned by PingOne to the administrator.                                                              | Optional         |
| **Browser Agent** | The browser name and version used for PingOne SSO.                                                                           | Optional         |
| **IP Address**    | The IP address of the host used to initiate the event.                                                                       | Optional         |
| **Resource Id**   | The unique identifier assigned by PingOne to the resource.                                                                   | Optional         |
| **Status**        | The status of the action. Possible values:- `SUCCESS`

- `FAILURE`                                                           | Optional         |

---

---
title: Supported PingID SDK adapter for PingFederate flows
description: The PingID SDK adapter for PingFederate permits the option to replace the customer server with PingFederate for pairing and authenticating a user.
component: pingid
page_id: pingid:pingid_sdk:pid_supported_pid_sdk_adapter_pf_flows
canonical_url: http://docs.pingidentity.com/pingid/pingid_sdk/pid_supported_pid_sdk_adapter_pf_flows.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 29, 2023
section_ids:
  supported-use-cases-and-flows: Supported use cases and flows
---

# Supported PingID SDK adapter for PingFederate flows

The PingID SDK adapter for PingFederate permits the option to replace the customer server with PingFederate for pairing and authenticating a user.

Administrators and developers should consider the supported flows when implementing the PingID SDK adapter for PingFederate.

![Diagram illustrating the automatic pairing flow between the PingID SDK server, PingFederate, a customer mobile application, PingID SDK component, and the user agent.](_images/dst1564020828365.png)

## Supported use cases and flows

The PingID SDK adapter for PingFederate supports the following use cases:

* Automatic device registration (web view)

  Automatic mobile device registration when a user initiates a pairing process for a mobile device.

  * This flow only supports the mobile web view. The user is authenticated as part of the PingFederate authentication flow, and after the user is successfully authenticated, control is returned to the mobile application and trust with the PingID SDK server is initiated. The adapter returns control to the mobile application.

  * This flow supports registration of mobile devices.

* Device authorization (web view)

  A seamless user sign-on to an already trusted mobile application, which includes PingID mobile SDK.

  * This flow only supports sign-on to the mobile application using mobile web view and then returns control to the mobile application.

  * This flow takes the user through the PingID SDK adapter authentication. On successful seamless device authentication, the user is signed on to the application.

* QR code authentication

  A user scanning a QR code with a trusted mobile device. The major objective of this approach is to permit secure passwordless authentication. The customer server does not need advance knowledge of who the user is. For example, first-factor authentication is not required.

  * The PingFederate PingID SDK adapter displays a QR code image in the web browser.

  * The user scans the QR code with their trusted mobile device, and the mobile application passes it back to the PingID SDK server. QR code-based authentication also supports authentication of multiple users who use the same device.

  * The PingID SDK server validates the QR code.

  * If the QR code is valid, the user is approved and authentication is completed.

  * If extra verification is required, a silent push is sent to verify the device. In addition, a user approval message can also be sent to the user for additional user confirmation.

* Out-of-band / step up authentication from web

  multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
  \<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
  \</div>)* during user sign-on to a web application.

  * Signing on through a web browser initiates PingFederate first-factor authentication. Since it is web based, no payload is sent to the PingID SDK server.

  * All of the PingID SDK authentication methods are supported: mobile SDK, SMS, voice, and email.

  * After successful first factor authentication, the adapter directs the PingID SDK server to send a push notification, SMS, voice message, or email to the authenticating device.

  * An application development design consideration would be to permit SMS, voice, and email device registration although not using PingFederate.

* Out-of -and / step up authentication from mobile

  MFA during user sign-on to a non-trusted mobile device, using the user's primary device for the approval process.

  * This flow supports pairing of new mobile devices only. Mobile, SMS, voice, and email devices can be used for approving the new device pairing.

  * The PingID SDK server sends an authentication request to the primary device, either as a push notification for a mobile device or a one-time passcode (OTP) *(tooltip: \<div class="paragraph">
    \<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>
    \</div>)* for SMS, voice, or email. The PingID SDK adapter returns a success or failure status.

  * This flow is relevant only when **Additional Trusted Devices** is configured to **Verify New Devices with Primary Device**. In cases where **Additional Trusted Devices** is configured to **Pair Each Device Individually**, the **Automatic device registration** flow is performed every time a user tries to pair an additional device.

* Transaction approval

  Transaction approval, also known as step-up authentication, is elevated security for a high-value or high-risk resource or service, within the particular context of an application. This requires authentication using a higher assurance credential than previously required for general access of the application.

In some applications, do not use the second-factor authentication capabilities during the sign-on process. Instead, activate it during certain user actions, such as a payments or bank transfers. These actions are called transaction approvals because they elevate the user's security context only when required by the business logic.

PingID SDK enables the developer to incorporate transaction approval flows and authentications into native applications quickly and easily. Transaction approvals rely on context-related information as part of the authentication. The context-related information is implemented using the dynamic parameters feature of the PingID SDK adapter for PingFederate. The native application can use it to show the transaction information or to display different behavior during the authentication.

* CIBA authenticator

  Out-of-band MFA using a trusted mobile device as a client-initiated backchannel authentication (CIBA) *(tooltip: \<div class="paragraph">
  \<p>An extension to OpenID Connect defining a new OAuth grant type where user consent can be requested and granted through an out-of-band authentication flow. CIBA uses direct relying party to OpenID provider communication without redirects through the user's browser.\</p>
  \</div>)* authenticator.

The accessing device initiates the authentication request. The authentication request is sent to a trusted mobile device for authentication, without the need for an additional redirect to PingFederate. The request is received by PingID SDK on the mobile device, and PingID SDK returns a success or failure status.

|   |                                                                 |
| - | --------------------------------------------------------------- |
|   | The PingID SDK CIBA authenticator supports mobile devices only. |

* PingFederate Authentication API

  Enables integration with the PingFederate Authentication API for end-user interactions, for step-up authentication and transaction approval. Additionally, it supports mobile device initiated flows such as mobile device registration and seamless device authorization. The PingFederate Authentication API provides access to the current state of the flow as an end user steps through a PingFederate authentication policy.

---

---
title: The PingID SDK adapter for PingFederate
description: The PingID SDK adapter for PingFederate is an out-of-the-box integration between PingID SDK and PingFederate user authentication flow and adapter chain that permits the option to replace the customer server with PingFederate.
component: pingid
page_id: pingid:pingid_sdk:pid_sdk_adapter_for_pf
canonical_url: http://docs.pingidentity.com/pingid/pingid_sdk/pid_sdk_adapter_for_pf.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 28, 2024
section_ids:
  supported-flows: Supported flows
---

# The PingID SDK adapter for PingFederate

The PingID SDK adapter for PingFederate is an out-of-the-box integration between PingID SDK and PingFederate user authentication flow and adapter chain that permits the option to replace the customer server with PingFederate.

PingID SDK is a mobile SDK for support of PingID multi-factor authentication (MFA) for customer use cases on organizations' own mobile applications. The basic implementation of PingID SDK requires the organization to set up a customer server.

![Diagram illustrating the PingID SDK paradigm flow.](_images/vqw1564020832647.png)

The PingID SDK adapter for PingFederate permits the option to replace the customer server with PingFederate in several use cases.

![Diagram illustrating the PingID SDK integration with PingFederate flow.](_images/zau1564020833420.png)

The PingID SDK adapter for PingFederate supports all of the PingID SDK authentication methods, including mobile SDK, SMS, voice, and email.

* PingID SDK adapter for PingFederate contains the `pingid.sdk.status` attribute. When an authentication flow using the PingID SDK adapter for PingFederate is successful, `pingid.sdk.status` provides additional information that can be used for determining user permission levels.

* PingID SDK adapter includes customizable pages that are presented to the user as part of the authentication flow.

## Supported flows

There are several use cases in which the PingID SDK adapter for PingFederate can replace a customer server, for the purpose of pairing and authenticating a user.

* Automatic device registration (web view)

  Automatic mobile device registration when a user initiates a pairing process for a mobile device.

* Device authorization (web view)

  Seamless user sign-on to an already trusted mobile application which includes PingID mobile SDK

* QR code authentication

  User scanning a QR code with a trusted mobile device. The major objective of this approach is to permit secure passwordless authentication. The customer server does not need advance knowledge of who the user is (for example, first factor authentication is not required).

* Out of band / step up authentication from web

  MFA during user sign-on to a web application

* Out of band / step up authentication from mobile

  MFA during user sign-on to a non trusted mobile device, using the user's primary device for the approval process.

* Transaction approval

  Elevated security for a high value or high risk resource or service, within the particular context of an application, which requires authentication using a higher assurance credential than previously required for general access of the application.

* CIBA authenticator

  Out-of-band MFA using a trusted mobile device as a Client-Initiated Backchannel Authentication (CIBA) authenticator.

* PingFederate Authentication API

  Enables integration with the PingFederate Authentication API for end-user interactions, for step-up authentication and transaction approval. Additionally, it supports mobile device initiated flows such as mobile device registration and seamless device authorization.

For more information, see [Supported PingID SDK adapter for PingFederate flows](pid_supported_pid_sdk_adapter_pf_flows.html).

---

---
title: Updating a PingID SDK app&#8217;s configuration
description: The following steps describe all the configurable options available for a PingID SDK app.
component: pingid
page_id: pingid:pingid_sdk:pid_sdk_update_app_configuration
canonical_url: http://docs.pingidentity.com/pingid/pingid_sdk/pid_sdk_update_app_configuration.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 23, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Updating a PingID SDK app's configuration

## About this task

The following steps describe all the configurable options available for a PingID SDK app.

## Steps

1. Log in to the admin web portal.

2. Select **Applications → PingID SDK Applications**.

   ![uay1564020819206](_images/uay1564020819206.png)

   If there are apps already defined for your organization, they will be listed on this page.

3. Select the **Down arrow** icon to the right of the app you want to configure, to expand the view. Click the **Pencil** icon in the right margin to edit the app's settings.

   ![vmn1569482218241](_images/vmn1569482218241.png)

4. Click the **Pencil** icon to the right of the app name, to change the name that appears in the application list.

   The system checks that there are no other apps registered for this organization with the identical name.

   ![hzn1569482832354](_images/hzn1569482832354.png)

   Select **Save** to save your changes.

5. Select the **Integration** tab to view the iOS and Android connection settings for the app. Click the **Pencil** icon in the right margin, to edit the settings.

   * **iOS**: You can upload and associate separate certificate files, for the **SANDBOX** and for **PRODUCTION**. When uploading a certificate file, a prompt appears for the **CERTIFICATE PASSWORD**. By selecting the **Eye** icon toggle, you can choose whether the password will be displayed on the screen, or masked.

   * **Android**: Both of the connection details fields, **SENDER ID** and **SERVER KEY**, may either be left blank, or both must be filled. Select **Save** to save your changes.

6. Select the **Configuration** tab to view the app's PingID configuration settings. Click the **Pencil** icon to edit the settings.

   ![tfp1564020822273](_images/tfp1564020822273.png)

   |   |                                                                      |
   | - | -------------------------------------------------------------------- |
   |   | Changes to the configuration will only take effect for new pairings. |

   1. **DEVICES**:

      ![kbl1564020822883](_images/kbl1564020822883.png)

      * **DEVICE SELECTION**:

        * **Default to Primary** is the default option for users to be automatically authenticated with their primary device.

          |   |                                                                                                                                                                                                                                                                                                                                                                                                                    |
          | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
          |   | If the user doesn't have a primary device, they will automatically be prompted with the first best fitting trusted device:- If the first device is a mobile phone, it will be regarded as the primary device.

          - If the first paired device is not a mobile phone (for example an iPad), and there is another paired device which is a mobile phone, then the mobile phone will be regarded as the primary device. |

        * **Prompt User to Select** for users to receive a prompt on each authentication to choose the device to use.

      * **MAXIMUM ALLOWED DEVICES**:

        * You may determine the **MAXIMUM ALLOWED DEVICES** that each user can have. The default value is 5, the minimum is 1, and the maximum value is 15. The user will not be able to add more devices for authentication than the maximum number that was configured. Assuming that **Prompt user to select** was chosen, this is the maximum number of devices the user will see listed, and be able to choose from, for authentication.

        * Possible error codes returned:

          * Top level error code: `REQUEST_FAILED`

          * Detailed error code: `SIZE_LIMIT_EXCEEDED`

   2. **MOBILE APP AUTHENTICATION**:

      ![bgf1613036966356](_images/bgf1613036966356.png)

      * **NEW REQUEST DURATION**:

        You can configure the amount of time that an authentication request lasts before timing out. Use this feature to customize the authentication experience to your user's needs, and reduce the number of users that experience a push notification timeout on authentication attempts.

        An authentication request's duration is determined by two configurable measurements:

        * **Device Timeout**: The amount of time in seconds that a new authentication request notification must reach a user's mobile device, before timing out.

        * **Total Timeout**: The total amount of time in seconds that a new authentication request will last, before timing out. This includes the time for **Device Timeout**, plus the time that the user has to respond to the authentication request.

        * Select **Default** to use the system's default timeout values:

          * Device timeout default: 20 seconds

          * Total timeout default: 40 seconds.

        * Select **Global** to apply a custom **Device Timeout** value and a custom **Total Timeout** value globally to all mobile application authentication requests, irrespective of where the request originated.

          |   |                                                                                                                              |
          | - | ---------------------------------------------------------------------------------------------------------------------------- |
          |   | The value in the **Total Timeout** field must be at least 15 seconds greater than the value in the **Device Timeout** field. |

          | Timeout setting | Device Timeout | Total Timeout |
          | --------------- | -------------- | ------------- |
          | Minimum         | 15 seconds     | 40 seconds    |
          | Maximum         | 40 seconds     | 150 seconds   |
          | Default         | 20 seconds     | 40 seconds    |

        * Select **Advanced** to apply individual custom **Device Timeout** and **Total Timeout** values to each origin of mobile application authentication requests.

          |   |                                                                                                                                                                                                                     |
          | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
          |   | The valid values range appears in parentheses for each origin's timeout. The value in the **Total Timeout** field must be at least 15 seconds greater than the value in its corresponding **Device Timeout** field. |

          Configure timeout values of mobile application authentication requests according to their origins:

          * **API**

            The amount of time in seconds for a new authentication request notification before timing out, for any API request that does not originate from either the CIBA Authenticator (version 1.1.2 and later) or from the PingID SDK Adapter (version 1.8.2 and later).

            | Timeout setting | Device Timeout | Total Timeout |
            | --------------- | -------------- | ------------- |
            | Minimum         | 15 seconds     | 40 seconds    |
            | Maximum         | 40 seconds     | 150 seconds   |
            | Default         | 20 seconds     | 40 seconds    |

          * **CIBA**

            The amount of time in seconds for a new authentication request notification before timing out, for any API request that originates from the CIBA Authenticator.

            |   |                                                                                                                                               |
            | - | --------------------------------------------------------------------------------------------------------------------------------------------- |
            |   | Relevant from CIBA Authenticator 1.1.2.If the CIBA Authenticator version is earlier than 1.1.2, the **API** timeout configuration is applied. |

            | Timeout setting | Device Timeout | Total Timeout |
            | --------------- | -------------- | ------------- |
            | Minimum         | 15 seconds     | 40 seconds    |
            | Maximum         | 40 seconds     | 150 seconds   |
            | Default         | 20 seconds     | 40 seconds    |

          * **SDK Adapter**

            The amount of time in seconds for a new authentication request notification before timing out, for any API request that originates from the PingID SDK Adapter for PingFederate.

            |   |                                                                                                                                 |
            | - | ------------------------------------------------------------------------------------------------------------------------------- |
            |   | Relevant from SDK Adapter 1.8.2.If the SDK Adapter version is earlier than 1.8.2, the **API** timeout configuration is applied. |

            | Timeout setting | Device Timeout | Total Timeout |
            | --------------- | -------------- | ------------- |
            | Minimum         | 15 seconds     | 40 seconds    |
            | Maximum         | 40 seconds     | 150 seconds   |
            | Default         | 20 seconds     | 40 seconds    |

          * **Extra verification silent push**

            If **Verify Devices** is enabled, you can configure the duration of the **Device Timeout** of the additional silent verification notification.

            | Timeout setting | Device Timeout |
            | --------------- | -------------- |
            | Minimum         | 3 seconds      |
            | Maximum         | 15 seconds     |
            | Default         | 7 seconds      |

          * **QR code**

            If **Verify QR Code Authentication** is enabled, you can configure the duration of the **Device Timeout** of the QR code's additional silent verification notification.

            | Timeout setting | Device Timeout |
            | --------------- | -------------- |
            | Minimum         | 1 second       |
            | Maximum         | 15 seconds     |
            | Default         | 7 seconds      |

      * **ONE-TIME PASSCODE FALLBACK**:

        * **Enable** (default): Upon mobile app response timeout, or if the device is pushless, the user will be presented with the OTP input screen, and may use OTP to authenticate.

          * **PASSCODE FAILURE LIMIT**: The maximum number of times that the OTP entry can fail for a user, before they are blocked.\
            Default: 3\
            Minimum: 1\
            Maximum: 7

          * **BLOCK DURATION**:\
            The amount of time a user's device will be blocked if they exceed the maximum number of passcode failures. The duration may be set in units of minutes or seconds.\
            Default: 2 minutes\
            Minimum: 2 minutes\
            Maximum: 30 minutes

      * **Disable**:\
        Upon mobile app response timeout, the user will not be able to authenticate using OTP as an alternative.

        |   |                                                                                                                                                                                                                                                           |
        | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        |   | Customized **PASSCODE FAILURE LIMIT** and **BLOCK DURATION** values are not saved when **ONE-TIME PASSCODE FALLBACK** is set to **Disable**. The next time it is enabled, these configurable settings initial values will be reset to the system default. |

   3. **MOBILE APPLICATION SDK**:

      ![pcr1564020824117](_images/pcr1564020824117.png)

      * **PAIRING KEY LIFETIME**: Set the duration of validity in minutes, hours or days for a manual pairing key, before it expires. The default is 48 hours, and the maximum is 31 days.

        * Possible status or error returned:

          * Top level error code: `NOT_FOUND`

      * **QR CODE AUTHENTICATION**:

        * **URL PREFIX**: Provide the application's URI prefix (URL or URI scheme), to which a user will be directed after successfully scanning the QR code or clicking the deep link.

          * The **URL PREFIX** must conform to the following requirements:

            * A string of up to 30 characters starting with an English character (a-z)

            * Subsequent characters may comprise only English alphanumerics (a-z, 0-9), the plus (+), minus (-) or dot(.) characters.

          * The resulting URL will have the format `[URL PREFIX]://pingidsdk?authentication_token=[generated_token]`. For example, if the Moderno application scheme (**URL PREFIX**) is "moderno", the resulting URL is: `moderno://pingidsdk?authentication_token=[generated_token]`.

          * If the **URL PREFIX** is not specified, the QR code content is only the generated token, and the resulting URL has the format: `pingidsdk?authentication_token=[generated_token]`. In this case, the user must use the camera from within the application.

          * When using the mobile browser, it is logical that this scheme should display the resulting URL as a deep link instead of the QR code. In such a case, when the user clicks the link, they will be navigated to the app specified in the application scheme. If the application scheme is not configured, the deep link won't work.

      * **USE PUSH NOTIFICATIONS**:

        * **VERIFY DEVICES**: Select **Enable** to use the Apple or Android push server to provide extra verification during device authorization. This is the default setting.

        * **VERIFY QR CODE AUTHENTICATION**: Select **Enable** to use the Apple or Android push server to provide extra verification during QR code based authentication. This is the default setting.

      * **DEVICE REQUIREMENTS**:

        ![kdr1569394818945](_images/kdr1569394818945.png)

        * **ROOTED OR JAILBROKEN DEVICES**:

          |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
          | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
          |   | Root and jailbroken devices detection can be invoked for applications built with:- PingID Mobile SDK for Android 1.4 and later

          - PingID Mobile SDK for iOS 1.4 and later**iOS only**: We recommend using PingID Mobile SDK for iOS 1.6.1 or later. When the check for jailbroken devices is activated, applications using PingID Mobile SDK for iOS versions before 1.6.1 for authentication are regarded as missing the required data to determine whether the device is jailbroken. Those requests proceed according to the **FALLBACK RESPONSE** configuration. |

          The default setting is **Ignore**.\
          Select **Enforce** to check integrity of devices as part of the MFA flow, and detect rooted or jailbroken devices. Click **Show Advanced Configuration** to configure the following parameters:

          * **IOS**: The PingID SDK integrity check solution uses its proprietary algorithm to determine if an iOS mobile device is jailbroken.

            * **Ignore** jailbreak detection for iOS devices.

            * Select **Enforce** to check the integrity of iOS devices and to detect jailbroken iOS devices (default).

          * **Android**: The PingID SDK root detection solution utilizes Google's SafetyNet attestation API to determine the integrity of Android mobile devices.\
            See Google's documentation for further information about SafetyNet integrity levels: <https://developer.android.com/training/safetynet/attestation.html#potential-integrity-verdicts>

            * **Ignore** root detection for Android devices.

            * Select **Require SafetyNet Basic Integrity** for the basic integrity check.

            * Select **Require SafetyNet CTS** to return a verdict for the more stringent Compatibility Test Suite standard (default).

          * **ANDROID SETTINGS**: Configurable when **Require SafetyNet Basic Integrity** or **Require SafetyNet CTS** are selected.

            * **CACHE DURATION**: Since SafetyNet is an external service provided by Google, every attestation request entails a certain time tradeoff. You may choose to cache successful SafetyNet calls for a predefined duration, between a minimum of 1 minute and a maximum of 48 hours.

              |   |                                                                                                                                  |
              | - | -------------------------------------------------------------------------------------------------------------------------------- |
              |   | Reducing this period once it has already been set, may cause users to fail MFA authentications, forcing them to re-authenticate. |

            * **SAFETYNET FALLBACK RESPONSE** Determine if PingID SDK should consider a failed SafetyNet response as a rooted or non-rooted device. Following an Android device's pairing or authentication request, determine whether the request will be granted, if SafetyNet doesn't respond in time, or if Google Play is not installed on the device:

              * **Deny** the Android device's pairing or authentication request. This is the default setting.

              * **Approve** the Android device's pairing or authentication request.

          * **FALLBACK RESPONSE**: Determine PingID SDK's behavior when an authentication or pairing request is missing the required data to determine the requesting device's integrity.\
            This could occur in apps using old mobile SDK component versions, or in apps using a new mobile component versions that call the root detection API with a false flag. The **Approve** setting may assist in a gradual rollout of the integrity check to all users.\
            Following an Android or iOS device's pairing or authentication request, determine whether the request will be granted, if the rooted or jailbroken status of the device can't be determined:

            * **Deny** the device's pairing or authentication request. This is the default setting.

            * **Approve** the device's pairing or authentication request.

   4. **ALTERNATE AUTHENTICATION METHODS**:

      ![vbl1575277889135](_images/vbl1575277889135.png)

      * **EMAIL**:\
        The default setting is **Disable**.\
        Select **Enable** to permit users to authenticate via email. When **EMAIL** is selected, a one time passcode will be sent to the user's email address.

        |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
        | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        |   | PingID SDK supports use of your organization's own trusted email domains and email addresses, using the PingID SDK APIs. This reinforces trust from the customer and also from the receiving servers. The APIs provide a further option to configure DKIM and SPF verification for outbound emails. In the PingID SDK developer's guide, see:- [Trusted email domains](https://apidocs.pingidentity.com/pingid-sdk/guide/server-api/pid_c_SDKapiEmailDomains/)

        - [Trusted email addresses](https://apidocs.pingidentity.com/pingid-sdk/guide/server-api/pid_c_SDKapiEmailAddress/)

        - [Email templates](https://apidocs.pingidentity.com/pingid-sdk/guide/server-api/pid_c_SDKapiEmailTemplates/)

        - [Authenticate with email](https://apidocs.pingidentity.com/pingid-sdk/guide/server-api/pid_c_SDKemailDevicesAuthenticate/) |

      * **SMS**:\
        The default setting is **Disable**.\
        Select **Enable** to permit users to authenticate via SMS. The **SMS & VOICE** daily limits configuration options appear.

      * **VOICE**:\
        The default setting is **Disable**.\
        Select **Enable** to permit users to authenticate via VOICE. The **SMS & VOICE** daily limits configuration options appear.

      * **SMS and VOICE daily limits**:

        When SMS or VOICE are selected, admins have the option to configure the daily limit for users' SMS and VOICE authentications:

        * **DAILY USED SMS/VOICE LIMIT: 1-50:** (default = 15).

          Configure the maximum combined number of SMS and VOICE authentication requests a user may receive and respond to each day.

          * Possible status or error returned:

            * Top level error code: `INVALID_REQUEST`

            * Detailed error code: `SMS_QUOTA_EXCEEDED`

        * **DAILY UNUSED SMS/VOICE LIMIT: 1-50:** (default = 10).

          Configure the maximum combined number of SMS and VOICE authentication requests a user may receive and not respond to each day.

          * Possible error codes returned:

            * Top level error code: `REQUEST_FAILED`

            * Detailed error code: `SMS_QUOTA_EXCEEDED`

      * **PASSCODE FAILURE LIMIT**, **BLOCK DURATION** and **PASSCODE LIFETIME IN MINUTES** for EMAIL, SMS and VOICE:

        When at least one of EMAIL, SMS or VOICE is enabled, admins have the option to configure the permitted number of OTP attempt failures before a user is blocked, the duration of the block, or the duration of an OTP.

        * **PASSCODE SETTINGS**:

          * **General**:\
            Admins can configure a single **PASSCODE FAILURE LIMIT**, **BLOCK DURATION** and **PASSCODE LIFETIME IN MINUTES**, which will apply equally to all of the enabled EMAIL, SMS and VOICE options.

            ![vbl1575277889135](_images/vbl1575277889135.png)

          * **Advanced**:\
            Admins can configure a separate individual **PASSCODE FAILURE LIMIT**, **BLOCK DURATION** and **PASSCODE LIFETIME IN MINUTES** for each of the enabled EMAIL, SMS and VOICE options.

            ![gif1575278791542](_images/gif1575278791542.png)

          * **PASSCODE FAILURE LIMIT**:\
            The maximum number of times that the OTP entry can fail for a user, before they are blocked.\
            Default: 3\
            Minimum: 1\
            Maximum: 7\
            After reaching the maximum number of failure attempts, the flow ends and the exits the OTP entry screen.

          * **BLOCK DURATION**:\
            The amount of time a user's device will be blocked if they exceed the maximum number of passcode failures. The duration may be set in units of minutes or seconds.\
            Default: 0 minutes (not blocked)\
            Minimum: 0 minutes\
            Maximum: 30 minutes

          * **PASSCODE LIFETIME IN MINUTES**:\
            The amount of time an OTP is valid before it expires.\
            The duration may be set in units of minutes.\
            Default: 30 minutes\
            Minimum: 1 minute\
            Maximum: 30 minutes

          * **Authentication** scenarios:\
            All of the **PASSCODE FAILURE LIMIT**, **PASSCODE LIFETIME IN MINUTES** and **BLOCK DURATION** settings apply for authentication attempts.

          * **Pairing** scenarios:\
            Only the **PASSCODE FAILURE LIMIT** and the **PASSCODE LIFETIME IN MINUTES** apply for pairing attempts, whereas **BLOCK DURATION** does not apply.

          * When switching configurations between the **General** and **Advanced** modes, only the current mode's **PASSCODE FAILURE LIMIT**, **BLOCK DURATION** and **PASSCODE LIFETIME IN MINUTES** settings are saved. Switching back to the other mode will not reinstate its previously saved configuration, but rather, it will reset back to its default values.

            |   |                                                                                                                                                                                                                                                                                                                                                     |
            | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
            |   | Customized parameter values such as **PASSCODE FAILURE LIMIT**, **BLOCK DURATION** and **PASSCODE LIFETIME IN MINUTES** are not saved for the specific **EMAIL**, **SMS** or **VOICE** feature, if that feature is set to **Disable**. The next time it is enabled, these configurable settings initial values will be reset to the system default. |

            |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
            | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
            |   | **Dedicated SMS and VOICE subaccounts**:PingID SDK supports a dedicated subaccount for pairing and authentication with SMS and VOICE one time passcodes (OTPs). You can determine the amount of dedicated phone numbers and the country-code from which the SMS and VOICE messages will be sent to the users.For further details and to activate subaccounts, contact Ping Support.- Note that if you wish to delete a subaccount's dedicated number, users associated with the deleted number will receive their OTP messages from one of the PingID primary account's assigned numbers for 2 minutes until completion of the deletion process. Once the deletion process is complete, they will receive their OTP messages from one of the subaccount's remaining numbers. |

7. Select **Save** to save your changes.

8. In the **Applications → PingID SDK Applications** list, select the gray/green toggle to the right of your app to **Enable** or **Disable** it.

   ![uay1564020819206](_images/uay1564020819206.png)

---

---
title: Using a custom Syniverse account with PingID SDK
description: If you have an existing custom Syniverse account, you can configure PingID SDK to use it for SMS or voice pairing and authentication.
component: pingid
page_id: pingid:pingid_sdk:pid_using_custom_syniverse_account_with_pid_sdk
canonical_url: http://docs.pingidentity.com/pingid/pingid_sdk/pid_using_custom_syniverse_account_with_pid_sdk.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 2, 2024
---

# Using a custom Syniverse account with PingID SDK

If you have an existing custom Syniverse account, you can configure PingID SDK to use it for SMS or voice pairing and authentication.

Keep the following points in mind:

* **Daily used SMS/Voice limits:**

  * **PingOne full licence accounts:** The daily SMS and Voice limits are enforced for fully licensed PingOne accounts that use a custom Syniverse account.

  * **PingOne trial accounts:** The daily SMS and Voice limits are not enforced for PingOne trial accounts that use a custom Syniverse account.

* **Billing:** Your Syniverse billing arrangements must be setup before you can configure PingID SDK to use your account.

* **Multiple Syniverse accounts:** If you have more than one Syniverse account, you can only use one of them.

* **Inactive Syniverse accounts:**It is the administrator's responsibility to delete a Syniverse account configuration in PingID SDK, if the account becomes inactive. See [Managing a Syniverse account for PingID SDK](pid_managing_syniverse_account_pid_sdk.html) for deleting a custom Syniverse account from PingID SDK.

To configure a custom Syniverse account go to [Configuring a Syniverse account for PingID SDK](pid_configuring_syniverse_account_for_sdk.html).

To manage a custom Syniverse account go to [Managing a Syniverse account for PingID SDK](pid_managing_syniverse_account_pid_sdk.html).

---

---
title: Using a custom Twilio account with PingID SDK
description: If you have an existing custom Twilio account, you can configure PingID SDK to use it for SMS or voice pairing and authentication.
component: pingid
page_id: pingid:pingid_sdk:pid_using_custom_twilio_account_pid_sdk
canonical_url: http://docs.pingidentity.com/pingid/pingid_sdk/pid_using_custom_twilio_account_pid_sdk.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 30, 2024
---

# Using a custom Twilio account with PingID SDK

If you have an existing custom Twilio account, you can configure PingID SDK to use it for SMS or voice pairing and authentication.

Keep the following points in mind:

* Daily used SMS/voice limits

  * PingOne full license accounts - The daily SMS and voice limits are enforced for fully licensed PingOne accounts that use a custom Twilio account.

  * PingOne trial accounts - The daily SMS and voice limits are not enforced for PingOne trial accounts that use a custom Twilio account.

* Billing

  You must set up your Twilio billing arrangements before you can configure PingID SDK to use your Twilio account.

* Multiple Twilio accounts

  If you have more than one Twilio account, you can only use one of them. If you have Twilio subaccounts, you can use either:

  * The main account

  * A single subaccount of the main account

|   |                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------- |
|   | Configuring a custom Twilio account overrides a PingID SDK subaccount if a PingID SDK subaccount is configured. |

* Inactive Twilio accounts

  It is the administrator's responsibility to delete a Twilio account configuration in PingID SDK if the account becomes inactive. For more information on deleting a custom Twilio account from PingID SDK, see [Managing a Twilio account for PingID SDK](pid_managing_twilio_account_for_sdk.html).