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