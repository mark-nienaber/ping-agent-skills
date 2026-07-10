---
title: Creating a credential
description: Define the information in PingOne that you want to collect from your customer and customize the look and feel of your credential.
component: pingone
page_id: pingone:digital_credentials_using_pingone_credentials:p1_credentials_creating_a_credential
canonical_url: https://docs.pingidentity.com/pingone/digital_credentials_using_pingone_credentials/p1_credentials_creating_a_credential.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 2, 2025
section_ids:
  about-this-task: About this task
  before-you-begin: Before you begin
  steps: Steps
  result: Result:
  choose-from: Choose from:
---

# Creating a credential

Define the information that you want to collect from your customer and customize the look and feel of your credential.

## About this task

* Customize a credential: Add a background, icon, and customize fonts and colors to create a credential with the branding that your customers know and trust.

* Customize data collection: Add directory attributes, date of issuance, or create alphanumeric text fields to capture more specific customer data. Specify which details appear on the credential and which details are collected as metadata only.

## Before you begin

* Add PingOne Credentials to your environment.

* (Optional) Add PingID to your environment to add PingID as a digital wallet.

  You can add PingOne Credentials or PingID with a [Workforce solution](../getting_started_with_pingone/p1_trial_workforce_solution.html) or [build your own solution](../getting_started_with_pingone/p1_building_solutions.html). Learn more in [Adding a new environment](../pingone_tutorials/p1_tutorial_config_mfa_experience_add_environment.html) and [Building solutions](../getting_started_with_pingone/p1_building_solutions.html).

* (Optional) Create a native [application](../applications/p1_application_types.html) to have an existing digital wallet to add to the credential. You can also wait to add a digital wallet during configuration.

## Steps

1. In the PingOne admin console, go to **Digital Credentials > Schemas**.

   ### Result:

   The **Credentials** page opens, showing a list of existing credentials.

   ![A screen capture of the credentials window. From here you have the option to create, edit, and issue a credential.](_images/p1_credentials_schemas.png)

2. Click the **[icon: plus, set=fa]**icon.

   The **Add Credential** panel opens.

3. For **Overview**:

   * Enter a **Credential Type** to identify the type of credential required for verification.

     |   |                                              |
     | - | -------------------------------------------- |
     |   | This value doesn't appear on the credential. |

   * Enter a user-friendly **Credential Name** to display on the credential.

4. In the **Fields** section, configure the data to store in the credential:

   * In the **Data Type** list, select an attribute.

   * In the **Field Title**, enter a field title to display on your credential.

   * To add a field, click **[icon: plus, set=fa]Add Field**.

   * To make a field required, select the checkbox.

     |   |                                              |
     | - | -------------------------------------------- |
     |   | Only required fields appear on the card SVG. |

   * To remove a field, click the **Delete** icon ([icon: trash, set=fa]).

5. In the **Issuance Rules** section, choose how often credentials are issued, updated, and revoked:

   * Click **Automatic** to automatically update credentials every 2 minutes in response to PingOne directory changes.

   * Click **Manual** to manually update credentials through API calls for immediate changes.

6. Click **Next**.

7. For **Issuance**, grant the credential to users:

   ### Choose from:

   * Select **Populations** to choose a population that you want to issue credentials to.

   * Select **Groups** to choose a group that you want to issue credentials to.

     |   |                                                                                                                                      |
     | - | ------------------------------------------------------------------------------------------------------------------------------------ |
     |   | If you select multiple groups or populations, a user has to be a member of at least one of those selected to be issued a credential. |

   * Select **Custom** to create a filter that identifies a certain category of users to automatically issue credentials based on attributes from the PingOne Directory.

     1. Enter the first condition:

        * **Attribute**: Select an attribute.

        * **Operator**: Select **Equals**, **Starts with**, **Ends with**, or **Contains**.

        * **Value**: Enter the appropriate value.

     2. (Optional) Click **+ Add**, and then click **Condition** to add another condition or **Condition Set** to add a set of conditions.

     3. Select **All** or **Any** to determine how the linked conditions will be evaluated.

     4. To delete a condition, click [icon: trash, set=fa].

   ![A screen capture of issuance rules.](_images/issuancecred.png)

8. Click **Next**.

9. For **Digital Wallet**, browse or search for the application you want to use.

   |   |                                                                                                                                                                               |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can only select one wallet.To manage existing digital wallets, edit your native applications on the [Applications](../applications/p1_edit_application_native.html) page. |

   * To add a PingID digital wallet, browse or search for the **PingID** wallet you want to use.

   * To add a new wallet, click **[icon: plus, set=fa]Add Wallet** and configure the following:

     * **Wallet Name**: Name of the digital wallet.

     * **Operating System**: Select **IOS**, **Android**, or both, and configure the following:

       | Operating system | Configuration                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
       | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
       | **IOS**          | **Bundle ID**: A unique identifier assigned to an iOS app, essential for configuring app-specific notifications and services.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
       | **Android**      | * **Google Play Services**: JSON key files generated in the Google Cloud Console that contain authentication details for a service account.

         * **Package Name**: A unique identifier for an Android app, structured like a reversed domain name ( com.example.app) required for configuring push notifications using Firebase Cloud Messaging (FCM).

       * **Huwei Mobile Services**: An alternative mobile services platform to Google Play Services, used for devices running on Huawei's ecosystem.

         * **Package Name** (Android): A unique identifier for an Android app, structured like a reversed domain name (com.example.app) required for configuring push notifications using Firebase Cloud Messaging (FCM).

         * **App ID**: The unique identifier for the app on the device and in the Huwei Mobile AppGallery. |

   * **Digital Wallet Link**: The mobile app URL for the wallet. Allows users to access their wallet from another app, such as through a browser or email, by clicking a URL link or scanning a QR Code.

   * To clear the selected wallet, click another wallet of your choice or click **No Selection**.

     ![A screen capture of digit wallet.](_images/digitalwallet.png)

10. Click **Next**.

