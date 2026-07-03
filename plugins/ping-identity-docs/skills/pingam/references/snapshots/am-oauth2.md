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

* **Realm level**: In the AM admin UI, go to Realms > *realm name* > Services > OAuth2 Provider > Advanced, and select Use token\_introspection claim for JWT.

* **Client level**: In the AM admin UI, go to Realms > *realm name* > Applications > OAuth 2.0 > *client ID* > OAuth2 Provider Overrides. Enable OAuth2 Provider Overrides, then select Use token\_introspection claim for JWT.

When enabled, AM wraps the introspected token's claims inside a `token_introspection` claim in the JWT. This separates the JWT's own top-level claims (such as `iss`, `aud`, and `iat` for the introspection response itself) from the introspected token's claims:

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

When enabled, the `aud` claim of the introspected token is always included in the response, including for stateless (client-side) tokens.

When disabled, the `aud` claim is omitted from the response, and a flat JWT structure is used.

|   |                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This setting is disabled by default to preserve existing behavior after upgrades. Enable it for new deployments or when your resource servers are ready to consume RFC 9701-compliant responses. |

## Response content

The following table describes fields you may find in the introspection response:

| Field         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `active`      | Whether the token is active (`true`) or not (`false`).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
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
title: Manage consent
description: Many OAuth 2.0 and OIDC flows require user consent to grant the client access to the user's resources.
component: pingam
version: 8.1
page_id: pingam:am-oauth2:oauth2-manage-consent
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oauth2/oauth2-manage-consent.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "OpenID Connect (OIDC)", "Authorization", "Setup &amp; Configuration"]
page_aliases: ["oauth2-guide:allowing-clients-to-skip-consent.adoc", "oauth2-guide:allowing-am-to-save-consent.adoc", ":description: Configure OAuth 2.0 and OIDC client applications to use implied consent", "gather user consent", "store consent decisions", "and revoke client access"]
section_ids:
  skip-consent: Implied consent
  gather-consent: Gather consent
  store-consent-decisions: Store consent decisions
  revoke_consent: Revoke consent
---

# Manage consent

Many OAuth 2.0 and OIDC flows require user consent to grant the client access to the user's resources.

## Implied consent

OAuth 2.0 and OIDC client applications can use *implied consent*. With implied consent, *AM does not prompt for consent during authorization flows*. This simplifies the flows. The user has only to sign on to grant the client access to protected resources.

To enable implied consent, follow these steps:

1. In the AM admin UI, go to Realms > *realm name* > Applications > OAuth 2.0 > Clients > *client ID* > Advanced.

2. Select Implied Consent.

3. Save your changes.

4. Make sure AM lets users skip granting consent.

   By default, this is enabled in the OAuth 2.0 provider configuration, Realms > *realm name* > Services > OAuth2 Provider > Consent > Allow Clients to Skip Consent.

   If that is disabled for your deployment, switch to the OAuth2 Provider Overrides tab in the client profile, make the following changes to the settings, and save your work:

   * Enable OAuth2 Provider Overrides

     Enabled

   * Allow Clients to Skip Consent

     Enabled

To disable implied consent and force users to grant consent during authorization flows, disable the settings described in the previous steps.

## Gather consent

Configure how the client application appears to the user. The following alternatives are available:

