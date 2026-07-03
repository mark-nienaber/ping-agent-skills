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
