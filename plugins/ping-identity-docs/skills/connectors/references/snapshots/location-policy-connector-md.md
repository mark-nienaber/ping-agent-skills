---
title: Location Policy Connector
description: The Location Policy connector lets you check a user's IP and geographic location in your PingOne DaVinci flow.
component: connectors
page_id: connectors::location_policy_connector
canonical_url: https://docs.pingidentity.com/connectors/location_policy_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 19, 2024
section_ids:
  setup: Setup
  resources: Resources
  configuring-the-location-policy-connector: Configuring the Location Policy connector
  using-the-connector-in-a-flow: Using the connector in a flow
  allow-requests-from-specified-locales: Allow requests from specified locales
  deny-requests-from-specified-locales: Deny requests from specified locales
  capabilities: Capabilities
  allow-by-cidr-block-or-ip-range: Allow by CIDR Block or IP Range
  deny-by-cidr-block-or-ip-range: Deny by CIDR Block or IP Range
  allow-by-location-name: Allow by Location Name
  deny-by-location-name: Deny by Location Name
---

# Location Policy Connector

The Location Policy connector lets you check a user's IP and geographic location in your PingOne DaVinci flow.

You can use the Location Policy connector to:

* Implement risk intelligence by creating a location policy.

* Allow or deny requests from specified locales

## Setup

### Resources

Learn more in the following:

* DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Configuring the Location Policy connector

In DaVinci, add a Location Policy connector. Learn more in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html).

This connector doesn't have a configuration at the environment level. You configure it in your flow instead.

## Using the connector in a flow

### Allow requests from specified locales

The connector has several capabilities that allow you to allow requests from specified locales:

* **Allow by CIDR Block or IP Range**

* **Allow by Location Name**

No special configuration is needed. Add the capability and populate its properties according to the help text.

### Deny requests from specified locales

The connector has several capabilities that allow you to deny requests from specified locales:

* **Deny by CIDR Block or IP Range**

* **Deny by Location Name**

No special configuration is needed. Add the capability and populate its properties according to the help text.

## Capabilities

### Allow by CIDR Block or IP Range

Allow transactions based on CIDR blocks or IP ranges.

> **Collapse: Show details**
>
> * * Properties
>   * IP Addresses `textArea`
>
>   The list of CIDR blocks or IP addresses to allow, such as "131.10.55.1/24". Separate multiple IP addresses with commas.
>
> - - Input Schema
>   - default `object`
>   - ipAddressList `string`
>   - Output Schema
>   - output `object`
>   - ipAddressList `array`

### Deny by CIDR Block or IP Range

Deny transactions based on CIDR blocks or IP ranges.

> **Collapse: Show details**
>
> * * Properties
>   * IP Addresses `textArea`
>
>   The list of CIDR blocks or IP addresses to allow, such as "131.10.55.1/24". Separate multiple IP addresses with commas.
>
> - - Input Schema
>   - default `object`
>   - ipAddressList `string`
>   - Output Schema
>   - output `object`
>   - ipAddressList `array`

### Allow by Location Name

Allow transactions that originate from named locations.

> **Collapse: Show details**
>
> * * Properties
>   * Locations `textArea`
>
>   The list of geographies, regions, countries, or cities to allow. Separate multiple regions with a comma.
>
> - - Input Schema
>   - default `object`
>   - regions `string`
>   - Output Schema
>   - output `object`
>   - regions `array`

### Deny by Location Name

Deny transactions that originate from named locations.

> **Collapse: Show details**
>
> * * Properties
>   * Locations `textArea`
>
>   The list of geographies, regions, countries, or cities to allow. Separate multiple regions with a comma.
>
> - - Input Schema
>   - default `object`
>   - regions `string`
>   - Output Schema
>   - output `object`
>   - regions `array`