* Customize the built-in consent screen:

  1. In the AM admin UI, go to Realms > *realm name* > Applications > OAuth 2.0 > Clients > *client ID*.

     Edit the following settings under the Advanced tab, then save your work:

     * Display name

       Display this name to the user when prompting for consent.

     * Display description

       Explain the decision to the user when prompting for consent.

     * Privacy Policy URI

       Add for the client applications privacy policy.

  2. Configure how scopes display.

     Users grant consent based on *scopes*. Scopes restrict what is shared with the client and limit what the client can do with the user's data. In OAuth 2.0, the meanings of scopes depend on the implementation. In OpenID Connect, scopes map to standard user data claims; for example, the `profile` scope requests access to the user's default profile claims.

     For details, refer to [Display scopes in the consent screen](oauth2-scopes.html#configure-scopes).

* Delegate consent gathering to another service.

  For details, refer to [Remote consent](oauth2-remote-consent.html).

## Store consent decisions

AM can store the consent decisions in the user profile. This minimizes redundant prompts and improves the user experience.

When an OAuth 2.0 client application requests scopes, AM checks the user profile for scopes the user has already consented to. AM does not prompt the user to consent again to the same scopes, only scopes the user has not consented to.

To save consent:

1. Add a multivalued string syntax attribute, such as `custom_consent`, to user profiles for saving consent decisions.

   The attribute must be of type `array`.

   For instructions on adding the attribute, refer to [Update the identity store for a custom attribute](../setup/customizing-data-stores.html#add-attr-to-identity-repository).

2. In the AM admin UI, go to Realms > *realm name* > Services > OAuth2 Provider and select the Consent tab.

3. In the Saved Consent Attribute field, add the name of the attribute you created, such as `custom_consent`.

4. Save your changes.

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | To force AM to prompt for consent for a specific client request, add the `prompt=consent` parameter. |

## Revoke consent

You can revoke a client application's access at any time through the user dashboard page:

1. Sign on as an end user.

   Your dashboard page displays.

2. Expand Authorized Apps.

3. Click the delete icon [icon: times, set=fa]to revoke access:

   ![Revoke client application access through the user dashboard.](_images/xui-oauth2-self-service.png)Figure 1. Authorized Apps pane

---

---
title: Mutual TLS
description: Authenticate OAuth 2.0 clients using mutual TLS with X.509 certificates, either self-signed or PKI-based, to PingAM
component: pingam
version: 8.1
page_id: pingam:am-oauth2:client-auth-mtls
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oauth2/client-auth-mtls.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Authentication", "OAuth 2.0", "TLS/SSL", "Federation", "Certificates", "Setup &amp; Configuration"]
page_aliases: ["oauth2-guide:client-auth-mtls.adoc"]
section_ids:
  pki-mtls: Mutual TLS using PKI
  configure_am_for_mutual_tls_using_pki: Configure AM for mutual TLS using PKI
  self-signed-mtls: Mutual TLS using self-signed X.509 certificates
  configure_am_for_mutual_tls_using_self_signed_x_509_certificates: Configure AM for Mutual TLS using self-signed X.509 certificates
  provide-mtls-certs: Provide client certificates to AM
  standard_tls_client_certificate_authentication: Standard TLS client certificate authentication
  trusted_headers: Trusted headers
---

# Mutual TLS

Clients can authenticate to AM by using mutual TLS (mTLS) and X.509 certificates. The certificates are either self-signed or use public key infrastructure (PKI), as per version 12 of the draft specification, [OAuth 2.0 Mutual TLS Client Authentication and Certificate Bound Access Tokens](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-mtls-12).

|   |                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | AM also supports the Certificate Bound Access Tokens part of the specification. Learn more in [Certificate-bound proof-of-possession](oauth2-PoP-Cert.html). |

## Mutual TLS using PKI

To authenticate OAuth 2.0 clients with mTLS, the certificate presented by the client must have a subject-distinguished name that exactly matches a value specified in the client profile in AM.

The Certificate Authority (CA) specified in the chain must also be trusted by AM. Configure a secret mapping with the secret label `am.services.oauth2.tls.client.cert.authentication` to specify the CAs AM trusts.

### Configure AM for mutual TLS using PKI

Follow these steps to configure AM to support mutual TLS using PKI:

1. If you haven't already done so, create an OAuth 2.0 client profile.

   Learn more in [Client application registration](oauth2-register-client.html).

2. Set up a secret store in the same realm as the OAuth 2.0 client.

   AM maintains the details of trusted CAs in this secret store.

   You can use an existing secret store or create a new store as follows:

   1. In the AM admin UI, go to Realms > *realm name* > Secret Stores, and click Add Secret Store.

   2. Enter an ID for the secret store (for example, `TrustStore`), select the store type, complete the required fields, and click Create.

   |   |                                                                                                                                                                                                                                             |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You might need to configure the credentials for accessing the new store in one of the other configured secret stores. Learn more about configuring secret stores in [Secrets, certificates, and keys](../security/secrets-certs-keys.html). |

3. Import the certificates belonging to the CAs you want the instance of AM to trust.

4. Map the aliases of the imported certificates to the `am.services.oauth2.tls.client.cert.authentication` secret label:

   * In the AM admin UI, go to Realms > *realm name* > Secret Stores > *store name* > Mappings, and click Add Mapping.

   * In the Secret Label field, select `am.services.oauth2.tls.client.cert.authentication`.

   * In the Aliases field, enter the alias of the imported CA certificate to trust and click Add.

   * Repeat the previous step to add the aliases of all the CA certificates to trust, and click Create.

5. Add the subject-distinguished name that must appear in the client certificate to be able to authenticate:

   * In the AM admin UI, go to Realms > *realm name* > Applications > OAuth 2.0 > *agent name* > Signing and Encryption.

   * In the mTLS Subject DN field, enter the client certificate subject DN. For example, `CN=myOauth2Client`. Certificate tools, such as OpenSSL, can display DN attributes in different orders or formats, so copied output might need adjusting to match the required format.

     |   |                                                                                                                                                        |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
     |   | If this field is left empty, the default value that must be found in a CA-signed client certificate is `CN=client ID`. For example, `CN=myMTLSClient`. |

   * Save your changes.

6. Configure the OAuth 2.0 provider to check whether the certificates presented by the authenticating clients have been revoked:

   * In the AM admin UI, go to Realms > *realm name* > Services > OAuth2 Provider > Advanced.

   * Enable Check TLS Certificate Revocation Status.

   * In the OCSP Responder URI field, enter the URI of the online certificate status protocol responder service. AM uses this service to check the certificates.

     If not specified, AM determines the appropriate URI from the certificate.

   * In the OCSP Responder Certificate field, enter the PEM-encoded certificate that AM will use to verify all OCSP responses.

     If not specified, AM determines the appropriate certificate from the trusted CA certificates configured in the `am.services.oauth2.tls.client.cert.authentication` secret label.

AM is now configured to accept CA-signed client certificates for authentication. For information on how to present the certificates when authenticating, refer to [Provide client certificates to AM](#provide-mtls-certs).

## Mutual TLS using self-signed X.509 certificates

This method of authenticating OAuth 2.0 clients requires that the self-signed X.509 certificate presented by the client exactly matches a certificate specified in the client profile in AM.

Specify the expected self-signed X.509 certificate in the client profile using one of these methods:

* JSON Web Key Set (JWKS)

  Specify the X.509 certificates in the X.509 Certificate Chain (`x5c`) attribute of the JSON Web Keys specified in the set.

* JSON Web Key Set URI (JWKS\_uri)

  AM periodically retrieves the JWKS from the specified URI, and uses the certificates provided in the X.509 Certificate Chain (`x5c`) attribute to verify the client certificate.

* Store the X.509 certificate as a secret in the secret store.

* Store the X.509 certificate in the configuration.

  Add the exact content of the X.509 certificate in the client profile.

  Unlike the other methods, only a single certificate can be specified using this method.

### Configure AM for Mutual TLS using self-signed X.509 certificates

Follow these steps to configure AM to support mutual TLS using self-signed certificates.

1. If you haven't already done so, [create an OAuth 2.0 client profile in AM](oauth2-register-client.html).

2. To provide the X.509 certificates the client will use to authenticate, go to Applications > OAuth 2.0 > Clients > *client ID* > Signing and Encryption, and then perform one of the following steps:

   * Use a JSON Web Key Set (JWKS) to specify the certificates:

     1. Set the Public key selector property to `JWKs`.

     2. Enter the contents of the JWKS in the Json Web Key property.

   * Use a JSON Web Key Set URI (JWKS\_uri) to specify the certificates:

     1. Set the Public key selector property to `JWKs_uri`.

     2. Enter the JWKS URI in the Json Web Key URI property.

   * Store the X.509 certificate as a secret in a secret store:

     1. Follow the steps in [Secret stores](../security/secret-stores.html) to add the certificate as a secret.

     2. Map this secret to the `am.applications.oauth2.client.identifier.mtls.trusted.cert` secret label, where `identifier` is the value of the Secret Label Identifier configured for the client on the Core tab.

   * Use the contents of an X.509 certificate:

     1. Set the Public key selector property to `X509`.

     2. In the mTLS Self-Signed Certificate field, enter the contents of the X.509 certificate in PEM or DER format.

   |   |                                                                                                                                                                                 |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | OIDC clients must also specify the authentication method they're using in their client profiles. Learn more in [OIDC client authentication](../am-oidc1/oidc-client-auth.html). |

3. Save your changes.

AM is now configured to accept self-signed client certificates for authentication. For information on how to present the certificates when authenticating, refer to [Provide client certificates to AM](#provide-mtls-certs).

## Provide client certificates to AM

The client can provide its certificate to AM using either standard TLS client certificate authentication or trusted headers.

|   |                                                                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You must configure the web container in which AM runs to use TLS connections, and to request and accept client certificates.Consult the documentation for your web container to determine the appropriate actions to take. |

### Standard TLS client certificate authentication

The client provides its certificates in the standard servlet client certificate attribute.

This method is preferred because the web container verifies that the client authenticated the TLS session with the private key associated with the certificate.

When you've configured AM to accept client certificates, the client can authenticate to the OAuth 2.0 `access_token` endpoint using one of the X.509 certificates registered in the client.

Any of the [OAuth 2.0 grant flows](oauth2-implementing-flows.html) that makes a call to the `access_token` endpoint can authenticate clients using X.509 certificates.

The following example uses the [Client credentials grant](oauth2-client-cred-grant.html) and attaches the client certificates to the request:

```bash
$ curl \
--request POST \
--data "client_id=myClient" \
--data "grant_type=client_credentials" \
--data "scope=write" \
--data "response_type=token" \
--cert "myClientCertificate.pem" \
--key "myClientCertificate.key.pem" \
"https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/access_token"
{
  "access_token": "sbQZuveFumUDV5R1vVBl6QAGNB8",
  "scope": "write",
  "token_type": "Bearer",
  "expires_in": 3599
}
```

### Trusted headers

AM receives the certificates in a configured, trusted HTTP header.

This method is intended for cases where TLS is being terminated at a reverse proxy or load balancer, so the container in which AM runs can't directly authenticate the client.

|   |                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | AM can receive certificates in the following formats:- DER-encoded.

- Raw PEM-encoded.

- DER- or PEM-encoded first, then URL-encoded, for compatibility with the NGINX `$ssl_client_escaped_cert` variable.

- DER- or PEM-encoded first, URL-encoded next, then included as a field in a multi-field trusted header, for compatibility with the Envoy `x-forwarded-client-cert` headers. |

You **must** configure the proxy or load balancer to do the following:

1. Forward the certificate to AM in the trusted header.

   To specify the format of the trusted header, go to Realms > *realm name* > Services > OAuth2 Provider > Advanced, and choose the appropriate value in the TLS Client Certificate Header Format drop-down list:

   * Use `BASE64_ENCODED_CERT` for Base64-encoded, URL-encoded certificates in PEM or DER format.

     AM infers the certificate type from the contents of the certificate. For example, a certificate that starts with `-----BEGIN CERTIFICATE-----` and ends with `-----END CERTIFICATE-----` is inferred to be a PEM format certificate. A certificate that starts and ends with a colon (`:`) is inferred to be a DER format certificate.

     NGINX, Google GKE, and AWS provide certificates in this format.

   * Use `X_FORWARDED_CLIENT_CERT` if the proxy provides the certificate in the `X-Forwarded-Client-Cert` header.

     Istio/Envoy proxies provide certificates in this way. Find more information in the [Envoy documentation](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_conn_man/headers#config-http-conn-man-headers-x-forwarded-client-cert).

2. Strip the trusted header from any incoming requests.

   |   |                                                                                                                          |
   | - | ------------------------------------------------------------------------------------------------------------------------ |
   |   | You must do this because AM has no way of authenticating the contents of this header, so will trust whatever is present. |

   To specify the name of the trusted header, in the AM admin UI, go to Realms > *realm name* > Services > OAuth2 Provider > Advanced, and enter the header name in the Trusted TLS Client Certificate Header property.

   |   |                                                                                                                                                                                                                                            |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Specify a strong, random name for the trusted header. A misconfigured proxy or load balancer could let an attacker send malicious header values. A trusted header name that's difficult to guess makes this type of attack more difficult. |

---

---
title: OAuth 2.0
description: Learn OAuth 2.0 concepts, configuration, and usage procedures for PingAM as an authorization server
component: pingam
version: 8.1
page_id: pingam:am-oauth2:preface
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oauth2/preface.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["index.adoc", "oauth2-guide:preface.adoc"]
---

# OAuth 2.0

This guide covers concepts, configuration, and usage procedures for working with OAuth 2.0 and PingAM.

[icon: handshake, set=fad, size=3x]

#### [AM as the authorization server](am-as-authz-server.html)

How AM plays the role of the authorization server.

[icon: edit, set=fad, size=3x]

#### [Configure AM for OAuth 2.0](oauth2-configure-authz.html)

Configure AM as an OAuth 2.0 authorization server.

[icon: random, set=fad, size=3x]

#### [OAuth 2.0 grant flows](oauth2-implementing-flows.html)

Discover the OAuth 2.0 flows and how to implement them in AM.

[icon: exchange-alt, set=fad, size=3x]

#### [OAuth 2.0 endpoints](oauth2-client-endpoints.html)

About endpoints AM exposes as an OAuth 2.0 authorization server.

[icon: check-square, set=fad, size=3x]

#### [OAuth 2.0 consent](oauth2-manage-consent.html)

Allow OAuth 2.0 clients to skip consent, and users to save and revoke consent.

[icon: tags, set=fad, size=3x]

#### [OAuth 2.0 scopes](oauth2-scopes.html)

Learn about scopes and how to configure them in AM.

---

---
title: OAuth 2.0 administration REST endpoints
description: Use PingAM OAuth 2.0 administration REST endpoints to manage clients, resource sets, and application tokens
component: pingam
version: 8.1
page_id: pingam:am-oauth2:oauth2-admin-endpoints
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oauth2/oauth2-admin-endpoints.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "Endpoints", "Administration", "REST API"]
page_aliases: ["oauth2-guide:oauth2-admin-endpoints.adoc"]
---

# OAuth 2.0 administration REST endpoints

AM exposes the following administration and supporting REST endpoints:

**OAuth 2.0 administration and supporting endpoints**

| Endpoint                            | Description                                                                                                                                                               |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/realm-config/agents/OAuth2Client` | Register, list, and delete OAuth 2.0 clients (AM specific-endpoint)                                                                                                       |
| `/users/user/oauth2/resources/sets` | Retrieve data for UMA resources registered to a particular user (AM-specific endpoint)                                                                                    |
| `/users/user/oauth2/applications`   | List OAuth 2.0 clients holding active tokens granted by specific resource owners, and delete tokens for a combination of resource owner and client (AM-specific endpoint) |

---

---
title: OAuth 2.0 client authentication
description: Configure OAuth 2.0 client applications to authenticate using HTTP Basic authentication, form parameters, JWT, or mutual TLS
component: pingam
version: 8.1
page_id: pingam:am-oauth2:oauth2-client-auth
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oauth2/oauth2-client-auth.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "Endpoints", "Authentication", "REST API"]
page_aliases: ["oauth2-guide:oauth2-client-auth.adoc"]
---

# OAuth 2.0 client authentication

OAuth 2.0 client applications send their authentication credentials using one of the following mechanisms:

* The [Authorization header (HTTP Basic)](client-auth-header.html) (default)

* [Form parameters (HTTP POST)](client-auth-form.html)

* A [JWT profile](client-auth-jwt.html)

* [Mutual TLS](client-auth-mtls.html)

Authentication depends on the Client type defined in the AM admin UI under Realms > *realm name* > Applications > OAuth 2.0 > Clients > *client ID* > Core:

* Confidential clients

  These applications include websites and services that make secure connections to AM.

  They can protect their client secret or JSON Web Token (JWT).

  You configure the authentication method for a confidential client in the AM admin UI under Realms > *realm name* > Applications > OAuth 2.0 > Clients > *client ID* > Advanced as the Token Endpoint Authentication Method.

  When a client authenticates with form parameters, the server can store POST data on the user-agent in an `OAUTH_REQUEST_ATTRIBUTES` cookie. AM uses the cookie to continue the authentication process across redirects. It marks the cookie for deletion on the next successful OAuth 2.0 authorization.

* Public clients

  These are single-page applications and applications running on devices.

  They cannot protect secrets.

  Public clients identify themselves by client ID, but do not fully authenticate.

  Public OIDC clients must specify `none` as their authentication method.

---

---
title: OAuth 2.0 endpoint parameters
description: Reference guide for OAuth 2.0 endpoint parameters used in authorization requests, token requests, and other OAuth 2.0 flows
component: pingam
version: 8.1
page_id: pingam:am-oauth2:oauth2-parameters
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oauth2/oauth2-parameters.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "Endpoints", "Properties"]
page_aliases: ["oauth2-guide:oauth2-parameters.adoc"]
section_ids:
  acr-values: acr_values
  actor-token: actor_token
  actor-token-type: actor_token_type
  auth-chain: auth_chain
  authorization_details: authorization_details
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
  general_validation_rules: General validation rules
  jar_validation_rules: JAR validation rules
  oidc_validation_rules: OIDC validation rules
  par_validation_rules: PAR validation rules
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

Authentication context class reference values communicate acceptable Levels of Assurance (LoAs) users must satisfy when authenticating to the OpenID provider. For details, refer to [Authentication requirements](../am-oidc1/oidc-authentication-requirements.html).

## `actor_token`

The token representing a delegate acting on behalf of another identity in [Token exchange](token-exchange.html).

## `actor_token_type`

The type of the actor token:

* `urn:ietf:params:oauth:token-type:access_token`

* `urn:ietf:params:oauth:token-type:id_token`

## `auth_chain`

A string naming the journey to authenticate the resource owner for the [Resource owner password credentials grant](oauth2-ropc-grant.html). The journey must permit username-password authentication without UI interaction. Otherwise, the request results in an HTTP 500 Internal Server Error.

Default: The default authentication journey for the realm.

## `authorization_details`

A valid JSON array containing fine-grained authorization requirements, as specified in [RFC 9396: OAuth 2.0 Rich Authorization Requests](https://www.rfc-editor.org/rfc/rfc9396.html). Each authorization detail object in the array must contain a non-blank `type` string. For example:

```json
"authorization_details": [{
      "type": "account_information",
      "actions": [
         "list_accounts",
         "read_balances",
         "read_transactions"
      ],
      "locations": [
         "https://example.com/accounts"
      ]
  }],
```

If the `type` is missing or blank, AM returns an `invalid_authorization_details` error.

## `claims`

A JSON object containing the user attributes to return in the ID token. [OIDC flows](https://openid.net/specs/openid-connect-core-1_0.html) only.

## `client_assertion`

A signed JSON Web Token (JWT) to use as client credentials for [JWT profile](client-auth-jwt.html) authentication.

## `client_assertion_type`

The type of assertion for [JWT profile](client-auth-jwt.html) authentication.

Set `client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer`.

## `client_id`

A unique string identifier for the application making the request.

For a [pushed authorization request](oauth2-authz-grant-par.html) or a [JWT-secured authorization request](https://www.rfc-editor.org/rfc/rfc9101.html) (RFC 9101), this value must match the `client_id` claim in the `request` object.

## `client_secret`

A string password credential for the confidential client application making the request.

Use this parameter for client authentication with [Form parameters (HTTP POST)](client-auth-form.html).

Do not use with the `cnf_key` parameter.

## `cnf_key`

A base64-encoded JSON Web Key (JWK) for [JWK-based proof-of-possession](oauth2-PoP-JWK.html) or a base64-encoded SHA-256 hash of the DER-encoded X.509 certificate for [Certificate-bound proof-of-possession](oauth2-PoP-Cert.html).

Do not use with the `client_secret` parameter.

## `code_challenge`

A generated code verifier string for RFC 7636 [Proof Key for Code Exchange](https://www.rfc-editor.org/rfc/rfc7636) (PKCE).

Learn more in [Generate a code verifier and a code challenge](oauth2-authz-grant-pkce.html#proc-auth-code-generate-pkce).

## `code_challenge_method`

A string specifying the method to derive the PKCE code challenge:

* `plain` (default; plaintext code challenge )

* `S256` (recommended; hashed code challenge)

## `code_verifier`

A random string correlating a PKCE authorization request with the token request.

## `csrf`

The SSO token string linking the request to user session to protect against Cross-Site Request Forgery (CSRF) attacks.

This parameter duplicates the value of the session cookie, the resource owner's SSO token.

Built-in consent pages include this parameter once the resource owner has authenticated, and send it with the resource owner's consent. Custom consent pages and flows that do not use a browser must set this parameter explicitly unless you use a [Remote consent](oauth2-remote-consent.html). For an example, refer to the [Authorization code grant](oauth2-authz-grant.html).

## `decision`

A string indicating whether the resource owner consents to the requested access:

* `allow` to grant consent

* Any other value denies consent

## `grant_type`

A string specifying the type of grant to acquire an access token:

* `authorization_code`

  For [authorization code grants](oauth2-authz-grant.html).

* `client_credentials`

  For the [Client credentials grant](oauth2-client-cred-grant.html).

* `password`

  For the [Resource owner password credentials grant](oauth2-ropc-grant.html).

* `refresh_token`

  To [refresh an access token](oauth2-refresh-tokens.html).

* `urn:ietf:params:oauth:grant-type:device_code`

  For the [Device authorization grant](oauth2-device-flow.html). AM also supports the earlier `http://oauth.net/grant_type/device/1.0` specification.

* `urn:ietf:params:oauth:grant-type:saml2-bearer`

  For the [SAML 2.0 profile for authorization](oauth2-saml2-bearer-grant.html).

* `urn:ietf:params:oauth:grant-type:jwt-bearer`

  For the [JWT profile for authorization](oauth2-jwt-bearer-grant.html).

* `urn:ietf:params:oauth:grant-type:token-exchange`

  For the [Token exchange](token-exchange.html).

* `urn:ietf:params:oauth:grant-type:uma-ticket`

  For the [UMA grant flow](../uma/uma-grant-flow.html).

* `urn:openid:params:grant-type:ciba`

  For the [Backchannel request grant](../am-oidc1/openid-connect-backchannel-request-flow.html).

## `id_token_hint`

A previously issued ID token passed as a hint about the end user's session with the client. [OIDC flows](https://openid.net/specs/openid-connect-core-1_0.html) only.

Set the `response_type` and `prompt` parameters to `none` when using this parameter. Learn more in [Session Management Draft 10](../am-oidc1/session-management.html#session_management_state).

## `login_hint`

A string specifying the ID used to log in. [OIDC flows](https://openid.net/specs/openid-connect-core-1_0.html) only.

The ID depends on the authentication journey.

When provided as part of the OpenID Connect authentication request, an `HttpOnly` cookie (only sent over HTTPS) named `oidcLoginHint` gets the value of `login_hint`. Learn more in [GSMA Mobile Connect](../am-oidc1/oidc-mobile-connect.html).

## `nonce`

A string linking the client session with the ID token to mitigate against replay attacks. [OIDC flows](https://openid.net/specs/openid-connect-core-1_0.html) only.

## `prompt`

A space-separated, case-sensitive list of ASCII strings that indicates whether to prompt the end user for authentication and consent. [OIDC flows](https://openid.net/specs/openid-connect-core-1_0.html) only.

* `consent`

  Prompt the end user for consent even if a consent response was previously saved.

* `login`

  Prompts the end user to authenticate using the journey specified with the [`service`](#service) parameter. AM destroys the original session and creates a new one for the new journey.

  Default: The default journey for the realm.

* `none`

  Don't display authentication or consent pages. Use this only when you set `id_token_hint` and `response_type=none`.

## `redirect_uri`

The URI to return the resource owner to after authorization is complete.

Default: A value from the client profile Redirection URIs setting in the AM admin UI.

## `response_mode`

A string specifying the mechanism for returning response parameters:

* `form_post`

  Return a self-submitting form that contains the code instead of redirecting to the redirect URL with the code as a string parameter. Learn more in [OAuth 2.0 Form Post Response Mode](https://openid.net/specs/oauth-v2-form-post-response-mode-1_0.html).

* `fragment`

  Return parameters encoded in the URL fragment; default when `response_type=token`.

* `fragment.jwt`

  Return a JWT in a fragment.

* `jwt`

  Return parameters in a JWT; in a query string for the `code` response type, or appended to the fragment for the `token` response type.

  A JWT-secured authorization response (JARM) returns authorization response parameters in a signed, optionally encrypted, JWT.

  Configure the algorithms to secure the JWT in the AM admin UI under Realms > *realm name* > Applications > OAuth 2.0 > Clients > *client ID* > Signing and Encryption.

  In addition to claims specific to the response type, such as `code` or `access_token`, the JWT contains these mandatory claims:

  * `iss`: the URL of the issuer—​the authorization server that generated the response

  * `aud`: the audience—​the client ID intended as the response recipient

  * `exp`: the expiration of the JWT—​10 minutes is the recommended maximum

  On error, the JWT contains:

  * An `error` string

  * A `state` string if specified by the client

  * An error description

  Learn more in [JWT-Secured Authorization Response Mode for OAuth 2.0 (JARM)](https://openid.net/specs/openid-financial-api-jarm.html).

* `query`

  Return parameters encoded in the query string; default when `response_type=code`.

* `query.jwt`

  Return a JWT in a query parameter. Do *not* use this with `id_token` or `token` response types unless the response JWT is encrypted.

Learn more in [Response Modes](https://openid.net/specs/oauth-v2-multiple-response-types-1_0.html#ResponseModes). AM publishes supported response modes as `response_modes_supported` through the [/oauth2/.well-known/openid-configuration](../am-oidc1/rest-api-oidc-discovery-configuration.html) endpoint.

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

AM validates request objects according to:

* The type of request

* The OAuth 2.0 provider configuration (specifically, the [Request Object Processing Specification](../setup/services-configuration.html#config-request-object-proc-spec) setting)

* The value of the [oauth2.provider.request.object.processing.enforced](../setup/server-advanced.html#request.object.processing.enforced) advanced server property

The validation rules apply whether you pass the request object by value with the `request` parameter or as a reference with the `request_uri` parameter.

> **Collapse: How AM determines which rules to apply**
>
> | Input                 |                   |                   |                   | Behavior     |
> | --------------------- | ----------------- | ----------------- | ----------------- | ------------ |
> | Specification value 1 | `enforced` flag 2 | OIDC parameters 3 | `/par` endpoint 4 | Rule applied |
> | OIDC                  | `false`           | Yes               | No                | OIDC         |
> | OIDC                  | `false`           | No                | No                | JAR          |
> | OIDC                  | `true`            | Yes               | No                | OIDC         |
> | OIDC                  | `true`            | No                | No                | OIDC         |
> | JAR                   | `false`           | Yes               | No                | JAR          |
> | JAR                   | `false`           | No                | No                | JAR          |
> | JAR                   | `true`            | Yes               | No                | JAR          |
> | JAR                   | `true`            | No                | No                | JAR          |
> | OIDC                  | `false`           | Yes               | Yes               | PAR          |
> | OIDC                  | `false`           | No                | Yes               | PAR          |
> | OIDC                  | `true`            | Yes               | Yes               | PAR          |
> | OIDC                  | `true`            | No                | Yes               | PAR          |
> | JAR                   | `false`           | Yes               | Yes               | PAR          |
> | JAR                   | `false`           | No                | Yes               | PAR          |
> | JAR                   | `true`            | Yes               | Yes               | PAR          |
> | JAR                   | `true`            | No                | Yes               | PAR          |
>
> 1 Value of the Request Object Processing Specification setting
>
> 2 Value of the `oauth2.provider.request.object.processing.enforced` advanced server property
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

  Read the [OAuth 2.0 provider](../setup/services-configuration.html#global-oauth-oidc) configuration reference to make sure the values meet the requirements of the [Financial-grade API (FAPI)](https://openid.net/specs/openid-financial-api-part-2-1_0-final.html#authorization-server) security profile.

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

  For example, include the `code_challenge` for an [Authorization code grant with PKCE](oauth2-authz-grant-pkce.html) flow.

* When you include the request object, omit all other parameters except to authenticate the client.

  The request object *must* include claims for all other request details. Otherwise, the response is an `Invalid parameter scope` error.

### Example request object

The following example JWT request object includes OIDC claims and `iss`, `aud`, `nbf`, and `exp` claims. AM ignores keys specified in JWT headers, such as `jku` and `jwe`:

```json
{
  "client_id": "myClient",
  "iss": "myClient",
  "aud": "https://am.example.com:8443/am/oauth2/realms/root/realms/alpha",
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

```none
https://am.example.com:8443/am/oauth2/realms/root/authorize? \
&request=eyJhbGciOiJSUzI1NiIsImtpZCI6ImsyYmRjIn0.ew0KICJpc3MiOiAiczZCaGRSa3…​. \
&client_id=myClient \
&scope=openid profile \
&response_type=code%20id_token \
&nonce=abc123 \
&state=123abc
```

## `request_uri`

A reference to [JWT request object(s)](#the-request-parameter).

* For [PAR flows](oauth2-authz-grant-par.html), this references the data at the time of the PAR request.

  The authorization request fails if the request URI has expired.

* For [OIDC flows](../am-oidc1/oidc-implementing-flows.html) and [JAR](https://www.rfc-editor.org/rfc/rfc9101.html) requests, this references an array of URIs to retrieve request objects whose claims constitute the request parameters.

  You must pre-register the URIs in the client profile. In the AM admin UI, go to Realms > *realm name* > Applications > OAuth 2.0 > Clients > *client ID* > Advanced > Request uris. Each request URI must not exceed 512 ASCII characters and must use either HTTP or HTTPS; for example, `https://www.example.com:8443/JWTs/myJWT`.

  AM caches the request objects to avoid requesting them too often. To force AM to flush the cache, add a unique fragment to the `request_uri` parameter; for example, `?request_uri=https://www.example.com:8443/JWTs/myJWT#foo`.

* The [PAR](https://www.rfc-editor.org/rfc/rfc9126.html) and [JAR](https://www.rfc-editor.org/rfc/rfc9101.html#section-5.2) specifications indicate the following:

  * The authorization server should ignore authorize parameters outside the `request_uri`.

  * When sending a JWT-Secured Authorization Request (JAR), the `request_uri` *must* be an `https` URI.

  To enforce this behavior in AM, set the [am.oauth2.request.object.restrictions.enforced](../setup/server-advanced.html#am.oauth2.request.object.restrictions.enforced) advanced server property to `true`.

## `requested_token_type`

The type of token requested for [Token exchange](token-exchange.html):

* `urn:ietf:params:oauth:token-type:access_token` (default)

* `urn:ietf:params:oauth:token-type:id_token`

## `save_consent`

`save_consent=on` means save the scopes the resource owner's consented to.

Saving consent requires prior configuration. Learn more in [Store consent decisions](oauth2-manage-consent.html#store-consent-decisions).

## `scope`

A string specifying the permissions the client application requests from the resource owner. Separate scopes with spaces.

Some grants, such as the authorization code grant, do not call the token endpoint with the scope. The scope is defined in the authorization code. Learn more in the documentation for the flow under [OAuth 2.0 grant flows](oauth2-implementing-flows.html).

Default: The default scopes specified in the client profile or the OAuth 2.0 provider configuration.

## `service`

A string naming the journey to authenticate the resource owner.

Default: The default authentication journey for the realm.

Learn more in [Authentication parameters](../am-authentication/authn-from-browser.html#authn-from-browser-parameters).

## `state`

A string value to maintain state between the request and the callback.

During authentication, the client sends this parameter to the authorization server. The authorization server sends it back unchanged in the response.

Use the value to ensure the response belongs to the user who initiated the requests. This mitigates against CSRF attacks.

Use a base64-encoded string of data that is unique to a user and to this request.

## `subject_token`

The original token to exchange in [Token exchange](token-exchange.html).

## `subject_token_type`

The type of the subject token:

* `urn:ietf:params:oauth:token-type:access_token`

* `urn:ietf:params:oauth:token-type:id_token`

## `ui_locales`

A string indicating the end user's preferred languages for the user interface. [OIDC flows](https://openid.net/specs/openid-connect-core-1_0.html) only.

The `ui_locales` parameter is a space-separated list ordered by preference; for example, `en fr-CA fr`.

---

---
title: OAuth 2.0 endpoints
description: OAuth 2.0 authorization server endpoints for client applications, including authorization, token, device flow, token revocation, and token introspection endpoints
component: pingam
version: 8.1
page_id: pingam:am-oauth2:oauth2-client-endpoints
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oauth2/oauth2-client-endpoints.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "Endpoints", "Authorization", "Clients", "REST API"]
page_aliases: ["oauth2-guide:oauth2-client-endpoints.adoc"]
---

# OAuth 2.0 endpoints

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

For reference documentation on related endpoints, refer to:

* [OAuth 2.0 administration REST endpoints](oauth2-admin-endpoints.html)

* [OpenID Connect 1.0 endpoints](../am-oidc1/oidc-client-endpoints.html)

* [UMA endpoints](../uma/uma-endpoints.html)