11. (Optional) For **Style Credential**, style how the credential will appear in the PingID wallet:

    |   |                                                                                             |
    | - | ------------------------------------------------------------------------------------------- |
    |   | As you set configurations, the **Credential View** and **Wallet View** update in real time. |

    * To add a logo, click the image under **Logo** and select the image file that you want to use.

      |   |                                         |
      | - | --------------------------------------- |
      |   | Logo images must be smaller than 25 KB. |

    * To delete a logo, hover over the logo image, click the **Camera** icon ([icon: camera, set=fa]), and click **Remove Image** or **Upload New Image**.

    * Select the **Background Color** and **Font Color** of your credential using the color picker or by entering an RGB value.

    * Enter a display name to add a **Title** and **Subtitle**.

    * Select up to three **Data Fields** to display on the credential.

      * To change the order in which the credential attributes are displayed, select a different data field.

      * To display a data field, click **Show label**.

        ![A screen capture of the style PingID credential page.](_images/stylecredential.png)

12. Click **Save**.

13. To enable the credential, click the toggle on the **Credentials** page to the right (blue).

---

---
title: Credential management method comparison
description: The PingOne Credentials service offers Automated and API credential management options.
component: pingone
page_id: pingone:digital_credentials_using_pingone_credentials:p1_credentials_management_method_comparison
canonical_url: https://docs.pingidentity.com/pingone/digital_credentials_using_pingone_credentials/p1_credentials_management_method_comparison.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 29, 2024
---

# Credential management method comparison

The PingOne Credentials service offers Automated and API credential management options.

Automated credential management relies on the PingOne platform to automatically issue, edit, and revoke credentials. For example, if you configure a credential to issue to everyone in your PingOne population, a new user added to the PingOne directory automatically receives a credential. If a user is removed from the population, the credential is revoked. Learn more in [Creating a credential](p1_credentials_creating_a_credential.html).

