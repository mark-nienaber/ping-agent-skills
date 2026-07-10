---
title: Accessing the API interactive documentation
description: PingFederate ships with interactive documentation for both developers and non-developers to explore the API endpoints, view documentation for the API, and experiment with API calls.
component: pingfederate
version: 13.1
page_id: pingfederate:developers_reference_guide:pf_access_api_interact_documentation
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/developers_reference_guide/pf_access_api_interact_documentation.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 8, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result:
---

# Accessing the API interactive documentation

PingFederate ships with interactive documentation for both developers and non-developers to explore the API endpoints, view documentation for the API, and experiment with API calls.

## About this task

In general, you can make API calls from an interactive user interface, custom applications, or from command line tools such as cURL. The endpoint is only available at the administrative port, as defined by the `pf.admin.https.port` property in `<pf_install>/pingfederate/bin/run.properties`.

|   |                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For enhanced API security, you must include `X-XSRF-Header: PingFederate` in all requests and use the `application/json` content type for PUT and POST requests. |

To access the administrative API documentation, follow these steps:

## Steps

1. Start PingFederate.

2. Start a web browser.

3. Browse to the following URL: https\://*\<pf\_host>*:9999/pf-admin-api/api-docs/

   |   |                                                                                                                                                                                                                                                                                   |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | *\<pf\_host>* is the network address of your PingFederate server. It can be an IP address, a host name, or a fully qualified domain name. It must be reachable from your computer.`9999` is the default value of the `pf.admin.https.port` property in the `run.properties` file. |

   |   |                                                                                                                                                                                                                                              |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The administrative API is also documented in the OpenAPI Specification, previously known as the Swagger Specification. Click on the `/pf-admin-api/v1/swagger.json` URL on the Administrative API Documentation page to access the contents. |

4. To test an administrative API, follow these steps:

   1. Select a section of the administrative API you would like to explore; for example, **/dataStores**.

   2. Expand the method you want to use; for example, **GET /dataStores**.

   3. Enter required parameters, if any. For more information, see **Operation Models** underneath the selected API endpoint.

   4. Click **Try it out**.

      |   |                                                                                                                                                                                                        |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | You might be prompted to sign on using administrative credentials over HTTP Basic authentication. The role assigned to the respective administrative accounts affects the access to the requested API. |

      ### Result:

   If the request completes successfully, the administrative API returns the **Request URL**, the **Response Body**, the **Response Code**, and the **Response Headers**.

---

---
title: Application endpoints
description: Application endpoints provide a means, through standard HTTP, by which external applications can communicate with the PingFederate server.
component: pingfederate
version: 13.1
page_id: pingfederate:developers_reference_guide:pf_app_endpoints
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/developers_reference_guide/pf_app_endpoints.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
---

# Application endpoints

Application endpoints provide a means, through standard HTTP, by which external applications can communicate with the PingFederate server.

The single sign-on (SSO) and single log-out (SLO) endpoints for an identity provider (IdP) and a service provider (SP) include optional parameters which you can use to specify error pages that users see in the event of an SSO or SLO failure. By default, PingFederate provides templates for these and other errors or conditions. For more information, see [Customizable user-facing pages](../administrators_reference_guide/pf_custom_user_facing_pages.html).

SP endpoints also include those available for system for cross-domain identity management (SCIM) inbound provisioning. For more information, see [Provisioning for SPs](../introduction_to_pingfederate/pf_provis_for_sp.html).

For either SP or IdP servers, PingFederate provides a maintenance endpoint for administrators to verify that the server is running. Endpoints applicable to both server roles include those needed for adapter-to-adapter mapping and retrieval of WS-Trust metadata. For more information, see [Adapter-to-adapter mappings](../administrators_reference_guide/pf_adaptertoadapter_mappings.html) and [WSC and WSP support](../introduction_to_pingfederate/pf_wsc_and_wsp_supp.html).

PingFederate provides a favorite icon for all application endpoints. For more information, see [Customizing the favicon for application and protocol endpoints](../administrators_reference_guide/pf_customiz_favicon_for_applicat_and_protocol_endpoints.html).

---

---
title: Authentication API
description: The PingFederate authentication API is a JSON-based API that enables external web applications to handle end-user interactions like credential prompts.It does this by providing access to the current state of the flow as an end-user proceeds through a PingFederate authentication policy.
component: pingfederate
version: 13.1
page_id: pingfederate:developers_reference_guide:pf_authentication_api
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/developers_reference_guide/pf_authentication_api.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 5, 2026
section_ids:
  key-concepts: Key concepts
  session-management: Session management
  authentication-api-explorer: Authentication API Explorer
  javascript-widget-for-the-pingfederate-authentication-api: JavaScript widget for the PingFederate authentication API
---

# Authentication API

The PingFederate authentication API *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)* is a JSON-based API that enables external web applications to handle end-user interactions like credential prompts.It does this by providing access to the current state of the flow as an end-user proceeds through a PingFederate authentication policy.

Authentication flows are initiated through browser-based single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)* application endpoints, such as `/idp/startSSO.ping`, or a protocol request, such as an OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
\</div>)* authentication request received at the authorization endpoint: `/as/authorization.oauth2`. As PingFederate runs the configured authentication policy, if it encounters an API-capable adapter or selector, and an authentication application is configured for the policy, PingFederate redirects to the authentication application's URL, passing the ID of the flow in the `flowId` query parameter.

The authentication application can then retrieve the current state of the flow by issuing a `GET` request to the `/pf-ws/authn/flows/{flowId}` endpoint. The `links` field in the response lists the available authentication actions that can be performed from the current state. To invoke an action, the authentication application sends a `POST` request to the `/pf-ws/authn/flows/{flowId}` endpoint.

|   |                                                                                                                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Authentication API requests are serviced by the `/pf-ws/authn/flows` endpoint, with flow IDs being passed as additional path information. If you're protecting the endpoint with a Web Application Firewall (WAF), you should apply the firewall to `/pf-ws/authn/flows` instead of `/pf-ws/authn/flows/{flowId}`. |

The API client can choose authentication actions using either an `action` query parameter or a custom content type. The `action` query parameter should be used when your networks block custom content types and is specified using the following format:

```
/pf-ws/authn/flows/{flowId}?action={actionID}
```

For example, to check username and password, pass the `checkUsernamePassword` action ID through the query parameter as follows:

```
/pf-ws/authn/flows/{flowId}?action=checkUsernamePassword
```

For the custom content type, the action ID is specified using the Content-Type HTTP request header in the following format:

```
application/vnd.pingidentity.{actionId}+json
```

For example, to indicate a username and password check from the HTML Form Adapter, specify the following:

```
application/vnd.pingidentity.checkUsernamePassword+json
```

When the application invokes an action, PingFederate responds either with the next state for the flow or an error.

When the user completes the authentication policy steps successfully, the authentication API returns a `RESUME` status to the authentication application. This status indicates that the API client should redirect the user's browser to the `resumeUrl` specified in the response. PingFederate is then responsible for the final step in the flow, such as passing a SAML assertion to a partner. A `RESUME` status is also sent if PingFederate encounters an identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)* connection in the policy tree, or an IdP adapter or selector that isn't API-capable. When the API client redirects the user, PingFederate takes the steps needed to invoke the authentication source.

If the user has interacted with an authentication application, and the flow terminates with an error, the API client receives a `FAILED` status from the API.

|   |                                                                                                                                                                                                                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | To avoid issues with third-party cookies in some browsers, give the authentication application the same parent domain as the PingFederate authentication API URL that the application accesses. This could be a common domain of PingFederate's base URL or one of PingFederate's defined [virtual hosts](../administrators_reference_guide/pf_virtual_host_names.html). |

## Key concepts

* Flow

  The SSO transaction invoking the authentication API.

* States

  The available states (if any) for a given API-enabled adapter or selector.

* Current state

  Indicates what the adapter or selector is ready to do next.

* Actions

  The available actions (if any) for a given state.

## Session management

The authentication API endpoint has the same domain as PingFederate's other application endpoints and shares the PingFederate session cookies with those endpoints. This ensures that session data created by API applications can be retrieved when the user interacts with PingFederate's other endpoints and vice versa.

|   |                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Because the authentication API relies on the PingFederate session cookies, only browser-based web applications can currently make use of the API. Server-side web applications aren't supported. |

In order for PingFederate to manage session cookies correctly, the JavaScript-written authentication application must set the `withCredentials` flag on the XMLHttpRequest object to `true`.

To protect against cross-site request forgeries, API clients are also required to include an X-XSRF-Header HTTP request header with each request, for example: `X-XSRF-Header: PingFederate`. This custom header ensures that browsers enforce cross-origin resource sharing (CORS) policies when API requests are sent. This header can have any value.

## Authentication API Explorer

PingFederate includes an API Explorer, which allows you to view the states, actions, and models available for the various API-capable adapters and selectors included in your PingFederate environment. The endpoint for the Authentication API Explorer is `/pf-ws/authn/explorer`.

You can download a Postman collection file from **Authentication > Integration > Authentication API Applications**. The file contains information converted from the Explorer into a Postman collection. You can then import the collection file into the Postman application. The collection file provides every possible action of every state in every plugin deployed in the PingFederate instance. It contains:

* All API-capable plugins, both adapters and selectors, with all of their states and actions.

* A prepopulated body containing information about required information types and parameters.

* Headers for API calls, both X-XSRF-Header and Content-Type.

Learn more in [Exploring the authentication API](pf_exploring_authentication_api.html).

## JavaScript widget for the PingFederate authentication API

The JavaScript Widget for the PingFederate authentication API is a customizable JavaScript library that provides the capabilities of the HTML Form Adapter and Identifier First Adapter through the authentication API:

* User Login

* Trouble Signing in

* Trouble with Username

* Password Reset

