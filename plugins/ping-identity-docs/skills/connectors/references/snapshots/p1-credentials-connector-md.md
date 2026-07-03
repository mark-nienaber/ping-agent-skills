---
title: PingOne Credentials Connector
description: Use the PingOne Credentials connector to issue, verify, and manage digital verifiable credentials with PingOne Credentials.
component: connectors
page_id: connectors::p1_credentials_connector
canonical_url: https://docs.pingidentity.com/connectors/p1_credentials_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 19, 2024
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  setting-up-pingone: Setting up PingOne
  setting-up-your-pingone-environment: Setting up your PingOne environment
  choosing-a-pingone-worker-app: Choosing a PingOne worker app
  getting-your-environment-details: Getting your environment details
  getting-your-application-credentials: Getting your application credentials
  setting-up-the-connector: Setting up the connector
  connector-settings: Connector settings
  environment-id: Environment ID
  client-id: Client ID
  client-secret: Client secret
  region: Region
  digital-wallet-application-id: Digital Wallet Application ID
  using-the-connector-in-a-flow: Using the connector in a flow
  capabilities: Capabilities
  readPairedDigitalWallets: Find Paired Wallet for User
  readUserDigitalWallet: Read User Wallet
  createUserDigitalWallet: Pair User Wallet to Application
  updateUserDigitalWallet: Update User Wallet
  deleteUserDigitalWallet: Delete User Digital Wallet
  readUserCredential: Read Credential
  readUserCredentials: Read All Credentials
  updateUserCredential: Revoke Credential
  applyStagedChanges: Issue/Update/Revoke Credential(s)
  createCredVerPresSession: Create Verification Session
  pollCredVerificationStatus: Poll for Verification Status
  readCredVerificationData: Return Verification Data
---

# PingOne Credentials Connector

Use the PingOne Credentials connector to issue, verify, and manage digital verifiable credentials with PingOne Credentials.

The connector sets up flows that help users issue credentials based on credentials templates and issuance rules that are configured and tied to the PingOne Digital Wallet Application.

This connector also helps set up flows that the credential verification service receives and responds to using the Decentralized Identity Foundation's [JWT VC Presentation Profile](https://identity.foundation/jwt-vc-presentation-profile/). Capabilities use the PingOne native protocols, which only work with apps that use the PingOne Neo Native SDKs.

## Setup

### Resources

Learn more in the following sections of the PingOne Credentials and DaVinci documentation:

