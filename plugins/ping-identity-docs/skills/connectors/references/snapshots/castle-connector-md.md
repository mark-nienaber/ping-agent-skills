---
title: Castle Connector
description: "Configure the Castle connector to add fraud and risk signals to PingOne DaVinci flows, block bots, and request risk evaluations from Castle's API"
component: connectors
page_id: connectors::castle_connector
canonical_url: https://docs.pingidentity.com/connectors/castle_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  setting-up-castle: Setting up Castle
  configuring-the-castle-connector: Configuring the Castle connector
  connector-configuration: Connector configuration
  api-secret: API Secret
  using-the-connector-in-a-flow: Using the connector in a flow
  registration-and-login-traffic-filtration: Registration and Login Traffic Filtration
  risk-evaluation: Risk evaluation
  creating-a-custom-api-call: Creating a custom API call
  capabilities: Capabilities
  filter-registration-and-login-traffic: Filter registration and login traffic
  risk-evaluation-2: Risk Evaluation
---

# Castle Connector

The Castle connector lets you add additional risk signals with Castle's fraud and risk management platform in your PingOne DaVinci flow.

You can use the Castle connector to:

* Filter registration and login traffic to block bots and bad traffic

* Request a risk evaluation from Castle's API

## Setup

### Resources

Learn more in the following:

* Castle documentation:

  * [Introduction to Castle](https://docs.castle.io/docs)

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* A Castle license

* Your Castle credentials

### Setting up Castle

Follow the instructions in the [Castle documentation](https://docs.castle.io/docs/an-introduction-to-castle).

### Configuring the Castle connector

Add the connector in PingOne DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

##### API Secret

Your 32-character Castle API secret, for example, `Olc3…​YIBF`.

## Using the connector in a flow

### Registration and Login Traffic Filtration

You can use the **Filter Registration and Login Traffic** capability to block bots and bad traffic early in the request chain based on context and user information.

No special configuration is needed. Add the capability and populate its properties according to the help text.

### Risk evaluation

You can use the **Get Risk Evaluation** capability to request a risk evaluation from Castle's API.

No special configuration is needed. Add the capability and populate its properties according to the help text.

### Creating a custom API call

If you want to do something not supported by one of the provided capabilities, you can use the **Make a Custom API Call** capability to define your own action.

This capability uses the credentials from your connector to make an API call with the HTTP method, headers, query parameters, and body you specify.

## Capabilities

### Filter registration and login traffic

Used to block bots and bad traffic early in the request chain, typically at registration.

> **Collapse: Show details**
>
> * * Properties
>   * Body `codeEditor` `required`
>
>   The raw JSON body, such as "{ "Username": "<jsmith@example.com>", "Session ID": "00e8a0000024zkjAAA" }".
>
> - - Output Schema
>   - output `object`
>   - rawResponse `object`
>   - statusCode `number`
>   - headers `object`
>   - status `string`

### Risk Evaluation

Used to request a risk evaluation from Castle's API

> **Collapse: Show details**
>
> * * Properties
>   * Body `codeEditor` `required`
>
>   The raw JSON body, such as "{ "Username": "<jsmith@example.com>", "Session ID": "00e8a0000024zkjAAA" }".
>
> - - Output Schema
>   - output `object`
>   - rawResponse `object`
>   - statusCode `number`
>   - headers `object`