---
title: PingFederate Connector
description: Tap into the power of your existing PingFederate authentication policies by including them in your PingOne DaVinci flows.
component: connectors
page_id: connectors::pf_connector
canonical_url: https://docs.pingidentity.com/connectors/pf_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 19, 2024
section_ids:
  redirectless-method: Redirectless method
  redirect-method: Redirect method
  setup: Setup
  resources: Resources
  requirements: Requirements
  setting-up-pingfederate: Setting up PingFederate
  enabling-the-authentication-a-specification-of-interactions-available-for-building-software-to-access-an-application-or-service-application-programming-interface-api: Enabling the authentication application programming interface (API)
  adding-davinci-as-an-the-application-in-an-oauth-framework-that-requests-access-to-resources-if-the-request-is-approved-by-the-authorization-server-the-client-is-issued-an-access-token-for-the-resources-oauth-client-in-pingfederate: Adding DaVinci as an OAuth client in PingFederate
  configuring-the-pingfederate-connector: Configuring the PingFederate connector
  connector-configuration: Connector configuration
  redirect-url: Redirect URL
  client-id: Client ID
  client-secret: Client Secret
  scope: Scope
  base-url: Base URL
  using-the-connector-in-a-flow: Using the connector in a flow
  using-the-connector-with-the-redirectless-method: Using the connector with the redirectless method
  using-the-connector-with-the-redirect-method: Using the connector with the redirect method
  capabilities: Capabilities
  authenticate: Authenticate User (Redirectless)
  loginFirstFactor: Authenticate User (Redirect)
---

# PingFederate Connector

Tap into the power of your existing PingFederate authentication policies by including them in your PingOne DaVinci flows.

![A diagram of a DaVinci flow with a PingFederate authentication policy embedded in it.](_images/connector-images/dvc-pf-pingfederate-authentication-policy-diagram.png)

The connector provides two ways to use PingFederate in your flow:

## Redirectless method

