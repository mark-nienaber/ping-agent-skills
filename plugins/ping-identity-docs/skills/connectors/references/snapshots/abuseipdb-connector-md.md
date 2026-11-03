---
title: AbuseIPDB Connector
description: Configure the AbuseIPDB connector in PingOne DaVinci to check whether an IP address has been associated with malicious activity and branch on the abuse confidence score
component: connectors
page_id: connectors::abuseipdb_connector
canonical_url: https://docs.pingidentity.com/connectors/abuseipdb_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-08T00:00:00Z
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  configuring-the-abuseipdb-connector: Configuring the AbuseIPDB connector
  connector-configuration: Connector configuration
  using-the-connector-in-a-flow: Using the connector in a flow
  checking-an-ip-address-for-malicious-activity: Checking an IP address for malicious activity
  capabilities: Capabilities
  getSingleIp: Returns a dataset around a single IP such as if the IP Address is public, allow listed, an Abuse Confidence Score, and more.
---

# AbuseIPDB Connector

The AbuseIPDB connector lets you check whether an IP address has been associated with malicious activity using [AbuseIPDB](https://www.abuseipdb.com/) in your PingOne DaVinci flow.

The connector takes an IP address as an input value and runs it against the AbuseIPDB API to determine whether it's from a bad actor. It outputs the abuse confidence score and related data points, such as whether the IP address is public, allow listed, or has been reported, that you can use to make decisions in your flow.

## Setup

### Resources

You can find more information and setup help in the following:

* AbuseIPDB documentation:

  * [AbuseIPDB API documentation](https://docs.abuseipdb.com/)

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* An AbuseIPDB tenant to gather an API key.

### Configuring the AbuseIPDB connector

Add the connector in PingOne DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

| Setting | Description                                                       |
| ------- | ----------------------------------------------------------------- |
| API Key | Your API key from the **API** tab of your AbuseIPDB account page. |

## Using the connector in a flow

### Checking an IP address for malicious activity

The capability returns a dataset around a single IP address, such as whether the IP address is public, allow listed, its abuse confidence score, and more.

At a high level:

1. The node sends a check request to AbuseIPDB for the IP address and maximum lookback period, in days, you specify in the node.

2. The connector outputs the abuse confidence score and related data points, such as whether the IP address is public, allow listed, or has been reported, that you can use to branch your flow.

|   |                                                       |
| - | ----------------------------------------------------- |
|   | The connector verifies a single IP address at a time. |

Test the flow by clicking **Save**, **Deploy**, and **Try Flow**.

## Capabilities

### Returns a dataset around a single IP such as if the IP Address is public, allow listed, an Abuse Confidence Score, and more.

Returns datapoints around a single IP Address

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Max Days textField
>
>   Maximum amount of days to look back to
>
> - IP Address textField
>
>   IP Address
>
> * default object
>
>   * properties object
>
>     * maxDays string required
>
>       Maximum amount of days to look back to
>
>     * ipAddress string required
>
>       IP Address of end user
>
> Input Example
>
> ```json
> {
>   "properties": {
>     "maxDays": "90",
>     "ipAddress": "118.25.6.39"
>   }
> }
> ```
>
> * output object
>
>   * rawResponse object
>
>   * statusCode number
>
>   * headers object
>
>   * ipAddress number
>
>   * isPublic object
>
>   * ipVersion number
>
>   * isWhitelisted object
>
>   * abuseConfidenceScore number
>
>   * countryCode object
>
>   * usageType object
>
>   * isp object
>
>   * domain object
>
>   * countryName object
>
>   * totalReports number
>
>   * numDistinctUsers number
>
>   * lastReportedAt object