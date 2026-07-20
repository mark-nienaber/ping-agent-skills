---
title: /json/token/macaroon
description: The /json/token/macaroon endpoint lets you inspect and manipulate macaroon tokens.
component: pingoneaic-api
page_id: pingoneaic-api:am-oauth2:oauth2-introspect-macaroon-endpoint
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-oauth2/oauth2-introspect-macaroon-endpoint.html
keywords: ["OAuth 2.0", "OpenID Connect (OIDC)", "Endpoints", "Macaroons", "Scope"]
---

# /json/token/macaroon

The `/json/token/macaroon` endpoint lets you inspect and manipulate [macaroon tokens](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-macaroons.html).

Specify the realm in the request URL; for example:

```none
https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/token/macaroon
```

This endpoint supports these parameters:

| Field             | Description                                             |
| ----------------- | ------------------------------------------------------- |
| `action=inspect`  | Return details about the macaroon.                      |
| `action=restrict` | Add a caveat to the macaroon, returning a new macaroon. |

You can manipulate macaroons locally using a macaroon library. Anyone in possession of a macaroon token can inspect and restrict the macaroon securely.

The following example restricts the scope of a macaroon token and inspects the result. The original scope of the unrestricted token is `openid profile`:

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "cache-control: no-cache" \
--data '{
  "macaroon": "<macaroon-token>",
  "caveat": {"type": "first-party", "identifier": {"scope": "profile"}}
}' \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/token/macaroon?_action=restrict'
{
  "macaroon": "<restricted-macaroon-token>"
}