The connector embeds the [JavaScript Widget for the PingFederate Authentication API](https://github.com/pingidentity/pf-authn-js-widget) in your DaVinci flow. This lets you create a user experience that starts and stays in DaVinci without redirecting the browser.

* The JavaScript Widget provides the user interface and communicates with the PingFederate authentication API.

* Your PingFederate authentication policy can include any of the integrations on the [widget compatibility list](https://github.com/pingidentity/pf-authn-js-widget/blob/master/docs/supportedIntegrations.md).

* To tailor the user experience to match your DaVinci flow or company branding, you can customize the JavaScript Widget's HTML, CSS, and JavaScript.

## Redirect method

This method redirects the browser to PingFederate to complete an authentication policy. When the policy completes, PingFederate redirects the browser back to DaVinci.

* The user interface is provided by an authentication application or adapter Velocity HTML templates, as configured in your PingFederate authentication policy.

* Your authentication policy can include any component you want. You aren't restricted to JavaScript Widget-compatible integrations.

* You can customize these templates in PingFederate. Learn more in [Customizable user-facing pages](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_custom_user_facing_pages.html) and the integration-specific documentation.

With both methods, the PingFederate connector makes the following available in your DaVinci flow:

* The access token *(tooltip: \<div class="paragraph">
  \<p>A data object by which a client authenticates to a resource server and lays claim to authorizations for accessing particular resources.\</p>
  \</div>)*

* The refresh token *(tooltip: \<div class="paragraph">
  \<p>A long-lived token used by OAuth clients to obtain a new access token without having to obtain fresh authorization from the resource owner.\</p>
  \</div>)*

* The ID token *(tooltip: \<div class="paragraph">
  \<p>A JSON Web Token (JWT) containing an assertion of a user's identity and profile information signed by an OAuth authorization server using JSON Web Signature (JWS) and sent to an OAuth client. The ID token can be encrypted using JSON Web Encryption (JWE). The client receives the ID token after a successful user authentication. The client can extract user information from the token for its purposes.\</p>
  \</div>)* (decoded and encoded)

* The complete (raw) response

## Setup

### Resources

Learn more in the following:

* PingFederate documentation

  * [JavaScript Widget for the PingFederate Authentication API](https://github.com/pingidentity/pf-authn-js-widget)

  * [Authentication applications and the authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_mobile_app_auth_through_rest_apis.html)

  * [Compatibility list for the PingFederate Authentication API and JavaScript Widget](https://github.com/pingidentity/pf-authn-js-widget/blob/master/docs/supportedIntegrations.md)

  * [Authentication policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_policies.html)

  * [Customizable user-facing pages](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_custom_user_facing_pages.html)

* DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* A configured PingFederate environment

* A configured PingFederate authentication policy

  |   |                                                                                                                                                                                                               |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If you want to use the redirectless approach, make sure your policy only includes adapters that are compatible with the [PingFederate JavaScript Widget](https://github.com/pingidentity/pf-authn-js-widget). |

### Setting up PingFederate

#### Enabling the authentication application programming interface (API) *(tooltip: \<div class="paragraph">&#xA;\<p>A specification of interactions available for building software to access an application or service.\</p>&#xA;\</div>)*

Enable the authentication API if:

* You want to use the connector with the redirectless (JavaScript Widget) method.

* You want to use the connector with the redirect method and you want to use an [authentication application](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_authentication_applications_authentication_api.html) in your PingFederate authentication policy.

  1. In PingFederate, go to **Authentication > Integration > Authentication API Applications**.

  2. Click **Enable Authentication API**.

  3. (Optional) If you're using the redirect method and want to use an authentication application in your authentication policy, add an authentication application. Learn more in [Configuring authentication applications](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_authenticationapplicationtasklet_authenticationapplicationstate.html) in the PingFederate documentation.

  4. Click **Save**.

  5. If you added an authentication application, select it in your authentication policy:

     1. Go to **Authentication > Policies > Your policy**.

     2. In the **Authentication Application** list, select your authentication application.

     3. Click **Done**.

#### Adding DaVinci as an OAuth client *(tooltip: \<div class="paragraph">&#xA;\<p>The application in an OAuth framework that requests access to resources. If the request is approved by the authorization server, the client is issued an access token for the resources.\</p>&#xA;\</div>)* in PingFederate

1. In PingFederate, go to **Applications > OAuth Clients > Clients**. Click **Add Client**.

2. In the **Client ID** field, enter a unique ID, such as `davinci-client`. Note the ID. You'll enter it in the connector settings.

3. In the **Client Name** field, enter a name, such as `DaVinci Client`.

4. For **Client Authentication**, select **Client Secret**.

5. For **Client Secret** field, click **Change Secret**, then click **Generate Secret**. Note the secret. You'll enter it in the connector settings.

6. If you want to use the connector with the redirectless method, select **Allow Authentication API OAuth Initiation**.

7. For **Allowed Grant Types**, select **Authorization Code**.

8. (Optional) If you want to use refresh tokens, for **Allowed Grant Types**, select **Refresh Token**.

9. For the **OpenID Connect** **ID Token Signing Algorithm**, select **RSA using SHA-256**.

10. Click **Save**.

### Configuring the PingFederate connector

Add the connector in DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

##### Redirect URL

This connector's redirect URL. If you use the connector with the redirect method, add this URL as a **Redirect URI** in your PingFederate OAuth Client configuration. This lets PingFederate redirect the browser back to this connector to continue the DaVinci flow. You don't need this with the redirectless method.

##### Client ID

The client ID that you noted in **Adding DaVinci as an OAuth Client in PingFederate.**

##### Client Secret

The client secret that you noted in **Adding DaVinci as an OAuth Client in PingFederate.**

##### Scope

The scope *(tooltip: \<div class="paragraph">
\<p>In OAuth, a parameter on an access request and resulting, issued access token that specifies a limitation or limitations on access to the protected resource or resources.\</p>
\</div>)* requested from PingFederate, including **openid**. If you configured other scopes in your PingFederate. OAuth Client, add them here. Separate multiple scopes with a space.

##### Base URL

Enter your PingFederate base URL. For example, `https://pf.example.com:9031`.

## Using the connector in a flow

### Using the connector with the redirectless method

![A screen capture that shows the complete flow.](_images/connector-images/dvc-pf-redirectless-authentication-flow.png)

1. Download the [PingFederate - Authentication (Redirectless)](https://marketplace.pingone.com/item/pingfederate-authentication-redirectless) flow template. Learn more in [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html).

2. Select the **Authenticate User (Redirectless)** node.

   1. (Optional) If you have your own custom version of the PingFederate JavaScript Widget, enter the URL in the **PingFederate JavaScript Widget URL** field.

   2. (Optional) If you want to show your own logo on the PingFederate JavaScript Widget, enter the image URL in the **PingFederate JavaScript Widget Logo URL** field.

   3. (Optional) If you want to customize the page that contains the PingFederate JavaScript Widget, edit the **HTML Template**, **CSS**, and **Script** fields. Learn more in **Building a custom page** in the [HTTP Connector](http_connector.html) connector documentation.

   4. Click **Apply**.

3. Test the flow by clicking **Save**, **Deploy**, and **Try Flow**.

4. Continue building your flow by replacing the **Custom HTML Message** node with a path to the resource that the user initially requested.

### Using the connector with the redirect method

![A screen capture that shows the complete flow.](_images/connector-images/dvc-pf-redirect-method-flow.jpg)

The **Authenticate User (Redirect)** capability allows you to redirect the browser to PingFederate to allow the user to authenticate.

No special configuration is needed. Add the capability and populate its properties according to the help text.

## Capabilities

### Authenticate User (Redirectless)

Embed a PingFederate authentication policy in the DaVinci flow. The authentication policy can include components that work with the PingFederate JavaScript Widget.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - PingFederate JavaScript Widget URL textField required
>
>   Default: `https://s3.amazonaws.com/pingone/public_downloads/pingfederate/widget/latest/pf.authn-widget.js`
>
> - * PingFederate JavaScript Widget Logo URL textField
>   * HTML Template textArea
>
>   Default:
>
>   ```none
>   <div class="content" style="padding: 30px">
>    <div class="heading">Authentication Application</div>
>    <form id="skForm">
>    <input id="skinput-response" type="hidden" name="response" value=""/>
>    <button data-skform="skForm" data-skbuttontype="form-submit" data-skbuttonvalue="submit" data-skvalue="submit" id="skbutton" data-skcomponent="skbutton" type="button" style="display:none"/>
>    <div/>
>    </button>
>    </form>
>    <div id="authnwidget">
>   </div>
>   ```
>
> - CSS codeEditor
>
>   Default:
>
>   ```none
>   @import "https://assets.pingone.com/ux/end-user/0.36.1/end-user.css";
>   @import "https://s3.amazonaws.com/pingone/public_downloads/pingfederate/widget/latest/main-styles.css";
>   ```
>
> - Script codeEditor
>
>   Write custom JavaScript. Caution: Custom code is for advanced users only. Before using custom code, review the security risks in the DaVinci documentation by searching for "Using custom code safely".
>
>   Default:
>
>   ```none
>   var script = document.createElement('script');
>   script.src = '{{widgetUrl}}';
>   script.onload = function () {
>    load();
>   };
>   document.head.appendChild(script);
>
>   function load() {
>    var authnWidget = new PfAuthnWidget("{{issuerUrl}}", {
>    divId: 'authnwidget',
>    logo: '{{widgetLogoUrl}}',
>    });
>
>    var config = {
>    client_id: '{{clientId}}',
>    scope: ['{{scope}}'],
>    state: '{{state}}',
>    response_type: 'code',
>    onAuthorizationSuccess: function (response) {
>    document.getElementById('skinput-response').value = JSON.stringify(response);
>    document.getElementById('skbutton').click();
>    },
>    onAuthorizationFailed: function (response) {
>    document.getElementById('skinput-response').value = JSON.stringify(response);
>    document.getElementById('skbutton').click();
>    },
>    };
>    authnWidget.initRedirectless(config);
>   }
>   ```
>
> * default object
>
>   * properties object
>
>     * widgetUrl string required
>
>       PingFederate JavaScript Widget URL
>
>     * widgetLogoUrl string
>
>       PingFederate JavaScript Widget Logo URL
>
>     * customHTML string required
>
>       HTML Template
>
>     * customCSS string required
>
>       CSS
>
>     * customScript string required
>
>       Script
>
> - output object
>
>   * rawResponse object
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
>   * statusCode number
>
>   * headers object
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

### Authenticate User (Redirect)

Redirect to a PingFederate authentication policy, then return to the DaVinci flow. The authentication policy can include any components you want.

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - - Display Name button
>   - Show "Powered by" Message toggleSwitch
>   - Skip Button Press toggleSwitch
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
