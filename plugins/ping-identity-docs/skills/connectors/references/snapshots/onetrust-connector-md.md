---
title: OneTrust Connector
description: The OneTrust connector lets you use OneTrust to manage receipts for user consent in your PingOne DaVinci flow.
component: connectors
page_id: connectors::onetrust_connector
canonical_url: https://docs.pingidentity.com/connectors/onetrust_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 19, 2024
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  setting-up-onetrust-consent-management: Setting up OneTrust consent management
  configuring-the-onetrust-connector: Configuring the OneTrust connector
  connector-configuration: Connector configuration
  client-id: Client ID
  client-secret: Client Secret
  setting-up-pingone: Setting up PingOne
  setting-up-onetrust-url-variables-in-davinci: Setting up OneTrust URL variables in DaVinci
  using-the-connector-in-a-flow: Using the connector in a flow
  creating-a-consent-receipt: Creating a consent receipt
  getting-information-about-an-existing-consent-receipt: Getting information about an existing consent receipt
  capabilities: Capabilities
  createConsentReceipt: Create Consent Receipt
  getReceiptInformation: Get Receipt Information
---

# OneTrust Connector

The OneTrust connector lets you use OneTrust to manage receipts for user consent in your PingOne DaVinci flow.

Using OneTrust as part of your user privacy and data governance solution, this connector lets you track whether a user has consented to a specific document, such as your terms and conditions. Specifically, the connector can create a consent receipt or get an existing consent receipt.

## Setup

### Resources

Learn more in the following:

