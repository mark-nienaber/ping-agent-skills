---
title: Akamai Account Protector Connector
description: Configure the Akamai Account Protector connector in PingOne DaVinci to evaluate Akamai user risk signals and branch your flow on the resulting risk level
component: connectors
page_id: connectors::akamai_account_protector_connector
canonical_url: https://docs.pingidentity.com/connectors/akamai_account_protector_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-03T00:00:00Z
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  configuring-the-akamai-account-protector-connector: Configuring the Akamai Account Protector connector
  connector-configuration: Connector configuration
  using-the-connector-in-a-flow: Using the connector in a flow
  evaluating-account-risk-during-sign-on: Evaluating account risk during sign-on
  capabilities: Capabilities
  evaluateRiskScore: Evaluate Akamai Risk Score
---

# Akamai Account Protector Connector

The Akamai Account Protector connector lets you evaluate [Akamai Account Protector](https://www.akamai.com/products/account-protector) risk signals in your PingOne DaVinci flow.

The connector parses the Akamai-User-Risk HTTP header, extracts the user risk score and related signals, and returns a risk level. Your flow can branch on that risk level to allow, challenge, or deny the request.

## Setup

### Resources

You can find more information and setup help in the following:

* Akamai documentation:

  * [Akamai Account Protector](https://www.akamai.com/products/account-protector)

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* An Akamai account with Account Protector enabled.

* Account Protector configured to include the Akamai-User-Risk header in requests.

* The Akamai-User-Risk header value passed into your flow.

### Configuring the Akamai Account Protector connector

Add the connector in PingOne DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

| Setting                     | Description                                                                                                                                                                                       |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Akamai User Risk Header** | The full value of the Akamai-User-Risk HTTP header, which contains the user risk score and related signals. You can supply this value from a flow variable or from the output of an earlier node. |
| **High Risk Threshold**     | The highest score treated as medium risk. Scores above this value are classified as high risk. The default is 50.                                                                                 |
| **Medium Risk Threshold**   | The highest score treated as low risk. Scores above this value, up to and including the **High Risk Threshold**, are classified as medium risk. The default is 25.                                |

## Using the connector in a flow

### Evaluating account risk during sign-on

The **Evaluate Akamai Risk Score** capability reads the Akamai risk signals for the current request and returns a risk level your flow can act on.

At a high level:

1. The capability parses the header value supplied in the **Akamai User Risk Header** field and extracts the score along with related signals, such as uuid, username, risk, trust, and action.

2. The capability compares the score against your configured thresholds and sets riskLevel to one of the following values:

   * LOW when the score is less than or equal to the **Medium Risk Threshold**.

   * MEDIUM when the score is greater than the **Medium Risk Threshold** and less than or equal to the **High Risk Threshold**.

   * HIGH when the score is greater than the **High Risk Threshold**.

3. Downstream nodes branch on riskLevel, such as allowing the request on LOW, requiring a step-up challenge on MEDIUM, and denying the request on HIGH.

If the header value does not contain a numeric score, the capability returns an error that your flow can handle on a separate branch.

Test the flow by clicking **Save**, **Deploy**, and **Try Flow**.

## Capabilities

### Evaluate Akamai Risk Score

Parses the Akamai-User-Risk HTTP header, extracts the user risk score and related signals, and returns a risk outcome based on configured thresholds.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Akamai User Risk Header textField required
>
>   HTTP header value that contains the Akamai User Risk score and related signals.
>
> - High Risk Threshold textField required
>
>   The maximum score for a high risk assessment. Scores above Medium and up to this value are categorized as High risk. Any score above this value are considered Critical risk.
>
> - Medium Risk Threshold textField required
>
>   The maximum score for a medium risk assessment. Scores above Low and up to this value are categorized as Medium risk.
>
> * default object
>
>   * properties object
>
>     * akamaiUserRiskHeader string
>
>       HTTP header value that contains the Akamai User Risk score and related signals.
>
>     * highValueThreshold number required
>
>       The maximum score for a high risk assessment
>
>     * mediumValueThreshold number required
>
>       The maximum score for a medium risk assessment
>
> Input Example
>
> ```json
> {
>   "properties": {
>     "highValueThreshold": "50",
>     "mediumValueThreshold": "25"
>   }
> }
> ```
>
> * output object
>
>   * riskLevel string
>
>   * uuid string
>
>   * username string
>
>   * emailDomain string
>
>   * ouid string
>
>   * requestid string
>
>   * status number
>
>   * score number
>
>   * general string
>
>   * risk string
>
>   * trust string
>
>   * allow string
>
>   * action string