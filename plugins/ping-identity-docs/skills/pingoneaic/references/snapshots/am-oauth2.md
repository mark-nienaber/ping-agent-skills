---
title: Access tokens
description: Customize OAuth 2.0 access tokens by modifying key-value pairs before access management issues them
component: pingoneaic
page_id: pingoneaic:am-oauth2:modifying-access-tokens-scripts
canonical_url: https://docs.pingidentity.com/pingoneaic/am-oauth2/modifying-access-tokens-scripts.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "Customization", "Scripting", "Plugins"]
page_aliases: ["oauth2-guide:plugins-access-token-modifier.adoc", "am-oauth2:plugins-access-token-modifier.adoc"]
section_ids:
  constraints: Constraints
  examples: Examples
  example-atm-legacy: Add profile data to access token (legacy script)
  update-profile-data: Prepare the resource owner profile
  prepare-atm-legacy: Create the script
  create-client-legacy: Use the script
  test-atm-legacy: Test the script
  example-atm-nextgen: Add external data to access token (next-generation script)
  create-resource-owner: Create the resource owner profile
  prepare-atm-nextgen: Create the script
  configure-atm-nextgen: Use the script
  test-atm-nextgen: Test the script
  use_a_validated_script: Use a validated script
---

# Access tokens

Use this extension point to modify the key-value pairs in an OAuth 2.0 access token before Advanced Identity Cloud issues it.

