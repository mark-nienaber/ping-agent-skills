---
title: Challenge Connector
description: Configure the Challenge connector to branch PingOne DaVinci flows and handle external events like MFA challenges using status-based polling
component: connectors
page_id: connectors::challenge_connector
canonical_url: https://docs.pingidentity.com/connectors/challenge_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  setup: Setup
  setting-up-the-challenge-connector: Setting up the Challenge connector
  using-the-connector-in-a-flow: Using the connector in a flow
  building-an-mfa-sign-on-flow: Building an MFA sign-on flow
  capabilities: Capabilities
  createChallenge: Add Transaction Status
  updateChallenge: Update Transaction Status
  getChallenge: Get Transaction Status
  pollChallenge: Poll for Transaction Status
---

# Challenge Connector

The Challenge connector allows you to branch your PingOne DaVinci flow to handle an external event, such as a multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)* step.

By using the Challenge connector, you can show the user a message and "waiting" indicator in the main flow while a secondary flow interacts with the user elsewhere. When the secondary flow is done, the Challenge connector can trigger the main flow to continue.

The connector works by creating, updating, or checking the status of a "challenge" in your flow. Challenges are special variables that can be created by several connectors, including the Challenge connector, [Flow Conductor Connector](flow_conductor_connector.html), and some authentication and verification connectors.

Other connectors, such as the [HTTP Connector](http_connector.html), can pause the flow until the status of a challenge changes.

The Challenge connector updates the status of a challenge, which triggers the waiting HTTP connector to continue the flow.

![A screen capture that shows an overview of how the Challenge connector branches a flow.](_images/connector-images/dvc-challenge-flow-branches.jpg)

## Setup

### Setting up the Challenge connector

In PingOne DaVinci, add a **Challenge** connection. Learn more in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html).

This connector doesn't have a configuration at the environment level. You configure it in your flow instead.

## Using the connector in a flow

The Challenge connector supports a variety of use cases, such as:

### Building an MFA sign-on flow

In this example, we want our user to complete an MFA challenge after entering their username and password. We'll show an HTML message in the browser telling the user to complete MFA. At the same time, we'll start the MFA connector in a secondary flow, which pushes a notification to the user's phone. When the user completes MFA on their phone, our secondary flow triggers the HTML message to continue the main flow.

Before you start, you'll need:

* A sign-on form. You can create one with the [HTTP](http_connector.html) connector.

* An MFA connector, such as the [PingOne MFA](p1_mfa_connector.html) connector.

  1. Create the challenge:

     1. In your flow, following the sign-on form, add the **Challenge** connector and select the **Add Transaction Status** capability. Select the new node in your flow.

     2. Turn off **Is challenge record complete**.

     3. In the **Challenge Status** list, select **started**.

  2. Show a page with a "waiting" animation until the user clicks the link:

     1. Following your **Add Transaction Status** node, add an [HTTP](http_connector.html) connector and select the **Custom HTML Message** capability. Select the new node in your flow.

     2. Build your message in the **HTML Template** field. To show a "waiting" animation on the page, click **{}** and select the `skpolling` variable from SK-Component.

        ![A screen capture that shows the user inserting the skpolling variable into the Message field.](_images/connector-images/dvc-challenge-connector-skpolling-variable.gif)

     3. In the **Challenge** field, click **{}** and select the `challenge` variable from your **Add Transaction Status** node. Turn on **Enable Polling**.

        This pauses the main flow on this page until the challenge status changes. We'll update the challenge status in the secondary flow.

        |   |                                                                                                |
        | - | ---------------------------------------------------------------------------------------------- |
        |   | Any change in the challenge status, regardless of the value, will cause this flow to continue. |

  3. Build a secondary flow that sends the MFA push and updates the challenge status:

     1. Following your Add **Transaction Status** node, parallel to your **Custom HTML Template** node, add an MFA node. In our example, we use the [PingOne MFA](p1_mfa_connector.html) connector. You can use your MFA service of choice or link to a subflow using the [Flow conductor](flow_conductor_connector.html) connector.

     2. Configure your MFA node by following its documentation. If you are using the **PingOne MFA** connector, refer to [PingOne MFA](p1_mfa_connector.html).

     3. Following your MFA node, add a **Challenge** connector and select the **Update Transaction Status** capability.

     4. In the **Challenge** field, click **{}** and select the `challenge` variable from your **Add Transaction Status** node.

     5. Turn on **Is challenge record complete**. This indicates to PingOne DaVinci that our **Custom HTML Template** can stop polling for the status of this challenge.

     6. In the **Challenge Status** list, select **approved**.

  4. Following your **Custom HTML Template** "waiting" page in the main flow, continue building the rest of your flow. For example, you could direct the user to their user account self-service portal.

