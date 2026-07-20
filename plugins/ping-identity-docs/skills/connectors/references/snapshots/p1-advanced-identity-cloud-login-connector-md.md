---
title: PingOne Advanced Identity Cloud Login Connector
description: Configure the PingOne Advanced Identity Cloud Login connector to authenticate users via the default journey in Advanced Identity Cloud
component: connectors
page_id: connectors::p1_advanced_identity_cloud_login_connector
canonical_url: https://docs.pingidentity.com/connectors/p1_advanced_identity_cloud_login_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 9, 2026
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  setting-up-pingone-advanced-identity-cloud: Setting up PingOne Advanced Identity Cloud
  configuring-the-pingone-advanced-identity-cloud-login-connector: Configuring the PingOne Advanced Identity Cloud Login connector
  connector-configuration: Connector configuration
  client-id: Client ID
  client-secret: Client Secret
  issuer-url: Issuer URL
  scope: Scope
  application-redirect-url: Application Redirect URL
  davinci-redirect-url: DaVinci Redirect URL
  using-the-connector-in-a-flow: Using the connector in a flow
  authenticating-users: Authenticating users
  capabilities: Capabilities
  loginFirstFactor: PingOne Advanced Identity Cloud Login
---

# PingOne Advanced Identity Cloud Login Connector

The PingOne Advanced Identity Cloud Login connector lets you authenticate users using the default journey in PingOne Advanced Identity Cloud in your PingOne DaVinci flow.

## Setup

### Resources

Learn more in the following:

* Advanced Identity Cloud documentation:

  * [What is PingOne Identity Governance?](https://docs.pingidentity.com/pingoneaic/identity-governance/administration/getting-started-what-is-iga.html)

  * [Identity Governance REST API](https://backstage.forgerock.com/docs/idcloud/latest/identity-governance/rest-api/rest-api-preface.html)

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* An Advanced Identity Cloud license

* A license for Identity Governance

### Setting up PingOne Advanced Identity Cloud

To allow PingOne DaVinci to access PingOne Advanced Identity Cloud environment, create an application:

1. In PingOne Advanced Identity Cloud, go to **Applications**.

2. Click **[icon: plus, set=fa]Custom Application**.

3. Select **OIDC - OpenId Connect**, then click **Next**.

4. Select **Web**, then click **Next**.

5. Enter the application name and description, and select an owner. Click **Next**.

6. Define a client ID and secret.

   |   |                                                                                     |
   | - | ----------------------------------------------------------------------------------- |
   |   | The **Client ID** and **Client Secret** are needed for the connector configuration. |

7. Click **Create Application**.

8. On the application details view, go to the **Sign On** tab.

9. In the PingOne Advanced Identity Cloud Login connector configuration, copy the **PingOne DaVinci Redirect URL** value from the connector settings and paste it into the **Sign-in URLs** field.

10. For **Grant Types**, use the defaults (`Authorization Code`, `Client Credentials`, and `Refresh Token`).

11. For **Scopes**, use `openid` at minimum. You can define additional OIDC scopes, such as `profile`, `email`, `address`, and `phone`.

12. Click **Save**.

### Configuring the PingOne Advanced Identity Cloud Login connector

Add the connector in PingOne DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

##### Client ID

The client ID you defined when configuring your application in PingOne Advanced Identity Cloud.

##### Client Secret

The client secret you defined when configuring your application in PingOne Advanced Identity Cloud.

##### Issuer URL

The URL containing information about the identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* that can be validated.

##### Scope

The OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
\</div>)* scopes used to request certain information about the user. Separate scopes with a space, such as `openid email profile`.

##### Application Redirect URL

Your application's redirect URL, such as "https\://app.yourorganization.com/". Enter this URL if you embed the PingOne DaVinci widget in your application. This allows PingOne DaVinci to redirect the browser back to your application.

##### DaVinci Redirect URL

Enter this URL in your Advanced Identity Cloud console under the **Application** tab.

## Using the connector in a flow

### Authenticating users

You can use the **PingOne Advanced Identity Cloud Login** capability to authenticate users, with Advanced Identity Cloud acting as a social identity provider.

The connector redirects the browser to Advanced Identity Cloud, initiates the default journey to allow the user to authenticate, then returns to PingOne DaVinci with the authentication result.

## Capabilities

### PingOne Advanced Identity Cloud Login

Authenticate the user using the default journey in PingOne Advanced Identity Cloud.

> **Collapse: Show details**
>
> * Output Schema
>
> - output object
>
>   * iss string
>
>   * sub string
>
>   * aud string
>
>   * exp number
>
>   * iat number
>
>   * auth\_time number
>
>   * name string
>
>   * family\_name string
>
>   * given\_name string
>
>   * zoneinfo string
>
>   * locale string
>
>   * email string
>
>   * address string
>
>   * phone\_number string
>
>   * tokens object
>
>     * access\_token string
>
>     * refresh\_token string
>
>     * id\_token string