---
title: /json/token/macaroon
description: Inspect and add caveats to macaroon tokens using the token manipulation endpoint
component: pingoneaic
page_id: pingoneaic:am-oauth2:oauth2-introspect-macaroon-endpoint
canonical_url: https://docs.pingidentity.com/pingoneaic/am-oauth2/oauth2-introspect-macaroon-endpoint.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "OpenID Connect (OIDC)", "Endpoints", "Macaroons", "Scope"]
page_aliases: ["oauth2-guide:varlist-oauth2-introspect-macaroon-endpoint.adoc", "oauth2-guide:oauth2-introspect-macaroon-endpoint.adoc"]
---

# /json/token/macaroon

The `/json/token/macaroon` endpoint lets you inspect and manipulate [macaroon tokens](oauth2-macaroons.html).

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
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/token/macaroon?action=restrict'
{
  "macaroon": "<restricted-macaroon-token>"
}

$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "cache-control: no-cache" \
--data '{"macaroon": "<restricted-macaroon-token>"}' \
'https://<tenant-env-fqdn>_/am/json/realms/root/realms/alpha/token/macaroon?_action=inspect'
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
description: Exchange authorization codes and other grants for access tokens using token endpoint
component: pingoneaic
page_id: pingoneaic:am-oauth2:oauth2-access_token-endpoint
canonical_url: https://docs.pingidentity.com/pingoneaic/am-oauth2/oauth2-access_token-endpoint.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
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
https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/access_token
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
| `cnf_key`               | A base64-encoded JSON Web Key (JWK); do not use with `client_secret`.                                                     | Yes, for [JWK-based proof-of-possession](oauth2-PoP-JWK.html)                      |
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
description: Obtain resource owner consent and authorization using OAuth 2.0 authorization endpoint
component: pingoneaic
page_id: pingoneaic:am-oauth2:oauth2-authorize-endpoint
canonical_url: https://docs.pingidentity.com/pingoneaic/am-oauth2/oauth2-authorize-endpoint.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
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
https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/authorize
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

| HTTP status        | Description                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `302 Found`        | Success. Advanced Identity Cloud redirects the resource owner's browser to the `redirect_uri`, appending the authorization code (or token, for the implicit grant) and any `state` value as query parameters.                                                                                                                                                                                                            |
| `400 Bad Request`  | The request is malformed. For example, a required parameter is missing or an unsupported value is supplied.                                                                                                                                                                                                                                                                                                              |
| `401 Unauthorized` | Advanced Identity Cloud could not authenticate the resource owner or the client.	When an error occurs at the authorization endpoint, Advanced Identity Cloud returns 401 rather than redirecting to the client's redirect\_uri with an error parameter as described in RFC 6749. This behavior is intentional and provides additional security by not disclosing error details to potentially unvalidated redirect URIs. |

---

---
title: /oauth2/bc-authorize
description: Initiate backchannel authorization for client-initiated backchannel authentication flows
component: pingoneaic
page_id: pingoneaic:am-oauth2:oauth2-bc-authorize-endpoint
canonical_url: https://docs.pingidentity.com/pingoneaic/am-oauth2/oauth2-bc-authorize-endpoint.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "Endpoints", "Authorization", "REST API"]
page_aliases: ["oauth2-guide:oauth2-bc-authorize-endpoint.adoc"]
section_ids:
  request_parameters: Request parameters
  responses: Responses
---

# /oauth2/bc-authorize

