---
title: WireWheel Connector
description: Configure the WireWheel connector in PingOne DaVinci to manage customer consent records in your flow
component: connectors
page_id: connectors::wirewheel_connector
canonical_url: https://docs.pingidentity.com/connectors/wirewheel_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 24, 2026
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  configuring-the-wirewheel-connector: Configuring the WireWheel connector
  connector-configuration: Connector configuration
  using-the-connector-in-a-flow: Using the connector in a flow
  managing-consent-records-in-a-flow: Managing consent records in a flow
  capabilities: Capabilities
  getChannel: Get Channel Information
  getExistingConsent: Get Existing Consent
  consentForm: Consent Form
  writeConsent: Write Consent Data
---

# WireWheel Connector

The WireWheel connector lets you manage customer consent records through [WireWheel](https://www.osano.com/solutions/consent-management-platform) in your PingOne DaVinci flow.

The connector displays consent forms and writes consent data to your WireWheel environment so that you can honor user privacy preferences in your flow.

## Setup

### Resources

You can find more information and setup help in the following:

* WireWheel documentation:

  * [WireWheel consent management documentation](https://www.osano.com/solutions/consent-management-platform)

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* The Base API URL of your WireWheel environment.

* The issuer URL, client ID, client secret, and channel ID from your WireWheel channel settings.

### Configuring the WireWheel connector

Add the connector in PingOne DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

| Setting                | Description                                                                              |
| ---------------------- | ---------------------------------------------------------------------------------------- |
| WireWheel Base API URL | The base API URL of your WireWheel environment, such as <https://api.upcp.wirewheel.io>. |
| Issuer URL             | The issuer URL from your WireWheel channel settings.                                     |
| Client ID              | The client ID from your WireWheel channel settings.                                      |
| Client Secret          | The client secret from your WireWheel channel settings.                                  |

## Using the connector in a flow

### Managing consent records in a flow

You can use the connector to retrieve channel information, check for existing consent, display the WireWheel consent form, and write consent data to WireWheel.

At a high level:

1. The **Get Channel Information** capability retrieves WireWheel channel information using the channel ID from your WireWheel channel settings.

2. The **Get Existing Consent** capability retrieves the existing consent record for the username you specify.

3. The **Consent Form** capability displays the WireWheel consent form with a default HTML template, CSS, and script, and writes the submitted consent record to WireWheel.

4. The **Write Consent Data** capability saves consent data to WireWheel using a properly formatted JSON consent payload.

|   |                                                           |
| - | --------------------------------------------------------- |
|   | The connector verifies a single consent record at a time. |

Test the flow by clicking **Save**, **Deploy**, and **Try Flow**.

## Capabilities

### Get Channel Information

Retrieve WireWheel Channel Information

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - Channel ID textField required
>
>   Channel ID from WireWheel Channel settings
>
> * output object
>
>   * channel object

### Get Existing Consent

Retrieve the existing consent by the username

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - Username textField required
>
>   Username of the consent record
>
> * output object
>
>   * consent object

### Consent Form

Displays the WireWheel Consent Form

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - Channel ID textField required
>
>   Channel ID from WireWheel Channel settings
>
> - Username textField required
>
>   Username of the consent record
>
> - Get Existing Consent toggleSwitch required
>
>   Toggle to retrieve existing consent record
>
> * output object
>
>   * consentPayload object
>
>   * writeConsentStatusCode number
>
>   * writeConsentStatusText string

### Write Consent Data

Saves the consent data to Wirewheel

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - Consent Payload (JSON) textArea
>
>   The Consent Payload from WireWheel in JSON format.
>
> * output object
>
>   * statusCode number
>
>   * headers object