* Template script

  [OAuth2 Access Token Modification Script](../am-scripting/sample-scripts.html#oauth2-access-token-modification-js)

* Script bindings

  [Access token modification scripting API](../am-scripting/access-token-modification-api.html)

The examples on this page use a script to add data to an access token.

## Constraints

You can modify both [client-side](client-side-tokens.html) and [server-side](server-side-tokens.html) access tokens. You can also modify [macaroons](oauth2-macaroons.html) used in place of regular tokens.

Advanced Identity Cloud stores the modifications in client-side and server-side access tokens. When issuing modified access tokens, consider the following constraints:

* Removing or changing native properties may render the access token unusable.

  Advanced Identity Cloud relies on native properties that it includes in the access token. If you remove or modify those properties, Advanced Identity Cloud considers the access token invalid. This can cause the OAuth 2.0 flows to break.

* Modifying access tokens can significantly increase the size of the token.

  Adding key-value pairs to OAuth 2.0 access tokens affects the size of client-side JSON web tokens (JWT), or the size of server-side tokens, if enabled.

  Make sure the modified tokens fit within your client and user-agent size limits.

Learn more in [Token storage](token-storage.html).

## Examples

The following examples use JavaScript in either a legacy or next-generation scripting environment to modify the access token.

* [Add profile data to access token (legacy script)](#example-atm-legacy)

* [Add external data to access token (next-generation script)](#example-atm-nextgen)

### Add profile data to access token (legacy script)

Complete the following steps to implement a custom access token modification script to set additional properties in the access token:

1. [Prepare the resource owner profile](#update-profile-data)

2. [Create the script](#prepare-atm-legacy)

3. [Use the script](#create-client-legacy)

4. [Test the script](#test-atm-legacy)

#### Prepare the resource owner profile

An OAuth 2.0 client requests the access token on behalf of a resource owner.

The script requires that the authenticated resource owner has an email address and telephone number in their profile.

The script adds the values of these fields to the access token.

1. [Create a resource owner profile](../identities/manage-identities.html#create-a-user-profile) and record the username and password.

2. Update the following settings in the new user profile and save your work:

   * Email Address

     `user@example.com`

   * Telephone Number

     `(555) 323-1234`

#### Create the script

1. In the Advanced Identity Cloud admin console, [create a script](../developer-docs/scripting-auth.html#create-a-new-auth-script) of type OAuth2 Access Token Modification.

2. Select Legacy as the script engine.

3. Enter a name for your script and save your changes.

4. Replace the default JavaScript with the following script:

   ```javascript
   (function () {
     // Add a field next to the access token in the /oauth2/access_token response.
     accessToken.addExtraData('hello', 'world');

     // Add identity profile attribute values to the /oauth2/introspect response.
     if (identity != null) {
       accessToken.setField('mail', identity.getAttribute('mail'));
       accessToken.setField('phone', identity.getAttribute('telephoneNumber').toArray()[0]);
     }

     // No return value is expected.
   }());
   ```

   The `accessToken` methods update the access token before Advanced Identity Cloud issues it.

   The `identity` methods get attribute values from the resource owner's profile.

   |   |                                                                                                                                                                                                                                                                             |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The `identity` binding is `null` if the resource owner doesn't exist in Advanced Identity Cloud, such as when a JWT bearer grant references an unknown subject.Learn more in [Access token modification scripting API](../am-scripting/access-token-modification-api.html). |

#### Use the script

The OAuth 2.0 client profile in this example overrides the OAuth 2.0 provider settings. This lets you test the script without affecting access tokens issued to other clients.

1. [Create an OIDC/ OAuth 2.0 web client application](../app-management/register-a-custom-application.html) with the following settings:

   * Name and Client ID

     `myClient`

   * Client Secret

     `mySecret`

   * Sign-in URLs

     `https://www.example.com:443/callback`

   * Scopes

     `access`

2. [Override OAuth 2.0 provider settings](plugins-customize.html#override-oauth2-provider-settings) for this client with the access token modification values.

#### Test the script

The example uses the [Authorization code grant](oauth2-authz-grant.html) flow:

* The resource owner authenticates to obtain an SSO token.

* The client relies on Implied Consent being enabled (default). It assumes the resource owner grants the client access.

* The client requests the authorization code and exchanges it for an access token your script modified.

* The client introspects the access token.

* The client requests the authorization code and exchanges it for an access token that's modified by your script. Follow these steps:

  1. [Get an authorization code](oauth2-authz-grant.html#proc-auth-code-browser) using the values configured for `myClient` and the resource owner's login credentials.

  2. [Exchange the authorization code for an access token](oauth2-authz-grant.html#proc-auth-code-token) providing the authorization code and the values for `myClient`.

     For example:

     ```bash
     curl \
     --request POST \
     --user 'myClient:mySecret' \
     --data 'grant_type=authorization_code' \
     --data 'code=<authorization-code>' \
     --data 'redirect_uri=https://www.example.com:443/callback' \
     'https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/access_token'
     {
       "access_token": "<access-token>",
       "refresh_token": "<refresh-token>",
       "scope": "access",
       "hello": "world",
       "token_type": "Bearer",
       "expires_in": 3599
     }
     ```

  The script added `"hello": "world"` alongside the access token in the [/oauth2/access_token](oauth2-access_token-endpoint.html) response.

  1. Make an HTTP call to [/oauth2/introspect](oauth2-introspect-endpoint.html) to verify that the access token includes the values for `mail` and `phone` from the resource owner's profile.

     For example:

     ```bash
     curl \
     --request POST \
     --user 'myClient:mySecret' \
     --data 'token=<access-token>' \
     'https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/introspect'
     {
       …​
       "mail": ["user@example.com"],
       "phone": "(555) 323-1234"
       …​
     }
     ```

### Add external data to access token (next-generation script)

Complete the following steps to implement a custom access token modification script to set additional properties in the access token:

1. [Create the resource owner profile](#create-resource-owner)

2. [Create the script](#prepare-atm-nextgen)

3. [Use the script](#configure-atm-nextgen)

4. [Test the script](#test-atm-nextgen)

#### Create the resource owner profile

An OAuth 2.0 client requests the access token on behalf of a resource owner.

1. [Create a resource owner profile](../identities/manage-identities.html#create-a-user-profile) and record the username and password.

#### Create the script

Write a script that does the following:

* Calls an external API to set values for browser and IP in the access token

* Sets a new expiry time in the access token and in the resource owner's profile data

* Generates random UUIDs to return in the JSON response

1. In the Advanced Identity Cloud admin console, [create a script](../developer-docs/scripting-auth.html#create-a-new-auth-script) of type OAuth2 Access Token Modification.

2. Leave Next Generation selected on the Choose Script Engine page.

3. Enter a name for your script.

4. Replace the default JavaScript with the following script:

   ```java
   // use httpclient to call external API
   var options = {
     method: "GET",
     headers: {
       "Content-Type": "application/json; charset=UTF-8"
     }
   };
   var response = httpClient.send("https://dummyjson.com/ip", options).get();
   if (response.status === 200) {
   	var ipInfo = response.json();
     // add values to the token
     accessToken.setField("browser", ipInfo.userAgent);
     accessToken.setField('ip', ipInfo.ip);

   } else {
     logger.error("Error getting IP and browser info: " + response.statusText);
   }

   // set a shorter expiry time
   var newExpiry = Date.now() + 300000;
   accessToken.setExpiryTime(newExpiry);

   // update profile data using the openidm binding
   var userID = identity.getAttributeValues("_id")[0];
   var user = openidm.read("managed/alpha_user/" + userID);
   user.description = "New access token expiry time: " + newExpiry;
   var updatedUser = openidm.update("managed/alpha_user/" + userID, null, user);

   // use utils binding to get random values
   var uids = [0,0,0];
   utils.crypto.getRandomValues(uids);

   // add values to be returned in the JSON response
   accessToken.addExtraJsonData('uids', uids);
   ```

   |   |                                                                                                                                                                                                                                                                                                                                                |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can find information about the common bindings such as `httpClient` and `utils` in [Common bindings](../am-scripting/script-bindings.html).You can find information about the bindings specific to access token modification scripts in the [Access token modification scripting API](../am-scripting/access-token-modification-api.html). |

5. Save your changes.

#### Use the script

The OAuth 2.0 client profile in this example overrides the OAuth 2.0 provider settings. This lets you test the script without affecting access tokens issued to other clients.

1. [Create an OIDC/ OAuth 2.0 web client application](../app-management/register-a-custom-application.html) with the following settings:

   * Name and Client ID

     `myClient`

   * Client Secret

     `mySecret`

   * Sign-in URLs

     `https://www.example.com:443/callback`

   * Scopes

     `access`

2. [Override OAuth 2.0 provider settings](plugins-customize.html#override-oauth2-provider-settings) for this client with the access token modification values.

#### Test the script

The example uses the [Authorization code grant](oauth2-authz-grant.html) flow:

* The resource owner authenticates to obtain an SSO token.

* The client relies on Implied Consent being enabled (default). It assumes the resource owner grants the client access.

* The client requests the authorization code and exchanges it for an access token your script modified.

* The client introspects the access token.

* The client requests the authorization code and exchanges it for an access token that's modified by your script. Follow these steps:

  1. [Get an authorization code](oauth2-authz-grant.html#proc-auth-code-browser) using the values configured for `myClient` and the resource owner's login credentials.

  2. [Exchange the authorization code for an access token](oauth2-authz-grant.html#proc-auth-code-token) providing the authorization code and the values for `myClient`.

     The response includes the JSON data (`uuids`) added by the script and the updated expiry time:

     ```json
     {
         "access_token": "anmKKgqxNkTMMGVRF2aOR3D2cCc",
         "uids": [
               841804401,
               732387389,
               290315868
           ],
         "scope": "access",
         "token_type": "Bearer",
         "expires_in": 299
         ]
     }
     ```

  3. Make an HTTP call [/oauth2/introspect](oauth2-introspect-endpoint.html) to verify that the access token includes the modified values for `browser`, `ip`, and `exp`. For example:

     ```json
     {
         {
             "active": true,
             "scope": "access",
             "realm": "/alpha",
             "client_id": "myClient",
             "user_id": "bjensen",
             ...
             "exp": 1755108160,
             "browser": "Apache-HttpAsyncClient/4.1.4 (Java/17.0.10)",
             "ip": "1.70.145.10"
         }
     }
     ```

## Use a validated script

Test your access token modification scripts as you did in the examples.

After validating your script by overriding the OAuth 2.0 provider settings with a test client, you can update Advanced Identity Cloud to use your script in one of the following ways:

* [Configure the OAuth 2.0 provider](plugins-customize.html#use-custom-oauth2-plugin) with the access token modification extension settings.

* In the Advanced Identity Cloud admin console, select [icon: code, set=material, size=inline] Extensions > Scripts > OAuth2 Access Token Modification Script, and replace the script content with your validated script.

---

---
title: Advanced Identity Cloud as authorization server
description: Understand how Advanced Identity Cloud functions as an OAuth 2.0 authorization server
component: pingoneaic
page_id: pingoneaic:am-oauth2:am-as-authz-server
canonical_url: https://docs.pingidentity.com/pingoneaic/am-oauth2/am-as-authz-server.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "OAuth 2.0", "Federation"]
page_aliases: ["oauth2-guide:openam-oauth2-authz-server.adoc", "oauth2-guide:am-as-authz-server.adoc"]
section_ids:
  oauth2-introduction: OAuth 2.0 concepts
  supported_oauth_2_0_features: Supported OAuth 2.0 features
  oauth2-security-considerations: Security considerations
---

# Advanced Identity Cloud as authorization server

As an authorization server, Advanced Identity Cloud *authenticates* resource owners and obtains their *authorization* to return access tokens to clients.

Before you configure OAuth 2.0 in your environment, familiarize yourself with the [OAuth 2.0 authorization framework](https://www.rfc-editor.org/info/rfc6749) and related standards.

## OAuth 2.0 concepts

RFC 6749, the [OAuth 2.0 authorization framework](https://www.rfc-editor.org/info/rfc6749) lets a third-party application obtain limited access to a resource (usually user data) on behalf of the resource owner or the application itself.

The main actors in the OAuth 2.0 authorization framework are the following:

**OAuth 2.0 framework actors**

| Actor                         | Description                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Resource owner (RO)**       | The owner of the resource. For example, a user who stores their photos in a photo-sharing service.The resource owner uses a *user-agent*, usually a web-browser, to communicate with the client.                                                                                                                                                             |
| **Client**                    | The third-party application that wants to access the resource. The client makes requests on behalf of the resource owner and with their authorization. For example, a printing service that needs to access the resource owner's photos to print them.Advanced Identity Cloud can act as a client.                                                           |
| **Authorization server (AS)** | The authorization service that authenticates the resource owner and/or the client, issues access tokens to the client, and tracks their validity. Access tokens prove that the resource owner authorizes the client to act on their behalf over specific resources for a limited period of time.Advanced Identity Cloud can act as the authorization server. |
| **Resource server (RS)**      | The service hosting the protected resources. For example, a photo-sharing service. The resource server must be able to validate the tokens issued by the authorization server.A website protected by a web or a Java agent can act as the resource server.                                                                                                   |

The following sequence diagram demonstrates the basic OAuth 2.0 flow:

![Advanced Identity Cloud can function as the authorization server and also as the client.](_images/oauth2-flow.svg)Figure 1. OAuth 2.0 protocol flow

To use Advanced Identity Cloud as an authorization server, register an OAuth 2.0 application (client) in the Advanced Identity Cloud admin console. Clients can also register themselves [dynamically](../am-oidc1/oauth2-dynamic-client-registration.html).

## Supported OAuth 2.0 features

As an authorization server, Advanced Identity Cloud supports the following features:

**OAuth 2.0 features**

| Feature                                                    | Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Grant types](oauth2-implementing-flows.html)              | * Authorization code

* Implicit

* Resource owner password credentials

* Client credentials

* Device flow

* SAML 2.0 profile for authorization grant

* JWT profile for OAuth 2.0 authorization grants                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Client authentication standards](oauth2-client-auth.html) | - JWT profile for OAuth 2.0 client authentication

- Mutual TLS                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Other OAuth 2.0 standards                                  | * [JWT proof-of-possession](oauth2-PoP-JWK.html)

* [OpenID Connect](../am-oidc1/preface.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Remote consent services](oauth2-remote-consent.html)      | Delegates the consent-gathering part of an OAuth 2.0 flow to a separate service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Customizable scope grants                                  | You can customize how scopes are granted to the client, regardless of the grant flow used.Advanced Identity Cloud can grant scopes statically or dynamically:* Statically (default)

  Configure several OAuth 2.0 clients with different subsets of scopes. Resource owners are redirected to a specific client, depending on the scopes required. As long as the resource owner can authenticate and the client can deliver the same or a subset of the requested scopes, Advanced Identity Cloud issues the token with the scopes requested. Two different users requesting scopes A and B from the same client will always receive scopes A and B.

* Dynamically

  Configure an OAuth 2.0 client with a comprehensive list of scopes. Resource owners authenticate against that client. When Advanced Identity Cloud receives a request for scopes, the authorization service grants or denies access scopes dynamically by evaluating authorization policies. Two different users requesting scopes A and B from the same client can receive different scopes, based on policy conditions.

  For details, refer to [Authorization and policy decisions](../am-authorization/what-is-authz-decision.html) and [Dynamic OAuth 2.0 authorization](../am-authorization/oauth2-authorization.html). |

## Security considerations

|   |                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | OAuth 2.0 messages involve credentials and access tokens that allow the bearer to retrieve protected resources. You must protect the messages going across the network and prevent attackers from capturing requests or responses. |

RFC 6749 includes a number of [security considerations](https://www.rfc-editor.org/rfc/rfc6749.html#section-10) and requires Transport Layer Security (TLS) to protect sensitive messages. Make sure you read these security considerations and implement them in your deployment.

When you are deploying a combination of other clients and resource servers, pay special attention to the [OAuth 2.0 threat model and security considerations](https://www.rfc-editor.org/info/rfc6819) before putting your service into production.

---

---
title: Advanced Identity Cloud as client and resource server
description: Configure Advanced Identity Cloud to function as both OAuth 2.0 client and resource server
component: pingoneaic
page_id: pingoneaic:am-oauth2:openam-oauth2-client
canonical_url: https://docs.pingidentity.com/pingoneaic/am-oauth2/openam-oauth2-client.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "Clients", "Authorization", "Setup &amp; Configuration"]
page_aliases: ["oauth2-guide:openam-oauth2-client.adoc"]
---

# Advanced Identity Cloud as client and resource server

When Advanced Identity Cloud functions as an OAuth 2.0 client, it provides a session after successfully authenticating the resource owner and obtaining authorization. The client can then access resources protected by agents.

To configure Advanced Identity Cloud as an OAuth 2.0 client, use the [Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/latest/social-provider-handler.html) node as part of the authentication journey.

This sequence diagram shows how the client gains access to protected resources where Advanced Identity Cloud functions as both authorization server and client:

![Advanced Identity Cloud as client, where authentication and authorization are handled by the authorization server. On success, an SSO session is created, so that Advanced Identity Cloud access management can happen as it normally does.](_images/oauth2-openam-client.svg)Figure 1. OAuth 2.0 client and authorization server

Because the OAuth 2.0 client functionality is implemented as an Advanced Identity Cloud authentication node, you do not need to deploy your own resource server implementation when using Advanced Identity Cloud as an OAuth 2.0 client. Use web or Java agents or PingGateway to protect resources.

Find more information on configuring Advanced Identity Cloud as an OAuth 2.0 client in [Social authentication](../authentication/social-authentication.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To use your own client and resource server, make sure the resource server implements the logic for handling access tokens and [refresh tokens](oauth2-refresh-tokens.html).The resource server can use the `/oauth2/introspect` endpoint to determine whether the access token is still valid, and to retrieve the scopes associated with the access token.To design your own scopes implementation, refer to [Customize OAuth 2.0 using JavaScript extensions](plugins-customize.html). |

---

---
title: Authorization code grant
description: Use authorization code grant flow to exchange authorization codes for access tokens
component: pingoneaic
page_id: pingoneaic:am-oauth2:oauth2-authz-grant
canonical_url: https://docs.pingidentity.com/pingoneaic/am-oauth2/oauth2-authz-grant.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "OpenID Connect (OIDC)", "Endpoints", "Authorization", "Grant Flow", "REST API"]
page_aliases: ["oidc1-guide:openid-connect-authorization-code-flow.adoc", "oauth2-guide:oauth2-authz-grant.adoc"]
section_ids:
  the_authorization_code_grant_flow: The authorization code grant flow
  oauth_2_0: OAuth 2.0
  oidc: OIDC
  oauth2-authz-demo: Demonstrate the authorization code grant flow
  prepare-demo: Prepare the demonstration
  proc-auth-code-browser: Get an authorization code using a browser
  proc-auth-code-no-browser: Get an authorization code using REST
  proc-auth-code-token: Exchange an authorization code for an access token
  additional_oidc_claims: Additional OIDC claims
---

# Authorization code grant

* Endpoints

  * [/oauth2/authorize](oauth2-authorize-endpoint.html)

  * [/oauth2/access_token](oauth2-access_token-endpoint.html)

  * [/oauth2/userinfo](../am-oidc1/rest-api-oidc-userinfo-endpoint.html) (OpenID Connect \[OIDC])

The authorization code grant flow for OAuth 2.0 and OIDC lets a confidential client, such as a web application running on a server, exchange an authorization code for an access token to get authorized access to protected resources.

The authorization code grant is secure because:

* It is a two-step process:

  1. The resource owner authenticates to the authorization server and authorizes the client to access the protected resource. As confirmation, the client receives a temporary authorization code from the server.

  2. The authorization server validates the authorization code and exchanges it for an access token.

* The authorization server delivers the access token directly to the client, usually over HTTPS. Neither the access token nor the client secret is exposed publicly, which protects confidential clients.

## The authorization code grant flow

### OAuth 2.0

![Advanced Identity Cloud supports the authorization code grant flow.](_images/oauth2-authz.svg)

1. The client, usually a web-based service, receives a request to access a protected resource. To access the resource, the client requires authorization from the resource owner.

2. The client redirects the resource owner's user-agent to the authorization server.

3. The authorization server authenticates the resource owner, confirms resource access, and gathers consent if required.

4. The authorization server redirects the resource owner's user agent to the client.

5. During the redirection process, the authorization server appends an authorization code.

6. The client receives the authorization code and authenticates to the authorization server to exchange the code for an access token.

   Note that this example assumes a confidential client. Public clients are not required to authenticate.

7. If the authorization code is valid, the authorization server returns an access token (and a refresh token, if configured) to the client.

8. The client requests access to the protected resource from the resource server.

9. The resource server contacts the authorization server to validate the access token.

10. The authorization server validates the token and responds to the resource server.

11. If the token is valid, the resource server lets the client access the protected resource.

### OIDC

![Advanced Identity Cloud supports the OpenID Connect authorization code grant flow.](_images/oidc-authz.svg)

1. The end user wants to use the services provided by the relying party (RP). The RP, usually a web-based service, requires an account to provide those services.

   The end user issues a request to share their information with the RP.

2. To access the end user's information in the OpenID provider (OP), the RP requires end user consent.

   The RP redirects the end user's user-agent...

3. ...to the OP.

4. The OP authenticates the end user, confirms resource access, and gathers consent if necessary.

5. The OP redirects the end user's user-agent to the RP.

6. During the redirection process, the OP appends an authorization code.

7. The RP authenticates to the OP and exchanges the authorization code for an access token and an ID token.

   Note that this example assumes a confidential client. Public clients are not required to authenticate.

8. If the authorization code is valid, the OP returns an access token and an ID token to the RP.

9. The RP validates the ID token and its claims.

   The RP can use the ID token subject ID claim as the end user's identity.

10. If the RP requires additional claims, it sends a request to the [/oauth2/userinfo](../am-oidc1/rest-api-oidc-userinfo-endpoint.html) endpoint with the access token for authorization.

11. If the access token is valid, the `/oauth2/userinfo` endpoint returns any additional claims.

    The RP can use the subject ID and the additional claims to identify the end user.

## Demonstrate the authorization code grant flow

Perform these steps to get an authorization code and exchange it for an access token:

1. [Prepare the demonstration](#prepare-demo)

2. [Get an authorization code using a browser](#proc-auth-code-browser) or [Get an authorization code using REST](#proc-auth-code-no-browser)

3. [Exchange an authorization code for an access token](#proc-auth-code-token)

### Prepare the demonstration

Complete these steps to prepare the authorization code grant flow demonstration:

1. [Create an application owner profile](../identities/manage-identities.html#create-a-user-profile) and record the username and password.

2. [Register a client application](../app-management/register-a-custom-application.html).

   1. In the Advanced Identity Cloud admin console, go to Applications > Applications and select + Custom Application.

   2. Select the sign-in method as OIDC - OpenId Connect and application type as Web.

   3. Create the application, providing the following details:

      * Name

        `myClient`

      * Owners

        `<application-owner>`

      * Client ID

        `myClient`

      * Client Secret

        `mySecret`

   4. Switch to the Sign On tab and under General Settings, set these fields to have the following values:

      * Sign-in URLs

        `https://www.example.com:443/callback`

      * Scopes

        `write` (for OAuth 2.0)\
        `openid` and `profile` (for OIDC)

   5. Save your changes.

3. [Create a resource owner profile](../identities/manage-identities.html#create-a-user-profile) and record the username and password.

### Get an authorization code using a browser

1. The client redirects the resource owner's user-agent to the authorization server's [/oauth2/authorize](oauth2-authorize-endpoint.html) endpoint, including the following query parameters:

   * **`client_id`**: `myClient`

   * **`response_type`**: `code`

   * **`scope`**: `write` (OAuth 2.0); `openid` and `profile` (OIDC)

   * **`redirect_uri`**: `https://www.example.com:443/callback`

   ```none
   https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/authorize
   ?client_id=myClient
   &response_type=code
   &scope=write
   &state=abc123
   &redirect_uri=https://www.example.com:443/callback
   ```

   For OIDC, set `scope=openid profile` instead.

   |   |                                                                                                                                                                                                                                                                 |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The URL is split and spaces added for readability purposes.The `scope` parameter is optional if default values are configured in the authorization server or the client.The `state` parameter is included to protect against CSRF attacks but is also optional. |

2. The resource owner authenticates to the authorization server. In this demonstration, they sign in using the default journey configured for the realm.

   |   |                                                                                                                                                                                                                                                                                                                                                             |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | By default, client applications in Advanced Identity Cloud use [implied consent](oauth2-manage-consent.html#skip-consent). If Advanced Identity Cloud is configured to require explicit consent, the authorization server presents the resource owner with a consent screen. To continue the flow, the resource owner must select `Allow` to grant consent. |

   The authorization server redirects the resource owner to the URL specified in the `redirect_uri` parameter.

3. Inspect the URL in the browser.

   It contains a `code` parameter with the authorization code issued by the authorization server.

   For example:

   `https://www.example.com/callback?code=<authorization-code>&iss...`

4. Follow the steps to [get an access token](#proc-auth-code-token).

### Get an authorization code using REST

1. [Authenticate](../am-authentication/authn-rest.html) as the resource owner.

   For example:

   ```bash
   $ curl \
   --request POST \
   --header 'Content-Type: application/json' \
   --header 'X-OpenAM-Username: <resource-owner-username>' \
   --header 'X-OpenAM-Password: <resource-owner-password>' \
   --header "Accept-API-Version: resource=2.0, protocol=1.0" \
   'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate'
   {
     "tokenId": "<tokenId>",
     "successUrl": "/enduser/?realm=/alpha",
     "realm": "/alpha"
   }
   ```

2. As the client, call the [/oauth2/authorize](oauth2-authorize-endpoint.html) endpoint to request the authorization code. Provide the resource owner's SSO token in a cookie and the following parameters:

   * **`scope`**: `write` (OAuth 2.0); `openid` and `profile` (OIDC)

   * **`response_type`**: `code`

   * **`client_id`**: `myClient`

   * **`csrf`**: `<tokenId>`

   * **`redirect_uri`**: `https://www.example.com:443/callback`

   * **`decision`**: `allow`

     For example:

     ```bash
     $ curl --dump-header - \
     --request POST \
     --cookie "<session-cookie-name>=<tokenId>" \
     --data "scope=write" \
     --data "response_type=code" \
     --data "client_id=myClient" \
     --data "csrf=<tokenId>" \
     --data "redirect_uri=https://www.example.com:443/callback" \
     --data "state=abc123" \
     --data "decision=allow" \
     "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/authorize"
     ```

     For OIDC, set `scope=openid profile` instead.

     |   |                                                                                                                                                                                                      |
     | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | The `scope` parameter is optional if default values are configured in the authorization server or the client.The `state` parameter is included to protect against CSRF attacks but is also optional. |

     If the authorization server is able to authenticate the user and the client, it returns an HTTP 302 response with the authorization code appended to the redirection URL:

     ```bash
     HTTP/2 302
     ...
     location: https://www.example.com:443/callback?code=<authorization-code>&iss=https%3A%2F%2Fam.example.com%3A8443%2Fam%2Foauth2%2Frealms%2Froot%2Frealms%2Falpha&state=abc123&client_id=myClient
     ...
     ```

3. Follow the steps to [get an access token](#proc-auth-code-token).

### Exchange an authorization code for an access token

As the client, call the [/oauth2/access_token](oauth2-access_token-endpoint.html) endpoint to exchange the authorization code for an access token. Provide the following parameters:

* **Authentication credentials**: `myClient:mySecret`

* **`grant_type`**: `authorization_code`

* **`code`**: `<authorization-code>`

* **`redirect_uri`**: `https://www.example.com:443/callback`

  For example:

  ```bash
  $ curl \
  --request POST \
  --user 'myClient:mySecret' \
  --data "grant_type=authorization_code" \
  --data "code=<authorization-code>" \
  --data "redirect_uri=https://www.example.com:443/callback" \
  "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/access_token"
  ```

  |   |                                                                                                                                                                                                                                                                                                                  |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | This example uses `--user '<client_id>:<client_secret>'` to authenticate the client, the default for Advanced Identity Cloud OAuth 2.0 client applications.For information about the different ways to authenticate confidential clients, refer to [Client application authentication](oauth2-client-auth.html). |

  The `redirect_uri` and client parameters must match those used for the authorization code request, or the authorization server will not validate the code.

  For OAuth 2.0, the authorization server returns an access token; for example:

  ```json
  {
    "access_token": "<access-token>",
    "refresh_token": "<refresh-token>",
    "scope": "write",
    "token_type": "Bearer",
    "expires_in": 3599
  }
  ```

  For OIDC, the OP returns an access token and an ID token; for example:

  ```json
  {
    "access_token": "<access-token>",
    "refresh_token": "<refresh-token>",
    "scope": "openid profile",
    "id_token": "<id-token>",
    "token_type": "Bearer",
    "expires_in": 3599
  }
  ```

  If the RP does not require the access token, [revoke it](oauth2-token-revoke-endpoint.html).

  By default, Advanced Identity Cloud also issues a [refresh token](oauth2-refresh-tokens.html) whenever it issues access tokens.

## Additional OIDC claims

An RP can request additional claims about the end user with the access token at the [/oauth2/userinfo](../am-oidc1/rest-api-oidc-userinfo-endpoint.html) endpoint:

```bash
$ curl \
--request GET \
--header "Authorization Bearer <access-token>" \
"https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/userinfo"
{
  "name": "<resource-owner-display-name>",
  "family_name": "<resource-owner-family-name>",
  "given_name": "<resource-owner-given-name>",
  "sub": "<resource-owner-id>",
  "subname": "<resource-owner-id>"
}
```

---

---
title: Authorization code grant with PAR
description: Use pushed authorization requests with authorization code grant for enhanced security
component: pingoneaic
page_id: pingoneaic:am-oauth2:oauth2-authz-grant-par
canonical_url: https://docs.pingidentity.com/pingoneaic/am-oauth2/oauth2-authz-grant-par.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "Endpoints", "Authorization", "JWT", "Grant Flow", "PAR", "REST API"]
page_aliases: ["oauth2-guide:oauth2-authz-grant-par.adoc"]
section_ids:
  oauth2-authz-par-flow: The authorization code grant with PAR flow
  oauth2-authz-par-demo: Demonstrate the authorization code grant with PAR flow
  prepare-par-demo: Prepare the demonstration
  proc-par-requesturi: Get a PAR request URI
  proc-par-browser: Get an authorization code using a browser
  proc-par-no-browser: Get an authorization code using REST
  proc-par-token: Exchange an authorization code for an access token
---

# Authorization code grant with PAR

* Endpoints

  * [/oauth2/par](oauth2-par-endpoint.html)

  * [/oauth2/authorize](oauth2-authorize-endpoint.html)

  * [/oauth2/access_token](oauth2-access_token-endpoint.html)

The pushed authorization request (PAR) endpoint provides enhanced security and cryptographic integrity when used with the authorization code grant flow, and optionally, in conjunction with PKCE.

PAR lets the authorization server authenticate the client before making an authorization request to enable early detection of invalid or illegal requests.

To further protect authorization details when passing through third-party applications, clients can use JWT-based request objects as defined by [RFC9101](https://datatracker.ietf.org/doc/html/rfc9101), to wrap confidential and potentially complex request parameters.

In response to this pre-authorization backchannel request, the client receives a request URI that's used to reference the payload data in subsequent interactions with the server.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | * PAR is optional by default. To *enforce* the use of the PAR endpoint to initiate authorization requests, enable Require Pushed Authorization Requests under Native Consoles > Access Management:

  * To force all clients in a realm to use PAR, [enable the setting](../am-reference/services-configuration.html#require-par) on the OAuth 2.0 provider's Advanced tab.

  * To force an individual client to use PAR, go to Realms > *Realm Name* > Applications > OAuth 2.0 > Clients > *Client ID* and enable the setting on the Advanced tab.

* The [PAR](https://www.rfc-editor.org/rfc/rfc9126.html) and [JAR](https://www.rfc-editor.org/rfc/rfc9101.html#section-5.2) specifications indicate the following:

  * The authorization server should ignore authorize parameters outside the `request_uri`.

  * When sending a JWT-Secured Authorization Request (JAR), the `request_uri` *must* be an `https` URI.

  To enforce this behavior in Advanced Identity Cloud, [create an ESV variable](../tenants/esvs.html#variables) named `esv.oauth2.request.object.restrictions.enforced` and set its value to `true`. |

## The authorization code grant with PAR flow

![Advanced Identity Cloud supports the authorization code grant flow with PAR.](_images/oauth2-authz-par.svg)Figure 1. OAuth 2.0 authorization code grant with PAR flow

1. The client pushes a request to the PAR endpoint, providing both client and request details.

2. Advanced Identity Cloud validates both client and request, and if successful, returns a request URI as a reference to the request payload and an expiry period for the request URI.

3. The client receives a request to access a protected resource. To access the resource, the client requires authorization from the resource owner.

4. The client redirects the resource owner's user-agent to Advanced Identity Cloud, the authorization server.

5. Advanced Identity Cloud authenticates the resource owner, confirms resource access, and gathers consent if not previously saved.

6. The client requests an authorization code, typically through a web browser, by passing in the `request_uri` and `client_id`.

7. Advanced Identity Cloud validates the `client_id` against the request and, if successful, returns the authorization code to the client.

8. The client authenticates to Advanced Identity Cloud using the received code in exchange for an access token.

   |   |                                                                                             |
   | - | ------------------------------------------------------------------------------------------- |
   |   | This example assumes a confidential client. Public clients aren't required to authenticate. |

9. If the authorization code is valid, Advanced Identity Cloud returns an access token (and a refresh token, if configured) to the client.

10. The client requests access to the protected resources from the resource server.

11. The resource server contacts Advanced Identity Cloud to validate the access token.

12. Advanced Identity Cloud validates the token and responds to the resource server.

13. If the token is valid, the resource server allows the client to access the protected resource.

## Demonstrate the authorization code grant with PAR flow

Follow these steps to get a PAR request URI and an authorization code to exchange for an access token:

1. [Prepare the demonstration](#prepare-par-demo)

2. [Get a PAR request URI](#proc-par-requesturi)

3. [Get an authorization code using REST](#proc-par-no-browser) or [Get an authorization code using a browser](#proc-par-browser)

4. [Exchange an authorization code for an access token](#proc-par-token)

### Prepare the demonstration

Complete these steps to prepare the authorization code grant with PAR flow demonstration:

1. [Create an application owner profile](../identities/manage-identities.html#create-a-user-profile) and record the username and password.

2. [Register a client application](../app-management/register-a-custom-application.html).

   1. In the Advanced Identity Cloud admin console, go to Applications > Applications and select + Custom Application.

   2. Select the sign-in method as OIDC - OpenId Connect and application type as Web.

   3. Create the application, providing the following details:

      * Name

        `myClient`

      * Owners

        `application-owner`

      * Client ID

        `myClient`

      * Client Secret

        `mySecret`

   4. Switch to the Sign On tab and under General Settings, set these fields to the following values:

      * Sign-in URLs

        `https://www.example.com:443/callback`

      * Scopes

        `write`

   5. Save your changes.

3. Configure the duration of the request URI:

   1. In the Advanced Identity Cloud admin console, go to [icon: vpn_key, set=material, size=inline] Authorization > OAuth2 Provider > Advanced.

   2. Set PAR Request URI Lifetime to a value sufficient to cover the duration of the PAR request.

      For more information, refer to [PAR Request URI Lifetime](../am-reference/services-configuration.html#par-request-uri-lifetime).

   3. Save your changes.

4. [Create a resource owner profile](../identities/manage-identities.html#create-a-user-profile) and record the username and password.

### Get a PAR request URI

As the client, call Advanced Identity Cloud's [/oauth2/par](oauth2-par-endpoint.html) endpoint. Specify parameters directly in the request body. Alternatively, for large or sensitive data, Advanced Identity Cloud supports the [JWT-Secured Authorization Request (JAR)](https://www.rfc-editor.org/info/rfc9101) standard for PAR, which lets you wrap parameters in a signed and encrypted JWT. When using JAR, sign the request JWT with the client's private key and encrypt it with the authorization server's public key. You can obtain the authorization server's public key from its JWKS URI.

Example parameters with a JWT:

* **`client_id`**: `myClient`

* **`client_secret`**: `mySecret`

* **`request`**: `signed-encrypted-jwt-value`

Example parameters without a JWT:

* **`client_id`**: `myClient`

* **`client_secret`**: `mySecret`

* **`redirect_uri`**: `https://www.example.com:443/callback`

* **`scope`**: `write`

* **`response_type`**: `code`

* **`code_challenge`**: `code_challenge`

* **`code_challenge_method`**: `S256`

For information about required parameters and an example JWT request object, refer to [/oauth2/par](oauth2-par-endpoint.html).

Example PAR request with a JWT:

```bash
$ curl --request POST \
--data "client_id=myClient" \
--data "client_secret=forgerock" \
--data "request=signed-encrypted-jwt-value" \
"https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/par"
```

Example PAR request without a JWT:

```bash
$ curl --request POST \
--data "client_id=myClient" \
--data "client_secret=forgerock" \
--data "response_type=code" \
--data "scope=write" \
--data "code_challenge=code_challenge" \
--data "code_challenge_method=S256" \
--data "redirect_uri=https://www.example.com:443/callback" \
"https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/par"
```

On success, the authorization server returns the following JSON:

```bash
{
  "request_uri": "zizBvZPwAmzfcDOMKTPv0QTaRA8", (1)
  "expires_in": 90 (2)
}
```

|       |                                                                  |
| ----- | ---------------------------------------------------------------- |
| **1** | `request_uri`: A reference to the PAR request payload.           |
| **2** | `expires_in`: The validity period of the request URI in seconds. |

### Get an authorization code using a browser

1. Ensure the client has retrieved a request URI by following the steps described in [Get a PAR request URI](#proc-par-requesturi).

2. The client redirects the resource owner's user-agent to Advanced Identity Cloud's [/oauth2/authorize](oauth2-authorize-endpoint.html) endpoint including the following parameters:

   * **`client_id`**: `myClient`

   * **`response_type`**: `code`

   * **`request_uri`**: `par_request_uri`

   * **`redirect_uri`**: `https://www.example.com:443/callback`

   For example:

   ```none
   https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/authorize \
   ?client_id=myClient \
   &response_type=code \
   &request_uri=zizBvZPwAmzfcDOMKTPv0QTaRA8 \
   &scope=write \
   &redirect_uri=https://www.example.com:443/callback
   ```

   |   |                                                                                                                                                                                |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | * The URL is split and spaces added for readability purposes.

   * The `scope` parameter is optional if default values are configured in the authorization server or the client. |

3. The resource owner authenticates to Advanced Identity Cloud. In this demonstration, they log in using the default journey configured for the realm.

   |   |                                                                                                                                                                                                                                                                                                                                                             |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | By default, client applications in Advanced Identity Cloud use [implied consent](oauth2-manage-consent.html#skip-consent). If Advanced Identity Cloud is configured to require explicit consent, the authorization server presents the resource owner with a consent screen. To continue the flow, the resource owner must select `Allow` to grant consent. |

   Advanced Identity Cloud redirects the resource owner to the URL specified in the `redirect_uri` parameter.

4. Inspect the URL in the browser.

   It contains a `code` parameter with the authorization code Advanced Identity Cloud issued.

   For example:

   `https://www.example.com/callback?code=authorization-code&iss...`

5. Follow the steps to [get an access token](#proc-par-token).

### Get an authorization code using REST

1. Ensure the client has retrieved a request URI by following the steps in [Get a PAR request URI](#proc-par-requesturi).

2. [Authenticate](../am-authentication/authn-rest.html) as the resource owner.

   For example:

   ```bash
   $ curl \
   -i \
   --request POST \
   --header "Content-Type: application/json" \
   --header 'X-OpenAM-Username: resource-owner-username' \
   --header 'X-OpenAM-Password: resource-owner-password' \
   --header "Accept-API-Version: resource=2.0, protocol=1.0" \
   'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate'
   {
     "tokenId": "tokenId",
     "successUrl": "/enduser/?realm=/alpha",
     "realm": "/alpha"
   }
   ```

3. As the client, call the [/oauth2/authorize](oauth2-authorize-endpoint.html) endpoint to request the authorization code. Provide the resource owner's SSO token in a cookie and the following parameters:

   * **`client_id`**: `myClient`

   * **`request_uri`**: `par_request_uri`

   * **`csrf`**: `tokenId`

   * **`decision`**: `allow`

   Find more information on the parameters supported by this endpoint in [/oauth2/authorize](oauth2-authorize-endpoint.html).

   For example:

   ```bash
   $ curl --dump-header - \
   --request POST \
   --cookie "<session-cookie-name>=tokenId" \
   --data "client_id=myClient" \
   --data "request_uri=par_request_uri" \
   --data "csrf=tokenId" \
   --data "decision=allow" \
   "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/authorize"
   ```

   If Advanced Identity Cloud can authenticate the user and the client, it returns an HTTP 302 response with the authorization code appended to the redirection URL:

   ```none
   HTTP/2 302
   ...
   location: https://www.example.com:443/callback?code=authorization-code&iss...
   ...
   ```

4. Perform the steps in [Exchange an authorization code for an access token](#proc-par-token) to get an access token.

### Exchange an authorization code for an access token

As the client, call the [/oauth2/access_token](oauth2-access_token-endpoint.html) endpoint to exchange the authorization code for an access token. Provide the following parameters:

* **`myClient:mySecret`**

* **`grant_type`**: `authorization_code`

* **`code`**: `authorization-code`

* **`redirect_uri`**: `https://www.example.com:443/callback`

* **`code_verifier`**: `code-verifier`

For example:

```bash
$ curl \
--request POST \
--user 'myClient:forgerock' \
--data "grant_type=authorization_code" \
--data "code=authorization-code" \
--data "redirect_uri=https://www.example.com:443/callback" \
--data "code_verifier=code-verifier" \
"https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/access_token"
```

The `redirect_uri` and client parameters specified in this call must match those used as part of the authorization code request, or the authorization server will not validate the code.

The authorization server returns an access token, for example:

```json
{
  "access_token": "access-token",
  "refresh_token":"refresh-token",
  "scope": "write",
  "token_type": "Bearer",
  "expires_in": 3599
}
```

By default, the authorization server also issues a [refresh token](oauth2-refresh-tokens.html) whenever it issues access tokens.

---

---
title: Authorization code grant with PKCE
description: Use Proof Key for Code Exchange to securely request access tokens for public OAuth 2.0 clients
component: pingoneaic
page_id: pingoneaic:am-oauth2:oauth2-authz-grant-pkce
canonical_url: https://docs.pingidentity.com/pingoneaic/am-oauth2/oauth2-authz-grant-pkce.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "OpenID Connect (OIDC)", "Endpoints", "Authorization", "Grant Flow", "PKCE", "REST API"]
page_aliases: ["oidc1-guide:openid-connect-authorization-code-flow-pkce.adoc", "oauth2-guide:oauth2-authz-grant-pkce.adoc"]
section_ids:
  oauth2-authz-pkce-flow: The authorization code grant with PKCE flow
  oauth_2_0: OAuth 2.0
  oidc: OIDC
  oauth2-authz-pkce-demo: Demonstrate the authorization code grant with PKCE flow
  prepare-demo-oauth2-authz-pkce: Prepare the demonstration
  proc-auth-code-generate-pkce: Generate a code verifier and a code challenge
  proc-auth-code-browser-pkce: Get an authorization code using a browser
  proc-auth-code-no-browser-pkce: Get an authorization code using REST
  proc-auth-code-token-pkce: Exchange an authorization code for an access token
  additional_oidc_claims: Additional OIDC claims
---

# Authorization code grant with PKCE

* Endpoints

  * [/oauth2/authorize](oauth2-authorize-endpoint.html)

  * [/oauth2/access_token](oauth2-access_token-endpoint.html)

  * [/oauth2/userinfo](../am-oidc1/rest-api-oidc-userinfo-endpoint.html) (OpenID Connect \[OIDC])

The authorization code grant, when combined with the Proof Key for Code Exchange (PKCE) standard ([RFC 7636](https://www.rfc-editor.org/info/rfc7636)), is used when a public client, such as a native or SPA application, requires access to protected resources.

The flow is similar to the regular [authorization code grant](oauth2-authz-grant.html), but the client must generate a code that is used in the communication between the client and the authorization server. This code mitigates against interception attacks performed by malicious users.

Browser-based clients making OAuth 2.0 requests to different domains must implement Cross-Origin Resource Sharing (CORS) calls to access OAuth 2.0 resources in different domains.

The PKCE flow adds three parameters to those used for the authorization code grant:

* `code_verifier`

  A random string that correlates the authorization request with the token request.

* `code_challenge`

  A string derived from the code verifier sent in the authorization request, which is validated against the code verifier during the token request.

* `code_challenge_method`

  The method used to derive the code challenge.

## The authorization code grant with PKCE flow

### OAuth 2.0

![Advanced Identity Cloud supports the authorization code grant with PKCE.](_images/oauth2-authz-pkce.svg)

1. The client receives a request to access a protected resource. To access the resource, the client requires authorization from the resource owner. When using the PKCE standard, the client must generate a unique code and a way to verify it, and append the code to the request for the authorization code.

2. The client redirects the resource owner's user-agent to the authorization server.

3. The authorization server authenticates the resource owner, confirms resource access, and gathers consent if not previously saved.

4. If the resource owner's credentials are valid, the authorization server stores the code challenge and redirects the resource owner's user agent to the redirection URI.

5. During the redirection process, the authorization server appends an authorization code to the request to the client.

6. The client receives the authorization code and calls the authorization server's token endpoint to exchange the authorization code for an access token appending the verification code to the request.

7. The authorization server verifies the code stored in memory using the validation code. It also verifies the authorization code. If both codes are valid, the authorization server returns an access token (and a refresh token, if configured) to the client.

8. The client requests access to the protected resource from the resource server.

9. The resource server contacts the authorization server to validate the access token.

10. The authorization server validates the token and responds to the resource server.

11. If the token is valid, the resource server allows the client to access the protected resource.

### OIDC

![Advanced Identity Cloud supports the authorization code grant with PKCE.](_images/oidc-authz-pkce.svg)

1. The end user wants to use the services provided by the relying party (RP). The RP, usually a web-based service, requires an account to provide those services.

   The end user issues a request to share their information with the RP.

2. To access the end user's information in the OpenID provider (OP), the RP requires end user consent. When using the PKCE standard, the RP must generate a unique code and a way to verify it, and append the code to the request for the authorization code.

3. The RP redirects the end user's user-agent with `code_challenge` and `code_challenge_method`...

4. ...to the OP.

5. The OP authenticates the end user, confirms resource access, and gathers consent if necessary.

6. On success, the OP stores the code challenge and its method.

7. The OP redirects the end user's user-agent to the redirection URI, usually at the RP.

8. During the redirection process, the OP appends an authorization code.

9. The RP authenticates to the OP and exchanges the authorization code for an access token and an ID token, appending the verification code to the request.

10. The OP verifies the code challenge it stored using the validation code, and verifies the authorization code.

11. If the codes are valid, the OP issues an access token and an ID token to the RP.

12. The RP validates the ID token and its claims.

    The RP can use the ID token subject ID claim as the end user's identity.

13. If the RP requires additional claims, it sends a request to the [/oauth2/userinfo](../am-oidc1/rest-api-oidc-userinfo-endpoint.html) endpoint with the access token for authorization.

14. If the access token is valid, the `/oauth2/userinfo` endpoint returns any additional claims.

    The RP can use the subject ID and the additional claims to identify the end user.

## Demonstrate the authorization code grant with PKCE flow

Perform these steps to get an authorization code and exchange it for an access token:

1. [Prepare the demonstration](#prepare-demo-oauth2-authz-pkce)

2. [Generate a code verifier and a code challenge](#proc-auth-code-generate-pkce)

3. [Get an authorization code using a browser](#proc-auth-code-browser-pkce) or [Get an authorization code using REST](#proc-auth-code-no-browser-pkce)

4. [Exchange an authorization code for an access token](#proc-auth-code-token-pkce)

### Prepare the demonstration

Complete these steps to prepare the authorization code grant with PKCE flow demonstration:

1. [Create an application owner profile](../identities/manage-identities.html#create-a-user-profile) and record the username and password.

2. [Register a client application](../app-management/register-a-custom-application.html).

   1. In the Advanced Identity Cloud admin console, go to Applications > Applications and select + Custom Application.

   2. Select the sign-in method as OIDC - OpenId Connect and application type as Native / SPA.

   3. Create the application, providing the following details:

      * Name

        `myClient`

      * Owners

        `<application-owner>`

      * Client ID

        `myClient`

   4. Switch to the Sign On tab and under General Settings, set these fields to have the following values:

      * Sign-in URLs

        `https://www.example.com:443/callback`

      * Scopes

        `write` (for OAuth 2.0)\
        `openid` and `profile` (for OIDC)

   5. Save your changes.

3. [Create a resource owner profile](../identities/manage-identities.html#create-a-user-profile) and record the username and password.

### Generate a code verifier and a code challenge

The client application must generate a *code verifier*, a high-entropy URL-safe random string between 43 and 128 characters long, and a *code challenge*, a base64url-encoded hash of the code verifier.

It is mandatory to create the challenge using a SHA-256 algorithm if the client supports it, as specified in the PKCE standard ([RFC 7636](https://www.rfc-editor.org/info/rfc7636)).

The following example code generates values such as `082b7ab3042995bcb3163ec83cf5f348ff4393d5713630eb5f09dcf7d0c2cca39749313556c260558eb49355ff86d0e61449` for the code verifier and `K7Dz7AcV1urbgo4FYNgy2QAAz6v2LyIdmmGPzsFZbAc` for the code challenge:

* Node.js

* Postman pre-request

```javascript
const crypto = require('crypto');

const verifier = crypto.randomBytes(50).toString('hex').slice(0, 128);
const challenge = crypto.createHash('sha256')
    .update(Buffer.from(verifier))
    .digest('base64')
    .replace(/=/g, '')
    .replace(/\+/g, '-')
    .replace(/\//g, '_');

console.log("verifier: " + verifier);
console.log("challenge: " + challenge);
```

```javascript
// Generate random 128-character code_verifier from 8 * 16-character random passwords
var code_verifier = "";
for (let i=0; i<8; i++ ){
    code_verifier += pm.variables.replaceIn('{{$randomPassword}}');
}

// Generate code_challenge with SHA-256 of verifier, then Base64 URL encode the result
var code_challenge = createSHA256Hash(code_verifier);

// Set global variables in Postman
pm.globals.set("code_verifier", code_verifier);
pm.globals.set("code_challenge", code_challenge);

function createSHA256Hash(code_verifier) {
    return code_challenge = base64URLEncode(CryptoJS.SHA256(code_verifier))
}

function base64URLEncode(hash) {
    return hash.toString(CryptoJS.enc.Base64)
    .replace(/=/g, '')
    .replace(/\+/g, '-')
    .replace(/\//g, '_');
}
```

The client is now ready to request an authorization code.

### Get an authorization code using a browser

1. The client redirects the resource owner's user-agent to the authorization server's [/oauth2/authorize](oauth2-authorize-endpoint.html) endpoint, including the following query parameters:

   * **`client_id`**: `myClient`

   * **`response_type`**: `code`

   * **`scope`**: `write` (OAuth 2.0); `openid` and `profile` (OIDC)

   * **`redirect_uri`**: `https://www.example.com:443/callback`

   * **`code_challenge`**: `<code_challenge>`

   * **`code_challenge_method`**: `S256`

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The `Code Verifier Parameter Required` setting (in the Advanced Identity Cloud admin console, under [icon: vpn_key, set=material, size=inline] Authorization > OAuth2 Provider > Advanced) specifies whether Advanced Identity Cloud requires clients to include a code verifier in their calls.However, if a client makes a call to Advanced Identity Cloud with the `code_challenge` parameter, Advanced Identity Cloud honors the code exchange regardless of the value of `Code Verifier Parameter Required`. Find more information in [Configure Advanced Identity Cloud as an authorization server](../authorization/oauth2-provider.html). |

   For example:

   ```none
   https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/authorize
   ?client_id=myClient
   &response_type=code
   &scope=write
   &redirect_uri=https://www.example.com:443/callback
   &code_challenge=K7Dz7AcV1urbgo4FYNgy2QAAz6v2LyIdmmGPzsFZbAc
   &code_challenge_method=S256
   &state=abc123
   ```

   For OIDC, set `scope=openid profile` instead.

   |   |                                                                                                                                                                                                                                                                 |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The URL is split and spaces added for readability purposes.The `scope` parameter is optional if default values are configured in the authorization server or the client.The `state` parameter is included to protect against CSRF attacks but is also optional. |

2. The resource owner authenticates to the authorization server. In this demonstration, they sign in using the default journey configured for the realm.

   |   |                                                                                                                                                                                                                                                                                                                                                             |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | By default, client applications in Advanced Identity Cloud use [implied consent](oauth2-manage-consent.html#skip-consent). If Advanced Identity Cloud is configured to require explicit consent, the authorization server presents the resource owner with a consent screen. To continue the flow, the resource owner must select `Allow` to grant consent. |

   The authorization server redirects the resource owner to the URL specified in the `redirect_uri` parameter.

3. Inspect the URL in the browser.

   It contains a `code` parameter with the authorization code the authorization server issued.

   For example:

   `https://www.example.com/callback?code=<authorization-code>&iss...`

4. Follow the steps to [get an access token](#proc-auth-code-token-pkce).

### Get an authorization code using REST

1. [Authenticate](../am-authentication/authn-rest.html) as the resource owner.

   For example:

   ```bash
   $ curl \
   --request POST \
   --header 'Content-Type: application/json' \
   --header 'X-OpenAM-Username: <resource-owner-username>' \
   --header 'X-OpenAM-Password: <resource-owner-password>' \
   --header "Accept-API-Version: resource=2.0, protocol=1.0" \
   'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate'
   {
     "tokenId": "<tokenId>",
     "successUrl": "/enduser/?realm=/alpha",
     "realm": "/alpha"
   }
   ```

2. As the client, call the [/oauth2/authorize](oauth2-authorize-endpoint.html) endpoint to request the authorization code. Provide the resource owner's SSO token in a cookie and the following parameters:

   * **`scope`**: `write` (OAuth 2.0); `openid` and `profile` (OIDC)

   * **`response_type`**: `code`

   * **`client_id`**: `myClient`

   * **`csrf`**: `<tokenId>`

   * **`redirect_uri`**: `https://www.example.com:443/callback`

   * **`decision`**: `allow`

   * **`code_challenge`**: `<code_challenge>`

   * **`code_challenge_method`**: `S256`

     |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | The `Code Verifier Parameter Required` setting (in the Advanced Identity Cloud admin console, under [icon: vpn_key, set=material, size=inline] Authorization > OAuth2 Provider > Advanced) specifies whether Advanced Identity Cloud requires clients to include a code verifier in their calls.However, if a client makes a call to Advanced Identity Cloud with the `code_challenge` parameter, Advanced Identity Cloud honors the code exchange regardless of the value of `Code Verifier Parameter Required`. Find more information in [Configure Advanced Identity Cloud as an authorization server](../authorization/oauth2-provider.html). |

     For example:

     ```bash
     $ curl --dump-header - \
     --request POST \
     --cookie "<session-cookie-name>=<tokenId>" \
     --data "scope=write" \
     --data "response_type=code" \
     --data "client_id=myClient" \
     --data "csrf=<tokenId>" \
     --data "redirect_uri=https://www.example.com:443/callback" \
     --data "state=abc123" \
     --data "decision=allow" \
     --data "code_challenge=K7Dz7AcV1urbgo4FYNgy2QAAz6v2LyIdmmGPzsFZbAc" \
     --data "code_challenge_method=S256" \
     "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/authorize"
     ```

     For OIDC, set `scope=openid profile` instead.

     |   |                                                                                                                                                                                                      |
     | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | The `scope` parameter is optional if default values are configured in the authorization server or the client.The `state` parameter is included to protect against CSRF attacks but is also optional. |

     If the authorization server is able to authenticate the user and the client, it returns an HTTP 302 response with the authorization code appended to the redirection URL:

     ```none
     HTTP/2 302
     ...
     location: https://www.example.com:443/callback?code=<authorization-code>&iss...
     ...
     ```

3. Follow the steps to [get an access token](#proc-auth-code-token-pkce).

### Exchange an authorization code for an access token

As the client, call the [/oauth2/access_token](oauth2-access_token-endpoint.html) endpoint to exchange the authorization code for an access token. Provide the following parameters:

* **`client_id`**: `myClient`

* **`grant_type`**: `authorization_code`

* **`code`**: `<authorization-code>`

* **`redirect_uri`**: `https://www.example.com:443/callback`

* **`code_verifier`**: `<code-verifier>`

  For example:

  ```bash
  $ curl \
  --request POST \
  --data "client_id=myClient" \
  --data "grant_type=authorization_code" \
  --data "code=<authorization-code>" \
  --data "redirect_uri=https://www.example.com:443/callback" \
  --data "code_verifier=<code-verifier>" \
  "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/access_token"
  ```

  The `client_id` and the `redirect_uri` parameters specified in this call must match those used for the authorization code request or the authorization server will not validate the code.

  For OAuth 2.0, the authorization server returns an access token; for example:

  ```json
  {
    "access_token": "<access-token>",
    "refresh_token": "<refresh-token>",
    "scope": "write",
    "token_type": "Bearer",
    "expires_in": 3599
  }
  ```

  For OIDC, the OP returns an access token and an ID token; for example:

  ```json
  {
    "access_token": "<access-token>",
    "refresh_token": "<refresh-token>",
    "scope": "openid profile",
    "id_token": "<id-token>",
    "token_type": "Bearer",
    "expires_in": 3599
  }
  ```

  By default, the authorization server also issues a [refresh token](oauth2-refresh-tokens.html) whenever it issues access tokens.

## Additional OIDC claims

An RP can request additional claims about the end user with the access token at the [/oauth2/userinfo](../am-oidc1/rest-api-oidc-userinfo-endpoint.html) endpoint:

```bash
$ curl \
--request GET \
--header "Authorization Bearer <access-token>" \
"https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/userinfo"
{
  "name": "<resource-owner-display-name>",
  "family_name": "<resource-owner-family-name>",
  "given_name": "<resource-owner-given-name>",
  "sub": "<resource-owner-id>",
  "subname": "<resource-owner-id>"
}
```

---

---
title: Authorization header (HTTP Basic)
description: Authenticate OAuth 2.0 clients using HTTP Basic authorization header with encoded credentials
component: pingoneaic
page_id: pingoneaic:am-oauth2:client-auth-header
canonical_url: https://docs.pingidentity.com/pingoneaic/am-oauth2/client-auth-header.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "Authentication", "OAuth 2.0", "Federation", "HTTP Basic", "Clients"]
page_aliases: ["oauth2-guide:client-auth-header.adoc"]
---

# Authorization header (HTTP Basic)

This is the default authentication method for Advanced Identity Cloud confidential clients.

The OAuth 2.0 client authenticates by sending the credentials in an HTTP Basic authentication (`Authorization`) header.

The value is `client_id:client_secret`, first [URL encoded](https://en.wikipedia.org/wiki/Percent-encoding), then base64 encoded. For example, `myClient:mySecret` encodes to `bXlDbGllbnQlM0FteVNlY3JldA`:

```bash
$ curl \
--request POST \
--header "Authorization: Basic bXlDbGllbnQlM0FteVNlY3JldA" \
...
```

To confirm this authentication method for a confidential OAuth 2.0 client, check the client profile in the Advanced Identity Cloud admin console:

1. Go to Applications > Applications > *Name* > Sign On > General Settings > Advanced > Authentication.

2. Verify the Token Endpoint Authentication Method is `client_secret_basic` and save your work.

Make sure all connections to Advanced Identity Cloud use HTTPS to protect the secret.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | URL encode the `client_id` and `client_secret` *before* base64 encoding the `client_id:client_secret` value.For example, a client with ID `example.com` and secret `s=cr%t` has characters you must URL encode in the secret:- The URL-encoded ID remains `example.com`.

- The URL-encoded secret is `s%3Dcr%25t`.

- The credentials are `example.com:s%3Dcr%25t` before base64 encoding.

- The base64-encoded form is `ZXhhbXBsZS5jb206cyUzRGNyJTI1dA==`.

- The final HTTP Basic header is `Authorization: Basic ZXhhbXBsZS5jb206cyUzRGNyJTI1dA==` |

---

---
title: Authorize endpoint data provider
description: Add custom data to OAuth 2.0 authorization endpoint responses through extension scripts
component: pingoneaic
page_id: pingoneaic:am-oauth2:plugins-auth-endpoint-data-provider
canonical_url: https://docs.pingidentity.com/pingoneaic/am-oauth2/plugins-auth-endpoint-data-provider.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "Customization", "Plugins", "Authorization", "Scripting"]
page_aliases: ["oauth2-guide:plugins-auth-endpoint-data-provider.adoc"]
section_ids:
  prepare_the_demonstration: Prepare the demonstration
  auth-endpoint-sample-script: Sample script
  auth-endpoint-oauth2-client: OAuth 2.0 client
  auth-endpoint-resource-owner: Resource owner
  test_the_demonstration: Test the demonstration
  use_a_validated_script: Use a validated script
---

# Authorize endpoint data provider

Use this extension point to add data to Advanced Identity Cloud's response to an [OAuth 2.0 authorization request](oauth2-authorize-endpoint.html).

* Template script

  [OAuth2 Authorize Endpoint Data Provider Script](../am-scripting/sample-scripts.html#oauth2-authorize-endpoint-data-provider-js)

* Script bindings

  [Authorization endpoint data provider scripting API](../am-scripting/authorize-endpoint-data-provider-api.html)

## Prepare the demonstration

Start by preparing the demonstration:

* [Create a sample script](#auth-endpoint-sample-script).

* [Create an OAuth 2.0 client](#auth-endpoint-oauth2-client).

* [Create a resource owner account](#auth-endpoint-resource-owner).

### Sample script

The sample adds query string parameters to the redirect URL in the OAuth 2.0 authorization response.

1. In the Advanced Identity Cloud admin console, [create a script](../developer-docs/scripting-auth.html#create-a-new-auth-script) of type OAuth2 Authorize Endpoint Data Provider.

2. Select either legacy or next-generation as the script engine.

3. Enter a suitable name for your script.

4. In the new script window, save the following script:

   * Legacy

   * Next-generation

   ```javascript
   (function () {
     var map = new java.util.HashMap()

     // Add an arbitrary query string parameter.
     map.put("key", "value")

     // Add the IP address if available.
     if (session) {
       map.put("ipAddress", session.getProperty("Host"))
     }

     return map
   }());
   ```

   ```javascript
   var map = {};

   // Add an arbitrary query string parameter.
   map.key = "value";

   // Add the IP address if available.
   if (session) {
       map.ipAddress = session.getProperty("Host");
   }

   map;
   ```

   |   |                                                                                                                                                                                                                                                                                                                                                                          |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | You can find information about the common bindings such as `logger` and `scriptName` in [Common bindings](../am-scripting/script-bindings.html).You can find information about the bindings specific to authorize endpoint data provider scripts in the [Authorization endpoint data provider scripting API](../am-scripting/authorize-endpoint-data-provider-api.html). |

### OAuth 2.0 client

The OAuth 2.0 client profile in this example overrides the Advanced Identity Cloud OAuth 2.0 provider settings. This lets you test the script without affecting access tokens issued to other clients.

1. Create a public OAuth 2.0 client account.

   In the Advanced Identity Cloud admin console, select Applications > Applications > + Custom Application, and create a new Native / SPA client with the following setting:

   * Client ID

     `myClient`

2. Add the following settings in the client profile and save your work:

   * Sign-in URLs

     `https://www.example.com:443/callback`

   * Scopes

     `access`

3. Override OAuth 2.0 provider settings for this client.

   Under Native Consoles > Access Management, select Realms > alpha > Applications > OAuth 2.0 > Clients > myClient, switch to the OAuth2 Provider Overrides tab, update the following settings and save your work:

   * Enable OAuth2 Provider Overrides

     Enabled

   * Authorize Endpoint Data Provider Plugin Type

     `SCRIPTED`

   * Authorize Endpoint Data Provider Script

     `Demo OAuth 2.0 authz data extension`

### Resource owner

An OAuth 2.0 client requests the access token on behalf of a resource owner.

Create the OAuth 2.0 resource owner account:

1. In the Advanced Identity Cloud admin console, select Identities > Manage > Alpha Realm - Users > + New Alpha Realm - User and fill the required fields.

2. Record the username and password.

## Test the demonstration

After preparing the demonstration, test your work using HTTP calls to REST endpoints.

The demonstration uses a partial [Authorization code grant](oauth2-authz-grant.html) flow. It validates only the extension to the authorization endpoint and stops before exchanging the code for an access token:

* The resource owner authenticates to obtain an SSO token.

* The client relies on Implied Consent being enabled (default). It assumes the resource owner grants the client access.

* The client requests the authorization code.

Follow these steps:

1. Authenticate as the resource owner:

   ```bash
   curl \
   --request POST \
   --header 'Content-Type: application/json' \
   --header 'X-OpenAM-Username: <resource-owner-username>' \
   --header 'X-OpenAM-Password: <resource-owner-password>' \
   --header 'Accept-API-Version: resource=2.0, protocol=1.0' \
   'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate'
   {
     "tokenId": "<resource-owner-tokenId>",
     "successUrl": "/enduser/?realm=/alpha",
     "realm": "/alpha"
   }
   ```

2. Request the authorization code as the client:

   ```bash
   curl \
   --dump-header - \
   --request POST \
   --cookie '<session-cookie-name>=<resource-owner-tokenId>' \
   --data 'scope=access' \
   --data 'response_type=code' \
   --data 'client_id=myClient' \
   --data 'csrf=<resource-owner-tokenId>' \
   --data 'redirect_uri=https://www.example.com:443/callback' \
   --data 'state=abc123' \
   --data 'decision=allow' \
   'https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/authorize'
   ...
   location: https://www.example.com:443/callback?code=...&ipAddress=IP-address&key=value...
   ...
   ```

   The script added `ipAddress=IP-address` and `key=value` to the redirect URL in the response.

## Use a validated script

Test your authorize endpoint data provider scripts as you did for the demonstration. After validating your script with OAuth 2.0 provider overrides in your test client, you can update the OAuth 2.0 provider configuration to use the script:

1. In the Advanced Identity Cloud admin console, go to [icon: vpn_key, set=material, size=inline] Authorization > OAuth2 Provider.

2. Switch to the Plugins tab and edit the following settings:

   * Authorize Endpoint Data Provider Plugin Type

     `SCRIPTED`

   * Authorize Endpoint Data Provider Script

     *Your script*

3. Save your work.

---

---
title: Client application authentication
description: Choose OAuth 2.0 client authentication methods for authorization server token endpoint
component: pingoneaic
page_id: pingoneaic:am-oauth2:oauth2-client-auth
canonical_url: https://docs.pingidentity.com/pingoneaic/am-oauth2/oauth2-client-auth.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "Endpoints", "Authorization", "REST API"]
page_aliases: ["oauth2-guide:oauth2-client-auth.adoc"]
---

# Client application authentication

OAuth 2.0 client applications send their authentication credentials using one of the following mechanisms:

* The [Authorization header (HTTP Basic)](client-auth-header.html) (default)

* [Form parameters (HTTP POST)](client-auth-form.html)

* A [JWT profile](client-auth-jwt.html)

Authentication depends on the Client Type defined in the Advanced Identity Cloud admin console under Applications > Applications > *Name* > Sign On > General Settings > Advanced > Authentication:

* Confidential clients

  These applications include websites and services that make secure connections to Advanced Identity Cloud.

  They can protect their client secret or JSON Web Token (JWT).

  You configure the authentication method for a confidential client in the Advanced Identity Cloud admin console under Applications > Applications > *Name* > Sign On > General Settings > Advanced > Authentication as the Token Endpoint Authentication Method.

  When a client authenticates with form parameters, the server can store POST data on the user-agent in an `OAUTH_REQUEST_ATTRIBUTES` cookie. Advanced Identity Cloud uses the cookie to continue the authentication process across redirects. It marks the cookie for deletion on the next successful OAuth 2.0 authorization.

* Public clients

  These are single-page applications (SPAs) and applications running on devices.

  They cannot protect secrets.

  Public clients identify themselves by client ID, but do not fully authenticate.

  Public OpenID Connect clients must specify `none` as their authentication method.

---

---
title: Client application registration
description: Register OAuth 2.0 clients to enable them to request authorization and obtain tokens
component: pingoneaic
page_id: pingoneaic:am-oauth2:oauth2-register-client
canonical_url: https://docs.pingidentity.com/pingoneaic/am-oauth2/oauth2-register-client.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "OpenID Connect (OIDC)", "Clients", "Setup &amp; Configuration", "Grant Flow"]
page_aliases: ["oauth2-guide:oauth2-register-client.adoc"]
section_ids:
  shared_application_settings: Shared application settings
  oauth2-client-profile-group: Create group settings
  oauth2-client-profile-assign-group: Inherit group settings
  oauth2app-journey: Client application journeys
---

# Client application registration

OAuth 2.0 or OIDC client applications must *register* with Advanced Identity Cloud before they can connect.

Registration involves setting up a client application profile in one of the following ways:

* Using the Advanced Identity Cloud admin console.

  For details, refer to [Application management](../app-management/applications.html).

* Programmatically.

  For details, refer to [Dynamic client registration](../am-oidc1/oauth2-dynamic-client-registration.html).

|   |                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To configure large numbers of short-lived clients at runtime, such as AI agents in Model Context Protocol (MCP) flows, use the [client ID metadata document (CIMD) feature](oauth2-cimd.html). |

## Shared application settings

To define shared settings for multiple client application profiles, you have these alternatives:

* Configure default settings for all clients in the realm.

  Client applications inherit their default settings from the OAuth 2.0 provider service. Configure these settings in the Advanced Identity Cloud admin console, under [icon: vpn_key, set=material, size=inline] Authorization > OAuth2 Provider.

* [Create an OAuth 2.0 client profile group](#oauth2-client-profile-group).

  Client applications that belong to the group can inherit its settings.

## Create group settings

1. Under Native Consoles > Access Management, go to Realms > *Realm Name* > Applications > OAuth 2.0 > Clients.

2. On the Groups tab, click + Add Group, and click Create.

3. Adjust the configuration as needed, saving changes on each tab.

4. [Assign clients to the group](#oauth2-client-profile-assign-group).

## Inherit group settings

1. Under Native Consoles > Access Management, go to Realms > *Realm Name* > Applications > OAuth 2.0 > Clients > *Client ID*.

2. On the Core tab, select the Group in the drop-down.

3. Save your work.

   Selecting a group refreshes the client configuration, discarding any other unsaved settings.

   Inheritance icons [icon: lock-open, set=fa]appear next to inherited group settings. Not all properties can inherit their value; for example, the Client secret property is specific to each client application.

   ![Set a client application's group to inherit settings.](_images/create-oauth2-profile-group.png)Figure 1. Inheriting group settings

4. Inherit settings by clicking their inheritance icons [icon: lock-open, set=fa].

   The icon changes to [icon: lock, set=fa], indicating the setting is inherited.

5. Save your work.

Configuration changes have the following effects:

* When you change inherited settings in the group, the client applications get them automatically.

* When you change a client application's Group, locked settings inherit from the new group.

* When you remove or delete a group, Advanced Identity Cloud writes inherited settings to the client profile, which you can edit independently.

## Client application journeys

You can configure OAuth 2.0 / OIDC client applications to redirect authentication requests to a specified journey.

Learn about configuring application journeys in [Application journeys](../app-management/application-journeys.html).

---

---
title: Client credentials grant
description: Request access tokens using client credentials grant when the client is the resource owner
component: pingoneaic
page_id: pingoneaic:am-oauth2:oauth2-client-cred-grant
canonical_url: https://docs.pingidentity.com/pingoneaic/am-oauth2/oauth2-client-cred-grant.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "Endpoints", "Authorization", "Clients", "Grant Flow", "REST API"]
page_aliases: ["oauth2-guide:oauth2-client-cred-grant.adoc"]
section_ids:
  the_client_credentials_grant_flow: The client credentials grant flow
  oauth2-client-credentials-demo: Demonstrate the client credentials grant flow
  prepare-demo-client-credentials: Prepare the demonstration
  proc-token-client-credentials: Get an access token using the client credentials grant
---

# Client credentials grant

* Endpoints

  * [/oauth2/access_token](oauth2-access_token-endpoint.html)

The client credentials grant is intended for clients who are also resource owners that need to access their own data rather than acting on behalf of a user.

For example, an application that needs access to a protected resource to update its configuration might use the client credentials grant to get an access token.

The client credentials grant flow supports confidential clients only.

In the client credentials grant, the client authenticates as itself, so the access token represents the client rather than an end user. If you need to add custom claims to a client credentials access token, use access token modification. Don't use OIDC claims customization for this flow. OIDC claims apply to end-user flows, not to tokens issued to a client acting on its own behalf. Learn more in [Access tokens](modifying-access-tokens-scripts.html).

## The client credentials grant flow

![Advanced Identity Cloud supports the client credentials grant.](_images/oauth2-client-cred.svg)Figure 1. OAuth 2.0 client credentials grant flow

1. The client sends its credentials to the authorization server to get authenticated and requests an access token.

2. If the client credentials are valid, the authorization server returns an access token to the client.

3. The client requests access to the protected resource from the resource server.

4. The resource server contacts the authorization server to validate the access token.

5. The authorization server validates the token and responds to the resource server.

6. If the token is valid, the resource server allows the client to access the protected resource.

## Demonstrate the client credentials grant flow

Perform these steps to get an access token:

1. [Prepare the demonstration](#prepare-demo-client-credentials)

2. [Get an access token using the client credentials grant](#proc-token-client-credentials)

### Prepare the demonstration

Complete these steps to prepare the client credentials grant flow demonstration:

1. [Create an application owner profile](../identities/manage-identities.html#create-a-user-profile) and record the username and password.

2. [Register a client application](../app-management/register-a-custom-application.html).

   1. In the Advanced Identity Cloud admin console, go to Applications > Applications and select + Custom Application.

   2. Select the sign-in method as OIDC - OpenId Connect and application type as Web.

   3. Create the application, providing the following details:

      * Name

        `myClient`

      * Owners

        `<application-owner>`

      * Client ID

        `myClient`

      * Client Secret

        `mySecret`

   4. Switch to the Sign On tab and under General Settings, update these fields to have the following values:

      * Sign-in URLs

        `https://www.example.com:443/callback`

      * Scopes

        `write`

   5. Ensure Grant Types contains `Client Credentials`.

   6. Save your changes.

3. [Create a resource owner profile](../identities/manage-identities.html#create-a-user-profile) and record the username and password.

4. In the Advanced Identity Cloud admin console, go to [icon: vpn_key, set=material, size=inline] Authorization > OAuth2 Provider > Advanced and ensure the Grant Types field includes `Client Credentials`.

### Get an access token using the client credentials grant

As the client, call [/oauth2/access_token](oauth2-access_token-endpoint.html) specifying the client's credentials, and `grant_type=client_credentials`.

For example:

```bash
$ curl
--request POST \
--user '<client-id>:<client-secret>' \
--data "grant_type=client_credentials" \
--data "scope=write" \
"https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/access_token"
```

|   |                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------- |
|   | The `scope` parameter is optional if default values are configured in the authorization server or the client. |

Advanced Identity Cloud returns an access token, for example:

```json
{
  "access_token": "<access-token>",
  "scope": "write",
  "token_type": "Bearer",
  "expires_in": 3599
}
```

---

---
title: Client ID metadata document (CIMD)
description: Configure Advanced Identity Cloud to accept OAuth 2.0 clients that identify themselves using a URL pointing to a hosted JSON metadata document, without requiring prior registration.
component: pingoneaic
page_id: pingoneaic:am-oauth2:oauth2-cimd
canonical_url: https://docs.pingidentity.com/pingoneaic/am-oauth2/oauth2-cimd.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-07T20:35:41Z
keywords: ["OAuth 2.0", "CIMD", "Client ID Metadata Document", "AI agents", "MCP", "dynamic client", "registration"]
section_ids:
  cimd-how-it-works: How it works
  cimd-document-format: Document format
  cimd-supported-grants: Grant types
  cimd-supported-auth-methods: Authentication methods
  cimd-limitations: Limitations
  cimd-configure: Configure a CIMD profile
  cimd-example-flow: Example authorization code flow
---

# Client ID metadata document (CIMD)

The client ID metadata document (CIMD) feature lets you configure OAuth 2.0 clients to identify themselves using an HTTPS URL as their `client_id`. Advanced Identity Cloud fetches the JSON metadata document at that URL and uses it to configure the client at runtime, with no prior registration required.

CIMD is particularly suited to large numbers of clients such as [AI agents](../identity-for-ai/ai-agent-identities.html) in Model Context Protocol (MCP) flows, where preregistering every short-lived or externally-hosted client is impractical.

Advanced Identity Cloud's support for CIMD aligns with the [IETF OAuth Client ID Metadata Document draft specification](https://datatracker.ietf.org/doc/draft-ietf-oauth-client-id-metadata-document/).

## How it works

When Advanced Identity Cloud receives an OAuth 2.0 request with a `client_id` that begins with `https://`, it treats the value as a URL pointing to a CIMD document and performs the following steps:

![How CIMD works](_images/oauth2-cimd-how-it-works.svg)

1. Advanced Identity Cloud receives a request with a URL-valued `client_id`.

2. Advanced Identity Cloud checks the realm for a CIMD profile whose URL pattern matches the `client_id`.

   If no matching profile exists, or if more than one profile matches, Advanced Identity Cloud rejects the request with an `invalid_client` error.

3. A matching CIMD profile defines the security settings that Advanced Identity Cloud applies to the request.

4. Advanced Identity Cloud fetches the JSON document at the `client_id` URL over HTTPS.

   Redirects aren't followed. Only an HTTP 200 response is accepted.

5. Advanced Identity Cloud receives the metadata document and …​

6. …​ validates that the document's own `client_id` field exactly matches the URL it was fetched from.

   If validation fails, the request is rejected with an `invalid_client` error.

7. Advanced Identity Cloud applies the security checks defined in the matching CIMD profile, including server-side request forgery (SSRF) protection and metadata denylist.

8. If the security checks are successful, Advanced Identity Cloud uses the fetched metadata as the client's runtime configuration for the flow.

9. The resulting client exists only for the duration of the flow and isn't persisted to the identity store.

10. The OAuth 2.0 flow continues.

## Document format

The metadata document follows the RFC 7591 [OAuth 2.0 Dynamic Client Registration Protocol](https://www.rfc-editor.org/rfc/rfc7591) client metadata format.

Example document:

```json
{
  "client_id": "https://app.example.com/oauth/client.json",
  "client_name": "Example MCP Client",
  "client_uri": "https://app.example.com",
  "redirect_uris": [
    "https://app.example.com/callback"
  ],
  "grant_types": ["authorization_code", "refresh_token"],
  "response_types": ["code"],
  "token_endpoint_auth_method": "none",
  "scope": "read write"
}
```

When Advanced Identity Cloud processes a CIMD metadata document, it applies the following constraints:

* The `client_id` must be an HTTPS URL that exactly matches the URL where the document is hosted.

* The following secret-based authentication fields are rejected:

  * `client_secret`

  * `client_secret_expires_at`

  * `token_endpoint_auth_method` secret values (`client_secret_basic`, `client_secret_post`, `client_secret_jwt`)

* The document must not exceed 5 KB.

* The following fields support localization using locale tags, for example `client_name#en` or `client_name#fr`:

  * `client_name`

  * `client_uri`

  * `logo_uri`

  * `policy_uri`

  * `tos_uri`

Learn more about metadata document constraints in the [Limitations](#cimd-limitations) section.

The matching CIMD profile and the metadata document both contribute to the client's runtime configuration. For each metadata field, Advanced Identity Cloud resolves the value in the following order:

1. If the field is in the profile's metadata override denylist, the profile's value is used.

2. Otherwise, if the document specifies the field, the document's value overrides the profile's value.

3. If neither the document nor the profile specifies a value, Advanced Identity Cloud applies the following defaults:

| Field                        | Default                     |
| ---------------------------- | --------------------------- |
| `scope`                      | The realm's default scopes. |
| `grant_types`                | `authorization_code`        |
| `response_types`             | `code`                      |
| `token_endpoint_auth_method` | `none`                      |

|   |                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Redirect URIs aren't required to share the same origin as the `client_id` URL. You can add `redirect_uri` to the override denylist to enforce that the requested redirect URI must be configured in the CIMD profile. |

### Grant types

The following grant types are available to CIMD clients:

* `authorization_code`

* `client_credentials`

* `refresh_token`

* `urn:ietf:params:oauth:grant-type:device_code`

* `urn:ietf:params:oauth:grant-type:jwt-bearer`

* `urn:ietf:params:oauth:grant-type:token-exchange`

A client's declared `grant_types` are filtered to the intersection of this list and the grant types enabled in the realm's OAuth 2.0 provider.

If a client declares grant types but none survive the filtering, Advanced Identity Cloud rejects the request. This prevents a client from accidentally proceeding with a misconfigured or entirely unsupported set of grant types.

### Authentication methods

The following token endpoint authentication methods are available to CIMD clients:

* `none`

* `private_key_jwt`

* `tls_client_auth`

* `self_signed_tls_client_auth`

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can't set the client type. Advanced Identity Cloud derives it from the authentication method in the metadata document:* `private_key_jwt`, `tls_client_auth`, or `self_signed_tls_client_auth` produces a confidential client.

* Any other method produces a public client.CIMD clients are public by design but can authenticate confidentially using `private_key_jwt` or mTLS. This is what enables flows such as `client_credentials` for CIMD clients. |

## Limitations

The following features aren't supported for CIMD clients:

* UMA (User-Managed Access)

* CIBA (Client-Initiated Backchannel Authentication)

* Backchannel logout. Advanced Identity Cloud ignores `backchannel_logout_uri` and `backchannel_logout_session_required` in the metadata document.

* Wildcard ports in CIMD profile URL patterns, for example `https://app.example.com:*/`

* Client secrets and symmetric authentication methods

* Setting the client type (public or confidential). This is derived from the authentication method in the metadata document.

* Authorization response signing and encryption

The CIMD profile doesn't expose the following OAuth 2.0 client properties, and CIMD documents can't set them:

* JavaScript origins

* Access token endpoint override

* Software identity and version (`software_id` and `software_version`)

* Group

* Secret label identifier

Additionally, CIMD has the following constraints:

* If the matching profile requires pushed authorization requests, CIMD clients must use a [pushed authorization request (PAR)](oauth2-authz-grant-par.html).

  A direct authorization request without PAR is rejected.

* Advanced Identity Cloud doesn't advertise support for CIMD in its authorization server metadata yet, so clients can't tell whether a realm supports CIMD until they try a CIMD flow.

## Configure a CIMD profile

CIMD is controlled by *CIMD profiles*. Each profile defines a URL pattern that Advanced Identity Cloud matches against incoming `client_id` values, along with security settings for that pattern. You configure CIMD profiles per realm in the Advanced Identity Cloud admin console.

|   |                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You use CIMD profiles to allow or deny specific origins. If no CIMD profile matches the `client_id` URL, Advanced Identity Cloud rejects the request. |

1. Under Native Consoles > Access Management, go to Realms > *realm name* > Applications > OAuth 2.0 > CIMD Profiles.

2. Click Add CIMD Profile.

3. Enter a unique CIMD profile name that adheres to the following rules:

   * Must not start with the `#` or `"` characters.

   * Must not start or end with the space character.

   * Must not contain any of the following characters: `\/+;,%[]|?`.

   * Must not be `.` or `..`.

4. Enter a valid CIMD Client ID URL Pattern that starts with `https://`. Advanced Identity Cloud matches the URL pattern against incoming `client_id` values. For example, `https://app.example.com/*` allows all CIMD clients hosted under that origin.

5. Click Create.

6. Configure additional profile properties as required and save your changes.

   | Property                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                          |
   | -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | CIMD Client ID URL Patterns      | *Required*. One or more HTTPS URLs that the `client_id` value must match.Only `https://` patterns are accepted. Wildcard paths are accepted, for example `https://app.example.com/*` allows all CIMD clients hosted under that origin. An explicit port is allowed, for example `https://app.example.com:8443/*`, but wildcard ports aren't.                                                                                                         |
   | CIMD Metadata Override Deny List | *Optional*. A list of metadata field names that always use the profile value. Advanced Identity Cloud ignores the corresponding fields in CIMD documents matched by this profile. For example, select `scope` from the list to ensure the client can't override the scope in the profile with a different value in its metadata document.Use this to prevent clients from asserting sensitive metadata values that your realm policy doesn't permit. |
   | CIMD SSRF Protection Enabled     | When `true`, Advanced Identity Cloud blocks `client_id` URLs that resolve to special-use or loopback IP addresses, to prevent SSRF attacks.Only set to `false` in controlled test environments where the CIMD server runs on loopback.Default: `true`                                                                                                                                                                                                |

## Example authorization code flow

1. [Configure a CIMD profile](#cimd-configure) that allows the client to use its metadata document URL as the `client_id`.

   For test purposes, use the following values in the [example metadata document](#cimd-document-format) to create the profile:

   * CIMD Client ID URL Pattern

     `https://app.example.com/oauth/client.json`

   * CIMD Metadata Override Deny List

     `scope`

   * CIMD SSRF Protection Enabled

     `false`

2. Save the profile.

3. On the Core tab in the client profile, set Scope(s) to `openid` and save your changes.

4. [Get an authorization code](oauth2-authz-grant.html#proc-auth-code-browser) in a browser using the metadata document URL as the `client_id`:

   ```none
   https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/authorize
     ?client_id=https%3A%2F%2Fapp.example.com%2Foauth%2Fclient.json
     &response_type=code
     &redirect_uri=https%3A%2F%2Fapp.example.com%2Fcallback
     &scope=read
     &state=state
   ```

   |   |                                            |
   | - | ------------------------------------------ |
   |   | The URL is split for readability purposes. |

   Advanced Identity Cloud fetches and validates the metadata document, then proceeds with the standard flow.

5. [Exchange the authorization code for an access token](oauth2-authz-grant.html#proc-auth-code-token) using the same `client_id` URL:

   ```bash
   $ curl \
   --request POST \
   --data "grant_type=authorization_code" \
   --data "code=authorization-code" \
   --data "client_id=https://app.example.com/oauth/client.json" \
   --data "redirect_uri=https://app.example.com/callback" \
   'https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/access_token'
   {
     "access_token": "access-token",
     "refresh_token": "refresh-token",
     "scope":"openid",
     "id_token":"id-token",
     "token_type":"Bearer",
     "expires_in":3599
   }
   ```

   The `scope` in the access token is `openid`, which comes from the configured CIMD profile, not `read` from the authorization request, because the profile's metadata override denylist includes `scope`. The `id_token` is also returned.

---

---
title: Client-side tokens
description: Store OAuth 2.0 tokens as JWTs on clients with optional signing and encryption protection
component: pingoneaic
page_id: pingoneaic:am-oauth2:client-side-tokens
canonical_url: https://docs.pingidentity.com/pingoneaic/am-oauth2/client-side-tokens.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "Endpoints", "Clients", "Setup &amp; Configuration"]
page_aliases: ["oauth2-guide:client-side-tokens.adoc"]
section_ids:
  client_side_token_characteristics: Client-side token characteristics
  protect-client-side-tokens: Protect client-side tokens
  encrypt-tokens: Encrypt tokens
  sign-tokens: Sign tokens
---

# Client-side tokens

By default, Advanced Identity Cloud returns a token to the client after successfully completing one of the [OAuth 2.0 grant flows](oauth2-implementing-flows.html).

This example shows the encoded client-side token as a value of the `access_token` property:

```json
{
   "access_token":"eyJ0eXAiOiJKV1QiLOT05FIiwiYWxnQY1lIjoxNTM5MDEzMzYyLsbSI6Ii8iLCj...",
   "scope":"write",
   "token_type":"Bearer",
   "expires_in":3599
}
```

An access token contains a large amount of information about the user, permissions, validity, and so on. You can see the information when the token is decoded.

> **Collapse: Example decoded access token**
>
> ```json
> {
>      typ: "JWT",
>      zip: "NONE",
>      alg: "HS256"
> }
> {
>      sub: "(usr!myClient)",
>      subname" "myClient",
>      cts: "OAUTH2_STATELESS_GRANT",
>      auditTrackingId: "f20f4099-5248-4399-a7f0-2d54d4020099-108676",
>      iss: "https://<tenant-env-fqdn>/am/oauth2",
>      tokenName: "access_token",
>      token_type: "Bearer",
>      authGrantId: "1LUgI8zcDWqcfEnnLdZDnNqA2wc",
>      aud: "myClient",
>      nbf: 1539075967,
>      grant_type: "client_credentials",
>      scope: [
>       "write"
>      ],
>      auth_time: 1539075967,
>      realm: "/alpha",
>      exp: 1539079567,
>      iat: 1539075967,
>      expires_in: 3600,
>      jti: "FTQT6eZkDhm6PHEaSthORoTLB80"
> }
> [signature]
> ```

## Client-side token characteristics

* Client-side tokens are larger than the *reference* returned for server-side tokens.

  If you send client-side tokens in a header, pay attention to their size. The size of the token can't exceed the maximum header size allowed by your end users' browsers.

  The size of a token increases when you customize Advanced Identity Cloud to store additional attributes in tokens.

* Client-side tokens are presented to the client after successfully completing an OAuth 2.0 grant flow, which makes them vulnerable to tampering attacks.

  Configure Advanced Identity Cloud to [sign and encrypt](#protect-client-side-tokens) them to mitigate this risk.

* Client-side tokens can be introspected without calling the authorization server.

* They incur an overhead when they're decrypted and verified because Advanced Identity Cloud doesn't store the decrypt sequence of the token in memory.

* Client-side tokens support *token denylisting*.

  Advanced Identity Cloud maintains a list of revoked tokens and authorization codes stored in the CTS token store. Token denylisting protects against replay attacks and is *always enabled* for client-side tokens.

  When a client presents a client-side token in a request, Advanced Identity Cloud checks whether the token has been revoked in the CTS token store. If the token hasn't been revoked, Advanced Identity Cloud decrypts the token to retrieve its information.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | * Advanced Identity Cloud periodically polls the CTS for changes to logged-out sessions. There is a small window during which the CTS might not be updated with the latest denylisted client-side tokens. If this window isn't acceptable in your deployment, use server-side tokens instead.

  * Client-side *refresh* tokens have corresponding entries in a CTS allowlist rather than a denylist. When presenting a client-side refresh token, Advanced Identity Cloud checks that a matching entry is found in the CTS allowlist, and prevents reissue if the record doesn't exist.

    Adding a client-side OAuth 2.0 token to the denylist removes the associated refresh token from the allowlist. |

## Protect client-side tokens

To protect OAuth 2.0 client-side access and refresh tokens, Advanced Identity Cloud supports encrypting their JWTs using AES authenticated encryption. Because this encryption also protects the integrity of the JWT, you only need to configure Advanced Identity Cloud to sign client-side tokens if token encryption is disabled.

|   |                                                                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Client-side tokens must be signed and/or encrypted for security reasons. If your environment does not support encrypting OAuth 2.0 tokens, you must configure signing to protect them against tampering. |

### Encrypt tokens

To configure the OAuth 2.0 provider to encrypt client-side and refresh tokens:

1. In the Advanced Identity Cloud admin console, go to [icon: vpn_key, set=material, size=inline] Authorization > OAuth2 Provider.

2. On the Advanced tab, enable Encrypt Client-Side Tokens.

3. Save your changes.

   Client-side OAuth 2.0 access and refresh tokens will now be encrypted.

|   |                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When you enable token encryption, token *signature* is disabled because Advanced Identity Cloud encrypts tokens using direct symmetric encryption. |

### Sign tokens

Advanced Identity Cloud secures the integrity of client-side tokens by signing them with digital signature algorithms.

Token signature is enabled by default for client-side tokens, using a `demo` key. You must change this key in production environments.

Advanced Identity Cloud exposes the public key to validate client-side token signatures in its JWK URI ([/oauth2/connect/jwk_uri](../am-oidc1/managing-jwk_uri.html)).

To configure the algorithm used to sign client-side tokens:

1. Under [icon: open_in_new, set=material, size=inline] Native Consoles > Access Management, go to Realms > *Realm Name* > Services.

2. Select OAuth2 Provider and click the Advanced tab.

3. In the OAuth2 Token Signing Algorithm list, select algorithm to use for signing client-side tokens.

4. Save your changes.

---

---
title: Customize OAuth 2.0 using JavaScript extensions
description: Customize OAuth 2.0 authorization server functionality using JavaScript extensions
component: pingoneaic
page_id: pingoneaic:am-oauth2:plugins-customize
canonical_url: https://docs.pingidentity.com/pingoneaic/am-oauth2/plugins-customize.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "Customization", "Federation", "Scripting"]
page_aliases: ["oauth2-guide:plugins-customize.adoc"]
section_ids:
  supported_extensions: Supported extensions
  use-custom-oauth2-plugin: Configure the OAuth 2.0 provider to use extensions
  override-oauth2-provider-settings: Override OAuth 2.0 provider extension settings
---

# Customize OAuth 2.0 using JavaScript extensions

Advanced Identity Cloud lets you script extensions in JavaScript to customize OAuth 2.0 authorization server functionality, such as modifying access tokens or customizing how Advanced Identity Cloud processes scopes.

## Supported extensions

You can create scripts for each of the supported extension points [using the Advanced Identity Cloud admin console](../developer-docs/scripting-auth.html). The scripts have access to [bindings](../am-scripting/oauth2-scripting-api.html) to help you write your customization.

The following table describes the extensible features of an Advanced Identity Cloud OAuth 2.0 authorization server.

| Feature                                                                      | Extension options                                                                                                      | Samples                                                                                                          |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| [Access tokens](modifying-access-tokens-scripts.html)                        | Modify the OAuth 2.0 access token before the token is persisted or returned to the client.                             | [oauth2-access-token-modification.js](../_attachments/scripts/oauth2-access-token-modification.js)               |
| [Authorize endpoint data provider](plugins-auth-endpoint-data-provider.html) | Return additional data from an authorization request.                                                                  | [oauth2-authorize-endpoint-data-provider.js](../_attachments/scripts/oauth2-authorize-endpoint-data-provider.js) |
| [Scope evaluation](plugins-scope-evaluator.html)                             | Evaluate and return an OAuth 2.0 access token's scope information.                                                     | [oauth2-evaluate-scope.js](../_attachments/scripts/oauth2-evaluate-scope.js)                                     |
| [Scope validation](plugins-scope-validator.html)                             | Customize the requested scopes for authorization, access token, refresh token, and backchannel authorization requests. | [oauth2-validate-scope.js](../_attachments/scripts/oauth2-validate-scope.js)                                     |
| [OIDC claims](plugins-user-info-claims.html)                                 | Fetch the resource owner's information based on an issued access token.                                                | [oidc-claims-extension.js](../_attachments/scripts/oidc-claims-extension.js)                                     |

## Configure the OAuth 2.0 provider to use extensions

After creating a script, configure the OAuth 2.0 provider service to use it:

1. In the Advanced Identity Cloud admin console, go to [icon: vpn_key, set=material, size=inline] Authorization > OAuth2 Provider > Plugins.

2. []()For your extension, set the extension type to `SCRIPTED` and select your script from the appropriate list:

   | Extension                        | Extension type setting                       | Script list setting                     |
   | -------------------------------- | -------------------------------------------- | --------------------------------------- |
   | Access token modification        | Access Token Modification Plugin Type        | Access Token Modification Script        |
   | Authorize endpoint data provider | Authorize Endpoint Data Provider Plugin Type | Authorize Endpoint Data Provider Script |
   | Scope evaluator                  | Scope Evaluation Plugin Type                 | Scope Evaluation Provider Script        |
   | Scope validator                  | Scope Validation Plugin Type                 | Scope Validation Provider Script        |
   | User info claims                 | OIDC Claims Plugin Type                      | OIDC Claims Script                      |

Learn more about the provider settings in [OAuth2 provider plugins](../authorization/oauth2-provider-settings.html#realm-oauth-oidc-plugins).

## Override OAuth 2.0 provider extension settings

You can also configure extensions in client profiles that override the settings in the OAuth 2.0 provider.

1. Under Native Consoles > Access Management, go to Realms > *Realm Name* > Applications > OAuth 2.0 > Clients > *Client ID* > OAuth2 Provider Overrides.

2. Select Enable OAuth2 Provider Overrides.

3. Configure the client overrides in the same way as [the provider](#extension-settings). Set the extension type to `SCRIPTED` and select your script from the appropriate list.

---

---
title: Demonstrate delegation
description: Demonstrate OAuth 2.0 token exchange with delegation by exchanging an access token for one with reduced scopes
component: pingoneaic
page_id: pingoneaic:am-oauth2:token-exchange-delegation
canonical_url: https://docs.pingidentity.com/pingoneaic/am-oauth2/token-exchange-delegation.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "OpenID Connect (OIDC)", "Scripting", "Setup &amp; Configuration"]
page_aliases: ["oauth2-guide:token-exchange-delegation.adoc"]
section_ids:
  prepare_the_demonstration: Prepare the demonstration
  delegation-script: May act script
  delegation-subject-oauth2-client: Subject client
  delegation-actor-oauth2-client: Actor client
  delegation-resource-owner: Resource owner
  test_the_demonstration: Test the demonstration
---

# Demonstrate delegation

This page demonstrates [token exchange with delegation](token-exchange.html#token-exchange-delegation). The example exchanges an access token for an access token with reduced scopes. You can also exchange ID tokens with delegation.

## Prepare the demonstration

Start by preparing the demonstration:

* [Create a may act script](#delegation-script).

* [Create the OAuth 2.0 client the subject uses](#delegation-subject-oauth2-client).

* [Create the OAuth 2.0 client for delegation](#delegation-actor-oauth2-client).

* [Create a resource owner account](#delegation-resource-owner).

### May act script

The script adds a `may_act` claim to the subject token.

1. In the Advanced Identity Cloud admin console, [create a new](../developer-docs/scripting-auth.html#create-a-new-auth-script) OAuth2 May Act script.

2. Select either legacy or next-generation as the script engine.

3. In the new script window, name the script `May act` and save the following JavaScript:

   * Legacy

   * Next-generation

   ```javascript
   (function () {
       var frJava = JavaImporter(
           org.forgerock.json.JsonValue
       );

       var mayAct = frJava.JsonValue.json(frJava.JsonValue.object())
       mayAct.put('client_id', 'delegateClient')
       mayAct.put('sub', 'delegateClient')
       token.setMayAct(mayAct)
   }());
   ```

   ```javascript
   (function () {
       var mayAct = {
           'client_id': 'delegateClient',
           'sub': 'delegateClient'
       };
       token.setMayAct(mayAct);
   }());
   ```

   This script generates a `may_act` claim to permit the delegate actor client to exchange the subject token, provided it also supplies an actor token where it is the subject.

### Subject client

The OAuth 2.0 client profile in this example overrides the OAuth 2.0 provider settings. This lets you test the script without affecting access tokens issued to other clients.

1. Create a confidential OAuth 2.0 client account to get an original token for the subject.

   In the Advanced Identity Cloud admin console, go to Applications > Applications > + Custom Application, and create a new Web client with the following settings:

   * Client ID

     `myClient`

   * Client Secret

     `mySecret`

2. Add the following settings under Sign On > General Settings and save your work:

   * Sign-in URLs

     `https://www.example.com:443/callback`

   * Scopes

     `change_contract`\
     `repair`

3. Override OAuth 2.0 provider settings for this client.

   Under Native Consoles > Access Management, select Realms > alpha > Applications > OAuth 2.0 > Clients > myClient. Switch to the OAuth2 Provider Overrides tab, update the following settings and save your work:

   * Enable OAuth2 Provider Overrides

     Enabled

   * OAuth2 Access Token May Act Script

     `May act`

   * OIDC ID Token May Act Script

     `May act`

### Actor client

1. Create a confidential OAuth 2.0 client account for the service that acts on behalf of the user.

   In the Advanced Identity Cloud admin console, go to Applications > Applications > + Custom Application, and create a new Service client with the following settings:

   * Client ID

     `delegateClient`

   * Client Secret

     `mySecret`

2. Add the following settings under Sign On > General Settings and save your work:

   * Grant Types

     `Refresh Token`\
     `Token Exchange`

   * Scopes

     `repair`

### Resource owner

An OAuth 2.0 client requests the access token on behalf of a resource owner.

1. [Create a user profile](../identities/manage-identities.html#create-a-user-profile).

2. Record the username and password.

## Test the demonstration

After preparing the demonstration, test your work using HTTP calls to REST endpoints.

The demonstration uses the [Authorization code grant](oauth2-authz-grant.html) and and [Client credentials grant](oauth2-client-cred-grant.html) flows followed by token exchange:

* The resource owner authenticates to obtain an SSO token.

* The subject client relies on Implied Consent being enabled (default) in the Advanced Identity Cloud admin console under Applications > Applications > *Name* > Sign On > Advanced settings > Authentication. It assumes the resource owner grants the client access.

* The subject client requests the authorization code and exchanges it for an access token. Your script sets the `may_act` claim in the access token.

* The actor client requests an actor token with its client credentials.

* The actor client exchanges the subject token and actor token for an ID token.

Follow these steps:

1. Authenticate as the resource owner:

   ```bash
   curl \
   --request POST \
   --header 'Content-Type: application/json' \
   --header 'X-OpenAM-Username: <resource-owner-username>' \
   --header 'X-OpenAM-Password: <resource-owner-password>' \
   --header 'Accept-API-Version: resource=2.0, protocol=1.0' \
   'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate'
   {
     "tokenId": "<resource-owner-tokenId>",
     "successUrl": "/enduser/?realm=/alpha",
     "realm": "/alpha"
   }
   ```

2. Request the authorization code as the subject client:

   ```bash
   curl \
   --dump-header - \
   --request POST \
   --cookie '<session-cookie-name>=<resource-owner-tokenId>' \
   --data 'scope=change_contract repair' \
   --data 'response_type=code' \
   --data 'client_id=myClient' \
   --data 'csrf=<resource-owner-tokenId>' \
   --data 'redirect_uri=https://www.example.com:443/callback' \
   --data 'state=abc123' \
   --data 'decision=allow' \
   'https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/authorize'
   ...
   location: https://www.example.com:443/callback?code=<authorization-code>&iss=https%3A%2F%2F...
   ...
   ```

   |   |                                                                                                                                          |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you're exchanging an ID token instead of an access token, set `scope=openid profile` here to return the ID token in the next command. |

3. Exchange the authorization code for an access token or ID token as the subject client:

   ```bash
   curl \
   --request POST \
   --user 'myClient:mySecret' \
   --data 'grant_type=authorization_code' \
   --data 'code=<authorization-code>' \
   --data 'redirect_uri=https://www.example.com:443/callback' \
   'https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/access_token'
   {
     "access_token": "<subject-access-token>",
     "refresh_token": "<refresh-token>",
     "scope": "change_contract repair",
     "token_type": "Bearer",
     "expires_in": 3599
   }
   ```

   Your script has set the `may_act` claim, which is not directly visible. To see the `may_act` claim, you must [introspect](oauth2-introspect-endpoint.html) the access token.

4. Request an access token as the actor client:

   ```bash
   curl \
   --request POST \
   --user 'delegateClient:mySecret' \
   --data 'grant_type=client_credentials' \
   --data 'scope=repair' \
   'https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/access_token'
   {"access_token":"<actor-access-token>","scope":"repair","token_type":"Bearer","expires_in":3599}
   ```

5. Request an exchanged token as the actor client:

   ```bash
   curl \
   --request POST \
   --user 'delegateClient:mySecret' \
   --data 'grant_type=urn:ietf:params:oauth:grant-type:token-exchange' \
   --data 'scope=repair' \
   --data 'subject_token=<subject-access-token>' \
   --data 'subject_token_type=urn:ietf:params:oauth:token-type:access_token' \
   --data 'actor_token=<actor-access-token>' \
   --data 'actor_token_type=urn:ietf:params:oauth:token-type:access_token' \
   --data 'requested_token_type=urn:ietf:params:oauth:token-type:id_token' \
   'https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/access_token'
   {
     "access_token": "<exchanged-id-token>",
     "refresh_token": "<new-refresh-token>,"
     "issued_token_type": "urn:ietf:params:oauth:token-type:id_token",
     "scope": "repair",
     "token_type": "Bearer",
     "expires_in": 3599
   }
   ```

   The `issued_token_type` shows this is an exchanged token.

   |   |                                                                                                                                                                                                |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If your subject token is an ID token rather than an access token, set `subject_token_type=urn:ietf:params:oauth:token-type:id_token` and provide the ID token as the value of `subject_token`. |

---

---
title: Demonstrate impersonation
description: "Demonstrate OAuth 2.0 token exchange with impersonation by exchanging tokens for others' access"
component: pingoneaic
page_id: pingoneaic:am-oauth2:token-exchange-impersonation
canonical_url: https://docs.pingidentity.com/pingoneaic/am-oauth2/token-exchange-impersonation.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "OpenID Connect (OIDC)", "Scripting", "Setup &amp; Configuration"]
page_aliases: ["oauth2-guide:token-exchange-impersonation.adoc"]
section_ids:
  prepare_the_demonstration: Prepare the demonstration
  impersonation-script: May act script
  impersonation-subject-oauth2-client: Subject client
  impersonation-actor-oauth2-client: Actor client
  impersonation-resource-owner: Resource owner
  test_the_demonstration: Test the demonstration
---

# Demonstrate impersonation

This page demonstrates [token exchange with impersonation](token-exchange.html#token-exchange-impersonation). The example exchanges an access token for an access token with reduced scopes. You can also exchange ID tokens with impersonation.

## Prepare the demonstration

Start by preparing the demonstration:

* [Create a may act script](#impersonation-script).

* [Create the OAuth 2.0 client the subject uses](#impersonation-subject-oauth2-client).

* [Create the OAuth 2.0 client for impersonation](#impersonation-actor-oauth2-client).

* [Create a resource owner account](#impersonation-resource-owner).

### May act script

The script adds a `may_act` claim to the subject token.

1. In the Advanced Identity Cloud admin console, [create a script](../developer-docs/scripting-auth.html#create-a-new-auth-script) of type OAuth2 May Act.

2. Select either legacy or next-generation as the script engine.

3. In the new script window, name the script `May act` and save the following JavaScript:

   * Legacy

   * Next-generation

   ```javascript
   (function () {
       var frJava = JavaImporter(
           org.forgerock.json.JsonValue
       );

       var mayAct = frJava.JsonValue.json(frJava.JsonValue.object())
       mayAct.put('client_id', 'impersonationClient')
       token.setMayAct(mayAct)
   }());
   ```

   ```javascript
   (function () {
       var mayAct = {
           'client_id': 'impersonationClient'
       };
       token.setMayAct(mayAct);
   }());
   ```

   This script generates a `may_act` claim to permit the impersonating actor client to exchange the subject token.

### Subject client

The OAuth 2.0 client profile in this example overrides the OAuth 2.0 provider settings. This lets you test the script without affecting access tokens issued to other clients.

1. Create a confidential OAuth 2.0 client account to get an original token for the subject.

   In the Advanced Identity Cloud admin console, go to Applications > Applications > + Custom Application, and create a new Web client with the following settings:

   * Client ID

     `myClient`

   * Client Secret

     `mySecret`

2. Add the following settings under Sign On > General Settings and save your work:

   * Sign-in URLs

     `https://www.example.com:443/callback`

   * Scopes

     `change_data`\
     `create_accounts`\
     `read_accounts`\
     `transfer`

3. Override OAuth 2.0 provider settings for this client.

   Under Native Consoles > Access Management, select Realms > alpha > Applications > OAuth 2.0 > Clients > myClient. Switch to the OAuth2 Provider Overrides tab, update the following settings and save your work:

   * Enable OAuth2 Provider Overrides

     Enabled

   * OAuth2 Access Token May Act Script

     `May act`

   * OIDC ID Token May Act Script

     `May act`

### Actor client

1. Create a confidential OAuth 2.0 client account for the service that acts on behalf of the user.

   In the Advanced Identity Cloud admin console, select Applications > Applications > + Custom Application, and create a new Service client with the following settings:

   * Client ID

     `impersonationClient`

   * Client Secret

     `mySecret`

2. Add the following settings under Sign On > General Settings and save your work:

   * Sign-in URLs

     `https://www.example.com:443/callback`

   * Grant Types

     `Refresh Token`\
     `Token Exchange`

   * Scopes

     `transfer`

### Resource owner

An OAuth 2.0 client requests the access token on behalf of a resource owner.

1. [Create a user profile](../identities/manage-identities.html#create-a-user-profile).

2. Record the username and password.

## Test the demonstration

After preparing the demonstration, test your work using HTTP calls to REST endpoints.

The demonstration uses the [Authorization code grant](oauth2-authz-grant.html) flow followed by token exchange:

* The resource owner authenticates to obtain an SSO token.

* The subject client relies on Implied Consent being enabled (default) in the Advanced Identity Cloud admin console under Applications > Applications > *Name* > Sign On > Advanced settings > Authentication. It assumes the resource owner grants the client access.

* The subject client requests the authorization code and exchanges it for an access token. Your script sets the `may_act` claim in the access token.

* The actor client exchanges the subject token for an access token.

Follow these steps:

1. Authenticate as the resource owner:

   ```bash
   curl \
   --request POST \
   --header 'Content-Type: application/json' \
   --header 'X-OpenAM-Username: <resource-owner-username>' \
   --header 'X-OpenAM-Password: <resource-owner-password>' \
   --header 'Accept-API-Version: resource=2.0, protocol=1.0' \
   'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate'
   {
     "tokenId": "<resource-owner-tokenId>",
     "successUrl": "/enduser/?realm=/alpha",
     "realm": "/alpha"
   }
   ```

2. Request the authorization code as the subject client:

   ```bash
   curl \
   --dump-header - \
   --request POST \
   --cookie '<session-cookie-name>=<resource-owner-tokenId>' \
   --data 'scope=change_data create_accounts read_accounts transfer' \
   --data 'response_type=code' \
   --data 'client_id=myClient' \
   --data 'csrf=<resource-owner-tokenId>' \
   --data 'redirect_uri=https://www.example.com:443/callback' \
   --data 'state=abc123' \
   --data 'decision=allow' \
   'https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/authorize'
   ...
   location: https://www.example.com:443/callback?code=<authorization-code>&iss=https%3A%2F%2F...
   ...
   ```

   |   |                                                                                                                                          |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you're exchanging an ID token instead of an access token, set `scope=openid profile` here to return the ID token in the next command. |

3. Exchange the authorization code for an access token or ID token as the subject client:

   ```bash
   curl \
   --request POST \
   --user 'myClient:mySecret' \
   --data 'grant_type=authorization_code' \
   --data 'code=<authorization-code>' \
   --data 'redirect_uri=https://www.example.com:443/callback' \
   'https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/access_token'
   {
     "access_token": "<access-token>",
     "refresh_token": "<refresh-token>",
     "scope": "change_data transfer create_accounts read_accounts",
     "token_type": "Bearer",
     "expires_in": 3599
   }
   ```

   Your script has set the `may_act` claim, which is not directly visible. To see the `may_act` claim, you must [introspect](oauth2-introspect-endpoint.html) the access token.

4. Request an exchanged token as the actor client:

   ```bash
   curl \
   --request POST \
   --user 'impersonationClient:mySecret' \
   --data 'grant_type=urn:ietf:params:oauth:grant-type:token-exchange' \
   --data 'scope=transfer' \
   --data 'subject_token=<access-token>' \
   --data 'subject_token_type=urn:ietf:params:oauth:token-type:access_token' \
   'https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/access_token'
   {
     "access_token": "<exchanged-token>",
     "refresh_token": "<new-refresh-token>",
     "issued_token_type": "urn:ietf:params:oauth:token-type:access_token",
     "scope": "transfer",
     "token_type": "Bearer",
     "expires_in": 3599
   }
   ```

   The `issued_token_type` shows this is an exchanged token.

   |   |                                                                                                                                                                                                |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If your subject token is an ID token rather than an access token, set `subject_token_type=urn:ietf:params:oauth:token-type:id_token` and provide the ID token as the value of `subject_token`. |

---

---
title: Device authorization grant
description: Enable input-constrained devices to request authorization using separate user agents for consent
component: pingoneaic
page_id: pingoneaic:am-oauth2:oauth2-device-flow
canonical_url: https://docs.pingidentity.com/pingoneaic/am-oauth2/oauth2-device-flow.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "Endpoints", "Authorization", "Grant Flow", "REST API", "Browser"]
page_aliases: ["oauth2-guide:oauth2-device-flow.adoc"]
section_ids:
  device-flow: The device authorization grant flow
  demo-device: Demonstrate the device authorization grant flow
  prepare-demo-device: Prepare the demonstration
  proc-device-flow-request-user-code: Get a user code for the device
  proc-device-flow-allow-access-no-browser: Grant consent using REST
  proc-device-flow-allow-access-browser: Grant consent using a browser
  proc-device-flow-poll-for-authz: Poll for authorization
---

# Device authorization grant

* Endpoints

  * [/oauth2/device/code](rest-api-oauth2-device-code.html)

  * [/oauth2/device/user](rest-api-oauth2-device-user.html)

  * [/oauth2/access_token](oauth2-access_token-endpoint.html)

The device authorization grant, formerly known as the device flow, is designed for client devices that have limited user interfaces, such as a set-top box, streaming radio, or a server process running on a headless operating system.

Instead of logging in with the client device, you can authorize the client to access protected resources on your behalf. You log in with a different user agent, such as a phone or Internet browser, and authenticate using a code that the client device displays.

## The device authorization grant flow

![Advanced Identity Cloud acting as the authorization server in the OAuth 2.0 device flow.](_images/oauth2-device-flow.svg)Figure 1. OAuth 2.0 device authorization grant flow

1. The client device requests a device code from Advanced Identity Cloud.

2. Advanced Identity Cloud returns a device code, a user code, a URL for entering the user code, and an interval, in seconds.

3. The client device provides instructions to the user. The client can choose an appropriate method to convey the instructions, for example, text instructions on screen, or a QR code.

4. The client device continuously polls Advanced Identity Cloud to check if authorization has completed.

5. If the user hasn't completed the authorization, Advanced Identity Cloud returns an HTTP 403 status code with an `authorization_pending` message.

6. The user is redirected to Advanced Identity Cloud's login page to authenticate.

7. Advanced Identity Cloud retrieves the associated device code and determines if any Authentication Context Class References (ACRs) were explicitly requested.

   * If ACRs were requested, they're used to determine the authentication journey.

   * If no ACRs were requested, Advanced Identity Cloud uses the default ACRs configured either at the client or OAuth 2.0 provider level.

8. On authentication, Advanced Identity Cloud prompts the user to confirm the user code and pre-populates the page with the code entered previously.

9. The user can authorize the client device. The Advanced Identity Cloud consent page also displays the requested scopes and their values.

   |   |                                                                                                                                                                                                                                                                                      |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | If the user had a valid session when they entered the code and the client is configured to skip consent, Advanced Identity Cloud doesn't display the confirmation or the consent pages.This is also true if you perform the call using REST and pass the `decision=allow` parameter. |

10. On authorization, Advanced Identity Cloud responds to the client device's polling with an HTTP 200 status and an access token, giving the client device access to the requested resources.

## Demonstrate the device authorization grant flow

Follow these steps to demonstrate the OAuth 2.0 device grant flow:

* [Prepare the demonstration](#prepare-demo-device)

* [Get a user code for the device](#proc-device-flow-request-user-code)

* [Grant consent using a browser](#proc-device-flow-allow-access-browser) or [Grant consent using REST](#proc-device-flow-allow-access-no-browser)

* [Poll for authorization](#proc-device-flow-poll-for-authz)

### Prepare the demonstration

Complete these steps to prepare the device authorization grant demonstration:

1. [Create an application owner profile](../identities/manage-identities.html#create-a-user-profile) and record the username and password.

2. [Register a client application](../app-management/register-a-custom-application.html).

   1. In the Advanced Identity Cloud admin console, go to Applications > Applications and select + Custom Application.

   2. Select the sign-in method as OIDC - OpenId Connect and application type as Native / SPA.

   3. Create the application, providing the following details:

      * Name

        `myClient`

      * Owners

        `<application-owner>`

      * Client ID

        `myClient`

   4. Switch to the Sign On tab and under General Settings, set these fields to have the following values:

      * Sign-in URLs

        `https://www.example.com:443/callback`

      * Scopes

        `write`

      * Grant Types

        `Device Code`

   5. Save your changes.

3. [Create a resource owner profile](../identities/manage-identities.html#create-a-user-profile) and record the username and password.

### Get a user code for the device

Devices can display a user code and instructions for a user. You can use these instructions on a separate client to provide consent, allowing the device to access resources.

User codes consist of a random selection of characters. You can configure the character set.

By default, Advanced Identity Cloud generates the user code from eight of the following characters:

```
234567ABCDEFGHIJKLMNOPQRSTVWXYZabcdefghijkmnopqrstvwxyz
```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can configure the list of possible characters to improve usability. For example, remove similar characters such as `4` and `A` to reduce ambiguity on low-resolution device screens, or limit input to either alphabetical or numerical characters to suit mobile keyboards.The length of the user code is also configurable.Find details on each configuration property in [device flow configuration](../authorization/oauth2-provider-settings.html#realm-oauth-oidc-device-flow). |

Perform the following steps to request a user code in the OAuth 2.0 device flow:

1. As the client, call the [/oauth2/device/code](rest-api-oauth2-device-code.html) endpoint, specifying at least the client ID, `myClient`.

   For information about client authentication methods, refer to [Client application authentication](oauth2-client-auth.html).

   For example:

   ```bash
   $ curl \
   --request POST \
   --data "client_id=myClient" \
   --data "scope=write" \
   "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/device/code"
   {
       "interval": 5,
       "device_code": "7a95a0a4-6f13-42e3-ac3e-d3d159c94c55...",
       "verification_uri": "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/device/user",
       "verification_url": "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/device/user",
       "verification_uri_complete": "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/device/user?user_code=VAL12e0v",
       "user_code": "VAL12e0v",
       "expires_in": 300
   }
   ```

   On success, Advanced Identity Cloud returns a user code, a `verification_uri`, and a `verification_uri_complete` value that comprises the user code appended to the URI. You can use the `verification_uri_complete` value to create QR codes.

   The output includes the `verification_url` to support earlier versions of the specification.

   Advanced Identity Cloud also returns an interval, in seconds, that the client device must wait before it can request an access token again.

   |   |                                                                                                                                                                                |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | In the Advanced Identity Cloud admin console, go to [icon: vpn_key, set=material, size=inline] Authorization > OAuth2 Provider > Device Flow to configure the returned values. |

2. The client device must now instruct the user to enter the user code and grant access to the OAuth 2.0 device.

   The client can choose an appropriate method to convey the instructions, for example, text instructions on screen or a QR code. Perform the steps in one of the following procedures:

   * To grant access to the client without using a browser, refer to [Grant consent using REST](#proc-device-flow-allow-access-no-browser).

   * To grant access to the client using a browser, refer to [Grant consent using a browser](#proc-device-flow-allow-access-browser).

3. The client device must start polling the authorization server for the access token using the interval and device code information obtained in the previous step.

   For more information, refer to [Poll for authorization](#proc-device-flow-poll-for-authz).

### Grant consent using REST

The OAuth 2.0 device authorization grant requires the user to grant consent to let a client device access a resource. The authorization server provides the client with an access token.

To grant consent with a user code without using a browser, perform the following steps:

1. The resource owner logs in to the authorization server.

   For example:

   ```bash
   $ curl \
   --include \
   --request POST \
   --header "Content-Type: application/json" \
   --header "X-OpenAM-Username: <resource-owner-username>" \
   --header "X-OpenAM-Password: <resource-owner-password>" \
   --header "Accept-API-Version: resource=2.0, protocol=1.0" \
   'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate'
   {
     "tokenId":"<tokenId>",
     "successUrl":"/enduser/?realm=/alpha",
     "realm":"/alpha
   "}
   ```

2. As the client, call the [/oauth2/device/user](rest-api-oauth2-device-user.html) endpoint. Provide the resource owner's SSO token in a cookie, and at least the following parameters:

   * **`user_code`**=\<resource-owner-user-code>

   * **`decision`**=`allow`

   * **`csrf`**=\<tokenId>

   The `scope` and the `client_id` parameters aren't required because the user code already contains that information.

   ```bash
   $ curl \
   --request POST \
   --header "Cookie: <session-cookie-name>=<tokenId>" \
   --data "user_code=VAL12e0v" \
   --data "decision=allow" \
   --data "csrf=<tokenId>" \
   "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/device/user"
   ```

   Advanced Identity Cloud returns HTML containing a JavaScript fragment named `pageData`, with details of the result. The following example shows the default HTML response:

   ```html
   <!DOCTYPE html>
   <!--
     Copyright …​
   -→
   <html lang="en">
   <head>
     <meta charset="utf-8">
     <meta http-equiv="X-UA-Compatible" content="IE=edge">
     <meta name="viewport" content="width=device-width, initial-scale=1">
     <meta name="description" content="OAuth2 Authorization">
     <title>OAuth2 Authorization Server</title>
   </head>

   <body style="display:none">
   <div id="wrapper">Loading…​</div>
   <footer id="footer" class="footer"></footer>
   <script type="text/javascript">
     pageData = {
         locale: "en_US",
         baseUrl : "https://<tenant-env-fqdn>/am",
         realm : "\/alpha",
         done: true
     };
   </script>
   <script src="https://<tenant-env-fqdn>/am/main-device.js"></script>
   </body>
   </html>
   ```

   The `done: true` line in the `pageData` fragment means the flow can continue.

   To return the output in JSON format instead of HTML, include the `Accept: application/json` header in the request. The following example returns the output in JSON:

   ```bash
   $ curl \
   --request POST \
   --header "Cookie: iPlanetDirectoryPro=ne1QUOjPzY0r…​" \
   --header "Accept: application/json" \
   --data "user_code=Gp4qkX4G" \
   --data "decision=allow" \
   --data "csrf=ne1QUOjPzY0r…​" \
   "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/device/user"
   {
     "baseUrl": "https://<tenant-env-fqdn>/am",
     "errorCode": null,
     "realm": "/alpha",
     "csrf": "1hQSplblZgaErLQ0/1rvcEvw5lj/cJQx3lrC3dV/3ac=",
     "locale": "en_US",
     "userCode": "Gp4qkX4G"
   }
   ```

   In this case, the `"errorCode": null` means the request is successful and the flow can continue.

   If the supplied user code is wrong or has been used, the output includes the following `pageData` fragment:

   ```javascript
   pageData = {
       locale: "en_US",
       errorCode: "not_found",
       realm : "/alpha",
       baseUrl : "https://<tenant-env-fqdn>/am"
       oauth2Data: {
             csrf: "ErFIk8pMraJ1rvKbloTgpp6b7GZ57kyk9HaIiKMVK3g=",
             userCode: "VAL12e0v"
       }
   }
   ```

|   |                                                                                                                                                                                                                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In accordance with [Section 4.1.1 of the OAuth 2.0 authorization framework](https://www.rfc-editor.org/rfc/rfc6749.html#section-4.1.1), the authorization server *must* obtain an authorization decision from the resource owner.Clients using the endpoints to register consent must ensure this requirement is met. Advanced Identity Cloud can't assert that consent was given in these cases. |

### Grant consent using a browser

The OAuth 2.0 device flow requires that the user grants consent to allow the client device to access the resources.

The authorization server would then provide the client with an access token.

To grant consent with a user code using a browser, perform the following steps:

1. The resource owner navigates to the verification URL acquired with the user code. For example:

   ```none
   https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/device/user
   ```

2. The resource owner logs in to the authorization server.

3. The resource owner enters their user code:

   ![Visit the verification URL to enter the user code.](_images/oauth2-device-user-code.png)Figure 2. OAuth 2.0 User Code

   |   |                                                                                                                                                                                                                        |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The `verification_uri_complete` property in the response appends the user code as a query parameter.Advanced Identity Cloud prefills the form with the user code value if provided in the `user_code` query parameter. |

4. The resource owner authorizes the device flow client by allowing the requested scopes:

   ![Advanced Identity Cloud lists the scopes requested by the client device, and their values.](_images/oauth2-authz-page-xui.png)Figure 3. OAuth 2.0 Consent Page

   |   |                                                                                                                                                                  |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | By default, client applications use [implied consent](oauth2-manage-consent.html#skip-consent). Advanced Identity Cloud does not display the screen to the user. |

5. Advanced Identity Cloud adds the OAuth 2.0 client to the user's profile page in the *Authorized Apps* section and displays that the user is done with the flow:

   ![The user code part of the device flow is done.](_images/oauth2-authz-page-done.png)Figure 4. OAuth 2.0 Done Page

   The device that polls the authorization server (Advanced Identity Cloud) can now obtain an access token.

### Poll for authorization

The client device must poll the authorization server for an access token, since it cannot know whether the resource owner has already given consent or not.

Perform the following steps to poll for an access token:

1. On the client device, create a POST request to poll the `/oauth2/access_token` endpoint to request an access token specifying, at least, the following parameters:

   * **`client_id`**=\<your-client-id>

   * **`grant_type`**=`urn:ietf:params:oauth:grant-type:device_code`

   * **`device_code`**=\<your-device-code>

   For information about the parameters supported by the `/oauth2/access_token` endpoint, refer to [/oauth2/access_token](oauth2-access_token-endpoint.html).

   The client device must wait for the number of seconds previously provided as the value of `interval` between polling Advanced Identity Cloud for an access token. For example:

   ```bash
   $ curl \
   --request POST \
   --data "client_id=myClient" \
   --data "grant_type=urn:ietf:params:oauth:grant-type:device_code" \
   --data "device_code=<your-device-code>" \
   "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/access_token"
   ```

   If the user has authorized the client device, Advanced Identity Cloud returns an HTTP 200 status code with an access token that can be used to request resources:

   ```json
   {
       "access_token": "<access-token>",
       "refresh_token": "<refresh-token>",
       "scope": "write",
       "token_type": "Bearer",
       "expires_in": 3599
   }
   ```

   If the user hasn't authorized the client device, Advanced Identity Cloud returns an HTTP 403 status code with the following error message:

   ```json
   {
       "error": "authorization_pending",
       "error_description": "The user has not yet completed authorization"
   }
   ```

   If the client device polls faster than the specified interval, Advanced Identity Cloud returns an HTTP 400 status code with the following error message:

   ```json
   {
       "error": "slow_down",
       "error_description": "The polling interval has not elapsed since the last request"
   }
   ```

---

---
title: Device authorization grant with PKCE
description: Combine device flow with PKCE to securely authenticate input-constrained device clients
component: pingoneaic
page_id: pingoneaic:am-oauth2:oauth2-device-flow-pkce
canonical_url: https://docs.pingidentity.com/pingoneaic/am-oauth2/oauth2-device-flow-pkce.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "Endpoints", "Authorization", "Grant Flow", "REST API", "Browser", "PKCE"]
page_aliases: ["oauth2-guide:oauth2-device-flow-pkce.adoc"]
section_ids:
  device-flow-pkce: The device authorization grant flow with PKCE
  demo-device-pkce: Demonstrate the device authorization grant flow with PKCE
  prepare-demo-device-pkce: Prepare the demonstration
  proc-device-flow-request-user-code-pkce: Get a user code for the device
  proc-device-flow-allow-access-no-browser-pkce: Grant consent using REST
  proc-device-flow-allow-access-browser-pkce: Grant consent using a browser
  proc-device-flow-poll-for-authz-pkce: Poll for authorization
---

# Device authorization grant with PKCE

* Endpoints

  * [/oauth2/device/code](rest-api-oauth2-device-code.html)

  * [/oauth2/device/user](rest-api-oauth2-device-user.html)

  * [/oauth2/access_token](oauth2-access_token-endpoint.html)

The device authorization grant is designed for client devices that have limited user interfaces, such as a set-top box. Because the devices are usually public clients, it's possible for malicious users to intercept the device code. If a device allows it, you can mitigate against interception attacks by combining the device authorization grant with the Proof Key for Code Exchange (PKCE) standard ([RFC 7636](https://www.rfc-editor.org/info/rfc7636)).

Advanced Identity Cloud implements this grant by adding the following parameters to those used for the [device authorization grant](#oauth2-device-flow):

* `code_verifier`

  Contains a random string that correlates the authorization request to the token request.

* `code_challenge`

  Contains a string derived from the code verifier that is sent in the authorization request and needs to be verified later with the code verifier.

* `code_challenge_method`

  Contains the method used to derive the code challenge.

## The device authorization grant flow with PKCE

![Advanced Identity Cloud acting as the authorization server in the OAuth 2.0 device flow with PKCE.](_images/oauth2-device-flow-pkce.svg)Figure 1. OAuth 2.0 device authorization grant flow with PKCE

1. When using the PKCE standard, the device must be able to generate a code verifier and a code challenge. For details, refer to the PKCE standard ([RFC 7636](https://www.rfc-editor.org/info/rfc7636)).

   For examples that generate a code verifier and a code challenge, refer to [Generate a code verifier and a code challenge](oauth2-authz-grant-pkce.html#proc-auth-code-generate-pkce).

2. The client device requests a device code from Advanced Identity Cloud, appending the code challenge previously generated to the request.

3. Advanced Identity Cloud returns a device code, a user code, a URL for entering the user code, and an interval, in seconds.

4. The client device provides instructions to the user to enter the user code. The client can choose an appropriate method to convey the instructions, for example, text instructions on screen, or a QR code.

5. The client device begins to continuously poll Advanced Identity Cloud to check if authorization has been completed, appending the code verifier previously generated.

6. If the user has not yet completed the authorization, Advanced Identity Cloud returns an HTTP 403 status code, with an `authorization_pending` message.

7. The user follows the instructions from the client device to enter the user code by using a separate device.

8. Advanced Identity Cloud verifies the code challenge stored in memory using the validation code. It also verifies the user code.

   If both codes are valid, Advanced Identity Cloud uses the user code to retrieve the associated device code and determine if any Authentication Context Class References (ACRs) were explicitly requested.

   * If ACRs were requested, they're used to determine the authentication journey.

   * If no ACRs were requested, Advanced Identity Cloud uses the default ACRs configured either at the client or OAUTH 2.0 provider level.

9. Advanced Identity Cloud redirects the user for authentication.

10. Upon authentication, the user is prompted to confirm the user code. The page is pre-populated with the one entered before.

11. The user can authorize the client device. The Advanced Identity Cloud consent page also displays the requested scopes, and their values.

    |   |                                                                                                                                                                                                                                                                       |
    | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | If the user has a valid session when they enter the code and the client can skip consent, Advanced Identity Cloud doesn't display the confirmation or the consent pages.This is also true if you perform the call using REST and pass the `decision=allow` parameter. |

12. Upon authorization, Advanced Identity Cloud responds to the client device's polling with an HTTP 200 status, and an access token, giving the client device access to the requested resources.

## Demonstrate the device authorization grant flow with PKCE

Follow these steps to grant consent with a user code and poll for authorization:

* [Prepare the demonstration](#prepare-demo-device-pkce)

* [Get a user code for the device](#proc-device-flow-request-user-code-pkce)

* [Grant consent using a browser](#proc-device-flow-allow-access-browser-pkce) or [Grant consent using REST](#proc-device-flow-allow-access-no-browser-pkce)

* [Poll for authorization](#proc-device-flow-poll-for-authz-pkce)

### Prepare the demonstration

Complete these steps to prepare the device authorization grant demonstration:

1. [Create an application owner profile](../identities/manage-identities.html#create-a-user-profile) and record the username and password.

2. [Register a client application](../app-management/register-a-custom-application.html).

   1. In the Advanced Identity Cloud admin console, go to Applications > Applications and select + Custom Application.

   2. Select the sign-in method as OIDC - OpenId Connect and application type as Native / SPA.

   3. Create the application, providing the following details:

      * Name

        `myClient`

      * Owners

        `<application-owner>`

      * Client ID

        `myClient`

   4. Switch to the Sign On tab and under General Settings, set these fields to have the following values:

      * Sign-in URLs

        `https://www.example.com:443/callback`

      * Scopes

        `write`

      * Grant Types

        `Device Code`

      |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | The `Code Verifier Parameter Required` setting (in the Advanced Identity Cloud admin console, under [icon: vpn_key, set=material, size=inline] Authorization > OAuth2 Provider > Advanced) specifies whether Advanced Identity Cloud requires clients to include a code verifier in their calls.However, if a client makes a call to Advanced Identity Cloud with the `code_challenge` parameter, Advanced Identity Cloud honors the code exchange regardless of the value of `Code Verifier Parameter Required`. Find more information in [Configure Advanced Identity Cloud as an authorization server](../authorization/oauth2-provider.html). |

   5. Save your changes.

3. [Create a resource owner profile](../identities/manage-identities.html#create-a-user-profile) and record the username and password.

### Get a user code for the device

Devices can display a user code and instructions for a user. These can be used on a separate client to provide consent, allowing the device to access the resources.

Devices can display a user code and instructions for a user. You can use these instructions on a separate client to provide consent, allowing the device to access resources.

User codes consist of a random selection of characters. You can configure the character set.

By default, Advanced Identity Cloud generates the user code from eight of the following characters:

```
234567ABCDEFGHIJKLMNOPQRSTVWXYZabcdefghijkmnopqrstvwxyz
```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can configure the list of possible characters to improve usability. For example, remove similar characters such as `4` and `A` to reduce ambiguity on low-resolution device screens, or limit input to either alphabetical or numerical characters to suit mobile keyboards.The length of the user code is also configurable.Find details on each configuration property in [device flow configuration](../authorization/oauth2-provider-settings.html#realm-oauth-oidc-device-flow). |

Perform the following steps to request a user code in the OAuth 2.0 device flow:

1. As the client, call the [/oauth2/device/code](rest-api-oauth2-device-code.html) endpoint, specifying at least the following parameters:

   * **`client_id`**=\<your-client-id>

   * **`code_challenge`**=\<your-code-challenge>

   * **`code_challenge_method`**=S256

     Creating the challenge using a SHA-256 algorithm is mandatory if the device supports it, as per [RFC 7636](https://www.rfc-editor.org/rfc/rfc7636).

     Refer to [Generate a code verifier and a code challenge](oauth2-authz-grant-pkce.html#proc-auth-code-generate-pkce).

   For information about client authentication methods, refer to [Client application authentication](oauth2-client-auth.html).

   For example:

   ```bash
   $ curl \
   --request POST \
   --data "client_id=myClient" \
   --data "code_challenge=<your-code-challenge>" \
   --data "code_challenge_method=S256" \
   --data "scope=write" \
   "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/device/code"
   {
       "interval": 5,
       "device_code": "7a95a0a4-6f13-42e3-ac3e-d3d159c94c55...",
       "verification_uri": "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/device/user",
       "verification_url": "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/device/user",
       "verification_uri_complete": "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/device/user?user_code=VAL12e0v",
       "user_code": "VAL12e0v",
       "expires_in": 300
   }
   ```

   On success, Advanced Identity Cloud returns a user code, a `verification_uri`, and a `verification_uri_complete` value that comprises the user code appended to the URI. You can use the `verification_uri_complete` value to create QR codes.

   The output includes the `verification_url` to support earlier versions of the specification.

   Advanced Identity Cloud also returns an interval, in seconds, that the client device must wait before it can request an access token again.

   |   |                                                                                                                                                                                |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | In the Advanced Identity Cloud admin console, go to [icon: vpn_key, set=material, size=inline] Authorization > OAuth2 Provider > Device Flow to configure the returned values. |

2. The client device should now provide instructions to the user to enter the user code and grant access to the OAuth 2.0 device.

   The client can choose an appropriate method to convey the instructions, for example, text instructions on screen, or a QR code. Perform the steps in one of the following procedures:

   * To grant access to the client using a browser, refer to [Grant consent using a browser](#proc-device-flow-allow-access-browser-pkce).

   * To grant access to the client without using a browser, refer to [Grant consent using REST](#proc-device-flow-allow-access-no-browser-pkce).

3. The client device should also begin polling the authorization server for the access token using the interval and device code information obtained in the previous step and the PKCE code verifier.

For more information, refer to [Poll for authorization](#proc-device-flow-poll-for-authz-pkce).

### Grant consent using REST

The OAuth 2.0 device authorization grant requires the user to grant consent to let a client device access a resource. The authorization server provides the client with an access token.

To grant consent with a user code without using a browser, perform the following steps:

1. The resource owner logs in to the authorization server.

   For example:

   ```bash
   $ curl \
   --include \
   --request POST \
   --header "Content-Type: application/json" \
   --header "X-OpenAM-Username: <resource-owner-username>" \
   --header "X-OpenAM-Password: <resource-owner-password>" \
   --header "Accept-API-Version: resource=2.0, protocol=1.0" \
   'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate'
   {
     "tokenId":"<tokenId>",
     "successUrl":"/enduser/?realm=/alpha",
     "realm":"/alpha
   "}
   ```

2. As the client, call the [/oauth2/device/user](rest-api-oauth2-device-user.html) endpoint. Provide the resource owner's SSO token in a cookie, and at least the following parameters:

   * **`user_code`**=\<resource-owner-user-code>

   * **`decision`**=`allow`

   * **`csrf`**=\<tokenId>

   The `scope` and the `client_id` parameters aren't required because the user code already contains that information.

   ```bash
   $ curl \
   --request POST \
   --header "Cookie: <session-cookie-name>=<tokenId>" \
   --data "user_code=VAL12e0v" \
   --data "decision=allow" \
   --data "csrf=<tokenId>" \
   "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/device/user"
   ```

   Advanced Identity Cloud returns HTML containing a JavaScript fragment named `pageData`, with details of the result. The following example shows the default HTML response:

   ```html
   <!DOCTYPE html>
   <!--
     Copyright …​
   -→
   <html lang="en">
   <head>
     <meta charset="utf-8">
     <meta http-equiv="X-UA-Compatible" content="IE=edge">
     <meta name="viewport" content="width=device-width, initial-scale=1">
     <meta name="description" content="OAuth2 Authorization">
     <title>OAuth2 Authorization Server</title>
   </head>

   <body style="display:none">
   <div id="wrapper">Loading…​</div>
   <footer id="footer" class="footer"></footer>
   <script type="text/javascript">
     pageData = {
         locale: "en_US",
         baseUrl : "https://<tenant-env-fqdn>/am",
         realm : "\/alpha",
         done: true
     };
   </script>
   <script src="https://<tenant-env-fqdn>/am/main-device.js"></script>
   </body>
   </html>
   ```

   The `done: true` line in the `pageData` fragment means the flow can continue.

   To return the output in JSON format instead of HTML, include the `Accept: application/json` header in the request. The following example returns the output in JSON:

   ```bash
   $ curl \
   --request POST \
   --header "Cookie: iPlanetDirectoryPro=ne1QUOjPzY0r…​" \
   --header "Accept: application/json" \
   --data "user_code=Gp4qkX4G" \
   --data "decision=allow" \
   --data "csrf=ne1QUOjPzY0r…​" \
   "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/device/user"
   {
     "baseUrl": "https://<tenant-env-fqdn>/am",
     "errorCode": null,
     "realm": "/alpha",
     "csrf": "1hQSplblZgaErLQ0/1rvcEvw5lj/cJQx3lrC3dV/3ac=",
     "locale": "en_US",
     "userCode": "Gp4qkX4G"
   }
   ```

   In this case, the `"errorCode": null` means the request is successful and the flow can continue.

   If the supplied user code is wrong or has been used, the output includes the following `pageData` fragment:

   ```javascript
   pageData = {
       locale: "en_US",
       errorCode: "not_found",
       realm : "/alpha",
       baseUrl : "https://<tenant-env-fqdn>/am"
       oauth2Data: {
             csrf: "ErFIk8pMraJ1rvKbloTgpp6b7GZ57kyk9HaIiKMVK3g=",
             userCode: "VAL12e0v"
       }
   }
   ```

|   |                                                                                                                                                                                                                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In accordance with [Section 4.1.1 of the OAuth 2.0 authorization framework](https://www.rfc-editor.org/rfc/rfc6749.html#section-4.1.1), the authorization server *must* obtain an authorization decision from the resource owner.Clients using the endpoints to register consent must ensure this requirement is met. Advanced Identity Cloud can't assert that consent was given in these cases. |

### Grant consent using a browser

The OAuth 2.0 device flow requires that the user grants consent to allow the client device to access the resources.

The authorization server would then provide the client with an access token.

To grant consent with a user code using a browser, perform the following steps:

1. The resource owner navigates to the verification URL acquired with the user code. For example:

   ```none
   https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/device/user
   ```

2. The resource owner logs in to the authorization server.

3. The resource owner enters their user code:

   ![Visit the verification URL to enter the user code.](_images/oauth2-device-user-code.png)Figure 2. OAuth 2.0 User Code

   |   |                                                                                                                                                                                                                        |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The `verification_uri_complete` property in the response appends the user code as a query parameter.Advanced Identity Cloud prefills the form with the user code value if provided in the `user_code` query parameter. |

4. The resource owner authorizes the device flow client by allowing the requested scopes:

   ![Advanced Identity Cloud lists the scopes requested by the client device, and their values.](_images/oauth2-authz-page-xui.png)Figure 3. OAuth 2.0 Consent Page

   |   |                                                                                                                                                                  |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | By default, client applications use [implied consent](oauth2-manage-consent.html#skip-consent). Advanced Identity Cloud does not display the screen to the user. |

5. Advanced Identity Cloud adds the OAuth 2.0 client to the user's profile page in the *Authorized Apps* section and displays that the user is done with the flow:

   ![The user code part of the device flow is done.](_images/oauth2-authz-page-done.png)Figure 4. OAuth 2.0 Done Page

   The device that polls the authorization server (Advanced Identity Cloud) can now obtain an access token.

### Poll for authorization

The client device must poll the authorization server for an access token, as it can't know whether the resource owner has given consent.

Perform the following steps to poll for an access token:

1. On the client device, create a POST request to poll the [/oauth2/access_token](oauth2-access_token-endpoint.html) endpoint to request an access token specifying, at least, the following parameters:

   * **`client_id`**=\<your-client-id>

   * **`grant_type`**=`urn:ietf:params:oauth:grant-type:device_code`

   * **`device_code`**=\<your-device-code>

   * **`code_verifier`**=\<your-code-verifier>

   The client device must wait for the number of seconds previously provided as the value of `interval` between polling Advanced Identity Cloud for an access token. For example:

   ```bash
   $ curl \
   --request POST \
   --data "client_id=myClient" \
   --data "grant_type=urn:ietf:params:oauth:grant-type:device_code" \
   --data "device_code=<your-device-code>" \
   --data "code_verifier=<your-code-verifier>" \
   "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/access_token"
   ```

   If the user has authorized the client device, Advanced Identity Cloud returns an HTTP 200 status code with an access token that can be used to request resources:

   ```json
   {
       "access_token": "<access-token>",
       "refresh_token": "<refresh-token>",
       "scope": "write",
       "token_type": "Bearer",
       "expires_in": 3599
   }
   ```

   If the user hasn't authorized the client device, Advanced Identity Cloud returns an HTTP 403 status code with the following error message:

   ```json
   {
       "error": "authorization_pending",
       "error_description": "The user has not yet completed authorization"
   }
   ```

   If the client device is polling faster than the specified interval, Advanced Identity Cloud returns an HTTP 400 status code with the following error message:

   ```json
   {
       "error": "slow_down",
       "error_description": "The polling interval has not elapsed since the last request"
   }
   ```

---

---
title: Form parameters (HTTP POST)
description: Authenticate OAuth 2.0 clients by sending credentials as HTTP POST form parameters
component: pingoneaic
page_id: pingoneaic:am-oauth2:client-auth-form
canonical_url: https://docs.pingidentity.com/pingoneaic/am-oauth2/client-auth-form.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "OAuth 2.0", "Federation", "HTTP", "Clients"]
page_aliases: ["oauth2-guide:client-auth-form.adoc"]
---

# Form parameters (HTTP POST)

The OAuth 2.0 client authenticates by sending `client_id` and `client_secret` form parameters in an HTTP POST request:

```bash
$ curl \
--request POST \
--data "client_id=myClient" \
--data "client_secret=mySecret" \
...
```

To use this authentication method for a confidential OAuth 2.0 client, edit the client profile in the Advanced Identity Cloud admin console:

1. Go to Applications > Applications > *Name* > Sign On > General Settings > Advanced > Authentication.

2. Set the Token Endpoint Authentication Method to `client_secret_post` and save your work.

Make sure all connections to Advanced Identity Cloud use HTTPS to protect the secret.

---

---
title: Implicit grant
description: Issue tokens directly to browser-based clients in authorization endpoint redirection URI
component: pingoneaic
page_id: pingoneaic:am-oauth2:oauth2-implicit-grant
canonical_url: https://docs.pingidentity.com/pingoneaic/am-oauth2/oauth2-implicit-grant.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "OpenID Connect (OIDC)", "Endpoints", "Authorization", "Grant Flow", "REST API"]
page_aliases: ["oidc1-guide:openid-connect-implicit-flow.adoc", "oauth2-guide:oauth2-implicit-grant.adoc"]
section_ids:
  oauth2-implicit-flow: The implicit grant flow
  oauth_2_0: OAuth 2.0
  oidc: OIDC
  oauth2-implicit-demo: Demonstrate the implicit grant flow
  prepare-demo-implicit: Prepare the demonstration
  proc-access-token-implicit-browser: Get an access token using a browser
  proc-access-token-implicit-rest: Get an access token using REST
  additional_oidc_claims: Additional OIDC claims
---

# Implicit grant

* Endpoints

  * [/oauth2/authorize](oauth2-authorize-endpoint.html)

  * [/oauth2/userinfo](../am-oidc1/rest-api-oidc-userinfo-endpoint.html) (OpenID Connect \[OIDC])

The implicit grant is designed for public clients that run inside the resource owner's user-agent, for example, JavaScript applications. For OIDC, this flow lets the relying party (RP) interact directly with the OpenID provider (OP), and receive tokens directly from the authorization endpoint.

Because applications running in the user-agent are considered less trusted than applications running in servers, the authorization server or OP never issues refresh tokens in this flow. Also, you must consider the security impact of cross-site scripting (XSS) attacks that could leak the access token to other systems, and implement cross-origin resource sharing (CORS) to make OAuth 2.0 requests to different domains.

Due to the security implications of this flow, ForgeRock recommends that you use the [Authorization code grant with PKCE](oauth2-authz-grant-pkce.html) flow whenever possible.

## The implicit grant flow

### OAuth 2.0

![Advanced Identity Cloud supports the implicit grant.](_images/oauth2-implicit.svg)

1. The client, usually a single-page application (SPA), receives a request to access a protected resource. To access the resource, the client requires authorization from the resource owner.

2. The client redirects the resource owner's user-agent or opens a new frame to the Advanced Identity Cloud authorization service.

3. The authorization server authenticates the resource owner, confirms resource access, and gathers consent if not previously saved.

4. If the resource owner's credentials are valid, the authorization server returns the access token to the user-agent as part of the redirection URI.

5. Now, the client must extract the access token from the URI. In this example, the user-agent follows the redirection to the web-hosted server that contains the protected resource without the access token.

6. The web-hosted server returns a web page with an embedded script to extract the access token from the URI.

   In another possible scenario, the redirection URI is a dummy URI in the client, and the client already has the logic in itself to extract the access token.

7. The user-agent executes the script and retrieves the access token.

8. The user-agent returns the access token to the client.

9. The client requests access to the protected resources presenting the access token to the resource server.

10. The resource server contacts the authorization server to validate the access token.

11. The authorization server validates the token and responds to the resource server.

12. If the token is valid, the resource server allows the client to access the protected resource.

### OIDC

![Advanced Identity Cloud supports the OIDC Implicit Flow.](_images/oidc-implicit.svg)

1. The RP, usually an SPA, receives a request to access user information at the OP. To access this information, the RP requires authorization from the end user.

2. The RP redirects the end user's user-agent or opens a new frame to the OP.

   As part of the implicit flow, the request includes the `openid` scope and the `nonce` parameter.

3. The OP authenticates the end user, confirms resource access, and gathers consent if necessary.

4. On success, the OP returns access and ID tokens to the user-agent in the redirection URI.

5. The user-agent extracts the tokens from the URI.

   In this example, the user-agent follows the redirection to the RP without the tokens.

6. The RP returns a web page with an embedded script to extract the tokens from the URI.

   In another possible scenario, the redirection URI is a dummy URI in the RP application and the RP application already has the logic to extract the tokens.

7. The user-agent executes the script and retrieves the tokens.

8. The user-agent returns the tokens to the RP.

9. The RP validates the ID token and its claims.

   The RP can use the ID token subject ID claim as the end user's identity.

10. If the RP requires additional claims, it sends a request to the [/oauth2/userinfo](../am-oidc1/rest-api-oidc-userinfo-endpoint.html) endpoint with the access token for authorization.

11. If the access token is valid, the `/oauth2/userinfo` endpoint returns any additional claims.

    The RP can use the subject ID and the additional claims to identify the end user.

## Demonstrate the implicit grant flow

Perform these steps to get an access token:

1. [Prepare the demonstration](#prepare-demo-implicit)

2. [Get an access token using a browser](#proc-access-token-implicit-browser) or [Get an access token using REST](#proc-access-token-implicit-rest)

### Prepare the demonstration

Complete these steps to prepare the implicit grant demonstration:

1. [Create an application owner profile](../identities/manage-identities.html#create-a-user-profile) and record the username and password.

2. [Register a client application](../app-management/register-a-custom-application.html).

   1. In the Advanced Identity Cloud admin console, go to Applications > Applications and select + Custom Application.

   2. Select the sign-in method as OIDC - OpenId Connect and application type as Native / SPA.

   3. Create the application, providing the following details:

      * Name

        `myClient`

      * Owners

        `<application-owner>`

      * Client ID

        `myClient`

   4. Switch to the Sign On tab and under General Settings, set these fields to have the following values:

      * Sign-in URLs

        `https://www.example.com:443/callback`

      * Scopes

        `write` (for OAuth 2.0)\
        `openid` and `profile` (for OIDC)

      * Grant Types

        `Implicit`

   5. Save your changes.

3. [Create a resource owner profile](../identities/manage-identities.html#create-a-user-profile) and record the username and password.

### Get an access token using a browser

1. The client redirects the resource owner's user-agent to the authorization server's [/oauth2/authorize](oauth2-authorize-endpoint.html) endpoint, including the following query parameters:

   * **`client_id`**: `myClient`

   * **response_type**: `token` (OAuth 2.0) or `token id_token` (OIDC)

   * **scope**: `write` (OAuth 2.0) or `openid` and `profile` (OIDC)

   * **`redirect_uri`**: `https://www.example.com:443/callback`

   * **nonce**: `<nonce-value>`(OIDC)

   Example OAuth 2.0 call:

   ```none
   https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/authorize \
   ?client_id=myClient \
   &response_type=token \
   &scope=write \
   &redirect_uri=https://www.example.com:443/callback \
   &state=abc123
   ```

   For OIDC, use `scope=openid profile`, `response_type=token id_token`, and include the `nonce` parameter.

   Example OIDC call:

   ```none
   https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/authorize \
   ?client_id=myClient \
   &response_type=token id_token \
   &scope=openid profile \
   &redirect_uri=https://www.example.com:443/callback \
   &state=abc123
   &nonce=123abc
   ```

   |   |                                                                                                                                                                                                                                                                 |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The URL is split and spaces added for readability purposes.The `scope` parameter is optional if default values are configured in the authorization server or the client.The `state` parameter is included to protect against CSRF attacks but is also optional. |

2. The resource owner authenticates to the authorization server. In this demonstration, they sign in using the default journey configured for the realm.

   |   |                                                                                                                                                                                                                                                                                                                                                             |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | By default, client applications in Advanced Identity Cloud use [implied consent](oauth2-manage-consent.html#skip-consent). If Advanced Identity Cloud is configured to require explicit consent, the authorization server presents the resource owner with a consent screen. To continue the flow, the resource owner must select `Allow` to grant consent. |

   The authorization server redirects the resource owner to the URL specified in the `redirect_uri` parameter.

3. Inspect the URL in the browser.

   For OAuth 2.0, it contains the access token the authorization server has issued. For example:

   `https://www.example.com/callback#access_token=<access_token>&iss...`

   For OIDC, it contains the access and ID tokens. For example:

   `https://www.example.com/callback#access_token=<access_token>&id_token=<id_token>...`

### Get an access token using REST

1. [Authenticate](../am-authentication/authn-rest.html) as the resource owner.

   For example:

   ```bash
   $ curl \
   --request POST \
   --header "Content-Type: application/json" \
   --header 'X-OpenAM-Username: <resource-owner-username>' \
   --header 'X-OpenAM-Password: <resource-owner-password>' \
   --header "Accept-API-Version: resource=2.0, protocol=1.0" \
   'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate'
   {
     "tokenId": "<tokenId>",
     "successUrl": "/enduser/?realm=/alpha",
     "realm": "/alpha"
   }
   ```

2. As the client, call the [/oauth2/authorize](oauth2-authorize-endpoint.html) endpoint to request the authorization code. Provide the resource owner's SSO token in a cookie and the following parameters:

   * **`client_id`**: `myClient`

   * **`response_type`**: `token` (OAuth 2.0) or `token id_token` (OIDC)

   * **`scope`**: `write` (OAuth 2.0) or `openid` and `profile` (OIDC)

   * **`nonce`**: `<nonce-value>` (OIDC)

   * **`csrf`**: `<tokenId>`

   * **`redirect_uri`**: `https://www.example.com:443/callback`

   * **`decision`**: `allow`

   Example OAuth 2.0 call:

   ```bash
   $ curl \
   --cookie "<session-cookie-name>=<tokenId>" \
   --request POST \
   --data "client_id=myClient" \
   --data "response_type=token" \
   --data "scope=write" \
   --data "state=abc123" \
   --data "decision=allow" \
   --data "csrf=<tokenId>" \
   --data "redirect_uri=https://www.example.com:443/callback" \
   "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/authorize"
   ```

   For OIDC, use `scope=openid profile`, `response_type=token id_token`, and include the `nonce` parameter.

   Example OIDC call:

   ```bash
   $ curl \
   --cookie "<session-cookie-name>=<tokenId>" \
   --request POST \
   --data "client_id=myClient" \
   --data "response_type=token id_token" \
   --data "scope=openid profile" \
   --data "state=abc123" \
   --data "nonce=123abc" \
   --data "decision=allow" \
   --data "csrf=<tokenId>" \
   --data "redirect_uri=https://www.example.com:443/callback" \
   "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/authorize"
   ```

   |   |                                                                                                                                                                                                      |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The `scope` parameter is optional if default values are configured in the authorization server or the client.The `state` parameter is included to protect against CSRF attacks but is also optional. |

   For OAuth 2.0, if the authorization server is able to authenticate the user, it returns an HTTP 302 response with the access token appended to the redirection URI:

   ```none
   HTTP/2 302
   ...
   location: https://www.example.com:443/callback#access_token=<access-token>&iss...
   ...
   ```

   For OIDC, it returns the access and ID tokens in the redirection URI:

   ```none
   HTTP/2 302
   ...
   location: https://www.example.com:443/callback#access_token=<access-token>&&id_token=<id_token>...
   ...
   ```

## Additional OIDC claims

An RP can request additional claims about the end user with the access token at the [/oauth2/userinfo](../am-oidc1/rest-api-oidc-userinfo-endpoint.html) endpoint:

```bash
$ curl \
--request GET \
--header "Authorization Bearer <access-token>" \
"https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/userinfo"
{
  "name": "<resource-owner-display-name>",
  "family_name": "<resource-owner-family-name>",
  "given_name": "<resource-owner-given-name>",
  "sub": "<resource-owner-id>",
  "subname": "<resource-owner-id>"
}
```