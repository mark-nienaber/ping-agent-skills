---
title: Splunk Connector
description: Configure the Splunk connector in PingOne DaVinci to post events to Splunk and gain real-time operational intelligence in your flows
component: connectors
page_id: connectors::splunk_connector
canonical_url: https://docs.pingidentity.com/connectors/splunk_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  setting-up-splunk: Setting up Splunk
  configuring-the-splunk-connector: Configuring the Splunk connector
  connector-configuration: Connector configuration
  base-url: Base URL
  port: Port
  token: Token
  using-the-connector-in-a-flow: Using the connector in a flow
  post-a-splunk-event: Post a Splunk event
  capabilities: Capabilities
  postEvent: Post Splunk Event
---

# Splunk Connector

The Splunk connector lets you gain real-time operational intelligence through Splunk in your PingOne DaVinci flow.

## Setup

### Resources

You can find more information and setup help in:

* Splunk:

  * [Splunk Cloud Platform Documentation](https://help.splunk.com/en/splunk-cloud-platform)

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* A Splunk license

* Your Splunk credentials

### Setting up Splunk

To set up Splunk, create an HTTP event collector token:

1. Click on Settings > Data > Data Inputs.

2. Click **HTTP Event Collector** or click Actions > Add new button.

3. Click **Global Settings** and use the following configuration:

   1. Enable the **All Tokens** field.

   2. Set the **Default Source Type** to **\_json**.

   3. Set the **Default Index** to **Main**.

      ![dvc splunk edit global](_images/connector-images/dvc-splunk-edit-global.png)

   4. Click **Save**.

4. Provide the **Token Name**, then click **Next**.

5. Select **Source Type** as **Automatic** and **Selected Allowed Indexes**. Click **Review**.

6. Click **Submit**.

   ![dvc splunk add data](_images/connector-images/dvc-splunk-add-data.png)

7. Copy the generated token.

### Configuring the Splunk connector

Add the connector in PingOne DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

##### Base URL

The **Base URL** you received by email from setting up Splunk.

##### Port

Enter `8088`.

##### Token

Paste the **Token** created when setting up Splunk.

## Using the connector in a flow

### Post a Splunk event

You can use the **Post Splunk Event** capability to post a Splunk event:

1. Add the connector to the flow and configure the fields based on the configuration selected when creating a token.

2. Select the **Event (String)** or **Event (JSON)** to post.

3. Click **Apply**.

## Capabilities

### Post Splunk Event

Create a new Splunk event.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Time textField
>
>   The event time in the format {sec}.{ms}.
>
> - Host textField
>
>   The host value to assign to the event data.
>
> - Source textField
>
>   The source value to assign to the event data.
>
> - Source Type textField
>
>   The sourcetype value to assign to the event data.
>
> - Index textField
>
>   The name of the index by which the event data is to be indexed.
>
> - Event (String) textField
>
>   Event in raw text.
>
> - Event (JSON) codeEditor
>
>   Event in raw JSON.
>
> - Fields keyValueList
>
>   Metadata in Key-Value format.
>
> * default object
>
>   * properties object
>
>     * apiUrl string required
>
>     * token string required
>
>     * time string
>
>     * host string required
>
>     * source string required
>
>     * sourcetype string required
>
>     * index string required
>
>     * event string
>
> - output object
>
>   * rawResponse object
>
>     * code number
>
>     * text string
>
> Output Example
>
> ```json
> {
>   "rawResponse": {
>     "code": 0,
>     "text": "Success"
>   }
> }
> ```