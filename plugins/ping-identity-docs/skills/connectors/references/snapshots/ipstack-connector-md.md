---
title: IPStack Connector
description: Configure the IPStack connector in PingOne DaVinci to look up IP address geolocation data and return location, currency, timezone, connection, and security data to your flow
component: connectors
page_id: connectors::ipstack_connector
canonical_url: https://docs.pingidentity.com/connectors/ipstack_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-08T00:00:00Z
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  configuring-the-ipstack-connector: Configuring the IPStack connector
  connector-configuration: Connector configuration
  using-the-connector-in-a-flow: Using the connector in a flow
  locating-an-ip-address: Locating an IP address
  capabilities: Capabilities
  standardLookup: Standard Lookup.
---

# IPStack Connector

The IPStack connector lets you look up the location of an IP address with [IPStack](https://ipstack.com/) in your PingOne DaVinci flow.

The connector returns location, currency, timezone, connection, and security data for the IP address that you can use in your flow.

## Setup

### Resources

You can find more information and setup help in the following:

* IPStack documentation:

  * [IPStack API documentation](https://docs.apilayer.com/ipstack/docs/api-documentation)

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* An IPStack API key.

### Configuring the IPStack connector

Add the connector in PingOne DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

| Setting                            | Description                                                                                                                                                                                                           |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| API key                            | The IPStack API key to use the service. You can get one from the [IPStack sign-up page](https://ipstack.com/product).                                                                                                 |
| Allow Insecure ipstack Connection? | (Optional) Allows connections to IPStack over HTTP instead of HTTPS. The IPStack subscription plan does not support HTTPS connections. Learn more in the [IPStack pricing information](https://ipstack.com/pricing/). |

## Using the connector in a flow

### Locating an IP address

The **Standard Lookup.** capability looks up geolocation data for a single IPv4 or IPv6 address.

At a high level:

1. The **Standard Lookup.** capability sends a lookup request to IPStack for the IP address you specify in the node. If you leave the field empty, the node looks up the IP address from the flow request.

2. The connector outputs the geolocation data, such as country, region, city, ZIP code, latitude, and longitude, that you can evaluate in your flow.

|   |                                                        |
| - | ------------------------------------------------------ |
|   | The connector currently supports standard lookup only. |

Test the flow by clicking **Save**, **Deploy**, and **Try Flow**.

## Capabilities

### Standard Lookup.

The ipstack's primary endpoint is called Standard Lookup and is used to look up single IPv4 or IPv6 addresses.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - IP Address textField
>
>   The IP address for which geolocation data should be obtained.
>
> * default object
>
>   * properties object
>
>     * ip string
>
>       The IP address. Ignore to use global.ip by default.
>
> - output object
>
>   * rawResponse object
>
>   * statusCode number
>
>   * headers object
>
>   * ip string
>
>   * type string
>
>   * continent_code string
>
>   * continent_name string
>
>   * country_code string
>
>   * country_name string
>
>   * region_code string
>
>   * region_name string
>
>   * city string
>
>   * zip string
>
>   * latitude number
>
>   * longitude number
>
>   * location object