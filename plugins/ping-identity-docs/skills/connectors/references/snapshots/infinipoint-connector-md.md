---
title: Infinipoint Connector
description: Configure the Infinipoint connector in PingOne DaVinci to authenticate users with Infinipoint Device-Identity-as-a-Service and verify device trust during login
component: connectors
page_id: connectors::infinipoint_connector
canonical_url: https://docs.pingidentity.com/connectors/infinipoint_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-07-30T00:00:00Z
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  configuring-the-infinipoint-connector: Configuring the Infinipoint connector
  connector-configuration: Connector configuration
  using-the-connector-in-a-flow: Using the connector in a flow
  logging-in-with-infinipoint: Logging in with Infinipoint
  capabilities: Capabilities
  loginFirstFactor: Redirect to Infinipoint
---

# Infinipoint Connector

The Infinipoint connector lets you authenticate users with Infinipoint Device-Identity-as-a-Service (DIaaS) in your PingOne DaVinci flow.

The connector performs an OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
\</div>)* redirect to Infinipoint, which verifies the user's identity along with the posture of their device. Infinipoint then redirects back to PingOne DaVinci with the user claims and tokens, so your flow can continue based on both user and device trust.

## Setup

### Resources

You can find more information and setup help in the following:

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* An Infinipoint account with an identity provider configured for PingOne DaVinci.

* Your Infinipoint client ID and client secret.

* The authorization, token, and user info endpoints for your Infinipoint identity provider.

* Your Infinipoint issuer URL, if you authenticate with OpenID Connect.

### Configuring the Infinipoint connector

In Infinipoint, use the **Identity Providers** wizard to add a PingOne DaVinci connector. The wizard provides the endpoint and credential values that you enter in the connector configuration.

Add the connector in PingOne DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

| Setting                          | Description                                                                                                                                                                                |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Provider Name**                | The name to display for Infinipoint as the identity provider.                                                                                                                              |
| **Auth Type**                    | Required. Select **OpenId** or **Oauth2** to match the identity provider you configured in Infinipoint.                                                                                    |
| **PingOne DaVinci Redirect URL** | The PingOne DaVinci redirect URL for this connector. This value is provided automatically as a read-only field and should be copied into your Infinipoint identity provider configuration. |
| **Issuer URL**                   | The issuer URL for your Infinipoint identity provider. This value is used to validate the identity provider when **OpenId** is selected as the **Auth Type**.                              |
| **Authorization Endpoint**       | The Infinipoint endpoint that starts the authorization request.                                                                                                                            |
| **Token Endpoint**               | The Infinipoint endpoint used to request and refresh tokens.                                                                                                                               |
| **User Info Endpoint**           | The Infinipoint endpoint that returns information about an authenticated user.                                                                                                             |
| **Client ID**                    | The client ID from your Infinipoint identity provider configuration.                                                                                                                       |
| **Client Secret**                | The client secret from your Infinipoint identity provider configuration.                                                                                                                   |
| **Scope**                        | The OIDC scope requested during authentication. This value is set to openid and can't be changed.                                                                                          |
| **Send state with request**      | Sends a unique state value with every authorization request. This option is disabled by default.                                                                                           |
| **Application Return To URL**    | Optional. When using the embedded flow player widget with an identity provider or social login connector, provide a callback URL for returning to your application.                        |

|   |                                                            |
| - | ---------------------------------------------------------- |
|   | These credentials and endpoints are issued by Infinipoint. |

## Using the connector in a flow

### Logging in with Infinipoint

The **Redirect to Infinipoint** capability redirects the user to Infinipoint for authentication and device verification, then returns to PingOne DaVinci to continue the flow.

At a high level:

1. The capability shows a login screen with the **OIDC Login** button, which sends the user to Infinipoint.

2. Infinipoint authenticates the user and verifies the posture of their device, then redirects back to the PingOne DaVinci redirect URL.

3. The connector outputs the user claims and tokens returned by Infinipoint, which you can evaluate in later nodes.

Test the flow by clicking **Save**, **Deploy**, and **Try Flow**.

## Capabilities

### Redirect to Infinipoint

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - - customAuth
>   - Display Name button
>   - showPoweredBy toggleSwitch
>   - skipButtonPress toggleSwitch
>
> * output object
>
>   * sub string
>
>   * aud string
>
>   * jti string
>
>   * iss string
>
>   * iat number
>
>   * exp number
>
>   * auth_time string
>
>   * tokens object
>
>     * access_token string
>
>     * refresh_token string
>
>     * id_token string
>
>     * token_type string
>
>     * expires_at number
>
>   * connectionId string
>
>   * connectorId string