The `/oauth2/bc-authorize` endpoint is the backchannel authorization endpoint for [OpenID Connect Client-Initiated Backchannel Authentication Flow - Core 1.0](https://openid.net/specs/openid-client-initiated-backchannel-authentication-core-1_0.html).

Use this endpoint to initiate backchannel authorization with the resource owner with the following flow:

* Backchannel request grant ([OpenID Connect](../am-oidc1/openid-connect-backchannel-request-flow.html))

Specify the realm in the request URL; for example:

```none
https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/bc-authorize
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
description: Request device and user codes for input-constrained devices using RFC 8628 device authorization
component: pingoneaic
page_id: pingoneaic:am-oauth2:rest-api-oauth2-device-code
canonical_url: https://docs.pingidentity.com/pingoneaic/am-oauth2/rest-api-oauth2-device-code.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "API Explorer", "Endpoints"]
page_aliases: ["oauth2-guide:rest-api-oauth2-device-code.adoc"]
---

# /oauth2/device/code

The [Device authorization grant](oauth2-device-flow.html) endpoint defined in RFC 8628 [OAuth 2.0 Device Authorization Grant](https://www.rfc-editor.org/info/rfc8628).

Client devices use this endpoint in the following flows to get the codes and information required to obtain the resource owner's consent for device access:

* Device flow ([OAuth 2.0](oauth2-device-flow.html))

* Device flow with PKCE ([OAuth 2.0](oauth2-device-flow-pkce.html))

Specify the realm in the request URL; for example:

```none
https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/device/code
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
description: Obtain resource owner consent for device flow authorization using device user endpoint
component: pingoneaic
page_id: pingoneaic:am-oauth2:rest-api-oauth2-device-user
canonical_url: https://docs.pingidentity.com/pingoneaic/am-oauth2/rest-api-oauth2-device-user.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "API Explorer", "Endpoints", "PKCE"]
page_aliases: ["oauth2-guide:rest-api-oauth2-device-user.adoc"]
---

# /oauth2/device/user

This is the [Device authorization grant](oauth2-device-flow.html) endpoint for user interaction.

Client devices use this endpoint to confirm the resource owner's consent in the following flows:

* Device flow ([OAuth 2.0](oauth2-device-flow.html))

* Device flow with PKCE ([OAuth 2.0](oauth2-device-flow-pkce.html))

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
description: Retrieve token metadata including scopes and expiry time using RFC 7662 token introspection
component: pingoneaic
page_id: pingoneaic:am-oauth2:oauth2-introspect-endpoint
canonical_url: https://docs.pingidentity.com/pingoneaic/am-oauth2/oauth2-introspect-endpoint.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "Endpoints", "Scope", "JWT", "Grant Flow", "REST API"]
page_aliases: ["oauth2-guide:varlist-oauth2-introspect-endpoint.adoc", "oauth2-guide:oauth2-introspect-endpoint.adoc"]
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
https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/introspect
```

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

## Introspection requirements

A client can only introspect a token if it meets one of the following requirements:

* Has a special scope

  The client has a [special introspection scope](oauth2-scopes.html#special-oauth2-scopes) (`am-introspect-all-tokens` or `am-introspect-all-tokens-any-realm`) specified in its client profile.

* Token was issued to the client (server-side tokens)

  For server-side tokens, Advanced Identity Cloud compares the `clientID` field stored in the token against the `client_id` of the client. If they match, the client can introspect the token.

  By default, the `clientID` field is set to the client that originally requested the token.

* Token audience includes the client (client-side tokens)

  For client-side tokens, Advanced Identity Cloud checks if the `client_id` of the client is present in the `aud` (audience) claim. If there's a match, the client can introspect the token.

  By default, the `aud` claim is set to the client that originally requested the token.

### Special tokens

To introspect macaroon access tokens containing third-party caveats, use the `X-Discharge-Macaroon` header to pass the discharge macaroon.

## Response signing and encryption

The default introspection response is a plain JSON object.

Advanced Identity Cloud also supports signed JWT (JSON Web Token) or signed and encrypted JWT introspection responses, as defined in [RFC 9701: JWT Response for OAuth Token Introspection](https://www.rfc-editor.org/info/rfc9701).

Regardless of the configured response format, a client can request a signed JWT response by adding one of the following headers to the introspection request:

* `Accept:application/jwt` (default, for compatibility with older clients)

* `Accept: application/token-introspection+jwt` (for compatibility with [RFC 9701](#rfc-9701-token-introspection-claim))

To enable signing and encryption for all requests to a client, follow these steps:

1. In the Advanced Identity Cloud admin console, go to Applications > *Client ID* > Sign On > General Settings > Show advanced settings > Endpoint Response Formats and select the response type in the Token Inspection Response Format list.

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

## RFC 9701 token\_introspection claim

By default, Advanced Identity Cloud returns a flat JWT introspection response for backwards compatibility with older clients. To comply with RFC 9701, enable the Use token\_introspection claim for JWT setting.

To enable the `token_introspection` claim, you can configure it at two levels:

* **Realm level**: Under Native Consoles > Access Management, go to Realms > *realm name* > Services > OAuth2 Provider > Advanced, and select Use token\_introspection claim for JWT.

* **Client level**: Under Native Consoles > Access Management, go to Realms > *realm name* > Applications > OAuth 2.0 > *client ID* > OAuth2 Provider Overrides. Enable OAuth2 Provider Overrides, then select Use token\_introspection claim for JWT.

When enabled, Advanced Identity Cloud wraps the introspected token's claims inside a `token_introspection` claim in the JWT. This separates the JWT's own top-level claims (such as `iss`, `aud`, and `iat` for the introspection response itself) from the introspected token's claims:

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

|   |                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For backwards compatibility, this setting is disabled by default. Enable it when your resource servers are ready to consume RFC 9701-compliant responses. |

## Response content

The following table describes fields you may find in the introspection response:

| Field        | Description                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `active`     | Whether the token is active (`true`) or not (`false`).                                                                                                                                                                                                                                                                                                                                                                           |
| `auth_level` | The authentication level for the resource owner who granted access to the token.                                                                                                                                                                                                                                                                                                                                                 |
| `client_id`  | The client the token was issued to.                                                                                                                                                                                                                                                                                                                                                                                              |
| `cnf`        | The confirmation key claim.The `jwk` type contains the decoded JWK for the access token in the [JWK-based proof-of-possession](oauth2-PoP-JWK.html) flow.                                                                                                                                                                                                                                                                        |
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
description: Push authorization request payloads to authorization server for early client authentication
component: pingoneaic
page_id: pingoneaic:am-oauth2:oauth2-par-endpoint
canonical_url: https://docs.pingidentity.com/pingoneaic/am-oauth2/oauth2-par-endpoint.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
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
https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/par
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
| `redirect_uri`          | The URI to return the resource owner to after authorization is complete.The value must match a redirect URI pre-registered for the client. Advanced Identity Cloud doesn't currently support per-request unregistered redirect URIs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | No                                                                                                                                  |
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
description: Revoke OAuth 2.0 access tokens and refresh tokens using RFC 7009 token revocation endpoint
component: pingoneaic
page_id: pingoneaic:am-oauth2:oauth2-token-revoke-endpoint
canonical_url: https://docs.pingidentity.com/pingoneaic/am-oauth2/oauth2-token-revoke-endpoint.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "Scopes", "Grant Flow", "Endpoints", "Setup &amp; Configuration"]
page_aliases: ["oauth2-guide:varlist-oauth2-token-revoke-endpoint.adoc", "oauth2-guide:oauth2-token-revoke-endpoint.adoc"]
section_ids:
  request_parameters: Request parameters
  responses: Responses
---

# /oauth2/token/revoke

Endpoint defined in RFC 7009 [Token Revocation](https://www.rfc-editor.org/info/rfc7009) to revoke access tokens and refresh tokens.

When you revoke a refresh token, you revoke all tokens issued with the same authorization grant. If you obtained multiple access tokens for a single user with different authorization grants, you must revoke the tokens separately to invalidate each one.

Specify the realm in the request URL; for example:

```none
https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/token/revoke
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
--data "token=refresh-token" \
"https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/token/revoke"
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
title: /oauth2/tokeninfo (Legacy)
description: Deprecated. Legacy OAuth 2.0 endpoints maintained for backward compatibility with existing clients
component: pingoneaic
page_id: pingoneaic:am-oauth2:legacy-oauth2-endpoints
canonical_url: https://docs.pingidentity.com/pingoneaic/am-oauth2/legacy-oauth2-endpoints.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "Endpoints", "Administration"]
page_aliases: ["oauth2-guide:legacy-oauth2-endpoints.adoc"]
---

# /oauth2/tokeninfo (Legacy)

Advanced Identity Cloud exposes the legacy `/oauth2/tokeninfo` endpoint.

|   |                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------- |
|   | Use this endpoint only when you can't use the standard [/oauth2/introspect](oauth2-introspect-endpoint.html) endpoint. |

Use this endpoint to validate tokens and retrieve token metadata to determine how to respond to requests for protected resources.

To inspect the contents of the token, send an HTTP GET request to:

```none
https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/realm/tokeninfo
```

Use the token as a bearer token in an authorization header; for example, `Authorization: Bearer <access-token>`.

---

---
title: /realm-config/agents/OAuth2Client
description: Create, list, and delete OAuth 2.0 clients programmatically using admin endpoint
component: pingoneaic
page_id: pingoneaic:am-oauth2:rest-api-oauth2-client-admin-endpoint
canonical_url: https://docs.pingidentity.com/pingoneaic/am-oauth2/rest-api-oauth2-client-admin-endpoint.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "API Explorer", "Administration", "Endpoints", "Clients"]
page_aliases: ["oauth2-guide:rest-api-oauth2-client-admin-endpoint.adoc"]
section_ids:
  create-oauth2-client: Create an OAuth 2.0 client
  update-oauth2-clients: Update an OAuth 2.0 client
  query-oauth2-clients: Query OAuth 2.0 clients
  delete_an_oauth_2_0_client: Delete an OAuth 2.0 client
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
description: List and revoke OAuth 2.0 tokens for resource owners across multiple client applications
component: pingoneaic
page_id: pingoneaic:am-oauth2:rest-api-oauth2-applications-endpoint
canonical_url: https://docs.pingidentity.com/pingoneaic/am-oauth2/rest-api-oauth2-applications-endpoint.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "API Explorer", "Endpoints", "Clients"]
page_aliases: ["oauth2-guide:rest-api-oauth2-applications-endpoint.adoc"]
section_ids:
  list_clients_with_active_tokens: List clients with active tokens
  delete_tokens_for_a_client: Delete tokens for a client
---

# /users/user/oauth2/applications

Invoke this Advanced Identity Cloud-specific endpoint to list the applications granted OAuth 2.0 access and to delete tokens for a specified client. This lets you manage the tokens granted to applications on behalf of a resource owner.

For example, you can revoke all tokens for a resource owner across all clients after a password change or a suspected account compromise. To do this:

1. Query the applications endpoint to list all clients with active tokens for the resource owner.

2. Delete the tokens for each client returned.

|   |                                                                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This approach revokes all tokens held by each client for the specified resource owner. If you want to revoke a single known access token or refresh token, use the [/oauth2/token/revoke](oauth2-token-revoke-endpoint.html) endpoint instead. |

To call the endpoint, you must compose the path to the realm where the client is registered.

## List clients with active tokens

This example lists all the OAuth 2.0 clients holding active tokens granted in the `alpha` realm for the resource owner, `bjensen`. You must provide the SSO token of the tenant administrator or the resource owner as a header, and include the `_id` of the resource owner (`bjensen`) in the URL:

```bash
$  curl --request GET \
--header "Accept-API-Version: resource=1.1" \
--header "<session-cookie-name>: Ua6fsH2vjgHqVY..." \
"https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/users/1dff18dc-ac57-4388-8127-dff309f80002/oauth2/applications?_queryFilter=true"
```

On success, Advanced Identity Cloud returns an HTTP 200 code and a JSON object describing each OAuth 2.0 client that currently holds at least one active access or refresh token for the specified resource owner. For example:

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

The following example deletes all tokens held by the OAuth 2.0 client `myClient` granted in the `alpha` realm by `bjensen`. You must provide the SSO token of the tenant administrator or the resource owner as a header, and include the `_id` of the resource owner (`bjensen`) and `_id` of the client (`myClient`) in the URL:

```bash
$ curl --request DELETE \
--header "Accept-API-Version: resource=1.1" \
--header "<session-cookie-name>: Ua6fsH2vjgHqVY..." \
"https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/users/1dff18dc-ac57-4388-8127-dff309f80002/oauth2/applications/myClient"
```

On success, Advanced Identity Cloud returns an HTTP 200 code and a JSON object with information about the deleted tokens, such as the granted scopes and ID of the client. For example:

```json
{
    "_id": "myClient",
    "_rev": "-1121350941",
    "name": "My client name",
    "scopes": {
        "write": "write"
    },
    "expiryDateTime": "2027-04-23T16:40:55.000Z",
    "logoUri": null
}
```

Repeat this request for each client `_id` returned when you queried the applications endpoint to delete all tokens for the resource owner across all clients.

---

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

1. [Create a resource owner profile](../identities/manage-identities.html#create_a_user_profile) and record the username and password.

2. Update the following settings in the new user profile and save your work:

   * Email Address

     `user@example.com`

   * Telephone Number

     `(555) 323-1234`

#### Create the script

1. In the Advanced Identity Cloud admin console, [create a script](../developer-docs/scripting-auth.html#create-a-new-auth-script) of type OAuth2 Access Token Modification.

2. Replace the default JavaScript with the following script:

   ```javascript
   (function () {
     // Add a field next to the access token in the /oauth2/access_token response.
     accessToken.addExtraData('hello', 'world');

     // Add identity profile attribute values to the /oauth2/introspect response.
     accessToken.setField('mail', identity.getAttribute('mail'));
     accessToken.setField('phone', identity.getAttribute('telephoneNumber').toArray()[0]);

     // No return value is expected.
   }());
   ```

   The `accessToken` methods update the access token before Advanced Identity Cloud issues it.

   The `identity` methods get attribute values from the resource owner's profile.

   Learn more in the [Access token modification scripting API](../am-scripting/access-token-modification-api.html).

#### Use the script

The OAuth 2.0 client profile in this example overrides the OAuth 2.0 provider settings. This lets you test the script without affecting access tokens issued to other clients.

1. [Create an OIDC/ OAuth 2.0 web client application](../app-management/register-a-custom-application.html#register_a_custom_application_or_service) with the following settings:

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

  The script added `"hello": "world"` alongside the access token in the [/oauth2/access\_token](oauth2-access_token-endpoint.html) response.

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

1. [Create a resource owner profile](../identities/manage-identities.html#create_a_user_profile) and record the username and password.

#### Create the script

Write a script that does the following:

* Calls an external API to set values for browser and IP in the access token

* Sets a new expiry time in the access token and in the resource owner's profile data

* Generates random UUIDs to return in the JSON response

1. Under Native Consoles > Access Management, go to Realms > *Realm Name* > Scripts, and click +New Script.

2. Provide a suitable name for your script and select the following values:

   * Script Type

     `OAuth2 Access Token Modification`

   * Evaluator Version

     `Next Generation`

3. Click Create.

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

1. [Create an OIDC/ OAuth 2.0 web client application](../app-management/register-a-custom-application.html#register_a_custom_application_or_service) with the following settings:

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

* In the Advanced Identity Cloud admin console, select Scripts > Auth Scripts > OAuth2 Access Token Modification Script, and replace the script content with your validated script.

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

For more information about configuring Advanced Identity Cloud as an OAuth 2.0 client, refer to [Social authentication](../self-service/social-registration.html).

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

  * [/oauth2/access\_token](oauth2-access_token-endpoint.html)

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

1. [Create an application owner profile](../identities/manage-identities.html#create_a_user_profile) and record the username and password.

2. [Register a client application](../app-management/register-a-custom-application.html).

   1. In the Advanced Identity Cloud admin console, go to Applications and select + Custom Application.

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

3. [Create a resource owner profile](../identities/manage-identities.html#create_a_user_profile) and record the username and password.

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

As the client, call the [/oauth2/access\_token](oauth2-access_token-endpoint.html) endpoint to exchange the authorization code for an access token. Provide the following parameters:

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

  * [/oauth2/access\_token](oauth2-access_token-endpoint.html)

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

1. [Create an application owner profile](../identities/manage-identities.html#create_a_user_profile) and record the username and password.

2. [Register a client application](../app-management/register-a-custom-application.html).

   1. In the Advanced Identity Cloud admin console, go to Applications and select + Custom Application.

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

   1. Under Native Consoles > Access Management, go to Services > OAuth2 Provider and switch to the Advanced tab.

   2. Set PAR Request URI Lifetime to a value sufficient to cover the duration of the PAR request.

      For more information, refer to [PAR Request URI Lifetime](../am-reference/services-configuration.html#par-request-uri-lifetime).

   3. Save your changes.

4. [Create a resource owner profile](../identities/manage-identities.html#create_a_user_profile) and record the username and password.

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

As the client, call the [/oauth2/access\_token](oauth2-access_token-endpoint.html) endpoint to exchange the authorization code for an access token. Provide the following parameters:

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

  * [/oauth2/access\_token](oauth2-access_token-endpoint.html)

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

1. [Create an application owner profile](../identities/manage-identities.html#create_a_user_profile) and record the username and password.

2. [Register a client application](../app-management/register-a-custom-application.html).

   1. In the Advanced Identity Cloud admin console, go to Applications and select + Custom Application.

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

3. [Create a resource owner profile](../identities/manage-identities.html#create_a_user_profile) and record the username and password.

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

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The `Code Verifier Parameter Required` setting (under Native Consoles > Access Management > Realms > *Realm Name* > Services > OAuth2 Provider > Advanced) specifies whether Advanced Identity Cloud requires clients to include a code verifier in their calls.However, if a client makes a call to Advanced Identity Cloud with the `code_challenge` parameter, Advanced Identity Cloud honors the code exchange regardless of the value of `Code Verifier Parameter Required`. For more information, refer to [Authorization server configuration](oauth2-configure-authz.html). |

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

     |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
     | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | The `Code Verifier Parameter Required` setting (under Native Consoles > Access Management > Realms > *Realm Name* > Services > OAuth2 Provider > Advanced) specifies whether Advanced Identity Cloud requires clients to include a code verifier in their calls.However, if a client makes a call to Advanced Identity Cloud with the `code_challenge` parameter, Advanced Identity Cloud honors the code exchange regardless of the value of `Code Verifier Parameter Required`. For more information, refer to [Authorization server configuration](oauth2-configure-authz.html). |

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

As the client, call the [/oauth2/access\_token](oauth2-access_token-endpoint.html) endpoint to exchange the authorization code for an access token. Provide the following parameters:

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

1. Go to Applications > *Name* > Sign On > General Settings > Advanced > Authentication.

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
title: Authorization server configuration
description: Configure Advanced Identity Cloud as an OAuth 2.0 authorization server for client and admin endpoints
component: pingoneaic
page_id: pingoneaic:am-oauth2:oauth2-configure-authz
canonical_url: https://docs.pingidentity.com/pingoneaic/am-oauth2/oauth2-configure-authz.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "Endpoints", "Authorization", "Setup &amp; Configuration"]
page_aliases: ["oauth2-guide:oauth2-configure-authz.adoc"]
section_ids:
  oauth2-configuration-options: Additional configuration options
---

# Authorization server configuration

Configure the OAuth 2.0 provider service to expose the [OAuth 2.0 endpoints](oauth2-client-endpoints.html) and [OAuth 2.0 administration endpoints](oauth2-admin-endpoints.html).

1. Under Native Consoles > Access Management, go to Realms > *Realm Name* > Services > OAuth2 Provider.

2. On the OAuth 2.0 provider page, select the Advanced tab.

3. Configure the Grant Types that clients will be able to use to request access, refresh, and ID tokens. For a list of supported grant types, refer to [OAuth 2.0 grant flows](oauth2-implementing-flows.html) and [OpenID Connect grant flows](../am-oidc1/oidc-implementing-flows.html).

   |   |                                                                                                     |
   | - | --------------------------------------------------------------------------------------------------- |
   |   | Although UMA is on the grant types list, UMA is not currently supported in Advanced Identity Cloud. |

4. Configure Persistent Claims.

   *Persistence* lets you retain custom claims when you refresh an access token.

   In the Persistent Claims field, enter the claims that must be persisted between tokens. When an access token is refreshed, any claims that are listed here will be on the new token.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | * These claims are added before the access token modification script, allowing you to manipulate them in the modification script. For example, if a token has a claim called `hostname` that you want to be persisted when the token is refreshed, you could add that claim to the Persistent Claims list. You could then modify the script to persist that `hostname` in the new token, if it exists, or to add a hostname to the new token, if it does not exist.

   * Only custom, non-standard claims can be persisted. Standard claims, such as `scope` (defined in the OAuth 2.0 specification) and `auditTrackingId` (defined by default in Advanced Identity Cloud) cannot be persisted. |

## Additional configuration options

The OAuth 2.0 provider is highly configurable:

* To configure the OAuth 2.0 provider, go to Native Consoles > Access Management, then to Realms > *Realm Name* > Services > OAuth2 Provider.

The following table describes the high-level configuration of the OAuth 2.0 provider service. For more details, refer to the [OAuth2 Provider reference](../am-reference/services-configuration.html#realm-oauth-oidc).

**OAuth 2.0 provider configuration options**

| Task                                                                                                                                                                                                                                                                                                                                                                                                       | Resources                                                                         |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **Configure the authorization server to issue refresh tokens**Learn why refresh tokens are useful in your environment, how to configure Advanced Identity Cloud to issue them, and how to request them.                                                                                                                                                                                                    | [Refresh tokens](oauth2-refresh-tokens.html)                                      |
| **Adjust the lifetimes of tokens and codes**If necessary, adjust the lifetimes for authorization codes (a lifetime of 10 minutes or less is [recommended in RFC 6749](https://www.rfc-editor.org/rfc/rfc6749.html#section-4.1.2)), access tokens, and refresh tokens.Configure them on the Core tab of the provider.                                                                                       | N/A                                                                               |
| **Configure the OAuth 2.0 service to provide scopes dynamically**The OAuth 2.0 provider can leverage the Advanced Identity Cloud Authorization service to grant or deny scopes dynamically.                                                                                                                                                                                                                | [Dynamic OAuth 2.0 authorization](../am-authorization/oauth2-authorization.html)  |
| **Decide how scopes appear in the consent pages**To change how scopes appear, configure the Client Registration Scope Allowlist field on the Advanced tab of the OAuth 2.0 provider.Define each scope as a string that represents the internal scope name, optionally followed by a `\|locale` and a `\|localized description`.For example: `read\|en\|Permission to view email messages in your account`. | [Scopes](oauth2-scopes.html)                                                      |
| **Decide how to manage consent**You can:- Allow users to save consent so the OAuth 2.0 provider remembers their consented scopes.

- Allow clients to skip consent so no consent page is displayed to the resource owners.

- Allow clients to revoke consent.                                                                                                                                             | [Manage consent](oauth2-manage-consent.html)                                      |
| **Configure a remote consent server**This is useful, for example, when your environment must hand off the consent-gathering part of the OAuth 2.0 flows to a separate service.                                                                                                                                                                                                                             | [Remote consent service](oauth2-remote-consent.html)                              |
| **Configure OpenID-Connect specific options**                                                                                                                                                                                                                                                                                                                                                              | [OIDC provider configuration](../am-oidc1/configure-openid-connect-provider.html) |