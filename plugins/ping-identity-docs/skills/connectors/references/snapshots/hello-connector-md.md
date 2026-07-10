---
title: Hellō Connector
description: The Hellō connector lets you add Hellō as a login option in your PingOne DaVinci flow.
component: connectors
page_id: connectors::hello_connector
canonical_url: https://docs.pingidentity.com/connectors/hello_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 9, 2026
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  configuring-the-hellō-connector: Configuring the Hellō connector
  connector-configuration: Connector configuration
  using-the-connector-in-a-flow: Using the connector in a flow
  logging-in-with-hellō: Logging in with Hellō
  capabilities: Capabilities
  loginFirstFactor: Redirect to Hellō
---

# Hellō Connector

The Hellō connector lets you add [Hellō](https://www.hello.dev/) as a login option in your PingOne DaVinci flow.

The connector performs an OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
\</div>)* redirect to the user's Hellō Wallet and then returns to DaVinci with the claims you request, such as verified email, verified phone, and profile picture, so you can use them in your flow.

## Setup

### Resources

You can find more information and setup help in the following:

* Hellō documentation:

  * [Hellō documentation](https://www.hello.dev/docs/)

  * [Hellō scopes and claims](https://www.hello.dev/docs/scopes/)

  * [Hellō Console](https://console.hello.dev/)

* DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* A Hellō application created in the Hellō Console.

* Your Hellō Client ID and Client Secret.

### Configuring the Hellō connector

[Add the connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html) in DaVinci, then configure it as follows.

#### Connector configuration

| Setting                       | Description                                                                                                                                                               |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Redirect URI**              | The DaVinci redirect URI for this connector. This value is provided automatically as a read-only field and should be copied into your Hellō application configuration.    |
| **Client ID**                 | The client ID from your application in the Hellō Console.                                                                                                                 |
| **Client Secret**             | The client secret from your application in the Hellō Console.                                                                                                             |
| **Scope**                     | The OIDC scopes to request. Include openid along with any additional claims you want to receive, such as openid name email picture.                                       |
| **Application Return To URL** | Optional. When using the embedded flow player widget with an identity provider (IdP) or social login connector, provide a callback URL for returning to your application. |

## Using the connector in a flow

### Logging in with Hellō

The **Redirect to Hellō** capability redirects the user to their Hellō Wallet to authenticate, then returns to DaVinci with the requested claims.

At a high level:

1. The **Redirect to Hellō** capability sends the user to the Hellō Wallet to sign in and consent to the requested claims.

2. After the user authenticates, Hellō redirects back to the DaVinci redirect URI and the connector outputs the user claims you can evaluate in your flow.

Test the flow by clicking **Save**, **Deploy**, and **Try Flow**.

## Capabilities

### Redirect to Hellō

Redirect to Hellō

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
>   * auth\_time string
>
>   * tokens object
>
>     * access\_token string
>
>     * refresh\_token string
>
>     * id\_token string
>
>     * token\_type string
>
>     * expires\_at number
>
>   * connectionId string
>
>   * connectorId string