$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "cache-control: no-cache" \
--data '{"macaroon": "<restricted-macaroon-token>"}' \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/token/macaroon?_action=inspect'
{
  "identifier": "<identifier>",
  "location": "",
  "caveats": [{
    "type": "first-party",
    "identifier": {
      "scope": "profile"
    }
  }],
  "signature": "<signature>"
}
```

|   |                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | OpenID Connect clients must ensure the following information is present in the JSON:- The `openid` scope; for example, `"scopes": ["profile", "openid"]`.

- The `id_token` response type; for example, `"response_types": ["code", "id_token code"]`. |

---

---
title: /oauth2/access_token
description: The /oauth2/access_token endpoint is the OAuth 2.0 token endpoint (RFC 6749).
component: pingoneaic-api
page_id: pingoneaic-api:am-oauth2:oauth2-access_token-endpoint
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-oauth2/oauth2-access_token-endpoint.html
keywords: ["OAuth 2.0", "Endpoints", "Authorization", "REST API"]
---

# /oauth2/access\_token

The `/oauth2/access_token` endpoint is the OAuth 2.0 [token endpoint](https://www.rfc-editor.org/rfc/rfc6749.html#section-3.2) (RFC 6749).

Use this endpoint to acquire an access or refresh token with the following flows:

* Authorization code grant ([OAuth 2.0 and OIDC](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-authz-grant.html))

* Authorization code grant with PKCE ([OAuth 2.0 and OIDC](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-authz-grant-pkce.html))

* Authorization code grant with PAR ([OAuth 2.0](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-authz-grant-par.html))

* Client credentials grant ([OAuth 2.0](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-client-cred-grant.html))

* Resource owner password credentials grant ([OAuth 2.0](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-ropc-grant.html))

* Device flow ([OAuth 2.0](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-device-flow.html))

* SAML 2.0 profile for authorization grant ([OAuth 2.0](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-saml2-bearer-grant.html))

* Token exchange ([OAuth 2.0 | OpenID Connect](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/token-exchange.html))

Specify the realm in the request URL; for example:

```none
https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/access_token
```

The `access_token` endpoint supports the following parameters:

| Parameter               | Description                                                                                                                                                                         | Required                                                                                                                                     |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `actor_token`           | The token representing a delegate acting on behalf of another identity.                                                                                                             | Yes, for [Token exchange](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/token-exchange.html)                                     |
| `actor_token_type`      | The type of actor token.                                                                                                                                                            | Yes, for [Token exchange](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/token-exchange.html)                                     |
| `auth_chain`            | A string naming the journey to authenticate the resource owner.                                                                                                                     | No, only for [Resource owner password credentials grant](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-ropc-grant.html)   |
| `assertion`             | A string holding a base64-encoded then URL-encoded SAML 2.0 assertion                                                                                                               | Yes, when `grant_type=urn:ietf:params:oauth:grant-type:saml2-bearer`                                                                         |
| `client_assertion`      | A signed JSON Web Token (JWT) to use as client credentials.                                                                                                                         | Yes, for [JWT profile](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/client-auth-jwt.html) authentication                        |
| `client_assertion_type` | The type of assertion, `client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer`.                                                                    | Yes, for [JWT profile](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/client-auth-jwt.html) authentication                        |
| `client_id`             | Uniquely identifies the application making the request.                                                                                                                             | Yes                                                                                                                                          |
| `client_secret`         | The password for a confidential client; do not use with `cnf_key`.                                                                                                                  | Yes, when authenticating with [Form parameters (HTTP POST)](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/client-auth-form.html) |
| `cnf_key`               | A base64-encoded JSON Web Key (JWK); do not use with `client_secret`.                                                                                                               | Yes, for [JWK-based proof-of-possession](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-PoP-JWK.html)                      |
| `code`                  | A string holding the authorization code for an authorization code grant.                                                                                                            | Yes, when `grant_type=authorization_code`                                                                                                    |
| `code_verifier`         | A random string correlating a PKCE authorization request with the token request.                                                                                                    | Yes, for flows with PKCE                                                                                                                     |
| `device_code`           | A string holding the device code requested from the user for a device flow.                                                                                                         | Yes, when `grant_type=urn:ietf:params:oauth:grant-type:device_code`                                                                          |
| `grant_type`            | A string specifying the type of grant to acquire an access token.                                                                                                                   | Yes                                                                                                                                          |
| `password`              | A string holding the resource owner password for the [Resource owner password credentials grant](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-ropc-grant.html). | Yes, when `grant_type=password`                                                                                                              |
| `redirect_uri`          | The URI to return the resource owner to after authorization is complete.                                                                                                            | Yes, when `grant_type=authorization_code` and it was included earlier in the flow                                                            |
| `refresh_token`         | The refresh to get a new access token.                                                                                                                                              | Yes, for [Refresh tokens](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-refresh-tokens.html)                              |
| `requested_token_type`  | The type of token requested in exchange.                                                                                                                                            | No, but recommended for [Token exchange](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/token-exchange.html)                      |
| `scope`                 | The scopes linked to the permissions requested by the client from the resource owner.                                                                                               | No                                                                                                                                           |
| `subject_token`         | The original token to exchange.                                                                                                                                                     | Yes, for [Token exchange](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/token-exchange.html)                                     |
| `subject_token_type`    | The type of subject token.                                                                                                                                                          | Yes, for [Token exchange](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/token-exchange.html)                                     |
| `username`              | A string holding the resource owner username for the [Resource owner password credentials grant](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-ropc-grant.html). | Yes, when `grant_type=password`                                                                                                              |

---

---
title: /oauth2/authorize
description: The /oauth2/authorize endpoint is the OAuth 2.0 authorization endpoint defined in RFC 6749.
component: pingoneaic-api
page_id: pingoneaic-api:am-oauth2:oauth2-authorize-endpoint
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-oauth2/oauth2-authorize-endpoint.html
keywords: ["OAuth 2.0", "Endpoints", "Authorization", "REST API"]
---

# /oauth2/authorize

The `/oauth2/authorize` endpoint is the OAuth 2.0 authorization endpoint defined in [RFC 6749](https://www.rfc-editor.org/info/rfc6749).

Use this endpoint to gather consent and authorization from the resource owner for the following flows:

* Authorization code grant ([OAuth 2.0 and OIDC](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-authz-grant.html))

* Authorization code grant with PKCE ([OAuth 2.0 and OIDC](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-authz-grant-pkce.html))

* Authorization code grant with PAR ([OAuth 2.0](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-authz-grant-par.html))

* Implicit grant ([OAuth 2.0 and OIDC](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-implicit-grant.html))

Specify the realm in the request URL; for example:

```none
https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/authorize
```

The authorization endpoint supports the following parameters:

| Parameter               | Description                                                                                                         | Required                                                                                                                                          |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `acr_values`            | The OpenID Connect authentication context class reference values.                                                   | Yes, if [required by the OpenID Connect provider](https://docs.pingidentity.com/pingoneaic/latest/am-oidc1/oidc-authentication-requirements.html) |
| `claims`                | The user attributes to be returned in the ID token.                                                                 | No                                                                                                                                                |
| `client_id`             | Uniquely identifies the application making the request.                                                             | Yes                                                                                                                                               |
| `code_challenge`        | The code verifier generated for the PKCE flow.                                                                      | Yes, for the [Authorization code grant with PKCE](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-authz-grant-pkce.html) flow    |
| `code_challenge_method` | The method to derive the code challenge.                                                                            | Yes, when the `code_challenge` is hashed (recommended)                                                                                            |
| `csrf`                  | The SSO token string linking the request to the user session to protect against Cross-Site Request Forgery attacks. | Yes, when gathering consent without a remote consent service                                                                                      |
| `decision`              | Specifies whether the resource owner consents to the requested access.                                              | Yes, when gathering consent unless consent is already saved for the scope                                                                         |
| `id_token_hint`         | Previously issued ID token passed as a hint about the end user's session with the client.                           | No                                                                                                                                                |
| `login_hint`            | String value that can be set to the ID the user uses to log in.                                                     | No                                                                                                                                                |
| `nonce`                 | String value that associates the client session with the ID token.                                                  | Yes, for the [Implicit Grant](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-implicit-grant.html) flow for OIDC                 |
| `prompt`                | Specifies whether to prompt the end user for authentication and consent.                                            | No                                                                                                                                                |
| `redirect_uri`          | The URI to return the resource owner to after authorization is complete.                                            | No                                                                                                                                                |
| `response_mode`         | Specifies the mechanism for returning response parameters.                                                          | No                                                                                                                                                |
| `response_type`         | The type of response expected from the authorization server.                                                        | Yes                                                                                                                                               |
| `request`               | The JWT request object.                                                                                             | Yes, for JAR request and OIDC flows requiring a request object and providing no `request_uri`                                                     |
| `request_uri`           | For PAR or OIDC flows, a reference to JWT request object(s).                                                        | Yes, for JAR request and OIDC flows requiring a request object and providing no `request`                                                         |
| `save_consent`          | Specifies whether to store a resource owner's consented scopes.                                                     | No                                                                                                                                                |
| `scope`                 | The scopes linked to the permissions requested by the client from the resource owner.                               | No                                                                                                                                                |
| `service`               | The authentication journey to use when authenticating the resource owner.                                           | No                                                                                                                                                |
| `state`                 | The value to maintain state between the request and the callback.                                                   | No, but strongly recommended                                                                                                                      |
| `ui_locales`            | The end user's preferred languages for the user interface.                                                          | No                                                                                                                                                |

---

---
title: /oauth2/bc-authorize
description: The /oauth2/bc-authorize endpoint is the backchannel authorization endpoint for OpenID Connect Client-Initiated Backchannel Authentication Flow - Core 1.0.
component: pingoneaic-api
page_id: pingoneaic-api:am-oauth2:oauth2-bc-authorize-endpoint
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-oauth2/oauth2-bc-authorize-endpoint.html
keywords: ["OAuth 2.0", "Endpoints", "Authorization", "REST API"]
---

# /oauth2/bc-authorize

The `/oauth2/bc-authorize` endpoint is the backchannel authorization endpoint for [OpenID Connect Client-Initiated Backchannel Authentication Flow - Core 1.0](https://openid.net/specs/openid-client-initiated-backchannel-authentication-core-1_0.html).

Use this endpoint to initiate backchannel authorization with the resource owner with the following flow:

* Backchannel request grant ([OpenID Connect](https://docs.pingidentity.com/pingoneaic/latest/am-oidc1/openid-connect-backchannel-request-flow.html))

Specify the realm in the request URL; for example:

```none
https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/bc-authorize
```

The endpoint supports the following parameters:

| Parameter               | Description                                                                                                      | Required                                                                                                                                     |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `client_assertion`(1)   | A signed JSON Web Token (JWT) to use as client credentials.                                                      | Yes, for [JWT profile](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/client-auth-jwt.html) authentication                        |
| `client_assertion_type` | The type of assertion, `client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer`. | Yes, for [JWT profile](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/client-auth-jwt.html) authentication                        |
| `client_id`             | Uniquely identifies the application making the request.                                                          | Yes                                                                                                                                          |
| `client_secret`         | The password for a confidential client.                                                                          | Yes, when authenticating with [Form parameters (HTTP POST)](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/client-auth-form.html) |

(1) The endpoint requires a signed JWT with these claims:

| Claim             | Description                                                                                                                                                                                                                                    | Example                                                                                                                                                                              |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `acr_values`      | A string identifying the mechanism for the end user to provide authorization.                                                                                                                                                                  | `"acr_values": "push"`                                                                                                                                                               |
| `aud`             | A string or array of strings indicating the intended audience of the JWT. Must include the authorization server OAuth 2.0 endpoint including port number 443.                                                                                  | `"aud": "https://<tenant-env-fqdn>:443/am/oauth2/realms/root/realms/alpha"`                                                                                                          |
| `binding_message` | A short (100 character max.) string message to display to the user when obtaining authorization.For push notification, messages must:- Begin with a letter, number, or punctuation mark.

- **Not** include line breaks or control characters. | `"binding_message": "Allow ExampleBank to transfer £50 from 'Main' to 'Savings'? (EB-0246326)"`                                                                                      |
| `exp`             | The expiration time in seconds since January 1, 1970 UTC. An expiration time more than 30 minutes in the future causes a `JWT expiration time is unreasonable` error message.                                                                  | `"exp": 1761066489`&#xA;&#xA;To generate a value just under 30 minutes in the future, run the following command in a Unix or Linux shell:&#xA;&#xA;$ echo $(($(date -u +%s) + 1799)) |
| `iss`             | The unique identifier of the JWT issuer; must match the client ID in the application profile.                                                                                                                                                  | `"iss": "myCIBAClient"`                                                                                                                                                              |
| `login_hint`      | A string identifying the principal and subject of the JWT (the end user).                                                                                                                                                                      | `"login_hint": "a0325ea4-9d9b-4056-931b-ab64704cc3da"`                                                                                                                               |
| `scope`           | A string holding a space-separated list of the requested scopes; must include `openid`.                                                                                                                                                        | `"scope": "openid profile"`                                                                                                                                                          |

---

---
title: /oauth2/device/code
description: The Device authorization grant endpoint defined in RFC 8628 OAuth 2.0 Device Authorization Grant.
component: pingoneaic-api
page_id: pingoneaic-api:am-oauth2:rest-api-oauth2-device-code
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-oauth2/rest-api-oauth2-device-code.html
keywords: ["OAuth 2.0", "API Explorer", "Endpoints"]
page_aliases: ["oauth2-guide:rest-api-oauth2-device-code.adoc"]
---

# /oauth2/device/code

The [Device authorization grant](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-device-flow.html) endpoint defined in RFC 8628 [OAuth 2.0 Device Authorization Grant](https://www.rfc-editor.org/info/rfc8628).

Client devices use this endpoint in the following flows to get the codes and information required to obtain the resource owner's consent for device access:

* Device flow ([OAuth 2.0](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-device-flow.html))

* Device flow with PKCE ([OAuth 2.0](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-device-flow-pkce.html))

Specify the realm in the request URL; for example:

```none
https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/device/code
```

The device code endpoint supports the following parameters:

| Parameter               | Description                                                                           | Required                                                                                                                                          |
| ----------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `acr_values`            | The OpenID Connect authentication context class reference values.                     | Yes, if [required by the OpenID Connect provider](https://docs.pingidentity.com/pingoneaic/latest/am-oidc1/oidc-authentication-requirements.html) |
| `claims`                | The user attributes to be returned in the ID token.                                   | No                                                                                                                                                |
| `client_id`             | Uniquely identifies the application making the request.                               | Yes                                                                                                                                               |
| `code_challenge`        | The code verifier generated for the PKCE flow.                                        | Yes, for the [Authorization code grant with PKCE](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-authz-grant-pkce.html) flow    |
| `code_challenge_method` | The method to derive the code challenge.                                              | Yes, when the `code_challenge` is hashed (recommended)                                                                                            |
| `login_hint`            | String value that can be set to the ID the user uses to log in.                       | No                                                                                                                                                |
| `nonce`                 | String value that associates the client session with the ID token.                    | No                                                                                                                                                |
| `prompt`                | Specifies whether to prompt the end user for authentication and consent.              | No                                                                                                                                                |
| `scope`                 | The scopes linked to the permissions requested by the client from the resource owner. | No                                                                                                                                                |
| `state`                 | The value to maintain state between the request and the callback.                     | No, but strongly recommended                                                                                                                      |
| `ui_locales`            | The end user's preferred languages for the user interface.                            | No                                                                                                                                                |

---

---
title: /oauth2/device/user
description: This is the Device authorization grant endpoint for user interaction.
component: pingoneaic-api
page_id: pingoneaic-api:am-oauth2:rest-api-oauth2-device-user
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-oauth2/rest-api-oauth2-device-user.html
keywords: ["OAuth 2.0", "API Explorer", "Endpoints", "PKCE"]
page_aliases: ["oauth2-guide:rest-api-oauth2-device-user.adoc"]
---

# /oauth2/device/user

This is the [Device authorization grant](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-device-flow.html) endpoint for user interaction.

Client devices use this endpoint to confirm the resource owner's consent in the following flows:

* Device flow ([OAuth 2.0](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-device-flow.html))

* Device flow with PKCE ([OAuth 2.0](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-device-flow-pkce.html))

Specify the realm in the request URL; for example:

```none
https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/device/user
```

The device user endpoint supports the following parameters:

| Parameter      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Required                                                                  |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `csrf`         | The SSO token string linking the request to the user session to protect against Cross-Site Request Forgery attacks.                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Yes, when gathering consent without a remote consent service              |
| `decision`     | Whether the resource owner consents to the requested access.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Yes, when gathering consent unless consent is already saved for the scope |
| `save_consent` | Whether to store a resource owner's consented scopes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | No                                                                        |
| `scope`        | The scopes linked to the permissions requested by the client from the resource owner.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | No                                                                        |
| `user_code`    | The user code confirmed by the resource owner.The endpoint checks for the `user_code` on the initial request and uses it to retrieve the associated device code to determine if any ACRs were requested. If ACRs were requested, the user authenticates through the specified authentication journey.If a user accesses the endpoint without supplying a `user_code`, the user authenticates through the default authentication journey. If that journey doesn't match the ACRs required by the device request, the user is prompted to reauthenticate after entering the code. | Yes                                                                       |

---

---
title: /oauth2/introspect
description: The /oauth2/introspect endpoint is defined in RFC 7662 OAuth 2.0 Token Introspection.
component: pingoneaic-api
page_id: pingoneaic-api:am-oauth2:oauth2-introspect-endpoint
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-oauth2/oauth2-introspect-endpoint.html
keywords: ["OAuth 2.0", "Endpoints", "Scope", "JWT", "Grant Flow", "REST API"]
section_ids:
  example: Example
  response-signing-and-encryption: Response signing and encryption
  response-content: Response content
---

# /oauth2/introspect

The `/oauth2/introspect` endpoint is defined in RFC 7662 [OAuth 2.0 Token Introspection](https://www.rfc-editor.org/info/rfc7662).

A resource server uses this endpoint to retrieve details about a token, such as:

* The approved scopes

* The user who authorized the client to obtain the token

* The expiry time

* The proof-of-possession JSON Web Key (JWK)

The resource server must authenticate to access this endpoint.

To introspect macaroon access tokens containing third-party caveats, use the `X-Discharge-Macaroon` header to pass the discharge macaroon.

Specify the realm in the request URL; for example:

```none
https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/introspect
```

The token introspection endpoint supports the following parameters:

| Parameter               | Description                                                                                                      | Required                                                                                                                                     |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `client_assertion`      | A signed JSON Web Token (JWT) to use as client credentials.                                                      | Yes, for [JWT profile](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/client-auth-jwt.html) authentication                        |
| `client_assertion_type` | The type of assertion, `client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer`. | Yes, for [JWT profile](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/client-auth-jwt.html) authentication                        |
| `client_id`             | Uniquely identifies the application making the request.                                                          | Yes                                                                                                                                          |
| `client_secret`         | The password for a confidential client.                                                                          | Yes, when authenticating with [Form parameters (HTTP POST)](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/client-auth-form.html) |
| `token`                 | The token to introspect.                                                                                         | Yes                                                                                                                                          |

## Example

The following example demonstrates token introspection:

```bash
$ curl \
--request POST \
--user "myClient:mySecret" \
--data "token=<access-token>" \
"https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/introspect"
{
  "active": true,
  "scope": "profile",
  "realm": "/alpha",
  "client_id": "myClient",
  "user_id": "a0325ea4-9d9b-4056-931b-ab64704cc3da",
  "username": "a0325ea4-9d9b-4056-931b-ab64704cc3da",
  "token_type": "Bearer",
  "exp": 1675703376,
  "sub": "a0325ea4-9d9b-4056-931b-ab64704cc3da",
  "subname": "a0325ea4-9d9b-4056-931b-ab64704cc3da",
  "iss": "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha",
  "auth_level": 0,
  "authGrantId": "sReMmkL05mN4xtDMQdVrpjXB_go",
  "auditTrackingId": "1d7a3317-03a9-4461-9d12-745f886019c2-5860187",
  "expires_in": 3575
}
```

## Response signing and encryption

The default introspection response is a plain JSON object.

Advanced Identity Cloud also supports the [JWT Response for OAuth Token Introspection](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-jwt-introspection-response-03) Internet-Draft, which adds signed JWT or signed and encrypted JWT responses.

A client application can request a signed JWT by adding an `Accept: application/jwt` header to the request.

To enable signing and encryption for all requests, follow these steps:

1. In the Advanced Identity Cloud admin console, go to Applications > *Client ID* > Sign On > General Settings > Show advanced settings > Endpoint Response Formats and select the response type in the Token Inspection Response Format drop-down list.

2. Save your work.

3. If you need to configure signing and encryption, go to Native Consoles > Access Management > Realms > *Realm Name* > Applications > OAuth 2.0 > Clients > *Client ID* > Signing and Encryption and configure the following properties:

   * Token introspection response signing algorithm

     Default: `RS256`

   * Token introspection response encryption algorithm

     Default: `RSA-OAEP-256`

   * Token introspection encrypted response encryption algorithm

     Default: `A128CBC-HS256`

4. Save your work.

Requests for plain JSON now return errors.

## Response content

The following table describes fields you may find in the introspection response:

| Field        | Description                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `active`     | Whether the token is active (`true`) or not (`false`).                                                                                                                                                                                                                                                                                                                                                                           |
| `auth_level` | The authentication level for the resource owner who granted access to the token.                                                                                                                                                                                                                                                                                                                                                 |
| `client_id`  | The client the token was issued to.                                                                                                                                                                                                                                                                                                                                                                                              |
| `cnf`        | The confirmation key claim.The `jwk` type contains the decoded JWK for the access token in the [JWK-based proof-of-possession](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-PoP-JWK.html) flow.                                                                                                                                                                                                              |
| `exp`        | Expiration time in seconds since January 1, 1970 UTC.                                                                                                                                                                                                                                                                                                                                                                            |
| `expires_in` | Expiration time in seconds from now; the value decreases with every request to Advanced Identity Cloud.Unlike the calculated value, the expiration time stored in the token does not change.For client-side tokens, Advanced Identity Cloud only returns this to a client in the same realm as the resource owner.                                                                                                               |
| `iss`        | The token issuer.                                                                                                                                                                                                                                                                                                                                                                                                                |
| `macaroon`   | The macaroon the token validates, including any caveats.                                                                                                                                                                                                                                                                                                                                                                         |
| `scope`      | The space-separated list of the scopes associated with the token.                                                                                                                                                                                                                                                                                                                                                                |
| `sub`        | The subject of the access token.This can use the format `(type!subject)`, where:- `subject` is the principal's ID.

- `type` can be one of the following:

  * `age`

    The *subject* is an OAuth 2.0 or OpenID Connect client, a Remote Consent Service agent, or a Web or Java Agent internal client.

  * `usr`

    The *subject* is a user, device, or similar identity.Examples: `(usr!bjensen)`, `(age!myOAuth2Client)` |
| `token_type` | The type of token.                                                                                                                                                                                                                                                                                                                                                                                                               |
| `user_id`    | Deprecated form of `username`.                                                                                                                                                                                                                                                                                                                                                                                                   |
| `username`   | The user who authorized the client to obtain the token.                                                                                                                                                                                                                                                                                                                                                                          |

---

---
title: /oauth2/par
description: The /oauth2/par endpoint is the OAuth 2.0 pushed authorization request (PAR) endpoint defined in RFC 9126.
component: pingoneaic-api
page_id: pingoneaic-api:am-oauth2:oauth2-par-endpoint
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-oauth2/oauth2-par-endpoint.html
keywords: ["OAuth 2.0", "OpenID Connect (OIDC)", "PAR", "Authorization", "Endpoints"]
page_aliases: ["oauth2-guide:oauth2-par-endpoint.adoc"]
---

# /oauth2/par

The `/oauth2/par` endpoint is the OAuth 2.0 pushed authorization request (PAR) endpoint defined in [RFC 9126](https://www.rfc-editor.org/info/rfc9126).

Use this endpoint to push an authorization request payload directly to the authorization server for the following flows:

* Authorization code grant ([OAuth 2.0 and OIDC](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-authz-grant.html))

* Authorization code grant with PKCE ([OAuth 2.0 and OIDC](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-authz-grant-pkce.html))

* Implicit grant ([OAuth 2.0 and OIDC](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-implicit-grant.html))

Specify the realm in the request URL; for example:

```none
https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/par
```

The PAR endpoint supports the following parameters:

| Parameter               | Description                                                                                                         | Required                                                                                                                                                                                      |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `acr_values`            | The OpenID Connect authentication context class reference values.                                                   | Yes, if [required by the OpenID Connect provider](https://docs.pingidentity.com/pingoneaic/latest/am-oidc1/oidc-authentication-requirements.html)                                             |
| `claims`                | The user attributes to be returned in the ID token.                                                                 | No                                                                                                                                                                                            |
| `client_assertion`      | A signed JSON Web Token (JWT) to use as client credentials.                                                         | Yes, for [JWT profile](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/client-auth-jwt.html) authentication                                                                         |
| `client_assertion_type` | The type of assertion, `client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer`.    | Yes, for [JWT profile](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/client-auth-jwt.html) authentication                                                                         |
| `client_id`             | Uniquely identifies the application making the request.                                                             | Yes, even when it is also included in a `request` object                                                                                                                                      |
| `client_secret`         | The password for a confidential client.                                                                             | Yes, when authenticating with [Form parameters (HTTP POST)](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/client-auth-form.html)                                                  |
| `code_challenge`        | The code verifier generated for the PKCE flow.                                                                      | Yes, for confidential clients and for all clients using the [Authorization code grant with PKCE](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-authz-grant-pkce.html) flow |
| `code_challenge_method` | The method to derive the code challenge.                                                                            | Yes, when the `code_challenge` is hashed (recommended)                                                                                                                                        |
| `csrf`                  | The SSO token string linking the request to the user session to protect against Cross-Site Request Forgery attacks. | Yes, when gathering consent without a remote consent service                                                                                                                                  |
| `decision`              | Specifies whether the resource owner consents to the requested access.                                              | Yes, when gathering consent unless consent is already saved for the scope                                                                                                                     |
| `id_token_hint`         | Previously issued ID token previously passed as a hint about the end user's session with the client.                | No                                                                                                                                                                                            |
| `login_hint`            | String value that can be set to the ID the user uses to log in.                                                     | No                                                                                                                                                                                            |
| `nonce`                 | String value that associates the client session with the ID token.                                                  | No                                                                                                                                                                                            |
| `prompt`                | Specifies whether to prompt the end user for authentication and consent.                                            | No                                                                                                                                                                                            |
| `redirect_uri`          | The URI to return the resource owner to after authorization is complete.                                            | No                                                                                                                                                                                            |
| `request`               | A base64url-encoded JWT with the claims required for PAR validation.(1)                                             | Yes                                                                                                                                                                                           |
| `response_mode`         | Specifies the mechanism for returning response parameters.                                                          | No                                                                                                                                                                                            |
| `response_type`         | The type of response expected from the authorization server.                                                        | Yes                                                                                                                                                                                           |
| `save_consent`          | Specifies whether to store a resource owner's consented scopes.                                                     | No                                                                                                                                                                                            |
| `scope`                 | The scopes linked to the permissions requested by the client from the resource owner.                               | No                                                                                                                                                                                            |
| `service`               | The authentication journey to use when authenticating the resource owner.                                           | No                                                                                                                                                                                            |
| `state`                 | The value to maintain state between the request and the callback.                                                   | No, but strongly recommended                                                                                                                                                                  |
| `ui_locales`            | The end user's preferred languages for the user interface.                                                          | No                                                                                                                                                                                            |

(1) When you use a `request` object, define all the request parameters as claims in the JWT. Use only the following client authentication parameters alongside the `request`:

`client_assertion`\
`client_assertion_type`\
`client_id`\
`client_secret`

Otherwise, the response is an `Invalid parameter scope` error.

The following is an example of a PAR `request` object:

```json
{
  "client_id": "myClient",
  "nbf": 1594140030,
  "redirect_uri": "https://www.example.com:8443",
  "scope" : "write",
  "exp": 1594140390,
  "response_type" : "code",
  "code_challenge" :  "QR1D-7w1-rOQvlFe1CeqZigqaIpmZXatDMVvZ50o",
  "code_challenge_method" : "S256"
}
```

---

---
title: /oauth2/token/revoke
description: Endpoint defined in RFC 7009 Token Revocation to revoke access tokens and refresh tokens.
component: pingoneaic-api
page_id: pingoneaic-api:am-oauth2:oauth2-token-revoke-endpoint
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-oauth2/oauth2-token-revoke-endpoint.html
keywords: ["OAuth 2.0", "Scopes", "Grant Flow", "Endpoints", "Setup &amp; Configuration"]
---

# /oauth2/token/revoke

Endpoint defined in RFC 7009 [Token Revocation](https://www.rfc-editor.org/info/rfc7009) to revoke access tokens and refresh tokens.

When you revoke a refresh token, you revoke all tokens issued with the same authorization grant. If you got multiple access tokens for a single user with different authorization grants, you must revoke the tokens separately to invalidate each one.

Specify the realm in the request URL; for example:

```none
https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/token/revoke
```

The revoke token endpoint supports the following parameters:

| Parameter               | Description                                                                                                      | Required                                                                                                                                     |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `client_assertion`      | A signed JSON Web Token (JWT) to use as client credentials.                                                      | Yes, for [JWT profile](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/client-auth-jwt.html) authentication                        |
| `client_assertion_type` | The type of assertion, `client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer`. | Yes, for [JWT profile](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/client-auth-jwt.html) authentication                        |
| `client_id`             | Uniquely identifies the application making the request.                                                          | Yes                                                                                                                                          |
| `client_secret`         | The password for a confidential client.                                                                          | Yes, when authenticating with [Form parameters (HTTP POST)](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/client-auth-form.html) |
| `token`                 | The access token or refresh token to revoke.                                                                     | Yes                                                                                                                                          |

The following example revokes a refresh token:

```bash
$ curl \
--request POST \
--user "myClient:mySecret" \
--data "client_id=myClient" \
--data "token=refresh-token" \
"https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/token/revoke"
{}
```

---

---
title: /realm-config/agents/OAuth2Client
description: Invoke this Advanced Identity Cloud-specific endpoint to create, list, and delete OAuth 2.0 clients.
component: pingoneaic-api
page_id: pingoneaic-api:am-oauth2:rest-api-oauth2-client-admin-endpoint
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-oauth2/rest-api-oauth2-client-admin-endpoint.html
keywords: ["OAuth 2.0", "API Explorer", "Administration", "Endpoints", "Clients"]
section_ids:
  create-oauth2-client: Create an OAuth 2.0 client
  update-oauth2-clients: Update an OAuth 2.0 client
  query-oauth2-clients: Query OAuth 2.0 clients
  delete-an-oauth-2-0-client: Delete an OAuth 2.0 client
---

# /realm-config/agents/OAuth2Client

Invoke this Advanced Identity Cloud-specific endpoint to create, list, and delete OAuth 2.0 clients.

## Create an OAuth 2.0 client

This example registers a basic OAuth 2.0 client named `myClient` in the `alpha` realm. Append the name of the client to the URL:

```bash
$ curl \
--request PUT \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--header "Accept: application/json" \
--header "Authorization: Bearer <access-token>" \
--data '{
   "coreOAuth2ClientConfig":{
      "agentgroup":"",
      "status":{
         "inherited":true,
         "value":"string"
      },
      "userpassword":"mySecret",
      "clientType":{
         "inherited":false,
         "value":"Confidential"
      },
      "redirectionUris":{
         "inherited":false,
         "value":[
            "https://www.example.com:443/callback"
         ]
      },
      "scopes":{
         "inherited":false,
         "value":[
            "write",
            "read"
         ]
      },
      "defaultScopes":{
         "inherited":true,
         "value":[
            "write"
         ]
      },
      "clientName":{
         "inherited":true,
         "value":[
            "My Test Client"
         ]
      }
   },
   "advancedOAuth2ClientConfig":{
      "name":{
         "inherited":false,
         "value":[
            null
         ]
      },
      "grantTypes":{
         "inherited":true,
         "value":[
            "authorization_code",
            "client_credentials"
         ]
      },
      "tokenEndpointAuthMethod":{
         "inherited":true,
         "value":"client_secret_basic"
      }
   }
}' \
"https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/realm-config/agents/OAuth2Client/myClient"
```

> **Collapse: Display output**
>
> ```bash
> {
>     "_id": "myClient",
>     "_rev": "720283894",
>     "overrideOAuth2ClientConfig": {
>         "issueRefreshToken": true,
>         "validateScopePluginType": "PROVIDER",
>         "tokenEncryptionEnabled": false,
>         "evaluateScopePluginType": "PROVIDER",
>         "oidcMayActScript": "[Empty]",
>         "oidcClaimsScript": "[Empty]",
>         "scopesPolicySet": "oauth2Scopes",
>         "accessTokenModificationPluginType": "PROVIDER",
>         "authorizeEndpointDataProviderClass": "org.forgerock.oauth2.core.plugins.registry.DefaultEndpointDataProvider",
>         "oidcClaimsPluginType": "PROVIDER",
>         "providerOverridesEnabled": false,
>         "authorizeEndpointDataProviderScript": "[Empty]",
>         "statelessTokensEnabled": false,
>         "authorizeEndpointDataProviderPluginType": "PROVIDER",
>         "remoteConsentServiceId": null,
>         "enableRemoteConsent": false,
>         "validateScopeClass": "org.forgerock.oauth2.core.plugins.registry.DefaultScopeValidator",
>         "usePolicyEngineForScope": false,
>         "evaluateScopeClass": "org.forgerock.oauth2.core.plugins.registry.DefaultScopeEvaluator",
>         "overrideableOIDCClaims": [],
>         "accessTokenMayActScript": "[Empty]",
>         "evaluateScopeScript": "[Empty]",
>         "clientsCanSkipConsent": false,
>         "accessTokenModificationScript": "[Empty]",
>         "issueRefreshTokenOnRefreshedToken": true,
>         "validateScopeScript": "[Empty]"
>     },
>     "advancedOAuth2ClientConfig": {
>         "logoUri": {
>             "inherited": false,
>             "value": []
>         },
>         "subjectType": {
>             "inherited": false,
>             "value": "public"
>         },
>         "clientUri": {
>             "inherited": false,
>             "value": []
>         },
>         "tokenExchangeAuthLevel": {
>             "inherited": false,
>             "value": 0
>         },
>         "responseTypes": {
>             "inherited": false,
>             "value": [
>                 "code",
>                 "token",
>                 "id_token",
>                 "code token",
>                 "token id_token",
>                 "code id_token",
>                 "code token id_token",
>                 "device_code",
>                 "device_code id_token"
>             ]
>         },
>         "mixUpMitigation": {
>             "inherited": false,
>             "value": false
>         },
>         "customProperties": {
>             "inherited": false,
>             "value": []
>         },
>         "javascriptOrigins": {
>             "inherited": false,
>             "value": []
>         },
>         "policyUri": {
>             "inherited": false,
>             "value": []
>         },
>         "softwareVersion": {
>             "inherited": false
>         },
>         "tosURI": {
>             "inherited": false,
>             "value": []
>         },
>         "sectorIdentifierUri": {
>             "inherited": false
>         },
>         "tokenEndpointAuthMethod": {
>             "inherited": false,
>             "value": "client_secret_basic"
>         },
>         "refreshTokenGracePeriod": {
>             "inherited": false,
>             "value": 0
>         },
>         "isConsentImplied": {
>             "inherited": false,
>             "value": false
>         },
>         "softwareIdentity": {
>             "inherited": false
>         },
>         "grantTypes": {
>             "inherited": false,
>             "value": [
>                 "authorization_code"
>             ]
>         },
>         "require_pushed_authorization_requests": {
>             "inherited": false,
>             "value": false
>         },
>         "descriptions": {
>             "inherited": false,
>             "value": []
>         },
>         "requestUris": {
>             "inherited": false,
>             "value": []
>         },
>         "name": {
>             "inherited": false,
>             "value": [
>                 "null"
>             ]
>         },
>         "contacts": {
>             "inherited": false,
>             "value": []
>         },
>         "updateAccessToken": {
>             "inherited": false
>         }
>     },
>     "signEncOAuth2ClientConfig": {
>         "tokenEndpointAuthSigningAlgorithm": {
>             "inherited": false,
>             "value": "RS256"
>         },
>         "idTokenEncryptionEnabled": {
>             "inherited": false,
>             "value": false
>         },
>         "tokenIntrospectionEncryptedResponseEncryptionAlgorithm": {
>             "inherited": false,
>             "value": "A128CBC-HS256"
>         },
>         "requestParameterSignedAlg": {
>             "inherited": false
>         },
>         "authorizationResponseSigningAlgorithm": {
>             "inherited": false,
>             "value": "RS256"
>         },
>         "clientJwtPublicKey": {
>             "inherited": false
>         },
>         "idTokenPublicEncryptionKey": {
>             "inherited": false
>         },
>         "mTLSSubjectDN": {
>             "inherited": false
>         },
>         "jwkStoreCacheMissCacheTime": {
>             "inherited": false,
>             "value": 60000
>         },
>         "jwkSet": {
>             "inherited": false
>         },
>         "idTokenEncryptionMethod": {
>             "inherited": false,
>             "value": "A128CBC-HS256"
>         },
>         "jwksUri": {
>             "inherited": false
>         },
>         "tokenIntrospectionEncryptedResponseAlg": {
>             "inherited": false,
>             "value": "RSA-OAEP-256"
>         },
>         "authorizationResponseEncryptionMethod": {
>             "inherited": false
>         },
>         "userinfoResponseFormat": {
>             "inherited": false,
>             "value": "JSON"
>         },
>         "mTLSCertificateBoundAccessTokens": {
>             "inherited": false,
>             "value": false
>         },
>         "publicKeyLocation": {
>             "inherited": false,
>             "value": "jwks_uri"
>         },
>         "tokenIntrospectionResponseFormat": {
>             "inherited": false,
>             "value": "JSON"
>         },
>         "requestParameterEncryptedEncryptionAlgorithm": {
>             "inherited": false,
>             "value": "A128CBC-HS256"
>         },
>         "userinfoSignedResponseAlg": {
>             "inherited": false
>         },
>         "idTokenEncryptionAlgorithm": {
>             "inherited": false,
>             "value": "RSA-OAEP-256"
>         },
>         "requestParameterEncryptedAlg": {
>             "inherited": false
>         },
>         "authorizationResponseEncryptionAlgorithm": {
>             "inherited": false
>         },
>         "mTLSTrustedCert": {
>             "inherited": false
>         },
>         "jwksCacheTimeout": {
>             "inherited": false,
>             "value": 3600000
>         },
>         "userinfoEncryptedResponseAlg": {
>             "inherited": false
>         },
>         "idTokenSignedResponseAlg": {
>             "inherited": false,
>             "value": "RS256"
>         },
>         "tokenIntrospectionSignedResponseAlg": {
>             "inherited": false,
>             "value": "RS256"
>         },
>         "userinfoEncryptedResponseEncryptionAlgorithm": {
>             "inherited": false,
>             "value": "A128CBC-HS256"
>         }
>     },
>     "coreOpenIDClientConfig": {
>         "claims": {
>             "inherited": false,
>             "value": []
>         },
>         "backchannel_logout_uri": {
>             "inherited": false
>         },
>         "defaultAcrValues": {
>             "inherited": false,
>             "value": []
>         },
>         "jwtTokenLifetime": {
>             "inherited": false,
>             "value": 0
>         },
>         "defaultMaxAgeEnabled": {
>             "inherited": false,
>             "value": false
>         },
>         "clientSessionUri": {
>             "inherited": false
>         },
>         "defaultMaxAge": {
>             "inherited": false,
>             "value": 600
>         },
>         "postLogoutRedirectUri": {
>             "inherited": false,
>             "value": []
>         },
>         "backchannel_logout_session_required": {
>             "inherited": false,
>             "value": false
>         }
>     },
>     "coreOAuth2ClientConfig": {
>         "userpassword": null,
>         "status": {
>             "inherited": false,
>             "value": "Active"
>         },
>         "clientName": {
>             "inherited": false,
>             "value": []
>         },
>         "clientType": {
>             "inherited": false,
>             "value": "Confidential"
>         },
>         "loopbackInterfaceRedirection": {
>             "inherited": false,
>             "value": false
>         },
>         "defaultScopes": {
>             "inherited": false,
>             "value": []
>         },
>         "refreshTokenLifetime": {
>             "inherited": false,
>             "value": 0
>         },
>         "scopes": {
>             "inherited": false,
>             "value": [
>                 "write",
>                 "read"
>             ]
>         },
>         "accessTokenLifetime": {
>             "inherited": false,
>             "value": 0
>         },
>         "redirectionUris": {
>             "inherited": false,
>             "value": [
>                 "https://www.example.com:443/callback"
>             ]
>         },
>         "authorizationCodeLifetime": {
>             "inherited": false,
>             "value": 0
>         }
>     },
>     "coreUmaClientConfig": {
>         "claimsRedirectionUris": {
>             "inherited": false,
>             "value": []
>         }
>     },
>     "_type": {
>         "_id": "OAuth2Client",
>         "name": "OAuth2 Clients",
>         "collection": true
>     }
> }
> ```

## Update an OAuth 2.0 client

To update an existing OAuth 2.0 client, use a similar PUT request to the create request. Make sure you include *all* the attributes to be retained in the client configuration. If you omit an attribute in the JSON payload, the request effectively deletes that attribute from the client. This doesn't apply to the client secret attribute.

## Query OAuth 2.0 clients

This example lists the OAuth 2.0 clients in the `alpha` realm.

```bash
$ curl \
--request GET \
--header "Accept-API-Version: resource=1.0" \
--header "Authorization: Bearer <access-token>" \
"https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/realm-config/agents/OAuth2Client?_queryFilter=true"
```

> **Collapse: Display output**
>
> ```bash
> {
>   "result": [
>     {
>       "_id": "myClient",
>       "_rev": "-1788958356",
>       "overrideOAuth2ClientConfig": {
>         "issueRefreshToken": true,
>         "validateScopePluginType": "PROVIDER",
>         "tokenEncryptionEnabled": false,
>         "evaluateScopePluginType": "PROVIDER",
>         "oidcMayActScript": "[Empty]",
>         "oidcClaimsScript": "[Empty]",
>         "accessTokenModificationPluginType": "PROVIDER",
>         "authorizeEndpointDataProviderClass": "org.forgerock.oauth2.core.plugins.registry.DefaultEndpointDataProvider",
>         "oidcClaimsPluginType": "PROVIDER",
>         "providerOverridesEnabled": false,
>         "authorizeEndpointDataProviderScript": "[Empty]",
>         "statelessTokensEnabled": false,
>         "authorizeEndpointDataProviderPluginType": "PROVIDER",
>         "remoteConsentServiceId": null,
>         "enableRemoteConsent": false,
>         "validateScopeClass": "org.forgerock.oauth2.core.plugins.registry.DefaultScopeValidator",
>         "usePolicyEngineForScope": false,
>         "evaluateScopeClass": "org.forgerock.oauth2.core.plugins.registry.DefaultScopeEvaluator",
>         "overrideableOIDCClaims": [],
>         "accessTokenMayActScript": "[Empty]",
>         "evaluateScopeScript": "[Empty]",
>         "clientsCanSkipConsent": false,
>         "accessTokenModificationScript": "[Empty]",
>         "issueRefreshTokenOnRefreshedToken": true,
>         "validateScopeScript": "[Empty]"
>       },
>       "advancedOAuth2ClientConfig": {
>         "logoUri": [],
>         "subjectType": "public",
>         "clientUri": [],
>         "tokenExchangeAuthLevel": 0,
>         "responseTypes": [
>           "code",
>           "token",
>           "id_token",
>           "code token",
>           "token id_token",
>           "code id_token",
>           "code token id_token",
>           "device_code",
>           "device_code id_token"
>         ],
>         "mixUpMitigation": false,
>         "customProperties": [],
>         "javascriptOrigins": [],
>         "policyUri": [],
>         "softwareVersion": null,
>         "sectorIdentifierUri": null,
>         "tosURI": [],
>         "tokenEndpointAuthMethod": "client_secret_basic",
>         "isConsentImplied": false,
>         "refreshTokenGracePeriod": 0,
>         "softwareIdentity": null,
>         "grantTypes": [
>           "authorization_code"
>         ],
>         "require_pushed_authorization_requests": false,
>         "descriptions": [],
>         "requestUris": [],
>         "name": [],
>         "contacts": [],
>         "updateAccessToken": null
>       },
>       "signEncOAuth2ClientConfig": {
>         "tokenEndpointAuthSigningAlgorithm": "RS256",
>         "idTokenEncryptionEnabled": false,
>         "tokenIntrospectionEncryptedResponseEncryptionAlgorithm": "A128CBC-HS256",
>         "requestParameterSignedAlg": null,
>         "authorizationResponseSigningAlgorithm": "RS256",
>         "clientJwtPublicKey": null,
>         "idTokenPublicEncryptionKey": null,
>         "mTLSSubjectDN": null,
>         "jwkStoreCacheMissCacheTime": 60000,
>         "jwkSet": null,
>         "idTokenEncryptionMethod": "A128CBC-HS256",
>         "jwksUri": null,
>         "tokenIntrospectionEncryptedResponseAlg": "RSA-OAEP-256",
>         "authorizationResponseEncryptionMethod": null,
>         "userinfoResponseFormat": "JSON",
>         "mTLSCertificateBoundAccessTokens": false,
>         "publicKeyLocation": "jwks_uri",
>         "tokenIntrospectionResponseFormat": "JSON",
>         "requestParameterEncryptedEncryptionAlgorithm": "A128CBC-HS256",
>         "userinfoSignedResponseAlg": null,
>         "idTokenEncryptionAlgorithm": "RSA-OAEP-256",
>         "requestParameterEncryptedAlg": null,
>         "authorizationResponseEncryptionAlgorithm": null,
>         "mTLSTrustedCert": null,
>         "jwksCacheTimeout": 3600000,
>         "userinfoEncryptedResponseAlg": null,
>         "idTokenSignedResponseAlg": "RS256",
>         "userinfoEncryptedResponseEncryptionAlgorithm": "A128CBC-HS256",
>         "tokenIntrospectionSignedResponseAlg": "RS256"
>       },
>       "coreOpenIDClientConfig": {
>         "claims": [],
>         "backchannel_logout_uri": null,
>         "defaultAcrValues": [],
>         "jwtTokenLifetime": 0,
>         "defaultMaxAgeEnabled": false,
>         "clientSessionUri": null,
>         "defaultMaxAge": 600,
>         "postLogoutRedirectUri": [],
>         "backchannel_logout_session_required": false
>       },
>       "coreOAuth2ClientConfig": {
>         "status": "Active",
>         "clientName": [],
>         "clientType": "Confidential",
>         "loopbackInterfaceRedirection": false,
>         "defaultScopes": [],
>         "agentgroup": null,
>         "refreshTokenLifetime": 0,
>         "scopes": [],
>         "accessTokenLifetime": 0,
>         "redirectionUris": [],
>         "authorizationCodeLifetime": 0
>       },
>       "coreUmaClientConfig": {
>         "claimsRedirectionUris": []
>       },
>       "_type": {
>         "_id": "OAuth2Client",
>         "name": "OAuth2 Clients",
>         "collection": true
>       }
>     }
>   ],
>   "resultCount": 1,
>   "pagedResultsCookie": null,
>   "totalPagedResultsPolicy": "EXACT",
>   "totalPagedResults": 1,
>   "remainingPagedResults": -1
> }
> ```

## Delete an OAuth 2.0 client

This example deletes an OAuth 2.0 client named `myClient` in the `alpha` realm. Append the name of the client to the URL:

```bash
$ curl \
--request DELETE \
--header "Accept-API-Version: resource=1.0" \
--header "Authorization: Bearer <access-token>" \
"https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/realm-config/agents/OAuth2Client/myClient"
{
    "_id": "myClient",
    "_rev": "-614477476",
    ...
}
```

---

---
title: /users/user/oauth2/applications
description: Invoke this Advanced Identity Cloud-specific endpoint to list the applications granted OAuth 2.0 access and to delete tokens for a specified client.
component: pingoneaic-api
page_id: pingoneaic-api:am-oauth2:rest-api-oauth2-applications-endpoint
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-oauth2/rest-api-oauth2-applications-endpoint.html
keywords: ["OAuth 2.0", "API Explorer", "Endpoints", "Clients"]
section_ids:
  query-applications: Query applications
  delete-tokens-for-a-client: Delete tokens for a client
---

# /users/user/oauth2/applications

Invoke this Advanced Identity Cloud-specific endpoint to list the applications granted OAuth 2.0 access and to delete tokens for a specified client.

To call the endpoint, you must compose the path to the realm where the client is registered.

## Query applications

This example lists all the OAuth 2.0 clients holding active tokens granted in the `alpha` realm for the resource owner, `bjensen`. You must provide the SSO token of the tenant administrator or the resource owner as a header, and include the resource owner's `_id` in the URL:

```bash
$  curl --request GET \
--header "Accept-API-Version: resource=1.1" \
--header "<session-cookie-name>: Ua6fsH2vjgHqVY..." \
"https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/users/1dff18dc-ac57-4388-8127-dff309f80002/oauth2/applications?_queryFilter=true"
{
    "result": [
        {
            "_id": "myClient",
            "_rev": "-1121350941",
            "name": null,
            "scopes": {
                "write": "write"
            },
            "expiryDateTime": null,
            "logoUri": null
        }
    ],
    "resultCount": 1,
    "pagedResultsCookie": null,
    "totalPagedResultsPolicy": "NONE",
    "totalPagedResults": -1,
    "remainingPagedResults": -1
}
```

On success, Advanced Identity Cloud returns an HTTP 200 code and a JSON object with information about the tokens, such as the granted scopes and the ID for the client to which they belong.

## Delete tokens for a client

The following example deletes all tokens held by the OAuth 2.0 client `myClient` granted in the `alpha` realm by `bjensen`. You must provide the SSO token of the tenant administrator or the resource owner as a header, and include the `_id` of the resource owner and `_id` of the client (`myClient`) in the URL:

```bash
$ curl --request DELETE \
--header "Accept-API-Version: resource=1.1" \
--header "<session-cookie-name>: Ua6fsH2vjgHqVY..." \
"https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/users/1dff18dc-ac57-4388-8127-dff309f80002/oauth2/applications/myClient"
{
    "_id": "myClient",
    "_rev": "-1121350941",
    "name": null,
    "scopes": {
        "write": "write"
    },
    "expiryDateTime": null,
    "logoUri": null
}
```

On success, Advanced Identity Cloud returns an HTTP 200 code and a JSON object with information about the deleted tokens, such as the granted scopes and ID of the client.

---

---
title: OAuth 2.0 administration endpoints
description: Advanced Identity Cloud exposes the following administration and supporting REST endpoints:
component: pingoneaic-api
page_id: pingoneaic-api:am-oauth2:oauth2-admin-endpoints
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-oauth2/oauth2-admin-endpoints.html
keywords: ["OAuth 2.0", "Endpoints", "Administration", "REST API"]
---

# OAuth 2.0 administration endpoints

Advanced Identity Cloud exposes the following administration and supporting REST endpoints:

**OAuth 2.0 administration and supporting endpoints**

| Endpoint                            | Description                                                                                                                                                                                    |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/realm-config/agents/OAuth2Client` | Register, list, and delete OAuth 2.0 clients (Advanced Identity Cloud specific-endpoint)                                                                                                       |
| `/users/user/oauth2/applications`   | List OAuth 2.0 clients holding active tokens granted by specific resource owners, and delete tokens for a combination of resource owner and client (Advanced Identity Cloud-specific endpoint) |

