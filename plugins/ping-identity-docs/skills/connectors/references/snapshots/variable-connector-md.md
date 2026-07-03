---
title: Variable Connector
description: The Variable connector lets you store and retrieve flow and user attributes as variables in your PingOne DaVinci flow.
component: connectors
page_id: connectors::variable_connector
canonical_url: https://docs.pingidentity.com/connectors/variable_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 19, 2024
section_ids:
  setup: Setup
  resources: Resources
  configuring-the-variable-connector: Configuring the Variable connector
  using-the-connector-in-a-flow: Using the connector in a flow
  flow-instance-variable: Flow Instance Variable
  flow-variable: Flow Variable
  user-variable: User Variable
  capabilities: Capabilities
  saveValue: Flow Instance Variable
  saveFlowValue: Flow Variable
  incrementByN: "Flow Instance variable: Increment by N"
  saveValueUserInfo: User Variable
  incrementByNUserInfo: "User variable: Increment by N"
  setLanguage: Set Language
---

# Variable Connector

The Variable connector lets you store and retrieve flow and user attributes as variables in your PingOne DaVinci flow.

## Setup

### Resources

Learn more in the following:

* DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Configuring the Variable connector

In DaVinci, add a Variable connector. Learn more in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html).

|   |                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------ |
|   | This connector doesn't have a configuration at the environment level. You configure it in your flow instead. |

## Using the connector in a flow

Variables are values that can be read and modified during a flow. In DaVinci, variables allow users to track and adjust values within flows. They can be read and modified during a flow. Variables can be strings, Boolean values, numbers, or objects.

In a flow, variables can be used to track information and a variable's value can be used to determine which nodes are run within the flow. Every variable has a context, which determines how widely its value is shared. There are three types of variables:

### Flow Instance Variable

Persists only for a single execution of a flow. This is useful for storing things temporarily for an execution, such as if you want to store a particular value from one node to use it later in the flow.

### Flow Variable

Persists across multiple executions of that flow. This is useful for storing common things that are shared across multiple executions of the same flow.

### User Variable

A shadow user must be available in order to use this variable. This capability adds a value to the user's details or `userInfo` in DaVinci.

The DaVinci Variable connector has several capabilities that allow you to manage flows, flow instances, and user variables used across flows and instances.

## Capabilities

### Flow Instance Variable

Add and update flow instance variable

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - saveVariables selectNameValueListColumn
>
> * default object
>
>   * properties object
>
> - output object::

### Flow Variable

Add and update flow variable

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - saveFlowVariables selectNameValueListColumn
>
> * default object
>
>   * properties object
>
> - output object::

### Flow Instance variable: Increment by N

Flow instance variables are local to the specific instance of a flow.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - - Local Variable Name textField
>   - incrementCounter textField
>
> * default object
>
>   * variables object
>
>   * properties object
>
>     * variable
>
>     * incrementCounter
>
> - output object
>
>   * newValue number
>
> Output Example
>
> ```json
> {
>   "newValue": 4
> }
> ```

### User Variable

Add and update user variables used across flows and flow instances.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - saveVariables selectNameValueListColumn
>
> * default object
>
>   * userInfo object required
>
>     User Information record to which the variable is saved.
>
>   * properties object
>
> - output object::

### User variable: Increment by N

If the user is known, variables can contain user context across flows and flow instances.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - - Local Variable Name textField
>   - incrementCounter textField
>
> * default object
>
>   * userInfo object required
>
>     User Information record to which the variable is saved.
>
>   * properties object
>
>     * variable
>
>     * incrementCounter
>
> - output object
>
>   * newValue number
>
> Output Example
>
> ```json
> {
>   "newValue": 4
> }
> ```

### Set Language

Set the language to be used for localized content.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Locale textField required
>
>   The language to be used for localized content. This should be a valid locale code, such as "en-US" or "fr-FR".
>
> * default object
>
>   * properties object
>
>     * locale string required
>
> - language string
