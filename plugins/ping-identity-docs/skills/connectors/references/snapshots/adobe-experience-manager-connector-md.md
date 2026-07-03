---
title: Adobe Experience Manager Connector
description: The Adobe Experience Manager connector enables your PingOne DaVinci flow to manage data privacy and consent within Adobe Experience Platform (AEP).
component: connectors
page_id: connectors::adobe_experience_manager_connector
canonical_url: https://docs.pingidentity.com/connectors/adobe_experience_manager_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 21, 2025
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  configuring-the-adobe-experience-manager-connector: Configuring the Adobe Experience Manager connector
  connector-configuration: Connector configuration
  client-id: Client ID
  client-secret: Client Secret
  organization-id: Organization ID
  using-the-connector-in-a-flow: Using the connector in a flow
  process-opt-out-of-sale-request: Process opt-out-of-sale request
  check-consent-status: Check consent status
  capabilities: Capabilities
  processOptOutOfSaleRequest: Opt Out of Sale Request
  getConsentStatus: Get Consent Status
---

# Adobe Experience Manager Connector

The Adobe Experience Manager connector enables your PingOne DaVinci flow to manage data privacy and consent within Adobe Experience Platform (AEP).

This connector provides two capabilities to help ensure CCPA/CPRA compliance:

* **Process opt-out-of-sale requests:** Allows customers to opt out of the selling or sharing of their personal data within AEP.

* **Check consent status:** Allows your flow to query customer profiles within AEP to check if their data is collectable or shareable.

## Setup

### Resources

You can find more information and setup help in the following:

* DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need an Adobe Experience Cloud license with API credentials provisioned for the [Privacy Service API](https://developer.adobe.com/experience-platform-apis/references/privacy-service/) and the [Real-time Customer Profile API](https://developer.adobe.com/experience-platform-apis/references/profile/).

### Configuring the Adobe Experience Manager connector

Add the connector in DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

To get the following information, you must create a service account integration in the [Adobe Developer Console](https://developer.adobe.com/console). Learn more in [Authenticate and access the Privacy Service API](https://experienceleague.adobe.com/en/docs/experience-platform/privacy/api/getting-started#) in the Adobe documentation.

##### Client ID

The public ID generated for your application. Used to identify the client requesting access to your Adobe Experience Cloud services.

##### Client Secret

The secret key generated for your application. Used to authenticate the client ID for your Adobe Experience Cloud services.

##### Organization ID

The ID representing your organization's tenant within Adobe Experience Cloud.

## Using the connector in a flow

### Process opt-out-of-sale request

![A screen capture of the complete opt-out-of-sale request flow.](_images/connector-images/tap-adobe-experience-manager-opt-out-request-flow.png)

This flow prompts a user to enter a namespace and an identifier for a profile within AEP. The connector then submits an opt-out-of-sale privacy job to the [Privacy Service API](https://developer.adobe.com/experience-platform-apis/references/privacy-service/) for that specific user and outputs whether the job was successfully created. Importantly, this returns the status of the job's creation, not the final successful completion of the opt-out request. This service applies the requested change to all sandboxes within your Adobe Experience Cloud tenant. You can find more information in the [Adobe documentation](https://experienceleague.adobe.com/en/docs/experience-platform/privacy/home).

Test the flow by clicking **Save**, **Deploy**, and **Try Flow**.

### Check consent status

![A screen capture of the complete check consent status flow.](_images/connector-images/tap-adobe-experience-manager-consent-status-flow.png)

This flow prompts a user to enter a namespace, an identifier, and a sandbox name to specify a profile within AEP. The connector then queries the [Real-time Customer Profile API](https://developer.adobe.com/experience-platform-apis/references/profile/) to retrieve and return the current consent status for that profile. To ensure functionality, the AEP profile schema used must be configured to include the default consent field group. You can find more information in the [Adobe documentation](https://experienceleague.adobe.com/en/docs/experience-platform/landing/governance-privacy-security/consent/adobe/dataset).

Test the flow by clicking **Save**, **Deploy**, and **Try Flow**.

## Capabilities

### Opt Out of Sale Request

Submits a privacy request to Adobe Experience Platform to register a customer's preference to opt out of data sale.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Name Space dropDown required
>
>   The identifier category
>
>   * Email (Default)
>
>   * Phone
>
>   * Adobe Advertising Cloud ID
>
>   * Adobe Audience Manager UUID
>
>   * Adobe Experience Cloud ID
>
>   * Adobe Target ID
>
>   * Apple ID for Advertisers
>
>   * Google Ad ID
>
>   * Windows AID
>
> - Value textField required
>
>   The specific identifier
>
> - Request ID textField
>
>   Tracking ID for this request
>
> - Transaction ID textField
>
>   Source transaction ID
>
> * default object
>
>   * properties object
>
>     * nameSpace string
>
>       The type of user identifier, recognized by Adobe Experience Platform (e.g., "email" or "ECID").
>
>     * value string
>
>       The specific identifier for the user, which must match the selected namespace (e.g., "<jane.doe@example.com>").
>
>     * requestId string
>
>       An optional identifier that tracks the individual API call for your own auditing and logging purposes.
>
>     * transactionId string
>
>       An optional identifier that links this privacy request to the originating transaction event.
>
> Input Example
>
> ```json
>  { "properties" :
>   { "nameSpace" : "email",
>    "value" : "jane.doe@example.com",
>    "requestId" : "f47ac10b-58cc-4372-a567-0e02b2c3d479",
>    "transactionId" : "crm-case-8812345" } }
> ```
>
> * output object
>
>   * rawResponse object
>
>     The full, unmodified JSON object returned directly from the external API call.
>
>   * statusCode number
>
>     The HTTP status code returned by the API request.
>
>   * message string
>
>     The success or failure message
>
> Output Example
>
> ```json
>  { "rawResponse" :
>   {  },
>   "statusCode" : 202,
>   "message" : "Accepted" }
> ```

### Get Consent Status

Checks a customer's current status for opting out of data sale.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Name Space dropDown required
>
>   The identifier category
>
>   * Email (Default)
>
>   * Phone
>
>   * Adobe Advertising Cloud ID
>
>   * Adobe Audience Manager UUID
>
>   * Adobe Experience Cloud ID
>
>   * Adobe Target ID
>
>   * Apple ID for Advertisers
>
>   * Google Ad ID
>
>   * Windows AID
>
> - Value textField required
>
>   The specific identifier
>
> - Sandbox Name textField required
>
>   Name of the Adobe Experience Platform sandbox to target
>
> * default object
>
>   * properties object
>
>     * nameSpace string
>
>       The type of user identifier, recognized by Adobe Experience Platform (e.g., "email" or "ECID").
>
>     * value string
>
>       The specific identifier for the user, which must match the selected namespace (e.g., "<jane.doe@example.com>").
>
>     * sandboxName string
>
>       The name of the Adobe Experience Platform sandbox to target. Sandboxes are isolated environments (e.g., "prod", "dev", "stage") that contain separate datasets, schemas, and profiles.
>
> Input Example
>
> ```json
>  { "properties" :
>   { "nameSpace" : "email",
>    "value" : "jane.doe@example.com",
>    "sandboxName" : "prod" } }
> ```
>
> * output object
>
>   * rawResponse object
>
>     The full, unmodified JSON object returned directly from the external API call.
>
>   * statusCode number
>
>     The HTTP status code returned by the API request.
>
>   * isDataCollectible string
>
>     The consent status for data collecting. "y" (yes/opt-in), "N" (no/opt-out), "undefined" (not available).
>
>   * isDataShareable string
>
>     The consent status for data sharing. "y" (yes/opt-in), "N" (no/opt-out), "undefined" (not available).
>
> Output Example
>
> ```json
>  { "rawResponse" :
>   { "entityId" : "jane.doe@example.com",
>    "entityIdNS" : "Email",
>    "entity" :
>    { "consents" :
>     { "collect" :
>      { "val" : "y" },
>      "share" :
>      { "val" : "n" },
>      "marketing" :
>      { "email" :
>       { "val" : "y" } },
>      "metadata" :
>      { "time" : "2025-10-01T09:00:00Z" } },
>     "identityMap" :
>     { "Email" :
>      [
>       { "id" : "jane.doe@example.com" } ] } },
>    "sources" :
>    [  ] },
>   "statusCode" : 200,
>   "isDataCollectible" : "y",
>   "isDataShareable" : "n" }
> ```