---

---
title: OAuth 2.0 client endpoints
description: Client applications can use the following OAuth 2.0 authorization server endpoints:
component: pingoneaic-api
page_id: pingoneaic-api:am-oauth2:oauth2-client-endpoints
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-oauth2/oauth2-client-endpoints.html
keywords: ["OAuth 2.0", "Endpoints", "Authorization", "Clients", "REST API"]
---

# OAuth 2.0 client endpoints

Client applications can use the following OAuth 2.0 authorization server endpoints:

| Endpoint               | Description                                                                                                                |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `/oauth2/par`          | Register a pushed authorization request and get a request URI (RFC 9126 PAR endpoint)                                      |
| `/oauth2/authorize`    | Obtain consent and an authorization grant (RFC 6749 authorization endpoint)                                                |
| `/oauth2/bc-authorize` | Initiate backchannel authorization (Backchannel flow endpoint)                                                             |
| `/oauth2/access_token` | Obtain an access token (RFC 6749 token endpoint)                                                                           |
| `/oauth2/device/code`  | Obtain a device code (Device flow endpoint)                                                                                |
| `/oauth2/device/user`  | Obtain consent and authorization grant (Device flow endpoint)                                                              |
| `/oauth2/token/revoke` | Revoke access tokens and refresh tokens (RFC 7009 endpoint)                                                                |
| `/oauth2/introspect`   | Retrieve metadata about a token, such as approved scopes and the context in which the token was issued (RFC 7662 endpoint) |
| `/json/token/macaroon` | Retrieve metadata about a macaroon, and add caveats.                                                                       |

