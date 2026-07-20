---
title: Teleport Connector
description: Configure the Teleport connector to visually organize and subdivide flows on the PingOne DaVinci flow canvas
component: connectors
page_id: connectors::teleport_connector
canonical_url: https://docs.pingidentity.com/connectors/teleport_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  setup: Setup
  resources: Resources
  configuring-the-teleport-connector: Configuring the Teleport connector
  using-the-connector-in-a-flow: Using the connector in a flow
  manage-large-flows: Manage large flows
  manage-looping-flows: Manage looping flows
  capabilities: Capabilities
  startNode: Define a Start Node
  goToNode: Go to Start Node
  returnBackToCallingNode: Return to Calling Node
---

# Teleport Connector

The Teleport connector lets you visually organize and subdivide a flow within your PingOne DaVinci flow canvas.

|   |                                                                                         |
| - | --------------------------------------------------------------------------------------- |
|   | Teleport nodes are only meant to function within a single flow and not across subflows. |

## Setup

### Resources

Learn more in the following:

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Configuring the Teleport connector

In PingOne DaVinci, add a Teleport connector. Learn more in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html).

|   |                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------ |
|   | This connector doesn't have a configuration at the environment level. You configure it in your flow instead. |

## Using the connector in a flow

### Manage large flows

Use Teleport nodes to connect different sections of the flow. This makes the flow more readable by breaking it down into discrete sections. It also lets you reuse some sections of the flow rather than duplicating content.

### Manage looping flows

When flows loop, the canvas can become cluttered. Avoid this by defining a start node at the point where the loop returns, then using the Teleport connector to go to that start node to execute the loop.

No special configuration is needed. Add the capability and populate its properties according to the help text.

## Capabilities

### Define a Start Node

Define the node where the flow will start.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> - inputSchema codeEditor
>
>   Follow example for JSON schema.
>
>   Default:
>
>   ```none
>   {
>   "type": "object",
>   "properties": {
>   "success": {
>   "type": "boolean",
>   "displayName": "success",
>   "preferredControlType": "textField",
>   "enableParameters": true,
>   "propertyName": "success"
>   }
>   }
>   }
>   ```
>
> * default object

### Go to Start Node

Go to a specific start node defined in the flow.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> - nodeInstanceId dropDown
>
>   Teleport to this node. Give your nodes a name in case there are duplicate names in the list.
>
> * default object

### Return to Calling Node

Return to the node where the flow starts.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> - outputSchema codeEditor
>
>   Follow example for JSON schema.
>
>   Default:
>
>   ```none
>   {
>   "type": "object",
>   "properties": {
>   "success": {
>   "type": "boolean",
>   "displayName": "success",
>   "preferredControlType": "textField",
>   "enableParameters": true,
>   "propertyName": "success"
>   }
>   }
>   }
>   ```
>
> * default object