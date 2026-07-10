---
title: PingOne Authorize node
description: Configure the PingOne Authorize node to send policy decision requests to a PingOne Authorize environment and evaluate authorization levels in a journey.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:pingone:pingone-authorize
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-authorize.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  example: Example
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  outcomes: Outcomes
---

# PingOne Authorize node

The PingOne Authorize node sends a decision request to a specified decision endpoint in your PingOne Authorize environment. These authorizations include:

* [Evaluate a Decision Request](https://developer.pingidentity.com/pingone-api/authorize/authorization-decisions/decision-evaluation/execute-a-decision-request.html)

* [Authorize Client with Individual Decision](https://developer.pingidentity.com/pingauthorize/pingauthorize/policy-decision/json-pdp/individual-requests/authorize-client-with-individual-decision.html)

To use the PingOne Authorize node, you must first set up the [PingOne Service](pingone-service.html).

## Example

The following example journey illustrates how to use the PingOne Authorize node:

![PingOne Authorize node example](_images/p1-authorize-journey.png)

The PingOne Authorize node gets the username from Username Collector node and evaluates the level authorization for the user. Based on the authorization level, further action is taken.

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes 1      |
| Ping Identity Platform (self-managed) | Yes 1      |

1 For self-managed products, download the node from the [Ping Identity Marketplace](https://marketplace.pingone.com/item/ping-authorize).

## Inputs

This node retrieves the attribute map from the shared state.

Additionally, the node first attempts to locate in shared state the `PingOne Authorize Policy Attribute(s)` defined in the policy that corresponds to the active decision endpoint.

## Dependencies

You must set up the following before using the PingOne Authorize node:

* [Authorization policies](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_policies.html)

* [Adding a worker application for the PingOne Authorize service](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_adding_worker_app.html)

  * Requires the [Identity Data Admin](https://developer.pingidentity.com/pingone-api/platform/roles.html) role

* [Connect AM to PingOne](https://docs.pingidentity.com/pingam/8.1/integrations/connect-am-to-pingone.html)

## Configuration

| Property               | Usage                                                                                                                                                                                                                                                                                                            |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PingOne Worker Service | Service for specific PingOne Worker application.                                                                                                                                                                                                                                                                 |
| Decision Endpoint ID   | The Decision Endpoint ID from the PingOne Authorize service.                                                                                                                                                                                                                                                     |
| Attribute Map          | The attribute map is to overcome the name differences between shared state attributes in PingOne Advanced Identity Cloud and the request parameters in PingOne. For example, if the shared store `firstName` refers to `givenName` in PingOne, then the `Attribute Map` entry would be: `firstName ⇒ givenName`. |
| Statement Codes        | Set the node outcomes based on the statements from the PingOne Authorize decision.                                                                                                                                                                                                                               |
| Continue               | Use the `Continue` toggle for a single outcome case.                                                                                                                                                                                                                                                             |

## Outputs

This node doesn't change the shared state.

## Outcomes

* `Permit`

  Satisfied the active policy's permit condition and authorized the user.

* `Deny`

  Satisfied the active policy's deny condition and did not authorize the user.

* `Indeterminate`

  Does not satisfy the active policy's permit or deny conditions.

* `Error`

  There was an error during the authorization process.

  If this node logs an error, review the log messages to find the reason for the error and address the issue appropriately.

---

---
title: PingOne Create User node
description: Configure the PingOne Create User node to create new users, including their profile data or as anonymized users, in the PingOne platform during a journey.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:pingone:pingone-create-user
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-create-user.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  example: Example
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  callbacks: Callbacks
  outcomes: Outcomes
---

# PingOne Create User node

The PingOne Create User node can create new users in the PingOne platform.

You can configure the node to create a user including their profile data or to create an anonymized user.

## Example

The following example journey integrates PingOne Verify to perform user identity verification.

![Example PingOne Verify journey](_images/pingone-verify-example-journey-full.png)Figure 1. Example PingOne Verify journey

* The user enters their credentials and the [Data Store Decision node](../data-store-decision.html) matches them against the identity store.

* a The [PingOne Identity Match node](pingone-identity-match.html) checks PingOne for a matching user.

* b If a user is found, the [PingOne Verify Completion Decision node](pingone-verify-completion-decision.html) checks the user's most recent verification transaction to determine the status:

  * Success

    The user successfully completed the most recent PingOne Verify transaction, so the journey progresses directly to the Success node and authentication is successful.

  * Not Completed

    The user has an existing PingOne Verify transaction in progress, so the journey resumes the existing verification transaction.

    The node adds the user's existing transaction ID to the shared node state in a variable named `pingOneVerifyTransactionId`.

  * Not Started / Failure / Expired

    * The user doesn't have an existing PingOne Verify transaction (`Not Started`)

    * The user hasn't successfully completed the most recent PingOne Verify transaction

    * The most recent PingOne Verify transaction has expired

    The journey continues to start a new verification transaction.

* c If no matching user is found, the [PingOne Create User node](pingone-create-user.html) creates a new user in PingOne.

* d The [PingOne Verify Evaluation node](pingone-verify-evaluation.html) starts a new PingOne Verify evaluation or continues an existing evaluation if `pingOneVerifyTransactionId` is present in the shared node state. The node either completes or fails the journey based on the result.

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | Yes        |

## Inputs

This node reads the `username` field from the shared node state to access the user's identity profile.

Implement a [Username Collector node](../am-only/username-collector.html) (standalone AM) or [Platform Username node](../platform-username.html) (Ping Identity Platform deployments) earlier in the journey.

## Dependencies

This node requires a PingOne Worker Service configuration so that it can authenticate to your PingOne instance.

Find more information in [Connect AM to PingOne](https://docs.pingidentity.com/pingam/8.1/integrations/connect-am-to-pingone.html).

## Configuration

| Property                  | Usage                                                                                                                                                                                                                                                                                                      |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PingOne Worker Service ID | The ID of the PingOne worker service for connecting to PingOne.                                                                                                                                                                                                                                            |
| Population ID             | The ID of the population in PingOne to check for users or provision new ones.If not specified, the node uses the environment's default population ID.                                                                                                                                                      |
| Anonymized user           | When enabled, the node creates a user in PingOne with only a unique identifier and a language attribute.It does not add any other profile attributes, helping prevent any personally identifiable information (PII) from being shared.                                                                     |
| AM Identity Attribute     | The attribute from the user's AM profile that the node uses as the username for the account created in PingOne.&#xA;&#xA;When creating anonymized users, choose a profile attribute that does not contain PII.Default: `uid`                                                                               |
| Capture failure           | Capture the details in shared state if a failure occurs.The node stores the details in a variable named `pingOneCreateUserFailureReason`.Default: `False`Example:```json
{
  "code": "MISSING_ATTRIBUTE_FROM_PROFILE",
  "message": "Could not get attribute from user profile.",
  "exception": "",
}
``` |

## Outputs

If the node was able to create a new user in PingOne it stores the PingOne user identifier in a state variable named `pingOneUserId`. For example `a648aaac-ch15-b357-457b-8d2e714180ff`.

If you select Capture failure, the node stores any error response in a shared state variable named `pingOneCreateUserFailureReason`.

## Callbacks

This node doesn't send any callbacks.

## Outcomes

`True`

The node created an account in PingOne.

`False`

The node did not create an account in PingOne.

The journey also uses this outcome if any error occurs. Enable Capture Failure to store the details in node state.

---

---
title: PingOne Credentials Delete Wallet node
description: Configure the PingOne Credentials Delete Wallet node to remove a paired digital wallet from a PingOne user during a journey.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:pingone:pingone-cred-delete-wallet
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-cred-delete-wallet.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  example: Example
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  outcomes: Outcomes
  errors: Errors
---

# PingOne Credentials Delete Wallet node

The PingOne Credentials Delete Wallet node lets you remove a paired digital wallet from a PingOne user.

## Example

Learn more in an [example journey using PingOne Credentials nodes](pingone-cred-overview.html#p1-cred-example-journey).

## Inputs

This node retrieves the `pingOneUserId` and `pingOneWalletId` from the journey state.

## Dependencies

This node requires that the PingOne Worker Service is configured so that it can connect to your PingOne instance and remove a paired digital wallet from the PingOne user.

## Configuration

| Property                    | Usage                                                                                                                        |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| PingOne Worker service ID   | The ID of the PingOne Worker service for connecting to PingOne.                                                              |
| PingOne UserID Attribute    | Local attribute name from which to retrieve `pingOneUserId`. The journey state is first looked up, then the local datastore. |
| Digital Wallet ID Attribute | Local attribute name to retrieve the digital wallet ID from the journey state.                                               |

## Outputs

This node doesn't change the shared state.

## Outcomes

* `Success`

  The wallet is successfully removed.

* `Not Found`

  No digital wallet was found to remove.

* `Error`

  There was an error during the wallet removal process.

## Errors

If the API call to PingOne Credentials fails, the following error is logged:

* `Error: PingOne Credentials Delete a Digital Wallet - Status Code - Response Body`

---

---
title: PingOne Credentials Find Wallets node
description: Configure the PingOne Credentials Find Wallets node to list all paired digital wallets for a PingOne user during a journey.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:pingone:pingone-cred-find-wallet
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-cred-find-wallet.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  example: Example
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  outcomes: Outcomes
  errors: Errors
---

# PingOne Credentials Find Wallets node

The PingOne Credentials Find Wallets node lets you list all paired digital wallets from the PingOne user.

## Example

Learn more in an [example journey using PingOne Credentials nodes](pingone-cred-overview.html#p1-cred-example-journey).

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | Yes        |

## Inputs

To perform the wallet look up, this node requires the PingOne User ID (UUID). The node first attempts to get the UUID from the `pingOneUserId` attribute. If `pingOneUserId` attribute is not set, then it gets the UUID from the `pingOneUserId` as a child attribute in `objectAttributes` in the shared state.

## Dependencies

This node requires that the PingOne Worker Service is configured so that it can connect to your PingOne instance and list the paired wallets of a user.

## Configuration

| Property                 | Usage                                                                                                                        |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| PingOne Service          | The ID of the PingOne Worker service for connecting to PingOne.                                                              |
| PingOne UserID Attribute | Local attribute name from which to retrieve `pingOneUserId`. The journey state is first looked up, then the local datastore. |

## Outputs

* `pingOneWalletId`: The PingOne digital wallet ID.

* `pingOneApplicationInstanceId`: The Application Instance ID of the digital wallet where the credential was stored.

* `pingOneActiveWallets`: The PingOne User's active digital wallets.

## Outcomes

* `Success`

  One digital wallet was found and returned.

* `Success Many`

  All digital wallets were found and listed.

* `Not Found`

  No digital wallet was found.

* `Error`

  There was an error during the process of finding the wallet.

## Errors

If the API call to PingOne Credentials fails, the following error is logged:

* Error: `PingOne Credentials Find a Wallet- Status Code - Response Body`

---

---
title: PingOne Credentials Issue node
description: "Configure the PingOne Credentials Issue node to create and issue a PingOne digital credential to a user's paired wallet during a journey."
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:pingone:pingone-cred-issue
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-cred-issue.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  example: Example
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  outcomes: Outcomes
  errors: Errors
---

# PingOne Credentials Issue node

The PingOne Credentials Issue node lets you create a PingOne credential in a journey.

## Example

Learn more in an [example journey using PingOne Credentials nodes](pingone-cred-overview.html#p1-cred-example-journey).

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | Yes        |

## Inputs

This node retrieves from the shared state the `pingOneUserId` and shared state attributes defined in the attribute map.

## Dependencies

This node requires that the PingOne Worker Service is configured so that it can connect to your PingOne instance and create a PingOne credential.

## Configuration

| Property                  | Usage                                                                                                                                                                                |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| PingOne Worker service ID | The ID of the PingOne Worker service for connecting to PingOne.                                                                                                                      |
| PingOne UserID Attribute  | Local attribute name from which to retrieve `pingOneUserId`. The journey state is first looked up, then the local datastore.                                                         |
| Credential Type ID        | The requested credential name                                                                                                                                                        |
| Attribute map             | The `Key` - `Value` mapping used for associating journey state attributes with credentials. The `Key` is the P1 Credential attribute, and the `Value` is the shared state attribute. |

## Outputs

`pingOneCredentialId` - The ID of the created credential.

## Outcomes

* `Success`

  The required credential was created and issued successfully.

* `Error`

  There was an error during the process of creating credentials.

## Errors

If the API call to PingOne Credentials fails, the following error is logged:

* Error: PingOne Credentials Create a User Credential

---

---
title: PingOne Credentials nodes
description: Overview of the PingOne Credentials nodes for implementing digital wallet pairing, credential management, and credential verification in PingAM journeys.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:pingone:pingone-cred-overview
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-cred-overview.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  dependencies: Dependencies
  p1-cred-example-journey: Example
---

# PingOne Credentials nodes

The PingOne Credentials nodes use the PingOne Credentials service to implement digital wallet pairing, credential management, and credential verification. You can find detailed information about PingOne Credentials service in [Introduction to PingOne Credentials](https://docs.pingidentity.com/pingone/digital_credentials_using_pingone_credentials/p1_credentials_introduction.html)

The [PingOne Credentials scenarios](https://docs.pingidentity.com/pingone/digital_credentials_using_pingone_credentials/p1_credentials_scenario_intro.html) provide high-level examples of how you can use the service.

To use the PingOne Credentials nodes in your authentication journeys, PingOne Advanced Identity Cloud provides the following artifacts :

* [Connect AM to PingOne](https://docs.pingidentity.com/pingam/8.1/integrations/connect-am-to-pingone.html)

* [PingOne Credentials Find Wallets node](pingone-cred-find-wallet.html)

* [PingOne Credentials Pair Wallet node](pingone-cred-pair-wallet.html)

* [PingOne Credentials Delete Wallet node](pingone-cred-delete-wallet.html)

* [PingOne Credentials Issue node](pingone-cred-issue.html)

* [PingOne Credentials Update node](pingone-cred-update.html)

* [PingOne Credentials Revoke node](pingone-cred-revoke.html)

* [PingOne Credentials Verification node](pingone-cred-verify.html)

## Dependencies

Before using the PingOne Credentials nodes, complete the following tasks:

* [Creating a credential](https://docs.pingidentity.com/pingone/digital_credentials_using_pingone_credentials/p1_credentials_creating_a_credential.html)

* [Adding a worker application for the PingOne Authorize service](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_adding_worker_app.html)

  * Requires the [Identity Data Admin role](https://developer.pingidentity.com/pingone-api/platform/roles.html)

* [Configure the PingOne service](pingone-service.html#configure-p1-service)

## Example

The following example journey shows how to use the PingOne Credentials nodes in a journey:

![PingOne Credentials Example](_images/p1-credentials-example.png)

* The [PingOne Credentials Find Wallets node](pingone-cred-find-wallet.html) searches for actively paired wallets for an end-user.

* The [PingOne Credentials Pair Wallet node](pingone-cred-pair-wallet.html) initiates a request for pairing a digital wallet through an SMS or email to the user, or a QR code that the user must scan with their digital wallet application.

* The [PingOne Credentials Issue node](pingone-cred-issue.html) creates and issues a new credential to the paired wallet using the attributes defined in the shared state.

* The [PingOne Credentials Verification node](pingone-cred-verify.html) initiates a verification request through a QR code the user must scan or a push notification to their digital wallet application.

---

---
title: PingOne Credentials Pair Wallet node
description: Configure the PingOne Credentials Pair Wallet node to pair a PingOne digital wallet with a PingOne user ID during a journey.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:pingone:pingone-cred-pair-wallet
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-cred-pair-wallet.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  example: Example
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  outcomes: Outcomes
  errors: Errors
---

# PingOne Credentials Pair Wallet node

The PingOne Credentials Pair Wallet node lets you pair PingOne digital wallet credentials with a PingOne user ID.

## Example

Learn more in an [example journey using PingOne Credentials nodes](pingone-cred-overview.html#p1-cred-example-journey).

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | Yes        |

## Inputs

This node retrieves `pingOneUserId` from the journey state, or from `objectAtrributes` in the journey state.

## Dependencies

This node requires that the PingOne Worker Service is configured so that it can connect to your PingOne instance and pair digital wallet credentials with a Ping user ID.

## Configuration

| Property                                     | Usage                                                                                                                                                                                                             |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PingOne Worker service ID                    | The ID of the PingOne Worker service for connecting to PingOne.                                                                                                                                                   |
| PingOne UserID Attribute                     | The local attribute name from which to retrieve the PingOne userID. The journey state is first searched for the PingOne User ID. If the ID is not found, the localdatastore is looked up.                         |
| PingOne Wallet Application ID                | Digital Wallet Application ID from PingOne Credentials admin UI.                                                                                                                                                  |
| Digital Wallet Pairing URL delivery method   | The method—​QR Code, email, or SMS used to deliver the digital wallet.                                                                                                                                            |
| Allow user to choose the URL delivery method | If enabled, prompt the user to select the URL delivery method.                                                                                                                                                    |
| Delivery method message                      | The message to display to the user, so that they can select the method—​QRCODE, SMS, or EMAIL, used to receive the pairing URL.                                                                                   |
| QR code message                              | The message with instructions to scan the QR code to begin the digital wallet pairing process.                                                                                                                    |
| Submission timeout                           | Timeout value, in seconds, for pairing the digital wallet.                                                                                                                                                        |
| Waiting Message                              | Localization overrides for the waiting message. This is a mapping of a locale to a message.                                                                                                                       |
| Store Wallet Response                        | Store the list of verified data submitted by the user in the shared state under a key named `pingOneWallet`.	The key is empty if the node is unable to retrieve the wallet pairing data from the PingOne service. |

## Outputs

pingOneWallet - The new PingOne User's digital wallet.

## Outcomes

* `Success`

  All configured checks passed.

* `Error`

  There was an error during the pairing process

* `Time Out`

  The pairing process reached the configured timeout value.

## Errors

If the API call to PingOne Credentials fails, the following error is logged:

* `Error: PingOne Credentials Create a Digital Wallet`

---

---
title: PingOne Credentials Revoke node
description: Configure the PingOne Credentials Revoke node to revoke existing PingOne credentials for a user during a journey.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:pingone:pingone-cred-revoke
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-cred-revoke.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  outcomes: Outcomes
  errors: Errors
---

# PingOne Credentials Revoke node

The PingOne Credentials Revoke node lets you revoke existing PingOne credentials in a journey.

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | Yes        |

## Inputs

This node retrieves the `PingOne User ID` and `Credential Type ID` from the shared state.

## Dependencies

This node requires that the PingOne Worker Service is configured so that it can connect to your PingOne instance and revoke PingOne credentials.

## Configuration

| Property                 | Usage                                                                                                                        |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| PingOne Service          | The ID of the PingOne Worker service for connecting to PingOne.                                                              |
| PingOne UserID Attribute | Local attribute name from which to retrieve `pingOneUserId`. The journey state is first looked up, then the local datastore. |
| Credential ID Attribute  | The local attribute name to retrieve the credential ID from the shared state.                                                |

## Outputs

This node doesn't change the shared state.

## Outcomes

* `Success`

  The credential is successfully revoked.

* `Not Found`

  No credential was found.

* `Error`

  There was an error while revoking a credential.

## Errors

If the API call to PingOne Credentials fails, the following error is logged:

* `` Error: PingOne Credentials Revoke a User's Credential- Status Code - Response Body` ``

---

---
title: PingOne Credentials Update node
description: Configure the PingOne Credentials Update node to update an existing PingOne credential for a user during a journey.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:pingone:pingone-cred-update
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-cred-update.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  outcomes: Outcomes
  errors: Errors
---

# PingOne Credentials Update node

The PingOne Credentials Update node lets you update a PingOne credential in a journey.

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | Yes        |

## Inputs

This node retrieves `pingOneUserId` and `pingOneCredentialId` from the journey state.

## Dependencies

This node requires that the PingOne Worker Service is configured so that it can connect to your PingOne instance and update PingOne credentials.

## Configuration

| Property                  | Usage                                                                                                                                                                                          |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PingOne Worker service ID | The ID of the PingOne Worker service for connecting to PingOne.                                                                                                                                |
| PingOne UserID Attribute  | Local attribute name from which to retrieve `pingOneUserId`. The journey state is first looked up, then the local datastore.                                                                   |
| Credential Type ID        | The requested credential name.                                                                                                                                                                 |
| Credential Id Attribute   | The local attribute name to retrieve the credential ID attribute from the shared state.                                                                                                        |
| Attribute map             | The `Key` - `Value` mapping used for associating shared state attributes with credentials. The `Key` is the shared state attribute, and the `Value` is the corresponding credential attribute. |

## Outputs

* `pingOneCredentialUpdate` — The response from the PingOne Credentials Update operation.

## Outcomes

* `Success`

  The credential is updated.

* `Error`

  There was an error when updating the credential.

## Errors

If the API call to PingOne Credentials fails, the following error is logged:

* `Error: PingOne Credentials Update a User Credential- Status Code - Response Body`

---

---
title: PingOne Credentials Verification node
description: Configure the PingOne Credentials Verification node to initiate verification of PingOne credentials through QR code or push notification during a journey.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:pingone:pingone-cred-verify
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-cred-verify.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  example: Example
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  outcomes: Outcomes
  errors: Errors
---

# PingOne Credentials Verification node

The PingOne Credentials Verification node initiates verification of PingOne credentials. The actual task of verification is performed by the PingOne Credentials service and not by this node.

## Example

Learn more in an [example journey using PingOne Credentials nodes](pingone-cred-overview.html#p1-cred-example-journey).

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | Yes        |

## Inputs

If the `Push` delivery method is selected, this node retrieves `pingOneApplicationInstanceId` from the journey state. If `Custom Requested Credentials` is selected, this node retrieves `requestedCredentials` from journey state.

## Dependencies

This node requires that the PingOne Worker Service is configured so that it can connect to your PingOne instance and initiate PingOne credentials verification.

## Configuration

| Property                                     | Usage                                                                                                                                                                                                                      |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PingOne Worker service ID                    | The ID of the PingOne Worker service for connecting to PingOne.                                                                                                                                                            |
| Credential Type                              | Type of credential to verify. Must be the name of a PingOne credential type issued by the credential issuer.                                                                                                               |
| Disclosure Attribute Keys                    | Attribute key names for selective disclosure to return from the credential.                                                                                                                                                |
| Digital Wallet Application ID                | Digital Wallet Application ID from PingOne Credentials required for the Push delivery method.                                                                                                                              |
| Verification URL Delivery Method             | The delivery method (QR code or Push) for delivering the verification URL.                                                                                                                                                 |
| Allow user to choose the URL delivery method | To prompt the user to select the URL delivery method.                                                                                                                                                                      |
| Delivery method message                      | The message to display to the user allowing them to select the delivery method (QR Code or `Push`) to receive the credential verification URL.                                                                             |
| QR code message                              | The message with instructions to scan the QR code and begin credential verification.                                                                                                                                       |
| Waiting Message                              | Localization overrides for the waiting message. This is a map of locale to message.                                                                                                                                        |
| Push Message                                 | A custom message for the user when requesting the credential.                                                                                                                                                              |
| Store Credential Verification Response       | Store the list of verified data submitted by the user in the shared state under the `pingOneCredentialVerification` key.&#xA;&#xA;The key is empty if the node is unable to retrieve the wallet pairing data from PingOne. |
| Verification Timeout                         | The period of time (in seconds) to wait for a response to the verification request. If no response is received within this time, the node times out and the verification process fails.                                    |
| Custom Requested Credentials                 | If selected, a custom requested credentials payload is retrieved from the `requestedCredentials` attribute in shared state.                                                                                                |

## Outputs

* `pingOneCredentialVerification`: The new PingOne Credential Verification request status and full response.

* `pingOneApplicationInstanceId`: The identifier of the application running the Wallet SDK on the user's device and registered with the service.

## Outcomes

* `Success`

  The credential verification was successful.

* `Error`

  There was an error during the verification process.

* `Time Out`

  The verification process reached the configured timeout value.

## Errors

If any of the API calls to PingOne Credentials fail, the following errors may be logged:

* `Error: PingOne Credentials Create Verification session- Status Code - Response Body`.

* `Error: PingOne Credentials Create Push Verification session- Status Code - Response Body`.

* `Error: PingOne Credentials Read a Verification session- Status Code - Response Body`.

---

---
title: PingOne DaVinci API node
description: Configure the PingOne DaVinci API node to trigger a PingOne DaVinci flow through API integration from within an PingAM authentication journey.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:pingone:pingone-davinci
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-davinci.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "PingOne", "DaVinci"]
section_ids:
  davinci-example: Example
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  prep-davinci-flow: Prepare the PingOne DaVinci flow
  config-input-schema: Configure the input schema
  create-davinci-app: Create a PingOne DaVinci application
  configuration: Configuration
  outputs: Outputs
  outcomes: Outcomes
---

# PingOne DaVinci API node

The PingOne DaVinci API node executes an API call to PingOne DaVinci to launch a specific DaVinci flow. This node lets an AM journey trigger a PingOne DaVinci flow through the API integration method and does not render any front-end UI pages.

|   |                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------- |
|   | This node is only effective for DaVinci flows without a UI component, as it is using the DaVinci flow API integration. |

![ping davinci api node](_images/ping-davinci-api-node.png)

## Example

This example highlights the use of the PingOne DaVinci node in a user registration journey:

![ping davinci journey](_images/ping-davinci-journey.png)

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes 1      |
| Ping Identity Platform (self-managed) | Yes        |

1 This functionality requires that you configure AM as part of a [Ping Identity Platform deployment](https://docs.pingidentity.com/platform/8.1/sample-setup/).

## Inputs

None. This node doesn't read shared state data.

## Dependencies

Before using this node, you must:

* [Prepare the PingOne DaVinci flow](#prep-davinci-flow)

* [Configure the input schema](#config-input-schema)

* [Create a PingOne DaVinci application](#create-davinci-app)

* [Set up the PingOne service](pingone-service.html)

This procedure only covers the steps and nodes required to prepare a PingOne DaVinci flow for invoking the API. It assumes you've already created the PingOne DaVinci flow.

### Prepare the PingOne DaVinci flow

1. In PingOne DaVinci, go to the Flows tab.

2. Find the flow you need, and click Edit.

   1. At the end of the Success Path, add an HTTP node to send a JSON success response.

   2. At the end of the Failure Path, add an HTTP node to send a JSON error response.

3. Click Save.

4. Click Deploy.

Refer to the [Configuring the Flow](https://docs.pingidentity.com/davinci/integrating_flows_into_applications/davinci_launching_a_flow_with_an_api_call.html#configuring-the-flow) page for further details.

### Configure the input schema

The PingOne DaVinci API node sends the journey node state to the PingOne DaVinci flow. You must configure the node state as an input parameter for the PingOne DaVinci flow.

1. Click Input Schema on the DaVinci flow canvas.

2. Click Add to add an input parameter.

   1. In the Parameter Name field, enter nodeState.

   2. In the Data Type field, select Object.

3. Click Save.

### Create a PingOne DaVinci application

1. In PingOne DaVinci, go to the Applications tab.

2. Click Add Application. The Add Application modal opens.

3. In the Name field, enter a name for the application, and click \[.label]#Create.

4. Find the application you need and click Edit.

5. On the General tab, note down the values for Company ID and API Key.

   You'll need these to configure the PingOne DaVinci API node parameters.

6. Go to the Flow Policy tab.

7. Click + Add Flow Policy.

   1. In the Name field, enter a name for the flow policy.

   2. In the Flow List, select your flow.

   3. In the Version List, select the desired flow version.

8. Click Create Flow Policy. The Edit Your Weight Distribution modal opens.

9. Click Save Flow Policy.

10. Note down the Policy ID of your flow policy. You'll need it to configure the PingOne DaVinci API node parameters.

Refer to the [Creating an Application](https://docs.pingidentity.com/davinci/integrating_flows_into_applications/davinci_launching_a_flow_with_an_api_call.html#creating-an-application) page for further details.

## Configuration

The configurable properties for this node are:

| Property        | Usage                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| PingOne Service | The ID of the PingOne Worker service for connecting to PingOne.                                                                                                                                                                                                                                                                                                                            |
| Flow Policy ID  | The PingOne DaVinci Flow Policy configured for the specific flow.                                                                                                                                                                                                                                                                                                                          |
| State Inputs    | A list of state inputs that will be passed to PingOne DaVinci, the DaVinci Flow input schema includes the node state parameter. This is a multi-value field to select specific node state attributes which are to be included in the API request to PingOne DaVinci.By default, the wildcard `(*)` value will include the entire journey node state in the API request to PingOne DaVinci. |

## Outputs

Any data configured to be returned to the PingOne DaVinci flow is put into the node state.

## Outcomes

* `True`

  The PingOne DaVinci flow executed and returned a Success response.

* `False`

  The PingOne DaVinci flow executed and returned an Error response.

* `Error`

  An error occurred causing the request to fail. Check the response code, response body, or logs to see more details of the error.

---

---
title: PingOne Delete User node
description: Configure the PingOne Delete User node to delete a user from the PingOne platform during a journey using the PingOne user ID from shared state.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:pingone:pingone-delete-user
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-delete-user.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  callbacks: Callbacks
  outcomes: Outcomes
---

# PingOne Delete User node

The PingOne Delete User node can delete users from the PingOne platform.

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | Yes        |

## Inputs

This node requires the `pingOneUserId` variable from node state. The variable must contain the identifier of the user to delete from PingOne. For example, `a648aaac-ch15-b357-457b-8d2e714180ff`.

Use either of the following nodes to populate the `pingOneUserId` variable in shared state:

* [PingOne Identity Match node](pingone-identity-match.html)

* [PingOne Create User node](pingone-create-user.html)

## Dependencies

This node requires a PingOne Worker Service configuration so that it can authenticate to your PingOne instance.

Find more information in [Connect AM to PingOne](https://docs.pingidentity.com/pingam/8.1/integrations/connect-am-to-pingone.html).

## Configuration

| Property                  | Usage                                                                                                                                                                                                                                                                                                                         |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PingOne Worker Service ID | The ID of the PingOne worker service for connecting to PingOne.                                                                                                                                                                                                                                                               |
| Capture failure           | Capture the details in shared state if a failure occurs.The node stores the details in a variable named `pingOneDeleteUserFailureReason`.Default: `False`Example:```json
{
  "code": "MISSING_PINGONE_USER_ID",
  "message": "Expected PingOne User ID to be set in sharedState or user's profile.",
  "exception": "",
}
``` |

## Outputs

If you select Capture failure, the node stores any error response in a shared state variable named `pingOneDeleteUserFailureReason`.

## Callbacks

This node doesn't send any callbacks.

## Outcomes

`True`

The node deleted the account from PingOne.

`False`

The node did not delete the account from PingOne.

The journey also uses this outcome if any error occurs. Enable Capture Failure to store the details in node state.

---

---
title: PingOne Identity Match node
description: "Configure the PingOne Identity Match node to verify that a user exists in both PingAM and PingOne, and populate shared state with the user's PingOne ID."
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:pingone:pingone-identity-match
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-identity-match.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  example: Example
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  callbacks: Callbacks
  outcomes: Outcomes
---

# PingOne Identity Match node

The PingOne Identity Match node checks that users that exist in the ForgeRock platform also exist in the PingOne platform.

## Example

The following example journey integrates PingOne Verify to perform user identity verification.

![Example PingOne Verify journey](_images/pingone-verify-example-journey-full.png)Figure 1. Example PingOne Verify journey

* The user enters their credentials and the [Data Store Decision node](../data-store-decision.html) matches them against the identity store.

* a The [PingOne Identity Match node](pingone-identity-match.html) checks PingOne for a matching user.

* b If a user is found, the [PingOne Verify Completion Decision node](pingone-verify-completion-decision.html) checks the user's most recent verification transaction to determine the status:

  * Success

    The user successfully completed the most recent PingOne Verify transaction, so the journey progresses directly to the Success node and authentication is successful.

  * Not Completed

    The user has an existing PingOne Verify transaction in progress, so the journey resumes the existing verification transaction.

    The node adds the user's existing transaction ID to the shared node state in a variable named `pingOneVerifyTransactionId`.

  * Not Started / Failure / Expired

    * The user doesn't have an existing PingOne Verify transaction (`Not Started`)

    * The user hasn't successfully completed the most recent PingOne Verify transaction

    * The most recent PingOne Verify transaction has expired

    The journey continues to start a new verification transaction.

* c If no matching user is found, the [PingOne Create User node](pingone-create-user.html) creates a new user in PingOne.

* d The [PingOne Verify Evaluation node](pingone-verify-evaluation.html) starts a new PingOne Verify evaluation or continues an existing evaluation if `pingOneVerifyTransactionId` is present in the shared node state. The node either completes or fails the journey based on the result.

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | Yes        |

## Inputs

This node reads the `username` field from the shared node state to access the user's identity profile.

Implement a [Username Collector node](../am-only/username-collector.html) (standalone AM) or [Platform Username node](../platform-username.html) (Ping Identity Platform deployments) earlier in the journey.

## Dependencies

This node requires a PingOne Worker Service configuration so that it can authenticate to your PingOne instance.

Find more information in [Connect AM to PingOne](https://docs.pingidentity.com/pingam/8.1/integrations/connect-am-to-pingone.html).

## Configuration

| Property                  | Usage                                                                                                                                                                                                                                                                                           |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PingOne Worker Service ID | The ID of the PingOne worker service for connecting to PingOne.                                                                                                                                                                                                                                 |
| Population ID             | The ID of the population in PingOne to check for users or provision new ones.If not specified, the node uses the environment's default population ID.                                                                                                                                           |
| AM Identity Attribute     | The attribute from the user's ForgeRock profile that the node uses to match their account in PingOne.Default: `uid`                                                                                                                                                                             |
| Ping Identity Attribute   | The attribute from the user's PingOne profile that the node uses to search for a matching account.If there are multiple entries with the same attribute value in the PingOne directory server, ensure that this property is specific enough to retrieve only one entry.Default: `username`      |
| Capture failure           | Capture the details in shared state if a failure occurs.The node stores the details in a variable named `pingOneIdentityMatchFailureReason`.Default: `False`Example:```json
{
  "code": "ACCESS_TOKEN",
  "message": "Unable to get access token for PingOne Worker.",
  "exception": "",
}
``` |

## Outputs

If the node was able to find a unique match in PingOne it stores the PingOne user identifier in a state variable named `pingOneUserId`. For example `a648aaac-ch15-b357-457b-8d2e714180ff`.

If you select Capture failure, the node stores any error response in a shared state variable named `pingOneIdentityMatchFailureReason`.

## Callbacks

This node doesn't send any callbacks.

## Outcomes

`True`

The node found a unique matching account in PingOne.

`False`

The node did not find a unique match in PingOne.

---

---
title: PingOne node (deprecated)
description: Deprecated. The PingOne node established a federated OIDC connection between PingOne and PingAM to delegate user flows to PingAM.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:pingone:pingone
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "PingOne", "DaVinci"]
section_ids:
  example: Example
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  node-ping-oidc-app-setup: Configure a PingOne OIDC application to connect to Advanced Identity Cloud
  configuration: Configuration
  outputs: Outputs
  outcomes: Outcomes
---

# PingOne node (deprecated)

The PingOne node establishes trust between PingOne and PingOne Advanced Identity Cloud by using a federated connection.

This node performs an OIDC request to PingOne to delegate the user flow from Advanced Identity Cloud to PingOne using a standard OIDC redirect.

|   |                                                                                                                                                                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * This node is deprecated and will be removed in a future release.

* Depending on your use case, use the following nodes instead:

  * [PingOne Identity Match node](pingone-identity-match.html)

  * [PingOne Create User node](pingone-create-user.html)

  * [PingOne Delete User node](pingone-delete-user.html)

  * [PingOne DaVinci API node](pingone-davinci.html) |

![pingone node diagram](_images/pingone_node_diagram.png)

## Example

This example journey highlights the use of the PingOne node:

![ping one journey](_images/ping-one-journey.png)

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes 1      |
| Ping Identity Platform (self-managed) | Yes        |

1 This functionality requires that you configure AM as part of a [Ping Identity Platform deployment](https://docs.pingidentity.com/platform/8.1/sample-setup/).

## Inputs

Any data in the node state that must be sent to PingOne.

## Dependencies

Before using the PingOne node, you must do the following:

* [Configure a PingOne OIDC application to connect to Advanced Identity Cloud](#node-ping-oidc-app-setup)

* Configure the [PingOne Service](pingone-service.html)

* (Optional) If you plan to trigger a DaVinci flow from the PingOne node, follow the steps in [Integrating Flows into Applications](https://docs.pingidentity.com/davinci/integrating_flows_into_applications/davinci_how_to_implement_a_flow.html).

### Configure a PingOne OIDC application to connect to Advanced Identity Cloud

Use the Applications page in the PingOne interface to add an application to connect to Advanced Identity Cloud.

1. Go to Applications > Applications.

2. Click +.

3. Create an application profile with these parameters:

   1. Application name: Advanced Identity Cloud Federation.

   2. Description (optional): Enables Advanced Identity Cloud federation with PingOne.

   3. Select `OIDC Web App` as the Application Type.

4. Click Save.

5. After the application profile is created, go to the Configuration tab and click the pencil icon to edit the application.

   1. In the PKCE Enforcement the drop-down, select `S256_REQUIRED`.

   2. In the Token Endpoint Authentication Method drop-down, select `Client Secret Basic`.

   3. Select Require Pushed Authorization Request.

   4. Enter the Redirect URIs of your Advanced Identity Cloud AM instance.

6. Click Save, and then select Enable.

## Configuration

| Property             | Usage                                                                                                                                                                                                                               |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PingOne Service      | The ID of the PingOne Worker service for connecting to PingOne.                                                                                                                                                                     |
| ACR Values(optional) | For triggering a specific PingOne application policy.                                                                                                                                                                               |
| Username             | The attribute that contains the name of the user for the object.                                                                                                                                                                    |
| State Inputs         | A multi-value field to select specific attributes from node state to include in the federation request to PingOne. By default, the wildcard (\*) value includes the entire journey node state in the federation request to PingOne. |

## Outputs

Any claims returned by PingOne during federation will be stored in the node state.

## Outcomes

* `Account exists`

  If the account returned by PingOne during federation matches an existing account, and it is linked to the account in Advanced Identity Cloud.

* `Account exists, no link`

  If the account returned by PingOne during federation exists in Advanced Identity Cloud, but it is not yet linked to the existing account in Advanced Identity Cloud.

* `No account exists`

  If the account returned by PingOne during federation does not exist in Advanced Identity Cloud.

- `Error`

  An error occurred causing the request to fail. Check the response code, response body, or logs to see more details of the error.

---

---
title: PingOne Protect Evaluation node
description: Configure the PingOne Protect Evaluation node to calculate a risk score and recommended actions for an authentication event using PingOne Protect risk policies.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:pingone:pingone-protect-evaluation
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-evaluation.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["auth-node-pingone-protect-evaluation.adoc"]
section_ids:
  example: Example
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  outcomes: Outcomes
  outcome_precedence: Outcome precedence
  errors: Errors
---

# PingOne Protect Evaluation node

The PingOne Protect Evaluation node contacts PingOne to calculate the risk level and other risk-related details associated with an event.

Depending on how you configure your risk policies in PingOne, the response could return a risk score, a risk level such as high, medium, or low, and recommended actions to take, such as mitigation against bots.

Learn more in [PingOne Protect > How it Works](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_introduction.html).

## Example

The following example journey leverages PingOne Protect functionality to perform a risk evaluation.

![Example PingOne Protect journey](_images/pingone-protect-example-journey.png)Figure 1. Example PingOne Protect journey

* a The [PingOne Protect Initialize node](pingone-protect-initialize.html) instructs the Ping SDK to initialize a PingOne Signals (Protect) SDK with the configured properties.

  |   |                                                                                                                                                                                                       |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Initialize a PingOne Signals (Protect) SDK as early in the journey as possible, before any user interaction.This enables it to gather sufficient contextual data to make an informed risk evaluation. |

  In the subsequent nodes, the end user enters their credentials, which are verified against the identity store.

* b The [PingOne Protect Evaluation node](pingone-protect-evaluation.html) performs a risk evaluation against a risk policy in PingOne.

  The example journey continues depending on the outcome:

  * `High`

    The journey requests that the user respond to a push notification.

  * `Medium` or `Low`

    The risk isn't significant, so no further authentication factors are required. The journey continues to a [PingOne Protect Result node](pingone-protect-result.html) that returns the success result to PingOne.

  * `Exceeds Score Threshold`

    The score returned is higher than the configured threshold and is considered too risky to complete successfully. The journey continues to a [PingOne Protect Result node](pingone-protect-result.html) that returns the failed result to PingOne.

  * `Failure`

    The risk evaluation could not be completed, so the authentication attempt continues to the Failure node.

  * `TEMP_EMAIL_MITIGATION`

    The risk evaluation returned a recommended action regarding the possibility of a temporary email address. The journey continues to an [Inner Tree Evaluator node](../inner-tree-evaluator.html) that requires the user to respond to a push notification.

  * `BOT_MITIGATION`

    The risk evaluation returned a recommended action to check for the presence of a human. The journey continues to a [CAPTCHA node](../captcha.html).

  * `AITM_MITIGATION`

    The risk evaluation returned a recommended action regarding the possible presence of an adversary-in-the-middle attack. The journey continues to a [PingOne Protect Result node](pingone-protect-result.html) that returns the failed result to PingOne.

  * `ClientError`

    The client returned an error when attempting to capture the data to perform a risk evaluation. The journey continues to the Failure node.

* c An instance of the [PingOne Protect Result node](pingone-protect-result.html) returns the `Success` result to PingOne to help with analysis and risk policy tuning.

* d A second instance of the [PingOne Protect Result node](pingone-protect-result.html) returns the `Failed` result to PingOne to help with analysis and risk policy tuning.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | You can broadly observe the risk evaluation results in the [PingOne threat protection dashboard](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_dashboard.html). You can also use an audit to [review specific risk evaluation results](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_reviewing_risk_evaluations.html), including the JSON response from the risk evaluation. |

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | Yes        |

|   |                                                             |
| - | ----------------------------------------------------------- |
|   | You can't use this node inside a [Page node](../page.html). |

## Inputs

This node can use shared state variables that contain the PingOne `user.id` and `user.name` as input. If these aren't available, the node uses the `UserId` and `Username` variables.

This node requires that you've initialized PingOne Protect in your client application. For example, by using a [PingOne Protect Initialize node](pingone-protect-initialize.html) node previously in the journey or by initializing the SDK within the app itself.

## Dependencies

This node requires a PingOne Worker Service configuration to connect to your PingOne instance and send it the necessary data to make risk evaluations.

Find more information in [Connect AM to PingOne](https://docs.pingidentity.com/pingam/8.1/integrations/connect-am-to-pingone.html).

The client application must be using Ping SDK 4.4.0 or later.

## Configuration

| Property                                        | Usage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PingOne Worker Service ID                       | The ID of the PingOne worker service for connecting to PingOne.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Target App ID                                   | (Optional) If the user is attempting to access a PingOne application through the journey, add its v4 UUID client ID.This correlates the authentication with the application in PingOne, letting you filter by the Resource Id that matches the entered Target App ID when viewing the [audit log](https://docs.pingidentity.com/pingone/monitoring/p1_reporting.html) in PingOne.For example, `12345678-abcd-4567-abcd-a123b123c123`.	If you enable Use Node State Attribute For Target App ID", the node uses this value as a key to retrieve the required value from node state. Otherwise, the node uses the literal value provided in this field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Use Node State Attribute For Target App ID      | Lets you set a dynamic target app ID. Setting this to `true` instructs the node to get the target app ID from the shared node state, in the variable specified by the value of Target App ID.You should use a [Scripted Decision node](../scripted-decision.html) before this node in the journey to add the target app ID to the shared state variable specified by the value of Target App ID.	If you don't set a value for Target App ID the node ignores this setting.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Target App Name                                 | (Optional) If the user is attempting to access a PingOne application through the journey, add its resource name.This correlates the authentication with the application in PingOne, letting you filter the [audit log](https://docs.pingidentity.com/pingone/monitoring/p1_reporting.html) by the Resource name that matches the value of the Target App Name.For example:```json
"event": {
	"completionStatus": "SUCCESS",
	"targetResource": {
		"id": "12345678-abcd-4567-abcd-a123b123c123",
		"name": "MyApp"
	},
	...
}
```&#xA;&#xA;If you enable Use Node State Attribute For Target App Name", the node uses this value as a key to retrieve the required value from node state. Otherwise, the node uses the literal value provided in this field.&#xA;&#xA;If you don't set a value for Target App ID, the node ignores this setting.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Use Node State Attribute For Target App Name    | Lets you set a dynamic target app name. Setting this to `true` instructs the node to get the target app name from the shared node state, in the variable specified by the value of Target App Name.Use a [Scripted Decision node](../scripted-decision.html) before this node in the journey to add the target app name to the shared state variable specified by the value of Target App Name.	If you don't set a value for Target App Name the node ignores this setting.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Risk Policy Set ID                              | The ID of the [risk policy](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_risk_policies.html) in PingOne.To view risk policies in the PingOne admin console, go to Threat Protection > Risk Policies.&#xA;&#xA;If not specified, the environment's default risk policy set is used.&#xA;&#xA;If you enable Targeted Policies Evaluation, this value is ignored.&#xA;&#xA;If you enable Use Node State Attribute For Risk Policy Set ID, the node uses this value as a key to retrieve the required value from node state. Otherwise, the node uses the literal value provided in this field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Use Node State Attribute For Risk Policy Set ID | Lets you set a dynamic risk policy set ID. Setting this to `true` instructs the node to get the risk policy set ID from the shared node state, in the variable specified by the value of Risk Policy Set ID.You should use a [Scripted Decision node](../scripted-decision.html) before this node in the journey to add the risk policy set ID to the shared state variable specified by the value of Risk Policy Set ID.&#xA;&#xA;If you don't set a value for Risk Policy Set ID the node ignores this setting.&#xA;&#xA;If a value corresponding to the key provided in Risk Policy Set ID can't be found, no value is sent to PingOne and the default risk policy is applied.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Targeted Policies Evaluation                    | When enabled, the API request sent to PingOne Protect includes a `targeted` property that's set to `true`. This property specifies that PingOne's risk evaluation should process the targeted risk policies defined in the user's PingOne environment instead of using a specific risk policy.PingOne responds with the name and ID of the selected risk policy. For example:```json
"riskPolicySet": {
    "id": "f394426f-9b71-4e01-ac78-2956a2e92ac2",
    "name": "Score-based policy",
    "targeted": true
},
```Find more information in [Risk policies](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_risk_policies.html) in the PingOne documentation.Default: Not enabled                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Flow Type                                       | The type of flow or event for which the risk evaluation is being carried out.Choose from:- `REGISTRATION`

  Initial registration of an account.

- `AUTHENTICATION`

  Standard authentication for login or actions such as password change.

- `ACCESS`

  Verification of whether the user can access the relevant application.

- `AUTHORIZATION`

  Verification of whether the user is authorized to perform a specific action such as a profile change.

- `TRANSACTION`

  Authentication carried out in the context of a purchase or other one-time transaction.The default is `AUTHENTICATION`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Authentication Flow Subtype                     | If the Flow Type is `AUTHENTICATION`, select the flow subtype for which the risk evaluation is being carried out.Choose from:- `NONE`

- `ACCOUNT_RECOVERY`

- `ACTIVE_SESSION`

- `KERBEROS`

- `NEO_CREDENTIALS`

- `PASSKEY`

- `PASSWORDLESS`

- `USER_CERTIFICATION`

- `USER_PASSWORD`

- `USERNAME_RECOVERY`The default is `NONE`.If you use the Node State Attribute For Flow Subtype to set the subtype dynamically, that value takes precedence over the static value set here.Learn more about flow types and subtypes in [Risk Evaluations](https://developer.pingidentity.com/pingone-api/protect/risk-evaluations.html) in the PingOne API documentation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Authorization Flow Subtype                      | If the Flow Type is `AUTHORIZATION`, select the flow subtype for which the risk evaluation is being carried out.Choose from:- `NONE`

- `ADD_ADDRESS`

- `ADD_MFA`

- `ADD_PAYEE`

- `ADD_PHONE_NUMBER`

- `ADD_USER`

- `CHANGE_PASSWORD`

- `DELETE_MFA`

- `DELETE_PAYEE`

- `UPDATE_ADDRESS`The default is `NONE`.If you use the Node State Attribute For Flow Subtype to set the subtype dynamically, that value takes precedence over the static value set here.Learn more about flow types and subtypes in [Risk Evaluations](https://developer.pingidentity.com/pingone-api/protect/risk-evaluations.html) in the PingOne API documentation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Node State Attribute For Flow Subtype           | Lets you set a dynamic flow subtype. Setting a value here instructs the node to get the risk flow subtype from this variable in the shared node state.Use a [Scripted Decision node](../scripted-decision.html) before this node in the journey to add the flow subtype to this shared state variable.This field applies only to `AUTHENTICATION` and `AUTHORIZATION` flow types. The dynamic flow subtype takes precedence over any static value set in the Authentication Flow Subtype or Authorization Flow Subtype fields.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Device Sharing Type                             | Whether the device is shared between users or not.Choose from:- `UNSPECIFIED`

- `SHARED`

- `PRIVATE`The default is `SHARED`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Score Threshold                                 | Scoring higher than this value results in evaluation continuing along the `Exceeds Score Threshold` outcome.The default is `300`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Recommended Actions                             | A list of recommended actions the risk evaluation could return. Each entry in the list becomes a node outcome.If the evaluation score doesn't exceed the Score Threshold value, and a recommended action is present in the response from PingOne Protect, the journey continues down the matching entry in this list.Possible values are:- `BOT_MITIGATION`

  PingOne suspects the client could be automated or a bot. You should route the journey to a CAPTCHA node or similar next step to mitigate against bots.

- `AITM_MITIGATION`

  PingOne suspects an adversary-in-the-middle (AitM) attack. You should route the journey to the failure node, and consider locking the account, and force a password change to mitigate against these attacks.

- `TEMP_EMAIL_MITIGATION`

  PingOne suspects the user has entered a temporary email address. Temporary email addresses are often associated with malicious activities. You should route the journey to an [Inner Tree Evaluator node](../inner-tree-evaluator.html), [Scripted Decision node](../scripted-decision.html), or similar, that requires the user to authenticate with a second factor.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Pause Behavioral Data                           | After receiving the device signal, instruct the client to pause collecting behavioral data.Default: Selected                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Node State Attribute For User ID                | The node state variable that contains the `user.id` as it appears in PingOne.If you leave this field blank, or if you provide a variable name but the node can't find it in the node state, it uses the current context `UserId` from the user object as the `user.id`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Node State Attribute For Username               | The node state variable that contains the `user.name` value to send to PingOne Protect.If you leave this field blank, the node uses the current context `Username` as the `user.name`.	If you're using this node in a registration journey associated with a risk policy that includes an Email reputation risk predictor, you must map this attribute to a node state attribute that contains an email address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Node State Attribute For User Groups            | The node state variable that contains a list of group names to send to PingOne Protect.Use a [Scripted Decision node](../scripted-decision.html) before this node in the journey to add the group names to this shared state variable.The node sends group names under the `event` object. For example:```json
"event": {
	"user": {
        "groups": [
            {"name": "employees"},
            {"name": "uk"}
        ]
	},
	...
}
```- If you leave this field blank, the node uses the current context from the user object.

- If you provide a variable name and that variable is *not* in the node state, the node sends no group information to PingOne Protect. It doesn't use the current context from the user object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Store Risk Evaluation                           | Stores the risk evaluation response in the transient node state under a key named `PingOneProtectEvaluationNode.RISK`.Default: Not enabledThe key is empty if the node can't retrieve a risk evaluation from PingOne.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Node State Attribute For Custom Attributes      | The node state variable that contains any custom attributes you want to send to PingOne.Use a [Scripted Decision node](../scripted-decision.html) before this node in the journey to create the node state variable and add it to the shared state.> **Collapse: Example**
>
> The Scripted Decision Node script adds a map of attributes to the node state. The values of these attributes are *objects* so the node supports strings, integers, and complex objects.
>
> ```javascript
> var details = {
>     "name": "test-details"
> }
> var customAttributes = {
>     "customAttribute1": 20,
>     "customAttribute2": nodeState.get("username"),
>     "customAttribute3": details
> };
> nodeState.putShared("exampleCustomAttributes", customAttributes);
> action.goTo("true");
> ```
>
> In this example, the value of the Node State Attribute For Custom Attributes property must be `exampleCustomAttributes`.
>
> These custom attributes are included in the API request to PingOne Protect in the data under `event.customAttributes`. For example:
>
> ```json
> {
>   "event": {
>     "completionStatus": "SUCCESS",
>     "ip": "127.0.0.1",
>     "flow": {
>       "type": "AUTHENTICATION"
>     },
>     "user": {
>       "id": "id=ce3c42e2-6f9c-4451-8590-9ee40fad3f83,ou=user,o=alpha,ou=services,ou=am-config",
>       "type": "EXTERNAL"
>     },
>     "sharingType": "SHARED",
>     "browser": {
>       "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
>     },
>     "device": {
>       "id": "Id-5a71aeee-0382-4fa3-b903-499cf2a331fb",
>       "externalId": "example-external-device-ID",
>       "os": {
>         "name": "Mac OS X"
>       },
>       "browser": {
>         "name": "Firefox"
>       }
>     },
>     "customAttributes": {
>       "customAttribute1": 20,
>       "customAttribute2": "bjensen",
>       "customAttribute3": {
>         "name": "test-details"
>       }
>     }
>   }
> }
> ``` |
| Node State Attribute For Device External ID     | The node state variable that contains an external device ID to send to PingOne Protect in the evaluation request.This property lets you send a custom device ID to PingOne Protect in addition to the device ID provided by the Signals SDK. For example, if your mobile native app incorporates a WebView, the mobile Signals SDK and the web Signals SDK would provide different device IDs. You can use this property to send a single, consistent device ID to PingOne Protect.If you set a value here, the node attempts to find this attribute in the node state and adds its value to the request if it's present and not null. If the attribute isn't in the node state, the node logs a warning.If you leave this field blank, no device external ID is sent in the request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Node State Attribute For Event Session ID       | The node state variable that contains the session ID to send to PingOne Protect in the risk evaluation request.You can use this session ID to track requests sent to PingOne Protect.If you set a value here, the node attempts to find this attribute in the node state and adds its value to the request if it's present and not `null`. If the attribute isn't in the node state, the node logs a warning.If you leave this field blank, the node sends the AM audit tracking ID for the session.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## Outputs

If you enable the Store Risk Evaluation property, the node outputs the risk evaluation response JSON in a state variable named `PingOneProtectEvaluationNode.RISK`.

The node outputs the following data to shared state:

* `PINGONE_VERIFY_DELIVERY_METHOD_KEY` The selected delivery method

* `PINGONE_VERIFY_TRANSACTION_ID_KEY` The transaction ID to send to PingOne

* `PINGONE_VERIFY_TIMEOUT_KEY` The timeout to send to PingOne

* `TRANSACTION_POLL_INTERVAL`: The poll interval to send to PingOne

* `PINGONE_VERIFY_EVALUATION_FAILURE_REASON_KEY` If the node couldn't obtain the risk evaluation from PingOne, the failure reason.

## Outcomes

* `High`

  The risk evaluation level is considered high.

* `Medium`

  The risk evaluation level is considered medium.

* `Low`

  The risk evaluation level is considered low.

* `Exceeds Score Threshold`

  The score returned is higher than the configured threshold.

* `Failure`

  The risk evaluation couldn't be completed.

* *Recommended Actions*

  The risk evaluation recommended a mitigation action to take, and it matched a value in the Recommended Actions list.

  Currently, the only possible values are:

  * `BOT_MITIGATION`, which recommends you check for the presence of a human, such as by using a CAPTCHA node.

  * `AITM_MITIGATION`, on suspicion of an adversary-in-the-middle (AitM) attack. The recommended action is to route the journey to the failure node, consider locking the account, and force a password change to mitigate against these attacks.

  * `TEMP_EMAIL_MITIGATION`, on suspicion of temporary email addresses. The recommended action is to require the user to authenticate with a second factor.

* `ClientError`

  The client returned an error when attempting to capture the data to perform a risk evaluation.

### Outcome precedence

Evaluation of the journey continues along an outcome based on the response received and the fields present in the response:

![Risk evaluation outcome path precedence](https://kroki.io/plantuml/svg/eNqVlOFO2zAQx7_7KU7eB7aItWvHgAFiKlCgEi2IlqFJSMhNLo1V165sp6VDPNBeY0-2cwJrhwJo_eCkvv_9_D_7nPoaA_odmunCylHm4fcvaH5qbsDH8NiEC6lH0ElQe-kXJLNTY4WXRrMib5BJB7FJEOjpDQwRcocJ4F2scidnqBYgNSm0xjikwVz67BVqgDqT-rmwCMaCQzuTMbpaEXkxD4ymlUyaonXg8jirhASHCkdCQUGQ6ArqPDOQiRmGWbTkXmoSChhKnYQFFeVqhyBGFnFCoreKWKuzPecXCveZoKpnFD-SlC0mcE8rXoik4DbZA0tMnBfIEID62oGIxyNrcp0cGkXWvRXaTakO7Yn6wPbqj2DmxlJTgJhPvO3VyVdAq7IjTEWu_LHRvicmCPwU1Qy9jAWvVvXlT4TGxiqjZzweGJugLZcaxridNp4LnvlJvmKSbq1i-plIzDwU4m2OjLGdS-nGgDOh8vKQLbqpoZPYZZqIUDQs45zTPLnjO3DPOf0H4Aqp9WiCd9tHnasuX38KuNhYpECjttHc_rLV-DtuLiUmt3HQ8NbJyWX7pDVoH91etzsnp4P-EmQxNhM6uQSTVtHZLmQcnA9uu51Bh5I6572l2i-mBfF76-yqzYvZBxopHUIpTKbwPooaNegHf3StqKTMqCSKbjRdnlSO8tCYQhdXC5FW_fYBfIY65P1AF0UfqIHeYRObaWMnitqFylXxTO7JOsJU-GyXksZSKYaKGpxQe3E4nR1abL9nSmjprVmDy2XJ8Fhzhb-J8HGGrsre0mA3iOiob3QUvYBdtXmjj6ll8E5MpgrXgT_fZ75b0ItKAF6phT4udHfp80DhzzUClY3CowhCm-GNFg5SodSQ2rVMiEWgQRRxfnZ-HaTl_Opun5l51c6uePqH89iUlaguJjKf_A_tlDqzmnVKF-RNEm18uSeseJcpK8c_kgbpsQ==)Figure 2. Risk evaluation outcome path precedence

1. If you've configured the Score Threshold property and the result contains a score that exceeds it, evaluation continues along the `Exceeds Score Threshold` outcome path.

2. If you have *not* configured the Score Threshold property, or the score does not exceed it, but *have* added a value in the Recommended Actions list that matches one in the response, evaluation continues along the relevant dynamic outcome path. For example, the `BOT_MITIGATION` outcome path.

3. If you have *not* configured the Score Threshold property, or the score does not exceed it, and have *not* added a matching value in the Recommended Actions list, then evaluation continues along the relevant `level` path, one of `Low`, `Medium`, or `High`.

## Errors

* If a recommended action outcome isn't defined, the node logs the following warning:

  `Outcome not found for recommended action action`

* If PingOne Protect couldn't perform the risk assessment, for whatever reason, the node logs the following warning:

  `PingOne Protect risk evaluation failed`

* If you've configured the node to read the Target App ID, Risk Policy Set ID, or any custom attributes from a shared state attribute, and it's unable to read these values from the shared state, it logs the following warning:

  `Expected attribute to be defined in node state`

---

---
title: PingOne Protect Initialize node
description: Configure the PingOne Protect Initialize node to instruct the client to initialize the PingOne Protect SDK to gather device signals and contextual information for risk evaluation.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:pingone:pingone-protect-initialize
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-initialize.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["auth-node-pingone-protect-initialize.adoc"]
section_ids:
  example: Example
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  callbacks: Callbacks
  outcomes: Outcomes
---

# PingOne Protect Initialize node

The PingOne Protect Initialize node instructs the client to initialize a PingOne Signals (Protect) SDK so that it can start gathering device signals and contextual information:

* If the client is a device or browser running a Ping SDK, this node initializes a PingOne Signals (Protect) SDK in the device or browser. This requires a Ping SDK v4.4.0 or later. Learn more in [Integrate with PingOne Protect for risk evaluations](https://docs.pingidentity.com/sdks/latest/sdks/integrations/integrate-with-pingone-protect.html).

You should place this node as early as possible in your journey so that it can gather sufficient contextual information to make risk evaluations.

This node initializes the PingOne Signals (Protect) SDK in the client only once. If you include a second instance of the node in a journey, it won't initialize the PingOne Signals (Protect) SDK again and won't override the initial node configuration.

Learn more in [Getting started with PingOne Protect](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_getting_started.html).

## Example

The following example journey leverages PingOne Protect functionality to perform a risk evaluation.

![Example PingOne Protect journey](_images/pingone-protect-example-journey.png)Figure 1. Example PingOne Protect journey

* a The [PingOne Protect Initialize node](pingone-protect-initialize.html) instructs the Ping SDK to initialize a PingOne Signals (Protect) SDK with the configured properties.

  |   |                                                                                                                                                                                                       |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Initialize a PingOne Signals (Protect) SDK as early in the journey as possible, before any user interaction.This enables it to gather sufficient contextual data to make an informed risk evaluation. |

  In the subsequent nodes, the end user enters their credentials, which are verified against the identity store.

* b The [PingOne Protect Evaluation node](pingone-protect-evaluation.html) performs a risk evaluation against a risk policy in PingOne.

  The example journey continues depending on the outcome:

  * `High`

    The journey requests that the user respond to a push notification.

  * `Medium` or `Low`

    The risk isn't significant, so no further authentication factors are required. The journey continues to a [PingOne Protect Result node](pingone-protect-result.html) that returns the success result to PingOne.

  * `Exceeds Score Threshold`

    The score returned is higher than the configured threshold and is considered too risky to complete successfully. The journey continues to a [PingOne Protect Result node](pingone-protect-result.html) that returns the failed result to PingOne.

  * `Failure`

    The risk evaluation could not be completed, so the authentication attempt continues to the Failure node.

  * `TEMP_EMAIL_MITIGATION`

    The risk evaluation returned a recommended action regarding the possibility of a temporary email address. The journey continues to an [Inner Tree Evaluator node](../inner-tree-evaluator.html) that requires the user to respond to a push notification.

  * `BOT_MITIGATION`

    The risk evaluation returned a recommended action to check for the presence of a human. The journey continues to a [CAPTCHA node](../captcha.html).

  * `AITM_MITIGATION`

    The risk evaluation returned a recommended action regarding the possible presence of an adversary-in-the-middle attack. The journey continues to a [PingOne Protect Result node](pingone-protect-result.html) that returns the failed result to PingOne.

  * `ClientError`

    The client returned an error when attempting to capture the data to perform a risk evaluation. The journey continues to the Failure node.

* c An instance of the [PingOne Protect Result node](pingone-protect-result.html) returns the `Success` result to PingOne to help with analysis and risk policy tuning.

* d A second instance of the [PingOne Protect Result node](pingone-protect-result.html) returns the `Failed` result to PingOne to help with analysis and risk policy tuning.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | You can broadly observe the risk evaluation results in the [PingOne threat protection dashboard](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_dashboard.html). You can also use an audit to [review specific risk evaluation results](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_reviewing_risk_evaluations.html), including the JSON response from the risk evaluation. |

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | Yes        |

|   |                                                             |
| - | ----------------------------------------------------------- |
|   | You can't use this node inside a [Page node](../page.html). |

## Inputs

None. This node doesn't read shared state data.

## Dependencies

This node requires a PingOne Worker Service configuration so that it can connect to your PingOne instance and send it the necessary data to make risk evaluations as part of the journey.

Find more information in [Connect AM to PingOne](https://docs.pingidentity.com/pingam/8.1/integrations/connect-am-to-pingone.html).

Only Ping SDKs v4.4.0 and later support this node.

## Configuration

| Property                                      | Usage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PingOne Worker Service ID                     | The ID of the PingOne worker service for connecting to PingOne.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Collect Behavioral Data                       | When selected, collect behavioral data.Otherwise, don't collect behavioral data.Default: Selected                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Enable Universal Device Identification        | Tie the device payload to a non-extractable crypto key stored in the browser for content authenticity verification.Default: Not selected                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Disable Tags                                  | When selected, the client doesn't collect tag data. Tags are used to record the pages the user visited, forming a browsing history.Default: Not selected (collect tag data)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Enable Agent Identification                   | When enabled, the [PingOne Signals (Protect) SDK](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_signals_sdk.html) collects device attributes from the PingID Device Trust Agent.	This field requires the PingIDDevice Trust agent to be installed on the end user's device.> **Collapse: Example response from PingOne with collected agent information**
>
> ```json
> "device": {
>     "agent": {
>         "customScript": {
>             "exitCode": 5,
>             "output": "b90ce386-f74f-473c-bc27-f19b3569b8b5"
>         },
>         "loggedInUser": {
>             "name": "bjensen",
>             "objectSid": "objectSid",
>             "domainName": "domainName"
>         },
>         "macAddress": "mac-address",
>         "os": {
>             "name": "macOS",
>             "version": "14.6.1"
>         },
>         "name": "mac-2CD4BNMD",
>         "id": "agent-id",
>         "version": "0.1.0"
>     },
>     "os": {
>         "name": "Mac OS X"
>     },
>     "browser": {
>         "name": "Chrome"
>     },
>     "id": "device-id",
>     "estimatedDistance": 0
> }
> ``` |
| Timeout for Agent                             | The time, in milliseconds, for establishing a connection with the PingID Device Trust Agent.Must be a value between `200` and `10,000` milliseconds.If you don't specify a value, the Signals SDK sets a default value.	This field requires the PingID Device Trust agent to be installed on the end user's device.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Port Number for Agent                         | The port number to use when connecting to the PingID Device Trust Agent.If you don't set a value, the connection goes through the default port: `9400`.	This field requires the PingID Device Trust agent to be installed on the end user's device.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Additional Signals SDK Initialization Options | Lets you pass additional signals options (not included in the existing node configuration properties) when you initialize the [PingOne Signals (Protect) SDK](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_signals_sdk.html).Provide a map of keys and values where Key is the PingOne Protect signals parameter and Value is the parameter value. For example:- Key: `waitForWindowLoad`

- Value: `true`Read the [SDKs documentation](https://docs.pingidentity.com/sdks/latest/sdks/integrations/pingone-protect/03-app.html#start) for the list of valid signals.	Don't include signals that are included in the existing node configuration properties. For example, don't add agentTimeout to this map.                                                                                                                                                                                                                                                                                                                                                                                                             |

## Outputs

This node doesn't change the shared state.

## Callbacks

The node sends a `PingOneProtectInitializeCallback` to the client application. The callback includes the `signalsInitializationOptions` object with the options used to initialize the SDK. For example:

```json
{
    "name": "signalsInitializationOptions",
    "value": {
        "agentIdentification": "true",
        "htmlGeoLocation": "true",
        "agentTimeout": "10000",
        "disableTags": "false",
        "behavioralDataCollection": "true",
        "agentPort": "8010",
        "enableTrust": "false"
    }
}
```

The client consumes this callback and initializes the PingOne Protect functionality so it can start gathering the data it needs to make risk evaluations.

## Outcomes

* `True`

  The client application confirmed successful receipt of the configuration.

* `False`

  The client application didn't confirm successful receipt of the configuration or returned a client error.

---

---
title: PingOne Protect Result node
description: Configure the PingOne Protect Result node to update the risk evaluation configuration or completion status of a PingOne Protect risk evaluation in progress.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:pingone:pingone-protect-result
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-result.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["auth-node-pingone-protect-result.adoc"]
section_ids:
  example: Example
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  outcomes: Outcomes
---

# PingOne Protect Result node

The PingOne Protect Result node updates the risk evaluation configuration or modifies the completion status of the resource while the risk evaluation is still in progress.

You can check the results of the evaluation in the PingOne admin console by filtering for `Risk Evaluation Updated` event types.

## Example

The following example journey leverages PingOne Protect functionality to perform a risk evaluation.

![Example PingOne Protect journey](_images/pingone-protect-example-journey.png)Figure 1. Example PingOne Protect journey

* a The [PingOne Protect Initialize node](pingone-protect-initialize.html) instructs the Ping SDK to initialize a PingOne Signals (Protect) SDK with the configured properties.

  |   |                                                                                                                                                                                                       |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Initialize a PingOne Signals (Protect) SDK as early in the journey as possible, before any user interaction.This enables it to gather sufficient contextual data to make an informed risk evaluation. |

  In the subsequent nodes, the end user enters their credentials, which are verified against the identity store.

* b The [PingOne Protect Evaluation node](pingone-protect-evaluation.html) performs a risk evaluation against a risk policy in PingOne.

  The example journey continues depending on the outcome:

  * `High`

    The journey requests that the user respond to a push notification.

  * `Medium` or `Low`

    The risk isn't significant, so no further authentication factors are required. The journey continues to a [PingOne Protect Result node](pingone-protect-result.html) that returns the success result to PingOne.

  * `Exceeds Score Threshold`

    The score returned is higher than the configured threshold and is considered too risky to complete successfully. The journey continues to a [PingOne Protect Result node](pingone-protect-result.html) that returns the failed result to PingOne.

  * `Failure`

    The risk evaluation could not be completed, so the authentication attempt continues to the Failure node.

  * `TEMP_EMAIL_MITIGATION`

    The risk evaluation returned a recommended action regarding the possibility of a temporary email address. The journey continues to an [Inner Tree Evaluator node](../inner-tree-evaluator.html) that requires the user to respond to a push notification.

  * `BOT_MITIGATION`

    The risk evaluation returned a recommended action to check for the presence of a human. The journey continues to a [CAPTCHA node](../captcha.html).

  * `AITM_MITIGATION`

    The risk evaluation returned a recommended action regarding the possible presence of an adversary-in-the-middle attack. The journey continues to a [PingOne Protect Result node](pingone-protect-result.html) that returns the failed result to PingOne.

  * `ClientError`

    The client returned an error when attempting to capture the data to perform a risk evaluation. The journey continues to the Failure node.

* c An instance of the [PingOne Protect Result node](pingone-protect-result.html) returns the `Success` result to PingOne to help with analysis and risk policy tuning.

* d A second instance of the [PingOne Protect Result node](pingone-protect-result.html) returns the `Failed` result to PingOne to help with analysis and risk policy tuning.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | You can broadly observe the risk evaluation results in the [PingOne threat protection dashboard](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_dashboard.html). You can also use an audit to [review specific risk evaluation results](https://docs.pingidentity.com/pingone/threat_protection_using_pingone_protect/p1_protect_reviewing_risk_evaluations.html), including the JSON response from the risk evaluation. |

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | Yes        |

|   |                                                             |
| - | ----------------------------------------------------------- |
|   | You can't use this node inside a [Page node](../page.html). |

## Inputs

This node requires that you've initialized PingOne Protect. For example, by using a [PingOne Protect Evaluation node](pingone-protect-evaluation.html) previously in the journey or by initializing it via the Ping SDK within the app itself.

## Dependencies

This node requires a PingOne Worker Service configuration so that it can connect to your PingOne instance and send it the necessary data to make risk evaluations as part of the journey.

Find more information in [Connect AM to PingOne](https://docs.pingidentity.com/pingam/8.1/integrations/connect-am-to-pingone.html).

## Configuration

| Property          | Usage                                                                                |
| ----------------- | ------------------------------------------------------------------------------------ |
| Completion Status | Report the status of the journey back to PingOne.Choose from:- `FAILED`

- `SUCCESS` |

## Outputs

This node doesn't change the shared state.

## Outcomes

Single outcome path.

The node attempts to update the PingOne server but continues along the single outcome without confirming the server received the update.

---

---
title: PingOne Service
description: Configure the PingOne Service to integrate PingOne Credentials and PingOne DaVinci nodes in PingAM authentication journeys.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:pingone:pingone-service
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-service.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "PingOne", "DaVinci"]
section_ids:
  configure-p1-service: Configure the PingOne service
---

# PingOne Service

The [PingOne Service](pingone-service.html) lets you integrate PingOne Credentials and PingOne DaVinci in your authentication journeys.

|   |                                                                                                                                                                                                                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Use this service *only* if you're integrating the PingOne Credentials and PingOne Davinci marketplace nodes.If you're integrating the PingOne Protect and PingOne Verify nodes, use the PingOne Worker service instead.Find more information in [Connect AM to PingOne](https://docs.pingidentity.com/pingam/8.1/integrations/connect-am-to-pingone.html). |

## Configure the PingOne service

1. Go to Realms > *realm name* > Services.

2. Click + Add a Service.

3. Select Ping One Service from the Choose a service type menu, and click Create.

4. In the Ping One Service page, make sure Enable is selected.

5. Click Save Changes.

6. Go to the Secondary Configuration tab, in the New PingOne Service configuration page, and configure these parameters:

   1. Environment ID: The ID of the environment to use in your PingOne server

      > **Collapse: How do I find an environment ID in PingOne?**
      >
      > To find your **Environment ID** value in PingOne:
      >
      > 1. In the PingOne admin console, click the Ping Identity logo.
      >
      > 2. Click **Environments**.
      >
      > 3. Select your environment from the list.
      >
      > 4. Copy the **Environment ID** value.
      >
      >    ![Locating your Environment ID and Region values in PingOne.](../../latest/_images/pingone-env-id-and-region.png)

   2. Environment Region: The region in which your PingOne environment is located

      > **Collapse: How do I find the environment region in PingOne?**
      >
      > To find your **Region** value in PingOne:
      >
      > 1. In the PingOne admin console, click the Ping Identity logo.
      >
      > 2. Click **Environments**.
      >
      > 3. Select your environment from the list.
      >
      > 4. Copy the **Region** value.
      >
      >    ![Locating your Environment ID and Region values in PingOne.](../../latest/_images/pingone-env-id-and-region.png)

   3. PingOne Client ID: Your PingOne node client ID

   4. PingOne Node Client Secret: Your PingOne node client secret

   5. PingOne Node Redirect URL: Your PingOne node redirection URL

   6. PingOne DaVinci API Key: Your PingOne DaVinci API key

   7. Worker Application Client ID: The client ID of your worker application

   8. Worker Application Client Secret: The client secret of your worker application

7. Click Create.

---

---
title: PingOne Verify Authentication node (deprecated)
description: Deprecated. The PingOne Verify Authentication node integrated PingOne Verify biometric authentication into a journey by comparing a stored picture to a live selfie.
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:pingone:pingone-verify-authn
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-authn.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["PingOne", "Verify", "Authentication"]
section_ids:
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  outcomes: Outcomes
---

# PingOne Verify Authentication node (deprecated)

The PingOne Verify Authentication node lets you integrate PingOne Verify biometric authentication functionality in your journey. The biometric authentication is achieved by comparing a stored picture to a live selfie.

|   |                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This node is deprecated and will be removed in a future release.Depending on your use case, use the following nodes instead:- [PingOne Verify Evaluation node](pingone-verify-evaluation.html)

- [PingOne Verify Completion Decision node](pingone-verify-completion-decision.html) |

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | Yes        |

## Inputs

This node reads these inputs from shared state:

The node reads the `username` from shared state.

To provide the `username` in shared state earlier in the journey, configure a node such as the [Platform Username node](../platform-username.html).

Additionally, the node first looks in the shared state for the attribute containing the PingOne UserID and the reference picture attribute, which contains a Base64-encoded reference self-image in JPEG format. If these two attributes are not found in the shared state, the node looks up the user in the local datastore to retrieve the PingOne UserID and the reference picture.

If the PingOne UserID is not found in the local datastore or the shared store, a new user is created in PingOne to perform facial-biometric authentication.

## Dependencies

You must configure [PingOne Verify service (deprecated)](pingone-verify-service.html) before using this node.

## Configuration

| Property                                                          | Usage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| PingOne Service                                                   | The ID of the PingOne Worker service for connecting to PingOne.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| PingOne Verify Policy ID                                          | The policy ID PingOne Verify node to use. The policy is expected to have the following details set:- ID Verification is set to `DISABLED`.

- Facial Comparison is set to `REQUIRED`.

- Liveness is set to `REQUIRED`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Verify URL delivery mode                                          | QR code to display or E-mail/SMS for direct delivery.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Let user choose the delivery method                               | If selected, the user is prompted for a delivery method.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Delivery message choice                                           | The message to display and allow user to select the delivery route (QR, SMS, eMail). The verify code displays along with the message.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Reference Picture Attribute                                       | The attribute key for retrieving the local reference picture. The node first looks in the shared state for the attribute containing the PingOne UserID and the reference picture attribute, which contains a Base64-encoded reference selfie in JPEG format. If these two attributes are not found in the shared state, the node looks up the user in the local datastore to retrieve the PingOne UserID and the reference picture.If `Let user choose the delivery method` is enabled or `Verify URL delivery mode` is set to use QR code, then you should store the reference picture in the shared state.If the reference picture is in the shared state, `Let user choose the delivery method` is not enabled, and `Verify URL delivery mode` is not set to use QR code, then you should store the reference picture in the transient state. |
| Attribute containing the PingOne UserID                           | Local attribute name that contains the PingOne UserID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Submission timeout                                                | Verification submission timeout value in seconds. The value must be within the authentication session validity time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Waiting message                                                   | The message to display while waiting for the user to complete the authentication with PingOne Verify.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Save verification metadata from PingOne Verify to Transient State | Save verification explanation data from PingOne Verify to Transient State with a key of `VerifyMetadataResult`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Leave access token in transientState                              | If seleted, the PingOne access token is preserved in the transient state.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Leave PingOne Verify transaction id in transientState             | If selected, the PingOne access token is preserved in the transient state, with a key of `VerifyAT`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Save verification metadata from PingOne Verify to Transient State | Save verification explanation data from PingOne Verify to Transient State with a key of `VerifyMetadataResult`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Leave access token in transientState                              | If selected, the PingOne access token is preserved in the transient state, with a key of `VerifyAT`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Leave PingOne Verify transaction id in transientState             | If checked, PingOne transaction ID is preserved in transient state with a key of `VerifyTransactionID`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Demo mode                                                         | When checked, the node always returns `SUCCESS` outcome.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

## Outputs

If the outcome is `Success (Patch ID)` or `Fail (Patch ID)`, the `Attribute containing the PingOne UserID` key is placed in shared state and in the `objectAttribute` object so the local user can be patched with the new user GUID that was created in PingOne for the verification. Save the returned GUID to the local user so the node doesn't need to create a new PingOne user on the next use.

## Outcomes

* `Success`

  Successfully authenticated the user's stored selfie and live selfie.

* `Success (Patch ID)`

  Successfully authenticated the user's stored picture and live selfie. Additionally, if the stored GUID on the local user was invalid or did not exist, the node created a new PingOne user to perform the verification. The node stored the new user's PingOne GUID in the shared state and in the objectAttribute, so the GUID can be used for future verification.

* `Fail`

  Failed to authenticate the user's stored picture and live selfie.

* `Fail (Patch ID)`

  Failed to authenticate the user's stored picture and live selfie.

* `Error`

  There was an error during the authentication process.

  If this node logs an error, review the log messages to find the reason for the error and address the issue appropriately.

---

---
title: PingOne Verify Completion Decision node
description: "Configure the PingOne Verify Completion Decision node to check the status of a user's most recent PingOne Verify identity verification transaction and return an outcome."
component: auth-node-ref
version: 8.1
page_id: auth-node-ref:pingone:pingone-verify-completion-decision
canonical_url: https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-completion-decision.html
llms_txt: https://docs.pingidentity.com/auth-node-ref/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  example: Example
  example_journey: Example journey
  example-scripts: Example scripts
  availability: Availability
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  callbacks: Callbacks
  outcomes: Outcomes
---

# PingOne Verify Completion Decision node

The PingOne Verify Evaluation node determines the completion status of the most recent identity verification transaction for a PingOne user.

The node checks the previous identity verification transaction for the user and returns an outcome based on the verification status.

You can use this node to prevent users from repeatedly having to verify their identity by checking their most recent verification transaction. You can also determine if a transaction is already in progress, to prevent multiple ongoing transactions.

For further customization of behavior, use a **PingOne Verify Completion Decision** script to evaluate the verification transactions started for the specified PingOne user, and the associated metadata. The script can then add additional context to the journey, or perform additional business logic, dependent on the verification metadata.

## Example

### Example journey

The following example journey integrates PingOne Verify to perform user identity verification.

![Example PingOne Verify journey](_images/pingone-verify-example-journey-full.png)Figure 1. Example PingOne Verify journey

* The user enters their credentials and the [Data Store Decision node](../data-store-decision.html) matches them against the identity store.

* a The [PingOne Identity Match node](pingone-identity-match.html) checks PingOne for a matching user.

* b If a user is found, the [PingOne Verify Completion Decision node](pingone-verify-completion-decision.html) checks the user's most recent verification transaction to determine the status:

  * Success

    The user successfully completed the most recent PingOne Verify transaction, so the journey progresses directly to the Success node and authentication is successful.

  * Not Completed

    The user has an existing PingOne Verify transaction in progress, so the journey resumes the existing verification transaction.

    The node adds the user's existing transaction ID to the shared node state in a variable named `pingOneVerifyTransactionId`.

  * Not Started / Failure / Expired

    * The user doesn't have an existing PingOne Verify transaction (`Not Started`)

    * The user hasn't successfully completed the most recent PingOne Verify transaction

    * The most recent PingOne Verify transaction has expired

    The journey continues to start a new verification transaction.

* c If no matching user is found, the [PingOne Create User node](pingone-create-user.html) creates a new user in PingOne.

* d The [PingOne Verify Evaluation node](pingone-verify-evaluation.html) starts a new PingOne Verify evaluation or continues an existing evaluation if `pingOneVerifyTransactionId` is present in the shared node state. The node either completes or fails the journey based on the result.

### Example scripts

These example scripts demonstrate some use cases for the PingOne Verify Completion Decision node. They use the `verifyTransactionsHelper` next-generation script binding, which gives access to the data used during a PingOne Verify transaction.

Find more information about this binding in [Access PingOne Verify transactions and manage associated user](https://docs.pingidentity.com/pingam/8.1/am-scripting/p1verify-completion-decision-api.html#common-verifytransactionshelper).

* Example 1

  Check the status of the user's most recent PingOne Verify transaction and that the ID used was a driving license.

  > **Collapse: Show example script**
  >
  > ```javascript
  > /** ******************************************************************
  >  *
  >  * The following script checks the status of the user's most recent
  >  * identity check, and ensures the ID used was a driver's license.
  >  *
  >  * Global node variables accessible within this scope:
  >  * 1. `nodeState` provides access to auth tree state attributes
  >  * 2. `verifyTransactionsHelper` provides access to verify transactions
  >  * 3. `outcome` variable maps to auth tree node outcomes; values are
  >  *    'successOutcome', 'notStartedOutcome', 'notCompletedOutcome',
  >  *    'expiredOutcome', or 'failureOutcome'.
  >  * ******************************************************************/
  >
  > // Retrieve the user's latest verified transaction.
  > var result = verifyTransactionsHelper.getLastVerifyTransaction();
  > if (result != null) {
  >     var lastTransaction = JSON.parse(result);
  >     if (lastTransaction.hasOwnProperty("transactionStatus")) {
  >         // Get the status of the transaction.
  >         var status = lastTransaction.transactionStatus.status;
  >         // Determine the document type and verify if it is a Driver's License.
  >         var verifiedDocuments = lastTransaction.verifiedDocuments;
  >         if (status == "SUCCESS" && verifiedDocuments.includes("driver_license")) {
  >             outcome = "successOutcome";
  >         } else {
  >             outcome = "failureOutcome";
  >         }
  >     } else {
  >         outcome = "notStartedOutcome";
  >     }
  > }
  > ```

- Example 2

  Check the ID used in the user's most recent PingOne Verify transaction and that their age is 18 or over.

  |   |                                                                                                                                                |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | This data is available for a short timeframe after the verification.Usually 30 minutes after PingOne Verify reaches its verification decision. |

  > **Collapse: Show example script**
  >
  > ```javascript
  > /** ******************************************************************
  >  *
  >  * The following script checks the ID used in the user's most recent
  >  * identity check, and that their age is 18 or over.
  >  *
  >  * Note:
  >  * This data is available for a short timeframe after the verification.
  >  * Usually 30 minutes after a verification decision is reached.
  >  *
  >  * Global node variables accessible within this scope:
  >  * 1. `nodeState` provides access to auth tree state attributes
  >  * 2. `verifyTransactionsHelper` provides access to verify transactions
  >  * 3. `outcome` variable maps to auth tree node outcomes; values are
  >  *    'successOutcome', 'notStartedOutcome', 'notCompletedOutcome',
  >  *    'expiredOutcome', or 'failureOutcome'.
  >  * ******************************************************************/
  >
  > // Retrieve the user's latest verified transaction.
  > var result = verifyTransactionsHelper.getLastVerifyTransaction();
  > if (result != null) {
  >     var lastTransaction = JSON.parse(result);
  >     if (lastTransaction.hasOwnProperty("id")) {
  >         // Obtain the ID of the last transaction.
  >         var lastTransactionId = lastTransaction.id;
  >         // Get the verified data for the Government ID provided by the user.
  >         var verifiedDataResult = verifyTransactionsHelper.getVerifiedDataByType(lastTransactionId, "GOVERNMENT_ID");
  >         // Determine the age of the user.
  >         if (verifiedDataResult != null) {
  >             var verifiedData = JSON.parse(verifiedDataResult);
  >             var dateString = verifiedData._embedded.verifiedData[0].data.birthDate;
  >             if (dateString != null && dateString.trim() != "") {
  >                 var birthDate = new Date(dateString + "T00:00:01");
  >                 var currentDate = new Date().getTime();
  >                 var difference = currentDate - birthDate;
  >                 var currentAge = Math.floor(difference / (1000 * 60 * 60 * 24 * 365.25));
  >                 if (currentAge >= 18) {
  >                     outcome = "successOutcome";
  >                 } else {
  >                     outcome = "failureOutcome";
  >                 }
  >             } else {
  >                 outcome = "failureOutcome";
  >             }
  >         } else {
  >             outcome = "notCompletedOutcome";
  >         }
  >     } else {
  >         outcome = "notStartedOutcome";
  >     }
  > } else {
  >     outcome = "notStartedOutcome";
  > }
  > ```

* Example 3

  Check the user's most recent PingOne Verify transaction to obtain the expiration date for the Government ID provided.

  The node stores this information in a variable named `governmentIdExpireDate` in the shared state, but you could also store it in a user attribute to determine when to perform the next identity verification.

  |   |                                                                                                                                                |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | This data is available for a short timeframe after the verification.Usually 30 minutes after PingOne Verify reaches its verification decision. |

  > **Collapse: Show example script**
  >
  > ```javascript
  > /** ******************************************************************
  >  *
  >  * The following script checks the user's most recent Verify transaction
  >  * to obtain the expiration date for the Government ID provided.
  >  *
  >  * This information is stored in a variable named `governmentIdExpireDate`
  >  * in the shared state, but could also be stored as a user attribute
  >  * to determine when to perform the next identity verification.
  >  *
  >  * Note:
  >  * This data is available for a short timeframe after the verification.
  >  * Usually 30 minutes after a verification decision is reached.
  >  *
  >  * Global node variables accessible within this scope:
  >  * 1. `nodeState` provides access to auth tree state attributes
  >  * 2. `verifyTransactionsHelper` provides access to verify transactions
  >  * 3. `outcome` variable maps to auth tree node outcomes; values are
  >  *    'successOutcome', 'notStartedOutcome', 'notCompletedOutcome',
  >  *    'expiredOutcome', or 'failureOutcome'.
  >  * ******************************************************************/
  >
  > // Retrieve the user's latest verified transaction.
  > var result = verifyTransactionsHelper.getLastVerifyTransaction();
  > if (result != null) {
  >     var lastTransaction = JSON.parse(result);
  >     if (lastTransaction.hasOwnProperty("id")) {
  >         // Obtain the ID of the last transaction.
  >         var lastTransactionId = lastTransaction.id;
  >         // Get the verified data for the Government ID provided by the user.
  >         var verifiedDataResult = verifyTransactionsHelper.getVerifiedDataByType(lastTransactionId, "GOVERNMENT_ID");
  >         // Get the expire date and set on shared state.
  >         if (verifiedDataResult != null) {
  >             var verifiedData = JSON.parse(verifiedDataResult);
  >             var expireDate = verifiedData._embedded.verifiedData[0].data.expirationDate;
  >             if (expireDate != null && expireDate.trim() != "") {
  >                 nodeState.putShared("governmentIdExpireDate", expireDate);
  >                 outcome = "successOutcome";
  >             } else {
  >                 outcome = "failureOutcome";
  >             }
  >         } else {
  >             outcome = "notCompletedOutcome";
  >         }
  >     } else {
  >         outcome = "notStartedOutcome";
  >     }
  > } else {
  >     outcome = "notStartedOutcome";
  > }
  > ```

- Example 4

  Check that the user has at least one successful identity verification in the past 365 days.

  > **Collapse: Show example script**
  >
  > ```javascript
  > /** ******************************************************************
  >  *
  >  * The following script checks that the user has at least one successful
  >  * identity verification in the past 365 days.
  >  *
  >  * Global node variables accessible within this scope:
  >  * 1. `nodeState` provides access to auth tree state attributes
  >  * 2. `verifyTransactionsHelper` provides access to verify transactions
  >  * 3. `outcome` variable maps to auth tree node outcomes; values are
  >  *    'successOutcome', 'notStartedOutcome', 'notCompletedOutcome',
  >  *    'expiredOutcome', or 'failureOutcome'.
  >  * ******************************************************************/
  >
  > // Retrieve all transactions for the user
  > var result = verifyTransactionsHelper.getAllVerifyTransactions();
  > if (result != null) {
  >     var allTransactions = JSON.parse(result);
  >     if (allTransactions != null) {
  >         // Loop through the transactions to find a successful verification within the last 12 months.
  >         var verifyTransactions = allTransactions._embedded.verifyTransactions;
  >         var found = false;
  >         for (var i = 0; i < verifyTransactions.length; i++) {
  >             var transaction = verifyTransactions[i];
  >             // Get the status of the transaction.
  >             var status = transaction.transactionStatus.status;
  >             // If status is success, verify if it is still valid
  >             if (status == "SUCCESS") {
  >                 found = true;
  >                 // Calculate the number of days
  >                 var dateString = transaction.createdAt;
  >                 var createdDate = new Date(dateString);
  >                 var currentDate = new Date().getTime();
  >                 var difference = Math.abs(createdDate - currentDate);
  >                 var numDaysBetween = difference / (1000 * 60 * 60 * 24);
  >                 if (numDaysBetween <= 365) {
  >                     outcome = "successOutcome";
  >                     break;
  >                 } else {
  >                     outcome = "expiredOutcome";
  >                 }
  >             }
  >         }
  >         // No successful transaction found
  >         if (found == false) {
  >             outcome = "failureOutcome";
  >         }
  >     } else {
  >         outcome = "notStartedOutcome";
  >     }
  > } else {
  >     outcome = "notStartedOutcome";
  > }
  > ```

* Example 5

  Check the user's most recent PingOne Verify transaction to review the biographic match results.

  The script uses the Failure outcome if the match confidence for any attribute is anything other than `HIGH`.

  > **Collapse: Show example script**
  >
  > ```javascript
  > /** ******************************************************************
  >  *
  >  * The following script checks the user's last identity verification to
  >  * review the "Biographic Match" results.
  >  *
  >  * The script uses the failure outcome if the match confidence for any
  >  * attribute is below `HIGH`.
  >  *
  >  * Global node variables accessible within this scope:
  >  * 1. `nodeState` provides access to auth tree state attributes
  >  * 2. `verifyTransactionsHelper` provides access to verify transactions
  >  * 3. `outcome` variable maps to auth tree node outcomes; values are
  >  *    'successOutcome', 'notStartedOutcome', 'notCompletedOutcome',
  >  *    'expiredOutcome', or 'failureOutcome'.
  >  * ******************************************************************/
  >
  > // Retrieve the user's latest verified transaction.
  > var result = verifyTransactionsHelper.getLastVerifyTransaction();
  > if (result != null) {
  >     var lastTransaction = JSON.parse(result);
  >     if (lastTransaction.hasOwnProperty("id")) {
  >         // Obtain the ID of the last transaction.
  >         var lastTransactionId = lastTransaction.id;
  >         // Get all the metadata.
  >         var allMetadataResult = verifyTransactionsHelper.getAllMetadata(lastTransactionId);
  >         // Loop through the metadata to find the biographic match results.
  >         var biographicMatchResults;
  >         if (allMetadataResult != null) {
  >             var allMetadataJson = JSON.parse(allMetadataResult);
  > 			var allMetadata = allMetadataJson._embedded.metaData;
  >             for (var i = 0; i < allMetadata.length; i++) {
  >                 var metadata = allMetadata[i];
  >                 var type = metadata.type;
  >                 var status = metadata.status;
  >                 if (type == "BIOGRAPHIC_MATCH" && status == "SUCCESS") {
  >                     biographicMatchResults = metadata.data.biographic_match_results;
  >                     break;
  >                 }
  >             }
  >         } else {
  >             outcome = "failureOutcome";
  >         }
  >         // Validate the biographic match results
  >         if (biographicMatchResults != null && biographicMatchResults.length > 0) {
  >             var success = true;
  >             for (var j = 0; j < biographicMatchResults.length; j++) {
  >                 var match = biographicMatchResults[j].match;
  >                 if (match != "HIGH") {
  > 					success = false;
  > 					break;
  >                 }
  >             }
  >             if (success) {
  >                 outcome = "successOutcome";
  >             } else {
  >                 outcome = "failureOutcome";
  >             }
  >         } else {
  >             outcome = "failureOutcome";
  >         }
  >     } else {
  >         outcome = "notStartedOutcome";
  >     }
  > } else {
  >     outcome = "notStartedOutcome";
  > }
  > ```

## Availability

| Product                               | Available? |
| ------------------------------------- | ---------- |
| PingOne Advanced Identity Cloud       | Yes        |
| PingAM (self-managed)                 | Yes        |
| Ping Identity Platform (self-managed) | Yes        |

## Inputs

This node requires that the user has an account in the PingOne environment. It requires that the journey stores the PingOne user ID for the account in the shared state variable named `pingOneUserId`.

Use a [PingOne Identity Match node](pingone-identity-match.html) to populate the shared state with the user's PingOne ID.

The shared state data must also include all required Script Inputs properties.

You can restrict available inputs using the Script Inputs field when configuring the node.

## Dependencies

This node requires a PingOne Worker Service configuration so that it can connect to your PingOne instance and send it the necessary data to perform PingOne Verify evaluations as part of the journey.

Find more information in [Connect AM to PingOne](https://docs.pingidentity.com/pingam/8.1/integrations/connect-am-to-pingone.html).

## Configuration

| Property                                    | Usage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PingOne Worker service ID                   | The ID of the PingOne worker service for connecting to PingOne.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Use a script to process Verify transactions | When enabled, use a **PingOne Verify Completion Decision** script to process verification transaction data relating to the user.> **Collapse: Example verification transaction data**
>
> ```json
> {
>     "_links": {
>         "self": {
>             "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/36ff33da-cba7-4d46-bedc-8b242889d461/verifyTransactions"
>         }
>     },
>     "_embedded": {
>         "verifyTransactions": [
>             {
>                 "_links": {
>                     "self": {
>                         "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/36ff33da-cba7-4d46-bedc-8b242889d461/verifyTransactions/029ea878-2618-4067-b7e3-922591e6b55f"
>                     },
>                     "environment": {
>                         "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
>                     },
>                     "user": {
>                         "href": "https://api.pingone.com/v1/users/36ff33da-cba7-4d46-bedc-8b242889d461"
>                     }
>                 },
>                 "id": "029ea878-2618-4067-b7e3-922591e6b55f",
>                 "transactionStatus": {
>                     "status": "APPROVED_NO_REQUEST"
>                 },
>                 "createdAt": "2022-02-17T20:32:22.052Z",
>                 "updatedAt": "2022-02-17T20:32:58.711Z",
>                 "expiresAt": "2022-02-17T21:02:58.711Z"
>             },
>             {
>                 "_links": {
>                     "self": {
>                         "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/36ff33da-cba7-4d46-bedc-8b242889d461/verifyTransactions/cca479e7-d130-4e3c-b888-74ba1920f59a"
>                     },
>                     "environment": {
>                         "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
>                     },
>                     "user": {
>                         "href": "https://api.pingone.com/v1/users/36ff33da-cba7-4d46-bedc-8b242889d461"
>                     }
>                 },
>                 "id": "cca479e7-d130-4e3c-b888-74ba1920f59a",
>                 "transactionStatus": {
>                     "status": "REQUESTED"
>                 },
>                 "qrUrl": "https://api.pingone.com/v1/idValidations/shortcode/086645084110/qr",
>                 "verificationCode": "086645084110",
>                 "createdAt": "2022-02-17T20:23:58.662Z",
>                 "updatedAt": "2022-02-17T20:23:58.662Z",
>                 "expiresAt": "2022-02-17T20:53:58.662Z"
>             },
>             {
>                 "_links": {
>                     "self": {
>                         "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/36ff33da-cba7-4d46-bedc-8b242889d461/verifyTransactions/52c9bf9a-0687-4e01-85d1-9caa9bb387ee"
>                     },
>                     "environment": {
>                         "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
>                     },
>                     "user": {
>                         "href": "https://api.pingone.com/v1/users/36ff33da-cba7-4d46-bedc-8b242889d461"
>                     }
>                 },
>                 "id": "52c9bf9a-0687-4e01-85d1-9caa9bb387ee",
>                 "transactionStatus": {
>                     "status": "REQUESTED"
>                 },
>                 "qrUrl": "https://api.pingone.com/v1/idValidations/shortcode/008299320746/qr",
>                 "verificationCode": "008299320746",
>                 "createdAt": "2022-02-17T20:23:08.887Z",
>                 "updatedAt": "2022-02-17T20:23:08.887Z",
>                 "expiresAt": "2022-02-17T20:53:08.887Z"
>             },
>             {
>                 "_links": {
>                     "self": {
>                         "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/36ff33da-cba7-4d46-bedc-8b242889d461/verifyTransactions/dd5a6d4f-a999-4819-b107-85a0a10138c6"
>                     },
>                     "environment": {
>                         "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
>                     },
>                     "user": {
>                         "href": "https://api.pingone.com/v1/users/36ff33da-cba7-4d46-bedc-8b242889d461"
>                     }
>                 },
>                 "id": "dd5a6d4f-a999-4819-b107-85a0a10138c6",
>                 "transactionStatus": {
>                     "status": "REQUESTED"
>                 },
>                 "createdAt": "2021-12-09T13:45:34.882Z",
>                 "updatedAt": "2021-12-09T13:45:34.882Z",
>                 "expiresAt": "2022-12-09T14:15:34.882Z"
>             },
>             {
>                 "_links": {
>                     "self": {
>                         "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/36ff33da-cba7-4d46-bedc-8b242889d461/verifyTransactions/bfc414cb-a1b4-46b8-b622-3d806a85002f"
>                     },
>                     "environment": {
>                         "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
>                     },
>                     "user": {
>                         "href": "https://api.pingone.com/v1/users/36ff33da-cba7-4d46-bedc-8b242889d461"
>                     }
>                 },
>                 "id": "bfc414cb-a1b4-46b8-b622-3d806a85002f",
>                 "transactionStatus": {
>                     "status": "REQUESTED"
>                 },
>                 "createdAt": "2021-12-08T21:34:52.424Z",
>                 "updatedAt": "2021-12-08T21:34:52.424Z",
>                 "expiresAt": "2022-12-08T22:04:52.424Z"
>             },
>             {
>                 "_links": {
>                     "self": {
>                         "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/36ff33da-cba7-4d46-bedc-8b242889d461/verifyTransactions/b21db4c4-01c5-47b5-a2a9-3d8df21d189b"
>                     },
>                     "environment": {
>                         "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
>                     },
>                     "user": {
>                         "href": "https://api.pingone.com/v1/users/36ff33da-cba7-4d46-bedc-8b242889d461"
>                     }
>                 },
>                 "id": "b21db4c4-01c5-47b5-a2a9-3d8df21d189b",
>                 "transactionStatus": {
>                     "status": "APPROVED_NO_REQUEST"
>                 },
>                 "createdAt": "2021-12-07T21:33:22.088Z",
>                 "updatedAt": "2021-12-07T21:45:22.944Z",
>                 "expiresAt": "2022-12-07T22:15:22.944Z"
>             },
>             {
>                 "_links": {
>                     "self": {
>                         "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/36ff33da-cba7-4d46-bedc-8b242889d461/verifyTransactions/e44ebfe2-6a76-4ffa-ac35-d71ee9365e57"
>                     },
>                     "environment": {
>                         "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
>                     },
>                     "user": {
>                         "href": "https://api.pingone.com/v1/users/36ff33da-cba7-4d46-bedc-8b242889d461"
>                     }
>                 },
>                 "id": "e44ebfe2-6a76-4ffa-ac35-d71ee9365e57",
>                 "transactionStatus": {
>                     "status": "APPROVED_NO_REQUEST"
>                 },
>                 "createdAt": "2021-12-07T19:55:16.630Z",
>                 "updatedAt": "2021-12-07T21:31:26.835Z",
>                 "expiresAt": "2022-12-07T22:01:26.835Z"
>             },
>             {
>                 "_links": {
>                     "self": {
>                         "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6/users/36ff33da-cba7-4d46-bedc-8b242889d461/verifyTransactions/fc695b11-93a4-48bb-9ec3-ff5738e3818c"
>                     },
>                     "environment": {
>                         "href": "https://api.pingone.com/v1/environments/abfba8f6-49eb-49f5-a5d9-80ad5c98f9f6"
>                     },
>                     "user": {
>                         "href": "https://api.pingone.com/v1/users/36ff33da-cba7-4d46-bedc-8b242889d461"
>                     }
>                 },
>                 "id": "fc695b11-93a4-48bb-9ec3-ff5738e3818c",
>                 "transactionStatus": {
>                     "status": "REQUESTED"
>                 },
>                 "createdAt": "2021-12-07T18:36:48.156Z",
>                 "updatedAt": "2021-12-07T18:36:48.156Z",
>                 "expiresAt": "2021-12-07T19:06:48.153Z"
>             }
>         ]
>     },
>     "size": 8
> }
> ```Learn more about verification transaction data in [Read All Verify Transactions](https://developer.pingidentity.com/pingone-api/verify/verify-transactions/read-all-verify-transactions.html). |
| Manage Verify transactions script           | The name of the script to process the JSON containing verification transactions relating to the user.The script must be of type PingOne Verify Completion Decision.Refer to [Example scripts](#example-scripts).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Script Inputs                               | Optionally, list the shared state data properties required by the script.Declare each required property, enter `null` for no properties, or set to `*` for access to all shared and transient state data.Default: `*`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Capture failure                             | Capture the details in shared state if a failure occurs.The node stores the details in a variable named `pingOneVerifyCompletionFailureReason`.Default: `False`Example:```json
{
  "code": "VERIFY_COMPLETION_SCRIPT_ERROR",
  "message": "Error evaluating the verify completion decision script.",
  "exception": "",
}
```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

## Outputs

If the node discovers that the user's most recent Verify transaction isn't yet complete, it adds the ID of the transaction to the shared state, in a variable named `pingOneVerifyTransactionId`. The [PingOne Verify Evaluation node](pingone-verify-evaluation.html) can use this value to continue the existing Verify evaluation, rather than start a brand new one.

If you select Capture failure, the node stores any error response in a shared state variable named `pingOneVerifyCompletionFailureReason`.

If you enable the Use a script to process Verify transactions property, the script you specify can add values to the shared state, as required.

## Callbacks

This node doesn't send any callbacks.

## Outcomes

* `Success`

  The user successfully completed their most recent PingOne Verify evaluation.

* `Failure`

  The user did not successfully complete their most recent PingOne Verify evaluation, or an error occurred.

* `Expired`

  The user's most recent PingOne Verify evaluation timed out. Usually this happens when a user starts a verification transaction, but does not complete it within the time limit.

* `Not Started`

  The user's most recent PingOne Verify evaluation has not yet started.

* `Not Completed`

  The user's most recent PingOne Verify evaluation has started, but not yet completed.