The widget is a ready-to-use drop-in bundle with CSS and customizable templates. This alternative to the PingFederate templates provides a sign-on experience as a single page application. You can find the widget in the [JavaScript Widget for the PingFederate Authentication API](https://github.com/pingidentity/pf-authn-js-widget) GitHub repository.

---

---
title: Authorization endpoint
description: The OAuth authorization server (OAuth AS) uses the authorization endpoint to interact directly with resource owners, authenticate them, and obtain their authorizations.
component: pingfederate
version: 13.1
page_id: pingfederate:developers_reference_guide:pf_authorization_endpoint
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/developers_reference_guide/pf_authorization_endpoint.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2026
section_ids:
  endpoint-asauthorization-oauth2: "Endpoint: /as/authorization.oauth2"
  openid-connect-parameters: OpenID Connect parameters
  oauth-access-token-management-parameters: OAuth access token management parameters
  example: Example
  example-a-partial-match: Example - A partial match
---

# Authorization endpoint

The OAuth authorization server (OAuth AS) *(tooltip: \<div class="paragraph">
\<p>The authorizing service in an OAuth framework that issues and manages access tokens for clients to access protected resources.\</p>
\</div>)* uses the authorization endpoint to interact directly with resource owners, authenticate them, and obtain their authorizations.

[The OAuth 2.0 Authorization Framework](https://tools.ietf.org/html/rfc6749) defines the authorization endpoint. Typically, an OAuth client makes an authorization request by directing a resource owner through an HTTP user-agent to the authorization endpoint. After the OAuth AS completes its interaction with the resource owner, the OAuth AS redirects the resource owner's user-agent back to the client's redirect URI with the response to the authorization request.

|   |                                                                                                                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This endpoint can be used in an OAuth Scope Authentication Selector configuration, which can affect the behavior of the endpoint. For example, the `idp` parameter might be enforced or overridden by policy determined by an instance of the OAuth Scope Authentication Selector.This endpoint accepts the HTTP GET and POST methods. |

## Endpoint: /as/authorization.oauth2

When transmitting through the HTTP POST method, the required `Content-Type` value is `application/x-www-form-urlencoded`. The following table describes parameters for this endpoint.

| Parameter                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `client_id`(Required)              | The client identifier.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `response_mode`                    | When set to `form_post`, the authorization response is returned to the client in an auto-POST form, in accordance with [the OAuth 2.0 Form Post Response Mode specification](https://openid.net/specs/oauth-v2-form-post-response-mode-1_0.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `response_type`                    | A value of `code` results in the Authorization Code grant type while a value of `token` implies the Implicit grant type. Additionally, a value of `id_token` can be requested by implicit clients. A value of `none` signals the Authorization Server to authenticate the user and check for an active session without returning any Authorization Code, Access Token, or ID Token.To initiate a Hybrid Flow, multiple response\_type values can be specified by space-separating them. When using the Hybrid Flow, some tokens are returned from the Authorization Endpoint and others are returned from the Token Endpoint. For information about multiple-valued response type combinations, see the description of the `restrictedResponseTypes` parameter in [OAuth Client Management Service](pf_oauth_client_manage_service.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `code_challenge`                   | To reduce the risk of authorization code interception attack, supply a one-time string value to associate the authorization request with the token request. For more information, see [Proof Key for Code Exchange (PKCE) by OAuth Public Clients](https://tools.ietf.org/html/rfc7636).Applicable only when `response_type` parameter value is `code`. Mandatory if the client is required to do so. For more information, see **Require Proof Key for Code Exchange (PKCE)** in [Configuring OAuth clients](../administrators_reference_guide/pf_configuring_oauth_clients.html).&#xA;&#xA;If used, the OAuth client must submit the corresponding code verifier when using the authorization code to obtain an access token. For more information, see code\_verifier in OAuth grant type parameters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `code_challenge_method`            | Applicable only when the `response_type` parameter value is `code` and a `code_challenge` parameter value is provided.This parameter indicates the transformation method used to derive the `code_challenge` parameter value from that of the `code_verifier` parameter. PingFederate OAuth AS supports two transformation methods:- `plain`, which indicates the `code_challenge` parameter value is that of the `code_verifier` parameter.

- `S256`, which indicates the `code_challenge` parameter is derived from the `code_verifier` parameter value as follows`[.parmname]`code\_challenge`=Base64Url-encode(SHA256(ASCII([.parmname]`code\_verifier`)))`, where:- `ASCII([.parmname]`code\_verifier`)` denotes the octets of the ASCII representation of the `code_verifier` value.

- `SHA256(octets)` denotes the SHA 256-bit hash of the octets.

- `Base64Url-encode(octets)` denotes the base64url encoding of octets; the output is URL-safe.

  &#xA;&#xA;For detailed information about the transformation method, see Proof Key for Code Exchange (PKCE) by OAuth Public Clients.The `code_challenge_method` parameter value is case-sensitive. An error message is returned to the clients for any other values.Omitting the `code_challenge_method` parameter has the same effect as providing the `code_challenge_method` parameter with a value of `plain`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `redirect_uri`                     | The URI to which PingFederate redirects the resource owner's user-agent after an authorization is obtained.For OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">&#xA;\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>&#xA;\</div>)* protocol compliance, clients that use the authorization code or implicit grant type must include this parameter in their authorization requests. It is also the default behavior in new PingFederate installations starting with version 9.1.4.For upgraded installations, this requirement remains true for clients that have been configured with more than one redirection URIs. For clients that have been configured with only one redirection URI, this requirement is waived to minimize the impact that it might impose on customers upgrading to version 9.1.4 or a subsequent release. As needed, it can be enabled at a later time.&#xA;&#xA;If this parameter is used, the same parameter and value must also be used in subsequent token requests. For more information, see OAuth grant type parameters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `claims_locales`                   | Specifies the end-user's preferred languages for claims being returned in a space-separated list, ordered by preference. The values must conform to the [IETF BCP 47](https://www.rfc-editor.org/info/bcp47) guidelines.&#xA;&#xA;You can map the claims\_locales value into the persistent grants (and therefore the access tokens, the ID tokens, or both) from an identity provider (IdP) adapter or an IdP connection by selecting Context under Source and Requested Claims Locales under Value in the Contract Fulfillment tab in the IdP Adapter Mapping configuration or the OAuth Attribute Mapping configuration in an IdP connection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `login_hint`                       | Provides a hint to the PingFederate AS about the end user. For example, when an OAuth client includes a `login_hint` in its authorization request and the authentication source is an HTML Form Adapter instance, the username field in the login form is pre-populated with the `login_hint` parameter value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `max_age`                          | Sets an allowable elapsed time in seconds since the end user last authenticated. If the elapsed time exceeds the value of `max_age`, PingFederate prompts the end user for authentication.&#xA;&#xA;The user's last authenticated time is tracked by Authentication Sessions and various adapters that have built-in session capabilities, such as the HTML Form Adapter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `request`                          | A single, self-contained parameter; a signed JSON Web Token (JWT) *(tooltip: \<div class="paragraph">&#xA;\<p>An IETF standard container format for a JSON object used for the secure exchange of content, such as identity or entitlement information. You can find the industry standard in \<a href="https\://datatracker.ietf.org/doc/html/rfc7519">RFC 7519\</a>.\</p>&#xA;\</div>)* whose claims represent the request parameters of the authorization request. The OpenID Connect specification calls this JWT a request object.The `request` parameter is required if a client is configured to transmit request parameters in signed request objects. When PingFederate receives an authorization request, it verifies the digital signature of the signed request object based on the key obtained from the pre-configured JWKS URL or JWKS, and the selected request object signing algorithms. If the signature does not pass the verification process, the request fails.The `request` parameter is optional if a client is not configured to transmit request parameters in signed request objects but is configured with a JWKS URL or an actual JWKS. This flexibility allows the client to transmit request parameters in signed request objects for some requests and without the use of signed request objects for some other transactions.If a client is not configured to transmit request parameters in signed request objects and is not configured with a JWKs URL or an actual JWKs, PingFederate ignores the `request` parameter. When PingFederate receives an authorization request with a signed request object, it processes the authorization request and disregards the signed request object. As needed, develop a custom IdP adapter using the PingFederate SDK to extract the `request` parameter and its value from the HTTP request for further processing.PingFederate can decrypt encrypted request objects, which are described in the [OpenID Connect 1.0 specification](https://openid.net/specs/openid-connect-core-1_0.html#EncryptedRequestObject). Request objects with asymmetric encryption must be encrypted using the public keys that PingFederate exposes at `/pf/JWKS`. Request objects with symmetric encryption need a key derived from the client's configured client secret and the client secret must be stored in a reversible format with, for example, symmetric encrypted ID tokens or hash-based message authentication code (HMAC) ID tokens. You can configure PingFederate to accept only request objects that are encrypted by enabling the `front-channel-encryption-required` setting in `jwt-request-object-options.xml`.&#xA;&#xA;If a client includes in an authorization request a request parameter other than client\_id, as a parameter outside of the signed request object and a claim inside of the signed request object, PingFederate always uses the claim value found inside the signed request object to process the request further.&#xA;&#xA;For the client\_id request parameter, the values outside of the signed request object must match the claim values inside of the signed request object. If the values do not match, PingFederate returns an error message to the client.&#xA;&#xA;If a request parameter is found only outside of the signed request object, PingFederate ignores the request parameter and returns no error message.	&#xA;&#xA;Per OAuth and OpenID Connect specifications, a client must always include in an authorization request the client\_id parameter outside of the signed request object.For client configuration information, see the **Require Signed Request** setting in [Configuring OAuth clients](../administrators_reference_guide/pf_configuring_oauth_clients.html). For more information about request objects, see [RFC 9101: JWT Secured Authorization Request (JAR)](https://datatracker.ietf.org/doc/rfc9101/). |
| `request_uri`                      | This parameter indicates that the client is using the [pushed authorization requests](https://datatracker.ietf.org/doc/html/rfc9126) (PAR) protocol to initiate an authorization flow. The client previously pushed an authorization request payload to the PAR endpoint of the AS. The payload can contain any of the parameters that usually comprise an authorization request and any additional parameters needed for client authentication.After the AS validates the request and saves the payload, it sends the `request_uri` parameter to the client to serve as a reference to the payload. The client uses the `request_uri` parameter to request an authorization code or token. The AS uses the `request_uri` value to look up the request payload and continue the authorization flow\.PingFederate invalidates the `request_uri` when consent details are presented to the user, or when the PAR reference timeout expires. Once consent details are presented, the `request_uri` is invalidated regardless of whether the user accepts, rejects, or abandons the flow. If consent details are not presented, the client can reuse the same `request_uri` in a subsequent authorization request until the PAR reference timeout expires.Learn more about PAR in [Pushed authorization requests endpoint](pf_pushed_authoriz_request_endpoint.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `scope`                            | Expresses the scope of the access request as a list of space-separated, case-sensitive strings. For detailed information about scopes, see [Scopes and scope management](../administrators_reference_guide/pf_scopes_and_scope_management.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `state`                            | An opaque value used by the client to maintain state between the request and callback. If included, the AS returns this parameter and the given value when redirecting the user agent back to the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `ui_locales`                       | Specifies the end-user's preferred languages for OAuth user interactions in a space-separated list, ordered by preference. The values must conform to the [IETF BCP 47](https://tools.ietf.org/html/bcp47) guidelines.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `idp` or `PartnerIdpId`            | A PingFederate OAuth AS parameter indicating the entity ID or the connection ID of the IdP with whom to initiate Browser single sign-on (SSO) *(tooltip: \<div class="paragraph">&#xA;\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>&#xA;\</div>)* for user authentication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `pfidpadapterid` or `IdpAdapterId` | A PingFederate OAuth AS parameter indicating the IdP adapter instance ID of the adapter to use for user authentication.&#xA;&#xA;This parameter might be overridden by policy based on authentication policies. For example, an OAuth Scope Authentication Selector instance could enforce the use of a given adapter instance based on client-requested scopes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `PolicyAction`(optional)           | The HTML Form Adapter immediately returns the value of this parameter in the `policy.action` attribute, allowing the policy to bypass the adapter in favor of an alternative authentication source, provided a rule matching the action is configured. When this parameter is set to `identity.registration` and the adapter is followed by a local identity profile, the user is directed to the registration page for the profile.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

If more than one source of authentication is configured in the system and no `pfidpadapterid` or `idp` parameter is provided, PingFederate provides users with an intermediate page asking them to choose among the available sources of authentication. The authentication results in a set of user attributes that must be mapped into the `USER_KEY` attribute for persistent grant storage and the `USER_NAME` attribute that displays on the user authorization page.

## OpenID Connect parameters

The following table describes OpenID Connect parameters for this endpoint.

| Parameter       | Description                                                                                                                                                                                                                                                                                                                                                                                    |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `acr_values`    | Specifies the Authentication Context Class Reference (acr) values for the AS to use when processing an Authentication Request. Express the values as a space-separated string, and list them in order of preference.                                                                                                                                                                           |
| `id_token_hint` | Includes an ID token as a hint to the PingFederate AS about the end user. If the authenticated user does not match the information stored in the ID token, the PingFederate AS rejects the authorization request and returns an error message.                                                                                                                                                 |
| `nonce`         | Specifies a string value used to associate a client session with an ID token and to reduce replay attacks. The value passes through unmodified from an authorization request to the ID token.                                                                                                                                                                                                  |
| `prompt`        | Specifies whether the AS prompts the end user for reauthentication and consent. Expressed as a list of space-separated, case-sensitive ASCII string values. If included, the client can use this parameter to verify that the end user is still present for the current session or to bring attention to the request.PingFederate supports values of `none`, `login`, `consent`, and `create`. |

## OAuth access token management parameters

PingFederate supports multiple access token management (ATM) instances. Clients can specify an ATM instance by providing the ATM ID (`access_token_manager_id`) or a resource URI (`aud` or `resource`) in their requests to the PingFederate OAuth AS.

| Parameter                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `access_token_manager_id` | The `access_token_manager_id` value is the instance ID of the desired ATM instance. When specified, PingFederate uses the desired ATM instance for the request if it's eligible; otherwise it aborts the request.&#xA;&#xA;When the access\_token\_manager\_id parameter is specified, PingFederate ignores the aud and resource parameter.&#xA;&#xA;When the aud parameter is specified, PingFederate ignores the resource parameter.                                                   |
| `aud`                     | The `aud` is the resource URI the client wants to access. The provided value is matched against resource URIs configured in access token management instances. When a match is found, PingFederate uses the corresponding access token management instance for the request if it's eligible; otherwise it aborts the request.                                                                                                                                                            |
| `resource`                | The `resource` is the resource URI that the wants to access. The provided value is matched against resource URIs configures in access token management instances. When a match is found, PingFederate uses the corresponding access token management instance for the request if it's elligible. Otherwise it aborts the request.If multiple resource parameters are requested, they must match to a single access token management instance. Otherwise PingFederate aborts the request. |

A match can be an exact match or a partial match where the provided URI has the same scheme and authority parts and a more specific path contained within the path of the pre-configured resource URI. PingFederate takes an exact match over a partial match. If there are multiple partial matches, PingFederate takes the partial match where the provided URI matches more specifically against the pre-configured resource URI.

## Example

## Example - A partial match

A resource URI of `https://app.example.local` is a partial match for the following provided URIs:

* https\://app.example.local/file1.ext

* https\://app.example.local/path/file2.ext

* https\://app.example.local/path/more

---

---
title: Client-initiated backchannel authentication endpoint
description: A CIBA-capable client uses this endpoint to initiate a backchannel, out-of-band flow to authenticate the resource owners and obtain their authorizations.
component: pingfederate
version: 13.1
page_id: pingfederate:developers_reference_guide:pf_ciba_endpoint
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/developers_reference_guide/pf_ciba_endpoint.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 20, 2023
section_ids:
  endpoint-asbc-auth-ciba: "Endpoint: /as/bc-auth.ciba"
  oauth-client-identification-and-authentication: OAuth client identification and authentication
  oauth-access-token-management-parameters: OAuth access token management parameters
  example: Example
  example-a-partial-match: Example - A partial match
  related-links: Related links
---

# Client-initiated backchannel authentication endpoint

A CIBA-capable client uses this endpoint to initiate a backchannel, out-of-band flow to authenticate the resource owners and obtain their authorizations.

The [OpenID Connect Client Initiated Backchannel Authentication Flow](https://openid.net/specs/openid-client-initiated-backchannel-authentication-core-1_0.html) defines the client-initiated backchannel authentication (CIBA) endpoint.

|   |                                                  |
| - | ------------------------------------------------ |
|   | This endpoint accepts only the HTTP POST method. |

## Endpoint: /as/bc-auth.ciba

The following table describes parameters for this endpoint. The required `Content-Type` value is `application/x-www-form-urlencoded`.

| Parameter                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `client_id`(Required)                            | The client identifier.&#xA;&#xA;When sending request parameters of an authentication request with a signed request object, the client must include the client\_id parameter and its value inside and outside of the request parameter value. Both client\_id parameter values must match.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `scope`(Required)                                | The scope of the access request. Expressed as a list of space-separated, case-sensitive strings.Scope values are globally defined on the **System > OAuth Settings > Scope Management** window. You can constrain scopes on a client-to-client basis.This parameter must include the `openid` scope value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `client_notification_token`                      | A bearer token provided by the client that PingFederate must include when sending a ping callback message to the client's notification endpoint. This usage must conform to the syntax for bearer credentials as defined in section 2.1 of [RFC 6750](https://tools.ietf.org/html/rfc6750).If the client is configured to use the poll delivery method, this parameter is required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `id_token_hint, login_hint_token, or login_hint` | Per the CIBA specification, the client must include one and only one hint for the OpenID Provider to identify the user. The valid hint parameters are `id_token_hint`, `login_hint`, and `login_hint_token`.- `id_token_hint`

  Use this parameter to include an ID token as a hint for PingFederate to identify the user. This ID token must be unencrypted. It must be a signed ID token.

- `login_hint_token`

  Use this parameter to include a JSON web token (JWT) as a hint for PingFederate to identify the user. The attributes of this token can vary from one use case to another. For more information how PingFederate uses the login hint token, see [Configuring identity hint contract](../administrators_reference_guide/help_cibapolicymanagementtasklet_cibapolicyrequesthintcontractstate.html).

- `login_hint`

  Use this parameter to provide a hint to PingFederate to identify the user. The value can contain an email address, phone number, account number, subject identifier, username, or any attribute that both sides agreed upon.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `user_code`                                      | A secret code that is known only to the user and verifiable by PingFederate through the use of a Password Credential Validator instance. The purpose of this code is to authorize the transmission of an authentication request to the user's authentication device.If the client record is configured to support user code and associated with a user code-enabled CIBA request policy, this parameter is required.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `binding_message`                                | An alphanumeric message intended to be made available on both the authentication device and the consumption device. The user can tie them together and decide whether to grant the authorization.When provided, the length of the message must range from 1 - 20 characters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `requested_expiry`                               | The requested expiration time of the request in seconds since the generation of the authentication request acknowledgment.&#xA;&#xA;PingFederate honors the requested expiration time only if the value is shorter than that of the Transaction Lifetime field found in the associated CIBA request policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `request`                                        | A single, self-contained parameter; a signed JWT whose claims represent the request parameters of the authentication request. The OpenID Connect specification calls this JWT a request object. The requirement of this parameter and the processing rules vary depending on whether the client is configured with the **Require CIBA Signed Requests** option.If the client is configured to transmit request parameters to the backchannel authentication endpoint in signed request objects, this parameter is required. In other words, the **Require CIBA Signed Requests** checkbox is selected in the configuration of the client. When PingFederate receives an authentication request with a signed request object, it verifies the digital signature of the signed request object based on the key obtained from the pre-configured JWKS URL (or JWKS) and the selected CIBA request object signing algorithm (or algorithms). If the signature does not pass the verification process, the request fails.If a client isn't configured to transmit request parameters to the backchannel authentication endpoint in signed request objects, but it is configured with a JWKS URL or an actual JWKS, this parameter is optional.This flexibility allows the client to transmit request parameters in signed request objects for some requests and without the use of signed request objects for some other transactions. When PingFederate receives an authentication request with a signed request object, it verifies the digital signature of the signed request object based on the key obtained from the pre-configured JWKS URL (or JWKS) and the selected CIBA request object signing algorithms. If the signature does not pass the verification process, the request fails.&#xA;&#xA;If the client is not configured to transmit request parameters to the backchannel authentication endpoint in signed request objects, and not configured with a JWKS URL or an actual JWKS, an authentication request with a signed request object will always fail. |

* Sample authentication request

```
POST /as/bc-auth.ciba HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Host: www.example.com

client_id=myCibaApp&scope=openid&login_hint=joe@example.com
```

* Sample authentication request acknowledgements

  * 200 - Success

    ```
    HTTP/1.1 200 OK
    ...
    {
        "auth_req_id": "HQnCgSeUzWNORZEv8n3E8wIip9L3iwBdJAAect04BqdpEsFBGqfxRvoa_Q",
        "interval": 3,
        "expires_in": 120
    }
    ```

  * 400 - Bad Request

    ```
    HTTP/1.1 400 Bad Request
    ...
    {
        "error_description": "CIBA authentication requests MUST contain the openid scope value.",
        "error": "invalid_scope"
    }
    ```

    ```
    HTTP/1.1 400 Bad Request
    ...
    {
        "error_description": "Authentication request parameters (such as binding_message) MUST NOT be present outside of the JWT when a signed authentication request is used.",
        "error": "invalid_request"
    }
    ```

    ```
    HTTP/1.1 400 Bad Request
    ...
    {
        "error_description": "Exactly one (not more, not less) of the hint parameters (i.e. 'login_hint_token', 'id_token_hint' or 'login_hint') must be provided.",
        "error": "invalid_request"
    }
    ```

    ```
    HTTP/1.1 400 Bad Request
    ...
    {
        "error_description": "User could not be sufficiently identified to initiate out-of-band auth",
        "error": "unknown_user_id"
    }
    ```

    ```
    HTTP/1.1 400 Bad Request
    ...
    { "error": "invalid_user_code" }
    ```

    ```
    HTTP/1.1 400 Bad Request
    ...
    { "error": "missing_user_code" }
    ```

    ```
    HTTP/1.1 400 Bad Request
    ...
    {
        "error_description": "Client is not configured to support user code but a user_code was sent in the request.",
        "error": "invalid_request"
    }
    ```

    ```
    HTTP/1.1 400 Bad Request
    ...
    {

        "error_description": "Policy is set to require a token for the user hint but login_hint was sent.",
        "error": "invalid_request"
    }
    ```

  * 401 - Unauthorized

    ```
    HTTP/1.1 401 Unauthorized
    ...
    {
        "error_description": "Invalid client or client credentials.",
        "error": "invalid_client"
    }
    ```

  * 500 - Server Error

    ```
    HTTP/1.1 500 Server Error
    ...
    {
        "error_description": "Client is configured to support user code but server policy doesn't have a PCV configured to do the user code checking",
        "error": "server_error"
    }
    ```

  For more information about error responses, see section [13. Authentication Error Response](https://openid.net/specs/openid-client-initiated-backchannel-authentication-core-1_0.html) in the specification.

## OAuth client identification and authentication

The authentication requirement of this endpoint depends on the client authentication method configured for the clients.

| Authentication method                | Parameters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Client secret                        | Clients can present their client identifier and client secret using the HTTP Basic authentication scheme, where the client identifier is the username, and the client secret is the password.Clients can provide credentials using the request parameters `client_id` and `client_secret`.&#xA;&#xA;This is a sensitive parameter. To avoid recording it in web server logs, only pass in this parameter with the HTTP POST method in the message body, or through the HTTP Basic authentication scheme.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Client certificate                   | Clients must present their client certificate for mutual TLS authentication. The issuer and the subject distinguished name (DN) of the client certificate must match values configured for the clients.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Private key JWT or Client Secret JWT | Clients must include request parameters `client_assertion_type` and `client_assertion` in the message body of their requests.- `client_assertion_type`

  The value describes the format of the assertion as defined by the authorization server. For the private\_key\_jwt and client\_secret\_jwt client authentication methods, the value is `urn:ietf:params:oauth:client-assertion-type:jwt-bearer`.

- `client_assertion`

  The value is the authentication token.**Example**```
...
client_assertion_type=
urn%3Aietf%3Aparams%3Aoauth%
3Aclient-assertion-type%3Ajwt-bearer&
client_assertion=
eyJhbGciOiJSUzI1NiIs...LbSWi1YO-TILOd4L7ZCg&
...
```&#xA;&#xA;For readability, line breaks are inserted and the authentication token is truncated.Learn more about the private\_key\_jwt and client\_secret\_jwt client authentication methods in [Client Authentication](https://openid.net/specs/openid-connect-core-1_0.html#ClientAuthentication) and [Using Assertions for Client Authentication](https://datatracker.ietf.org/doc/html/rfc7521/#autoid-7). |
| None                                 | Clients must pass in the `client_id` parameter in a query string or the message body to identify themselves.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## OAuth access token management parameters

PingFederate supports multiple access token management (ATM) instances. Clients can specify an ATM instance by providing the ATM ID (`access_token_manager_id`) or a resource URI (`aud` or `resource`) in their requests to the PingFederate OAuth AS.

| Parameter                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `access_token_manager_id` | The `access_token_manager_id` value is the instance ID of the desired ATM instance. When specified, PingFederate uses the desired ATM instance for the request if it is eligible; otherwise it aborts the request.&#xA;&#xA;When the access\_token\_manager\_id parameter is specified, PingFederate ignores the aud and resource parameter.&#xA;&#xA;When the aud parameter is specified, PingFederate ignores the resource parameter.                                                   |
| `aud`                     | The `aud` is the resource URI the client wants to access. The provided value is matched against resource URIs configured in access token management instances. When a match is found, PingFederate uses the corresponding access token management instance for the request if it is eligible; otherwise it aborts the request.                                                                                                                                                            |
| `resource`                | The `resource` is the resource URI that the wants to access. The provided value is matched against resource URIs configures in access token management instances. When a match is found, PingFederate uses the corresponding access token management instance for the request if it is elligible. Otherwise it aborts the request.If multiple resource parameters are requested, they must match to a single access token management instance. Otherwise PingFederate aborts the request. |

A match can be an exact match or a partial match where the provided URI has the same scheme and authority parts and a more specific path contained within the path of the pre-configured resource URI. PingFederate takes an exact match over a partial match. If there are multiple partial matches, PingFederate takes the partial match where the provided URI matches more specifically against the pre-configured resource URI.

## Example

## Example - A partial match

A resource URI of `https://app.example.local` is a partial match for the following provided URIs:

* https\://app.example.local/file1.ext

* https\://app.example.local/path/file2.ext

* https\://app.example.local/path/more

## Related links

* [Scopes and scope management](../administrators_reference_guide/pf_scopes_and_scope_management.html)

* [Configuring OAuth clients](../administrators_reference_guide/pf_configuring_oauth_clients.html)

* [Managing CIBA request policies](../administrators_reference_guide/help_cibapoliciesmanagementtasklet_cibapoliciesmanagementstate.html)

* [Defining a request policy](../administrators_reference_guide/help_cibapolicymanagementtasklet_cibapolicymanagementstate.html)

---

---
title: Cluster configuration replication
description: A web service endpoint is available to replicate the administrative-console configuration to other nodes in a PingFederate cluster from the Connection Management Service.
component: pingfederate
version: 13.1
page_id: pingfederate:developers_reference_guide:pf_cluster_config_replication
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/developers_reference_guide/pf_cluster_config_replication.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  code-sample: Code sample
---

# Cluster configuration replication

A web service endpoint is available to replicate the administrative-console configuration to other nodes in a PingFederate cluster from the Connection Management Service.

The cluster configuration replication web service endpoint allows a client of this web service to create, update, or delete a connection, and then push the new configuration to the other cluster nodes.

The service endpoint is `/pf-mgmt-ws/ws/ConfigReplication`.

The WSDL document describing this service can be retrieved from `/pf-mgmt-ws/ws/ConfigReplication?wsdl`.

The web service exposes the following method: `public void replicateConfiguration();`.

## Code sample

Below is example client code using the Apache AXIS libraries that invokes the configuration replication functionality.

```
Call call2 = (Call) service.createCall();
    call2.setUsername("joe");
    call2.setPassword("test");
    String addr2 = "https://localhost:9999/pf-mgmt-ws/ws/ConfigReplication";
    call2.setTargetEndpointAddress(addr2);
    call2.setOperationName("replicateConfiguration");
    call2.invoke(new Object[]{});
```

---

---
title: Coding example
description: When you integrate a web application with PingFederate, use the single sign-on (SSO) Directory Service to generate a connection or adapter list. The code needed to create any of the lists is similar.
component: pingfederate
version: 13.1
page_id: pingfederate:developers_reference_guide:pf_coding_example
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/developers_reference_guide/pf_coding_example.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
---

# Coding example

When you integrate a web application with PingFederate, use the single sign-on (SSO) Directory Service to generate a connection or adapter list. The code needed to create any of the lists is similar.

The following Java code example retrieves an identity provider (IdP) list from the web service. The program calls the getIDPList method in the SSO Directory Service to retrieve an IdP list and print it to the console. This example uses the Apache Axis library and includes optional code for authentication to the PingFederate server. For more information see [Configuring service authentication](../administrators_reference_guide/help_manageserviceauthenticationtasklet_serviceauthenticationstate.html). HTTPS is recommended when including credentials.

```
import org.apache.axis.client.Call;
import org.apache.axis.client.Service;
import java.net.URL;
import javax.xml.namespace.QName;
import com.pingidentity.ws.SSOEntity;
public class SSODirectoryClientSample
{
   public static void main(String[] args) throws Exception
   {
    Service service = new Service();
    Call call = (Call) service.createCall();
    call.setUsername("username");
    call.setPassword("pass");
    URL serviceUrl = new URL(
       "https://localhost:9031/pf-ws/services/
         SSODirectoryService");
    QName qn = new QName("urn:BeanService", "SSOEntity");
    call.registerTypeMapping(SSOEntity.class, qn,
      new org.apache.axis.encoding.ser.BeanSerializerFactory(
          SSOEntity.class, qn),

       new org.apache.axis.encoding.ser.BeanDeserializerFactory(
           SSOEntity.class, qn));
    call.setTargetEndpointAddress( serviceUrl );
    call.setOperationName( new QName(
      "http://www.pingidentity.com/servicesSSODirectoryService",
        "getIDPList"));
    Object result = call.invoke( new Object[] {} );
    if (result instanceof SSOEntity[])
    {
       SSOEntity[] idpArray = (SSOEntity[])result;
       for (SSOEntity idp : idpArray)
      {
        System.out.println(idp.getEntityId() + " " +
          idp.getCompany());
      }
    }
    else
    {
       System.out.println("Received problem response from
          server: " + result);
    }
  }
}
```

---

---
title: Configure access to the administrative API
description: Similar to the administrative console, access to the administrative API after initial setup can be protected by several authentication and authorization schemes.
component: pingfederate
version: 13.1
page_id: pingfederate:developers_reference_guide:pf_config_access_to_admin_api
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/developers_reference_guide/pf_config_access_to_admin_api.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
---

# Configure access to the administrative API

Similar to the administrative console, access to the administrative API after initial setup can be protected by several authentication and authorization schemes.

Access to the administrative API after initial setup is protected by one of the following authentication and authorization schemes:

* [Native authentication, against local administrative accounts](pf_enable_native_auth_for_admin_api.html)

* [LDAP authentication](pf_enable_ldap_authen.html)

* [RADIUS authentication](pf_enable_radius_authen.html)

* [Mutual TLS client certificate-based authentication](pf_enable_cert_based_authen.html)

* [OAuth 2.0 authorization](pf_enable_oauth20_authoriz.html)

* [JWT authorization](pf_enabling_jwt_authorization.html)

For new installations, native authentication is the default.

For upgrades, if the authentication or authorization method of the administrative API wasn't previously set, such as when upgrading from PingFederate 7.3 or an earlier version, the Upgrade Utility sets the value to that of the administrative console. Otherwise, it preserves the previously set value, such as when upgrading from PingFederate 8.0 to a later release.

You can change the authentication or authorization method for the administrative API to any of the methods, regardless of which authentication or authorization method you choose for the administrative console.

In addition to authentication and authorization, PingFederate provides role-based access control, as described in the following table. The roles assigned to the accounts affect the results of the API calls.

**PingFederate User Access Control**

| Account type | Administrative role | Access privileges                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------ | ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Admin        | User Admin          | Create users, deactivate users, change or reset passwords, and install replacement license keys.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Admin        | Admin               | Configure partner connections and most system settings, except the management of local accounts and the handling of local keys and certificates.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Admin        | Expression Admin    | Map user attributes by using the expression language, Object-Graph Navigation Language (OGNL).&#xA;&#xA;Only Administrative users who have both the Admin role and the Expression Admin role:&#xA;&#xA;Can be granted the User Admin role. This restriction prevents non-Expression Admin users from granting themselves the Expression Admin Role.&#xA;&#xA;Can be granted write access to the file system or directory where PingFederate is installed. This restriction prevents a non-Expression Admin user from placing a data.zip file containing expressions into the \<pf\_install>/pingfederate/server/default/deploy directory, which would introduce expressions into PingFederate. |
| Admin        | Crypto Admin        | Manage local keys and certificates.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Auditor      | Not applicable      | View-only permissions for all administrative functions. When the **Auditor** role is assigned, no other administrative roles can be set.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | All four administrative roles are required to access and make changes through the following services:- The `/bulk`, `/configArchive`, and `/configStore` administrative API endpoints

- The **Configuration Archive** window, accessed from **System > Server**, in the administrative console

- The **Connection Management** configuration item on the **Service Authentication** window, accessed from **Security > System Integration** |

---

---
title: Connection Management Service
description: The Connection Management Service supports basic connection management capabilities and is accessible only on a PingFederate server running the administrative console.
component: pingfederate
version: 13.1
page_id: pingfederate:developers_reference_guide:pf_connection_management_service
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/developers_reference_guide/pf_connection_management_service.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
---

# Connection Management Service

The Connection Management Service supports basic connection management capabilities and is accessible only on a PingFederate server running the administrative console.

|   |                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------- |
|   | As of PingFederate 10.2, the Connection Management Service has been deprecated and will be removed in a future release. |

The Connection Management Service is useful in a variety of circumstances. Consider the following use cases:

* Using the Connection Management Service as a utility, you can migrate changes to a partner connection through staging environments. For example, development, test, and production.

  Using the Connection Management Service, you might need to make changes to URLs and keys to make the connection appropriate to the next environment.

* Using the Connection Management Service, an external application can update or delete connections programmatically, or create new ones using an exported connection XML file as a template.

You can find the WAR file for this service, `pf-mgmt-ws.war`, in the `<pf_install>/pingfederate/server/default/deploy2` directory.

|   |                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------- |
|   | If you do not want to allow use of the service, do not deploy it: remove the WAR file from the `deploy2` directory. |

The SOAP-accessible service endpoint is `pf-mgmt-ws/ws/ConnectionMigrationMgr`.

The web services Description Language (WSDL) document describing this service can be retrieved from `/pf-mgmt-ws/ws/ConnectionMigrationMgr?wsdl`.

---

---
title: Constructing an alternative metadata exchange endpoint
description: You can embed virtual server ID information into a security token service (STS) metadata exchange endpoint or a SAML and WS-Federation metadata exchange endpoint.
component: pingfederate
version: 13.1
page_id: pingfederate:developers_reference_guide:pf_construct_alt_metadata_exchange_endpoint
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/developers_reference_guide/pf_construct_alt_metadata_exchange_endpoint.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
  example: Example:
  example-2: Example:
  example-3: Example:
---

# Constructing an alternative metadata exchange endpoint

You can embed virtual server ID information into a security token service (STS) metadata exchange endpoint or a SAML and WS-Federation metadata exchange endpoint.

## About this task

This process is useful for scenarios where partners prefer to retrieve metadata by sending one query parameter such as`PartnerSpId` or `PartnerIdpId`, instead of two query parameters such as `PartnerSpId` or `PartnerIdpId` and `vsid`.

## Steps

1. Construct a JSON object containing a key-value pair of the virtual server ID by using the following format. `\{"vsid":"<VirtualServerIdValue>"}`

   ### Example:

   For example, if the virtual server ID is `Engineering`, the JSON object is `\{"vsid":"Engineering"}`.

2. Base64url-encode the JSON object.

   ### Example:

   For example, if the JSON object is `\{"vsid":"Engineering"}`, the base64url-encoded value is `eyJ2c2lkIjoiRW5naW5lZXJpbmcifQ`.

   Learn more about base64url in [RFC 4648](https://datatracker.ietf.org/doc/html/rfc4648#autoid-10).

3. Insert the base64url-encoded value prefixed with a forward slash into the metadata exchange endpoints, described as follows:

   * Federation metadata endpoint (`/pf/federation_metadata.ping`)

     Between `/pf` and `/federation_metadata.ping`.

   * STS metadata endpoint (`/pf/sts_mex.ping`)

     Between `/pf` and `/sts_mex.ping`.

     ### Example:

     For example, if the base64url-encoded value is `eyJ2c2lkIjoiRW5naW5lZXJpbmcifQ`, the metadata exchange endpoints embedding with the virtual server ID are:

   * Federation metadata endpoint

     `/pf/eyJ2c2lkIjoiRW5naW5lZXJpbmcifQ/federation_metadata.ping`

     Example: https\://idp.example.com:9031/pf/eyJ2c2lkIjoiRW5naW5lZXJpbmcifQ/federation\_metadata.ping?PartnerSpId=sp.example.org

   * STS metadata endpoint

     `/pf/eyJ2c2lkIjoiRW5naW5lZXJpbmcifQ/sts_mex.ping`

   Example: https\://idp.example.com:9031/pf/eyJ2c2lkIjoiRW5naW5lZXJpbmcifQ/sts\_mex.ping?PartnerSpId=sp.example.org

---

---
title: Deleting connections
description: You can invoke the web service to delete connections.
component: pingfederate
version: 13.1
page_id: pingfederate:developers_reference_guide:pf_delet_connect
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/developers_reference_guide/pf_delet_connect.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  code-sample: Code sample
---

# Deleting connections

You can invoke the web service to delete connections.

The web service exposes the following method for connection deletion.

```
public void deleteConnection( String entityId, String role) throws IOException
```

The `entityId` parameter is the connection ID, which identifies the connection to be deleted. The `role` parameter is the connection role, identity provider (IdP) or service provider (SP).

## Code sample

The following example uses the Apache AXIS libraries to invoke this web service to delete a connection.

```
Service service = new Service();
Call call = (Call) service.createCall();
call.setUsername("username");
call.setPassword("password");
call.setTargetEndpointAddress(
	"https://localhost:9999/pf-mgmt-ws/ws/ConnectionMigrationMgr"
	);
call.setOperationName("deleteConnection");
call.invoke(new Object[]{"entityid", "SP"});
```

---

---
title: Developer&#8217;s Reference Guide
description: This section describes the PingFederate endpoints and APIs.
component: pingfederate
version: 13.1
page_id: pingfederate:developers_reference_guide:pf_dev_ref
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/developers_reference_guide/pf_dev_ref.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 15, 2022
---

# Developer's Reference Guide

This section describes the PingFederate endpoints and APIs.

Use this developer's guide to learn how to develop authentication API-capable adapters and selectors with the following endpoints and APIs:

* [OAuth 2.0 endpoints](pf_oauth_20_endpoints.html)

* [Web service interfaces and APIs](pf_web_service_interface_api.html)

* [Application endpoints](pf_app_endpoints.html)

* [Authentication API](pf_authentication_api.html)

* [Developing authentication API-capable adapters and selectors](../sdk_developers_guide/pf_develop_auth_api_capable_adapt_selec.html)

---

---
title: Device authorization endpoint
description: The device authorization endpoint allows a user to grant authorization to a device client using a browser on a second device, such as a smart phone or a computer.
component: pingfederate
version: 13.1
page_id: pingfederate:developers_reference_guide:pf_device_auth_endpoint
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/developers_reference_guide/pf_device_auth_endpoint.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 20, 2023
section_ids:
  endpoint-asdevice_authz-oauth2: "Endpoint: /as/device_authz.oauth2"
  example-request: Example request
  exampleresponse-codes-and-example-responses: ExampleResponse codes and example responses
  oauth-client-identification-and-authentication: OAuth client identification and authentication
  related-links: Related links
---

# Device authorization endpoint

The device authorization endpoint allows a user to grant authorization to a device client using a browser on a second device, such as a smart phone or a computer.

The [OAuth 2.0 Device Authorization Grant](https://tools.ietf.org/html/rfc8628) defines the device authorization endpoint. Based on the specification, the device sends a device authorization request to PingFederate, the authorization server (AS), at its device authorization endpoint.

|   |                                                                            |
| - | -------------------------------------------------------------------------- |
|   | Per OAuth specifications, this endpoint accepts only the HTTP POST method. |

## Endpoint: /as/device\_authz.oauth2

The required `Content-Type` value is `application/x-www-form-urlencoded`. The following table describes parameters for this endpoint.

| Parameter         | Description                                                                                                                                                                                                                                                                                                                                                           |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `client_id`       | A unique identifier the client provides to the resource server *(tooltip: \<div class="paragraph">&#xA;\<p>In OAuth 2.0, a server that hosts protected resources and can accept and respond to resource requests from clients presenting a valid access token.\</p>&#xA;\</div>)* to identify itself. This identifier is included with every request the client makes |
| `scope`(Optional) | The scope of the access request expressed as a list of space-delimited, case-sensitive strings.Scopes can also be constrained on a client-to-client basis. For more information about scopes, see [Scopes and scope management](../administrators_reference_guide/pf_scopes_and_scope_management.html).                                                               |

Both the request and the response follow the [OAuth 2.0 Device Authorization Grant](https://tools.ietf.org/html/draft-ietf-oauth-device-flow).

## Example request

```
POST /as/device_authz.oauth2 HTTP/1.1
Content-Type: application/x-www-form-urlencoded
Host: www.example.com
...

client_id=df_client
```

## ExampleResponse codes and example responses

200 - Success

```
HTTP/1.1 200 OK

...
{
    "user_code": "YYD6-CD4T",
    "device_code": "4EHsIngavzIPvvqMlFgQlseTCsH7EpU75f9yGvj60T",
    "interval": 5,
    "verification_uri_complete": "https://www.example.com/as/user_authz.oauth2?user_code=YYD6-CD4T",
    "verification_uri": "https://www.example.com/as/user_authz.oauth2",
    "expires_in": 600
}
```

400 - Bad Request

```
HTTP/1.1 400 Bad Request

...
{
    "error_description": "The requested scope(s) must be blank or a subset of the provided scopes.",
    "error": "invalid_scope"
}
```

401 - Unauthorized

```
HTTP/1.1 401 Unauthorized

...
{
    "error_description": "Invalid client or client credentials.",
    "error": "invalid_client"
}
```

## OAuth client identification and authentication

The authentication requirement of this endpoint depends on the client authentication method configured for the clients.

| Authentication method                | Parameters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Client secret                        | Clients can present their client identifier and client secret using the HTTP Basic authentication scheme, where the client identifier is the username, and the client secret is the password.Clients can provide credentials using the request parameters `client_id` and `client_secret`.&#xA;&#xA;This is a sensitive parameter. To avoid recording it in web server logs, only pass in this parameter with the HTTP POST method in the message body, or through the HTTP Basic authentication scheme.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Client certificate                   | Clients must present their client certificate for mutual TLS authentication. The issuer and the subject distinguished name (DN) of the client certificate must match values configured for the clients.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Private key JWT or Client Secret JWT | Clients must include request parameters `client_assertion_type` and `client_assertion` in the message body of their requests.- `client_assertion_type`

  The value describes the format of the assertion as defined by the authorization server. For the private\_key\_jwt and client\_secret\_jwt client authentication methods, the value is `urn:ietf:params:oauth:client-assertion-type:jwt-bearer`.

- `client_assertion`

  The value is the authentication token.**Example**```
...
client_assertion_type=
urn%3Aietf%3Aparams%3Aoauth%
3Aclient-assertion-type%3Ajwt-bearer&
client_assertion=
eyJhbGciOiJSUzI1NiIs...LbSWi1YO-TILOd4L7ZCg&
...
```&#xA;&#xA;For readability, line breaks are inserted and the authentication token is truncated.Learn more about the private\_key\_jwt and client\_secret\_jwt client authentication methods in [Client Authentication](https://openid.net/specs/openid-connect-core-1_0.html#ClientAuthentication) and [Using Assertions for Client Authentication](https://datatracker.ietf.org/doc/html/rfc7521/#autoid-7). |
| None                                 | Clients must pass in the `client_id` parameter in a query string or the message body to identify themselves.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## Related links

* [Device authorization grant](../introduction_to_pingfederate/pf_device_auth_grant.html)

* [Configuring authorization server settings](../administrators_reference_guide/help_authorizationserversettingstasklet_oauthauthorizationserversettingsstate.html)

---

---
title: Device authorization through mobile applications
description: In addition to initiating a regular OAuth authorization flow, mobile applications and single-page web applications can use the authentication API to initiate and complete the user authorization side of the OAuth device authorization flow.
component: pingfederate
version: 13.1
page_id: pingfederate:developers_reference_guide:pf_device_authorization_through_mobile_applications
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/developers_reference_guide/pf_device_authorization_through_mobile_applications.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 6, 2023
---

# Device authorization through mobile applications

In addition to initiating a regular OAuth authorization flow, mobile applications and single-page web applications can use the authentication API to initiate and complete the user authorization side of the OAuth [device authorization](../introduction_to_pingfederate/pf_device_auth_grant.html) flow.

There are a few differences between this case and the non-device case:

* You don't need to select **Allow Authentication API Redirectless Mode** on the **Client** window for the OAuth device client because the mobile or single-page web application doesn't receive tokens at the end of the flow.

* For the same reason, in the case of web applications, you don't need to enable **Allow Redirectless Mode** on the **Authentication Application** window when configuring the authentication API application.

* The initial request is made to the user authorization endpoint `/as/user_authz.oauth2` rather than `/as/authorization.oauth2`. As with the non-device flow, you must specify `pi.flow` for the `response_mode`. Optionally, the initial request can also provide the `user_code`. This endpoint doesn't need any other parameters.

* At the end of the flow, the `OAUTH_DEVICE_COMPLETED` state is returned to the API client. This response doesn't include an authorization code or tokens.

As with the non-device flow, you must select **Bypass Authorization Approval** on the **Client** window for the device client because the PingFederate authentication API does not yet support the OAuth consent approval step.

The models and actions for the `OAUTH_DEVICE_USER_CODE_REQUIRED`, `OAUTH_DEVICE_USER_CODE_CONFIRMATION_REQUIRED`, and `OAUTH_DEVICE_COMPLETED` states are documented in the [Authentication API Explorer](pf_exploring_authentication_api.html) under the PingFederate Core adapter.

---

---
title: Dynamic client registration endpoint
description: The client registration endpoint allows developers to dynamically register OAuth clients on a PingFederate authorization server.
component: pingfederate
version: 13.1
page_id: pingfederate:developers_reference_guide:pf_dynamic_registra_endpoint
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/developers_reference_guide/pf_dynamic_registra_endpoint.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  endpoint-asclients-oauth2: "Endpoint: /as/clients.oauth2"
  example-1: Example 1
  example-2: Example 2
  example-3: Example 3
  related-links: Related links
---

# Dynamic client registration endpoint

The client registration endpoint allows developers to dynamically register OAuth clients on a PingFederate authorization server.

The [OAuth 2.0 Dynamic Client Registration Protocol](https://tools.ietf.org/html/rfc7591) defines this endpoint. Developers can send client registrations with the desired properties, such as client metadata, to this endpoint. If the requests are valid, PingFederate evaluates them and returns a response with a client ID and the registered client metadata values.

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | This runtime endpoint is only active when the dynamic registration client is enabled and configured. |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | As dynamic client registration can expose your server to unwanted client registrations, we recommend protecting PingFederate by requiring an initial access token, configuring one or more client registration policies, and protecting access to the dynamic client registration endpoint.You can configure access token requirement and client registration policies using the **System > OAuth Settings > Client Settings** window. To further protect against unauthorized access to the dynamic client registration endpoint, consider using PingAccess or your choice of web access management solution to do so. |

|   |                                                  |
| - | ------------------------------------------------ |
|   | This endpoint accepts only the HTTP POST method. |

## Endpoint: /as/clients.oauth2

Both the request and the response follow the [OAuth 2.0 Dynamic Client Registration Protocol](https://tools.ietf.org/html/rfc7591).

## Example 1

A developer wants to register a client that supports the authorization code flow, two redirection URIs, two scopes, and HTTP Basic as the client authentication method. In this example, PingFederate is not configured to require an initial access token.

* Request

```
POST /as/clients.oauth2 HTTP/1.1
Content-Type: application/json
Accept: application/json
Host: sso.example.com

{
  "client_name":"Example Org Sample One",
  "redirect_uris":[
    "https://example.org/app1",
    "https://example.org/appM"
  ],
  "scope":"email phone",
  "grant_types":[
    "authorization_code"
  ]
}
```

* Response

```
HTTP/1.1 201 Created
Date: Fri, 13 Oct 2017 12:34:56 GMT
Referrer-Policy: origin
Content-Type: application/json
Transfer-Encoding: chunked

{
  "client_id": "dc-F3JxcBlNCtjk36J3Yi4yQK",
  "client_name": "Example Org Sample One",
  "redirect_uris": [
    "https://example.org/app1",
    "https://example.org/appM"
  ],
  "token_endpoint_auth_method": "client_secret_basic",
  "grant_types": [
    "authorization_code"
  ],
  "client_secret": "fYhGUjnkjGp0UPQGaAfdcS",
  "client_secret_expires_at": 0,
  "scope": "phone email",
  "validate_using_all_eligible_atms": false,
  "refresh_token_rolling_policy": "server_default",
  "persistent_grant_expiration_type": "server_default",
  "grant_access_session_revocation_api": false
  "grant_access_session_management_api": false
}
```

PingFederate returns `201 Created`, the client ID, and other registered client metadata after creating the new client.

Additionally, when a registration request does not specify a client authentication method (`token_endpoint_auth_method`), PingFederate defaults to `client_secret_basic` per [OAuth 2.0 Dynamic Client Registration Protocol](https://datatracker.ietf.org/doc/html/rfc7591).

## Example 2

A developer wants to register a client that supports the authorization code flow, refresh tokens, one redirection URI, one `profile` scope, and HTTP Basic as the client authentication method. In this example, PingFederate is not configured to require an initial access token. However, the `profile` scope is restricted. As a result, the registration request should fail.

* Request

```
POST /as/clients.oauth2 HTTP/1.1
Content-Type: application/json
Accept: application/json
Host: www.example.com

{
  "client_name":"Example Org Sample Two",
  "redirect_uris":[
    "https://example.org/app2"
  ],
  "scope":"profile",
  "grant_types":[
    "authorization_code",
    "refresh_token"
  ]
}
```

* Response

```
HTTP/1.1 400 Bad Request
Date: Fri, 13 Oct 2017 13:00:00 GMT
Referrer-Policy: origin
Content-Type: application/json
Transfer-Encoding: chunked
{
  "error": "invalid_client_metadata",
  "error_description": "The requested scope is invalid."
}
```

PingFederate returns `400 Bad Request` and the relevant error message when a client registration fails.

## Example 3

A developer wants to register a client that supports the authorization code flow, two redirection URIs, two scopes, and HTTP Basic as the client authentication method. In this example, PingFederate is configured to require an initial access token.

* Request

```
POST /as/clients.oauth2 HTTP/1.1
Content-Type: application/json
Accept: application/json
Authorization: Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImsxIn0.eyJzY29wZSI6WyJkQ1IiXSwiY2xpZW50X2lkX25hbWUiOiJwYXJ0bmVyRGV2X0FjbWUiLCJhZ2lkIjoiMG44NHV6Nm1mZFJWbzNIWU9VODlrc3FxMTVNR3hxUFMiLCJVc2VybmFtZSI6Ikl2YW4gTW9rIiwiT3JnTmFtZSI6IkFDTUUgRGV2IiwiZXhwIjoxNTA4MzY3MDcyfQ.XfKd8--CHtcQ79Wefz2Sw5GOB5LfV9mWJ0n3vzJ93Ie7wbEAkalIFg53J-9e7s59MjA1igx6ybflGMQ9QAjYobs-jM24arJZZgopEXvcx6IQpyU8U4AMTJ7tr9Lmody8P0QZOKcUDBTT5egv9vr5NuXCtUBfVPhGZ-3p5g5mwrnGHBfqZOAsg7U4hKq8cauKQtVyBBV9iIZNG5Q3ovnxBTclKII9HX-oDhmilbmiga4319YSFfX5-U3li9XPeN3JZB2ukLbTFjjVIVLJIInbSR_IFTWP5Irg92aXLrIfm5MvBp8D1fOU6xYjbgjvw9QKNiFFVD7oEeJG9MwzgcGruw
Host: www.example.com

{
  "client_name":"Example Org Sample Three",
  "redirect_uris":[
    "https://example.org/app3",
    "https://example.org/appN"
  ],
  "scope":"email phone",
  "grant_types":[
    "authorization_code"
  ]
}
```

* Response

```
HTTP/1.1 201 Created
Date: Fri, 13 Oct 2017 15:30:00 GMT
Referrer-Policy: origin
Content-Type: application/json
Transfer-Encoding: chunked

{
  "client_id": "dc-rqUtii4vRXj5NMztkAeJ1S",
  "client_name": "Example Org Sample Three",
  "redirect_uris": [
    "https://example.org/app3",
    "https://example.org/appN"
  ],
  "token_endpoint_auth_method": "client_secret_basic",
  "grant_types": [
    "authorization_code"
  ],
  "client_secret": "p7MD0Ul1DNI9xRDc5kcOxs",
  "client_secret_expires_at": 0,
  "scope": "phone email",
  "validate_using_all_eligible_atms": false,
  "refresh_token_rolling_policy": "server_default",
  "persistent_grant_expiration_type": "server_default",
  "grant_access_session_revocation_api": false
  "grant_access_session_management_api": false
}
```

The registration request must include an `Authorization` HTTP header with a valid access token as its value.

If the authorization fails, PingFederate returns the following JSON payload in the response.

```json
{
  "error": "invalid_access_token",
  "error_description": "Please provide a valid Access Token with the correct scope"
}
```

## Related links

* [Configuring dynamic client registration settings](../administrators_reference_guide/help_clientsettingstasklet_oauthdynamicclientregistrationstate.html)

* [Supported client metadata](../administrators_reference_guide/pf_supp_client_metadata.html)

---

---
title: Enabling certificate-based authentication
description: When client-certificate authentication is enabled, the API calls must be authenticated by X.509 client certificates; otherwise, the administrative API returns an error message.
component: pingfederate
version: 13.1
page_id: pingfederate:developers_reference_guide:pf_enable_cert_based_authen
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/developers_reference_guide/pf_enable_cert_based_authen.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Enabling certificate-based authentication

When client-certificate authentication is enabled, the API calls must be authenticated by X.509 client certificates; otherwise, the administrative API returns an error message.

## About this task

In addition to X.509 client certificate authentication, the corresponding root certificate authority (CA) certificates must either be contained in the Java runtime or be imported into the PingFederate's Trusted CA store. For more information, see [Manage trusted certificate authorities](../administrators_reference_guide/help_certmanagementtasklet_trustedcas_certmanagementstate.html).

The rest of the certificate-based authentication setup, including specifying the Issuer DN of the root CA certificates and the applicable roles of the client certificates, is available through `<pf_install>/pingfederate/bin/cert_auth.properties`. The roles assigned to the certificates affect the results of the API calls.

## Steps

1. Sign on to the administrative console with an account that has the role Crypto Admin.

2. Ensure the client-certificate's root CA and any intermediate CA certificates are contained in the trusted store, either for the Java runtime, or PingFederate, or both.

   |   |                                                                                                                  |
   | - | ---------------------------------------------------------------------------------------------------------------- |
   |   | To import a certificate, click **Trusted CAs** in the Certificate Management section under Server Configuration. |

   |   |                                                                                                     |
   | - | --------------------------------------------------------------------------------------------------- |
   |   | Click the Serial number and copy the Issuer distinguished name (DN) to use in a couple steps later. |

3. Verify the `pf.admin.api.authentication` value in `<pf_install>/pingfederate/bin/run.properties` is set to `cert`. Update as needed.

4. In the `<pf_install>/pingfederate/bin/cert_auth.properties` file, enter the Issuer DN for the client certificate as a value for the property: `rootca.issuer.<x>`, where *\<x>* is a sequential number starting at 1. For more information, see the properties file.

   |   |                                              |
   | - | -------------------------------------------- |
   |   | The configuration values are case-sensitive. |

   If you copied the Issuer DN a couple steps earlier, paste this value.

5. Repeat the previous step for any additional CAs as needed.

6. Enter the certificate's Subject DN for the applicable PingFederate permission roles, as described in the properties file. For information about permissions attached to the PingFederate roles, see the PingFederate User Access Control table in [Configure access to the administrative API](pf_config_access_to_admin_api.html).

   |   |                                              |
   | - | -------------------------------------------- |
   |   | The configuration values are case-sensitive. |

   |   |                                                                                                                                                                                  |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When assigning roles, keep in mind that all client certificates specified in `cert_auth.properties` can be used to access the administrative API and the administrative console. |

7. Repeat the previous step for all client certificates as needed.

8. Restart PingFederate.

   |   |                                                                                                                                   |
   | - | --------------------------------------------------------------------------------------------------------------------------------- |
   |   | In a clustered PingFederate environment, you only need to modify `run.properties` and `cert_auth.properties` on the console node. |

---

---
title: Enabling JWT authorization
description: PingFederate clients can gain access to the administrative API endpoint by providing a JSON Web Token (JWT). The <pf_install>/pingfederate/bin/jwt.properties file contains settings that allow you to configure information required to interact with one or more authorization servers as a client.
component: pingfederate
version: 13.1
page_id: pingfederate:developers_reference_guide:pf_enabling_jwt_authorization
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/developers_reference_guide/pf_enabling_jwt_authorization.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 26, 2026
section_ids:
  steps: Steps
---

# Enabling JWT authorization

PingFederate clients can gain access to the administrative API endpoint by providing a JSON Web Token (JWT) *(tooltip: \<div class="paragraph">
\<p>An IETF standard container format for a JSON object used for the secure exchange of content, such as identity or entitlement information. You can find the industry standard in \<a href="https\://datatracker.ietf.org/doc/html/rfc7519">RFC 7519\</a>.\</p>
\</div>)*. The `<pf_install>/pingfederate/bin/jwt.properties` file contains settings that allow you to configure information required to interact with one or more authorization servers as a client.

|   |                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | `JWT` Admin API authorization currently doesn't support encrypted JWTs. The [OAuth2](pf_enable_oauth20_authoriz.html) authorization method can accept encrypted JWTs. |

## Steps

1. In the `<pf_install>/pingfederate/bin/run.properties` file, set the value of the `pf.admin.api.authentication` property to `JWT`.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can configure PingFederate to support both `JWT` authorization and a basic authentication method by specifying two values separated with a comma. For example, specify `pf.admin.api.authentication=JWT,LDAP`. The basic authentication methods are `native`, `LDAP`, `JWT`, and `RADIUS`. Supporting two authentication methods is helpful when you want to change applications from one method to another. You can find more information about supporting two authentication methods in the description of `pf.admin.api.authentication` in [Configuring PingFederate properties](../administrators_reference_guide/pf_config_pf_propert.html). |

2. In the `<pf_install>/pingfederate/bin/jwt.properties` file, change the property values as needed. You can find instructions and additional information in the comments in the file.

   |   |                                                                                                                                                                                                                                                                                                                          |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Assign at least one of the PingFederate administrative roles, as indicated in the properties file. You can find more information about permissions attached to the PingFederate roles in the PingFederate User Access Control table in [Configure access to the administrative API](pf_config_access_to_admin_api.html). |

3. Restart PingFederate.

   |   |                                                                                                                             |
   | - | --------------------------------------------------------------------------------------------------------------------------- |
   |   | In a clustered PingFederate environment, you only need to modify `run.properties` and `jwt.properties` on the console node. |

---

---
title: Enabling LDAP authentication
description: When the administrative application programming interface (API) is protected by Lightweight Directory Access Protocol (LDAP) authentication, the API calls must be authenticated by valid LDAP credentials over HTTP Basic authentication; otherwise, the administrative API returns an error message.
component: pingfederate
version: 13.1
page_id: pingfederate:developers_reference_guide:pf_enable_ldap_authen
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/developers_reference_guide/pf_enable_ldap_authen.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 24, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Enabling LDAP authentication

When the administrative application programming interface (API) *(tooltip: \<div class="paragraph">
\<p>A specification of interactions available for building software to access an application or service.\</p>
\</div>)* is protected by Lightweight Directory Access Protocol (LDAP) *(tooltip: \<div class="paragraph">
\<p>An open, cross platform protocol used for interacting with directory services.\</p>
\</div>)* authentication, the API calls must be authenticated by valid LDAP credentials over HTTP Basic authentication; otherwise, the administrative API returns an error message.

## About this task

The LDAP authentication setup, including role assignment, is available through `<pf_install>/pingfederate/bin/ldap.properties`. The roles assigned to the LDAP accounts affect the results of the API calls.

|   |                                                                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When you configure LDAP authentication, PingFederate does not lock out accounts based upon the number of failed sign-on attempts. The LDAP server is responsible for preventing access and is enforced according to its password lockout settings. |

## Steps

1. In the `<pf_install>/pingfederate/bin/run.properties` file, set the value of the `pf.admin.api.authentication` property to `LDAP`.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can configure PingFederate to support both `LDAP` authentication and OAuth 2.0 authorization by specifying two values separated with a comma. For example, specify `pf.admin.api.authentication=OAuth2,LDAP`. Supporting two authentication methods is helpful when you want to change applications from one method to another. For more information about supporting two authentication methods, see the description of `pf.admin.api.authentication` in [Configuring PingFederate properties](../administrators_reference_guide/pf_config_pf_propert.html). |

2. In the `<pf_install>/pingfederate/bin/ldap.properties` file, change property values as needed for your network configuration. For instructions and additional information, see the comments in the file.

   |   |                                                                                                                                                                                                                                                                                                                                                                            |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Remember to assign LDAP users or designated LDAP groups, or both, to at least one of the PingFederate administrative roles, as indicated in the properties file. For information about permissions attached to the PingFederate roles, see the PingFederate User Access Control table in [Configure access to the administrative API](pf_config_access_to_admin_api.html). |

   |   |                                                                                                                                                         |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When you assign roles, remember that all LDAP accounts specified in `ldap.properties` can access the administrative API and the administrative console. |

   |   |                                                                                                                                                  |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | You can also use this configuration file in conjunction with RADIUS authentication to determine permissions dynamically with an LDAP connection. |

3. Restart PingFederate.

   |   |                                                                                                                              |
   | - | ---------------------------------------------------------------------------------------------------------------------------- |
   |   | In a clustered PingFederate environment, you only need to modify `run.properties` and `ldap.properties` on the console node. |

---

---
title: Enabling native authentication for the administrative API
description: When the administrative API is protected by native authentication, access to the administrative API is restricted to the users defined in the Account Management window.
component: pingfederate
version: 13.1
page_id: pingfederate:developers_reference_guide:pf_enable_native_auth_for_admin_api
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/developers_reference_guide/pf_enable_native_auth_for_admin_api.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 24, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Enabling native authentication for the administrative API

When the administrative API is protected by native authentication, access to the administrative API is restricted to the users defined in the **Account Management** window.

## About this task

The API calls must be authenticated by valid credentials over HTTP Basic authentication; otherwise, the administrative API returns an error message. The roles assigned to the users affect the results of the API calls.

## Steps

1. In the `<pf_install>/pingfederate/bin/run.properties` file, set the value of the `pf.admin.api.authentication` property to `native`. Then restart PingFederate.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can configure PingFederate to support both `native` authentication and OAuth 2.0 authorization by specifying two values separated with a comma. For example, specify `pf.admin.api.authentication=OAuth2,native`. Supporting two authentication methods is helpful when you want to change applications from one method to another. For more information about supporting two authentication methods, see the description of `pf.admin.api.authentication` in [Configuring PingFederate properties](../administrators_reference_guide/pf_config_pf_propert.html). |

   |   |                                                                                                        |
   | - | ------------------------------------------------------------------------------------------------------ |
   |   | In a clustered PingFederate environment, you only need to modify `run.properties` on the console node. |

2. Sign on to the administrative console with an account that has the User Admin role.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When the administrative console is protected by an alternative console authentication, such as certificate-based, LDAP, or RADIUS authentication, most user-management functions are handled outside the scope of the PingFederate administrative console. Therefore, the administrative console disables the functionality of the **System > Server > Administrative Accounts** window unless the logged-on administrator has been granted User Admin permissions.To create or manage users in this scenario, add at least one external account to the role setting `userAdmin` in the configuration file for the respective authentication method. When the administrator logs on to the administrative console, the **Administrative Accounts** window becomes available to create or manage users for the purposes of accessing the administrative API.For more information about the alternative console authentication and the respective configuration, see [Alternative console authentication](../administrators_reference_guide/pf_alt_console_auth.html). |

3. On the **Administrative Accounts** window, create or manage users as needed, and assign various PingFederate administrative roles as indicated by the PingFederate User Access Control table. For more information, see [Configure access to the administrative API](pf_config_access_to_admin_api.html).

   |   |                                                                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When assigning roles, remember that all users defined in the **Administrative Accounts** window can access the administrative API and the administrative console. |

---

---
title: Enabling OAuth 2.0 authorization
description: PingFederate clients can gain access to the administrative API endpoint by providing an OAuth 2.0 access token. The <pf_install>/pingfederate/bin/oauth2.properties file contains settings that allow you to configure information required to interact with the authorization server as a client.
component: pingfederate
version: 13.1
page_id: pingfederate:developers_reference_guide:pf_enable_oauth20_authoriz
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/developers_reference_guide/pf_enable_oauth20_authoriz.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 24, 2022
section_ids:
  steps: Steps
---

# Enabling OAuth 2.0 authorization

PingFederate clients can gain access to the administrative API endpoint by providing an OAuth 2.0 access token. The `<pf_install>/pingfederate/bin/oauth2.properties` file contains settings that allow you to configure information required to interact with the authorization server as a client.

## Steps

1. In the `<pf_install>/pingfederate/bin/run.properties` file, set the value of the `pf.admin.api.authentication` property to `OAuth2`.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can also configure PingFederate to support both `OAuth2` authorization and a basic authentication method by specifying two values separated with a comma. For example, specify `pf.admin.api.authentication=OAuth2,LDAP`. The basic authentication methods are `native`, `LDAP`, and `RADIUS`. Supporting two authentication methods is helpful when you want to change applications from one method to another. For more information about supporting two authentication methods, see the description of `pf.admin.api.authentication` in [Configuring PingFederate properties](../administrators_reference_guide/pf_config_pf_propert.html). |

2. In the `<pf_install>/pingfederate/bin/oauth2.properties` file, change property values as needed. For instructions and additional information, see the comments in the file.

   |   |                                                                                                                                                                                                                                                                                                                          |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Remember to assign at least one of the PingFederate administrative roles, as indicated in the properties file. For information about permissions attached to the PingFederate roles, see the PingFederate User Access Control table in [Configure access to the administrative API](pf_config_access_to_admin_api.html). |

3. Restart PingFederate.

   |   |                                                                                                                                |
   | - | ------------------------------------------------------------------------------------------------------------------------------ |
   |   | In a clustered PingFederate environment, you only need to modify `run.properties` and `oauth2.properties` on the console node. |