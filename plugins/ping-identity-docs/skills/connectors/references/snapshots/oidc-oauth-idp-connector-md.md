---
title: OIDC and OAuth IdP Connector
description: Configure the OIDC and OAuth IdP connector in PingOne DaVinci to authenticate users with an external IdP using OpenID Connect or OAuth 2.0
component: connectors
page_id: connectors::oidc_oauth_idp_connector
canonical_url: https://docs.pingidentity.com/connectors/oidc_oauth_idp_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  setup: Setup
  resources: Resources
  configuring-the-oidc-and-oauth-idp-connector: Configuring the OIDC and OAuth IdP connector
  connector-configuration: Connector configuration
  provider-name: Provider Name
  auth-type: Auth Type
  redirect-url: Redirect URL
  issuer-url: Issuer URL
  authorization-endpoint: Authorization Endpoint
  token-endpoint: Token Endpoint
  token-attachment: Token Attachment
  userinfo-endpoint: UserInfo Endpoint
  app-id: App ID
  client-secret: Client Secret
  scope: Scope
  user-info-post-process: User Info Post Process
  application-return-to-url: Application Return to URL
  using-the-connector-in-a-flow: Using the connector in a flow
  oidc-or-oauth-authentication: OIDC or OAuth authentication
  user-information-collection: User information collection
  access-token-management: Access token management
  capabilities: Capabilities
  sign-on: Sign On
  get-user-details: Get User Details
  get-access-token-client-credentials-grant: Get Access Token (Client Credentials Grant)
  get-access-token-password-credentials-grant: Get Access Token (Password Credentials Grant)
---

# OIDC and OAuth IdP Connector

The OIDC and OAuth IdP connector lets you authenticate users with an identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* that supports OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
\</div>)* or OAuth 2.0 in your PingOne DaVinci flow.

You can use the OIDC and OAuth IdP connector to authenticate users with an IdP.

## Setup

### Resources

Learn more in the following:

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Configuring the OIDC and OAuth IdP connector

Add the connector in PingOne DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

##### Provider Name

The name of the IdP.

##### Auth Type

The authorization or authentication type, such as **OAuth2** or **OpenId**.

##### Redirect URL

Include this URL in your IdP configuration to allow it to redirect the browser back to PingOne DaVinci. If you use a custom PingOne domain, modify the URL accordingly.

##### Issuer URL

If **OpenId** is selected as the **Auth Type**, include this URL, which contains information about the IdP that can be validated.

##### Authorization Endpoint

The IdP endpoint, such as \` /rest/api/3\`. This endpoint is added to the base API URL selected in the connector endpoint configuration.

##### Token Endpoint

The IdP token endpoint, which is used to request or refresh tokens.

##### Token Attachment

If a token is attached, prepend its name with either `bearer` or `token`, as appropriate.

##### UserInfo Endpoint

The IdP endpoint, which returns information about an authenticated user.

##### App ID

The unique identifier for an IdP tenant.

##### Client Secret

The IdP secret, which the application must have to obtain a token.

##### Scope

The OIDC scope used during authentication to authorize access to user information. Separate scopes with a space. For example, enter `openid email profile`.

##### User Info Post Process

The code that contains information about an authenticated user using HTTP POST.

##### Application Return to URL

The URL that returns user to the application after an embedded flowplayer video has played or social login authentication is complete.

## Using the connector in a flow

### OIDC or OAuth authentication

You can use the **Sign On** capability to authenticate a user with OIDC or OAuth2.

### User information collection

You can use the **Get User Details** capability to validate an ID token.

No special configuration is needed. Add the capability and populate its properties according to the help text.

### Access token management

The connector has several capabilities to manage access tokens:

* **Get Access Token (Client Credentials Grant)**

* **Get Access Token (Password Credentials Grant)**

## Capabilities

### Sign On

> **Collapse: Show details**
>
> * * Properties
>   * Sign On `button`
>   * showPoweredBy `toggleSwitch`
>   * skipButtonPress `toggleSwitch`
>   * Output Schema
>   * oauth2 `object`
>   * accessToken `string`
>   * expiresIn `string`

### Get User Details

> **Collapse: Show details**
>
> * * Properties
>   * Sign On `button`
>   * showPoweredBy `toggleSwitch`
>   * skipButtonPress `toggleSwitch`

### Get Access Token (Client Credentials Grant)

> **Collapse: Show details**
>
> * * Input Schema
>   * default `object`
>   * type `object`
>   * additionalProperties `additionalProperties: true`

### Get Access Token (Password Credentials Grant)

> **Collapse: Show details**
>
> * * Properties
>   * Username `textField` `required`
>   * Password `textField` `required`
>   * Input Schema
>   * default `object`
>   * username `string` `required`
>   * password `string` `required`