API credential management uses the Credential APIs to issue, edit, and revoke credentials. API credential management requires you to set up listeners to respond to lifecycle events that happen in their external data source to know when to take the appropriate action on the user credential. Learn more about [User Credentials](https://developer.pingidentity.com/pingone-api/credentials/user-credentials.html) in the API documentation.

|                                 | Definition                                                                                                                             | Integration                                                                                        | Pros                                                                                                                         | Cons                                                                                                                                             | Choose if                                                                              |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------- |
| Automated credential management | Automatically handles interactions between the directory of PingOne and the credential service to issue, edit, or revoke a credential. | Low integration level.Data sync is required to use attributes stored outside of PingOne Directory. | Automated credential management eliminates implementation complexity. PingOne takes care of all credential lifecycle events. | * Personal identifiable information (PII) is stored in PingOne.

* Not suited if you have strict data residency or on-prem data residency needs. | You rely on the PingOne platform as your system of record.                             |
| API credential management       | Uses APIs to issue, edit, or revoke a credential.                                                                                      | Complex integration level                                                                          | Personal identifiable information (PII) is not stored in PingOne or subject to data residency concerns.                      | - More complex integration.

- Credential lifecycle policy logic is the responsibility of the customer to maintain.                              | You have strict data residency requirements or existing data stores outside of PingOne |

---

---
title: Customizing PingOne Credentials notification templates
description: Customize notification templates for PingOne Credentials notifications that end users receive.
component: pingone
page_id: pingone:digital_credentials_using_pingone_credentials:p1_credentials_customizing_notification_templates
canonical_url: https://docs.pingidentity.com/pingone/digital_credentials_using_pingone_credentials/p1_credentials_customizing_notification_templates.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 29, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  example: Example:
---

# Customizing PingOne Credentials notification templates

Customize notification templates for PingOne Credentials notifications that end users receive.

## Before you begin

You must have PingOne MFA in your environment.

|   |                                                          |
| - | -------------------------------------------------------- |
|   | PingOne MFA provides the default notification templates. |

## About this task

PingOne Credentials notifications include:

* Credential Issued

  Notifications to end users when a credential is issued.

* Credential Revoked

  Notifications to end users when a credential is revoked.

* Credential Updated

  Notifications to end users when a credential is updated.

* Digital Wallet Pairing

  Notifications to end users to set up and pair a digital wallet app for storing credentials.

For more information about notification templates, see [Notification templates](../user_experience/p1_notifications.html) and [Editing a notification](../user_experience/p1_edit_notification.html).

To customize notification templates for the notifications that groups or populations receive:

## Steps

1. Go to **User Experience → Notification Templates**.

![A screen capture of notification templates showing different types of existing templates.](_images/yyj1678731436094.png)

1. Click the **More Options (⋮)** icon for the notification template you want to customize.

2. Click **Edit**.

3. To edit a notification detail, click the **Pencil** icon for the field you want to edit.

   ### Example:

   For the **Digital Wallet Pairing** template, click the **Pencil** icon for the **New Email** field and enter a custom message, such as `To set up your BX Insurance Digital Wallet, click on this link to download and set up the app.`

   ![A screen capture of Digital Wallet Pairing notification templates New Email edits.](_images/fiy1678749986399.png)

4. Click the **Checkmark** icon to save your changes.

---

---
title: Digital Credentials using PingOne Credentials
description: The PingOne Credentials service allows an issuer to create verifiable credentials that they can send to a compatible wallet app.
component: pingone
page_id: pingone:digital_credentials_using_pingone_credentials:p1_credentials_start
canonical_url: https://docs.pingidentity.com/pingone/digital_credentials_using_pingone_credentials/p1_credentials_start.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 30, 2025
section_ids:
  getting-started: Getting started
  integrations-and-connectors: Integrations and connectors
  developer-resources: Developer resources
---

# Digital Credentials using PingOne Credentials

The PingOne Credentials service allows an issuer to create verifiable credentials that they can send to a compatible wallet app.

## Getting started

* [What is PingOne Credentials?](p1_credentials_introduction.html)

* [Get started with PingOne Credentials](p1_credentials_getting_started.html)

* [Developing and registering the wallet app that runs the PingOne wallet native SDK^](p1_credentials_getting_started.html#neo_sdk)

* [PingOne Credentials scenarios](p1_credentials_scenario_intro.html)

* [Customizing PingOne Credentials notification templates](p1_credentials_customizing_notification_templates.html)

* [Creating a credential](p1_credentials_creating_a_credential.html)

* [Editing a credential](p1_credentials_editing_a_credential.html)

* [Revoking credentials](p1_credentials_revoking_a_credential.html)

## Integrations and connectors

* [Ping Identity Marketplace: PingOne Credentials](https://marketplace.pingone.com/browse?products=credentials)

* [PingOne Credentials Connector](https://docs.pingidentity.com/connectors/p1_credentials_connector.html)

## Developer resources

* [Get started with PingOne APIs](https://developer.pingidentity.com/pingone-api/getting-started/introduction.html)

* [PingOne wallet native SDK](https://developer.pingidentity.com/pingone-api/native-sdks/pingone-neo-native-sdks/pingone-wallet-native-sdks.html)

* [PingOne Credentials](https://developer.pingidentity.com/pingone-api/credentials/introduction.html)

* [Credential issuers](https://developer.pingidentity.com/pingone-api/credentials/credential-profiles.html)

---

---
title: Editing a credential
description: Edit the look and feel of your credential in PingOne, the recipients of the credential, and the digital wallet.
component: pingone
page_id: pingone:digital_credentials_using_pingone_credentials:p1_credentials_editing_a_credential
canonical_url: https://docs.pingidentity.com/pingone/digital_credentials_using_pingone_credentials/p1_credentials_editing_a_credential.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 2, 2025
section_ids:
  steps: Steps
  result: Result:
---

# Editing a credential

Edit the look and feel of your credential, the recipients of the credential, and the digital wallet.

## Steps

1. In the PingOne admin console, go to **Digital Credentials > Schemas**.

   ### Result:

   The **Credentials** page opens, showing a list of existing credentials.

2. For the credential you want to edit, click the credential and then click the **Pencil** icon ([icon: pencil, set=fa]) in the relevant section.

3. Edit any of the following:

   * On the **Profile** tab:

     * For **Style Credential**, edit the style of how the credential will appear in the PingID wallet:

       |   |                                                                                             |
       | - | ------------------------------------------------------------------------------------------- |
       |   | As you set configurations, the **Credential View** and **Wallet View** update in real time. |

       * To add or update logo, click the image under **Logo** and select the image file that you want to use.

         |   |                                         |
         | - | --------------------------------------- |
         |   | Logo images must be smaller than 25 KB. |

       * To delete a logo, hover over the logo image, click the **Camera** icon ([icon: camera, set=fa]), and click **Remove Image** or **Upload New Image**.

       * To update or edit the **Background Color** and **Font Color** of your credential, use the color picker or by entering an RGB value.

       * Enter a **Title** and **Subtitle**.

       * Select up to three **Data Fields** to display on the credential.

         * To change the order in which the credential attributes are displayed, select a different data field.

         * To display a data field, click **Show label**.

     * For **Overview**:

       * Enter a **Credential Type** to identify the type of credential required for verification.

         |   |                                              |
         | - | -------------------------------------------- |
         |   | This value doesn't appear on the credential. |

       * Enter a user-friendly **Credential Name** to display on the credential.

     * For **Fields**, configure the data to store in the credential:

       * In the **Data Type** list, select an attribute.

       * In the **Field Title**, enter a field title to display on your credential.

       * To add a field, click **[icon: plus, set=fa]Add Field**.

       * To make a field required, select the checkbox.

         |   |                                              |
         | - | -------------------------------------------- |
         |   | Only required fields appear on the card SVG. |

       * To remove a field, click the **Delete** icon [icon: trash, set=fa].

     * For **Issuance Rules**, choose how often credentials are issued, updated, and revoked:

       * Click **Automatic** to automatically update credentials every 2 minutes in response to PingOne directory changes.

       * Click **Manual** to manually update credentials through API calls for immediate changes.

   * On the **Wallets** tab:

     |   |                                                                                                                                                                               |
     | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | You can only select one wallet.To manage existing digital wallets, edit your native applications on the [Applications](../applications/p1_edit_application_native.html) page. |

     * To select a wallet, browse or search for the wallet you want to use.

     * To add a wallet, configure the following:

       | Operating system | Configuration                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
       | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
       | **IOS**          | **Bundle ID**: A unique identifier assigned to an iOS app, essential for configuring app-specific notifications and services.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
       | **Android**      | * **Google Play Services**: JSON key files generated in the Google Cloud Console that contain authentication details for a service account.

         * **Package Name**: A unique identifier for an Android app, structured like a reversed domain name ( com.example.app) required for configuring push notifications using Firebase Cloud Messaging (FCM).

       * **Huwei Mobile Services**: An alternative mobile services platform to Google Play Services, used for devices running on Huawei's ecosystem.

         * **Package Name** (Android): A unique identifier for an Android app, structured like a reversed domain name (com.example.app) required for configuring push notifications using Firebase Cloud Messaging (FCM).

         * **App ID**: The unique identifier for the app on the device and in the Huwei Mobile AppGallery. |

     * To clear the selected wallet, click another wallet of your choice or click **No Wallet**.

   * On the **Population**, **Group**, or **Custom** tab, edit the recipient of the credential by selecting one of the following:

     * **Groups**: Choose a group to issue the credential to.

     * **Populations**: Choose a population to issue the credential to.

     * **Custom**: Create a filter that identifies a category of users to issue the credential to:

       * Select an **Attribute** and **Operator**, and enter a **Value**.

         You can find a full list of operators and supported attributes in [SCIM operators](https://developer.pingidentity.com/pingone-api/platform/users/users-1.html#users-scim-operators) in the PingOne API documentation.

       * To add a new attribute, click **[icon: plus, set=fa]Add** and select **Condition** or **Condition Set**.

       * Click **All** or **Any** to determine how to filter using your attributes.

       * To delete a condition, click [icon: trash, set=fa].

4. Click **Update**.

---

---
title: Getting started with PingOne Credentials
description: Learn how to get started with PingOne Credentials.
component: pingone
page_id: pingone:digital_credentials_using_pingone_credentials:p1_credentials_getting_started
canonical_url: https://docs.pingidentity.com/pingone/digital_credentials_using_pingone_credentials/p1_credentials_getting_started.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 23, 2025
page_aliases: ["p1_credentials_creating_registering_neo_sdk.adoc"]
section_ids:
  before-you-begin: Before you begin
  neo_sdk: Developing and registering the wallet app that runs the PingOne wallet native SDK
  about-this-task: About this task
  steps: Steps
  result: Result:
  result-2: Result:
---

# Getting started with PingOne Credentials

Learn how to get started with PingOne Credentials.

To try out issuance and verification demos for PingOne Credentials, learn more in [PingOne Credentials issuance](https://auth.pingone.com/851e6ca2-7400-49b6-8c24-707ffc2be5ba/davinci/policy/c7eb99d991615349a5a119e69f332d75/authorize?client_id=09df0479f79681a4eaf5879a5c83c633\&response_type=code\&scope=openid\&redirect_uri=https://auth.pingone.com/851e6ca2-7400-49b6-8c24-707ffc2be5ba/davinci/testrp) and [PingOne Credentials verification test](https://auth.pingone.com/851e6ca2-7400-49b6-8c24-707ffc2be5ba/davinci/policy/ad3dcfea4bddcfae3faaf24b05898e1a/authorize?client_id=33fe69dc2d19ad2c238cad3e123d5261\&response_type=code\&scope=openid\&redirect_uri=https://auth.pingone.com/851e6ca2-7400-49b6-8c24-707ffc2be5ba/davinci/testrp).

|   |                                       |
| - | ------------------------------------- |
|   | These demos don't require any set up. |

## Before you begin

**To get started with and access PingOne Credentials, you must have:**

* A PingOne account. Learn more in [Starting a PingOne trial](../getting_started_with_pingone/p1_start_a_p1_trial.html).

* An environment with a workforce solution that includes PingOne Credentials, PingID, and DaVinci. Learn more in [Building solutions](../getting_started_with_pingone/p1_building_solutions.html).

* The PingID mobile app.

  |   |                                                                                                                                                                                                                                            |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | For native integration, use the SDK. Learn more in [PingOne wallet native SDK](https://developer.pingidentity.com/pingone-api/native-sdks/pingone-neo-native-sdks/pingone-wallet-native-sdks.html) in the PingOne developer documentation. |

**To set up PingID as your digital wallet, you must have:**

* The PingID mobile app.

* A new environment with a workforce solution. Learn more in [Building solutions](../getting_started_with_pingone/p1_building_solutions.html).

  ![A screen capture of the Create Environment page with Workforce solution selected.](_images/workforce.png)

* The PingOne Credentials and DaVinci service in your environment.

  ![A screen capture of PingOne Credentials service selected.](_images/addcredservice.png)

* A credential. Learn more in [Creating a credential](p1_credentials_creating_a_credential.html). For compatibility with the DaVinci flows used for testing, the **Issue**, **Update**, and **Revoke** issuance rules should be set to **Periodic**, and the PingOne Credentials fields must include the following attributes:

  * **Name - Given Name**

  * **Name - Family Name**

  * **Title**

* PingID selected as your wallet. Learn more in [Creating a credential](p1_credentials_creating_a_credential.html).

  ![ A screen capture of the PingID digital wallet selected.](_images/pingid.png)

**To test pairing PingID and issuing a credential, you must:**

1. Download the [DaVinci flow - Setup a User Digital Wallet](https://marketplace.pingone.com/item/pingone-neo-starter-flow-setup-a-user-digital-wallet).

2. Import the flow using the instructions on how to import a flow in [How to create a flow](https://docs.pingidentity.com/davinci/flows/davinci_how_to_create_a_flow.html) in the DaVinci documentation.

3. Launch the flow.

**To test verifying a credential, you must:**

1. Download the [DaVinci flow - Verifiable Credential Presentation Request](https://marketplace.pingone.com/item/pingone-neo-starter-flow-verifiable-credential-presentation-request).

2. Import the flow using the instructions on how to import a flow in [How to create a flow](https://docs.pingidentity.com/davinci/flows/davinci_how_to_create_a_flow.html) in the DaVinci documentation.

3. Launch the flow.

## Developing and registering the wallet app that runs the PingOne wallet native SDK

### About this task

The mobile app guides the user through the process of accepting and sharing credentials. Each user is invited to install and pair their digital wallet by installing a customer-developed app running the SDK.

### Steps

1. Develop an app (for iOS or Android) that runs the SDK, or embed the SDK into an existing app.

   Learn more in [PingOne wallet native SDK](https://developer.pingidentity.com/pingone-api/native-sdks/pingone-neo-native-sdks/pingone-wallet-native-sdks.html) in the PingOne developer documentation.

2. In the PingOne admin console, create a PingOne application to register your wallet app:

   1. Go to **Applications > Applications**.

   2. Click the **[icon: plus, set=fa]**icon.

      #### Result:

      The **Add Application** panel opens.

   3. Enter the appropriate **Application Name** and **Description**.

   4. In the **Application Type** section, click **Native**.

   5. Click **Save**.

      #### Result:

   The details panel opens.

3. To configure the app, on the **Mobile** tab, click the **Pencil** icon:

   1. Click **Configure for Android** to configure the app for Android and provide the **Package Name** for Google Play Services or the **Package Name** and **App ID** for Huawei Mobile Services.

   2. Click **Configure for iOS** to configure the app for iOS and provide the **Bundle ID**, as registered in the app store.

   ![Screen capture of the application details panel which the admin can choose to configure.](_images/peo1678922238012.png)

4. **Optional:** To allow push notifications, click **[icon: plus, set=fa]Add Push Notifications**:

   1. For Android apps that use Google Play Services, enter a **Server Key**, as provided by FCM.

   2. For Android apps that use Huawei Mobile Services, enter a **OAuth 2.0 Client ID** and **Client Secret**.

   3. For iOS, enter the **Team ID**, **Select a file** for the**Authentication Token Signing Key**, and enter the **Key ID**, as provided by Apple to your organization.

5. In the **Settings** section:

   1. To turn on **Device Integrity Check**, click **On** to prevent the use of compromised devices for pairing or authentication.

   You can enable device integrity checking separately for Google play Services and iOS.

   1. Adjust the **Cache Duration**, the last device integrity check will be cached for a minimum of 1 minute or a maximum 48 hours.

   2. If your organization is using the PingOne MFA SDK to allow authentication with a QR code in certain flows, provide the relevant **Universal / App Link** or URI scheme that the application should use for this purpose, depending on which deep-linking mechanism the app developers used.

   3. Use the **Passcode Refresh Duration** field to specify the amount of time a passcode should be displayed before it's replaced with a new passcode.

   4. To turn on **Configuration for Credentials Digital Wallet link**, click **On**, and enter a **Digital Wallet Link**. The **Digital Wallet Link** value should match the value defined in the customer's application.

      The **Digital Wallet Link** is used to create pairing links and QR codes that open the customer application. This link can be the same as the **Universal / App Link** or a different one to help distinguish between links for MFA and links for credentials.

      |   |                                                                                                                                   |
      | - | --------------------------------------------------------------------------------------------------------------------------------- |
      |   | The **Package Name**, **App ID**, **Bundle ID**, and push notification settings can't be modified after you save the application. |

6. Click **Save.**

   |   |                                                                                                  |
   | - | ------------------------------------------------------------------------------------------------ |
   |   | To enable or disable your application in PingOne, click the toggle on the **Applications** page. |

---

---
title: Introduction to PingOne Credentials
description: PingOne Credentials is a service that allows issuers to customize and issue verifiable digital credentials that users can store in their wallet, eliminating cost and management of issuing physical credentials.
component: pingone
page_id: pingone:digital_credentials_using_pingone_credentials:p1_credentials_introduction
canonical_url: https://docs.pingidentity.com/pingone/digital_credentials_using_pingone_credentials/p1_credentials_introduction.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 25, 2024
section_ids:
  how-pingone-credentials-works: How PingOne Credentials works
  users-download-a-compatible-wallet-app-and-create-a-digital-identity-profile: "Users: Download a compatible wallet app and create a digital identity profile"
  issuers-create-and-issue-a-new-credential-in-pingone-credentials: "Issuers: Create and issue a new credential in PingOne Credentials"
  verifiers-verifying-a-credential: "Verifiers: Verifying a credential"
  pingone-credentials-example: PingOne Credentials example
---

# Introduction to PingOne Credentials

PingOne Credentials is a service that allows issuers to customize and issue verifiable digital credentials that users can store in their wallet, eliminating cost and management of issuing physical credentials.

The three parties that enable decentralized identity are:

* Issuer

  The proprietor and issuer of official sources of data, such as college transcripts, vaccination status, or employment history.

* Verifier

  Any individual or institution (service provider) with which a user chooses to share data that requires verification, such as sharing a driver license as proof of age or credit card information when applying for a loan.

* User

  An individual who matches the issuance rule of a group, population, or SCIM filter with a PingOne Credentials profile. Users can receive credentials from issuers, store them securely in their compatible wallet app, and use it to share their credentials with verifiers.

![Illustration showing examples of issues, such as universities, credit bureaus, and vaccine providers, verifiers, such as businesses, healthcare providers, and other individuals, with the user at the center, using the compatible wallet app to receive credentials from issuers, store them securely in the wallet app, and share details with verifiers.](_images/oqv1679005014232.jpg)

Issuers and verifiers can be any entity that the user engages with, such as a university, an insurance company, employer, health provider, or a financial institution.

Users that need to receive or provide proof of a credential to these institutions might already have a record of their activity with that institution, which won't change. However, if the user needs to share that record with another entity, traditionally they must allow the other entity (a verifier) to contact the original institution (the issuer) to get the information and confirm that it's valid. This can be cumbersome, expensive, and time-consuming and could violate the user's privacy if not managed properly.

Using decentralized identity, it's possible for an issuer, such as a university or employer, to provide a verifiable credential about the user's qualifications or employment to the user in the form of a digital credential that the user can store in their compatible wallet app. Because the credential is always with the user, the user can share that information with the new business to seek employment. The potential employer can verify the data for its authenticity in real-time without contacting the issuer, so there's no further friction or exposure of privacy.

The issuer creates a credential in PingOne Credentials using the automated issuance rules that automatically issues a verifiable credential to all users who match a provided filter. The filter is based on Groups, Populations, or a SCIM filter. The issuer can also define individual fields on the credential in the form of key-value pairs to provide the appropriate details for the service credential they are offering to their users.

Credential details will vary according to the industry and the specific credentials the issuer wants to offer. For example, in addition to name and date of birth, an insurance company might want to provide the type of insurance, policy number, and expiry date. A bank might want to include the bank account number and date of issue, and a university might want to include the type of degree obtained.

![Screen capture showing an example of a credential for a finance company.](_images/jug1678888718741.jpg)

The PingOne Credentials service maintains a unique private-key for each issuer within the PingOne environment. It uses the PingOne wallet native SDK to allow creation of verifiable credentials in the backend.

To simplify the creation and issuance of credentials, PingOne Credentials wraps the API calls in a more consumable and user-friendly interface within the PingOne administrator console. This service also provides APIs that allow customers to interact programmatically and with additional customizations.

Credentials issued by this service can be shared:

* With other users through a compatible wallet app

* With custom QR codes that can be generated with the API calls

The following diagram shows examples of three different issuers, providing credentials to an individual user and the various ways a user can provide information to verifiers using these credentials:

* A medical provider issues a primary provider credential that includes details of the provider, date of last vaccination, and personal medical details. The user stores the certificate as a credential in their compatible wallet app. When a blood drive event requests proof of a primary care provider, the user can send it to them without providing all of the personal details it contains.

* A car insurer provides an insurance policy as a credential to a user. Credentials might include the user's ID, date of birth, and medical status, but when a car rental service asks for the user's insurance policy, the user can share just the policy number and expiry date.

* A university provides a degree certificate as a credential to the user. The user stores the credential in their compatible wallet app. The user can provide a potential employer with the full degree certificate (as well as any other qualifications their wallet app holds) immediately.

  ![Illustration showing examples of issuers, verifiers and user's digital wallet app.](_images/qou1679004159439.jpg)

PingOne Credentials, along with a compatible wallet app, makes this verifiable exchange of data possible. You can use PingOne Credentials through the PingOne unified administrator console or through its API.

## How PingOne Credentials works

### Users: Download a compatible wallet app and create a digital identity profile

Each user is invited to install and pair their digital wallet by installing a customer-developed app running the [PingOne Neo SDK](https://developer.pingidentity.com/pingone-api/native-sdks/pingone-neo-native-sdks.html). An email or SMS notification can be sent to the user with a link that takes the users to a customer site that helps them install the customer app.

After the app is installed, clicking on the link prompts the user to complete digital wallet pairing. The SDK shares the application instance ID with PingOne Credentials and that is stored for future issued or revoked credentials.

### Issuers: Create and issue a new credential in PingOne Credentials

* Creating a credential

  ![Image showing an example of a credential.](_images/mqv1678889684027.jpg)

In PingOne Credentials, an issuer creates a new custom credential. A credential defines the field attributes required to issue a credential, the fields displayed on the credential, and an identifying logo and relevant branding. The field values can be supplied by the issuer or taken partly from both the issuer and the user, such as their selfie and verified first and last name.

|   |                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------- |
|   | The credential can be used to issue a credential to any group or population listed in PingOne Credentials. |

* Issuing a credential to a user

  1. The issuer creates a credential and uses the issuance rule to select a group, population, or uses a System for Cross-domain Identity Management (SCIM) *(tooltip: \<div class="paragraph">
     \<p>An application-level, HTTP-based protocol for provisioning and managing user identity information. SCIM supplies a common schema for representing users and groups and provides a REST API.\</p>
     \</div>)* filter to issue the credential to.

  2. Credentials are automatically sent to a user who is a part of the issuance rule to their digital wallet.

  3. If a user doesn't have a digital wallet, a message is sent to invite the user to download the app.

  4. After downloading the app, the digital wallet is paired.

  5. When the user accepts the credential, it's stored in their wallet app and can be shared with verifiers that request proof of a credential from a user.

* Revoking a credential

  An issuer can revoke a user's credentials remotely from PingOne Credentials. This ensures that wallet app credentials held by a user are always up-to-date.

Based on the issuance rule, revoking happens automatically for users if a directory attribute changes. For example, if a user is removed from the group, population, or SCIM filter, their credentials are revoked.

After a user's credential is revoked, if a user attempts to share credential data with a verifier, the verifier will see that the data is no longer valid by the issuer. The issuer can always reissue the credential to the user if necessary.

### Verifiers: Verifying a credential

When asked for proof of a credential, such as age, valid license, or insurance, the user can share some or all of the information on a credential with a verifier. If the user approves a verifier's request, the user's compatible wallet app shares the specific data and the signed certifications with the verifier.

The verifier can then independently assert the validity of the data by checking whether the credential's digital signatures matches the issuer's public-key. This is done without requiring the verifier to communicate with the issuer directly. This creates a greater level of privacy for the user because the issuer never becomes aware of the user's interaction with the verifier. Additionally, the transaction can be done in real time.

## PingOne Credentials example

As an issuer, BX Insurance Company, wants to issue a car insurance policy as a credential to their customers (users) digitally. They want to include the customer's picture, driver license ID, car insurance policy number, and the expiration date for the insurance policy.

The insurance company creates a credential in PingOne Credentials that includes the company logo, company branding, and all of the fields that they require for the type of insurance that they're issuing.

![An image showing an example of a credential for an insurance company](_images/vkd1678925529262.jpg)

They use the credential to issue insurance policy digital credentials that the user stores in their compatible wallet app.

If the user wants to rent a car, they can share digital insurance credential details with the car rental company. Likewise, if the user is involved in a traffic accident, they can share details with the other driver (verifiers) to prove that they have insurance and to verify that their policy is valid.

If the user's insurance coverage stops before the expiration date specified during issuance, such as because of a lack of payment that renders the insurance invalid, BX Insurance Company can revoke the credential given to the user in real-time.

Sharing information from a digital wallet gives the verifiers the additional assurance that the information is up-to-date and represents the real-time status of the person's insurance, something that a paper copy can't provide.

PingOne Credentials allows BX Insurance Company to create numerous custom credentials for all the insurance policies that they want to cover, including:

* House insurance

* Health insurance

* Travel insurance

* Mortgages

After they create these credentials, they can issue them to their users.

---

---
title: Managing an issuer profile
description: Manage details about your organization and issuer profile in PingOne.
component: pingone
page_id: pingone:digital_credentials_using_pingone_credentials:p1_credentials_issuer_profile
canonical_url: https://docs.pingidentity.com/pingone/digital_credentials_using_pingone_credentials/p1_credentials_issuer_profile.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Dec 3, 2025
section_ids:
  steps: Steps
---

# Managing an issuer profile

Manage details about your organization and issuer profile of verifiable credentials.

|   |                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | We recommend setting a custom domain for your issuer details. This ensures they originate from a domain registered to your issuing authority. Learn more in [Setting up a custom domain](../settings/p1_set_up_custom_domain.html). |

## Steps

1. In the PingOne admin console, go to **Digital Credentials > Issuer Profile**.

2. Click the **Pencil** icon ([icon: pencil, set=fa]) and enter or edit the following:

   * **Issuer Name**: The name of the organization issuing the credential.

   * **Issuer Logo**: The official logo of the organization.

   * **Site URL**: The official website of the issuer.

   * **Remote Signing URL**: Endpoint used to sign credentials securely. `https://signer.customer.com/sign`

   * **Headers**: Enter the **Key**, the name of the HTTP header, and **Value**.

     |   |                                         |
     | - | --------------------------------------- |
     |   | There is a limit of 10 key-pair values. |

   * (Optional) **[icon: plus, set=fa]Add HTTP Header**: Add another HTTP header.

   * **[icon: plus, set=fa]Add Registered Key**: Add a registered key for remote signing:

     * **Key Name**: The name of the key.

     * **JSON Web Key**: The JSON for the key.

     * **Enable**: Click the toggle to enable the key.

     * Click **Save**.

     * To delete a key, click the **Delete [icon: trash, set=fa]**icon.

       |   |                                                                            |
       | - | -------------------------------------------------------------------------- |
       |   | For remote credential signing, at least one key must be added and enabled. |

3. Click **Save**.

---

---
title: PingOne Credentials scenarios
description: These scenarios provide high-level examples of how you can use PingOne Credentials.
component: pingone
page_id: pingone:digital_credentials_using_pingone_credentials:p1_credentials_scenario_intro
canonical_url: https://docs.pingidentity.com/pingone/digital_credentials_using_pingone_credentials/p1_credentials_scenario_intro.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 29, 2024
---

# PingOne Credentials scenarios

These scenarios provide high-level examples of how you can use PingOne Credentials.

The three scenarios that are covered are:

* [Creating and receiving credentials](p1_credentials_creating_credential_for_auto_issuance.html)

  Learn how a company can customize the credentials they issue to their customers and the notifications that customers receive.

* [Presenting and verifying a user credential](p1_credentials_scenario_present_verify_cred.html)

  Learn how a user can provide proof of credentials to a provider of service (in this case, proof of insurance to a car rental company) and how the provider of service can then verify the user's credentials.

* [Revoking a credential and notifying a user](p1_credentials_scenario_revoke_cred_notify_user.html)

  Learn how credentials can be revoked from a user's digital wallet app and how users can be notified that the credential was revoked. This scenario also covers how a user's credentials can be reissued.

---

---
title: Revoking a credential
description: "You can revoke a credential in PingOne if it's no longer valid."
component: pingone
page_id: pingone:digital_credentials_using_pingone_credentials:p1_credentials_revoking_a_credential
canonical_url: https://docs.pingidentity.com/pingone/digital_credentials_using_pingone_credentials/p1_credentials_revoking_a_credential.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 2, 2025
section_ids:
  steps: Steps
  choose-from: Choose from:
  result: Result
---

# Revoking a credential

You can revoke a credential if it's no longer valid and should be removed.

To revoke a credential, you change the issuance rule or SCIM filter. You can either remove or change the group, population, or custom filter so that the user doesn't match anymore. You can also revoke a credential from a user in the **Users** page. Learn more in [Managing a user's credentials](../directory/p1_manage_user_credentials.html).

|   |                                                   |
| - | ------------------------------------------------- |
|   | You can only delete a credential through the API. |

To revoke credentials in PingOne Credentials:

## Steps

1. In the PingOne admin console, go to **Digital Credentials > Schemas**.

2. Click the relevant credential to open the details panel.

3. In the **Population**, **Group**, or **Custom** tab, click the **Pencil** icon ([icon: pencil, set=fa])

   ### Choose from:

   * Select **Populations** and in the **Selected Populations** tab, click the population to revoke credentials.

   * Select **Groups** and in the **Selected Groups** tab, click the group to revoke credentials.

   * Select **Custom** and delete or edit conditions as needed to revoke permissions based on different criteria.

4. Click **Update**.

## Result

Credentials for users no longer meeting the criteria are revoked.

---

---
title: "Scenario: Creating and receiving a credential"
description: In this scenario, a car insurance company, BX Insurance (the issuer) wants to customize an email invitation for digital wallet pairing and create a digital credential they can issue to their customer, John Smith (a user). Afterward, (in a second scenario) John is notified, downloads the digital wallet app, and receives the credential.
component: pingone
page_id: pingone:digital_credentials_using_pingone_credentials:p1_credentials_creating_credential_for_auto_issuance
canonical_url: https://docs.pingidentity.com/pingone/digital_credentials_using_pingone_credentials/p1_credentials_creating_credential_for_auto_issuance.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 29, 2024
section_ids:
  scenario-participants: Scenario participants
  assumptions: Assumptions
  scenario: Scenario
---

# Scenario: Creating and receiving a credential

In this scenario, a car insurance company, BX Insurance (the issuer) wants to customize an email invitation for digital wallet pairing and create a digital credential they can issue to their customer, John Smith (a user). Afterward, (in a second scenario) John is notified, downloads the digital wallet app, and receives the credential.

## Scenario participants

The following parties are involved in this scenario:

* Credential Issuer

  BX Insurance

* User

  John Smith

## Assumptions

BX Insurance (the credential issuer) meets the following requirements:

* PingOne Credentials, and PingOne MFA are available in the BX Insurance PingOne environment.

* BX Insurance has a group in their environment named **Current auto insurance subscribers**, and John Smith is a member of that group.

  For more information about creating a group, see [Creating a group](../directory/p1_create_group.html).

* A mobile developer for BX Insurance has developed and registered an app that runs the SDK.

* A native application connection added in the BX Insurance environment registered the wallet app.

  You can find more information about developing a sample app that runs the SDK and adding a native application connection to register the wallet app in [PingOne wallet native SDK](https://developer.pingidentity.com/pingone-api/native-sdks/pingone-neo-native-sdks/pingone-wallet-native-sdks.html).

## Scenario

![Creating and issuing a credential flow](_images/njh1680289114412.png)

1. BX Insurance customizes an email invitation with the BX Insurance name with the text **To set up your BX Insurance Digital Wallet, click this link to download and set up the app**.

2. They create a new credential with the following attributes:

   * First and last name

   * Date of birth

   * Car insurance policy ID number

   * Policy expiration date

3. They select the group **Current auto insurance subscribers**, which John Smith is a part of, to issue the credential to.

4. They select the digital wallet application, save the credential, and then enable it, automatically sending the credential to John Smith.

5. John Smith receives the email invitation on his phone containing a link that says **To set up your BX Insurance Digital Wallet, click this link to download and set up the app**.

6. After clicking the link, he's redirected to the BX Insurance company app in the app store.

7. After he installs the app, the message `Please confirm to pair your wallet to receive a credential` appears.

8. John is presented the option to **Cancel** or **Confirm**.

9. After he taps **Confirm**, the BX Insurance credential is accepted and appears in his digital wallet.

---

---
title: "Scenario: Presenting and verifying a user credential"
description: In this scenario, John Smith (the user) wants to reserve a car from BX Rental Cars (the credential verification service) for his vacation next month. Before he can complete the reservation, BX Rental Cars requires that John provide proof that he has a car insurance policy that will be valid throughout the rental period.
component: pingone
page_id: pingone:digital_credentials_using_pingone_credentials:p1_credentials_scenario_present_verify_cred
canonical_url: https://docs.pingidentity.com/pingone/digital_credentials_using_pingone_credentials/p1_credentials_scenario_present_verify_cred.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 29, 2024
section_ids:
  scenario-participants: Scenario participants
  assumptions: Assumptions
  scenario: Scenario
---

# Scenario: Presenting and verifying a user credential

In this scenario, John Smith (the user) wants to reserve a car from BX Rental Cars ([the credential verification service](https://developer.pingidentity.com/pingone-api/credentials/credential-verifications.html)) for his vacation next month. Before he can complete the reservation, BX Rental Cars requires that John provide proof that he has a car insurance policy that will be valid throughout the rental period.

## Scenario participants

The following parties are involved in this scenario:

* Credential issuer

  BX Insurance

* User

  John Smith

* Provider of a service

  BX Rental Cars

* Verifier service

  The service BX Insurance contracts with for credential verification

## Assumptions

BX Insurance (the credential issuer) meets the following requirements:

* PingOne Credentials and PingOne MFA are available in the BX Insurance PingOne environment.

* They created a credential type for the user data required to issue the credential. The credential type includes a connection to a digital wallet app that users can install and use to store their personal credentials.

  For more information about creating a credentials template, see [Creating a credential](p1_credentials_creating_a_credential.html).

* BX Insurance customized the following credentials-related notification templates to inform users about the ongoing status of their credentials:

  * Digital Wallet Pairing

  * Credential Issued

  * Credential Revoked

  * Credential Updated

  For more information about notification templates, see [Notification Templates](../user_experience/p1_notifications.html).

Additionally, John Smith has previously received his credential from BX Insurance, and it is stored in a compatible digital wallet app on his phone. For more information, see [Scenario: Creating and receiving a credential](p1_credentials_creating_credential_for_auto_issuance.html).

## Scenario

![Presenting and verifying credential flow](_images/dki1680284300903.png)

1. John visits the **Reservations** page of the BX Rental Cars website from his computer and starts a reservation request.

2. An API call is made from the website to the verifier service BX Rental Cars uses. This creates a new verification session and provides a QR code that BX Rental Cars displays on the screen for John to scan.

3. Using the wallet app on his phone, John scans the QR code.

4. Depending on how the wallet app is configured, John is authenticated by the app.

5. John sees that BX Rental Cars requires the following attributes from his BX Insurance credential:

   * First and last name

   * Date of birth

   * Car insurance policy ID number

   * Policy expiration date

6. Using the app, John agrees to share this data with BX Rental Cars.

7. The verifier service receives the credential, and checks the validity of the data using the public key that BX Insurance uploaded to the Verifiable Data Registry in PingOne Credentials.

8. After the data is verified, the data is delivered to the BX Rental Cars reservation site, and, meeting all of the requirements, John is permitted to complete his rental car reservation.

---

---
title: "Scenario: Revoking a credential and notifying the user"
description: In this scenario, John Smith (the user) decided he had a good experience with BX Rental Cars (the credential verification service) on his previous trip over the summer, and decides to rent with them again when he visits his family over the holidays. However, he missed both a notice from BX Insurance (the credential issuer) prompting him to renew his auto insurance and a later notification in his wallet app that his credential was revoked. He no longer has an active auto policy.
component: pingone
page_id: pingone:digital_credentials_using_pingone_credentials:p1_credentials_scenario_revoke_cred_notify_user
canonical_url: https://docs.pingidentity.com/pingone/digital_credentials_using_pingone_credentials/p1_credentials_scenario_revoke_cred_notify_user.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 29, 2024
section_ids:
  scenario-participants: Scenario participants
  assumptions: Assumptions
  scenario: Scenario
---

# Scenario: Revoking a credential and notifying the user

In this scenario, John Smith (the user) decided he had a good experience with BX Rental Cars ([the credential verification service](https://developer.pingidentity.com/pingone-api/credentials/credential-verifications.html)) on his previous trip over the summer, and decides to rent with them again when he visits his family over the holidays. However, he missed both a notice from BX Insurance (the credential issuer) prompting him to renew his auto insurance and a later notification in his wallet app that his credential was revoked. He no longer has an active auto policy.

## Scenario participants

The following parties are involved in this scenario:

* Credential issuer

  BX Insurance

* User

  John Smith

* Provider of a service

  BX Rental Cars

* Verifier service

  The service BX Insurance contracts with for credential verification

## Assumptions

BX Insurance meets the following requirements:

* PingOne Credentials and PingOne MFA are available in the BX Insurance PingOne environment.

* They created a credential type for the user data required to issue the credential. The credential type includes a connection to a digital wallet app that users can install and use to store their personal credentials.

  For more information about creating a credential type, see [Creating a credential](p1_credentials_creating_a_credential.html).

* The issuance rules for the credential type require that the user belong to the "Active Policy" group in PingOne. Membership in that group requires that the user's auto insurance policy is not expired.

  For more information about groups, see [Groups](../directory/p1_groups.html).

* BX Insurance customized the Credential Revoked notification template to inform users when their credentials are revoked.

  For more information about notification templates, see [Notification Templates](../user_experience/p1_notifications.html).

## Scenario

![Revoking and notifying user credential flow](_images/klx1680284800034.png)

1. John visits the **Reservations** page of the BX Rental Cars website from his computer and starts his new reservation request.

2. An API call is made from the website to the verifier service BX Rental Cars uses. This creates a new verification session and provides a QR code that BX Rental Cars displays on the screen for John to scan.

3. Using the wallet app on his phone, John scans the QR code.

4. Depending on how the wallet app is configured, John is authenticated by the app.

5. John sees a notification that his credential from BX Insurance was revoked. When John did not renew his auto policy, he was removed from the "Active Policy" group, invalidating his credential. He cannot complete his reservation.

6. John calls his BX Insurance agent, renews his policy, and pays for his policy extension.

7. After John's policy data updates, John is re-added to the "Active Policy" group and his credential from BX Insurance is reissued.

8. After receiving the updated credential and saving it to his wallet app, John returns to BX Rental Cars reservation site and is able to complete the reservation process.

For more information about revoking credentials, see [Revoking a credential](p1_credentials_revoking_a_credential.html).