---
title: ScrambleID Connector
description: Configure the ScrambleID connector to enable OIDC-based authentication with ScrambleID in a PingOne DaVinci flow
component: connectors
page_id: connectors::scrambleid_connector
canonical_url: https://docs.pingidentity.com/connectors/scrambleid_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  configuring-the-scrambleid-connector: Configuring the ScrambleID connector
  connector-configuration: Connector configuration
  discovery-document-url: Discovery Document URL
  authorization-endpoint: Authorization Endpoint
  token-endpoint: Token Endpoint
  client-id: Client ID
  client-secret: Client Secret
  scope: Scope
  davinci-redirect-uri: DaVinci Redirect URI
  using-the-connector-in-a-flow: Using the connector in a flow
  redirecting-users-to-scrambleid: Redirecting users to ScrambleID
  capabilities: Capabilities
  loginFirstFactor: Redirect to ScrambleID
---

# ScrambleID Connector

The ScrambleID connector lets you use OpenID Connect (OIDC) login with [ScrambleID](https://www.scrambleid.com/) in your PingOne DaVinci flow.

The connector redirects users to ScrambleID for authentication, handles the token exchange automatically, and returns validated identity tokens and claims to your flow.

## Setup

### Resources

You can find more information and setup help in the following:

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* A ScrambleID account with OIDC access

* Administrator permissions to create or manage OIDC clients in ScrambleID

* OIDC integration (Client ID, Client Secret, and redirect URI) configured in your ScrambleID tenant

### Configuring the ScrambleID connector

Add the connector in PingOne DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

##### Discovery Document URL

The OIDC discovery document URL (well-known endpoint) for your ScrambleID environment.

##### Authorization Endpoint

The OIDC authorization endpoint for initiating the login redirect.

##### Token Endpoint

The OIDC token endpoint used to exchange the authorization code for tokens.

##### Client ID

The OIDC client identifier registered with ScrambleID.

##### Client Secret

The OIDC client secret registered with ScrambleID.

##### Scope

The OIDC scopes to request. Defaults to openid offline\_access.

##### DaVinci Redirect URI

The redirect URI registered in ScrambleID that allows tokens to be returned to PingOne DaVinci.

## Using the connector in a flow

### Redirecting users to ScrambleID

![A screen capture of the complete ScrambleID redirect flow.](_images/connector-images/tap-scrambleid-redirecttoscrambleid-flow.png)

This flow redirects the user to ScrambleID for OIDC authentication. After the user signs in, PingOne DaVinci automatically completes the token exchange and returns identity claims to the flow for downstream logic.

Test the flow by clicking **Save**, **Deploy**, and **Try Flow**.

## Capabilities

### Redirect to ScrambleID

OIDC redirect to ScrambleID

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