* OneTrust documentation (sign on required)

  * [Consent Management](https://my.onetrust.com/s/topic/0TO3q000000kIWOGA2/consent-management)

  * [Managing OAuth 2.0 Client Credentials](https://my.onetrust.com/s/article/UUID-3faa8a9f-7635-bcda-5184-c01a157c3132)

  * [Managing OAuth 2.0 API Keys](https://my.onetrust.com/s/article/UUID-76f55697-ba16-d000-849a-d33e3d217f41)

* DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need a OneTrust license.

### Setting up OneTrust consent management

1. Set up consent management in OneTrust as shown in [Consent Management](https://my.onetrust.com/s/topic/0TO3q000000kIWOGA2/consent-management).

   For your Collection Point, use the following settings:

   * Choose the **Custom API** type.

   * On the **Collection Points > *\<your collection point>* > Settings** tab, turn on **Enable Consent Withheld Transactions on this Collection Point**.

2. Create client credentials as shown in [Managing OAuth 2.0 Client Credentials](https://my.onetrust.com/s/article/UUID-3faa8a9f-7635-bcda-5184-c01a157c3132), with the following settings:

   * **Access Token Lifetime**: **1 hour**

   * **Restrict IP Addresses**: **Off**

   * **Scopes**:

     * **CONSENT**

     * **CONSENT\_READ**

       Note your client ID and secret. You'll use them to set up the connector configuration.

### Configuring the OneTrust connector

Add the connector in DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

##### Client ID

The client ID you created in [Setting up OneTrust consent management](#setting-up-onetrust-consent-management).

##### Client Secret

The client secret you created in [Setting up OneTrust consent management](#setting-up-onetrust-consent-management).

### Setting up PingOne

The example flows below use the PingOne user directory to store consent receipts. To use the provided flow templates:

1. If you don't have an existing PingOne connection in DaVinci, set up the [PingOne Connector](p1_connector.html), including the required PingOne setup.

2. In PingOne, add a user attribute to hold a list of the user's consent receipts. Learn more in [Adding user attributes](https://docs.pingidentity.com/pingone/directory/p1_adduserattributes.html). Use the following details:

   * **Attribute Type**: **JSON**

   * **Name**: `consentReceipts`

   * Select **Allow multiple values**

### Setting up OneTrust URL variables in DaVinci

The flow templates provided below use variables to populate your organization's OneTrust URLs.

To use the flow templates, set the following variables in DaVinci.

|   |                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Learn more in [Adding a variable](https://docs.pingidentity.com/davinci/variables/davinci_adding_a_variable.html) in the DaVinci documentation. |

| Name                          | Variable Context | Data Type   | Example Value                                       |
| ----------------------------- | ---------------- | ----------- | --------------------------------------------------- |
| `oneTrustPrivacyPortalDomain` | **string**       | **company** | https\://*yourorganization*-privacy.my.onetrust.com |
| `oneTrustApplicationDomain`   | **string**       | **company** | https\://*yourorganization*.my.onetrust.com         |
| `oneTrustDataSubjectPortal`   | **string**       | **company** | https\://*yourorganization*-privacy.my.onetrust.com |

## Using the connector in a flow

### Creating a consent receipt

![A screen capture of the complete consent receipt creation flow.](_images/connector-images/dvc-onetrust-consent-receipt-creation-flow.png)

This flow collects the user's consent and user ID, checks that the user account exists, and sends the consent and user information to OneTrust. After OneTrust generates a consent receipt, the flow adds the new receipt to the user's list of existing receipts and updates the user account in include::partial$common\_product\_keydefs.adoc\[tags=pingone].

|   |                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This flow uses include::partial$common\_product\_keydefs.adoc\[tags=pingone]as an example user directory. You can modify the flow to use a different directory. |

1. Download the [OneTrust - New consent receipt](https://marketplace.pingone.com/item/onetrust-consent-receipt-retrieval) flow template. Learn more in [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html).

2. Customize the consent form:

   1. Select the **Consent Form** node.

   2. In the **HTML Template** field, modify the HTML to include the text of the terms and conditions (or other document) that you want consent for, and modify the example form controls to show the relevant "purposes", "options", and "custom preferences" in your OneTrust consent management scheme.

      |   |                                                                                                                                                                                                                                                                                                       |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | * Click **Switch View** to display the HTML formatted with syntax highlighting.

      * Click the **Maximize** ([icon: expand, set=fas]) icon to give yourself more room to work.

      * To access a variety of useful tools, right-click the field when you're in syntax highlighting mode (dark background). |

   3. In the **Output Fields List** section, edit the **Property Name** of the purposes, options, and custom preferences to match the element IDs of the purposes and options you included in the HTML form. Remove any unwanted properties by clicking **Edit** at the end of the list.

   4. Click **Apply**.

3. Add the IDs for your OneTrust purposes, options, and custom preferences.

   |   |                                                                                                                                                                                                             |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The flow uses a custom function to match the consent form inputs with the IDs of your OneTrust consent management elements. The function then builds a `purposes` object that is ready to send to OneTrust. |

   1. In OneTrust, get the `id` value for each purpose, option, and custom preference you want to use:

      1. Go to the OneTrust **Universal Consent & Preference Management** portal. For example, `https://company.my.onetrust.com/consent`.

      2. For purposes, go to **Purposes > *\<your purpose>* > Details > Purpose ID**.

      3. For custom preferences, go to **Purposes > *\<your purpose>* > Custom Preferences > ID**. Also, go to **Options** and note the options listed.

      4. For options, go to **Collection Points > *\<your collection point>* > Integrations > Example Payload**. Match the IDs under `Options` with the options that you noted in the **Custom Preferences** view.

         ![A screen capture of the example payload IDs matched up with a screen capture of the options from the Custom Preferences view.](_images/connector-images/dvc-onetrust-example-payload-ids.jpg)

   2. Select the **Combine Form Results** node.

   3. In the **Variable Input List** section, edit the **Variable Name** of the purposes, options, and custom preferences to match the **Property Name** in your **Consent Form** node. In the **Value** field, click **{}** and select the matching variable from your **Consent Form** node. Remove any unwanted properties by clicking **Edit** at the end of the list.

   4. In the **Code** field, modify the code to use the name and ID of your own purposes, options, and custom preferences and remove unused elements.

   5. Click **Apply**.

4. Configure the **OneTrust** node:

   1. Select the **OneTrust** node.

   2. In the **API Token** field, enter the API token from **Collection Points > Integrations > Your API Token** in OneTrust.

   3. Modify the **Additional Data Elements** list to reflect the data elements you included when configuring your collection point in OneTrust. For a list of data elements, go to **Collection Points > Details > Configuration > Data Elements**.

   4. Click **Apply**.

5. Test the flow:

   1. Click **Save**, **Deploy**, then **Run**.

   2. On the consent form, enter the email address for one of the identities in your include::partial$common\_product\_keydefs.adoc\[tags=pingone] directory, select the purposes, options, and custom preferences, then click **I Agree**.

   3. Read the resulting consent receipt, including the receipt ID.

      ![A screen capture of the Consent Result page.](_images/connector-images/dvc-onetrust-consent-result.jpg)

      |   |                                                                                                                                           |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Note the value of `x-onetrust-receiptId`. You'll use this to test the "Get information about an existing consent receipt" use case below. |

### Getting information about an existing consent receipt

![A screen capture of the complete get receipt flow.](_images/connector-images/dvc-onetrust-get-recipt-flow.png)

You can use a receipt ID to check for an existing consent receipt in OneTrust. This allows you to check whether a user has consented to your terms before using your service, for example.

1. Download the [OneTrust - Consent receipt retrieval](https://marketplace.pingone.com/item/onetrust-consent-receipt-retrieval) flow template. Learn more in [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html).

2. Test the flow:

   1. Click **Save**, **Deploy**, then **Run**.

   2. In the **Enter Receipt ID** form, enter the receipt ID that you copied from your test run of the **Creating a consent receipt** flow. Click **Next**.

      ![A screen capture of the Enter Receipt ID form.](_images/connector-images/dvc-onetrust-enter-receipt-id-form.jpg)

   3. The receipt information displays.

      ![A screen capture of the Receipt Information page.](_images/connector-images/dvc-onetrust-receipt-information-page.jpg)

## Capabilities

### Create Consent Receipt

Create Receipt from a Collection Point

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Privacy Portal Domain textField required
>
>   The URL of your OneTrust Privacy Portal, such as "https\://company-privacy.my.onetrust.com".
>
> - API Token textField required
>
>   Your OneTrust API token.
>
> - User Identifier textField required
>
>   The unique identifier for the user, such as a username or user ID.
>
> - Additional Data Elements keyValueList
>
>   Additional information collected about the user.
>
> - Purposes textField required
>
>   The flow variable that contains the "purposes" to associate with the consent.
>
> * default object
>
>   * properties object
>
>     * privacyPortalDomain string required
>
>       Data Subject Portal Domain
>
>     * apiToken string required
>
>       API Token
>
>     * userIdentifier string required
>
>       User identifier
>
>     * dataElements array required
>
>       Data Elements
>
>     * purposes string required
>
> - output object
>
>   * rawResponse object
>
>     * access\_token string
>
>     * refresh\_token string
>
>     * id\_token string
>
>     * token\_type string
>
>     * expires\_at number
>
>   * statusCode number
>
>   * headers object
>
>   * claims object
>
>     * moc string
>
>     * sub string
>
>     * attachments
>
>     * notes
>
>     * syncGroup
>
>     * iss
>
>     * language
>
>     * processVersion number
>
>     * enableParentPrimaryIdentifiers boolean
>
>     * authenticationRequired boolean
>
>     * dynamicCollectionPoint boolean
>
>     * processId string
>
>     * dsDataElements array
>
>     * doubleOptIn boolean
>
>     * consentType string
>
>     * additionalIdentifiers object
>
>     * iat string
>
>     * customPayload
>
>     * jti string
>
>     * policy\_uri
>
>     * identifier string
>
>     * parentPrimaryIdentifiersType
>
>     * gacString
>
>     * tcStringV2
>
>     * reconfirmActivePurpose boolean
>
>     * allowNotGivenConsents boolean
>
>     * notices array
>
>     * isAnonymous boolean
>
>     * multipleIdentifierTypes boolean
>
>     * purposes array
>
>     * tenantId string
>
>     * overrideActivePurpose boolean
>
>     * parentPrimaryIdentifiers array
>
>     * otJwtVersion number
>
>     * enableGeolocation boolean

### Get Receipt Information

Get Receipt Information

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Application Domain textField required
>
>   The URL of your OneTrust domain, such as "https\://company.my.onetrust.com".
>
> - Receipt ID textField required
>
>   The flow variable that contains the unique identifier for the consent receipt.
>
> - Include "Consent Not Given" Transactions toggleSwitch
>
>   When enabled, OneTrust returns results for transactions where the user did not provide consent.
>
> * default object
>
>   * properties object
>
>     * applicationDomain string required
>
>       Application Domain
>
>     * clientId string required
>
>       Client ID
>
>     * clientSecret string required
>
>       Client Secret
>
>     * receiptId string required
>
>       Receipt ID
>
>     * includeNotGiven boolean required
>
>       Include Not Given Transactions
>
> - output object
>
>   * collectionPointName string
>
>   * attributes object
>
>   * collectionPointType string
>
>   * collectionPointUUID string
>
>   * collectionPointVersion number
>
>   * consentCreationDate string
>
>   * customPayload string
>
>   * dataSubjectIdentifier string
>
>   * dataSubjectIdentifierHash string
>
>   * doubleOptIn boolean
>
>   * unsubscribeAll boolean
>
>   * id string
>
>   * interactionDate string
>
>   * isAnonymous boolean
>
>   * language string
>
>   * origin string
>
>   * otJwtVersion number
>
>   * purposes array
>
>   * receiptJwt string
>
>   * test boolean
