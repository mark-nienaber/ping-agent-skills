---
title: Socure Connector
description: The Socure connector lets you verify identity documents and get fraud scores in your PingOne DaVinci flows.
component: connectors
page_id: connectors::socure_connector
canonical_url: https://docs.pingidentity.com/connectors/socure_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 19, 2024
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  configuring-the-socure-connector: Configuring the Socure connector
  connector-configuration: Connector configuration
  id-key: ID+ Key
  sdk-key: SDK Key
  api-url: API URL
  webhook-url: Webhook URL
  dv-socure-connector-setting-up-socure: Setting up Socure
  allowing-the-davinci-webhook-url-in-your-socure-configuration: Allowing the DaVinci webhook URL in your Socure configuration
  allowing-the-davinci-domain-in-your-socure-configuration: Allowing the DaVinci domain in your Socure configuration
  dv-socure-getting-api-keys: Getting your Socure ID+ and SDK keys
  using-the-connector-in-a-flow: Using the connector in a flow
  verify-identity-documents-with-a-link-or-qr-code: Verify identity documents with a link or QR code
  verify-identity-documents-with-an-sms-prompt: Verify identity documents with an SMS prompt
  getting-id-scores: Getting ID+ scores
  capabilities: Capabilities
  documentVerification: Verify a Document
  webhook: Wait for the Documentation Verification Result
  getScore: Get an ID+ Score
  makeCustomApiCall: Make Custom API Call
  getVerificationUrl: Get a Document Verification URL and QR Code
---

# Socure Connector

The Socure connector lets you verify identity documents and get fraud scores in your PingOne DaVinci flows.

The connector allows you to direct users to a unique verification URL where they submit their driver license or passport along with selfie photos. After Socure verifies the user's identity, it sends the results to DaVinci where you can branch your flow accordingly.

To make sure a camera is available to scan the documents and take photos, the user typically completes the verification process on a mobile device.

## Setup

### Resources

Learn more in the following:

* DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need a Socure license.

### Configuring the Socure connector

Add the connector in DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

##### ID+ Key

Your Socure ID+ key, such as "a1b234cd-75e1-9e01-f234-56abcdef6789".

