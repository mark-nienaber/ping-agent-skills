---
title: PingOne RADIUS Gateway Connector
description: The PingOne RADIUS Gateway connector enables you to integrate PingOne DaVinci flows with a PingOne RADIUS Gateway.
component: connectors
page_id: connectors::p1_radius_gateway_connector
canonical_url: https://docs.pingidentity.com/connectors/p1_radius_gateway_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 19, 2024
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  setting-up-the-connector: Setting up the connector
  using-the-connector-in-a-flow: Using the connector in a flow
  radius-gateway-flow-templates: RADIUS gateway flow templates
  capabilities: Capabilities
  radiusResponse: Radius Response
---

# PingOne RADIUS Gateway Connector

The PingOne RADIUS Gateway connector enables you to integrate PingOne DaVinci flows with a PingOne RADIUS Gateway.

## Setup

### Resources

Learn more in the following:

* PingOne documentation:

  * [Getting started with PingOne](https://docs.pingidentity.com/pingone/getting_started_with_pingone/p1_getting_started.html)

  * [PingOne Gateways documentation](https://docs.pingidentity.com/pingone/integrations/p1_radius_gateways_intro.html)

* DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* A PingOne license.

* A PingOne environment.

* A RADIUS gateway. Learn how to create and configure a RADIUS gateway in [RADIUS Gateways](https://docs.pingidentity.com/pingone/integrations/p1_radius_gateways_intro.html).

### Setting up the connector

In DaVinci, go to **Connections** and add a PingOne RADIUS gateway connector. Learn more in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html).

## Using the connector in a flow

Use the RADIUS Gateway connector to instruct DaVinci to respond to a RADIUS Gateway authentication session request. The connector can send one of the following responses:

* **Accept**: Indicates that a user has completed all the required authentication steps. The RADIUS gateway sends an `ACCESS_ACCEPT` response to the RADIUS client, and grants the user access.

  |   |                                                                                                                                                 |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | You can send user RADIUS attributes back to the RADIUS client, and the connector also provides the option to define vendor-specific attributes. |

* **Reject**: Indicates that a user failed a required authentication step. The RADIUS gateway sends an `ACCESS_REJECT` response to the RADIUS client, and rejects the user's authentication request.

* **Challenge**: Instructs the gateway to send a challenge to the authenticating user by sending an \`ACCESS\_CHALLENGE\`response to the RADIUS client.

  |   |                                                                                                            |
  | - | ---------------------------------------------------------------------------------------------------------- |
  |   | This response type is only supported when using a RADIUS client that supports `ACCESS_CHALLENGE` requests. |

* **Poll**: Indicates that the user is authenticating with the PingID mobile app, and the DaVinci flow is waiting for a push response.

### RADIUS gateway flow templates

PingOne provides out-of-the-box DaVinci flows that you can integrate into your RADIUS gateway.

|   |                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------- |
|   | To use a RADIUS gateway flow template, you first need to add thePingID connector and the PingOne RADIUS Gateway connector. |

The following RADIUS gateway flows are available:

* [RADIUS Gateway Authentication](https://marketplace.pingone.com/item/radius-gateway-authentication) flow: This flow can be used to authenticate users when accessing RADIUS clients that support the RADIUS PAP protocol. You can customize the following options:

  * OTP Fallback: If the PingID server can't reach the device or the push response can't be completed, allow users to authenticate with a one-time passcode instead.

  * Newline Character: Select a line separation character to use for RADIUS server challenge messages.

  * RADIUS response attribute.

To download this flow, search for [RADIUS gateway Authentication](https://marketplace.pingone.com/item/radius-gateway-authentication) flow in [Ping Identity Marketplace](https://marketplace.pingone.com/home).

* [RADIUS Gateway - Registration and Authentication](https://marketplace.pingone.com/item/radius-gateway-registration-and-authentication) flow: This flow can be used to register and authenticate users when accessing RADIUS clients that support Challenge mode. Customization options are the same as those in the RADIUS Gateway - authentication flow.

* [RADIUS Gateway - No Challenge Authentication](https://marketplace.pingone.com/item/radius-gateway-no-challenge-authentication) flow: This flow can be used when accessing RADIUS clients that support the RADIUS PAP protocol to authenticate users with VPN clients that do not support Challenge mode. You can customize the Custom Separator to enable users to enter the OTP with their password. If you define a specific custom separator:

  * When a user wants to authenticate using PingID mobile app they only need to add the custom separator after their password and then the word push.

  * When using other OTP-based authentication methods (such as PingID Desktop app or a YubiKey), the user should add a custom separator after their password and then the OTP. For example `password,123456`.

  * If the user is registered with multiple devices supported by this mode, an OTP generated by any one of those devices authenticates the user.

  * This flow does not support on-the-fly registration.

    |   |                                                                                                                                               |
    | - | --------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | If a custom separator is not defined the user can enter their password followed by the OTP, without a separator. For example `<password>OTP`. |

* [RADIUS Gateway - Advanced Protocols Authentication](https://marketplace.pingone.com/item/radius-gateway-advanced-protocols-authentication) flow: This flow can be used when accessing RADIUS clients that support advanced protocols (such as MS-CHAPv2) to authenticate users. A comma is defined as the Custom Separator by default to enable users to enter the OTP with their username. The custom separator must be the same as that defined in your NPS, and you can customize it in the **Flow settings** node, if required. The custom separator enables the following user experience:

  * When a user wants to authenticate using PingID mobile app they only need to add the custom separator after their username and then the word push.

  * When using other OTP-based authentication methods (such as PingID Desktop app or a YubiKey), the user should add a custom separator after their username and then the OTP. For example `John,123456`.

  * If the user is registered with multiple devices supported by this mode, an OTP generated by any one of those devices authenticates the user.

  * This flow does not support on-the-fly registration.

    To customize the RADIUS Gateway authentication flow template:

    1. In the [Ping Identity Marketplace](https://marketplace.pingone.com/home) search for RADIUS gateway authentication flow and import the flow. Learn more in [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html).

       ![RADIUS gateway authentication flow showing the flow settings node](_images/connector-images/dvc-p1-radius-gateway-flow-settings-node.png)

    2. To configure an OTP Fallback, select the**Flow settings** node and modify the `OTP_FALLBACK`variable. Possible values: `True` or `False`.

    3. To define a Newline Character, select the**Flow settings** node and modify the `NEWLINE_CHARACTER` variable. Choose from:

       * None: (leave the field empty if you do not want to define a newline character).

       * `\n`: Unix style.

       * `\r\n`: Windows style.

       * `<br>`: HTML

    4. To add a RADIUS response attribute `` : Select the Authentication Approved node` ``, click **Add**, and define the attribute properties.

       ![RADIUS gateway authentication flow showing the Authentication Approved node](_images/connector-images/dvc-p1-radius-gateway-authentication-approved-node.png)

## Capabilities

### Radius Response

The returned message sent to the RADIUS client.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Response Type dropDown
>
>   The type of returned message sent to the RADIUS client. Valid response types are CHALLENGE, POLL, ACCEPT, or REJECT.
>
>   * CHALLENGE
>
>   * POLL
>
>   * ACCEPT
>
>   * REJECT
>
> - Response Value textField
>
>   The text that displays in the Reply-Message, which is sent to the RADIUS client and visible to the user, limited to 253 characters.
>
> - * Use the following fields to map values from your flow to RADIUS attributes. label
>   * Attribute Mapping attributesRulesList
>
> * default object
>
>   * properties object
>
>     * responseType string required
>
>     * responseValue string
>
>     * description string
>
>     * attributeMapping array
>
> - output object
>
>   * text string