## Capabilities

### Add Transaction Status

Add the transaction status challenge to the flow.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - - isChallengeComplete toggleSwitch
>   - challengeStatus dropdownWithCreate
>
>   started:
>
>   This status signifies that the challenge has been created and can be polled until the status changes or times out
>
>   approved:
>
>   This status signifies that the challenge has been approved and should be treated as a success event
>
>   denied:
>
>   This status signifies that the challenge has been denied. This status will still be treated as a success event and the flow is expected to move forward to the true path. Flow can then decide what next to do with the denied status
>
> - * Challenge Timeout in seconds (default 300secs) textField
>   * updatedByFlowId textField
>   * claimsNameValuePairs selectNameValueListColumn
>
> * default object
>
>   * parameters object
>
>     * challengeStatus string
>
>     * updatedByFlowId string
>
> - output object
>
>   * challenge string
>
>   * challengeStatus string
>
>   * updateByFlowId string
>
> Output Example
>
> ```json
> {
>   "challenge": "IXaa0MwwUFtrI4AJedpr4ha40wZmEeOisisRPFlnA0c",
>   "challengeStatus": "started",
>   "updateByFlowId": "MwwUFtrI4AJedpr4ha40wZmEeO"
> }
> ```

### Update Transaction Status

Update the transaction status challenge in the flow.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - - Challenge textField
>   - isChallengeComplete toggleSwitch
>   - challengeStatus dropdownWithCreate
>
>   started:
>
>   This status signifies that the challenge has been created and can be polled until the status changes or times out
>
>   approved:
>
>   This status signifies that the challenge has been approved and should be treated as a success event
>
>   denied:
>
>   This status signifies that the challenge has been denied. This status will still be treated as a success event and the flow is expected to move forward to the true path. Flow can then decide what next to do with the denied status
>
> - * updatedByFlowId textField
>   * claimsNameValuePairs selectNameValueListColumn
>
> * default object
>
>   * parameters object
>
>     * challenge string minLength: 1 maxLength: 100
>
>       Unique string to identify the Transaction
>
>     * challengeStatus string minLength: 1 maxLength: 50
>
>       Current status of the Transaction
>
>     * updatedByFlowId string minLength: 1 maxLength: 100
>
>       Id of the flow updating the challenge
>
> - output object
>
>   * challenge string
>
>   * challengeStatus string
>
>   * updateByFlowId string
>
> Output Example
>
> ```json
> {
>   "challenge": "IXaa0MwwUFtrI4AJedpr4ha40wZmEeOisisRPFlnA0c",
>   "challengeStatus": "approved",
>   "updateByFlowId": "MwwUFtrI4AJedpr4ha40wZmEeO"
> }
> ```

### Get Transaction Status

Retrieve transaction status information in the flow.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Challenge textField
>
> * default object
>
>   * parameters object
>
>     * challenge string minLength: 1 maxLength: 100
>
>       Unique string to identify the Transaction
>
> - output object
>
>   * challenge string
>
>   * challengeStatus string
>
>   * updateByFlowId string
>
> Output Example
>
> ```json
> {
>   "challenge": "IXaa0MwwUFtrI4AJedpr4ha40wZmEeOisisRPFlnA0c",
>   "challengeStatus": "approved",
>   "updateByFlowId": "MwwUFtrI4AJedpr4ha40wZmEeO",
>   "createdDate": 16353453453,
>   "statusUpdatedDate": 16353453453
> }
> ```

### Poll for Transaction Status

Poll for transaction status information in the flow.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - - Challenge textField
>   - pollInterval textField
>   - pollRetries textField
>
> * default object
>
>   * parameters object
>
>     * challenge string minLength: 1 maxLength: 100
>
>       Unique string to identify the Transaction
>
>     * pollInterval number
>
>       Poll Interval in ms
>
>     * pollRetries number
>
>       Number of Poll Retries
>
> - output object
>
>   * challenge string
>
>   * challengeStatus string
>
>   * updateByFlowId string
>
> Output Example
>
> ```json
> {
>   "challenge": "IXaa0MwwUFtrI4AJedpr4ha40wZmEeOisisRPFlnA0c",
>   "challengeStatus": "approved",
>   "updateByFlowId": "MwwUFtrI4AJedpr4ha40wZmEeO"
> }
> ```