Learn more about related endpoints in:

* [OAuth 2.0 administration endpoints](oauth2-admin-endpoints.html)

* [OIDC 1.0 endpoints](../am-oidc1/oidc-client-endpoints.html)

---

---
title: OAuth 2.0 endpoint parameters
description: Requests to OAuth 2.0 endpoints use the following parameters.
component: pingoneaic-api
page_id: pingoneaic-api:am-oauth2:oauth2-parameters
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-oauth2/oauth2-parameters.html
keywords: ["OAuth 2.0", "Endpoints", "Properties"]
section_ids:
  acr-values: acr_values
  actor-token: actor_token
  actor-token-type: actor_token_type
  auth-chain: auth_chain
  claims: claims
  client-assertion: client_assertion
  client-assertion-type: client_assertion_type
  client-id: client_id
  client-secret: client_secret
  cnf-key: cnf_key
  code-challenge: code_challenge
  code-challenge-method: code_challenge_method
  code-verifier: code_verifier
  csrf: csrf
  decision: decision
  grant-type: grant_type
  id-token-hint: id_token_hint
  login-hint: login_hint
  nonce: nonce
  prompt: prompt
  redirect-uri: redirect_uri
  response-mode: response_mode
  response-type: response_type
  the-request-parameter: request
  general-validation-rules: General validation rules
  jar-validation-rules: JAR validation rules
  oidc-validation-rules: OIDC validation rules
  par-validation-rules: PAR validation rules
  example-request-object: Example request object
  request-uri: request_uri
  requested-token-type: requested_token_type
  save-consent: save_consent
  scope: scope
  service: service
  state: state
  subject-token: subject_token
  subject-token-type: subject_token_type
  ui-locales: ui_locales
