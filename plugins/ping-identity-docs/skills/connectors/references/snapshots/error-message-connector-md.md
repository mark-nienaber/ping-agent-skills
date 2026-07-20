---
title: Error Message Connector
description: Configure the Error Message connector to create and customize error messages displayed to users in your PingOne DaVinci flows
component: connectors
page_id: connectors::error_message_connector
canonical_url: https://docs.pingidentity.com/connectors/error_message_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  setup: Setup
  resources: Resources
  configuring-the-error-message-connector: Configuring the Error Message connector
  using-the-connector-in-a-flow: Using the connector in a flow
  custom-error-message-creation: Custom error message creation
  capabilities: Capabilities
  customErrorMessage: Custom Error Message On Screen
---

# Error Message Connector

The Error Message connector lets you create and customize the error messages that appear in your PingOne DaVinci flow.

You can use the Error Message connector to customize an error message shown in the user interface.

## Setup

### Resources

Learn more in the following:

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Configuring the Error Message connector

In PingOne DaVinci, add an Error Message connector. Learn more in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html).

This connector doesn't have a configuration at the environment level. You configure it in your flow instead.

## Using the connector in a flow

### Custom error message creation

You can use the **Custom error message on screen** capability to create a custom error message and set when that error appears on screen.

To use the connector in the flow, you must add the `skerror` component to an HTTP connector node in your flow.

|   |                                                                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can add the component to the **Custom HTML Template** of the HTTP connector in your flow, formatted as `<div data-skcomponent="skerror"></div>`. Learn more in [SK-Components reference](https://docs.pingidentity.com/davinci/flows/davinci_sk_components_reference_guide.html). |

## Capabilities

### Custom Error Message On Screen

Customize Error message shown on UI/Screen

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> - errorMessage textField
>
>   Custom Error Message
>
> - errorDescription textField
>
>   Custom Error Description
>
> - Error Code dropDown
>
>   Custom Error Code
>
>   * 400
>
>   * 403
>
>   * 404
>
>   * 405
>
>   * 429
>
>   * 500
>
> - errorReason textField
>
>   Custom Error Reason
>
> - errorCallbackSuppress toggleSwitch
>
> * default object