* PingOne Credentials:

  * [Introduction to PingOne Credentials](https://docs.pingidentity.com/pingone/digital_credentials_using_pingone_credentials/p1_credentials_introduction.html)

  * [Getting started with PingOne Credentials](https://docs.pingidentity.com/pingone/digital_credentials_using_pingone_credentials/p1_credentials_getting_started.html)

* DaVinci:

  * [Introduction to PingOne](https://docs.pingidentity.com/pingone/introduction_to_pingone/p1_introduction.html)

  * [Getting started with PingOne](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_getting_started.html)

  * [Adding an application](https://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html)

### Requirements

To use the PingOne Credentials connector, you'll need:

* A PingOne license with PingOne credentials ([Try PingOne for free](https://www.pingidentity.com/en/try-ping.html))

* A PingOne environment with a configured application

* A PingOne application associated with a digital wallet and a Digital Wallet URL used to send notifications to the user related to the credentials

Depending on flow use case and the capabilities you use, you might also need:

* A PingOne Digital Wallet Application ID, the Identifier (UUID) associated with the credential digital wallet app. You can find more information on developing and registering the wallet app that runs the PingOne Neo SDK in [Getting started with PingOne Credentials](https://docs.pingidentity.com/pingone/digital_credentials_using_pingone_credentials/p1_credentials_getting_started.html).

* A Credential Type ID, the Identifier (UUID) associated with the credential type, used by compatible wallet apps. You can learn more about creating and updating a credential type in the [PingOne admin console](https://docs.pingidentity.com/pingone/digital_credentials_using_pingone_credentials/p1_credentials_creating_a_credential.html), or [PingOne Credential Types API endpoint](https://apidocs.pingidentity.com/pingone/platform/v1/api/).

* A Issuance Rule ID, the Identifier (UUID) of the credential issuance rules operations to create, read, and update rules for issuing, updating, and revoking credentials by credential type. Credential issuance rules can be set through the [PingOne admin console](https://docs.pingidentity.com/pingone/digital_credentials_using_pingone_credentials/p1_credentials_creating_a_credential.html), or [Credential Issuance Rules API endpoint](https://apidocs.pingidentity.com/pingone/platform/v1/api/).

### Setting up PingOne

#### Setting up your PingOne environment

Sign up for PingOne and configure an environment with PingOne Credentials. Make sure to also add the PingOne DaVinci service to your environment. Follow the instructions in [Getting started with PingOne](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_getting_started.html) and [Creating an environment](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_getting_started_adding_environment.html).

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

#### Getting your environment details

Get your **Environment ID** and **Region** before setting up the PingOne Credentials connector in DaVinci:

1. In your PingOne environment, go to **Settings > Environment Properties**.

2. Locate the **Environment ID** and **Region**.

3. Copy these values to a secure location.

#### Getting your application credentials

Get the **Client ID** and **Client secret** from the PingOne console before setting up the PingOne Credentials connector in DaVinci:

1. In your PingOne environment, go to **Applications > Applications**. Learn how to add an application in [Adding an application](https://docs.pingidentity.com/pingone/applications/p1_applications_add_applications.html).

2. Locate the application you identified in [Choosing a PingOne worker app](#choosing-a-pingone-worker-app) and click it to open the details panel.

3. On the **Profile** tab, locate the **Client ID** and **Client secret**.

4. Copy these values to a secure location.

### Setting up the connector

In DaVinci, go to **Connections** and add a **PingOne Credentials** connection. Learn more in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html).

#### Connector settings

##### Environment ID

The unique identifier for the appropriate PingOne environment. Learn how to find the environment ID in [Environment properties](https://docs.pingidentity.com/pingone/settings/p1_environments.html).

##### Client ID

The unique public identifier for the PingOne application that you identified in [Choosing a PingOne worker app](#choosing-a-pingone-worker-app). Learn how to find the client ID in [Viewing application details](https://docs.pingidentity.com/pingone/applications/p1_viewapplications.html).

##### Client secret

The cryptographic secret that is known only to the application and the authorization server. Use the client secret of the application that you identified in [Choosing a PingOne worker app](#choosing-a-pingone-worker-app). Learn how to find the client secret in [Viewing a client secret](https://docs.pingidentity.com/pingone/applications/p1_view_client_secret_application.html).

##### Region

The geographic region that hosts your PingOne tenant. Learn how to find the region in [Environment properties](https://docs.pingidentity.com/pingone/settings/p1_environments.html).

##### Digital Wallet Application ID

The unique identifier for the PingOne Digital Wallet Application that is associated with the credential types you want to issue and verify. This is required if you want to use the issuance and verification capabilities in the connector. Learn how to find the Digital Wallet Application ID in [Getting started with PingOne Credentials](https://docs.pingidentity.com/pingone/digital_credentials_using_pingone_credentials/p1_credentials_getting_started.html).

## Using the connector in a flow

You can use the PingOne Credentials connector to issue, verify, and manage digital verifiable credentials.

The following example flows show issuance and verification demonstrations.

The example issuance flow contains the following nodes.

![A screen capture of an issuance flow in PingOne DaVinci.](_images/connector-images/dvc-p1-credentials-issuance-flow.png)

1. Simulate user proofing/authentication:

   1. The `Get user details` node lets the user input their information into PingOne.

   2. The `Create user` node creates the user in PingOne.

2. Create user digital wallet and pair it to the existing digital wallet application:

   1. The `Pair user wallet to application` node creates a digital wallet for the user. The digital wallet application must already be configured in PingOne.

3. Determine if mobile device, then show QR code for desktop and link for mobile:

   1. The `Determine if Mobile Device` node determines if the user has a mobile device or not. If the user has a mobile device, then the digital wallet app URL opens. If the user is on a desktop, a QR code for the digital wallet app displays.

4. Poll and wait until the user has paired their digital wallet:

   1. The `Find paired wallet for user` node filters all user wallets to find if a paired wallet exists for the configured PingOne application.

   2. The `Wallet ACTIVE? A==B` node determines whether a digital wallet for the user has been paired or not.

   3. The `Continue polling` node continues to check for the digital wallet application status. When the status changes to paired, then the flow continues.

5. Apply credential issuance rule to staged changes for the user:

   1. The `Issue credentials` node is used to apply the changes staged by the credential issuance rule for the credential type in an environment.

   2. `User wallet successfully paired` node displays a success message to the user when the digital wallet is successfully paired.

      The example verification flow contains the following nodes.

      ![A screen capture of a verification flow in PingOne DaVinci.](_images/connector-images/dvc-p1-credentials-verification-flow.png)

6. Begin a session to verify a user's credential:

   1. The `Create verification session` node lets an issuer begin a verification session to verify a user's credential.

   2. The `Show QR Image` node displays a QR code for the user to verify their credential.

7. Poll session status and return verification result from the verified credential:

   1. The `Poll for verification status` node checks and returns the status of the verification session.

   2. The `Check verification status` node checks for the verification status to be "verified".

   3. The `Return verification data` node returns data from the verified credential.

   4. The `Show verification data` node displays the verified credential data.

## Capabilities

### Find Paired Wallet for User

Check if a user has a paired wallet

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
>   PingOne user ID
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>       User Id
>
> - output object
>
>   * digitalWallets object
>
>     * size number
>
>     * pairedWallets array
>
>   * rawResponse object
>
>     * size number
>
>     * pairedWallets array
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
>     "pairedDigitalWallets": {
>       "size": 2,
>       "digitalWallets": [
>         {
>           "id": "11dd742c-9f9b-4bde-b8f7-1ce6c8f56c3d",
>           "createdAt": "2023-04-14T16:04:51.449Z",
>           "updatedAt": "2023-04-14T16:04:51.449Z",
>           "environment": {
>             "id": "73056e49-0ebc-4a58-a126-dc9e1efb4ffe"
>           },
>           "user": {
>             "id": "5a942438-cca2-4edd-ac53-c1384c6e0329"
>           },
>           "digitalWalletApplication": {
>             "id": "1ab1e656-e7fa-46b9-a5ce-3eb7444e4eb8"
>           },
>           "status": "ACTIVE",
>           "pairingSession": {
>             "id": "54bfcb17-4981-4764-a243-a2449e0f06e8",
>             "createdAt": "2023-04-14T16:04:51.449Z",
>             "updatedAt": "2023-04-14T16:04:51.449Z",
>             "environment": {
>               "id": "73056e49-0ebc-4a58-a126-dc9e1efb4ffe"
>             },
>             "user": {
>               "id": "5a942438-cca2-4edd-ac53-c1384c6e0329"
>             },
>             "digitalWallet": {
>               "id": "11dd742c-9f9b-4bde-b8f7-1ce6c8f56c3d"
>             },
>             "challenge": "qid86j8gjbfb3oj3",
>             "qrUrl": "https://api-test.pingone.com/v1/distributedid/requests/057d510a-860f-493f-b969-9206920cb416"
>           },
>           "notification": {
>             "methods": [
>               "EMAIL",
>               "SMS"
>             ],
>             "results": [
>               {
>                 "method": "EMAIL",
>                 "sent": true,
>                 "notification": {
>                   "id": "00be2a92-3df7-4817-aa21-f835f91f3da9"
>                 }
>               },
>               {
>                 "method": "SMS",
>                 "sent": true,
>                 "notification": {
>                   "id": "0064c622-d8b2-4141-bc3f-b017f677a08a"
>                 }
>               }
>             ]
>           }
>         }
>       ]
>     }
>   }
> }
> ```

### Read User Wallet

Return a specified digital wallet for a user

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Digital Wallet ID textField
>
>   Identifier (UUID) of the digital wallet associated with the provisioned credential.
>
> - User ID textField
>
>   PingOne user ID
>
> * default object
>
>   * properties object
>
>     * digitalWalletId string required minLength: 0 maxLength: 100
>
>       Digital Wallet Id
>
>     * userId string required minLength: 0 maxLength: 100
>
>       User Id
>
> - output object
>
>   * userDigitalWallet object
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
>     * digitalWalletApplication object
>
>       * id string
>
>     * status string
>
>     * createdAt string
>
>     * updatedAt string
>
>     * pairingSession
>
>     * id string
>
>     * createdAt string
>
>     * updatedAt string
>
>     * environment object
>
>       * id string
>
>     * user object
>
>       * id string
>
>     * digitalWallet object
>
>       * id string
>
>     * challenge string
>
>     * qrUrl string
>
>     * status string
>
>     * notification object
>
>       * methods array
>
>     * results array
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
>     * digitalWalletApplication object
>
>       * id string
>
>     * status string
>
>     * createdAt string
>
>     * updatedAt string
>
>     * pairingSession
>
>     * id string
>
>     * createdAt string
>
>     * updatedAt string
>
>     * environment object
>
>       * id string
>
>     * user object
>
>       * id string
>
>     * digitalWallet object
>
>       * id string
>
>     * challenge string
>
>     * qrUrl string
>
>     * status string
>
>     * notification object
>
>       * methods array
>
>     * results array
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
>     "userDigitalWallet": {
>       "id": "43148164-4a97-4c57-9db6-918a73f6f6ac",
>       "createdAt": "2023-03-02T18:22:38.366Z",
>       "updatedAt": "2023-03-02T18:22:38.366Z",
>       "environment": {
>         "id": "6a2b43f8-457f-45ab-bcdd-2e001f095e46"
>       },
>       "user": {
>         "id": "3d930cdf-9dd2-42b7-b9be-99540ea3469f"
>       },
>       "digitalWalletApplication": {
>         "id": "f7ae218d-83de-41f8-8ae5-f2ce78a84623"
>       },
>       "status": "PAIRING_REQUIRED",
>       "pairingSession": {
>         "id": "7829a13d-45b7-4416-804b-6d552e2cb3bd",
>         "createdAt": "2023-03-02T18:22:38.366Z",
>         "updatedAt": "2023-03-02T18:22:38.366Z",
>         "environment": {
>           "id": "6a2b43f8-457f-45ab-bcdd-2e001f095e46"
>         },
>         "user": {
>           "id": "3d930cdf-9dd2-42b7-b9be-99540ea3469f"
>         },
>         "digitalWallet": {
>           "id": "43148164-4a97-4c57-9db6-918a73f6f6ac"
>         },
>         "challenge": "p829otr1e433tep2",
>         "qrUrl": "https://api-test.pingone.com/v1/distributedid/requests/fcbd2ad7-887b-41d5-9fdc-970273b5ec78",
>         "status": "INITIAL"
>       },
>       "notification": {
>         "methods": [
>           "EMAIL",
>           "SMS"
>         ],
>         "results": [
>           {
>             "method": "EMAIL",
>             "sent": false,
>             "error": {
>               "id": "c4211b03-2734-4d9a-8a80-3934d2ec1796",
>               "code": "NOT_FOUND",
>               "message": "The request could not be completed. The requested resource was not found."
>             }
>           },
>           {
>             "method": "SMS",
>             "sent": false,
>             "error": {
>               "id": "c4211b03-2734-4d9a-8a80-3934d2ec1796",
>               "code": "NOT_FOUND",
>               "message": "The request could not be completed. The requested resource was not found."
>             }
>           }
>         ]
>       }
>     }
>   }
> }
> ```

### Pair User Wallet to Application

Create a digital wallet and pair it to an application for a user

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Notification Methods dropDownMultiSelect
>
>   * Email
>
>   * SMS
>
> - User ID textField
>
>   PingOne user ID
>
> * default object
>
>   * properties object
>
>     * notificationMethods array uniqueItems: true
>
>     * userId string required minLength: 0 maxLength: 100
>
>       User Id
>
> - output object
>
>   * userDigitalWallet object
>
>     * \_links object
>
>       * environment object
>
>         * href string
>
>       * digitalWalletApplications object
>
>         * href string
>
>       * qrUrl object
>
>         * href string
>
>       * appOpen object
>
>         * href string
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
>     * digitalWalletApplication object
>
>       * id string
>
>     * status string
>
>     * createdAt string
>
>     * updatedAt string
>
>     * pairingSession object
>
>       * id string
>
>       * createdAt string
>
>       * updatedAt string
>
>       * environment object
>
>         * id string
>
>       * user object
>
>         * id string
>
>       * digitalWallet object
>
>         * id string
>
>       * challenge string
>
>       * qrUrl string
>
>       * status string
>
>     * notification object
>
>       * methods array
>
>     * results array
>
>   * rawResponse object
>
>     * \_links object
>
>       * environment object
>
>         * href string
>
>       * digitalWalletApplications object
>
>         * href string
>
>       * qrUrl object
>
>         * href string
>
>       * appOpen object
>
>         * href string
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
>     * digitalWalletApplication object
>
>       * id string
>
>     * status string
>
>     * createdAt string
>
>     * updatedAt string
>
>     * pairingSession object
>
>       * id string
>
>       * createdAt string
>
>       * updatedAt string
>
>       * environment object
>
>         * id string
>
>       * user object
>
>         * id string
>
>       * digitalWallet object
>
>         * id string
>
>       * challenge string
>
>       * qrUrl string
>
>       * status string
>
>     * notification object
>
>       * methods array
>
>     * results array
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
>     "userDigitalWallet": {
>       "_links": {
>         "environment": {
>           "href": "https://api.test-one-pingone.com/v1/environments/18889d16-ea1b-4350-b4a7-be55faea0ebb"
>         },
>         "digitalWalletApplications": {
>           "href": "https://api.test-one-pingone.com/v1/environments/18889d16-ea1b-4350-b4a7-be55faea0ebb/digitalWalletApplications/985fd4b0-6802-402d-917a-5420b4ca5eff"
>         },
>         "appOpen": {
>           "href": "https://neowallet.ping-eng.com/appopen/?u=https%3A%2F%2Fapi.test-one-pingone.com%2Fv1%2Fdistributedid%2Frequests%2F8f4281ad-cc4d-43b0-bfc2-3059da8a4c0a"
>         },
>         "qrUrl": {
>           "href": "https://api.test-one-pingone.com/v1/distributedid/requests/8f4281ad-cc4d-43b0-bfc2-3059da8a4c0a"
>         }
>       },
>       "environment": {
>         "id": "18889d16-ea1b-4350-b4a7-be55faea0ebb"
>       },
>       "user": {
>         "id": "0b229251-0fba-472d-adf9-450dea1e237d"
>       },
>       "digitalWalletApplication": {
>         "id": "985fd4b0-6802-402d-917a-5420b4ca5eff"
>       },
>       "status": "PAIRING_REQUIRED",
>       "pairingSession": {
>         "id": "6e244046-1f91-4fc2-86c7-b8365a3b6284",
>         "createdAt": "2025-01-28T00:30:54.729645592Z",
>         "updatedAt": "2025-01-28T00:30:54.729645842Z",
>         "environment": {
>           "id": "18889d16-ea1b-4350-b4a7-be55faea0ebb"
>         },
>         "user": {
>           "id": "0b229251-0fba-472d-adf9-450dea1e237d"
>         },
>         "digitalWallet": {
>           "id": "f121ef78-4ebe-42b0-82e4-32232c77d7da"
>         },
>         "challenge": "3caois8okj6m436o",
>         "qrUrl": "https://api.test-one-pingone.com/v1/distributedid/requests/8f4281ad-cc4d-43b0-bfc2-3059da8a4c0a"
>       },
>       "notification": {
>         "methods": [
>           "EMAIL",
>           "SMS"
>         ],
>         "results": [
>           {
>             "method": "EMAIL",
>             "sent": true,
>             "notification": {
>               "id": "00cbf8d0-d2d5-4266-9214-99ee270b5448"
>             }
>           },
>           {
>             "method": "SMS",
>             "sent": true,
>             "notification": {
>               "id": "00c0312f-c031-48d5-b60e-5424a4ee25cb"
>             }
>           }
>         ]
>       },
>       "id": "f121ef78-4ebe-42b0-82e4-32232c77d7da"
>     }
>   }
> }
> ```

### Update User Wallet

Update the status of a digital wallet for a user

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
>   PingOne user ID
>
> - Digital Wallet ID textField
>
>   Identifier (UUID) of the digital wallet associated with the provisioned credential.
>
> - Status dropDown
>
>   Status of the wallet
>
>   * ACTIVE (Default)
>
>   * DISABLED
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>       User Id
>
>     * digitalWalletId string required minLength: 0 maxLength: 100
>
>       Digital Wallet Id
>
>     * digitalWalletStatus string required minLength: 0 maxLength: 100
>
>       Digital Wallet Status
>
> - output object
>
>   * userDigitalWallet object
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
>     * digitalWalletApplication object
>
>       * id string
>
>     * status string
>
>     * applicationInstance object
>
>       * id string
>
>     * deviceData object
>
>       * appPackage string
>
>       * sdkVersion string
>
>       * osType string
>
>       * osVersion string
>
>       * manufacturer string
>
>       * model string
>
>       * pushSandbox boolean
>
>       * pushToken string
>
>     * createdAt string
>
>     * updatedAt string
>
>     * notification object
>
>       * methods array
>
>     * results array
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
>     * digitalWalletApplication object
>
>       * id string
>
>     * status string
>
>     * applicationInstance object
>
>       * id string
>
>     * deviceData object
>
>       * appPackage string
>
>       * sdkVersion string
>
>       * osType string
>
>       * osVersion string
>
>       * manufacturer string
>
>       * model string
>
>       * pushSandbox boolean
>
>       * pushToken string
>
>     * createdAt string
>
>     * updatedAt string
>
>     * notification object
>
>       * methods array
>
>     * results array
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
>     "userDigitalWallet": {
>       "environment": {
>         "id": "18889d16-ea1b-4350-b4a7-be55faea0ebb"
>       },
>       "user": {
>         "id": "0b229251-0fba-472d-adf9-450dea1e237d"
>       },
>       "digitalWalletApplication": {
>         "id": "985fd4b0-6802-402d-917a-5420b4ca5eff"
>       },
>       "status": "DISABLED",
>       "applicationInstance": {
>         "id": "a5683da7-b7c6-4189-9c54-999ad5aa896b"
>       },
>       "deviceData": {
>         "appPackage": "com.pingidentity.pingonewallet.sample",
>         "sdkVersion": "1.1.0",
>         "osType": "IOS",
>         "osVersion": "18.1.1",
>         "manufacturer": "Apple",
>         "model": "iPhone15,2",
>         "pushSandbox": false,
>         "pushToken": "1077a9061162cdd15ddd682f7420479dafb66efe6c65eaced8f8c0f01746ab2e"
>       },
>       "notification": {
>         "methods": [
>           "EMAIL",
>           "SMS"
>         ],
>         "results": [
>           {
>             "method": "EMAIL",
>             "sent": true,
>             "notification": {
>               "id": "0069d1d2-d91e-405d-992d-c6eb40a44f82"
>             }
>           },
>           {
>             "method": "SMS",
>             "sent": true,
>             "notification": {
>               "id": "009d97e7-876e-4652-b74e-96511f491e73"
>             }
>           }
>         ]
>       },
>       "pairingAttempts": [
>         {
>           "success": true,
>           "attemptedAt": "2025-01-26T23:22:48.330480980Z"
>         }
>       ],
>       "id": "7a70cefe-d375-40ff-a1ce-510491b91ca9",
>       "createdAt": "2025-01-26T23:22:30.325Z",
>       "updatedAt": "2025-01-29T19:19:19.207542024Z"
>     }
>   }
> }
> ```

### Delete User Digital Wallet

Remove a digital wallet and all associated credentials for a user

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
>   PingOne user ID
>
> - Digital Wallet ID textField
>
>   Identifier (UUID) of the digital wallet associated with the provisioned credential.
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>       User Id
>
>     * digitalWalletId string required minLength: 0 maxLength: 100
>
>       Digital Wallet Id
>
> - output object
>
>   * rawResponse object
>
>   * headers object
>
>   * statusCode integer

### Read Credential

Read a credential

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Credential ID textField
>
>   Identifier (UUID) of the provisioned user credential
>
> - User ID textField
>
>   PingOne user ID
>
> * default object
>
>   * properties object
>
>     * credentialId string required minLength: 0 maxLength: 100
>
>       Credential ID
>
>     * userId string required minLength: 0 maxLength: 100
>
>       User Id
>
> - output object
>
>   * userCredential object
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
>     * credentialType object
>
>       * id string
>
>       * version object
>
>         * number number
>
>         * uri string
>
>     * title string
>
>     * status string
>
>     * createdAt string
>
>     * updatedAt string
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
>     * credentialType object
>
>       * id string
>
>       * version object
>
>         * number number
>
>         * uri string
>
>     * title string
>
>     * status string
>
>     * createdAt string
>
>     * updatedAt string
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
>     "userCredential": {
>       "id": "31175df4-207d-411e-a6d3-95090bc1b000",
>       "createdAt": "2025-01-26T20:50:09.116Z",
>       "updatedAt": "2025-01-26T22:03:07.640Z",
>       "environment": {
>         "id": "18889d16-ea1b-4350-b4a7-be55faea0ebb"
>       },
>       "user": {
>         "id": "0b229251-0fba-472d-adf9-450dea1e237d"
>       },
>       "credentialType": {
>         "id": "20d91c39-a84f-410c-b07e-6594a2c862a0",
>         "version": {
>           "number": 1,
>           "uri": "https://api.test-one-pingone.com/v1/distributedid/credentialTypes/20d91c39-a84f-410c-b07e-6594a2c862a0/v1"
>         }
>       },
>       "title": "verifiedEmployee",
>       "status": "ISSUED"
>     }
>   }
> }
> ```

### Read All Credentials

Return all credentials for a user

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
>   PingOne user ID
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>       User Id
>
> - output object
>
>   * userCredentials object
>
>     * \_embedded object
>
>       * items array
>
>     * size number
>
>   * rawResponse object
>
>     * \_embedded object
>
>       * items array
>
>     * size number
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
>     "userCredentials": {
>       "_embedded": {
>         "items": [
>           {
>             "id": "31175df4-207d-411e-a6d3-95090bc1b000",
>             "createdAt": "2025-01-26T20:50:09.116Z",
>             "updatedAt": "2025-01-26T22:03:07.640Z",
>             "environment": {
>               "id": "18889d16-ea1b-4350-b4a7-be55faea0ebb"
>             },
>             "user": {
>               "id": "0b229251-0fba-472d-adf9-450dea1e237d"
>             },
>             "credentialType": {
>               "id": "20d91c39-a84f-410c-b07e-6594a2c862a0",
>               "version": {
>                 "number": 1,
>                 "uri": "https://api.test-one-pingone.com/v1/distributedid/credentialTypes/20d91c39-a84f-410c-b07e-6594a2c862a0/v1"
>               }
>             },
>             "title": "verifiedEmployee",
>             "status": "ISSUED"
>           }
>         ]
>       },
>       "size": 1
>     }
>   }
> }
> ```

### Revoke Credential

Revoke a user's credential

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
>   PingOne user ID
>
> - Credential ID textField
>
>   Identifier (UUID) of the provisioned user credential
>
> - Notification Methods dropDownMultiSelect
>
>   * Email
>
>   * SMS
>
> * default object
>
>   * properties object
>
>     * userId string required minLength: 0 maxLength: 100
>
>       User Id
>
>     * credentialId string required minLength: 0 maxLength: 100
>
>       Credential ID
>
>     * notificationMethods array uniqueItems: true
>
> - output object
>
>   * userCredential object
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
>     * credentialType object
>
>       * id string
>
>       * version object
>
>         * number integer
>
>         * uri string
>
>     * title string
>
>     * status string
>
>     * createdAt string
>
>     * updatedAt string
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
>     * credentialType object
>
>       * id string
>
>       * version object
>
>         * number integer
>
>         * uri string
>
>     * title string
>
>     * status string
>
>     * createdAt string
>
>     * updatedAt string
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
>     "userCredential": {
>       "id": "31175df4-207d-411e-a6d3-95090bc1b000",
>       "createdAt": "2025-01-26T20:50:09.116Z",
>       "updatedAt": "2025-01-29T15:55:34.604072679Z",
>       "environment": {
>         "id": "18889d16-ea1b-4350-b4a7-be55faea0ebb"
>       },
>       "user": {
>         "id": "0b229251-0fba-472d-adf9-450dea1e237d"
>       },
>       "credentialType": {
>         "id": "20d91c39-a84f-410c-b07e-6594a2c862a0",
>         "version": {
>           "number": 1,
>           "uri": "https://api.test-one-pingone.com/v1/distributedid/credentialTypes/20d91c39-a84f-410c-b07e-6594a2c862a0/v1"
>         }
>       },
>       "title": "verifiedEmployee",
>       "status": "REVOKED",
>       "expiresAt": "2025-01-29T15:55:33.325Z"
>     }
>   }
> }
> ```

### Issue/Update/Revoke Credential(s)

Apply credential issuance rule to staged changes

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Apply Issue for User ID(s) textFieldArrayView
>
>   Array of one or more user IDs for which credentials should be issued
>
> - Apply Update for User ID(s) textFieldArrayView
>
>   Array of one or more identifiers (UUIDs) of users whose credentials are in an update action state and should be updated
>
> - Apply Revoke for User ID(s) textFieldArrayView
>
>   Array of one or more identifiers (UUIDs) of users whose credentials are in a revoke action state and should be revoked
>
> - Issuance Rule ID textField
>
>   Identifier (UUID) of the credential issuance rule.
>
> - Credential Type ID textField
>
>   Identifier (UUID) associated with the credential type.
>
> * default object
>
>   * properties object
>
>     * applyIssue array uniqueItems: true
>
>       Issue
>
>     * applyUpdate array uniqueItems: true
>
>       Update
>
>     * applyRevoke array uniqueItems: true
>
>       Revoke
>
>     * issuanceRuleId string required minLength: 0 maxLength: 100
>
>       Issuance Rule Id
>
>     * credentialTypeId string required minLength: 0 maxLength: 100
>
>       Credential Type ID
>
> - output object
>
>   * stagedChanges object
>
>     * \_embedded object
>
>       * stagedChanges array
>
>     * size number
>
>   * rawResponse object
>
>     * \_embedded object
>
>       * stagedChanges array
>
>     * size number
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
>     "stagedChanges": {
>       "_embedded": {
>         "stagedChanges": [
>           {
>             "environment": {
>               "id": "e43b0fcb-f382-439f-a812-5fe72ee03c70"
>             },
>             "credentialType": {
>               "id": "bdb8e84c-b26c-4f5f-a0dd-bc263b548efe"
>             },
>             "issuanceRule": {
>               "id": "3320b796-d12d-48f8-a49a-2a48a29e9f50"
>             },
>             "user": {
>               "id": "4bed75bf-54a2-421f-a42c-597c39b261f7"
>             },
>             "action": "ISSUE",
>             "scheduled": false,
>             "id": "78cdc229-858f-4ae7-80b6-73349b2cfea7",
>             "createdAt": "2023-04-04T21:46:03.249Z"
>           }
>         ]
>       },
>       "size": 1
>     }
>   }
> }
> ```

### Create Verification Session

Begin a session to verify a user's credential

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Message textField
>
>   A message shown to the user by the compatible wallet app to alert the user
>
> - Protocol dropDown
>
>   Protocol to use for verification; can be OPENID4VP or NATIVE. Defaults to NATIVE.
>
>   * NATIVE (Default)
>
>   * OPENID4VP
>
> - Application Instance textField
>
>   Application Instance Id.
>
> - didMethod dropDown
>
>   DID Method
>
>   * WEB (Default)
>
>   * JWK
>
>   * ION
>
> - Filter by DIDs textFieldArrayView
>
>   Array of unique decentralized identifiers (DIDs) to be searched for the Issuer of the presented credential (OPENID4VP only).
>
> - Filter by PingOne Environment ID textFieldArrayView
>
>   Array of PingOne environment IDs to be searched for the Issuer of the presented credential.
>
> - Requested Credentials variableInputList
>
>   Requested Credentials. Variable Name ⇒credential type, value⇒(comma separated keys)
>
> - Notification Locale textField
>
>   Add a locale to allow localized notifications for end-users. ISO Language Codes are supported.
>
> - Custom Value textField
>
>   You can enter a custom template name, or leave blank to use the default template. You can also enter a parameter from a previous connector, or any text.
>
> - Notification Variables variableInputList
>
>   If Custom variables are defined in the notification body, map them here.
>
> * default object
>
>   * properties object
>
>     * message string minLength: 0 maxLength: 100
>
>       Message
>
>     * protocol string required minLength: 0 maxLength: 100
>
>       didMethod
>
>     * applicationInstance string minLength: 0 maxLength: 100
>
>       Application Instance Id
>
>     * issuerFilterDids array uniqueItems: true
>
>       Issue Filter Dids
>
>     * issuerFilterEnvIds array uniqueItems: true
>
>       Issue Filter Environment Ids
>
>     * requestedCredentials array
>
>       Requested Credentials
>
>     * templateLocale null/string
>
>     * templateVariant null/string
>
>     * templateVariables array
>
> - output object
>
>   * credVerPresentationSession object
>
>     * \_links object
>
>       * qr object
>
>         * href string
>
>       * appOpenUrl object
>
>         * href string
>
>     * id string
>
>     * qrCodeImage string
>
>     * osType string
>
>     * status string
>
>     * createdAt string
>
>     * expiresAt string
>
>     * applicationInstance object
>
>       * id string
>
>     * notification object
>
>       * template object
>
>         * locale string
>
>         * variant string
>
>         * variables object string
>
>   * rawResponse object
>
>     * \_links object
>
>       * qr object
>
>         * href string
>
>       * appOpenUrl object
>
>         * href string
>
>     * id string
>
>     * qrCodeImage string
>
>     * osType string
>
>     * status string
>
>     * createdAt string
>
>     * expiresAt string
>
>     * applicationInstance object
>
>       * id string
>
>     * notification object
>
>       * template object
>
>         * locale string
>
>         * variant string
>
>         * variables object string
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
>     "credVerPresentationSession": {
>       "_links": {
>         "qr": {
>           "href": " data:image/png;base64,iVBORw0KGgoAAAANSUhEU....."
>         },
>         "appOpenUrl": {
>           "href": "openid-vc://?request_uri=https://api-test.pingone.com/v1/distributedid/verifications/presentationSessions/8460cee9-74ae-4bb8-a8de-38830dbf19c2/requestSD"
>         }
>       },
>       "id": "8460cee9-74ae-4bb8-a8de-38830dbf19c2",
>       "status": "INITIAL",
>       "applicationInstance": {
>         "id": "b378c504-3b26-4be1-a9a0-85b5ba12b142"
>       },
>       "createdAt": "2025-01-13T14:00:21.181885042Z",
>       "expiresAt": "2025-01-13T14:05:21.181883482Z",
>       "notification": {
>         "template": {
>           "locale": "en",
>           "variant": "variant_B",
>           "variables": {
>             "name": "foo",
>             "family": "foo1"
>           }
>         }
>       }
>     }
>   }
> }
> ```

### Poll for Verification Status

Return the status of a verification session

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Credential Verification ID textField
>
>   Identifier (UUID) of the verification credential data
>
> * default object
>
>   * properties object
>
>     * credentialsVerificationId string required minLength: 0 maxLength: 100
>
>       Credentials Verification ID
>
> - output object
>
>   * credVerificationStatus object
>
>     * id string
>
>     * qrCodeImage string
>
>     * osType string
>
>     * status string
>
>   * rawResponse object
>
>     * id string
>
>     * qrCodeImage string
>
>     * osType string
>
>     * status string
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
>     "credVerificationStatus": {
>       "id": "a5efb6a1-c8bf-4fc7-b550-78d5707e0761",
>       "status": "INITIAL"
>     }
>   }
> }
> ```

### Return Verification Data

Return data from verified credential

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Credential Verification ID textField
>
>   Identifier (UUID) of the verification credential data
>
> * default object
>
>   * properties object
>
>     * credentialsVerificationId string required minLength: 0 maxLength: 100
>
>       Credentials Verification ID
>
> - output object
>
>   * credVerificationData object
>
>     * id string
>
>     * status string
>
>     * sessionData object
>
>       * id string
>
>       * credentialsDataList array
>
>   * rawResponse object
>
>     * id string
>
>     * status string
>
>     * sessionData object
>
>       * id string
>
>       * credentialsDataList array
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
>     "credVerificationData": {
>       "id": "10d5bab3-70e0-4e05-871e-04ef9c4b297b",
>       "status": "VERIFICATION_SUCCESSFUL",
>       "sessionData": {
>         "id": "10d5bab3-70e0-4e05-871e-04ef9c4b297b",
>         "credentialsDataList": [
>           {
>             "issuerId": "e43b0fcb-f382-439f-a812-5fe72ee03c70",
>             "issuerName": "Issuer name",
>             "type": "VerifiedEmployee",
>             "data": [
>               {
>                 "key": "CardImage",
>                 "value": "<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 740 480\"><rect fill=\"none\" width=\"736\" height=\"476\" stroke=\"#CACED3\" stroke-width=\"3\" rx=\"10\" ry=\"10\" x=\"2\" y=\"2\"></rect><rect fill=\"#FFFFFF\" height=\"476\" rx=\"10\" ry=\"10\" width=\"736\" x=\"2\" y=\"2\" opacity=\"50\"></rect><image href=\"\" opacity=\"50\" height=\"476\" rx=\"10\" ry=\"10\" width=\"736\" x=\"2\" y=\"2\"></image><line y2=\"160\" x2=\"695\" y1=\"160\" x1=\"42.5\" stroke=\"#000000\"></line><text fill=\"#000000\" font-weight=\"450\" font-size=\"30\" x=\"45\" y=\"90\">VerifiedEmployee</text><text fill=\"#000000\" font-size=\"25\" font-weight=\"300\" x=\"45\" y=\"130\">Target</text><text fill=\"#000000\" font-weight=\"500\" font-size=\"20\" x=\"50\" y=\"228\">First Name: M</text><text fill=\"#000000\" font-weight=\"500\" font-size=\"20\" x=\"50\" y=\"278\">Last Name: </text></svg>"
>               },
>               {
>                 "key": "First Name",
>                 "value": "M"
>               }
>             ],
>             "verificationStatus": "VALID"
>           }
>         ]
>       }
>     }
>   }
> }
> ```