---

# OAuth 2.0 endpoint parameters

Requests to OAuth 2.0 endpoints use the following parameters.

Refer to the individual OAuth 2.0 endpoint pages to determine the required and optional parameters for each endpoint.

## `acr_values`

The OpenID Connect authentication context class reference values. [OpenID Connect (OIDC) flows](https://openid.net/specs/openid-connect-core-1_0.html) only.

Authentication context class reference values communicate acceptable Levels of Assurance (LoAs) users must satisfy when authenticating to the OpenID provider. Learn more in [Authentication requirements](https://docs.pingidentity.com/pingoneaic/latest/am-oidc1/oidc-authentication-requirements.html).

## `actor_token`

The token representing a delegate acting on behalf of another identity in [Token exchange](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/token-exchange.html).

## `actor_token_type`

The type of the actor token:

* `urn:ietf:params:oauth:token-type:access_token`

* `urn:ietf:params:oauth:token-type:id_token`

## `auth_chain`

A string naming the journey to authenticate the resource owner for [Resource owner password credentials grant](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-ropc-grant.html). The journey must permit username-password authentication without UI interaction. Otherwise, the request results in an HTTP 500 Internal Server Error.

Default: The default authentication journey for the realm.

## `claims`

A JSON object containing the user attributes to return in the ID token. [OIDC flows](https://openid.net/specs/openid-connect-core-1_0.html) only.

## `client_assertion`

A signed JSON Web Token (JWT) to use as client credentials for [JWT profile](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/client-auth-jwt.html) authentication.

## `client_assertion_type`

The type of assertion for [JWT profile](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/client-auth-jwt.html) authentication.

Set `client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer`.

## `client_id`

A unique string identifier for the application making the request.

For a [pushed authorization request](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-authz-grant-par.html) or a [JWT-secured authorization request](https://www.rfc-editor.org/rfc/rfc9101.html) (RFC 9101), this value must match the `client_id` claim in the `request` object.

## `client_secret`

A string password credential for the confidential client application making the request.

Use this parameter for client authentication with [Form parameters (HTTP POST)](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/client-auth-form.html).

Do not use with the `cnf_key` parameter.

## `cnf_key`

A base64-encoded JSON Web Key (JWK) for [JWK-based proof-of-possession](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-PoP-JWK.html).

Do not use with the `client_secret` parameter.

## `code_challenge`

A generated code verifier string for RFC 7636 [Proof Key for Code Exchange](https://www.rfc-editor.org/rfc/rfc7636) (PKCE).

Learn more in [Generate a code verifier and a code challenge](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-authz-grant-pkce.html#proc-auth-code-generate-pkce).

## `code_challenge_method`

A string specifying the method to derive the PKCE code challenge:

* `plain` (default; plaintext code challenge )

* `S256` (recommended; hashed code challenge)

## `code_verifier`

A random string correlating a PKCE authorization request with the token request.

## `csrf`

The SSO token string linking the request to user session to protect against Cross-Site Request Forgery (CSRF) attacks.

This parameter duplicates the value of the session cookie, the resource owner's SSO token.

Built-in consent pages include this parameter once the resource owner has authenticated, and send it with the resource owner's consent. Custom consent pages and flows that do not use a browser must set this parameter explicitly unless you use a [Remote consent service](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-remote-consent.html). Find an example in [Authorization code grants](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-authz-grant.html).

## `decision`

A string indicating whether the resource owner consents to the requested access:

* `allow` to grant consent

* Any other value denies consent

## `grant_type`

A string specifying the type of grant to acquire an access token:

* `authorization_code`

  For [authorization code grants](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-authz-grant.html).

* `client_credentials`

  For the [client credentials grant](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-client-cred-grant.html).

* `password`

  For the [Resource owner password credentials grant](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-ropc-grant.html).

* `refresh_token`

  To [refresh an access token](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-refresh-tokens.html).

* `urn:ietf:params:oauth:grant-type:device_code`

  For the [device grant](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-device-flow.html). Advanced Identity Cloud also supports the earlier `http://oauth.net/grant_type/device/1.0` specification.

* `urn:ietf:params:oauth:grant-type:saml2-bearer`

  For the [SAML 2.0 profile for authorization](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-saml2-bearer-grant.html).

* `urn:ietf:params:oauth:grant-type:jwt-bearer`

  For the [JWT profile for authorization](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-jwt-bearer-grant.html).

* `urn:ietf:params:oauth:grant-type:token-exchange`

  For the [Token exchange](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/token-exchange.html).

* `urn:openid:params:grant-type:ciba`

  For the [Backchannel request grant](https://docs.pingidentity.com/pingoneaic/latest/am-oidc1/openid-connect-backchannel-request-flow.html).

## `id_token_hint`

A previously issued ID token passed as a hint about the end user's session with the client. [OIDC flows](https://openid.net/specs/openid-connect-core-1_0.html) only.

Set the `response_type` and `prompt` parameters to `none` when using this parameter. Learn more in [Session Management Draft 10](https://docs.pingidentity.com/pingoneaic/latest/am-oidc1/session-management.html#session_management_state).

## `login_hint`

A string specifying the ID used to log in. [OIDC flows](https://openid.net/specs/openid-connect-core-1_0.html) only.

The ID depends on the authentication journey.

When provided as part of the OpenID Connect authentication request, an `HttpOnly` cookie (only sent over HTTPS) named `oidcLoginHint` gets the value of `login_hint`. Learn more in [GSMA Mobile Connect](https://docs.pingidentity.com/pingoneaic/latest/am-oidc1/oidc-mobile-connect.html).

## `nonce`

A string linking the client session with the ID token to mitigate against replay attacks. [OIDC flows](https://openid.net/specs/openid-connect-core-1_0.html) only.

## `prompt`

A space-separated, case-sensitive list of ASCII strings that indicates whether to prompt the end user for authentication and consent. [OIDC flows](https://openid.net/specs/openid-connect-core-1_0.html) only.

* `consent`

  Prompt the end user for consent even if a consent response was previously saved.

* `login`

  Prompts the end user to authenticate using the journey specified with the [`service`](#service) parameter. When the user re-authenticates, Advanced Identity Cloud destroys the original session and creates a new one for the new journey.

  Default: The default journey for the realm.

* `none`

  Do not display authentication or consent pages. Use this only when you set `id_token_hint` and `response_type=none`.

## `redirect_uri`

The URI to return the resource owner to after authorization is complete.

Default: A value from the client profile Sign-in URLs setting in the Advanced Identity Cloud admin console.

## `response_mode`

A string specifying the mechanism for returning response parameters:

* `form_post`

  Return a self-submitting form that contains the code instead of redirecting to the redirect URL with the code as a string parameter. For details, refer to [OAuth 2.0 Form Post Response Mode](https://openid.net/specs/oauth-v2-form-post-response-mode-1_0.html).

* `fragment`

  Return parameters encoded in the URL fragment; default when `response_type=token`.

* `fragment.jwt`

  Return a JWT in a fragment.

* `jwt`

  Return parameters in a JWT; in a query string for the `code` response type, or appended to the fragment for the `token` response type.

  A JWT-secured authorization response (JARM) returns authorization response parameters in a signed, optionally encrypted, JWT.

  Configure the algorithms to secure the JWT in the Advanced Identity Cloud admin console under Applications > *Client ID* > Sign On > General Settings > Show advanced settings > Signing and Encryption.

  In addition to claims specific to the response type, such as `code` or `access_token`, the JWT contains these mandatory claims:

  * `iss`: the URL of the issuer—​the authorization server that generated the response

  * `aud`: the audience—​the client ID intended as the response recipient

  * `exp`: the expiration of the JWT—​10 minutes is the recommended maximum

  On error, the JWT contains:

  * An `error` string

  * A `state` string if specified by the client

  * An error description

  For details, refer to [JWT-Secured Authorization Response Mode for OAuth 2.0 (JARM)](https://openid.net/specs/openid-financial-api-jarm.html).

* `query`

  Return parameters encoded in the query string; default when `response_type=code`.

* `query.jwt`

  Return a JWT in a query parameter. Do *not* use this with `id_token` or `token` response types unless the response JWT is encrypted.

For details, refer to [Response Modes](https://openid.net/specs/oauth-v2-multiple-response-types-1_0.html#ResponseModes). Advanced Identity Cloud publishes supported response modes as `response_modes_supported` through the [/oauth2/.well-known/openid-configuration](../am-oidc1/rest-api-oidc-discovery-configuration.html) endpoint.

## `response_type`

A string specifying the response expected from the authorization server:

* `code`

  An authorization code for an authorization code grant

* `code id_token`

  An authorization code and an ID token for a hybrid grant

* `code token`

  An authorization code and an access token for a hybrid grant

* `code token id_token`

  An authorization code, an access token, and an ID token for a hybrid grant

* `id_token`

  An ID token for an implicit grant

* `none`

  Do not issue any token or code in the response; for use with [`id_token_hint`](#id-token-hint) only

* `token`

  An access token for an implicit grant

* `token id_token`

  An access token and an ID token for an implicit grant

## `request`

A base64url-encoded JWT whose claims are required for an [OIDC flow](https://openid.net/specs/openid-connect-core-1_0.html), a [JWT-secured authorization (JAR) request](https://www.rfc-editor.org/rfc/rfc9101.html) (RFC 9101), or a [pushed authorization request (PAR)](https://www.rfc-editor.org/info/rfc9126) (RFC 9126).

This JWT is called the *request object*.

Advanced Identity Cloud validates request objects according to:

* The type of request

* The OAuth 2.0 provider configuration (specifically, the [Request Object Processing Specification](https://docs.pingidentity.com/pingoneaic/latest/am-reference/services-configuration.html#config-request-object-proc-spec) setting)

* The value of the ESV named `esv-oauth2-provider-request-object-processing-enforced`, if set

The validation rules apply whether you pass the request object by value with the `request` parameter or as a reference with the `request_uri` parameter:

> **Collapse: How Advanced Identity Cloud determines which rules to apply**
>
> | Input                 |                 |                  |                  | Behavior     |
> | --------------------- | --------------- | ---------------- | ---------------- | ------------ |
> | Specification value 1 | `enforced` ESV2 | OIDC parameters3 | `/par` endpoint4 | Rule applied |
> | OIDC                  | `false`         | Yes              | No               | OIDC         |
> | OIDC                  | `false`         | No               | No               | JAR          |
> | OIDC                  | `true`          | Yes              | No               | OIDC         |
> | OIDC                  | `true`          | No               | No               | OIDC         |
> | JAR                   | `false`         | Yes              | No               | JAR          |
> | JAR                   | `false`         | No               | No               | JAR          |
> | JAR                   | `true`          | Yes              | No               | JAR          |
> | JAR                   | `true`          | No               | No               | JAR          |
> | OIDC                  | `false`         | Yes              | Yes              | PAR          |
> | OIDC                  | `false`         | No               | Yes              | PAR          |
> | OIDC                  | `true`          | Yes              | Yes              | PAR          |
> | OIDC                  | `true`          | No               | Yes              | PAR          |
> | JAR                   | `false`         | Yes              | Yes              | PAR          |
> | JAR                   | `false`         | No               | Yes              | PAR          |
> | JAR                   | `true`          | Yes              | Yes              | PAR          |
> | JAR                   | `true`          | No               | Yes              | PAR          |
>
> 1 Value of the Request Object Processing Specification setting
>
> 2 The value of the ESV named `esv-oauth2-provider-request-object-processing-enforced`
>
> 3 Request contains OIDC parameters
>
> 4 Request is sent to [/oauth2/par](oauth2-par-endpoint.html) endpoint

### General validation rules

These rules apply for all request objects:

* The request object must include a `client_id` that matches the [`client_id`](#client-id) parameter of the request.

* If the request object is signed or encrypted, you *must* include the `iss` and `aud` parameters, as shown in the [Example request object](#example-request-object).

  For the public keys to encrypt a request object JWT, send a request to the realm's [/oauth2/connect/jwk\_uri](../am-oidc1/managing-jwk_uri.html) endpoint.

* The `exp` (expiration time) and `nbf` (not before) claims set the timeframe during which the request object is valid.

  If the OAuth 2.0 provider settings declare them mandatory, you *must* include the `exp` and `nbf` claims.

  If specified, validation uses these claims even when the OAuth 2.0 provider settings don't require them.

  Read the [OAuth 2.0 provider](https://docs.pingidentity.com/pingoneaic/latest/am-reference/services-configuration.html#realm-oauth-oidc) configuration reference to make sure the values meet the requirements of the [Financial-grade API (FAPI)](https://openid.net/specs/openid-financial-api-part-2-1_0-final.html#authorization-server) security profile.

* Compressed JWTs mustn't be larger than 32 KiB (32768 bytes) when uncompressed.

### JAR validation rules

* The request object is signed. (It *may* also be encrypted.)

* The authorization request uses only the request object claims, even when the request specifies the same claims in query string parameters.

### OIDC validation rules

* The request object doesn't require signing or encryption.

* You *may* send query string parameters and a request object in the same request.

  You can keep sensitive information protected in the request object, and keep parameters that change frequently, such as `nonce` and `state`, visible and mutable across calls.

  The claims in the request object supersede the query string parameters.

* You *must* include the `response_type` as a query string parameter, even if you include it in the request object.

  The values in the request object must match those passed as query string parameters.

* If the request object contains the `openid` scope, you *must* include the `openid` scope in the request syntax.

  The `scope` claim *may* differ from the `scope` query string parameter. Use this to protect application-related scopes in the request object, but process the request as part of an OpenID Connect flow.

### PAR validation rules

* The request object *must* be signed. It *may* be encrypted.

* You *must* include claims for all other parameters required for the successful completion of the grant flow.

  For example, include the `code_challenge` for an [Authorization code grant with PKCE](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-authz-grant-pkce.html) flow.

* When you include the request object, omit all other parameters except to authenticate the client.

  The request object *must* include claims for all other request details. Otherwise, the response is an `Invalid parameter scope` error.

### Example request object

The following example JWT request object includes OIDC claims and `iss`, `aud`, `nbf`, and `exp` claims. Advanced Identity Cloud ignores keys specified in JWT headers, such as `jku` and `jwe`:

```json
{
  "client_id": "myClient",
  "iss": "myClient",
  "aud": "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha",
  "nbf": 1675351332,
  "exp": 1675351692,
  "redirect_uri": "https://www.example.com:8443",
  "scope": "openid profile",
  "claims": {
    "id_token": {
      "acr": {
        "essential": true,
        "values": ["example_journey1", "example_journey2"]
      }
    }
  }
}
```

To pass the request object by value, specify the encoded JWT as shown in this example OIDC call:

```
https://<tenant-env-fqdn>/am/oauth2/realms/root/authorize? \
&request=eyJhbGciOiJSUzI1NiIsImtpZCI6ImsyYmRjIn0.ew0KICJpc3MiOiAiczZCaGRSa3... \
&client_id=myClient \
&scope=openid profile \
&response_type=code%20id_token \
&nonce=abc123 \
&state=123abc
```

## `request_uri`

A reference to [JWT request object(s)](#the-request-parameter).

* For [PAR flows](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-authz-grant-par.html), this references the data at the time of the PAR request.

  The authorization request fails if the request URI has expired.

* For [OIDC flows](https://docs.pingidentity.com/pingoneaic/latest/am-oidc1/oidc-implementing-flows.html) and [JAR](https://www.rfc-editor.org/rfc/rfc9101.html) requests, this references an array of URIs to retrieve request objects whose claims constitute the request parameters.

  You must pre-register the URIs in the client profile. In the Advanced Identity Cloud admin console, go to Applications > *Client ID* > Sign On > Show advanced settings > Authentication > Request URIs. Each request URI must not exceed 512 ASCII characters and must use either HTTP or HTTPS; for example, `https://www.example.com:8443/JTWs/myJWT`.

  Advanced Identity Cloud caches the request objects to avoid requesting them too often. To force Advanced Identity Cloud to flush the cache, add a unique fragment to the `request_uri` parameter; for example, `?request_uri=https://www.example.com:8443/JTWs/myJWT#foo`.

* The [PAR](https://www.rfc-editor.org/rfc/rfc9126.html) and [JAR](https://www.rfc-editor.org/rfc/rfc9101.html#section-5.2) specifications indicate the following:

  * The authorization server should ignore authorize parameters outside the `request_uri`.

  * When sending a JWT-Secured Authorization Request (JAR), the `request_uri` *must* be an `https` URI.

  To enforce this behavior in Advanced Identity Cloud, [create an ESV variable](https://docs.pingidentity.com/pingoneaic/latest/tenants/esvs.html#variables) named `esv.oauth2.request.object.restrictions.enforced` and set its value to `true`.

## `requested_token_type`

The type of token requested for [Token exchange](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/token-exchange.html):

* `urn:ietf:params:oauth:token-type:access_token` (default)

* `urn:ietf:params:oauth:token-type:id_token`

## `save_consent`

`save_consent=on` means save the scopes the resource owner's consented to.

Saving consent requires prior configuration. Learn more in [Store consent decisions](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-manage-consent.html#store-consent-decisions).

## `scope`

A string specifying the permissions the client application requests from the resource owner. Separate scopes with spaces.

Some grants, such as the authorization code grant, do not call the token endpoint with the scope. The scope is defined in the authorization code. For details, refer to the documentation for the flow under [OAuth 2.0 grant flows](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-implementing-flows.html).

Default: The default scopes specified in the client profile or the OAuth 2.0 provider configuration.

## `service`

A string naming the journey to authenticate the resource owner.

Default: The default authentication journey for the realm.

Learn more in [Authentication parameters](https://docs.pingidentity.com/pingoneaic/latest/am-authentication/authn-from-browser.html#authn-from-browser-parameters).

## `state`

A string value to maintain state between the request and the callback.

During authentication, the client sends this parameter to the authorization server. The authorization server sends it back unchanged in the response.

Use the value to ensure the response belongs to the user who initiated the requests. This mitigates against CSRF attacks.

Use a base64-encoded string of data that is unique to a user and to this request.

## `subject_token`

The original token to exchange in [Token exchange](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/token-exchange.html).

## `subject_token_type`

The type of the subject token:

* `urn:ietf:params:oauth:token-type:access_token`

* `urn:ietf:params:oauth:token-type:id_token`

## `ui_locales`

A string indicating the end user's preferred languages for the user interface. [OIDC flows](https://openid.net/specs/openid-connect-core-1_0.html) only.

The `ui_locales` parameter is a space-separated list ordered by preference; for example, `en fr-CA fr`.