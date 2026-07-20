---
title: /json/token/macaroon
description: Use the /json/token/macaroon endpoint to inspect and manipulate macaroon tokens in PingAM OAuth 2.0 and OpenID Connect flows
component: pingam
version: 8.1
page_id: pingam:am-oauth2:oauth2-introspect-macaroon-endpoint
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oauth2/oauth2-introspect-macaroon-endpoint.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "OpenID Connect (OIDC)", "Endpoints", "Macaroons", "Scope"]
page_aliases: ["varlist-oauth2-introspect-macaroon-endpoint.adoc", "oauth2-guide:oauth2-introspect-macaroon-endpoint.adoc"]
---

# /json/token/macaroon

The `/json/token/macaroon` endpoint lets you inspect and manipulate [macaroon tokens](oauth2-macaroons.html).

Specify the realm in the request URL; for example:

```none
https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/token/macaroon
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
'https://am.example.com:8443/am/json/realms/root/realms/alpha/token/macaroon?_action=restrict'
{
  "macaroon": "<restricted-macaroon-token>"
}

$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "cache-control: no-cache" \
--data '{"macaroon": "<restricted-macaroon-token>"}' \
'https://am.example.com:8443/am/json/realms/root/realms/alpha/token/macaroon?_action=inspect'
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

|   |                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | OIDC clients must ensure the following information is present in the JSON:- The `openid` scope; for example, `"scopes": ["profile", "openid"]`.

- The `id_token` response type; for example, `"response_types": ["code", "id_token code"]`. |

---

---
title: /oauth2/access_token
description: Use the /oauth2/access_token endpoint to acquire access or refresh tokens with various OAuth 2.0 grant flows in PingAM
component: pingam
version: 8.1
page_id: pingam:am-oauth2:oauth2-access_token-endpoint
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oauth2/oauth2-access_token-endpoint.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "Endpoints", "Authorization", "REST API"]
page_aliases: ["oauth2-guide:oauth2-access_token-endpoint.adoc"]
section_ids:
  request_parameters: Request parameters
  responses: Responses
---

# /oauth2/access\_token

The `/oauth2/access_token` endpoint is the OAuth 2.0 [token endpoint](https://www.rfc-editor.org/rfc/rfc6749.html#section-3.2) (RFC 6749).

Use this endpoint to acquire an access or refresh token with the following flows:

* Authorization code grant ([OAuth 2.0 and OIDC](oauth2-authz-grant.html))

* Authorization code grant with PKCE ([OAuth 2.0 and OIDC](oauth2-authz-grant-pkce.html))

* Authorization code grant with PAR ([OAuth 2.0](oauth2-authz-grant-par.html))

* Client credentials grant ([OAuth 2.0](oauth2-client-cred-grant.html))

* Resource owner password credentials grant ([OAuth 2.0](oauth2-ropc-grant.html))

* Device flow ([OAuth 2.0](oauth2-device-flow.html))

* SAML 2.0 profile for authorization grant ([OAuth 2.0](oauth2-saml2-bearer-grant.html))

* Token exchange ([OAuth 2.0 | OpenID Connect](token-exchange.html))

Specify the realm in the request URL; for example:

```none
https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/access_token
```

## Request parameters

The `access_token` endpoint supports the following parameters:

| Parameter               | Description                                                                                                               | Required                                                                           |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `actor_token`           | The token representing a delegate acting on behalf of another identity.                                                   | Yes, for [Token exchange](token-exchange.html)                                     |
| `actor_token_type`      | The type of actor token.                                                                                                  | Yes, for [Token exchange](token-exchange.html)                                     |
| `auth_chain`            | A string naming the journey to authenticate the resource owner.                                                           | No, only for [Resource owner password credentials grant](oauth2-ropc-grant.html)   |
| `assertion`             | A string holding a base64-encoded then URL-encoded SAML 2.0 assertion                                                     | Yes, when `grant_type=urn:ietf:params:oauth:grant-type:saml2-bearer`               |
| `client_assertion`      | A signed JSON Web Token (JWT) to use as client credentials.                                                               | Yes, for [JWT profile](client-auth-jwt.html) authentication                        |
| `client_assertion_type` | The type of assertion, `client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer`.          | Yes, for [JWT profile](client-auth-jwt.html) authentication                        |
| `client_id`             | Uniquely identifies the application making the request.                                                                   | Yes                                                                                |
| `client_secret`         | The password for a confidential client; do not use with `cnf_key`.                                                        | Yes, when authenticating with [Form parameters (HTTP POST)](client-auth-form.html) |
| `cnf_key`               | A base64-encoded JSON Web Key (JWK) or hash of the X.509 certificate; do not use with `client_secret`.                    | Yes, for [Proof-of-possession](oauth2-proof-of-possession.html).                   |
| `code`                  | A string holding the authorization code for an authorization code grant.                                                  | Yes, when `grant_type=authorization_code`                                          |
| `code_verifier`         | A random string correlating a PKCE authorization request with the token request.                                          | Yes, for flows with PKCE                                                           |
| `device_code`           | A string holding the device code requested from the user for a device flow.                                               | Yes, when `grant_type=urn:ietf:params:oauth:grant-type:device_code`                |
| `grant_type`            | A string specifying the type of grant to acquire an access token.                                                         | Yes                                                                                |
| `password`              | A string holding the resource owner password for the [Resource owner password credentials grant](oauth2-ropc-grant.html). | Yes, when `grant_type=password`                                                    |
| `redirect_uri`          | The URI to return the resource owner to after authorization is complete.                                                  | Yes, when `grant_type=authorization_code` and it was included earlier in the flow  |
| `refresh_token`         | The refresh to get a new access token.                                                                                    | Yes, for [Refresh tokens](oauth2-refresh-tokens.html)                              |
| `requested_token_type`  | The type of token requested in exchange.                                                                                  | No, but recommended for [Token exchange](token-exchange.html)                      |
| `scope`                 | The scopes linked to the permissions requested by the client from the resource owner.                                     | No                                                                                 |
| `subject_token`         | The original token to exchange.                                                                                           | Yes, for [Token exchange](token-exchange.html)                                     |
| `subject_token_type`    | The type of subject token.                                                                                                | Yes, for [Token exchange](token-exchange.html)                                     |
| `username`              | A string holding the resource owner username for the [Resource owner password credentials grant](oauth2-ropc-grant.html). | Yes, when `grant_type=password`                                                    |

## Responses

| HTTP status       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `200 OK`          | Success. The response body contains a JSON object with the issued tokens, including, `access_token`, `token_type`, `expires_in`, and optionally `refresh_token` and `id_token`. For example:```json
{
  "access_token": "access-token",
  "token_type": "Bearer",
  "expires_in": 3600,
  "refresh_token": "refresh-token",
  "scope": "read write",
  "id_token": "id-token"
}
```                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `400 Bad Request` | * The request is malformed or contains an unsupported or invalid parameter value. For example:

  ```json
  {
    "error": "invalid_request",
    "error_description": "Invalid Content Type"
  }
  ```

* The request is missing a required parameter. For example:

  ```json
  {
    "error": "invalid_request",
    "error_description": "Missing parameters: grant_type code redirect_uri"
  }
  ```

* Invalid/unauthorized client. For example:

  ```json
  {
    "error": "unauthorized_client",
    "error_description": "Public clients can't use client credentials grant."
  }
  ```

* Invalid grant (authorization code / password / refresh token problems). For example:

  ```json
  {
    "error": "invalid_grant",
    "error_description": "The provided access grant is invalid, expired, or revoked."
  }
  ``` |

---

---
title: /oauth2/authorize
description: Use the OAuth 2.0 authorization endpoint to gather resource owner consent and authorization for authorization code, PKCE, PAR, and implicit grant flows
component: pingam
version: 8.1
page_id: pingam:am-oauth2:oauth2-authorize-endpoint
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oauth2/oauth2-authorize-endpoint.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "Endpoints", "Authorization", "REST API"]
page_aliases: ["oauth2-guide:oauth2-authorize-endpoint.adoc"]
section_ids:
  request_parameters: Request parameters
  responses: Responses
---

# /oauth2/authorize

The `/oauth2/authorize` endpoint is the OAuth 2.0 authorization endpoint defined in [RFC 6749](https://www.rfc-editor.org/info/rfc6749).

Use this endpoint to gather consent and authorization from the resource owner for the following flows:

* Authorization code grant ([OAuth 2.0 and OIDC](oauth2-authz-grant.html))

* Authorization code grant with PKCE ([OAuth 2.0 and OIDC](oauth2-authz-grant-pkce.html))

* Authorization code grant with PAR ([OAuth 2.0](oauth2-authz-grant-par.html))

* Implicit grant ([OAuth 2.0 and OIDC](oauth2-implicit-grant.html))

Specify the realm in the request URL; for example:

```none
https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/authorize
```

## Request parameters

The authorization endpoint supports the following parameters:

| Parameter               | Description                                                                                                                                                         | Required                                                                                             |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `acr_values`            | The OpenID Connect authentication context class reference values.                                                                                                   | Yes, if [required by the OpenID Connect provider](../am-oidc1/oidc-authentication-requirements.html) |
| `authorization_details` | Additional fine-grained authorization requirements, as specified in [RFC 9396: OAuth 2.0 Rich Authorization Requests](https://www.rfc-editor.org/rfc/rfc9396.html). | No. Accepted only if [remote consent](oauth2-remote-consent.html) is configured.                     |
| `claims`                | The user attributes to be returned in the ID token.                                                                                                                 | No                                                                                                   |
| `client_id`             | Uniquely identifies the application making the request.                                                                                                             | Yes                                                                                                  |
| `code_challenge`        | The code verifier generated for the PKCE flow.                                                                                                                      | Yes, for the [Authorization code grant with PKCE](oauth2-authz-grant-pkce.html) flow                 |
| `code_challenge_method` | The method to derive the code challenge.                                                                                                                            | Yes, when the `code_challenge` is hashed (recommended)                                               |
| `csrf`                  | The SSO token string linking the request to the user session to protect against Cross-Site Request Forgery attacks.                                                 | Yes, when gathering consent without a remote consent service                                         |
| `decision`              | Specifies whether the resource owner consents to the requested access.                                                                                              | Yes, when gathering consent unless consent is already saved for the scope                            |
| `id_token_hint`         | Previously issued ID token passed as a hint about the end user's session with the client.                                                                           | No                                                                                                   |
| `login_hint`            | String value that can be set to the ID the user uses to log in.                                                                                                     | No                                                                                                   |
| `nonce`                 | String value that associates the client session with the ID token.                                                                                                  | Yes, for the [Implicit grant](oauth2-implicit-grant.html) flow for OIDC                              |
| `prompt`                | Specifies whether to prompt the end user for authentication and consent.                                                                                            | No                                                                                                   |
| `redirect_uri`          | The URI to return the resource owner to after authorization is complete.                                                                                            | No                                                                                                   |
| `response_mode`         | Specifies the mechanism for returning response parameters.                                                                                                          | No                                                                                                   |
| `response_type`         | The type of response expected from the authorization server.                                                                                                        | Yes                                                                                                  |
| `request`               | The JWT request object.                                                                                                                                             | Yes, for JAR request and OIDC flows requiring a request object and providing no `request_uri`        |
| `request_uri`           | For PAR or OIDC flows, a reference to JWT request object(s).                                                                                                        | Yes, for JAR request and OIDC flows requiring a request object and providing no `request`            |
| `save_consent`          | Specifies whether to store a resource owner's consented scopes.                                                                                                     | No                                                                                                   |
| `scope`                 | The scopes linked to the permissions requested by the client from the resource owner.                                                                               | No                                                                                                   |
| `service`               | The authentication journey to use when authenticating the resource owner.                                                                                           | No                                                                                                   |
| `state`                 | The value to maintain state between the request and the callback.                                                                                                   | No, but strongly recommended                                                                         |
| `ui_locales`            | The end user's preferred languages for the user interface.                                                                                                          | No                                                                                                   |

## Responses

| HTTP status        | Description                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `302 Found`        | Success. AM redirects the resource owner's browser to the `redirect_uri`, appending the authorization code (or token, for the implicit grant) and any `state` value as query parameters.                                                                                                                                                                                       |
| `400 Bad Request`  | The request is malformed. For example, a required parameter is missing or an unsupported value is supplied.                                                                                                                                                                                                                                                                    |
| `401 Unauthorized` | AM could not authenticate the resource owner or the client.	When an error occurs at the authorization endpoint, AM returns 401 rather than redirecting to the client's redirect\_uri with an error parameter as described in RFC 6749. This behavior is intentional and provides additional security by not disclosing error details to potentially unvalidated redirect URIs. |

---

---
title: /oauth2/bc-authorize
description: Use the backchannel authorization endpoint to initiate OpenID Connect Client Initiated Backchannel Authentication Flow with resource owners
component: pingam
version: 8.1
page_id: pingam:am-oauth2:oauth2-bc-authorize-endpoint
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oauth2/oauth2-bc-authorize-endpoint.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "Endpoints", "Authorization", "REST API"]
page_aliases: ["oauth2-guide:oauth2-bc-authorize-endpoint.adoc"]
section_ids:
  request_parameters: Request parameters
  responses: Responses
---

# /oauth2/bc-authorize

The `/oauth2/bc-authorize` endpoint is the backchannel authorization endpoint for [OpenID Connect Client Initiated Backchannel Authentication Flow](https://openid.net/specs/openid-client-initiated-backchannel-authentication-core-1_0.html).

Use this endpoint to initiate backchannel authorization with the resource owner with the following flow:

* Backchannel request grant ([OpenID Connect](../am-oidc1/openid-connect-backchannel-request-flow.html))

Specify the realm in the request URL; for example:

```none
https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/bc-authorize
```

## Request parameters

The endpoint supports the following parameters:

| Parameter               | Description                                                                                                      | Required                                                                           |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `client_assertion`(1)   | A signed JSON Web Token (JWT) to use as client credentials.                                                      | Yes, for [JWT profile](client-auth-jwt.html) authentication                        |
| `client_assertion_type` | The type of assertion, `client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer`. | Yes, for [JWT profile](client-auth-jwt.html) authentication                        |
| `client_id`             | Uniquely identifies the application making the request.                                                          | Yes                                                                                |
| `client_secret`         | The password for a confidential client.                                                                          | Yes, when authenticating with [Form parameters (HTTP POST)](client-auth-form.html) |

(1) The endpoint requires a signed JWT with these claims:

| Claim             | Description                                                                                                                                                                                                                                    | Example                                                                                         |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `acr_values`      | A string identifying the mechanism for the end user to provide authorization.                                                                                                                                                                  | `"acr_values": "push"`                                                                          |
| `aud`             | A string or array of strings indicating the intended audience of the JWT. Must include the authorization server OAuth 2.0 endpoint.                                                                                                            | `"aud": "https://am.example.com:8443/am/oauth2"`                                                |
| `binding_message` | A short (100 character max.) string message to display to the user when obtaining authorization.For push notification, messages must:- Begin with a letter, number, or punctuation mark.

- **Not** include line breaks or control characters. | `"binding_message": "Allow ExampleBank to transfer £50 from 'Main' to 'Savings'? (EB-0246326)"` |
| `exp`             | The expiration time in seconds since January 1, 1970 UTC. An expiration time more than 30 minutes in the future causes a `JWT expiration time is unreasonable` error message.                                                                  | `"exp": 1675681183`                                                                             |
| `id_token_hint`   | An ID token identifying the principal and subject of the JWT (the end user).Required when not using `login_hint`.                                                                                                                              | `"id_token_hint": "<id-token>"`                                                                 |
| `iss`             | The unique identifier of the JWT issuer; must match the client ID in the application profile.                                                                                                                                                  | `"iss": "myCIBAClient"`                                                                         |
| `login_hint`      | A string identifying the principal and subject of the JWT (the end user).Required when not using `id_token_hint`.                                                                                                                              | `"login_hint": "a0325ea4-9d9b-4056-931b-ab64704cc3da"`                                          |
| `scope`           | A string holding a space-separated list of the requested scopes; must include `openid`.                                                                                                                                                        | `"scope": "openid profile"`                                                                     |

## Responses

| HTTP status | Description                                                                                                                                                                                                                                                                                                                                               |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `200 OK`    | Success. The response body contains a JSON object with `auth_req_id` (the backchannel authentication request identifier), `expires_in`, and optionally `interval`. For example:```json
{
  "auth_req_id": "auth-req-id",
  "expires_in": 600,
  "interval": 2
}
```                                                                                       |
| `4xx`       | Standard OAuth 2.0 error JSON object including `error` (typically `invalid_request`, `invalid_client`, and so on) and `error_description` (human-readable explanation of what failed). For example:```json
{
  "error": "invalid_request",
  "error_description": "Request must have a 'request' parameter the value of which must be a signed jwt"
}
``` |

---

---
title: /oauth2/device/code
description: Get device codes and information required to obtain resource owner consent for device access using the OAuth 2.0 Device Authorization Grant flow
component: pingam
version: 8.1
page_id: pingam:am-oauth2:rest-api-oauth2-device-code
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oauth2/rest-api-oauth2-device-code.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "API Explorer", "Endpoints"]
page_aliases: ["oauth2-guide:rest-api-oauth2-device-code.adoc"]
---

# /oauth2/device/code

The [Device authorization grant](oauth2-device-flow.html) endpoint defined in RFC 8628 [OAuth 2.0 Device Authorization Grant](https://www.rfc-editor.org/info/rfc8628).

Client devices use this endpoint in the following OAuth 2.0 flows to get the codes and information required to obtain the resource owner's consent for device access:

* [Device authorization grant](oauth2-device-flow.html)

* [Device authorization grant with PKCE](oauth2-device-flow-pkce.html)

Specify the realm in the request URL; for example:

```none
https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/device/code
```

The device code endpoint supports the following parameters:

| Parameter               | Description                                                                           | Required                                                                                             |
| ----------------------- | ------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `acr_values`            | The OpenID Connect authentication context class reference values.                     | Yes, if [required by the OpenID Connect provider](../am-oidc1/oidc-authentication-requirements.html) |
| `claims`                | The user attributes to be returned in the ID token.                                   | No                                                                                                   |
| `client_id`             | Uniquely identifies the application making the request.                               | Yes                                                                                                  |
| `code_challenge`        | The code verifier generated for the PKCE flow.                                        | Yes, for the [Authorization code grant with PKCE](oauth2-authz-grant-pkce.html) flow                 |
| `code_challenge_method` | The method to derive the code challenge.                                              | Yes, when the `code_challenge` is hashed (recommended)                                               |
| `login_hint`            | String value that can be set to the ID the user uses to log in.                       | No                                                                                                   |
| `nonce`                 | String value that associates the client session with the ID token.                    | No                                                                                                   |
| `prompt`                | Specifies whether to prompt the end user for authentication and consent.              | No                                                                                                   |
| `scope`                 | The scopes linked to the permissions requested by the client from the resource owner. | No                                                                                                   |
| `state`                 | The value to maintain state between the request and the callback.                     | No, but strongly recommended                                                                         |
| `ui_locales`            | The end user's preferred languages for the user interface.                            | No                                                                                                   |

---

---
title: /oauth2/device/user
description: Device user endpoint for confirming resource owner consent in OAuth 2.0 device flow and device flow with PKCE authorization flows
component: pingam
version: 8.1
page_id: pingam:am-oauth2:rest-api-oauth2-device-user
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oauth2/rest-api-oauth2-device-user.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "API Explorer", "Endpoints", "PKCE"]
page_aliases: ["oauth2-guide:rest-api-oauth2-device-user.adoc"]
---

# /oauth2/device/user

This is the [Device authorization grant](oauth2-device-flow.html) endpoint for user interaction. Client devices use this endpoint to confirm the resource owner's consent in the following flows:

* [Device authorization grant](oauth2-device-flow.html)

* [Device authorization grant with PKCE](oauth2-device-flow-pkce.html)

Specify the realm in the request URL; for example:

```none
https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/device/user
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
description: Retrieve details about an OAuth 2.0 token, including approved scopes, user authorization, expiry time, and proof-of-possession keys
component: pingam
version: 8.1
page_id: pingam:am-oauth2:oauth2-introspect-endpoint
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oauth2/oauth2-introspect-endpoint.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "Endpoints", "Scope", "JWT", "Grant Flow", "REST API"]
page_aliases: ["varlist-oauth2-introspect-endpoint.adoc", "oauth2-guide:oauth2-introspect-endpoint.adoc"]
section_ids:
  example: Example
  introspection_requirements: Introspection requirements
  special_tokens: Special tokens
  response_signing_and_encryption: Response signing and encryption
  rfc-9701-token-introspection-claim: RFC 9701 token_introspection claim
  response_content: Response content
