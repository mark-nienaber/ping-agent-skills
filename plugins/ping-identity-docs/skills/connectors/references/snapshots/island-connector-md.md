---
title: Island Connector
description: The Island connector lets you use Island device trust signals in your PingOne DaVinci flow.
component: connectors
page_id: connectors::island_connector
canonical_url: https://docs.pingidentity.com/connectors/island_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 30, 2025
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  configuring-the-island-connector: Configuring the Island connector
  connector-configuration: Connector configuration
  redirect-url: Redirect URL
  island-api-key: Island API Key
  island-base-url: Island Base URL
  generate-challenge-endpoint: Generate Challenge Endpoint
  verify-challenge-endpoint: Verify Challenge Endpoint
  application-return-to-url: Application Return To URL
  using-the-connector-in-a-flow: Using the connector in a flow
  device-trust: Device Trust
  capabilities: Capabilities
  initializeAuthorizationRequest: Device Trust
---

# Island Connector

The Island connector lets you use Island device trust signals in your PingOne DaVinci flow.

## Setup

### Resources

You can find more information and setup help in the following:

* Island documentation

  * [Island Resources](https://www.island.io/resources)

* DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* An Island API key

* Your Island base URL

* Endpoint paths for generating and verifying the device trust challenge.

### Configuring the Island connector

Add the connector in DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

##### Redirect URL

The redirect URL used by DaVinci. This value is provided automatically in the connector as a read-only field.

##### Island API Key

Your Island API key.

##### Island Base URL

The base URL for your Island environment.

##### Generate Challenge Endpoint

The endpoint path to request a device trust challenge from Island.

##### Verify Challenge Endpoint

The endpoint path to verify a device trust challenge with Island.

##### Application Return To URL

(Optional) When using the embedded flow player widget and an identity provider (IdP) or social login connector, provide a callback URL for returning to your application.

## Using the connector in a flow

### Device Trust

The **Device Trust** capability initiates a device challenge with Island, then verifies the response and returns device context to your flow.

At a high level:

1. The capability initializes and redirects the user to the DaVinci OAuth2 callback URL with the Island challenge included in the x-verified-access-challenge header.

2. After the user returns to the flow, the capability reads the corresponding x-verified-access-challenge-response value, verifies it with Island, and outputs device trust details you can evaluate in your journey.

When device trust is enabled and the response is verified, the output includes device trust status and related device context.

If device trust isn't enabled, the connector returns a success status with device trust disabled and empty response details so your flow can continue accordingly.

## Capabilities

### Device Trust

Authenticate against the Island Enterprise Browser for Device Trust verification.

> **Collapse: Show details**
>
> * Input Schema
>
> * Output Schema
>
> - default object
>
>   * properties object
>
> * output object
>
>   * rawResponse object
>
>   * statusCode number
>
>   * headers object
>
>   * deviceTrustEnabled boolean
>
>   * devicePermanentId string
>
>   * virtualDeviceId string
>
>   * virtualProfileId string
>
>   * customerId string
>
>   * profileCustomerId string
>
>   * keyTrustLevel string
>
>   * profileKeyTrustLevel string
>
>   * deviceSignals object
>
>     * browserVersion string
>
>     * builtInDnsClientEnabled boolean
>
>     * chromeCleanupEnabled boolean
>
>     * chromeRemoteDesktopAppBlocked boolean
>
>     * crowdStrikeAgentId string
>
>     * crowdStrikeCustomerId string
>
>     * deviceAffiliationIds array
>
>     * hostname string
>
>     * deviceManufacturer string
>
>     * deviceModel string
>
>     * diskEncryption string
>
>     * displayName string
>
>     * macAddresses array
>
>     * operatingSystem string
>
>     * osFirewall string
>
>     * osVersion string
>
>     * realtimeUrlCheckMode string
>
>     * safeBrowsingProtectionLevel string
>
>     * screenLockSecured string
>
>     * secureBootEnabled string
>
>     * serialNumber string
>
>     * siteIsolationEnabled boolean
>
>     * systemDnsServers array
>
>     * thirdPartyBlockingEnabled boolean
>
>     * passwordProtectionWarningTrigger string
>
>     * trigger string
>
>     * windowsMachineDomain string
>
>     * windowsUserDomain string
>
>     * profileAffiliationIds array
>
>     * profileEnrollmentDomain string
>
>     * deviceEnrollmentDomain string
>
>     * signedPublicKeyAndChallenge string