Get this key from [Setting up Socure](#dv-socure-connector-setting-up-socure).

##### SDK Key

Your Socure SDK key, such as "d450e856-9e01-75e1-8cec-64efe8eef39b".

Get this key from [Setting up Socure](#dv-socure-connector-setting-up-socure).

##### API URL

The Socure API URL to target. Select the environment that you chose in [Getting your Socure ID+ and SDK keys](#dv-socure-getting-api-keys).

Get this URL from [Setting up Socure](#dv-socure-connector-setting-up-socure).

##### Webhook URL

The DaVinci webhook URL for this instance of your connector.

Copy this URL. You'll use it in [Setting up Socure](#dv-socure-connector-setting-up-socure).

### Setting up Socure

#### Allowing the DaVinci webhook URL in your Socure configuration

1. Sign on to the Socure administrator portal at <https://admin.socure.com>.

2. Go to **Developer > Webhook**. Click **New Webhook**.

3. In the **Subscription Type** list, select **Document Verification**.

4. In the **Subscription Channel Name** field, enter a name.

5. In the **Webhook URL** field, enter the webhook URL that you copied from your Socure connector configuration.

6. Leave the **Secret Key** field blank.

7. Leave the **Choose certificate** section blank.

8. Click **Test**. Check that the test was successful.

#### Allowing the DaVinci domain in your Socure configuration

Click **Create**.

You can find a list of domains that DaVinci uses in [IP address and domain reference](https://docs.pingidentity.com/pingone/developer_tools/p1_ip_address_domain_reference.html). Follow the steps below to add all the domains for your region:

1. Sign on to the Socure administrator portal at <https://admin.socure.com>.

2. Go to **Developers > IPs & Domains**.

3. Click **New Domain**.

4. In the **IP/DOMAINS** field, enter the domain. Click **Create**.

5. Repeat this process for each DaVinci domain in your region.

#### Getting your Socure ID+ and SDK keys

|   |                                                                      |
| - | -------------------------------------------------------------------- |
|   | Your **ID+ Key** and **SDK Key** are different for each environment. |

1. Sign on to the Socure administrator portal at <https://admin.socure.com>.

2. Select the environment you want to connect to:

   1. Click your organization.

   2. Click to select the **Production**, **Certification**, or **Sandbox** environment.

      ![A screen capture that shows the environments list in the Socure administator portal.](_images/connector-images/dvc-socure-environments-list.png)

   3. Go to **Developers > ID+ Keys** and **SDK Key** to get your ID+ and SDK keys.

      ![A screen capture of the Socure admin portal that shows the ID+ and SDK keys.](_images/connector-images/dvc-socure-admin-portal.gif)

## Using the connector in a flow

### Verify identity documents with a link or QR code

![A screen capture of the complete verify document flow.](_images/connector-images/dvc-socure-verify-document-flow.png)

This flow uses Socure to get a unique verification URL and show it as a link and QR code in the user's web browser. When the user opens the link with their mobile device, they are guided through the process of submitting photos of their identification card (either a driver license or passport) and taking a selfie photo. After the documents and photos are accepted, the flow continues where it started in the web browser.

This flow creates a "challenge" to pause the main flow on the QR code while a secondary flow continues the verification process. When the verification process is complete, a [Challenge](challenge_connector.html) connector resolves the challenge and triggers the main flow to continue. Learn more about this technique in [Challenge Connector](challenge_connector.html).

1. Download the [Socure - Identity verification with link or QR code](https://support.pingidentity.com/s/marketplace-integration/a7iDo0000010xc0IAA/socure-identity-verification-with-link-or-qr-code) flow template. Learn more in [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html).

2. On the flow canvas, select the **Get a Document Verification URL and QR Code** node.

3. (Optional) In the **Customer User ID** field, change the value to a test user ID that exists in your Socure records. In a real-world flow, click **{}** and populate this with a variable from earlier in your flow.

4. (Optional) Customize the document verification prompt:

   1. Select the **Verification Prompt** node.

   2. In the **Message Title** field, customize the title of the prompt.

   3. In the **Message** field, customize the user-facing text.

   4. Click **Apply**.

5. Test the flow:

   1. Click **Save**, **Deploy**, and **Try Flow**.

   2. With your mobile device, scan the QR code and open the link.

   3. Complete the document verification process on your mobile device.

   4. The result displays in your web browser on the original device.

### Verify identity documents with an SMS prompt

![A screen capture of the complete verify identity documents with an SMS prompt flow.](_images/connector-images/dvc-socure-verify-documents-flow-sms.png)

In this flow, Socure prompts the user to enter their phone number in their web browser. Socure sends an SMS message to the number, which guides the user through the process of submitting photos of their identification card (either a driver license or passport) and taking a selfie photo. After the documents and photos are accepted, the flow continues where it started in the web browser.

This flow creates a "challenge" to pause the main flow on the QR code while a secondary flow continues the verification process. When the verification process is complete, a [Challenge Connector](challenge_connector.html) connector resolves the challenge and triggers the main flow to continue. Learn more about this technique in [Challenge Connector](challenge_connector.html).

1. Download the [Socure - Identity verification with SMS prompt](https://support.pingidentity.com/s/marketplace-integration/a7iDo0000010xc5IAA/socure-identity-verification-with-sms-prompt) flow template. Learn more in [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html).

2. (Optional) Customize the "Check Your Device" message:

   ![A screen capture of the Check Your Device message telling the use to complete the document verification process on their mobile device.](_images/connector-images/dvc-socure-check-your-device.png)

   1. Select the **Check Your Device** node.

   2. In the **Message Title** field, customize the title of the prompt.

   3. In the **Message** field, customize the user-facing text.

   4. Click **Apply**.

3. Test the flow:

   1. Click **Save**, **Deploy**, and **Try Flow**.

   2. Register a new user or sign in with an existing user.

   3. Enter your mobile device SMS number.

   4. Complete the document verification process on your mobile device.

   5. The result displays in your web browser on the original device.

### Getting ID+ scores

![A screen capture of the complete Get ID+ scores flow](_images/connector-images/dvc-socure-get-scores-flow.png)

You can use the connector to get a variety of risk scores, fraud scores, and other information based on information you provide about a person or device.

This flow sends information about a person to Socure then shows the resulting score. You can customize the information you send to and get from Socure.

1. Download the [Socure - ID+ score check](https://support.pingidentity.com/s/marketplace-integration/a7iDo0000010xbvIAA/socure-id-score-check) flow template. Learn more in [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

2. Select the Socure ID+ modules that you want to use:

   1. On the flow canvas, select the **Get an ID+ Score** node.

   2. In the **Modules** list, select one or more modules.

      |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Socure ID+ modules represent a variety of data sources that verify identities. Learn more in [ID+ Modules](https://developer.socure.com/docs/idplus/modules/modules-overview) in the Socure documentation.When you use the **Get an ID+ Score** capability, you can select as many modules as you want, with the following limitations:- Only select modules that you have a license to use in Socure.

      - Only select one **Global Watchlist** module.

      - If you select the **Decision** module, you have to select at least one other module. Learn more in [Decision](https://developer.socure.com/docs/idplus/modules/decision) in the Socure documentation.

      - The **Device Risk** capability requires a device session ID. To get a session ID, include the device profiling script in your web app. The script sends a device profile to Socure and provides a session ID that DaVinci uses to get the device risk score. Learn more in [Sigma Device Client-Side Javascript](https://developer.socure.com/docs/sdks/sigma-device/js-sdk/js-overview) in the Socure documentation. |

3. Populate the personal attributes by clicking **{ }** and selecting variables from your flow.

   |   |                                                                                                                                                                                                                                    |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | For demonstration purposes, the flow template includes an HTML form with pre-filled information. When you build your own flow, you can collect information about the person from a form, database, or another source in your flow. |

4. Populate the **Document UUID** field with the unique ID for an identity document that the person submitted.

5. Click **Apply**.

6. Test the flow:

   1. Click **Save**, **Deploy**, and **Try Flow**.

   2. Submit the HTML form.

## Capabilities

### Verify a Document

Verify the authenticity of an identity document. This uses the Socure Predictive Document Verification Web SDK.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> - - screen0Config
>   - title textField
>
>   Default:
>
>   ```none
>   Socure Document Verification
>   ```
>
> - bodyHeaderText textField
>
>   Default:
>
>   ```none
>   Receive you Document verification URL through SMS
>   ```
>
> - Verification Level dropDown required
>
>   Set the verification process workflow for the transaction.
>
>   * Document upload only (Default)
>
>   * Document upload and document verification
>
>   * Document upload, document verification, and Phone RiskScore
>
> - Country textField
>
>   Two letter ISO Country
>
> * registerInitiate object
>
>   * properties object
>
>     * sdkKey string required
>
>   * parameters object
>
>     * phoneNumber string required minLength: 6
>
> * registerComplete object
>
>   * parameters object
>
>     * referenceId string
>
>     * credId string

### Wait for the Documentation Verification Result

Wait for Socure to send the result of a document verification check to the DaVinci webhook URL.

> **Collapse: Show details**
>
> * Output Schema
>
> - output object
>
>   * rawResponse object
>
>     * id string
>
>     * origId string
>
>     * eventGroup string
>
>     * reason string
>
>     * environmentName string
>
>     * event object
>
>       * eventType string
>
>       * data object
>
>         * address string
>
>         * dob string
>
>         * documentNumber string
>
>         * expirationDate string
>
>         * firstName string
>
>         * surName string
>
>         * fullName string
>
>         * parsedAddress object
>
>       * referenceId string
>
>       * customerUserId number
>
>       * message string
>
>   * uuid string
>
>     The value will be undefined for events other than DOCUMENTS\_UPLOADED.
>
>   * challenge string
>
>   * credentialStatusObject object
>
>     * detailStatus string
>
>     * rawStatus object
>
>     * challenge string
>
>     * credId string
>
>     * userId string
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "id": "efgh2345-6fg7-89h0-12ij-3k4567l890n",
>     "origId": "af096ad4-b9ba-4935-a148-61837aa535c4",
>     "eventGroup": "DocvNotification",
>     "reason": "DOCUMENTS_UPLOADED",
>     "environmentName": "production",
>     "event": {
>       "eventType": "DOCUMENTS_UPLOADED",
>       "data": {
>         "address": "965 Maxwell Street Petty, TX 75470",
>         "dob": "1979-05-07",
>         "documentNumber": "SOC86753099",
>         "expirationDate": "2022-10-13",
>         "firstName": "John",
>         "surName": "Smith",
>         "fullName": "John Smith",
>         "parsedAddress": {}
>       },
>       "referenceId": "abcd1234-5ef6-78g9-01hi-2j3456k7890m",
>       "customerUserId": 121212,
>       "message": "Documents Upload Successful"
>     }
>   },
>   "challenge": "66680a42-2d4d-408f-aa64-f40c8dd752d0",
>   "credentialStatusObject": {
>     "detailStatus": "VERIFICATION_COMPLETED",
>     "rawStatus": {},
>     "challenge": "66680a42-2d4d-408f-aa64-f40c8dd752d0",
>     "credId": "6d9vb6l0p2e56jgfsha7oke318akm556",
>     "userId": "1f9cd66c12e46eaf15c7e2e318a7c5d3"
>   }
> }
> ```

### Get an ID+ Score

Get a Socure ID+ score for a user based on the ID+ modules that you select. The result is a number between 0 and 1, with a higher value indicating higher probability of fraud.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - - modules dropDownMultiSelect
>   - First Name textField
>   - Sur Name textField
>   - Email textField
>   - Country textField
>   - Physical Address textField
>   - Physical Address 2 textField
>   - City textField
>   - State textField
>   - Zip textField
>   - Mobile Number textField
>   - Geocodes (lat long) textField
>   - National ID textField
>   - Date of Birth textField
>   - Company Name textField
>   - Document UUID textField
>   - Order Amount textField
>   - Account Creation Date textField
>   - Submission Date textField
>   - Previous Order Count textField
>   - Last Order Date textField
>   - Order Channel textField
>   - Customer User ID textField
>
>   The unique identifier for the user, such as "123".
>
> - * Watchlist Filters textField
>   * Recipient Country textField
>   * Payment Type textField
>   * Disbursement Type textField
>   * Operation System textField
>   * Device Type textField
>   * Device Session ID textField
>   * Device Interface textField
>
> * login object
>
>   * properties object
>
>     * baseUrl string required
>
>     * apiKey string required
>
>     * modules array required
>
>   * ip string
>
>   * userAgent string
>
> - output object
>
>   * rawResponse object
>
>     * referenceId string
>
>     * nameAddressCorrelation object
>
>       * reasonCodes array
>
>       * score number
>
>     * namePhoneCorrelation object
>
>       * reasonCodes array
>
>       * score number
>
>     * fraud object
>
>       * reasonCodes array
>
>       * scores array
>
>     * kyc object
>
>       * reasonCodes array
>
>       * cvi integer
>
>       * correlationIndices object
>
>         * nameAddressPhoneIndex integer
>
>         * nameAddressSsnIndex integer
>
>       * decision object
>
>         * modelName string
>
>         * modelVersion string
>
>         * status string
>
>       * fieldValidations object
>
>         * firstName number
>
>         * surName number
>
>         * streetAddress number
>
>         * city number
>
>         * state number
>
>         * zip number
>
>         * mobileNumber number
>
>         * dob number
>
>         * ssn number
>
>     * addressRisk object
>
>       * reasonCodes array
>
>       * score number
>
>     * emailRisk object
>
>       * reasonCodes array
>
>       * score number
>
>     * phoneRisk object
>
>       * reasonCodes array
>
>       * score number
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "referenceId": "123a456b-789c-1234-567c-9307e6e0a83f",
>     "nameAddressCorrelation": {
>       "reasonCodes": [
>         "I709",
>         "I708",
>         "I710"
>       ],
>       "score": 0.9096
>     },
>     "namePhoneCorrelation": {
>       "reasonCodes": [
>         "I621",
>         "I622",
>         "I618"
>       ],
>       "score": 0.9984
>     },
>     "fraud": {
>       "reasonCodes": [
>         "I610",
>         "I626",
>         "I705",
>         "I609",
>         "I553",
>         "I611",
>         "I614",
>         "I127",
>         "I630",
>         "I708",
>         "I618",
>         "I555",
>         "I707",
>         "I602"
>       ],
>       "scores": [
>         {
>           "name": "sigma",
>           "version": "1.0",
>           "score": 0.167
>         }
>       ]
>     },
>     "kyc": {
>       "reasonCodes": [
>         "I919"
>       ],
>       "cvi": 0,
>       "correlationIndices": {
>         "nameAddressPhoneIndex": 0,
>         "nameAddressSsnIndex": 0
>       },
>       "decision": {
>         "modelName": "SOCURE_FIX",
>         "modelVersion": "1.0",
>         "status": "REFER"
>       },
>       "fieldValidations": {
>         "firstName": 0.99,
>         "surName": 0.99,
>         "streetAddress": 0.99,
>         "city": 0.99,
>         "state": 0.99,
>         "zip": 0.99,
>         "mobileNumber": 0.99,
>         "dob": 0.99,
>         "ssn": 0.99
>       }
>     },
>     "addressRisk": {
>       "reasonCodes": [
>         "I610",
>         "I705",
>         "I720",
>         "I708",
>         "I707"
>       ],
>       "score": 0.364
>     },
>     "emailRisk": {
>       "reasonCodes": [
>         "I520",
>         "I553",
>         "I555"
>       ],
>       "score": 0.133
>     },
>     "phoneRisk": {
>       "reasonCodes": [
>         "I610",
>         "I626",
>         "I609",
>         "I620",
>         "I611",
>         "I614",
>         "I630",
>         "I618",
>         "I602"
>       ],
>       "score": 0.122
>     }
>   }
> }
> ```

### Make Custom API Call

Define and invoke custom call to the Socure REST API.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Endpoint textField required
>
>   The Socure API endpoint, such as /api/3.0/EmailAuthScore.
>
> - HTTP Method dropDown required
>
>   The HTTP method of the API call.
>
>   * GET
>
>   * POST
>
>   * PUT
>
>   * DELETE
>
> - Query Parameters keyValueList
>
>   Define additional query parameters to send to Socure.
>
> - Additional Headers keyValueList
>
>   Additional headers for the request. Connector automatically adds 'Authorization' and 'Content-Type' headers.
>
> - Body codeEditor
>
>   The body of the API call.
>
> * default object
>
>   * properties object
>
>     * apiKey string required
>
>     * endpoint string required
>
>     * method string required
>
>     * queryParams array
>
>     * headers array
>
>     * bodyData object
>
> Input Example
>
> ```json
> {
>   "properties": {
>     "endpoint": "/api/3.0/EmailAuthScore",
>     "method": "POST",
>     "bodyData": {
>       "modules": [
>         "addressrisk"
>       ],
>       "firstName": "John",
>       "surName": "Smith",
>       "physicalAddress": "123 Example Street",
>       "physicalAddress2": "Apt. 5",
>       "city": "New York",
>       "state": "NY",
>       "zip": "10001",
>       "country": "us"
>     }
>   }
> }
> ```
>
> * output object
>
>   * headers object
>
>   * statusCode integer
>
>   * rawResponse object

### Get a Document Verification URL and QR Code

Get a unique document verification URL and QR code based on a user identifier.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Verification Level dropDown required
>
>   Set the verification process workflow for the transaction.
>
>   * Document upload only (Default)
>
>   * Document upload and document verification
>
>   * Document upload, document verification, and Phone RiskScore
>
> - Customer User ID textField
>
>   The unique identifier for the user, such as "123".
>
> - Phone Number textField
>
>   Used with Verification Level 3
>
> - Country textField
>
>   Two letter ISO Country
>
> * documentVerificationUrl object::
>
> - output object
>
>   * qrcode string
>
>   * url string
