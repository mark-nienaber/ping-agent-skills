---
title: Screen Connector
description: Configure the Screen connector to display forms and custom UI elements to collect user information or show PingOne DaVinci flow progress
component: connectors
page_id: connectors::screen_connector
canonical_url: https://docs.pingidentity.com/connectors/screen_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  setup: Setup
  resources: Resources
  configuring-the-screen-connector: Configuring the Screen connector
  using-the-connector-in-a-flow: Using the connector in a flow
  present-a-custom-view: Present a custom view
  capabilities: Capabilities
  createView: View
  createPolling: Client side polling with Message
---

# Screen Connector

The Screen connector lets you display forms and customized UI to retrieve information from a user or show flow progress in your PingOne DaVinci flow.

You can use the Screen connector to:

* Display a form for collecting user information.

* Present custom UI elements and views in one or more nodes of a flow.

## Setup

### Resources

Learn more in the following:

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Configuring the Screen connector

In PingOne DaVinci, add a Screen connector. Learn more in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html).

|   |                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------ |
|   | This connector doesn't have a configuration at the environment level. You configure it in your flow instead. |

## Using the connector in a flow

### Present a custom view

You can use the **View** capability to create a unique ID for a user. No special flow configuration is needed. Add the capability and populate its properties according to the help text.

## Capabilities

### View

Present a custom view

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - screen0Config
>
> * default object
>
>   * parameters object
>
> - output object
>
>   * screenComponentList object

### Client side polling with Message

> **Collapse: Show details**
>
> * Properties
>
> - screen0Config