---

# /oauth2/introspect

The `/oauth2/introspect` endpoint, defined in RFC 7662 [OAuth 2.0 Token Introspection](https://www.rfc-editor.org/info/rfc7662), lets a client (including resource servers) retrieve details about a token. These details include:

* The approved scopes

* The user who authorized the client to obtain the token

* The expiry time

* The proof-of-possession JSON Web Key (JWK)

The client making the request must authenticate to this endpoint.

Specify the realm in the request URL. For example:

```none
https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/introspect
```

The default settings for this endpoint don't allow:

* HTTP GET requests

* Use of `token` as a query parameter

To change this behavior for compatibility, use the `org.forgerock.openam.introspect.token.query.param.allowed` advanced server property.

The token introspection endpoint supports the following parameters:

| Parameter               | Description                                                                                                                   | Required                                                                           |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `client_assertion`      | A signed JSON Web Token (JWT) to use as client credentials.                                                                   | Yes, for [JWT profile](client-auth-jwt.html) authentication                        |
| `client_assertion_type` | The type of assertion, `client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer`.              | Yes, for [JWT profile](client-auth-jwt.html) authentication                        |
| `client_id`             | Uniquely identifies the application making the request.                                                                       | Yes                                                                                |
| `client_secret`         | The password for a confidential client.                                                                                       | Yes, when authenticating with [Form parameters (HTTP POST)](client-auth-form.html) |
| `token`                 | The token to introspect.                                                                                                      | Yes                                                                                |
| `token_type_hint`       | A hint about the type of token to introspect. Valid values are `access_token`, `refresh_token`, and `requesting_party_token`. | No                                                                                 |

## Example

The following example demonstrates token introspection:

```bash
$ curl \
--request POST \
--user "myClient:mySecret" \
--data "token=<access-token>" \
"https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/introspect"
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
  "iss": "https://am.example.com:8443/am/oauth2/realms/root/realms/alpha",
  "auth_level": 0,
  "authGrantId": "sReMmkL05mN4xtDMQdVrpjXB_go",
  "auditTrackingId": "1d7a3317-03a9-4461-9d12-745f886019c2-5860187",
  "expires_in": 3575
}
```

## Introspection requirements

A client can only introspect a token if it meets one of the following requirements:

* The client has a special scope

  The client has a [special introspection scope](oauth2-scopes.html#special-oauth2-scopes) (`am-introspect-all-tokens` or `am-introspect-all-tokens-any-realm`) specified in its client profile.

* Token was issued to the client (server-side tokens)

  For server-side tokens, AM compares the issuing client identity stored in the token against the `client_id` of the introspecting client. If they match, the client can introspect the token.

* Token audience includes the client

  When the `Allow audience members to introspect tokens` setting is enabled on the OAuth 2.0 Provider, AM checks if the `client_id` of the introspecting client is present anywhere in the token's `aud` (audience) claim. If there's a match, the client can introspect the token.

  By default, the `aud` claim contains the requesting client ID for client-side tokens and might be absent for server-side tokens. Token exchange can add audience values when `Accept Audience Parameters in Token Exchange Requests` is enabled and the requested values are allowed.

* The `client_id` claim matches (client-side tokens only)

  When the `Include client_id claim in stateless access tokens` setting is enabled, AM checks whether the `client_id` JWT claim in the token matches the `client_id` of the introspecting client. If there's a match, the client can introspect the token.

### Special tokens

* To introspect macaroon access tokens containing third-party caveats, use the `X-Discharge-Macaroon` header to pass the discharge macaroon.

* To introspect UMA RPT tokens, use the PAT of the resource owner in an `authorization: Bearer` header to authenticate to the endpoint.

## Response signing and encryption

The default introspection response is a plain JSON object.

AM also supports signed JWT (JSON Web Token) or signed and encrypted JWT introspection responses, as defined in [RFC 9701: JWT Response for OAuth Token Introspection](https://www.rfc-editor.org/info/rfc9701).

Regardless of the configured response format, a client can request a signed JWT response by adding one of the following headers to the introspection request:

* `Accept:application/jwt` (default, for compatibility with older clients)

* `Accept: application/token-introspection+jwt` (for compatibility with [RFC 9701](#rfc-9701-token-introspection-claim))

To enable signing and encryption for all requests to a client, follow these steps:

1. In the AM admin UI, go to Realms > *realm name* > Applications > OAuth 2.0 > *client ID* > Advanced and select the response type in the Token introspection response format list.

2. If you need to configure signing and encryption algorithms, set the following properties:

   * Token introspection response signing algorithm

     Default: `RS256`

   * Token introspection response encryption algorithm

     Default: `RSA-OAEP-256`

   * Token introspection encrypted response encryption algorithm

     Default: `A128CBC-HS256`

3. Save your work.

Requests for plain JSON now return errors.

## RFC 9701 token\_introspection claim

By default, AM returns a flat JWT introspection response for backwards compatibility with older clients. To comply with RFC 9701, enable the Use token\_introspection claim for JWT setting.

To enable the `token_introspection` claim, you can configure it at two levels:

* **Realm level**:

  1. In the AM admin UI, go to Realms > *realm name* > Services > OAuth2 Provider > Advanced.

  2. Select Use token\_introspection claim for JWT.

* **Client level**:

  1. In the AM admin UI, go to Realms > *realm name* > Applications > OAuth 2.0 > *client ID* > OAuth2 Provider Overrides.

  2. Enable OAuth2 Provider Overrides and select Use token\_introspection claim for JWT.

  * When enabled

    AM wraps the introspected token's claims inside a `token_introspection` claim in the JWT. This separates the JWT's own top-level claims (such as `iss`, `aud`, and `iat` for the introspection response itself) from the introspected token's claims:

    ```json
    {
      "iss": "<authorization-server-issuer>",
      "aud": "<resource-server-client-id>",
      "iat": 1234567890,
      "token_introspection": {
        "active": true,
        "scope": "profile",
        "client_id": "myClient",
        "aud": ["myClient", "api.example.com"],
        "sub": "a0325ea4-9d9b-4056-931b-ab64704cc3da",
        "exp": 1675703376
      }
    }
    ```

    The `aud` claim of the introspected token is always included in the JWT response, including for client-side tokens. The JSON introspection response also includes the `aud` claim of the introspected token, if present.

  * When not enabled

    AM returns a flat JWT structure. The `aud` claim is omitted from the JWT response and the JSON response for client-side tokens.

|   |                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This setting isn't enabled by default to preserve existing behavior after upgrades. Enable it for new deployments or when your resource servers are ready to consume RFC 9701-compliant responses. |

## Response content

The following table describes fields you may find in the introspection response:

| Field         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `active`      | Whether the token is active (`true`) or not (`false`).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `aud`         | The audience of the token. In a JWT response, the top-level `aud` identifies the audience of the introspection response itself, whereas `token_introspection.aud` is the audience claim from the token being introspected.                                                                                                                                                                                                                                                                                                                                                                              |
| `auth_level`  | The AM authentication level for the resource owner who granted access to the token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `client_id`   | The client the token was issued to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `cnf`         | The confirmation key claim.The `jwk` type contains the decoded JWK for the access token in the [JWK-based proof-of-possession](oauth2-PoP-JWK.html) flow.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `exp`         | Expiration time in seconds since January 1, 1970 UTC.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `expires_in`  | Expiration time in seconds from now; the value decreases with every request to AM.Unlike the calculated value, the expiration time stored in the token does not change.For client-side tokens, AM only returns this to a client in the same realm as the resource owner.                                                                                                                                                                                                                                                                                                                                |
| `iss`         | The token issuer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `macaroon`    | The macaroon the token validates, including any caveats.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `permissions` | (UMA only) An array containing the following:- RPT token expiration time (`exp`)

- Resource scopes of the token

- Resource ID                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `scope`       | The space-separated list of the scopes associated with the token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `sub`         | The subject of the access token.The subject claim is in the format `(type!subject)`, where:- `subject` is the identifier of the user/identity, or the name of the OAuth 2.0/OpenID Connect client that is the subject of the token.

- `type` can be one of the following:

  * `age`. Indicates the *subject* is an OAuth 2.0/OpenID Connect-related user-agent or client. For example, an OAuth 2.0 client, a Remote Consent Service agent, and a Web and Java Agent internal client.

  * `usr`. Indicates the *subject* is a user/identity.For example, `(usr!bjensen)`, or `(age!myOAuth2Client)`. |
| `token_type`  | The type of token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `user_id`     | Deprecated form of `username`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `username`    | The user who authorized the client to obtain the token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

---

---
title: /oauth2/par
description: Submit OAuth 2.0 pushed authorization requests to the authorization server for code grant, code grant with PKCE, and implicit flows
component: pingam
version: 8.1
page_id: pingam:am-oauth2:oauth2-par-endpoint
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oauth2/oauth2-par-endpoint.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "OpenID Connect (OIDC)", "PAR", "Authorization", "Endpoints"]
page_aliases: ["oauth2-guide:oauth2-par-endpoint.adoc"]
section_ids:
  request_parameters: Request parameters
  responses: Responses
---

# /oauth2/par

The `/oauth2/par` endpoint is the OAuth 2.0 pushed authorization request (PAR) endpoint defined in [RFC 9126](https://www.rfc-editor.org/info/rfc9126).

Use this endpoint to push an authorization request payload directly to the authorization server for the following flows:

* Authorization code grant ([OAuth 2.0 and OIDC](oauth2-authz-grant.html))

* Authorization code grant with PKCE ([OAuth 2.0 and OIDC](oauth2-authz-grant-pkce.html))

* Implicit grant ([OAuth 2.0 and OIDC](oauth2-implicit-grant.html))

Specify the realm in the request URL; for example:

```none
https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/par
```

## Request parameters

The PAR endpoint supports the following parameters:

| Parameter               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Required                                                                                                                            |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `acr_values`            | The OpenID Connect authentication context class reference values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Yes, if [required by the OpenID Connect provider](../am-oidc1/oidc-authentication-requirements.html)                                |
| `authorization_details` | Additional fine-grained authorization requirements, as specified in [RFC 9396: OAuth 2.0 Rich Authorization Requests](https://www.rfc-editor.org/rfc/rfc9396.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | No. Accepted only if [remote consent](oauth2-remote-consent.html) is configured.                                                    |
| `claims`                | The user attributes to be returned in the ID token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | No                                                                                                                                  |
| `client_assertion`      | A signed JSON Web Token (JWT) to use as client credentials.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Yes, for [JWT profile](client-auth-jwt.html) authentication                                                                         |
| `client_assertion_type` | The type of assertion, `client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Yes, for [JWT profile](client-auth-jwt.html) authentication                                                                         |
| `client_id`             | Uniquely identifies the application making the request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Yes, even when it is also included in a `request` object                                                                            |
| `client_secret`         | The password for a confidential client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Yes, when authenticating with [Form parameters (HTTP POST)](client-auth-form.html)                                                  |
| `code_challenge`        | The code verifier generated for the PKCE flow.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Yes, for confidential clients and for all clients using the [Authorization code grant with PKCE](oauth2-authz-grant-pkce.html) flow |
| `code_challenge_method` | The method to derive the code challenge.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Yes, when the `code_challenge` is hashed (recommended)                                                                              |
| `csrf`                  | The SSO token string linking the request to the user session to protect against Cross-Site Request Forgery attacks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Yes, when gathering consent without a remote consent service                                                                        |
| `decision`              | Specifies whether the resource owner consents to the requested access.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Yes, when gathering consent unless consent is already saved for the scope                                                           |
| `id_token_hint`         | Previously issued ID token previously passed as a hint about the end user's session with the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | No                                                                                                                                  |
| `login_hint`            | String value that can be set to the ID the user uses to log in.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | No                                                                                                                                  |
| `nonce`                 | String value that associates the client session with the ID token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | No                                                                                                                                  |
| `prompt`                | Specifies whether to prompt the end user for authentication and consent.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | No                                                                                                                                  |
| `redirect_uri`          | The URI to return the resource owner to after authorization is complete.The value must match a redirect URI pre-registered for the client. AM doesn't currently support per-request unregistered redirect URIs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | No                                                                                                                                  |
| `request`               | A signed and encrypted JWT that contains the request parameters used for [JWT-Secured Authorization Requests (JAR)](https://www.rfc-editor.org/info/rfc9101).When using JAR, the request JWT must be signed with the client's private key and optionally encrypted with the authorization server's public key. You can obtain the authorization server's public key from its JWKS URI.All request parameters must be included as claims inside the JWT. Only the following client authentication parameters can be used alongside the `request` parameter:- `client_assertion`

- `client_assertion_type`

- `client_id`

- `client_secret`Otherwise, the response is an `Invalid parameter scope` error. | No                                                                                                                                  |
| `response_mode`         | Specifies the mechanism for returning response parameters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | No                                                                                                                                  |
| `response_type`         | The type of response expected from the authorization server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Yes                                                                                                                                 |
| `save_consent`          | Specifies whether to store a resource owner's consented scopes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | No                                                                                                                                  |
| `scope`                 | The scopes linked to the permissions requested by the client from the resource owner.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | No                                                                                                                                  |
| `service`               | The authentication journey to use when authenticating the resource owner.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | No                                                                                                                                  |
| `state`                 | The value to maintain state between the request and the callback.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | No, but strongly recommended                                                                                                        |
| `ui_locales`            | The end user's preferred languages for the user interface.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | No                                                                                                                                  |

## Responses

| HTTP status   | Description                                                                                                                                                                                                                                                                                                                                               |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `201 Created` | Success. The response body contains a JSON object with a `request_uri` (for use in a subsequent authorization request) and `expires_in`. For example:```json
{
  "request_uri": "C2c3yhu2IApAELttmZtfPNPQaIJxvTCHk",
  "expires_in": 90
}
```                                                                                                             |
| `4xx`         | Standard OAuth 2.0 error JSON object including `error` (typically `invalid_request`, `invalid_client`, and so on) and `error_description` (human-readable explanation of what failed). For example:```json
{
  "error": "invalid_request",
  "error_description": "Request must have a 'request' parameter the value of which must be a signed jwt"
}
``` |

---

---
title: /oauth2/token/revoke
description: Use the OAuth 2.0 token revocation endpoint to revoke access tokens and refresh tokens according to RFC 7009
component: pingam
version: 8.1
page_id: pingam:am-oauth2:oauth2-token-revoke-endpoint
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oauth2/oauth2-token-revoke-endpoint.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "Scopes", "Grant Flow", "Endpoints", "Setup &amp; Configuration"]
page_aliases: ["varlist-oauth2-token-revoke-endpoint.adoc", "oauth2-guide:oauth2-token-revoke-endpoint.adoc"]
section_ids:
  request_parameters: Request parameters
  responses: Responses
---

# /oauth2/token/revoke

Endpoint defined in RFC 7009 [Token Revocation](https://www.rfc-editor.org/info/rfc7009) to revoke access tokens and refresh tokens.

When you revoke a refresh token, you revoke all tokens issued with the same authorization grant. If you obtained multiple access tokens for a single user with different authorization grants, you must revoke the tokens separately to invalidate each one.

Specify the realm in the request URL; for example:

```none
https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/token/revoke
```

## Request parameters

The revoke token endpoint supports the following parameters:

| Parameter               | Description                                                                                                      | Required                                                                           |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `client_assertion`      | A signed JSON Web Token (JWT) to use as client credentials.                                                      | Yes, for [JWT profile](client-auth-jwt.html) authentication                        |
| `client_assertion_type` | The type of assertion, `client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer`. | Yes, for [JWT profile](client-auth-jwt.html) authentication                        |
| `client_id`             | Uniquely identifies the application making the request.                                                          | Yes                                                                                |
| `client_secret`         | The password for a confidential client.                                                                          | Yes, when authenticating with [Form parameters (HTTP POST)](client-auth-form.html) |
| `token`                 | The access token or refresh token to revoke.                                                                     | Yes                                                                                |
| `token_type_hint`       | A hint about the type of token to revoke. Valid values are `access_token` and `refresh_token`.                   | No                                                                                 |

The following example revokes a refresh token:

```bash
$ curl \
--request POST \
--user "myClient:mySecret" \
--data "client_id=myClient" \
--data "token=<refresh-token>" \
"https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/token/revoke"
{}
```

## Responses

| HTTP status | Description                                                                                                                                                                                                                                                                         |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `200 OK`    | Success. The response body is an empty JSON object (`{}`).                                                                                                                                                                                                                          |
| `400`       | Missing or invalid client authentication:```json
{
    "error_description":"Client authentication failed",
    "error":"invalid_client"
}
```Malformed request or bad request parameters:```json
{
    "error_description":"error-description",
    "error":"invalid_request"
}
``` |
| `500`       | Server-side failure:```json
{
    "error": "server_error",
    "error_description": "Failed to revoke access token"
}
```                                                                                                                                                           |

---

---
title: /realm-config/agents/OAuth2Client
description: Use the OAuth2Client endpoint to create, list, and delete OAuth 2.0 clients, including scalable clients for managing large numbers without performance impact
component: pingam
version: 8.1
page_id: pingam:am-oauth2:rest-api-oauth2-client-admin-endpoint
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oauth2/rest-api-oauth2-client-admin-endpoint.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "API Explorer", "Endpoints", "Clients"]
page_aliases: ["oauth2-guide:rest-api-oauth2-client-admin-endpoint.adoc"]
section_ids:
  create_an_oauth_2_0_client: Create an OAuth 2.0 client
  update-oauth2-client: Update an OAuth 2.0 client
  query-oauth2-clients: Query OAuth 2.0 clients
  delete_an_oauth_2_0_client: Delete an OAuth 2.0 client
---

# /realm-config/agents/OAuth2Client

AM-specific endpoint that lets AM and agent administrators create, list, and delete OAuth 2.0 clients.

You can also use the endpoint with [scalable clients](oauth2-scalable-clients.html) to create and manage large numbers of OAuth 2.0 clients without impacting system performance.

|   |                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Use the AM API explorer for detailed information about the parameters supported by this endpoint, and to test it against your deployed AM instance.In the AM admin UI, click the Help icon, and go to API Explorer > /realm-config > /agents > /OAuth2Client. |

## Create an OAuth 2.0 client

This example registers a basic OAuth 2.0 client named `myClient` in the `alpha` realm. Provide the SSO token of an administrative user as a header, and append the name of the client to the URL.

> **Collapse: Example**
>
> ```bash
> $ curl \
> --request PUT \
> --header "Accept-API-Version: resource=1.0" \
> --header "Content-Type: application/json" \
> --header "Accept: application/json" \
> --header "iPlanetDirectoryPro: AQIC5wM…​3MTYxOA..*" \
> --data '{
>    "coreOAuth2ClientConfig":{
>       "agentgroup":"",
>       "status":{
>          "inherited":true,
>          "value":"string"
>       },
>       "userpassword":"forgerock",
>       "clientType":{
>          "inherited":false,
>          "value":"Confidential"
>       },
>       "redirectionUris":{
>          "inherited":false,
>          "value":[
>             "https://www.example.com:443/callback"
>          ]
>       },
>       "scopes":{
>          "inherited":false,
>          "value":[
>             "write",
>             "read"
>          ]
>       },
>       "defaultScopes":{
>          "inherited":true,
>          "value":[
>             "write"
>          ]
>       },
>       "clientName":{
>          "inherited":true,
>          "value":[
>             "My Test Client"
>          ]
>       }
>    },
>    "advancedOAuth2ClientConfig":{
>       "name":{
>          "inherited":false,
>          "value":[
>             null
>          ]
>       },
>       "grantTypes":{
>          "inherited":true,
>          "value":[
>             "authorization_code",
>             "client_credentials"
>          ]
>       },
>       "tokenEndpointAuthMethod":{
>          "inherited":true,
>          "value":"client_secret_basic"
>       }
>    }
> }' \
> "https://am.example.com:8443/am/json/realms/root/realms/alpha/realm-config/agents/OAuth2Client/myClient"
> {
>    "_id":"myClient",
>    "_rev":"-60716879",
>    "advancedOAuth2ClientConfig":{
>       "descriptions":{
>          "inherited":false,
>          "value":[
>
>          ]
>       },
>
> …​
>
>       "clientType":{
>          "inherited":false,
>          "value":"Confidential"
>       },
> …​
>       "_type":{
>       "_id":"OAuth2Client",
>       "name":"OAuth2 Clients",
>       "collection":true
>    }
> }
> ```

To manage a large number of clients, refer to [Scalable OAuth 2.0 clients](oauth2-scalable-clients.html).

## Update an OAuth 2.0 client

To update an existing OAuth 2.0 client, use a similar PUT request to the create request. Make sure you include *all* the attributes to be retained in the client configuration. If you omit an attribute in the JSON payload, the request effectively deletes that attribute from the client. This doesn't apply to the client secret attribute.

## Query OAuth 2.0 clients

This example lists the OAuth 2.0 clients in the `alpha` realm. Provide the SSO token of an administrative user as a header.

> **Collapse: Example**
>
> ```bash
> $ curl \
> --request GET \
> --header "Accept-API-Version: resource=1.0" \
> --header "iPlanetDirectoryPro: AQIC5wM…​3MTYxOA..*" \
> "https://am.example.com:8443/am/json/realms/root/realms/alpha/realm-config/agents/OAuth2Client?_queryFilter=true"
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

To query a large number of clients, refer to [Scalable OAuth 2.0 clients](oauth2-scalable-clients.html).

## Delete an OAuth 2.0 client

This example deletes an OAuth 2.0 client named `myClient` in the `alpha` realm. Provide the SSO token of and administrative user as a header, and append the name of the client to the URL.

> **Collapse: Example**
>
> ```bash
> $ curl \
> --request DELETE \
> --header "Accept-API-Version: resource=1.0" \
> --header "iPlanetDirectoryPro: AQIC5wM…​3MTYxOA..*" \
> "https://am.example.com:8443/am/json/realms/root/realms/alpha/realm-config/agents/OAuth2Client/myClient"
> {
>     "_id": "myClient",
>     "_rev": "-614477476",
>     ...
> }
> ```

---

---
title: /users/user/oauth2/applications
description: List OAuth 2.0 clients with active tokens for a resource owner and revoke tokens granted to applications in PingAM
component: pingam
version: 8.1
page_id: pingam:am-oauth2:rest-api-oauth2-applications-endpoint
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oauth2/rest-api-oauth2-applications-endpoint.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "API Explorer", "Endpoints", "Clients"]
page_aliases: ["oauth2-guide:rest-api-oauth2-applications-endpoint.adoc"]
section_ids:
  list_clients_with_active_tokens: List clients with active tokens
  delete_tokens_for_a_client: Delete tokens for a client
---

# /users/user/oauth2/applications

Invoke this AM-specific endpoint to list the applications granted OAuth 2.0 access and to delete tokens for a specified client. This lets you manage the tokens granted to applications on behalf of a resource owner.

For example, you can revoke all tokens for a resource owner across all clients after a password change or a suspected account compromise. To do this:

1. Query the applications endpoint to list all clients with active tokens for the resource owner.

2. Delete the tokens for each client returned.

|   |                                                                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This approach revokes all tokens held by each client for the specified resource owner. If you want to revoke a single known access token or refresh token, use the [/oauth2/token/revoke](oauth2-token-revoke-endpoint.html) endpoint instead. |

To call the endpoint, you must compose the path to the realm where the client is registered.

|   |                                                                                                                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Use the AM API explorer for detailed information about the parameters supported by this endpoint, and to test it against your deployed AM instance.In the AM admin UI, click the Help icon, and go to API Explorer > /users > /*user* > /oauth2 > /applications. |

## List clients with active tokens

This example lists all the OAuth 2.0 clients holding active tokens granted in the `alpha` realm for the resource owner, `bjensen`. You must provide the SSO token of an admin user or the resource owner as a header, and include the name of the resource owner (`bjensen`) in the URL:

```bash
$ curl \
--request GET \
--header "Accept-API-Version: resource=1.1" \
--header "iPlanetDirectoryPro: Ua6fsH2vjgHqVY…​" \
"https://am.example.com:8443/am/json/realms/root/realms/alpha/users/bjensen/oauth2/applications?_queryFilter=true"
```

On success, AM returns an HTTP 200 code and a JSON object describing each OAuth 2.0 client that currently holds at least one active access or refresh token for the specified resource owner. For example:

```json
{
    "result": [
        {
            "_id": "myClient",
            "_rev": "-1121350941",
            "name": "My client name",
            "scopes": {
                "write": "write"
            },
            "expiryDateTime": "2027-04-23T16:40:55.000Z",
            "logoUri": null
        },
        {
            "_id": "anotherClient",
            "_rev": "987654321",
            "name": "Another client name",
            "scopes": {
                "read": "read",
                "openid": "openid"
            },
            "expiryDateTime": null,
            "logoUri": null
        }
    ],
    "resultCount": 2,
    "pagedResultsCookie": null,
    "totalPagedResultsPolicy": "NONE",
    "totalPagedResults": -1,
    "remainingPagedResults": -1
}
```

**Response fields**

| Field            | Description                                                                                                                                        |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `_id`            | The client ID of the OAuth 2.0 client that holds tokens on behalf of the resource owner.                                                           |
| `name`           | The display name of the client, if configured. Returns `null` if no display name is set.                                                           |
| `scopes`         | The scopes granted to this client by the resource owner, collected across all active access and refresh tokens for this resource owner and client. |
| `expiryDateTime` | The expiry date of the longest-lived token held by this client for the resource owner. Returns `null` if the tokens have no expiry.                |
| `logoUri`        | The URI of the client's logo, if configured. Returns `null` if no logo URI is set on the client.                                                   |

## Delete tokens for a client

The following example deletes all tokens held by the OAuth 2.0 client `myClient` granted in the `alpha` realm by `bjensen`. You must provide the SSO token of an admin user or the resource owner as a header, and the username of the resource owner (`bjensen`) and the `_id` of the client (`myClient`) in the URL:

```bash
$ curl \
--request DELETE \
--header "Accept-API-Version: resource=1.1" \
--header "iPlanetDirectoryPro: Ua6fsH2vjgHqVY…​" \
"https://am.example.com:8443/am/json/realms/root/realms/alpha/users/bjensen/oauth2/applications/myClient"
```

On success, AM returns an HTTP 200 code and a JSON object with information about the deleted tokens, such as the granted scopes and ID of the client. For example:

```json
{
    "_id": "myClient",
    "_rev": "-1121350941",
    "name": null,
    "name": "My client name",
    "scopes": {
        "write": "write"
    },
    "expiryDateTime": null,
    "expiryDateTime": "2027-04-23T16:40:55.000Z",
    "logoUri": null
}
```

Repeat this request for each client `_id` returned when you queried the applications endpoint to delete all tokens for the resource owner across all clients.

---

---
title: /users/user/oauth2/resources/sets
description: Use the PingAM REST API to view and update OAuth 2.0 resources registered to a particular user in a realm
component: pingam
version: 8.1
page_id: pingam:am-oauth2:rest-api-oauth2-resourceset-endpoint
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oauth2/rest-api-oauth2-resourceset-endpoint.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "API Explorer", "Endpoints"]
page_aliases: ["oauth2-guide:rest-api-oauth2-resourceset-endpoint.adoc"]
---

# /users/user/oauth2/resources/sets

AM-specific endpoint for viewing and updating a resource registered to a particular user.

|   |                                                                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Use the AM API explorer for detailed information about the parameters supported by this endpoint, and to test it against your deployed AM instance.In the AM admin UI, click the Help icon, and go to API Explorer > /users > /*user* > /oauth2 > /resources > /sets. |

To call the endpoint, you must compose the path to the realm where the resource is registered.

This example reads an OAuth 2.0 resource and related policy in the `alpha` realm.

You must provide the SSO token of an administrative user or of the resource owner as a header, and that the name of the resource owner (`bjensen`, in this example) is part of the URL:

```bash
$ curl \
--request GET \
--header "iPlanetDirectoryPro: AQIC5wM2LY4Sfcxs…​EwNDU2NjE0*" \
"https://am.example.com:8443/am/json/realms/root/realms/alpha/users/bjensen \
/oauth2/resources/sets/43225628-4c5b-4206-b7cc-5164da81decd0"
{
    "scopes": [
         "http://photoz.example.com/dev/scopes/view",
         "http://photoz.example.com/dev/scopes/comment"
    ],
    "_id": "43225628-4c5b-4206-b7cc-5164da81decd0",
    "resourceServer": "UMA-Resource-Server",
    "name": "My Videos",
    "icon_uri": "http://www.example.com/icons/cinema.png",
    "policy": {
        "permissions": [
            {
                "subject": "user.1",
                "scopes": [
                    "http://photoz.example.com/dev/scopes/view"
                ]
            },
            {
                "subject": "user.2",
                "scopes": [
                    "http://photoz.example.com/dev/scopes/comment",
                    "http://photoz.example.com/dev/scopes/view"
                ]
            }
        ]
    },
    "type": "http://www.example.com/rsets/videos"
}
```

|   |                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------ |
|   | You can specify the fields that are returned with the `_fields` query string filter. For example, `?_fields=scopes, resourceServer, name`. |

On success, an HTTP 200 OK status code is returned, with a JSON body representing the resource. If a policy relating to the resource exists, a representation of the policy is also returned in the JSON.

If the specified resource does not exist, an HTTP 404 Not Found status code is returned, as follows:

```json
{
    "code": 404,
    "reason": "Not Found",
    "message": "No resource set with id, bad-id-3e28-4c19-8a2b-36fc24c899df0, found."
}
```

If the SSO token used is not that of the resource owner or an administrator, an HTTP 403 Forbidden status code is returned, as follows:

```json
{
    "code": 403,
    "reason": "Forbidden",
    "message": "User, user.1, not authorized."
}
```

---

---
title: Access token modification
description: Use a script to modify OAuth 2.0 access token key-value pairs, such as adding profile data or making REST calls to external services before token issuance
component: pingam
version: 8.1
page_id: pingam:am-oauth2:modifying-access-tokens-scripts
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oauth2/modifying-access-tokens-scripts.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "Customization", "Scripting", "Java", "Plugins"]
page_aliases: ["oauth2-guide:modifying-access-tokens-scripts.adoc"]
section_ids:
  about_modifying_access_tokens: About modifying access tokens
  modifying-access-tokens-scripts-prepare: Examples
  example-atm-legacy: Add profile data to access token (legacy script)
  update-profile-data: Update the user profile
  prepare-atm-legacy: Prepare the script
  configure-atm-legacy: Configure AM to use the script
  try-atm-legacy: Try the script
  example-atm-nextgen: Add external data to access token (next-generation script)
  prepare-atm-nextgen: Create the script
  configure-atm-nextgen: Configure AM to use the script
  try-atm-nextgen: Try the script
---

# Access token modification

Use this extension point to modify the key-value pairs in an OAuth 2.0 access token. For example, you could make a REST call to an external service and add or change a key-value pair in the access token based on the response before issuing the token to the OAuth 2.0 client.

* Sample scripts

  * [OAuth2 Access Token Modification Script](../am-scripting/sample-scripts.html#oauth2-access-token-modification-js) (Legacy JavaScript)

  * [OAuth2 Access Token Modification Script](../am-scripting/sample-scripts.html#oauth2-access-token-modification-groovy) (Groovy)

* Script bindings

  * [Common bindings](../am-scripting/script-bindings.html)

  * [Access token modification scripting API](../am-scripting/access-token-modification-api.html)

* Java interface

  `org.forgerock.oauth2.core.plugins.AccessTokenModifier`

  > **Collapse: Sample Java code**
  >
  > ```java
  > /*
  >  * Copyright 2021-2025 Ping Identity Corporation. All Rights Reserved
  >  *
  >  * This code is to be used exclusively in connection with Ping Identity
  >  * Corporation software or services. Ping Identity Corporation only offers
  >  * such software or services to legal entities who have entered into a
  >  * binding license agreement with Ping Identity Corporation.
  >  */
  >
  > package org.forgerock.openam.examples;
  >
  > import org.forgerock.oauth2.core.AccessToken;
  > import org.forgerock.oauth2.core.OAuth2Request;
  > import org.forgerock.oauth2.core.plugins.AccessTokenModifier;
  >
  > /**
  >  * Custom implementation of the Access Token Modifier
  >  * plugin interface {@link org.forgerock.oauth2.core.plugins.AccessTokenModifier}
  >  *
  >  * <li>
  >  * In this example the {@code modifyAccessToken} method adds an additional field to the token.
  >  * </li>
  >  *
  >  */
  > public class CustomAccessTokenModifier implements AccessTokenModifier {
  >
  >     @Override
  >     public void modifyAccessToken(AccessToken accessToken, OAuth2Request request) {
  >         //Field to always include in token
  >         accessToken.setField("additional", "field");
  >     }
  > }
  > ```

## About modifying access tokens

You can modify both [client-side](stateless-stateful-tokens.html#client-side-tokens) and [server-side](stateless-stateful-tokens.html#server-side-tokens) access tokens. Modifications are stored permanently in the issued JWT for client-side tokens or in the CTS for server-side access tokens. You can also modify [macaroons](oauth2-macaroons.html) used in place of regular tokens. In this case, you implement the plugin to modify the key pairs in the token and, optionally, to add caveats. Learn more in [MacaroonToken](../_attachments/apidocs/org/forgerock/openam/oauth2/token/macaroon/MacaroonToken.html) interface.

When issuing modified access tokens, consider the following important points:

* Removing or changing native properties could render the access token unusable.

  AM requires that certain native properties are present in the access token to consider it valid. Removing or modifying these properties could cause the OAuth 2.0 flows to break.

  |   |                                                                                                                                                                                      |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | The [AccessToken API documentation](../_attachments/apidocs/org/forgerock/oauth2/core/AccessToken.html) indicates the native properties and warns against changing or removing them. |

* Modifying access tokens affects the size of the client-side token or server-side entry.

  Changing OAuth 2.0 access tokens directly affects the size of server-side tokens or JSON web tokens (JWTs) if client-side tokens are enabled.

  Make sure the token size remains within your client or user-agent size limits.

  Learn more in [Token storage location](stateless-stateful-tokens.html).

## Examples

The following examples use a script to modify the access token.

* [Add profile data to access token (legacy script)](#example-atm-legacy)

* [Add external data to access token (next-generation script)](#example-atm-nextgen)

|   |                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Learn more about configuring AM to use an access token modification Java plugin in [Configure AM to use a Java OAuth 2.0 plugin](customizing-oauth2-scopes.html#configure-java-oauth2-plugin). |

### Add profile data to access token (legacy script)

Complete the following steps to implement a custom access token modification script to set additional properties in the access token:

1. [Update the user profile](#update-profile-data)

2. [Prepare the script](#prepare-atm-legacy)

3. [Configure AM to use the script](#configure-atm-legacy)

4. [Try the script](#try-atm-legacy)

This example uses a legacy script in Groovy.

#### Update the user profile

The script requires that the authenticated user of the access token has an email address and telephone number in their profile. The script adds the values of these fields to the access token.

1. Log in as an AM administrator, for example, `amAdmin`.

2. Add an email address and telephone number value to a test user's profile, for example, `bjensen`.

   1. Select Realms > *realm name* > Identities.

   2. On the Identities tab, select `bjensen`.

   3. In Email Address, enter a valid address. For example, `bjensen@example.com`.

   4. In Telephone Number, enter a value. For example, `44 117 496 0228`.

   5. Save your changes.

#### Prepare the script

Modify the default legacy access token modification script to set additional fields:

1. Go to Realms > *realm name* > Scripts, and click OAuth2 Access Token Modification Script.

2. In the Script field:

   * Uncomment the following line, by surrounding with a pair of `*/` and `/*` strings:

     ```groovy
     /* ... */
     accessToken.setField("hello", "world")
     /* ... */
     ```

   * Similarly, uncomment these lines:

     ```groovy
     /* ... */
     def attributes = identity.getAttributes(["mail", "telephoneNumber"].toSet())
     accessToken.setField("mail", attributes["mail"])
     accessToken.setField("phone", attributes["telephoneNumber"])
     /* ... */
     ```

     |   |                                                                                                                                                            |
     | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | Find information about the available script bindings in the [Access token modification scripting API](../am-scripting/access-token-modification-api.html). |

     |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
     | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | To include additional data in the [/oauth2/access\_token](oauth2-access_token-endpoint.html) response, edit your script to call the `addExtraData` method. For example:```groovy
     accessToken.addExtraData("hello", "world")
     ```This returns the data as part of the response body in the following way:```json
     {
       "access_token":"sbQZuveFumUDV5R1vVBl6QAGNB8",
       "hello":"world",
       "scope":"write",
       "token_type":"Bearer",
       "expires_in":3599
     }
     ``` |

3. Save your changes.

#### Configure AM to use the script

Perform this task to set up an OAuth 2.0 provider that uses the modified default access token modification script.

1. [Configure the provider](customizing-oauth2-scopes.html#configure-scripted-oauth2-plugin) and make sure the following properties are set:

   * Access Token Modification Plugin Type to `SCRIPTED`.

   * Access Token Modification Plugin Script to `OAuth2 Access Token Modification Script`.

   By default, a new OAuth 2.0 provider uses the default access token modification script.

2. Save your changes.

#### Try the script

To verify that the script modifies the access token as expected, run an OAuth 2.0 authorization code flow as follows:

1. [Create an OAuth 2.0 client](oauth2-register-client.html) with the following values:

   * **Client ID**: `myClient`

   * **Client secret**: `mySecret`

   * **Redirection URIs**: `https://www.example.com:443/callback`

   * **Scope(s)**: `access|Access to your data`

2. [Get an authorization code](oauth2-authz-grant.html#proc-auth-code-browser) using the values configured for `myClient` and the login credentials for `bjensen`.

3. [Exchange the authorization code for an access token](oauth2-authz-grant.html#proc-auth-code-token) providing the authorization code and the values for `myClient`.

4. Finally, call [/oauth2/introspect](oauth2-introspect-endpoint.html) to verify that the access token includes the modified values:

   * The resource owner's telephone number and email address.

   * A `hello:world` key-value pair.

### Add external data to access token (next-generation script)

Complete the following steps to implement a custom access token modification script to set additional properties in the access token:

1. [Create the script](#prepare-atm-nextgen)

2. [Configure AM to use the script](#configure-atm-nextgen)

3. [Try the script](#try-atm-nextgen)

This example uses a next-generation script.

#### Create the script

Write a next-generation access token modification script to manipulate profile data.

1. [Create a script](../am-scripting/manage-scripts-console.html) of type OAuth2 Access Token Modification Script. Make sure you select Next-Generation as the evaluator version and click Create.

2. In the Script field, paste the following code:

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
   // use utils binding to get random values
   var uids = [0,0,0];
   utils.crypto.getRandomValues(uids);

   // add values to be returned in the JSON response
   accessToken.addExtraJsonData('uids', uids);

   // set a shorter expiry time
   var newExpiry = Date.now() + 300000;
   accessToken.setExpiryTime(newExpiry);
   ```

   |   |                                                                                                                                                                                                                                                                                                                                                                |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can find information about the next-generation common bindings such as `httpClient` and `utils` in [Common bindings](../am-scripting/script-bindings.html).You can find information about the bindings specific to access token modification scripts in the [Access token modification scripting API](../am-scripting/access-token-modification-api.html). |

3. Save your changes.

#### Configure AM to use the script

Set up an OAuth 2.0 provider to use the custom access token modification script.

1. [Configure the provider](customizing-oauth2-scopes.html#configure-scripted-oauth2-plugin) and make sure the following properties are set:

   * Access Token Modification Plugin Type to `SCRIPTED`.

   * Access Token Modification Plugin Script to the name of your custom access token modification script.

2. Save your changes.

#### Try the script

To verify that the script modifies the access token as expected, run an OAuth 2.0 authorization code flow as follows:

1. [Create an OAuth 2.0 client](oauth2-register-client.html) with the following values:

   * **Client ID**: `myClient`

   * **Client secret**: `mySecret`

   * **Redirection URIs**: `https://www.example.com:443/callback`

   * **Scope(s)**: `access|Access to your data`

2. [Get an authorization code](oauth2-authz-grant.html#proc-auth-code-browser) using the values configured for `myClient` and the login credentials for `bjensen`.

3. [Exchange the authorization code for an access token](oauth2-authz-grant.html#proc-auth-code-token) providing the authorization code and the values for `myClient`.

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

4. Finally, call [/oauth2/introspect](oauth2-introspect-endpoint.html) to verify that the access token includes the modified values for `browser`, `ip`, and `exp`. For example:

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
           "ip": "1.240.195.84"
       }
   ```

---

---
title: AI agent acting autonomously
description: Use dynamic client registration to create an autonomous AI agent that registers itself and obtains access tokens with appropriate privilege levels
component: pingam
version: 8.1
page_id: pingam:am-oauth2:ai-agents-autonomous
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oauth2/ai-agents-autonomous.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  aiagent-autonomous-create-mayact: Create the may act script
  aiagent-autonomous-create-dcr-script: Create the DCR script
  aiagent-autonomous-configure-provider: Configure the OAuth 2.0 provider
  aiagent-autonomous-setup-agent: Register the AI agent
  aiagent-user-token-exchange-flow: The token exchange flow
  example_token_exchange: Example token exchange
---

# AI agent acting autonomously

This example describes how to use dynamic client registration (DCR) to create an autonomous AI agent.

* Use case

  An automatic software update AI agent is installed on a laptop or a server, registers itself dynamically with AM, and gets its own access token with a read-only scope to check for critical updates.

  If an update is required, the agent performs a token exchange to get an access token with greater privileges so that it can install the software.

* Prerequisites

  * [AI agents enabled](ai-agents.html#enable-ai-agents).

* Steps

  * [Create the may act script](#aiagent-autonomous-create-mayact) for the software agent to act autonomously.

  * [Create the DCR script](#aiagent-autonomous-create-dcr-script) to ensure the agent runs the may act script.

  * [Configure the OAuth 2.0 provider](#aiagent-autonomous-configure-provider) for DCR.

  * [Register the AI agent](#aiagent-autonomous-setup-agent) using DCR.

## Create the may act script

1. Create a [may act script](token-exchange-delegation.html#delegation-script) named `Software agent may act script` that adds the software agent to the `may_act` claim in the subject token:

   * Next-generation

   * Legacy

   ```javascript
   (function () {
       var mayAct = {
           client_id: clientProperties.clientId,
           sub: `(age!${clientProperties.clientId})`
     };
       token.setMayAct(mayAct);
   }());
   ```

   ```javascript
   (function () {
       var frJava = JavaImporter(
           org.forgerock.json.JsonValue);

       var mayAct = frJava.JsonValue.json(frJava.JsonValue.object());
       // the client ID that can exchange the token
       mayAct.put('client_id', clientProperties.clientId);
       // the subject of the token that can exchange the token
       mayAct.put('sub', '(age!' + clientProperties.clientId + ')');
       token.setMayAct(mayAct);
   }());
   ```

   `age`: Stands for agent. It tells the system that the identity following the exclamation mark is an automated agent or a service account, rather than a human user.

2. Save your changes.

3. Make a note of the script `_id`, for example, `4478ca08-5a2a-4b1a-adee-d57c5c032d72`. When you create the DCR script, use this ID to make sure the software agent runs the may act script.

   |   |                                                                                                                       |
   | - | --------------------------------------------------------------------------------------------------------------------- |
   |   | You can find the script ID by calling the `/scripts` REST endpoint and checking the JSON output for your script name. |

## Create the DCR script

1. Create a [DCR script](../am-oidc1/dynamic-client-registration-script.html#dcr-create-script) named `Software agent DCR script` that overrides the default behavior of the OAuth 2.0 provider to set the following attributes:

   * Enable OAuth2 Provider Overrides

     *enabled*

   * OAuth2 Access Token May Act Script

     may-act-script-id

   * Use Client-Side Access & Refresh Tokens

     *enabled*

   For example:

   * Next-generation

   * Legacy

   ```javascript
   if (operation === "CREATE" && clientIdentity.isAIAgent()) {
       clientIdentity.setAttribute("providerOverridesEnabled", ["true"]);
       clientIdentity.setAttribute("accessTokenMayActScript",["4478ca08-5a2a-4b1a-adee-d57c5c032d72"]);
       clientIdentity.setAttribute("statelessTokensEnabled", ["true"]);
       clientIdentity.store();
   };
   ```

   *Not available*

2. Save your changes.

## Configure the OAuth 2.0 provider

1. Complete the steps to [enable DCR in the provider](ai-agents.html#register-ai-agents-dcr).

2. Configure the provider to use your DCR script:

   1. In the AM admin UI, go to Realms > *realm name* > Services > OAuth2 Provider > Client Dynamic Registration.

   2. Set Dynamic Client Registration Script to `Software agent DCR script`.

   3. Save your changes.

## Register the AI agent

Use the AI agent endpoint to register an agent dynamically.

1. Post a DCR request to the AI agent endpoint with the following JSON body, for example:

   ```bash
   $ curl \
   --request POST \
   --header "Content-Type: application/json" \
   --data '{
     "grant_types": ["client_credentials", "urn:ietf:params:oauth:grant-type:token-exchange"],
     "client_name": "software agent",
     "response_types": ["token"],
     "redirect_uris": ["https://www.example.com:443/callback"],
     "scopes": ["read", "write"]
   }' \
   "https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/aiagent/register"
   ```

   > **Collapse: Show the response**
   >
   > ```bash
   > {
   >   "authorization_signed_response_alg": "RS256",
   >   "request_object_encryption_alg": "",
   >   "introspection_encrypted_response_alg": "RSA-OAEP-256",
   >   "default_max_age": 0,
   >   "application_type": "web",
   >   "introspection_encrypted_response_enc": "A128CBC-HS256",
   >   "introspection_signed_response_alg": "RS256",
   >   "providerOverridesEnabled": true,
   >   "userinfo_encrypted_response_enc": "",
   >   "registration_client_uri": "https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/aiagent/register?client_id=software-agent-client_id",
   >   "client_type": "Confidential",
   >   "userinfo_encrypted_response_alg": "",
   >   "registration_access_token": "nAn6REdGvAthrKK6EhMo_eT2Rzw",
   >   "token_endpoint_auth_method": "client_secret_basic",
   >   "userinfo_signed_response_alg": "",
   >   "client_id": "software-agent-client_id",
   >   "enableApplicationContext": false,
   >   "public_key_selector": "x509",
   >   "scope": "read write",
   >   "require_pushed_authorization_requests": false,
   >   "authorization_code_lifetime": 0,
   >   "client_secret": "software-agent-client_secret",
   >   "user_info_response_format_selector": "JSON",
   >   "tls_client_certificate_bound_access_tokens": false,
   >   "backchannel_logout_session_required": false,
   >   "client_name": "Software Agent",
   >   "grant_types": [
   >     "client_credentials",
   >     "urn:ietf:params:oauth:grant-type:token-exchange"
   >   ],
   >   "jwt_token_lifetime": 0,
   >   "id_token_encryption_enabled": false,
   >   "redirect_uris": [
   >     "https://www.example.com:443/callback"
   >   ],
   >   "jwks_cache_miss_cache_time": 60000,
   >   "jwks_cache_timeout": 3600000,
   >   "id_token_encrypted_response_alg": "RSA-OAEP-256",
   >   "id_token_encrypted_response_enc": "A128CBC-HS256",
   >   "client_secret_expires_at": 0,
   >   "access_token_lifetime": 0,
   >   "refresh_token_lifetime": 0,
   >   "scopes": [
   >     "read",
   >     "write"
   >   ],
   >   "request_object_signing_alg": "",
   >   "response_types": [
   >     "token"
   >   ]
   > }
   > ```

   The software agent is now registered and can operate autonomously. The client ID and client secret are automatically generated.

   When the agent performs a token exchange, the may act script adds the software agent DCR client to the `may_act` claim in the subject token, allowing it to act on behalf of itself.

## The token exchange flow

![aiagent autonomous](_images/aiagent-autonomous.svg)

### Example token exchange

1. [Get an agent access token](oauth2-client-cred-grant.html) for the software agent using the client credentials flow:

   ```bash
   $ curl \
   --request POST \
   --data 'grant_type=client_credentials' \
   --data 'client_id=software-agent-client_id' \
   --data 'client_secret=software-agent-client_secret' \
   --data 'scope=read' \
   'https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/access_token'
   {
     "access_token":"software-agent-access-token",
     "scope":"read",
     "token_type":"Bearer",
     "expires_in":3599
   }
   ```

   The access token gives the software agent read access to protected resources so that it can check software versions.

2. The software agent detects that the software is out of date and needs to be updated.

   The agent performs a [token exchange](token-exchange-delegation.html) to get the increased permissions (`scope=read write`) required to run a software update:

   ```bash
   $ curl \
   --request POST \
   --data 'client_id=software-agent-client_id' \
   --data 'client_secret=software-agent-client_secret' \
   --data 'grant_type=urn:ietf:params:oauth:grant-type:token-exchange' \
   --data 'scope=read write' \
   --data 'subject_token=software-agent-access-token' \
   --data 'subject_token_type=urn:ietf:params:oauth:token-type:access_token' \
   'https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/access_token'
   {
     "access_token": "exchanged-id-token",
     "refresh_token": "new-refresh-token,"
     "issued_token_type": "urn:ietf:params:oauth:token-type:access_token",
     "scope": "read write",
     "token_type": "Bearer",
     "expires_in": 3599
   }
   ```

   The `issued_token_type` shows this is an exchanged token.

---

---
title: AI agent on behalf of a user
description: Configure an AI agent to obtain a delegation token on behalf of a user using OAuth 2.0 token exchange
component: pingam
version: 8.1
page_id: pingam:am-oauth2:ai-agents-user
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oauth2/ai-agents-user.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  aiagent-user-create-mayact: Create the may act script
  aiagent-user-oauth2client: Configure the OAuth 2.0 client
  aiagent-user-setup-agent: Register the AI agent
  the_token_exchange_flow: The token exchange flow
  example_token_exchange: Example token exchange
---

# AI agent on behalf of a user

This example describes how to configure an AI agent to get a delegation token on behalf of a user using token exchange.

* Use case

  An employee wants to use an HR digital assistant to update their health plan in a third-party HR system that's protected by AM.

* Prerequisites

  * [AI agents enabled](ai-agents.html#enable-ai-agents).

  * An employee user profile, for example, `bjensen`.

* Steps

  * [Create the may act script](#aiagent-user-create-mayact) for the HR agent to act on behalf of the employee.

  * [Configure the OAuth 2.0 client](#aiagent-user-oauth2client), for example, `hr-client`.

  * [Register the AI agent](#aiagent-user-setup-agent), for example, `hr-agent`.

## Create the may act script

1. Write a [may act script](token-exchange-delegation.html#delegation-script) that adds the AI agent, `hr-agent`, to the `may_act` claim in the subject token:

   * Next-generation

   * Legacy

   ```javascript
   (function () {
       var mayAct = {
           "client_id": "hr-agent",
           "sub": "(age!hr-agent)"
       };
       token.setMayAct(mayAct);
   }());
   ```

   ```javascript
   (function () {
       var frJava = JavaImporter(
           org.forgerock.json.JsonValue);

       var mayAct = frJava.JsonValue.json(frJava.JsonValue.object());
       // the client ID that can exchange the token
       mayAct.put('client_id', 'hr-agent');
       // the subject claim for the agent / OAuth 2.0 client application
       mayAct.put('sub', '(age!hr-agent)');
       token.setMayAct(mayAct);
   }());
   ```

2. Save your changes.

## Configure the OAuth 2.0 client

Create a client application that overrides the OAuth 2.0 provider settings. This is the client that the employee uses to log in and get an access token from.

1. In the AM admin UI, go to Realms > *realm name* > Applications > OAuth 2.0 > Clients and [register a confidential OAuth 2.0 client](oauth2-register-client.html) in the same realm as the provider and user journeys.

   Provide the following values and click Create:

   * Client ID

     `hr-client`

   * Client secret

     `mySecret`

   * Redirection URIs

     `https://www.example.com:443/callback`

   * Scope(s)

     `read` `write` `delete`

2. On the Advanced tab, verify the following settings:

   * Grant Types

     `Authorization Code`

   * Token Endpoint Authentication Method

     `client_secret_basic`

3. On the OAuth2 Provider Overrides tab, save these settings:

   * Enable OAuth2 Provider Overrides

     *enabled*

   * OAuth2 Access Token May Act Script

     may act script name

## Register the AI agent

Create an OAuth 2.0 AI agent to act as the HR agent that gets a delegation token to act on behalf of the employee.

1. In the AM admin UI, go to Realms > *realm name* > Applications > OAuth 2.0 > AI Agents and [register an AI agent](ai-agents.html#register-ai-agents-ui).

   Provide the following values and click Create:

   * Client ID

     `hr-agent`

   * Client secret

     `mySecret`

   * Redirection URIs

     `https://www.example.com:443/callback`

   * Scope(s)

     `read` `write` `delete`

## The token exchange flow

![aiagent on behalf user](_images/aiagent-on-behalf-user.svg)

### Example token exchange

1. [Authenticate](../am-authentication/authn-rest.html) as the employee, `bjensen`, for example:

   ```bash
   $ curl \
   --request POST \
   --header "X-OpenAM-Username: bjensen" \
   --header "X-OpenAM-Password: Ch4ng31t" \
   --header 'Accept-API-Version: resource=2.0, protocol=1.0' \
   'https://am.example.com:8443/am/json/realms/root/realms/alpha/authenticate'
   {
       "tokenId":"user-token",
       "successUrl":"/am/console",
       "realm":"/alpha"
   }
   ```

2. [Request an authorization code](oauth2-authorize-endpoint.html) with the user token:

   ```bash
   $ curl \
   --dump-header - \
   --request POST \
   --cookie 'iPlanetDirectoryPro=user-token' \
   --data 'scope=read' \
   --data 'response_type=code' \
   --data 'client_id=hr-client' \
   --data 'csrf=user-token' \
   --data 'redirect_uri=https://www.example.com:443/callback' \
   --data 'decision=allow' \
   'https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/authorize'
   …​
   location: https://www.example.com:443/callback?code=authorization-code&iss=https%3A%2F%2F…​
   …​
   ```

3. [Get a user access token](oauth2-access_token-endpoint.html) with the authorization code:

   ```bash
   $ curl \
   --request POST \
   --data 'grant_type=authorization_code' \
   --data 'client_id=hr-client' \
   --data 'client_secret=mySecret' \
   --data 'code=authorization-code' \
   --data 'redirect_uri=https://www.example.com:443/callback' \
   --data 'scope=read' \
   'https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/access_token'
   {
     "access_token": "user-access-token",
     "refresh_token": "refresh-token",
     "scope": "read",
     "token_type": "Bearer",
     "expires_in": 3599
   }
   ```

4. [Get an agent access token](oauth2-client-cred-grant.html) for `hr-agent` using the client credentials flow:

   ```bash
   $ curl \
   --request POST \
   --data 'grant_type=client_credentials' \
   --data 'client_id=hr-agent' \
   --data 'client_secret=mySecret' \
   --data 'scope=read' \
   'https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/access_token'
   {
     "access_token":"agent-access-token",
     "scope":"read",
     "token_type":"Bearer",
     "expires_in":3599
   }
   ```

5. [Exchange the two access tokens](token-exchange-delegation.html) to allow the HR agent to act on behalf of `bjensen`, with scopes managed by AM:

   ```bash
   $ curl \
   --request POST \
   --data 'client_id=hr-agent' \
   --data 'client_secret=mySecret' \
   --data 'grant_type=urn:ietf:params:oauth:grant-type:token-exchange' \
   --data 'scope=read write delete' \
   --data 'subject_token=user-access-token' \
   --data 'subject_token_type=urn:ietf:params:oauth:token-type:access_token' \
   --data 'actor_token=agent-access-token' \
   --data 'actor_token_type=urn:ietf:params:oauth:token-type:access_token' \
   'https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/access_token'
   {
     "access_token": "exchanged-id-token",
     "refresh_token": "new-refresh-token,"
     "issued_token_type": "urn:ietf:params:oauth:token-type:access_token",
     "scope": "read write delete",
     "token_type": "Bearer",
     "expires_in": 3599
   }
   ```

   The `issued_token_type` shows this is an exchanged token.

---

---
title: AI agent on behalf of an agent
description: Configure AI agents where both the subject and actor are machine agents, enabling one agent to act on behalf of another using token exchange and delegation
component: pingam
version: 8.1
page_id: pingam:am-oauth2:ai-agents-agent
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oauth2/ai-agents-agent.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  aiagent-agent-create-mayact: Create the may act script
  aiagent-agent-setup-subject-agent: Register the subject AI agent
  aiagent-agent-setup-actor-agent: Register the actor AI agent
  aiagent-user-token-exchange-flow: The token exchange flow
  example_token_exchange: Example token exchange
---

# AI agent on behalf of an agent

This example describes how to configure AI agents where both the subject and the actor are machine agents, not end users.

* Use case

  A risk orchestrator AI agent acts on behalf of a data-processing agent to call risk-scoring APIs, select the best result, and log an explanation.

* Prerequisites

  * [AI agents enabled](ai-agents.html#enable-ai-agents).

* Steps

  * [Create the may act script](#aiagent-agent-create-mayact) for the risk operator agent to act on behalf of the data-processing agent.

  * [Register the subject AI agent](#aiagent-agent-setup-subject-agent), for example, `data-agent`.

  * [Register the actor AI agent](#aiagent-agent-setup-actor-agent), for example, `risk-agent`.

## Create the may act script

1. Write a [may act script](token-exchange-delegation.html#delegation-script) that adds the actor AI agent, `risk-agent`, to the `may_act` claim in the subject token:

   * Next-generation

   * Legacy

   ```javascript
   (function () {
       var mayAct = {
           "client_id": "risk-agent",
           "sub": "(age!risk-agent)"
       };
       token.setMayAct(mayAct);
   }());
   ```

   ```javascript
   (function () {
       var frJava = JavaImporter(
           org.forgerock.json.JsonValue);

       var mayAct = frJava.JsonValue.json(frJava.JsonValue.object());
       // the client ID that can exchange the token
       mayAct.put('client_id', 'risk-agent');
       // the subject claim for the agent / OAuth 2.0 client application
       mayAct.put('sub', '(age!risk-agent)');
       token.setMayAct(mayAct);
   }());
   ```

2. Save your changes.

## Register the subject AI agent

Create an OAuth 2.0 AI agent to act as the data-processing agent that delegates tasks to the actor agent.

1. In the AM admin UI, go to Realms > *realm name* > Applications > OAuth 2.0 > AI Agents and [register an AI agent](ai-agents.html#register-ai-agents-ui).

   Provide the following values and click Create:

   * Client ID

     `data-agent`

   * Client secret

     `mySecret`

   * Redirection URIs

     `https://www.example.com:443/callback`

   * Scope(s)

     `read` `write` `delete`

2. On the OAuth2 Provider Overrides tab, save these settings:

   * Enable OAuth2 Provider Overrides

     *enabled*

   * OAuth2 Access Token May Act Script

     may act script name

## Register the actor AI agent

Create an OAuth 2.0 AI agent as the risk orchestrator that gets a delegation token to act on behalf of the data-processsing agent.

1. In the AM admin UI, go to Realms > *realm name* > Applications > OAuth 2.0 > AI Agents and [register an AI agent](ai-agents.html#register-ai-agents-ui).

   Provide the following values and click Create:

   * Client ID

     `risk-agent`

   * Client secret

     `mySecret`

   * Redirection URIs

     `https://www.example.com:443/callback`

   * Scope(s)

     `read` `write` `delete`

## The token exchange flow

![aiagent on behalf agent](_images/aiagent-on-behalf-agent.svg)

### Example token exchange

1. [Get an agent access token](oauth2-client-cred-grant.html) for `risk-agent` using the client credentials flow:

   ```bash
   $ curl \
   --request POST \
   --data 'grant_type=client_credentials' \
   --data 'client_id=risk-agent' \
   --data 'client_secret=mySecret' \
   --data 'scope=read' \
   'https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/access_token'
   {
     "access_token":"risk-agent-access-token",
     "scope":"read",
     "token_type":"Bearer",
     "expires_in":3599
   }
   ```

2. [Get an agent access token](oauth2-client-cred-grant.html) for `data-agent` using the client credentials flow:

   ```bash
   $ curl \
   --request POST \
   --data 'grant_type=client_credentials' \
   --data 'client_id=data-agent' \
   --data 'client_secret=mySecret' \
   --data 'scope=read' \
   'https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/access_token'
   {
     "access_token":"data-agent-access-token",
     "scope":"read",
     "token_type":"Bearer",
     "expires_in":3599
   }
   ```

3. [Exchange the two access tokens](token-exchange-delegation.html) to allow the risk-orchestrating agent to act on behalf of the data processing agent, with scopes managed by AM:

   ```bash
   $ curl \
   --request POST \
   --data 'client_id=risk-agent' \
   --data 'client_secret=mySecret' \
   --data 'grant_type=urn:ietf:params:oauth:grant-type:token-exchange' \
   --data 'scope=read' \
   --data 'subject_token=data-agent-access-token' \
   --data 'subject_token_type=urn:ietf:params:oauth:token-type:access_token' \
   --data 'actor_token=risk-agent-access-token' \
   --data 'actor_token_type=urn:ietf:params:oauth:token-type:access_token' \
   'https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/access_token'
   {
     "access_token": "exchanged-id-token",
     "refresh_token": "new-refresh-token,"
     "issued_token_type": "urn:ietf:params:oauth:token-type:access_token",
     "scope": "read write delete",
     "token_type": "Bearer",
     "expires_in": 3599
   }
   ```

   The `issued_token_type` shows this is an exchanged token.

---

---
title: AI agents
description: Enable AI agents in PingAM to register specialized OAuth 2.0 identities that securely perform delegated tasks on behalf of end users through token exchange
component: pingam
version: 8.1
page_id: pingam:am-oauth2:ai-agents
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oauth2/ai-agents.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  how_to_use_an_ai_agent: How to use an AI agent
  enable-ai-agents: Enable AI agents
  register-ai-agents-ui: Register an AI agent in the UI
  create-group-settings: Create group settings
  register-ai-agents-dcr: Register an AI agent dynamically
---

# AI agents

AI agents are specialized OAuth 2.0 identities that securely perform tasks on behalf of end users through a delegated token exchange process, ensuring distinct accountability and granular access control.

You can use AI agents to securely build [digital assistants](https://developer.pingidentity.com/identity-for-ai/glossary/idai-glossary.html#digital-assistant) that operate on behalf of end users, such as a chatbot on a retail website helping a user navigate products, or an internal workforce assistant acting on behalf of an employee to access enterprise tools like Salesforce.

* Token delegation

  Using OAuth 2.0 token exchange, an AI agent can swap an existing access token for a new, constrained, *delegation* token that encodes both the original subject and the acting agent. The AI agent can then complete tasks on behalf of a user or another agent, with scopes and audiences controlled by the authorization server.

* Common use cases

  * **Automated operations:** Use an AI agent to handle routine high-volume tasks, such as triaging tickets or provisioning access.

  * **Digital assistants:** Use AI agents to search products, manage preferences, or place orders.

## How to use an AI agent

To use an AI agent, you must first complete these steps:

* [Enable AI agents](#enable-ai-agents)

* Register the agent in one of the following ways:

  * [Manually in the UI](#register-ai-agents-ui)

  * [Dynamically over REST](#register-ai-agents-dcr).

Once registered, you can use the AI agent in delegation use cases. For example:

* [AI agent on behalf of a user](ai-agents-user.html)

* [AI agent on behalf of an agent](ai-agents-agent.html)

* [AI agent acting autonomously](ai-agents-autonomous.html)

## Enable AI agents

In AM, AI agents are switched off by default.

To enable AI agents:

1. In the AM admin UI, set the [advanced property](../setup/server-advanced.html#org.forgerock.am.oauth2.aiagents.enabled) `org.forgerock.am.oauth2.aiagents.enabled` to `true`, and save your changes.

2. Enable AI agents in the OAuth 2.0 provider.

   1. Go to Realms > *realm name* > Services.

   2. [Create an OAuth 2.0 provider service](oauth2-configure-authz.html) if one doesn't exist already.

   3. On the OAuth 2.0 provider page, select the AI Agents tab, and select Enable AI Agents.

   4. Save your changes.

   5. Refresh the UI for the changes to apply.

3. Go to Applications > OAuth 2.0 and verify that AI Agents appears as the last item in the menu.

## Register an AI agent in the UI

Use the AI agents UI to onboard an AI agent, configure its standard OAuth 2.0 properties as a specialized OAuth 2.0 client, update, or delete an agent.

To create an AI agent:

1. Go to Applications > OAuth 2.0 > AI Agents and click + Add AI Agent.

2. Provide values for Client ID, Client secret, Redirection URIs, Scope(s), and Default Scope(s), and click Create.

   The new AI agent is created with standard OAuth 2.0 client properties, with both the `Client Credentials` and `Token Exchange` grant types enabled by default.

3. Configure the AI agent properties to suit your use case and save your changes.

   Find out more about OAuth 2.0 client properties in [Client application registration](oauth2-register-client.html).

### Create group settings

You can optionally configure shared settings for AI agents by adding them to an AI agent group. They work in the same way as OAuth 2.0 client groups.

Learn about creating groups and inheriting group settings in [Shared application settings](oauth2-register-client.html#shared-application-settings).

## Register an AI agent dynamically

Use [dynamic client registration](../am-oidc1/dynamic-client-registration-script.html) (DCR) when you want to use automation or agents to onboard themselves.

1. Enable DCR in the provider:

   1. In the AM admin UI, go to Realms > *realm name* > Services > OAuth2 Provider.

   2. On the Client Dynamic Registration tab, enable Allow Open Dynamic Client Registration and save your changes.

   3. On the Advanced tab, add the scopes the agent can register in the Client Registration Scope Allowlist, for example `read write`.

   4. Save your changes.

2. *Optional*. If you require [RFC 8414](https://datatracker.ietf.org/doc/html/rfc8414) compliance, configure your webserver to map the DCR endpoint to appear under the authorization server metadata.

   For example, for an Apache Tomcat deployment:

   1. Edit the `server.xml` to add the mapping:

      `<Valve className="org.apache.catalina.valves.rewrite.RewriteValve" />` to `/Server/Service/Engine/Host`

   2. Create a file called `rewrite.config` and place it under `CATALINA_HOME/conf/Catalina/localhost/`.

   3. Add the following mapping to `rewrite.config`:

      `RewriteRule ^/\.well-known/oauth-authorization-server$ /am/oauth2/realms/root/.well-known/oauth-authorization-server/aiagent [L]`

   4. Save your changes.

   5. Restart Tomcat.

3. *Optional.* You can verify the AI agent registration URL by calling the well-known authorization server endpoint and reading the `registration_endpoint` value.

   * Example URLs

     If the rewrite rule was added:

     ```bash
     $ curl https://am.example.com:8443/.well-known/oauth-authorization-server
     {
       "…​": "…​",
       "registration_endpoint": "https://am.example.com:8443/am/oauth2/aiagent/register",
       "…​": "…​"
     }
     ```

     Without the rewrite rule:

     ```bash
     $ curl https://am.example.com:8443/am/oauth2/realms/root/.well-known/oauth-authorization-server/aiagent
     {
       "…​": "…​",
       "registration_endpoint": "https://am.example.com:8443/am/oauth2/aiagent/register",
       "…​": "…​"
     }
     ```

4. To register an agent, you can now post a [DCR request](../am-oidc1/oauth2-dynamic-client-registration.html) to the AI agent endpoint.

   Specify the same parameters as for the DCR `/register` endpoint, for example:

   ```bash
   $ curl \
   --request POST \
   --header "Content-Type: application/json" \
   --data '{
     "grant_types": ["client_credentials", "urn:ietf:params:oauth:grant-type:token-exchange"],
     "client_name": "DCR AI agent",
     "response_types": ["token"],
     "redirect_uris": ["'"https://www.example.com:443/callback"'"],
     "scopes": ["read", "write", "delete"]
   }' \
   "https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/aiagent/register"
   ```

   By default, only the `authorization_code` grant type is set for DCR clients, so you must include `urn:ietf:params:oauth:grant-type:token-exchange` if you want the agent to be able to exchange tokens.

   |   |                                                                                                                                                                                                                                                                                                             |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can use [DCR scripting](../am-oidc1/dynamic-client-registration-script.html) to run extra checks and processes after you create, update, or delete an agent.For example, for IDM integrations, verify attribute values or patch the underlying PingIDM object with custom AI agent identity attributes. |

---

---
title: AM as client and authorization server
description: Set up PingAM as both an OAuth 2.0 authorization server and client to protect resources on a resource server using a PingAM web agent
component: pingam
version: 8.1
page_id: pingam:am-oauth2:oauth2-client-plus-authz
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oauth2/oauth2-client-plus-authz.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "Endpoints", "Authorization", "Clients", "Agents", "Setup &amp; Configuration"]
page_aliases: ["oauth2-guide:oauth2-client-plus-authz.adoc"]
---

# AM as client and authorization server

You can set up AM as both an OAuth 2.0 authorization server *and* an OAuth 2.0 client to protect resources on a resource server using an AM web agent.

![This example uses an authorization server, a client, and a resource server protected with a web agent.](_images/oauth2-end-to-end-example.png)Figure 1. Authorization server, client, and resource server

This example configuration uses three servers:

| Server | Example URL                          | Role                                                                                                                  |
| ------ | ------------------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| AM1    | `https://authz.example.com:8443/am`  | OAuth 2.0 authorization server                                                                                        |
| AM2    | `https://client.example.com:8443/am` | OAuth 2.0 client, which also handles policies                                                                         |
| RS     | `https://www.example.com:8443/`      | OAuth 2.0 resource server protected with an AM web agent, where the protected resources are deployed in Apache Tomcat |

The two AM servers communicate using OAuth 2.0. The web agent on the resource server communicates with AM using AM specific requests. The resource server in this example doesn't need to support OAuth 2.0.

The high-level configuration steps are as follows:

1. On the AM server that acts as an OAuth 2.0 client (AM2), configure an agent profile and the policy used to protect the resources.

2. On the web server or application container that acts as an OAuth 2.0 resource server (RS), install and configure an AM web agent.

   Make sure that you can access the resources when you log in through an authentication tree that you know is working, such as the default `ldapService` tree.

   For example, if you try to access `https://www.example.com:8443/examples/`, the web agent redirects you to the AM login page. After you log in successfully as a user with access rights to the resource, AM redirects you back to `https://www.example.com:8443/examples/` and the web agent lets you access the requested resources.

3. Configure AM1 as an OAuth 2.0 authorization service.

   Learn more in [Authorization server configuration](oauth2-configure-authz.html).

4. Configure AM2 as an OAuth 2.0 client by setting up a social identity provider service.

   Learn more in [Social authentication](../am-authentication/social-registration.html).

5. On AM1, register the OAuth 2.0 or OIDC identity provider as an OAuth 2.0 client.

   Learn more in [Client application registration](oauth2-register-client.html).

6. Create a social registration journey that references your social authentication provider.

   Learn more in [Configure social registration trees](../am-authentication/social-registration.html#basic-social-registration).

7. Log out and log in again using the social authentication journey to verify that you can access the protected resources.

---

---
title: AM as client and resource server
description: Configure PingAM as an OAuth 2.0 client to authenticate resource owners and provide sessions for accessing protected resources
component: pingam
version: 8.1
page_id: pingam:am-oauth2:openam-oauth2-client
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oauth2/openam-oauth2-client.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "Clients", "Authorization", "Setup &amp; Configuration"]
page_aliases: ["oauth2-guide:openam-oauth2-client.adoc"]
---

# AM as client and resource server

When AM functions as an OAuth 2.0 client, it provides a session after successfully authenticating the resource owner and obtaining authorization. The client can then access resources protected by agents.

To configure AM as an OAuth 2.0 client, use a [Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/8.1/social-provider-handler.html) as part of the authentication journey.

The following sequence diagram shows how the client gains access to protected resources in the scenario where AM functions as both authorization server and client:

![AM as client, where authentication and authorization are handled by the authorization server. On success, an SSO session is created, so that AM access management can happen as it normally does.](_images/oauth2-openam-client.svg)Figure 1. OAuth 2.0 client and authorization server

Because the OAuth 2.0 client functionality is implemented as an AM authentication node, you don't need to deploy your own resource server implementation when using AM as an OAuth 2.0 client. Use web or Java agents or PingGateway to protect resources.

Find information about configuring AM as an OAuth 2.0 client in [Social authentication](../am-authentication/social-registration.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To use your own client and resource server, make sure the resource server implements the logic for handling access tokens and [refresh tokens](oauth2-refresh-tokens.html).The resource server can use the `/oauth2/introspect` endpoint to determine whether the access token is still valid, and to retrieve the scopes associated with the access token.To design your own scopes implementation, refer to [Customize OAuth 2.0](customizing-oauth2-scopes.html). |

---

---
title: AM as the authorization server
description: Use PingAM as an OAuth 2.0 authorization server to authenticate resource owners, obtain their authorization, and issue access tokens to clients
component: pingam
version: 8.1
page_id: pingam:am-oauth2:am-as-authz-server
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oauth2/am-as-authz-server.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authorization", "OAuth 2.0", "Federation"]
page_aliases: ["openam-oauth2-authz-server.adoc", "oauth2-guide:am-as-authz-server.adoc"]
section_ids:
  oauth2-introduction: OAuth 2.0 concepts
  supported_oauth_2_0_features: Supported OAuth 2.0 features
  oauth2-security-considerations: Security considerations
  oauth2-sample-mobile-applications: OAuth 2.0 sample mobile applications
---

# AM as the authorization server

As an authorization server, AM *authenticates* resource owners and obtains their *authorization* to return access tokens to clients.

Before you configure OAuth 2.0 in your environment, familiarize yourself with the [OAuth 2.0 authorization framework](https://www.rfc-editor.org/info/rfc6749) and the [RFCs, Internet-Drafts, and standards](../am-reference/am-supported-standards.html#standards-oauth2) that AM supports relating to OAuth 2.0.

## OAuth 2.0 concepts

RFC 6749, the [OAuth 2.0 authorization framework](https://www.rfc-editor.org/info/rfc6749) lets a third-party application obtain limited access to a resource (usually user data) on behalf of the resource owner or the application itself.

The main actors in the OAuth 2.0 authorization framework are the following:

**OAuth 2.0 framework actors**

| Actor                         | Description                                                                                                                                                                                                                                                                                                                             |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Resource owner (RO)**       | The owner of the resource. For example, a user who stores their photos in a photo-sharing service.The resource owner uses a *user-agent*, usually a web-browser, to communicate with the client.                                                                                                                                        |
| **Client**                    | The third-party application that wants to access the resource. The client makes requests on behalf of the resource owner and with their authorization. For example, a printing service that needs to access the resource owner's photos to print them.AM can act as a client.                                                           |
| **Authorization server (AS)** | The authorization service that authenticates the resource owner and/or the client, issues access tokens to the client, and tracks their validity. Access tokens prove that the resource owner authorizes the client to act on their behalf over specific resources for a limited period of time.AM can act as the authorization server. |
| **Resource server (RS)**      | The service hosting the protected resources. For example, a photo-sharing service. The resource server must be able to validate the tokens issued by the authorization server.A website protected by a web or a Java agent can act as the resource server.                                                                              |

The following sequence diagram demonstrates the basic OAuth 2.0 flow:

![AM can function as the authorization server and also as the client.](_images/oauth2-flow.svg)Figure 1. OAuth 2.0 protocol flow

To use AM as an authorization server, register an OAuth 2.0 client in the AM admin UI. Clients can also register themselves dynamically. For details, refer to [Client application registration](oauth2-register-client.html).

## Supported OAuth 2.0 features

As an authorization server, AM supports the following features:

**OAuth 2.0 Features**

| Feature                                                    | Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Grant types](oauth2-implementing-flows.html)              | * Authorization code

* Implicit

* Resource owner password credentials

* Client credentials

* Device flow

* SAML 2.0 profile for authorization grant

* JWT profile for OAuth 2.0 authorization grants                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Client authentication standards](oauth2-client-auth.html) | - JWT profile for OAuth 2.0 client authentication

- Mutual TLS                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Token exchange standards](token-exchange.html).           | OAuth 2.0 token exchange                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Other OAuth 2.0 standards                                  | * [JWT proof-of-possession](oauth2-PoP-JWK.html)

* [Certificate-based proof-of-possession](oauth2-PoP-Cert.html)

* [User-managed access (UMA) 2.0](../uma/preface.html)

* [OpenID Connect](../am-oidc1/preface.html)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Remote consent services](oauth2-remote-consent.html)      | Delegates the consent-gathering part of an OAuth 2.0 flow to a separate service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Customizable scope grants                                  | You can customize how scopes are granted to the client, regardless of the grant flow used.AM can grant scopes statically or dynamically:* Statically (default)

  Configure several OAuth 2.0 clients with different subsets of scopes. Resource owners are redirected to a specific client, depending on the scopes required. As long as the resource owner can authenticate and the client can deliver the same or a subset of the requested scopes, AM issues the token with the scopes requested. Two different users requesting scopes A and B from the same client will always receive scopes A and B.

* Dynamically

  Configure an OAuth 2.0 client with a comprehensive list of scopes. Resource owners authenticate against that client. When AM receives a request for scopes, the authorization service grants or denies access scopes dynamically by evaluating authorization policies. Two different users requesting scopes A and B from the same client can receive different scopes, based on policy conditions.

  For details, refer to [Authorization and policy decisions](../am-authorization/what-is-authz-decision.html) and [Dynamic OAuth 2.0 authorization](../am-authorization/oauth2-authorization.html). |

## Security considerations

|   |                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | OAuth 2.0 messages involve credentials and access tokens that allow the bearer to retrieve protected resources. You must protect the messages going across the network and prevent attackers from capturing requests or responses. |

RFC 6749 includes a number of [security considerations](https://www.rfc-editor.org/rfc/rfc6749.html#section-10) and requires Transport Layer Security (TLS) to protect sensitive messages. Make sure you read these security considerations and implement them in your deployment.

When you are deploying a combination of other clients and resource servers, pay special attention to the [OAuth 2.0 threat model and security considerations](https://www.rfc-editor.org/info/rfc6819) before putting your service into production.

## OAuth 2.0 sample mobile applications

Download the sample mobile application to try the capabilities of AM as an authorization server.

For access to the source code, refer to [How do I access and build the sample code provided for PingAM?](https://support.pingidentity.com/s/article/How-do-I-access-and-build-the-sample-code-provided-for-PingAM) in the *Knowledge Base*.