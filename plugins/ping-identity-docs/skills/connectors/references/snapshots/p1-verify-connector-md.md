---
title: PingOne Verify Connector
description: "Use the PingOne Verify connector with PingOne DaVinci to securely verify a user's identity"
component: connectors
page_id: connectors::p1_verify_connector
canonical_url: https://docs.pingidentity.com/connectors/p1_verify_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  setting-up-pingone: Setting up PingOne
  setting-up-your-pingone-environment: Setting up your PingOne environment
  getting-your-environment-details: Getting your environment details
  choosing-a-pingone-worker-app: Choosing a PingOne worker app
  getting-your-application-credentials: Getting your application credentials
  setting-up-the-connector: Setting up the connector
  connector-settings: Connector settings
  environment-id: Environment ID
  client-id: Client ID
  client-secret: Client secret
  region: Region
  using-the-pingone-verify-connector-in-a-flow: Using the PingOne Verify connector in a flow
  capabilities: Capabilities
  createVerifyTransaction: Create Transaction
  readVerifyTransaction: Read Transaction
  readVerifyTransactions: Read Transactions
  readUserData: Read User Data
  readGovernmentID: Read Government ID
  readVerifiedData: Read Verified Data
  readSelfie: Read Selfie
  readMetaData: Read Metadata
  readVerifyPolicy: Read Verify Policy
  setVerifyStatus: Set Verify Status
  readDocuments: Return All Collected Data
  readDocument: Read Collected Data
  createDocument: Submit Collected Data
  updateDocument: Update Collected Data
  deleteDocument: Delete Collected Data
  processDocuments: Process All Data Collected
  createExtClientResponse: Create Response for External Client
  backgroundReplacer: Replace Background
  identityRecordMatching: Identity Record Matching
  troubleshooting: Troubleshooting
  solutions: Solutions
  resources-2: Resources
---

# PingOne Verify Connector

Use the PingOne Verify connector to securely verify a user's identity based on a government-issued document and other user-submitted data, such as a live face capture (selfie).

The user ID information is captured using a unique QR code and sent to the PingOne ID Verification service. The PingOne ID Verification service interacts with service providers that verify the submitted user ID information. When a user's ID information is successfully verified, the PingOne ID Verification service approves the user authentication and sends the ID verification status to the browser or to the next connector in the flow.

## Setup

### Resources

Learn more about setup help in the following sections of PingOne Verify and PingOne DaVinci:

* PingOne Verify documentation

  * [Introduction to PingOne Verify](https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_introduction.html)

  * [Getting started with PingOne Verify](https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_getting_started_with_p1_verify.html)

* PingOne DaVinci documentation

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the PingOne Verify connector, you'll need:

* A PingOne license with PingOne Verify ([Try PingOne for free](https://www.pingidentity.com/en/try-ping.html)).

* A PingOne environment with a configured worker application. Learn more in [Choosing a PingOne worker app](#choosing-a-pingone-worker-app).

### Setting up PingOne

#### Setting up your PingOne environment

Sign up for PingOne and configure an environment with PingOne Verify. Learn more in [Getting started with PingOne](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_getting_started.html).

#### Getting your environment details

Get your **Environment ID** and **Region** before setting up the PingOne Verify connector in PingOne DaVinci:

1. In the PingOne admin console, go to **Settings > Environment Properties**.

2. Locate the **Environment ID** and **Region**.

3. Copy these values to a secure location.

#### Choosing a PingOne worker app

Most environments include a preconfigured worker app that you can use with DaVinci connectors.

To add a worker app:

1. Decide whether to connect to the host PingOne tenant or a different PingOne tenant.

2. In the PingOne admin console, go to **Applications > Applications**.

3. Select the preconfigured **PingOne DaVinci Connection** worker app.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | A small number of older environments might not have the preconfigured worker app. If that applies to your environment, you can:- Reuse a worker app you've already created.

- Create a new worker app.

  > **Collapse: Details**
  >
  > To create a new worker app for this connector:
  >
  > 1. Sign on to PingOne.
  >
  > 2. Create a worker app as described in the [PingOne documentation](https://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html).
  >
  > 3. Make sure you set the authentication method as `Client secret basic`.
  >
  >    The PingOne connector receives a token using your application's credentials.
  >
  > 4. Assign the following roles to the worker app:
  >
  >    * **Identity Data Admin**
  >
  >    * **Environment Admin**
  >
  > 5. Note the **Client ID**, **Client Secret**, and **Environment ID** for the worker app.
  >
  > 6. Click **Finish**.
  >
  > 7. Go to **Applications > Applications**, click the application to open the application details, and click the toggle switch in the upper right to enable the application. |

#### Getting your application credentials

Get the **Client ID** and **Client secret** from your PingOne admin console before setting up the PingOne Verify connector in PingOne DaVinci:

1. In the PingOne admin console, go to **Applications > Applications**. If you haven't added the application yet, you can find instructions in [Adding an application](https://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html) in the PingOne documentation.

2. Locate the application from [Choosing a PingOne worker app](#choosing-a-pingone-worker-app) and then click its entry to open the details panel.

3. On the **Profile** tab, locate the **Client ID** and **Client secret**.

4. Copy these values to a secure location.

### Setting up the connector

In PingOne DaVinci, go to **Connections** and add a **PingOne Verify** connection. Learn more in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html).

#### Connector settings

##### Environment ID

The unique identifier for the appropriate PingOne environment. You can learn how to find the environment ID in [Environment properties](https://docs.pingidentity.com/pingone/settings/p1_environments.html) in the PingOne documentation.

##### Client ID

The unique public identifier for the PingOne application you identified in [Choosing a PingOne worker app](#choosing-a-pingone-worker-app). Learn how to find the client ID in [Viewing application details](https://docs.pingidentity.com/pingone/applications/p1_viewapplications.html) in the PingOne documentation.

##### Client secret

The cryptographic secret that is known only to the application and the authorization server. Use the client secret of the application you identified in [Choosing a PingOne worker app](#choosing-a-pingone-worker-app). Learn how to find the client secret in [Viewing a client secret](https://docs.pingidentity.com/pingone/applications/p1_view_client_secret_application.html) in the PingOne documentation.

##### Region

The geographic region that hosts your PingOne tenant. Learn how to find the region in [Environment properties](https://docs.pingidentity.com/pingone/settings/p1_environments.html) in the PingOne documentation.

## Using the PingOne Verify connector in a flow

You can use the PingOne Verify connector to add user verification based on a government-issued document and live face capture (selfie) and the other [PingOne Verify types of verification](https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_types_of_verification.html) configurable with a [PingOne Verify policy](https://docs.pingidentity.com/pingone/identity_verification_using_pingone_verify/p1_verify_policies.html).

The PingOne Verify connector is typically added to an existing flow, such as a registration flow or sign-on flow.

|   |                                                                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When **Debug Mode** is selected in the flow settings, logs can include sensitive data. Learn more in [Debugging and Analytics](https://docs.pingidentity.com/davinci/davinci_best_practices/davinci_best_practices_debugging_and_analytics.html). |

In the flow example below, when a user's ID information is successfully verified, the PingOne ID Verification service approves the user authentication and sends the ID verification status to the browser or to the next connector in the flow.

The example flow contains the following nodes:

![A screen capture of a PingOne Verify flow example showing various nodes.](_images/connector-images/dvc-verify-flow.png)

The `Get User Details` node lets the user input their information into PingOne using the `Create User` node. This information is also used for biographic matching requirements needed in a PingOne Verify transaction.

The `Create Verify Transaction` node enables the user verification status and creates the PingOne Verify transaction. You can use this node to add biographic fields, such as a user's first name, last name, and birth date, which are used for biographic matching. If the transaction succeeds, the user sees a unique QR code in the browser.

The `Return Verify Result` and `Check Transaction Status` nodes read the results of the verification transaction, and then check the status of the transaction. The status is evaluated as follows:

* `Fail`: The flow continues to `Read government ID` node, `Return all collected` node, and `Read metadata` node.

* `Success`: The flow continues to `Read government ID` node, `Return all collected` node, and `Read metadata` node.

* `No match`: The flow shows the QR code again, and the user can try again.

The `Return Document Images`, `Read Metadata`, `Return Government ID`, and `Return Selfie Image` nodes read the verified data from the government ID, user-submitted data, and metadata related to the verification. The output can be selectively used in the `Display User Data` node.

`Read Metadata` results include biographic matching that was required in the `Create Verify Transaction` node. The biographic matching results show the comparison between what the end user inputs as their data against the verified data extracted from their government ID, returning a confidence level of high, medium, or low.

## Capabilities

### Create Transaction

Create verify transaction

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   ID of the user
>
> - Device OS Type dropDown
>
>   The OS type of the device to receive SMS messages during verification.
>
>   * Mobile Web (Default)
>
> - Verify Policy dropDown
>
>   Name of the verify policy.
>
>   * Use Verify Policy ID
>
> - Verify Policy ID textField
>
>   ID of the verify policy.
>
> - Notification Phone Number textField
>
>   The phone number to receive SMS notifications during verification.
>
> - Notification Email Address textField
>
>   The email address to receive email notifications during verification.
>
> - Verification Phone Number multipleTextFields
>
>   The phone number(s) to be verified for phone-verification-required policy.
>
> - Verification Email Address multipleTextFields
>
>   The email address(es) to be verified for email-verification-required policy.
>
> - Reference Image textField
>
>   Base64 encoded reference image for facial-comparison-only verify policy.
>
> - Biographic Fields selectNameValueListColumn
>
>   Use this section to add biographic fields
>
>   * Given Name
>
>   * Family Name
>
>   * Name
>
>   * Address
>
>   * Birthdate
>
> - Challenge textField
>
>   Optional challenge. If not provided, a random challenge will be generated.
>
> - Redirect URL textField
>
>   The Redirect URL where the user is returned to after document collection. Only secure (https\://) URLs are allowed.
>
> - Redirect Message textField
>
>   Displayed after document collection and before redirecting to the specified URL. Requires a configured Redirect URL. Limited to 256 characters.
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>       User ID
>
>     * deviceOsType string required
>
>       device OS type
>
>     * verifyPolicy string minLength: 0 maxLength: 100
>
>       verify policy
>
>     * verifyPolicyId string minLength: 0 maxLength: 100
>
>       verify policy ID
>
>     * notifyPhone string
>
>       phone number for notification
>
>     * notifyEmail string
>
>       email address for notification
>
>     * verifyPhone array uniqueItems: true
>
>       phone number(s) for verification
>
>     * verifyEmail array uniqueItems: true
>
>       email address(es) for verification
>
>     * referenceImage string
>
>       base64 encoded reference image for facial-comparison-only verify policy
>
>     * biographic array
>
>       biographic info
>
>     * challenge string minLength: 1 maxLength: 100
>
>       challenge Id
>
>     * redirectUri string
>
>       Redirect URL
>
>     * redirectMessage string
>
>       Redirect message
>
> - output object
>
>   * transaction object
>
>     * id string
>
>     * verifyPolicy object
>
>       * id string
>
>     * transactionStatus object
>
>       * status string
>
>     * qrUrl string
>
>     * webVerificationUrl string
>
>     * webVerificationCode string
>
>     * createdAt string
>
>     * updatedAt string
>
>     * expiresAt string
>
>   * rawResponse object
>
>     * id string
>
>     * verifyPolicy object
>
>       * id string
>
>     * transactionStatus object
>
>       * status string
>
>     * qrUrl string
>
>     * webVerificationUrl string
>
>     * webVerificationCode string
>
>     * createdAt string
>
>     * updatedAt string
>
>     * expiresAt string
>
>   * headers object
>
>   * statusCode integer
>
>   * challenge string
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "transaction": {
>       "id": "c8d41d45-7f0b-42b6-88ee-fba3f6e883bf",
>       "verifyPolicy": {
>         "id": "a661f3bf-0e7b-45aa-a9db-6fc926ccacd3"
>       },
>       "transactionStatus": {
>         "status": "REQUESTED"
>       },
>       "qrUrl": "https://api.pingone.com/v1/idValidations/webVerifications/c8d41d45-7f0b-42b6-88ee-fba3f6e883bf/qr",
>       "webVerificationUrl": "https://verifycredential.pingone.com/verify-webapp/index.html?txnid=c8d41d45-7f0b-42b6-88ee-fba3f6e883bf&url=https%3A%2F%2Fapi.pingone.com%2Fv1%2FidValidations%2FwebVerifications&code=082754",
>       "webVerificationCode": "082754",
>       "createdAt": "2021-11-04T17:32:17.195Z",
>       "updatedAt": "2021-11-04T17:32:17.195Z",
>       "expiresAt": "2021-11-04T18:02:17.195Z"
>     }
>   }
> }
> ```

### Read Transaction

Read verify transaction

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   ID of the user
>
> - Transaction ID textField
>
>   ID of the transaction
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>       User ID
>
>     * transactionId string required minLength: 0 maxLength: 100
>
>       Transaction ID
>
> - output object
>
>   * transaction object
>
>     * id string
>
>     * verifyPolicy object
>
>       * id string
>
>     * transactionStatus object
>
>       * status string
>
>       * providerMessagesList array
>
>     * qrUrl string
>
>     * webVerificationUrl string
>
>     * webVerificationCode string
>
>     * verifiedDocuments string
>
>     * createdAt string
>
>     * updatedAt string
>
>     * expiresAt string
>
>   * rawResponse object
>
>     * id string
>
>     * verifyPolicy object
>
>       * id string
>
>     * transactionStatus object
>
>       * status string
>
>       * providerMessagesList array
>
>     * qrUrl string
>
>     * webVerificationUrl string
>
>     * webVerificationCode string
>
>     * verifiedDocuments string
>
>     * createdAt string
>
>     * updatedAt string
>
>     * expiresAt string
>
>   * headers object
>
>   * statusCode integer
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "transaction": {
>       "id": "c8d41d45-7f0b-42b6-88ee-fba3f6e883bf",
>       "verifyPolicy": {
>         "id": "a661f3bf-0e7b-45aa-a9db-6fc926ccacd3"
>       },
>       "transactionStatus": {
>         "status": "REQUESTED"
>       },
>       "qrUrl": "https://api.pingone.com/v1/idValidations/webVerifications/c8d41d45-7f0b-42b6-88ee-fba3f6e883bf/qr",
>       "webVerificationUrl": "https://verifycredential.pingone.com/verify-webapp/index.html?txnid=c8d41d45-7f0b-42b6-88ee-fba3f6e883bf&url=https%3A%2F%2Fapi.pingone.com%2Fv1%2FidValidations%2FwebVerifications&code=082754",
>       "webVerificationCode": "082754",
>       "createdAt": "2021-11-04T17:32:17.195Z",
>       "updatedAt": "2021-11-04T17:32:17.195Z",
>       "expiresAt": "2021-11-04T18:02:17.195Z"
>     }
>   }
> }
> ```

### Read Transactions

Read Verify transactions

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   ID of the user
>
> - limit textField
>
>   Number of transactions to return
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>       User ID
>
>     * limit integer
>
>       Specifies the maximum number of latest records to return
>
> - output object
>
>   * transactions object
>
>     * \_embedded object
>
>       * verifyTransactions array
>
>     * size number
>
>   * rawResponse object
>
>     * \_embedded object
>
>       * verifyTransactions array
>
>     * size number
>
>   * headers object
>
>   * statusCode integer

### Read User Data

Read verified user data

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   ID of the user
>
> - Transaction ID textField
>
>   ID of the transaction
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>       User ID
>
>     * transactionId string required minLength: 0 maxLength: 100
>
>       Transaction ID
>
> - output object
>
>   * userData object
>
>     * id string
>
>     * transactionStatus object
>
>       * status string
>
>     * verifiedUserData object
>
>       * firstName string
>
>       * lastName string
>
>       * middleName string
>
>       * gender string
>
>       * expirationDate string
>
>       * idNumber string
>
>       * addressStreet string
>
>       * addressCity string
>
>       * addressState string
>
>       * addressZip string
>
>       * country string
>
>       * issueDate string
>
>       * weight string
>
>       * height string
>
>       * hairColor string
>
>       * eyeColor string
>
>       * nationality string
>
>       * issuingCountry string
>
>       * personalNumber string
>
>       * birthDate string
>
>       * idType string
>
>   * rawResponse object
>
>     * id string
>
>     * transactionStatus object
>
>       * status string
>
>     * verifiedUserData object
>
>       * firstName string
>
>       * lastName string
>
>       * middleName string
>
>       * gender string
>
>       * expirationDate string
>
>       * idNumber string
>
>       * addressStreet string
>
>       * addressCity string
>
>       * addressState string
>
>       * addressZip string
>
>       * country string
>
>       * issueDate string
>
>       * weight string
>
>       * height string
>
>       * hairColor string
>
>       * eyeColor string
>
>       * nationality string
>
>       * issuingCountry string
>
>       * personalNumber string
>
>       * birthDate string
>
>       * idType string
>
>   * headers object
>
>   * statusCode integer

### Read Government ID

Read verified data parsed off the government ID images

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   ID of the user
>
> - Transaction ID textField
>
>   ID of the transaction
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>       User ID
>
>     * transactionId string required minLength: 0 maxLength: 100
>
>       Transaction ID
>
> - output object
>
>   * governmentID object
>
>     * \_embedded object
>
>       * verifiedData array
>
>     * size number
>
>   * rawResponse object
>
>     * \_embedded object
>
>       * verifiedData array
>
>     * size number
>
>   * headers object
>
>   * statusCode integer

### Read Verified Data

Read Verified Data

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   ID of the user
>
> - Transaction ID textField
>
>   ID of the transaction
>
> - attempt textField
>
>   Limit the number verified attempts. Valid values (ALL, LATEST, 1, 2, 3, 4)
>
> - Verified Type(s) dropDownMultiSelect
>
>   Selected Verified data type(s)
>
>   * Selfie
>
>   * Government ID
>
>   * Front Image
>
>   * Back Image
>
>   * Barcode
>
>   * Cropped Portrait
>
>   * Cropped Document
>
>   * Cropped Signature
>
>   * Voice Sample
>
>   * Voice Input
>
>   * End User Client
>
> * default object
>
>   * properties object
>
>     * userId string required
>
>       Verified Type
>
>     * transactionId string required minLength: 0 maxLength: 100
>
>       Transaction ID
>
> - output object
>
>   * verifiedData object
>
>     * \_embedded object
>
>       * verifiedData array
>
>     * size number
>
>   * rawResponse object
>
>     * \_embedded object
>
>       * verifiedData array
>
>     * size number
>
>   * headers object
>
>   * statusCode integer

### Read Selfie

Read selfie provided by the user

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   ID of the user
>
> - Transaction ID textField
>
>   ID of the transaction
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>       User ID
>
>     * transactionId string required minLength: 0 maxLength: 100
>
>       Transaction ID
>
> - output object
>
>   * selfie object
>
>     * \_embedded object
>
>       * verifiedData array
>
>     * size number
>
>   * rawResponse object
>
>     * \_embedded object
>
>       * verifiedData array
>
>     * size number
>
>   * headers object
>
>   * statusCode integer

### Read Metadata

Read metadata related to verification

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   ID of the user
>
> - Transaction ID textField
>
>   ID of the transaction
>
> - Metadata Type dropDown
>
>   Type of the metadata. Select ALL to get all metadata.
>
>   * LIVENESS
>
>   * FACIAL\_COMPARISON
>
>   * BIOGRAPHIC\_MATCH
>
>   * DOCUMENT\_AUTHENTICATION
>
>   * DOCUMENT\_MANUAL\_AUTHENTICATION
>
>   * VOICE\_ENROLLMENT
>
>   * VOICE\_VERIFICATION
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>       User ID
>
>     * transactionId string required minLength: 0 maxLength: 100
>
>       Transaction ID
>
>     * metadataType string
>
>       metadata type
>
> - output object
>
>   * metaData object
>
>     * \_embedded object
>
>       * metaData array
>
>     * size number
>
>   * rawResponse object
>
>     * \_embedded object
>
>       * metaData array
>
>     * size number
>
>   * headers object
>
>   * statusCode integer

### Read Verify Policy

Read verify policy for verification

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Verify Policy dropDown
>
>   Name of the verify policy.
>
>   * Use Verify Policy ID (Default)
>
> - Verify Policy ID textField
>
>   ID of the verify policy.
>
> * default object
>
>   * properties object
>
>     * verifyPolicySelect string required minLength: 0 maxLength: 100
>
>       verify policy
>
>     * verifyPolicyIdSelect string minLength: 0 maxLength: 100
>
>       verify policy ID
>
> - output object
>
>   * verifyPolicy object
>
>     * id string
>
>     * environment object
>
>       * id string
>
>     * name string
>
>     * description string
>
>     * default boolean
>
>     * governmentId object
>
>       * verify string
>
>     * facialComparison object
>
>       * verify string
>
>       * threshold string
>
>     * liveness object
>
>       * verify string
>
>       * threshold string
>
>     * email object
>
>       * verify string
>
>       * createMfaDevice boolean
>
>       * otp object
>
>         * attempts object
>
>           * count number
>
>         * lifeTime object
>
>           * duration number
>
>           * timeUnit object
>
>         * deliveries object
>
>           * count number
>
>           * cooldown object
>
>           * duration number
>
>           * timeUnit string
>
>         * notification object
>
>           * templateName string
>
>           * variantName string
>
>     * phone object
>
>       * verify string
>
>       * createMfaDevice boolean
>
>       * otp object
>
>         * attempts object
>
>           * count number
>
>         * lifeTime object
>
>           * duration number
>
>           * timeUnit object
>
>         * deliveries object
>
>           * count number
>
>           * cooldown object
>
>           * duration number
>
>           * timeUnit string
>
>         * notification object
>
>           * templateName string
>
>           * variantName string
>
>     * createdAt string
>
>     * updatedAt boolean
>
>   * rawResponse object
>
>     * id string
>
>     * environment object
>
>       * id string
>
>     * name string
>
>     * description string
>
>     * default boolean
>
>     * governmentId object
>
>       * verify string
>
>     * facialComparison object
>
>       * verify string
>
>       * threshold string
>
>     * liveness object
>
>       * verify string
>
>       * threshold string
>
>     * email object
>
>       * verify string
>
>       * createMfaDevice boolean
>
>       * otp object
>
>         * attempts object
>
>           * count number
>
>         * lifeTime object
>
>           * duration number
>
>           * timeUnit object
>
>         * deliveries object
>
>           * count number
>
>           * cooldown object
>
>           * duration number
>
>           * timeUnit string
>
>         * notification object
>
>           * templateName string
>
>           * variantName string
>
>     * phone object
>
>       * verify string
>
>       * createMfaDevice boolean
>
>       * otp object
>
>         * attempts object
>
>           * count number
>
>         * lifeTime object
>
>           * duration number
>
>           * timeUnit object
>
>         * deliveries object
>
>           * count number
>
>           * cooldown object
>
>           * duration number
>
>           * timeUnit string
>
>         * notification object
>
>           * templateName string
>
>           * variantName string
>
>     * createdAt string
>
>     * updatedAt boolean
>
>   * headers object
>
>   * statusCode integer

### Set Verify Status

Set verify status for user

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   ID of the user
>
> - Verify Status dropDown
>
>   Verify status of the user to be set.
>
>   * ENABLED (Default)
>
>   * DISABLED
>
>   * NOT\_INITIATED
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>       User ID
>
>     * verifyStatus string required
>
>       verify status
>
> - output object
>
>   * verifyStatus object
>
>     * verifyStatus string
>
>   * rawResponse object
>
>     * verifyStatus string
>
>   * headers object
>
>   * statusCode integer

### Return All Collected Data

Return all data collected from the user.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   ID of the user
>
> - Transaction ID textField
>
>   ID of the transaction
>
> - Document Types dropDownMultiSelect
>
>   Types of the data collected. The document types accepted are determined by the transaction's policy requirements.
>
>   * Driver License Front
>
>   * Driver License Back
>
>   * Driver License Code
>
>   * Passport Front
>
>   * Passport Card Front
>
>   * Passport Card Back
>
>   * Selfie
>
>   * Phone
>
>   * Email
>
>   * Voice Sample
>
>   * Voice Input
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>       User ID
>
>     * transactionId string required minLength: 0 maxLength: 100
>
>       Transaction ID
>
>     * documentTypes array uniqueItems: true
>
>       document types
>
> - output object
>
>   * documents object
>
>     * \_embedded object
>
>       * documents array
>
>     * size number
>
>   * rawResponse object
>
>     * \_embedded object
>
>       * documents array
>
>     * size number
>
>   * headers object
>
>   * statusCode integer

### Read Collected Data

Return a piece of data collected from the user.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   ID of the user
>
> - Transaction ID textField
>
>   ID of the transaction
>
> - Document ID textField
>
>   ID of the data collected from user.
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>       User ID
>
>     * transactionId string required minLength: 0 maxLength: 100
>
>       Transaction ID
>
>     * documentId string required minLength: 0 maxLength: 100
>
>       document ID
>
> - output object
>
>   * document object
>
>     * id string
>
>     * environment object
>
>       * id string
>
>     * user object
>
>       * id string
>
>     * verifyTransaction object
>
>       * id string
>
>     * type string
>
>     * value string
>
>     * status string
>
>     * source object
>
>       * provider string
>
>   * rawResponse object
>
>     * id string
>
>     * environment object
>
>       * id string
>
>     * user object
>
>       * id string
>
>     * verifyTransaction object
>
>       * id string
>
>     * type string
>
>     * value string
>
>     * status string
>
>     * source object
>
>       * provider string
>
>   * headers object
>
>   * statusCode integer

### Submit Collected Data

Submit a piece of data collected from the user during verification.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   ID of the user
>
> - Transaction ID textField
>
>   ID of the transaction
>
> - Document Type dropDown
>
>   Type of the data collected. The document types accepted are determined by the transaction's policy requirements.
>
>   * Driver License Front (Default)
>
>   * Driver License Back
>
>   * Driver License Code
>
>   * Passport Front
>
>   * Passport Card Front
>
>   * Passport Card Back
>
>   * Selfie
>
>   * Phone
>
>   * Email
>
>   * Voice Sample
>
>   * Voice Input
>
> - Voice Sample Index textField
>
>   voice sample index starting from 1.
>
> - Document Value textField
>
>   Base64 encoded jpeg or textual data collected from user.
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>       User ID
>
>     * transactionId string required minLength: 0 maxLength: 100
>
>       Transaction ID
>
>     * documentTypeName string required minLength: 0 maxLength: 255
>
>       document type
>
>     * voiceSampleIndex integer
>
>       voice sample index starting from 1
>
>     * documentValue string required
>
>       base64 encoded jpeg or textual document depending on document type
>
> - output object
>
>   * document object
>
>     * id string
>
>     * environment object
>
>       * id string
>
>     * user object
>
>       * id string
>
>     * verifyTransaction object
>
>       * id string
>
>     * type string
>
>     * value string
>
>     * status string
>
>     * source object
>
>       * provider string
>
>   * rawResponse object
>
>     * id string
>
>     * environment object
>
>       * id string
>
>     * user object
>
>       * id string
>
>     * verifyTransaction object
>
>       * id string
>
>     * type string
>
>     * value string
>
>     * status string
>
>     * source object
>
>       * provider string
>
>   * headers object
>
>   * statusCode integer

### Update Collected Data

Update a piece of data collected from the user.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   ID of the user
>
> - Transaction ID textField
>
>   ID of the transaction
>
> - Document ID textField
>
>   ID of the data collected from user.
>
> - Document Type dropDown
>
>   Type of the data collected. The document types accepted are determined by the transaction's policy requirements.
>
>   * Driver License Front (Default)
>
>   * Driver License Back
>
>   * Driver License Code
>
>   * Passport Front
>
>   * Passport Card Front
>
>   * Passport Card Back
>
>   * Selfie
>
>   * Phone
>
>   * Email
>
>   * Voice Sample
>
>   * Voice Input
>
> - Document Value textField
>
>   Base64 encoded jpeg or textual data collected from user.
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>       User ID
>
>     * transactionId string required minLength: 0 maxLength: 100
>
>       Transaction ID
>
>     * documentId string required minLength: 0 maxLength: 100
>
>       document ID
>
>     * documentTypeName string required minLength: 0 maxLength: 255
>
>       document type
>
>     * documentValue string required
>
>       base64 encoded jpeg or textual document depending on document type
>
> - output object
>
>   * document object
>
>     * id string
>
>     * environment object
>
>       * id string
>
>     * user object
>
>       * id string
>
>     * verifyTransaction object
>
>       * id string
>
>     * type string
>
>     * value string
>
>     * status string
>
>     * source object
>
>       * provider string
>
>   * rawResponse object
>
>     * id string
>
>     * environment object
>
>       * id string
>
>     * user object
>
>       * id string
>
>     * verifyTransaction object
>
>       * id string
>
>     * type string
>
>     * value string
>
>     * status string
>
>     * source object
>
>       * provider string
>
>   * headers object
>
>   * statusCode integer

### Delete Collected Data

Delete a piece of data collected from the user.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   ID of the user
>
> - Transaction ID textField
>
>   ID of the transaction
>
> - Document ID textField
>
>   ID of the data collected from user.
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>       User ID
>
>     * transactionId string required minLength: 0 maxLength: 100
>
>       Transaction ID
>
>     * documentId string required minLength: 0 maxLength: 100
>
>       document ID
>
> - output object
>
>   * rawResponse object
>
>   * headers object
>
>   * statusCode integer

### Process All Data Collected

Process all data collected from the user during verification.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   ID of the user
>
> - Transaction ID textField
>
>   ID of the transaction
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>       User ID
>
>     * transactionId string required minLength: 0 maxLength: 100
>
>       Transaction ID
>
> - output object
>
>   * documents object
>
>     * \_embedded object
>
>       * documents array
>
>     * size number
>
>   * rawResponse object
>
>     * \_embedded object
>
>       * documents array
>
>     * size number
>
>   * headers object
>
>   * statusCode integer

### Create Response for External Client

Create JSON response for an integration with a mobile application.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Web Verification URL textField
>
>   web verification url
>
> - Challenge textField
>
>   Required challenge. To be added to the output for polling in subsequent step.
>
> - Is Last Client Step toggleSwitch
>
>   If isLastClientStep is false, the continueLink will be generated and added to the output, otherwise the link will not be added.
>
> * default object
>
>   * properties object
>
>     * webVerificationUrl string required
>
>       web verification url
>
>     * challengeId string required minLength: 1 maxLength: 100
>
>       challenge Id
>
>     * isLastClientStep boolean
>
>       If isLastClientStep is false, the continueLink will be generated and added to the output, otherwise the link will not be added.
>
> - output object
>
>   * clientState string
>
>   * webVerificationUrl string
>
>   * continueLink string
>
>   * challenge string

### Replace Background

Reshape the background of a selfie image.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   ID of the user
>
> - Transaction ID textField
>
>   ID of the transaction
>
> - Selfie ID textField
>
>   ID of the selfie
>
> - colorPicker colorPicker
>
>   Select color.
>
> - Aspect Width textField
>
>   Width of the aspect ratio
>
> - Aspect Height textField
>
>   Height of the aspect ratio
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>       User ID
>
>     * transactionId string required minLength: 0 maxLength: 100
>
>       Transaction ID
>
>     * selfieId string minLength: 0 maxLength: 100
>
>       Selfie ID
>
>     * colorPicker string
>
>       Color Picker
>
>     * aspectHeight integer minimum: 1 maximum: 1000
>
>       Aspect ratio height
>
>     * aspectWidth integer minimum: 1 maximum: 1000
>
>       Aspect ratio width
>
> - output object
>
>   * backgroundReplace object
>
>     * id string
>
>     * type string
>
>     * data object
>
>       * IMAGE string
>
>       * FORMAT string
>
>     * createdAt string
>
>   * rawResponse object
>
>     * id string
>
>     * type string
>
>     * data object
>
>       * IMAGE string
>
>       * FORMAT string
>
>     * createdAt string
>
>   * headers object
>
>   * statusCode integer

### Identity Record Matching

Identity Record Matching.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   ID of the user
>
> - Biographic Fields selectNameValueListColumn
>
>   Use this section to add biographic fields
>
>   * Given Name
>
>   * Family Name
>
>   * Name
>
>   * Address
>
>   * Birthdate
>
> - Probe Biographic Fields selectNameValueListColumn
>
>   Use this section to add probe biographic fields
>
>   * Given Name
>
>   * Family Name
>
>   * Name
>
>   * Address
>
>   * Birthdate
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>       User ID
>
>     * biographic array required
>
>       Probe Biographic Info
>
> - output object
>
>   * matchingResults object
>
>     * detailedResults object
>
>       * address object
>
>         * probeValue string
>
>         * galleryValue string
>
>         * rawScore number
>
>         * confidence string
>
>       * birth\_date object
>
>         * probeValue string
>
>         * galleryValue string
>
>         * rawScore number
>
>         * confidence string
>
>       * given\_name object
>
>         * probeValue string
>
>         * galleryValue string
>
>         * rawScore number
>
>         * confidence string
>
>       * family\_name object
>
>         * probeValue string
>
>         * galleryValue string
>
>         * rawScore number
>
>         * confidence string
>
>       * name object
>
>         * probeValue string
>
>         * galleryValue string
>
>         * rawScore number
>
>         * confidence string
>
>     * overallWeightedScore number
>
>     * overallConfidenceScore string
>
>   * rawResponse object
>
>     * detailedResults object
>
>       * address object
>
>         * probeValue string
>
>         * galleryValue string
>
>         * rawScore number
>
>         * confidence string
>
>       * birth\_date object
>
>         * probeValue string
>
>         * galleryValue string
>
>         * rawScore number
>
>         * confidence string
>
>       * given\_name object
>
>         * probeValue string
>
>         * galleryValue string
>
>         * rawScore number
>
>         * confidence string
>
>       * family\_name object
>
>         * probeValue string
>
>         * galleryValue string
>
>         * rawScore number
>
>         * confidence string
>
>       * name object
>
>         * probeValue string
>
>         * galleryValue string
>
>         * rawScore number
>
>         * confidence string
>
>     * overallWeightedScore number
>
>     * overallConfidenceScore string
>
>   * headers object
>
>   * statusCode integer

## Troubleshooting

The following resources can help you solve issues with the connector.

### Solutions

* The flow fails with no error message

  Ensure that the application is enabled in PingOne. Learn more in [Enabling or disabling an application](https://docs.pingidentity.com/pingone/applications/p1_enable_application.html).

* The flow fails when reading or updating a user

  Ensure that you are using the PingOne `user ID` attribute, not the `username` attribute.

### Resources

* Audit

  You can use the audit log to identify potential issues. Learn more in [Audit](https://docs.pingidentity.com/pingone/monitoring/p1_reporting.html).

* Testing capabilities

  Testing your flows frequently is the key to making them work correctly. Learn more in [Getting Started with PingOne DaVinci](https://docs.pingidentity.com/davinci/flows/davinci_getting_started.html).