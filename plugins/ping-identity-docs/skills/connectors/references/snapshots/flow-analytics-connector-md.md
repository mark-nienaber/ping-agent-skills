---
title: Flow Analytics Connector
description: The Flow Analytics connector lets you log details about flow outcomes that you can review in flow analytics.
component: connectors
page_id: connectors::flow_analytics_connector
canonical_url: https://docs.pingidentity.com/connectors/flow_analytics_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 30, 2026
section_ids:
  setup: Setup
  resources: Resources
  configuring-the-connector: Configuring the connector
  using-the-connector-in-a-flow: Using the connector in a flow
  capture-flow-information: Capture flow information
  using-global-variables-in-flow-analytics: Using global variables in flow analytics
  capabilities: Capabilities
  logOutcome: Log Flow Outcomes
---

# Flow Analytics Connector

The Flow Analytics connector lets you log details about flow outcomes that you can review in flow analytics.

You can use the Flow Analytics connector to:

* Track analytics based on different flow outcomes.

* Create a policy for running flows if logging errors occur.

## Setup

### Resources

Learn more in the following:

* DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Configuring the connector

Add the connector in DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

This connector doesn't have a configuration at the environment level. You configure it in your flow instead.

## Using the connector in a flow

### Capture flow information

You can use the **Log flow outcomes** capability to log details about flow outcomes based on outcome type and outcome status.

The following character limits apply to flow outcome fields. Content that exceeds a limit is automatically trimmed during flow execution.

* **Outcome Type**: Max 75 characters

* **Outcome Status**: Max 75 characters

* **Outcome Status Detail**: Max 75 characters

* **Outcome Description/Comment**: Max 2500 characters

### Using global variables in flow analytics

The following global variables are available for use in Flow Analytics connector fields:

| Variable                      | Description                           |
| ----------------------------- | ------------------------------------- |
| `{{global.flowName}}`         | The name of the current flow          |
| `{{global.flowVersionId}}`    | The version ID of the current flow    |
| `{{global.flowVersionAlias}}` | The version alias of the current flow |

You can map these variables into outcome fields like in the following example:

```json
{
  "outcomeType": "{{global.flowName}}",
  "outcomeStatus": "success",
  "outcomeStatusDetail": "{{global.flowVersionAlias}}"
}
```

## Capabilities

### Log Flow Outcomes

Log custom flow outcomes.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - - outcomeType dropDown required
>   - Custom Value textField
>
>   Enter a custom text or map any previous connector outcome
>
> - * outcomeStatus dropDown required
>   * Custom Value textField
>
>   Enter a custom text or map any previous connector outcome
>
> - * outcomeStatusDetail textField
>   * outcomeDescription textArea
>   * customTimestamp textField
>   * shouldContinueOnError toggleSwitch
>
> * default object
>
>   * properties object
>
>     * outcomeType string required minLength: 2 maxLength: 75
>
>       Type of outcome from flow (e.g. login, enrollment, etc.)
>
>     * outcomeStatus string required minLength: 2 maxLength: 75
>
>       Status of the outcome from the flow (e.g. success, error, denied, fraud, approved, etc.)
>
>     * outcomeStatusDetail string minLength: 2 maxLength: 250
>
>       Details about status of the outcome
>
>     * outcomeDescription string minLength: 2 maxLength: 2500
>
>       Description of the outcome
>
>     * customTimestamp string minLength: 2 maxLength: 75
>
>       Custom timestamp to be logged along with the outcome
>
>     * shouldContinueOnError boolean
>
>       true if flow should continue if an error is encountered in logging
>
> Input Example
>
> ```json
> {
>   "properties": {
>     "outcomeType": "login",
>     "outcomeStatus": "success"
>   }
> }
> ```