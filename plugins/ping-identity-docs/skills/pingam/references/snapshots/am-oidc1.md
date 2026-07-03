---
title: /.well-known/webfinger
description: Discover the OpenID provider for an end user using the WebFinger endpoint in PingAM
component: pingam
version: 8.1
page_id: pingam:am-oidc1:rest-api-oidc-discovery-webfinger
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oidc1/rest-api-oidc-discovery-webfinger.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OpenID Connect (OIDC)", "Standards", "Endpoints"]
page_aliases: ["oidc1-guide:rest-api-oidc-discovery-webfinger.adoc"]
section_ids:
  supported_parameters: Supported parameters
  example: Example
---

# /.well-known/webfinger

The `/.well-known/webfinger` endpoint is described in [OpenID Connect Discovery 1.0 incorporating errata set 1](https://openid.net/specs/openid-connect-discovery-1_0.html).

Use it to discover the OpenID provider for an end user.

*Do not* specify the realm in the request URL; for example:

```none
https://am.example.com:8443/am/.well-known/webfinger
```

This endpoint is disabled by default. For details, refer to [OIDC discovery](oidc-am-provider.html#configure-openid-connect-discovery).

## Supported parameters

The discovery endpoint supports the following parameters:

| Parameter  | Description                                                                                                                                                                                                                                                                                                                                                                  | Required                                              |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| `realm`    | The AM realm to query for the user profile.                                                                                                                                                                                                                                                                                                                                  | No                                                    |
| `rel`      | The URI identifying the type of service.                                                                                                                                                                                                                                                                                                                                     | Yes; use `http://openid.net/specs/connect/1.0/issuer` |
| `resource` | The URL-encoded subject of the request.; one of:`acct:user-email` `acct:user-email@host` `http(s)://host/username` `http(s)://host:port`The `host` relates to the discovery URL. For example, if the endpoint is `http://server.example.com/am/.well-known/webfinger`, the host is `server.example.com`.The `resource` parameter does not support wildcard characters (`*`). | Yes                                                   |

## Example

```bash
$ curl \
'https://am.example.com:8443/am/.well-known/webfinger?resource=acct%3Abjensen%40example.com&rel=http%3A%2F%2Fopenid.net%2Fspecs%2Fconnect%2F1.0%2Fissuer'
{
  "subject": "acct:bjensen@example.com",
  "links": [{
    "rel": "http://openid.net/specs/connect/1.0/issuer",
    "href": "https://am.example.com:8443/am/oauth2/realms/root/realms/alpha"
  }]
}
```

---

---
title: /oauth2/.well-known/openid-configuration
description: Discover OpenID Connect provider configuration settings including supported algorithms, endpoints, and grant types from PingAM
component: pingam
version: 8.1
page_id: pingam:am-oidc1:rest-api-oidc-discovery-configuration
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oidc1/rest-api-oidc-discovery-configuration.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OpenID Connect (OIDC)", "Standards", "Endpoints", "Setup &amp; Configuration"]
page_aliases: ["oidc1-guide:rest-api-oidc-discovery-configuration.adoc"]
---

# /oauth2/.well-known/openid-configuration

The OpenID provider configuration endpoint is defined in [OpenID Connect Discovery 1.0](https://openid.net/specs/openid-connect-discovery-1_0.html).

Use this to discover the provider settings. For details, refer to [OIDC discovery](oidc-am-provider.html#configure-openid-connect-discovery).

Specify the realm in the request URL; for example:

```bash
$ curl https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/.well-known/openid-configuration
```

> **Collapse: Show output**
>
> ```json
> {
>   "request_parameter_supported": true,
>   "pushed_authorization_request_endpoint": "https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/par",
>   "introspection_encryption_alg_values_supported": ["ECDH-ES+A256KW", "ECDH-ES+A192KW", "RSA-OAEP", "ECDH-ES+A128KW", "RSA-OAEP-256", "A128KW", "A256KW", "ECDH-ES", "dir", "A192KW"],
>   "claims_parameter_supported": false,
>   "introspection_endpoint": "https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/introspect",
>   "issuer": "https://am.example.com:8443/am/oauth2/realms/root/realms/alpha",
>   "id_token_encryption_enc_values_supported": ["A256GCM", "A192GCM", "A128GCM", "A128CBC-HS256", "A192CBC-HS384", "A256CBC-HS512"],
>   "userinfo_encryption_enc_values_supported": ["A256GCM", "A192GCM", "A128GCM", "A128CBC-HS256", "A192CBC-HS384", "A256CBC-HS512"],
>   "authorization_endpoint": "https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/authorize",
>   "authorization_encryption_alg_values_supported": ["ECDH-ES+A256KW", "ECDH-ES+A192KW", "RSA-OAEP", "ECDH-ES+A128KW", "RSA-OAEP-256", "A128KW", "A256KW", "ECDH-ES", "dir", "A192KW"],
>   "introspection_encryption_enc_values_supported": ["A256GCM", "A192GCM", "A128GCM", "A128CBC-HS256", "A192CBC-HS384", "A256CBC-HS512"],
>   "claims_supported": [],
>   "rcs_request_signing_alg_values_supported": ["PS384", "ES384", "RS384", "HS256", "HS512", "ES256", "RS256", "HS384", "ES512", "PS256", "PS512", "RS512"],
>   "token_endpoint_auth_methods_supported": ["client_secret_post", "private_key_jwt", "self_signed_tls_client_auth", "tls_client_auth", "none", "client_secret_basic"],
>   "tls_client_certificate_bound_access_tokens": true,
>   "response_modes_supported": ["fragment", "jwt", "form_post.jwt", "form_post", "fragment.jwt", "query", "query.jwt"],
>   "backchannel_logout_session_supported": true,
>   "token_endpoint": "https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/access_token",
>   "response_types_supported": ["code token id_token", "code", "code id_token", "device_code", "id_token", "code token", "token", "token id_token"],
>   "authorization_encryption_enc_values_supported": ["A256GCM", "A192GCM", "A128GCM", "A128CBC-HS256", "A192CBC-HS384", "A256CBC-HS512"],
>   "revocation_endpoint_auth_methods_supported": ["client_secret_post", "private_key_jwt", "self_signed_tls_client_auth", "tls_client_auth", "none", "client_secret_basic"],
>   "request_uri_parameter_supported": true,
>   "grant_types_supported": ["implicit", "urn:ietf:params:oauth:grant-type:saml2-bearer", "refresh_token", "password", "client_credentials", "urn:ietf:params:oauth:grant-type:device_code", "authorization_code", "urn:openid:params:grant-type:ciba", "urn:ietf:params:oauth:grant-type:uma-ticket", "urn:ietf:params:oauth:grant-type:jwt-bearer"],
>   "version": "3.0",
>   "userinfo_endpoint": "https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/userinfo",
>   "require_request_uri_registration": true,
>   "code_challenge_methods_supported": ["plain", "S256"],
>   "id_token_encryption_alg_values_supported": ["ECDH-ES+A256KW", "ECDH-ES+A192KW", "RSA-OAEP", "ECDH-ES+A128KW", "RSA-OAEP-256", "A128KW", "A256KW", "ECDH-ES", "dir", "A192KW"],
>   "authorization_signing_alg_values_supported": ["PS384", "RS384", "EdDSA", "ES384", "HS256", "HS512", "ES256", "RS256", "HS384", "ES512", "PS256", "PS512", "RS512"],
>   "request_object_signing_alg_values_supported": ["PS384", "ES384", "RS384", "HS256", "HS512", "ES256", "RS256", "HS384", "ES512", "PS256", "PS512", "RS512"],
>   "request_object_encryption_alg_values_supported": ["ECDH-ES+A256KW", "ECDH-ES+A192KW", "ECDH-ES+A128KW", "RSA-OAEP", "RSA-OAEP-256", "A128KW", "A256KW", "ECDH-ES", "dir", "A192KW"],
>   "rcs_response_signing_alg_values_supported": ["PS384", "ES384", "RS384", "HS256", "HS512", "ES256", "RS256", "HS384", "ES512", "PS256", "PS512", "RS512"],
>   "introspection_signing_alg_values_supported": ["PS384", "RS384", "EdDSA", "ES384", "HS256", "HS512", "ES256", "RS256", "HS384", "ES512", "PS256", "PS512", "RS512"],
>   "check_session_iframe": "https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/connect/checkSession",
>   "scopes_supported": ["address", "phone", "openid", "profile", "fr:idm:*", "am-introspect-all-tokens", "email"],
>   "backchannel_logout_supported": true,
>   "acr_values_supported": [],
>   "request_object_encryption_enc_values_supported": ["A256GCM", "A192GCM", "A128GCM", "A128CBC-HS256", "A192CBC-HS384", "A256CBC-HS512"],
>   "rcs_request_encryption_alg_values_supported": ["ECDH-ES+A256KW", "ECDH-ES+A192KW", "RSA-OAEP", "ECDH-ES+A128KW", "RSA-OAEP-256", "A128KW", "A256KW", "ECDH-ES", "dir", "A192KW"],
>   "userinfo_signing_alg_values_supported": ["ES384", "HS256", "HS512", "ES256", "RS256", "HS384", "ES512"],
>   "require_pushed_authorization_requests": false,
>   "rcs_response_encryption_enc_values_supported": ["A256GCM", "A192GCM", "A128GCM", "A128CBC-HS256", "A192CBC-HS384", "A256CBC-HS512"],
>   "userinfo_encryption_alg_values_supported": ["ECDH-ES+A256KW", "ECDH-ES+A192KW", "RSA-OAEP", "ECDH-ES+A128KW", "RSA-OAEP-256", "A128KW", "A256KW", "ECDH-ES", "dir", "A192KW"],
>   "end_session_endpoint": "https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/connect/endSession",
>   "rcs_request_encryption_enc_values_supported": ["A256GCM", "A192GCM", "A128GCM", "A128CBC-HS256", "A192CBC-HS384", "A256CBC-HS512"],
>   "revocation_endpoint": "https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/token/revoke",
>   "rcs_response_encryption_alg_values_supported": ["ECDH-ES+A256KW", "ECDH-ES+A192KW", "ECDH-ES+A128KW", "RSA-OAEP", "RSA-OAEP-256", "A128KW", "A256KW", "ECDH-ES", "dir", "A192KW"],
>   "token_endpoint_auth_signing_alg_values_supported": ["PS384", "ES384", "RS384", "HS256", "HS512", "ES256", "RS256", "HS384", "ES512", "PS256", "PS512", "RS512"],
>   "jwks_uri": "https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/connect/jwk_uri",
>   "subject_types_supported": ["public", "pairwise"],
>   "id_token_signing_alg_values_supported": ["PS384", "ES384", "RS384", "HS256", "HS512", "ES256", "RS256", "HS384", "ES512", "PS256", "PS512", "RS512"],
>   "registration_endpoint": "https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/register"
> }
> ```

---

---
title: /oauth2/connect/checkSession
description: Retrieve session state and check end user login status using HTML5 postMessage requests with this OpenID Connect session management endpoint
component: pingam
version: 8.1
page_id: pingam:am-oidc1:rest-api-oidc-checksession-endpoint
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oidc1/rest-api-oidc-checksession-endpoint.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OpenID Connect (OIDC)", "Standards", "Endpoints", "Sessions"]
page_aliases: ["oidc1-guide:rest-api-oidc-checksession-endpoint.adoc"]
---

# /oauth2/connect/checkSession

Use this endpoint to retrieve session state. Learn more in [Session management](session-management.html).

A relying party client creates an invisible iframe with the URL to the endpoint as the `src` attribute of the `iframe` tag. Use the endpoint to accept HTML5 `postMessage` requests from the `iframe`, and to generate `postMessage` requests to the `iframe` with the end user's login status.

*Don't* specify the realm in the request URL. For example:

```none
https://am.example.com:8443/am/oauth2/connect/checkSession
```

---

---
title: /oauth2/connect/endSession
description: Use the end session endpoint to terminate authenticated OpenID Connect sessions and optionally redirect users after logout
component: pingam
version: 8.1
page_id: pingam:am-oidc1:rest-api-oidc-endsession-endpoint
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oidc1/rest-api-oidc-endsession-endpoint.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OpenID Connect (OIDC)", "Standards", "Endpoints", "Sessions"]
page_aliases: ["oidc1-guide:rest-api-oidc-endsession-endpoint.adoc"]
section_ids:
  supported_parameters: Supported parameters
  example: Example
---

# /oauth2/connect/endSession

Use this endpoint to terminate authenticated sessions. Learn more in [Session management](session-management.html).

To find the URL for this endpoint, read the `end_session_endpoint` field of the [well-known configuration endpoint](rest-api-oidc-discovery-configuration.html) for the realm:

```bash
$ curl https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/.well-known/openid-configuration
{
  "…​": "…​",
  "end_session_endpoint": "https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/connect/endSession",
  "…​": "…​"
}
```

## Supported parameters

The end session endpoint supports the following query parameters:

| Parameter                  | Description                                                                                                                                                                                                                                                                                                    | Required                            |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| `client_id`                | Uniquely identifies the application making the request.This parameter is *not* compliant with the specification.                                                                                                                                                                                               | Yes, when the ID token is encrypted |
| `id_token_hint`            | Previously issued ID token identifying the authenticated session.                                                                                                                                                                                                                                              | Yes                                 |
| `post_logout_redirect_uri` | Redirect to this URI after logout.This must match one of the values in the Post Logout Redirect URIs setting of the client profile.By default, this profile setting is empty. To update the setting in the AM admin UI, go to Realms > *realm name* > Applications > OAuth 2.0 > *client ID* > OpenID Connect. | No                                  |

The `post_logout_redirect_uri` parameter determines the result on successful logout:

* If included, AM redirects to the specified location.

* If omitted, AM returns HTTP 204 No Content to indicate the end user logged out.

## Example

AM deletes the authenticated session when the user successfully logs out and is redirected to the post-logout URL:

```bash
$ curl \
--dump-header - \
--request GET \
'https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/connect/endSession?id_token_hint=id-token&post_logout_redirect_uri=https://www.example.com/signout'
HTTP/2 302
…​
location: https://www.example.com/signout
content-length: 0
…​
```

---

---
title: /oauth2/connect/jwk_uri
description: Access public keys exposed by the JWK URI endpoint to verify token signatures and encrypt OIDC ID requests in PingAM OAuth 2.0 and OpenID Connect environments
component: pingam
version: 8.1
page_id: pingam:am-oidc1:managing-jwk_uri
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oidc1/managing-jwk_uri.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OpenID Connect (OIDC)", "Standards", "Setup &amp; Configuration", "Security", "Endpoints"]
page_aliases: ["oidc1-guide:managing-jwk_uri.adoc"]
section_ids:
  obtaining-public-signing-key: Access the keys exposed by the JWK URI endpoint
  oauth2-oidc-digital-signatures: Configure ID token signatures
  deprecating-algorithms: Deprecate algorithms and rotate public keys
  deprecate-algorithms: Deprecate supported algorithms and their keys
  customizing-kids: Customize public key IDs
  kid-multiple-keys: Display every algorithm and key type associated with a key ID
  map-custom-kids: Map custom key IDs to secrets
  override-default-kid-values: Override default kid values
---

# /oauth2/connect/jwk\_uri

Each realm configured for OAuth 2.0 exposes a JSON web key (JWK) URI endpoint that contains public keys that clients can use to:

* Verify the signature of [client-side](../am-oauth2/stateless-stateful-tokens.html#client-side-tokens) access tokens and OIDC ID tokens.

* Encrypt OIDC ID requests to AM sent as a JWT.

> **Collapse: Where do the keys come from?**
>
> By default, the endpoint exposes an internal URI relative to the AM deployment. For example, `openam/oauth2/realms/root/connect/jwk_uri`.
>
> The keys appearing in that URI are those configured in the AM [secret stores](../security/secret-stores.html), regardless of the algorithms configured in the OAuth 2.0 provider. This is to support the process of [deprecating keys and algorithms](#deprecating-algorithms).
>
> Secrets are configured by default; delete the ones you aren't planning to use so that they aren't exposed on the endpoint.
>
> In environments where secrets are centralized, you might want AM to share the URI of your secrets API instead of the local AM endpoint. To set this custom URI, go to Realms > *realm name* > Services > OAuth2 Provider, and add the URI to the Remote JSON Web Key URL field.

Public keys are for asymmetric encryption. *Symmetric* key algorithms, such as direct encryption and AES key wrapping encryption use the client secret, and HMAC-based algorithms use the secret mapped to the `am.services.oauth2.stateless.signing.HMAC` label. Clients don't need to check the JWK URI endpoint for these algorithms.

> **Collapse: The endpoint is exposed, but I haven't configured an OAuth 2.0 provider yet**
>
> Web and Java agents use an internal OAuth 2.0 provider to connect to AM. This provider exposes the endpoint so that agents can access the key configured for the `am.global.services.oauth2.oidc.agent.idtoken.signing` secret label.

|   |                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Configure the [base URL source service](../security/reverse-proxy.html#configure-base-url-source) to change the URL used in the `.well-known` endpoints used in OIDC 1.0 and UMA. |

The following table summarizes the high-level tasks you need to complete to manage the JWK URI endpoint in your environment:

| Task                                                                                                                                                                                                                                                                                                                                                                           | Resources                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------- |
| **Learn where to find and how to query the JWK URI endpoint.**Clients need to find the endpoint to, for example, validate tokens signed by AM.                                                                                                                                                                                                                                 | [Access the keys exposed by the JWK URI endpoint](#obtaining-public-signing-key)    |
| **Control which keys are displayed.**The JWK URI endpoint returns keys based on the secret mappings configured for the relevant OAuth 2.0/OIDC functionality. Therefore, to control which keys are displayed, ensure that you only map the secrets required in your environment.                                                                                               | [Configure ID token signatures](#oauth2-oidc-digital-signatures)                    |
| **Learn how to deprecate algorithms and how to rotate public keys.**You may need to perform these tasks to replace algorithms with more secure ones.                                                                                                                                                                                                                           | [Deprecate algorithms and rotate public keys](#deprecating-algorithms)              |
| **Customize the key ID (`kid`) of the exposed keys.**By default, AM generates a `kid` for each public key exposed in the `jwk_uri` endpoint when AM is configured as an OAuth 2.0 authorization server.You need to customize AM if any exposed keys in your environment need a specific `kid`.                                                                                 | [Customize public key IDs](#customizing-kids)                                       |
| **Decide if the JWK URI endpoint should display duplicated key IDs**By default, each `kid` exposed by the `jwk_uri` endpoint matches a unique secret, as required by the [RFC7517](https://datatracker.ietf.org/doc/html/rfc7517#section-4.5) specification.If you have several algorithms and key types associated with one `kid`, configure AM to display them individually. | [Display every algorithm and key type associated with a key ID](#kid-multiple-keys) |
| **Map custom key IDs to secret aliases**If you provide custom key IDs to sign JWTs, create mappings to guarantee that the `kid` header of the signed JWT references the correct key in your remote JWKS.                                                                                                                                                                       | [Map custom key IDs to secrets](#map-custom-kids)                                   |

## Access the keys exposed by the JWK URI endpoint

Perform the following steps to access the public keys:

1. To find the JWK URI that AM exposes, perform an HTTP GET at `/oauth2/realms/root/.well-known/openid-configuration`.

   For example:

   ```bash
   $ curl https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/.well-known/openid-configuration
   {
     "request_parameter_supported": true,
     "claims_parameter_supported": false,
     "introspection_endpoint": "https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/introspect",
     "check_session_iframe": "https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/connect/checkSession",
     "scopes_supported": [],
     "issuer": "https://am.example.com:8443/am/oauth2/realms/root/realms/alpha",
     "id_token_encryption_enc_values_supported": [
       "A256GCM",
       "A192GCM",
       "A128GCM",
       "A128CBC-HS256",
       "A192CBC-HS384",
       "A256CBC-HS512"
     ],
   …​
     "jwks_uri": "https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/connect/jwk_uri",
     "subject_types_supported": [
       "public"
     ],
   …​
   }
   ```

   By default, AM exposes the JWK URI as an endpoint relative to the deployment URI. For example, `https://am.example.com:8443/am/oauth2/realms/root/connect/jwk_uri`.

   In environments where secrets are centralized, you might want AM to share the URI of your secrets API instead of the local AM endpoint.

   To configure this URI, go to Realms > *realm name* > Services > OAuth2 Provider > Advanced OpenID Connect and add your URI to the Remote JSON Web Key URL field.

2. Perform an HTTP GET at the JWK URI to get the relevant public keys.

   For example:

   ```bash
   $ curl https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/connect/jwk_uri
   {
   "keys":[
         {
            "kty":"EC",
            "kid":"I4x/IijvdDsUZMghwNq2gC/7pYQ=",
            "use":"sig",
            "x5t":"GxQ9K-sxpsH487eSkJ7lE_SQodk",
            "x5c":[
               "MIIB/zCCAYYCCQDS7UWmBdQtETAJ0mN0TZL7/MaY…​"
                  ],
            "x":"k5wSvW_6JhOuCj-9PdDWdEA4oH90RSmC2GTliiUHAhXj6rmTdE2S-_zGmMFxufuV",
            "y":"XfbR-tRoVcZMCoUrkKtuZUIyfCgAy8b0FWnPZqevwpdoTzGQBOXSNi6uItN_o4tH",
            "crv":"P-384"
         },
         …​
      ]
   }
   ```

## Configure ID token signatures

ID tokens are signed by default with a test key configured during installation. Change this key on production-like and production environments.

Perform the steps in this procedure to configure the signing algorithm AM should use to sign OpenID Connect tokens:

1. In the AM admin UI, go to Realms > *realm name* > Services > OAuth2 Provider.

2. In the OpenID Connect tab, ensure that the ID Token Signing Algorithms supported list has the signing algorithms your environment requires.

   AM supports the signing algorithms listed in *JSON Web Algorithms (JWA)*: ["alg" (Algorithm) Header Parameter Values for JWS](https://datatracker.ietf.org/doc/html/draft-ietf-jose-json-web-algorithms#section-3.1).

   Note that the alias mapped to the algorithms are defined in the secret stores, as shown in the table below:

   > **Collapse: Sign OIDC tokens**
   >
   > The following table shows the secret label mapping used to sign OIDC ID tokens and backchannel logout tokens:
   >
   > | Secret label                            | Default alias      | Algorithms(1)                       |
   > | --------------------------------------- | ------------------ | ----------------------------------- |
   > | `am.services.oauth2.oidc.signing.ES256` | `es256test`        | ES256                               |
   > | `am.services.oauth2.oidc.signing.ES384` | `es384test`        | ES384                               |
   > | `am.services.oauth2.oidc.signing.ES512` | `es512test`        | ES512                               |
   > | `am.services.oauth2.oidc.signing.RSA`   | `rsajwtsigningkey` | PS256 PS384 PS512 RS256 RS384 RS512 |
   > | `am.services.oauth2.oidc.signing.EDDSA` |                    | EdDSA with SHA-512                  |
   >
   > (1) The following applies to confidential clients only:
   >
   > If you select an HMAC algorithm for signing ID tokens (HS256, HS384, or HS512), the Client Secret property value in the OAuth 2.0 Client is used as the HMAC secret instead of an entry from the secret stores.
   >
   > Since the HMAC secret is shared between AM and the client, a malicious user compromising the client could potentially create tokens that AM would trust. Therefore, to protect against misuse, AM also signs the token using a non-shared signing key configured in the `am.services.oauth2.jwt.authenticity.signing` secret label.

   By default, secret labels are mapped to demo keys contained in the default keystore provided with AM and mapped to the `default-keystore` keystore secret store. Use these keys for demo and test purposes only. For production environments, replace the secrets as required and create mappings for them in a secret store configured in AM.

   For more information about managing secret stores and mapping secret labels to aliases, refer to [Secrets, certificates, and keys](../security/secrets-certs-keys.html).

3. If the client is configured in AM, go to Realms > *realm name* > Applications > OAuth 2.0 > Clients > *client ID*.

   Clients registering dynamically can obtain the algorithms that the provider supports by calling the `/oauth2/.well-known/openid-configuration` endpoint.

4. In the ID Token Signing Algorithm field, enter the signing algorithm that AM will use to sign the ID token for this client.

   Note that the OAuth 2.0 provider must support signing with the chosen algorithm.

5. Save your changes.

   AM is ready to sign ID tokens with the algorithm you configured.

   |   |                                                                                                                                                                                                  |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | If you chose a non-HMAC-based algorithm, the client will need to make a request to AM's JWK URI endpoint for the realm to recover the signing public key they can use to validate the ID tokens. |

## Deprecate algorithms and rotate public keys

Signing and encryption methods change rapidly. In the lifecycle of your OAuth 2.0 deployment you'll need to deprecate older, less secure signing and/or encrypting algorithms in favor of new ones.

In the same way, you'll rotate the keys AM uses for signing and encryption if you suspect they've been leaked or to comply with security policies, such as deprecated algorithms or keys that have reached the end of their lifetime.

The keys you expose in the JWK URI endpoint should reflect the algorithms currently supported by AM as well as the deprecated ones. Otherwise, clients still using tokens signed with deprecated keys wouldn't be able to validate them.

Deprecating supported algorithms in the OAuth 2.0/OIDC provider is a two-step process:

1. Remove the old algorithm from the OAuth 2.0 provider supported algorithm list.

   This stops new clients from registering with that algorithm.

2. After a grace period, remove the secret mapping associated with that algorithm.

   This removes the associated public keys from the JWK URI endpoint.

### Deprecate supported algorithms and their keys

Perform the steps in this procedure to deprecate an algorithm and its related keys. If you only want to deprecate keys or rotate them as part of your environment's security policies, refer to [Map and rotate secrets](../security/secret-mapping.html) instead.

1. Configure the new algorithm, if required.

   * Go to Realms > *realm name* > Services > OAuth2 Provider > OpenID Connect.

   * In the ID Token Signing Algorithm supported field, add the new signing algorithm, if not already present.

   * In the ID Token Encryption Algorithms supported field, add the new encryption algorithm, if not already present.

   * Save your changes.

2. Configure secret label mappings for the keys using the new algorithm, if required.

   Learn more in [Secret stores](../security/secret-stores.html).

3. Remove the algorithm to be deprecated from the relevant OAuth 2.0 provider algorithm list:

   * Go to Realms > *realm name* > Services > OAuth2 Provider > OpenID Connect.

   * In the ID Token Signing Algorithm supported field, remove the deprecated signing algorithm.

   * In the ID Token Encryption Algorithms supported field, remove the deprecated encryption algorithm.

   * Save your changes.

4. Decide on a grace period.

   For example, a month. During this period both the deprecated and the new algorithms/keys are supported.

   New clients can't register with the deprecated algorithms and are forced to use a supported algorithm. However, since the deprecated keys are still mapped to secret labels, existing clients still can use them to validate active tokens and encrypt requests.

   Existing clients must change their configuration during the grace period to use one of the supported algorithms.

5. After the grace period, remove the secret label mappings relevant to the deprecated algorithm.

   Learn more about secret mappings in [Map and rotate secrets](../security/secret-mapping.html).

## Customize public key IDs

By default, AM generates a key ID (`kid`) for each public key exposed in the `jwk_uri` URI when AM is configured as an OAuth 2.0 authorization server.

For keys stored in a keystore or HSM secret store, you can customize how key ID values are determined by writing an implementation of the `KeyStoreKeyIdProvider` interface and configuring it in AM:

1. Write your own implementation of the `KeyStoreKeyIdProvider` interface that provides a specific key ID for a provided public key. Find more information in the [KeyStoreKeyIdProvider](../_attachments/apidocs/org/forgerock/openam/secrets/KeyStoreKeyIdProvider.html) interface in the *AM Public API Javadoc*.

2. In the AM admin UI, configure the OAuth 2.0/OIDC Provider service, if you haven't already done so.

   Learn more in [Authorization server configuration](../am-oauth2/oauth2-configure-authz.html).

3. Go to Configure > Server Defaults > Advanced.

4. Add an advanced server property called `org.forgerock.openam.secrets.keystore.keyid.provider`, whose value is the fully qualified name of the class you wrote in previous steps.

   For example:

   ```properties
   org.forgerock.openam.secrets.keystore.keyid.provider = com.mycompany.am.secrets.CustomKeyStoreKeyIdProvider
   ```

5. Restart the AM instance or the container in which it runs.

6. Verify that the customized key IDs are displayed by navigating to the OAuth 2.0 authorization server's `jwk_uri` URI.

   For example, `https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/connect/jwk_uri`.

## Display every algorithm and key type associated with a key ID

By default, each key ID (`kid`) exposed by the `jwk_uri` endpoint matches a unique secret, as recommended by the [RFC7517](https://www.rfc-editor.org/rfc/rfc7517.html#section-4.5) specification. This means that each `kid` is of a particular key type, and uses a particular algorithm.

If you have several algorithms and key types associated with one `kid`, configure the JWK URI endpoint to display them as different keys in the JWK. Note that when including all combinations associated with a `kid`, that `kid` doesn't uniquely identify a particular secret.

1. In the AM admin UI, go to Realms > *realm name* > Services > OAuth2 Provider > Advanced OpenID Connect.

2. Enable Include all kty and alg combinations in jwk\_uri.

3. Save your changes.

4. Verify that you can now see duplicate `kid` entries for different combinations of algorithms and key types.

   Learn more in [Access the keys exposed by the JWK URI endpoint](#obtaining-public-signing-key).

## Map custom key IDs to secrets

If your deployment requires custom key IDs provided by a third party, you can map those key IDs to AM secrets.

When AM signs a JWT using the secret, the `kid` header parameter in the JWT is the custom `kid`.

1. In the AM admin UI, go to Realms > *realm name* > Services > OAuth2 Provider > Advanced OpenID Connect.

2. Make sure Remote JSON Web Key URL contains the URI of your secrets API.

3. Under JWT Signing kid Header Mappings, add mappings from the secret aliases of the key used to sign JWTs to the custom `kid` header values.

   * Key is the secret alias of the key used to sign the given JWT.

   * Value is the custom `kid` value.

4. Click + Add for each mapping.

5. Save your changes.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * The custom `kid` is applied for any signed JWT that's part of communication between the OAuth 2.0 client and AM. This includes:

  * Stateless access tokens

  * Stateless refresh tokens

  * Device code JWTs

  * OIDC ID tokens

  * Token introspection responses when the format is JWT

  * User info responses when the format is JWT

  * Authorization response JWTs

* Custom key IDs mapped in the OAuth 2.0 provider configuration take precedence over [custom key IDs](#customizing-kids) provided by the `KeyStoreKeyIdProvider` interface.

* If the same alias is mapped to the same secret label across different keystores, the custom `kid` will apply for *all* secrets that share that alias.

  You should map each secret label only once per realm, or globally.

* Private signing keys stored in File System Secret Stores don't support custom `kid` header values because this store type does not support aliases. |

## Override default `kid` values

For certificates stored in a [GSM secret store](../security/secret-stores.html#create-GSM-secret-stores), the public key published in the JWK\_URI has a `kid` value that includes the name of the secret. For example:

```json
"kid" : "secrets/secret-name/versions/1"
```

|   |                                                                                                                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This is a change in behavior. Prior to AM 8.1, the `kid` value contained only the GSM secret *version*, for example:```json
"kid" : "1"
```To revert to the previous behavior, set the [am.secrets.gsm.stableid.version.only](../setup/server-advanced.html#am.secrets.gsm.stableid.version.only) advanced server property to `true`. |

---

---
title: /oauth2/connect/rp/jwk_uri
description: Expose the PingAM relying party JSON Web Key URI endpoint that providers use to encrypt ID tokens, verify JWT signatures, and decrypt client authentication JWTs
component: pingam
version: 8.1
page_id: pingam:am-oidc1:managing-rp-jwk_uri
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oidc1/managing-rp-jwk_uri.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OpenID Connect (OIDC)", "Standards", "Setup &amp; Configuration", "Security", "Endpoints"]
page_aliases: ["oidc1-guide:managing-rp-jwk_uri.adoc"]
---

# /oauth2/connect/rp/jwk\_uri

As well as acting as the provider, AM can also act as the relying party. To share its client public secrets, AM exposes a JSON web key (JWK) URI endpoint for each realm.

Use this endpoint during [Social authentication](../am-authentication/social-registration.html), where providers can use the exposed secrets to:

* Encrypt ID tokens returned to AM.

* Verify the signature of JWTs coming from AM, such as that of request objects or client authentication JWTs.

* Decrypt client authentication JWTs coming from AM.

Specify the AM realm path in the URI, as follows:

```
/oauth2/realms/root/realms/alpha/connect/rp/jwk_uri
```

Example:

```bash
$ curl https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/connect/rp/jwk_uri
{
  "keys": [
    {
      "kty": "RSA",
      "kid": "DkKMPE7hFVEn77WWhVuzaoFp4O8=",
      "use": "enc",
      "x5t": "JRxY4hJRL3sI_dAUWUEosCEQJ3A",
      "x5c": [
        "MIIDYTCCAkm…​eP4wLr3cM="
      ],
      "n": "i7t6m4d_02dZ8dOe-DFc…​zflF8jR9pewTbQ",
      "e": "AQAB"
    },
    {
      "kty": "RSA",
      "kid": "wU3ifIIaLOUAReRB/FG6eM1P1QM=",
      "use": "sig",
      "x5t": "5eOfy1Nn2MMIKVRRkq0OgFAw348",
      "x5c": [
        "MIIDdzCCAl+gAwIBAgIES3eb+zANBgk…​s009kbW6inN8zA6"
      ],
      "n": "10iGQ5l5IdqB…​AJW4ZSg1PPO2UJSQ",
      "e": "AQAB"
    }
  ]
}
```

Supply the JWK URI to the provider when registering AM as a relying party. Consult the documentation provided by your OpenID provider for more information.

The JWK URI endpoint publishes keys based on secret mappings made either globally, or in the specific realm.

The secret labels to map are as follows:

* `am.services.oauth2.oidc.rp.jwt.authenticity.signing`

  The OpenID Connect provider obtains the public key from the alias mapped to this secret, and uses it to verify the signature applied to request objects it receives.

  All aliases configured for the secret label are published at the endpoint so that, when you [rotate secrets](../security/secret-mapping.html), the provider is still able to validate JWTs with all the secrets.

  The active secret is the only one that AM uses for signing, however.

* `am.services.oauth2.oidc.rp.idtoken.encryption`

  The OpenID Connect provider obtains the public key from the alias mapped to this secret, and uses it to encrypt ID tokens and `userinfo` endpoint data in JWT format before returning it to AM.

  Unlike the signing secret label above, only the alias that is marked as *active* in the mappings is published at the endpoint. Any additional mappings are ignored.

* `am.services.oauth2.mtls.client.authentication`

  The OpenID Connect provider obtains the public JWK from the alias mapped to this secret, and uses it to verify the mutual TLS self-signed certificate that the client uses to authenticate.

Secrets configured globally will show in the JWK URI for all realms.

In a new AM installation, these signing and encryption secret labels are mapped by default, as explained in the table below:

> **Collapse: Decrypt ID tokens**
>
> This table shows the secret label mapping to support decryption of ID tokens and `userinfo` endpoint data in JWT format when AM is configured as a relying party of the Social Identity Provider Service:
>
> | Secret label                                    | Default alias | Algorithms                                                   |
> | ----------------------------------------------- | ------------- | ------------------------------------------------------------ |
> | `am.services.oauth2.oidc.rp.idtoken.encryption` | `test`        | Consult the `.well-known` endpoint of the identity provider. |
>
> The public key is exposed in the [/oauth2/connect/rp/jwk\_uri](managing-rp-jwk_uri.html).
>
> For more information about the algorithms supported, and how to configure this secret label mapping, refer to [Social authentication](../am-authentication/social-registration.html).

> **Collapse: Sign JWTs and objects**
>
> This table shows the secret label mapping that AM uses to sign JWTs and objects when configured as a relying party of the Social Identity Provider Service:
>
> | Secret label                                          | Default alias      | Algorithms                                                   |
> | ----------------------------------------------------- | ------------------ | ------------------------------------------------------------ |
> | `am.services.oauth2.oidc.rp.jwt.authenticity.signing` | `rsajwtsigningkey` | Consult the `.well-known` endpoint of the identity provider. |
>
> The public key is exposed in the [/oauth2/connect/rp/jwk\_uri](managing-rp-jwk_uri.html).
>
> For more information about the algorithms supported, and how to configure this secret label mapping, refer to [Social authentication](../am-authentication/social-registration.html).

|   |                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------- |
|   | In upgraded AM instances, the secret labels won't have default aliases mapped, and the JWK URI endpoint returns an empty JWK set. |

By default, secret labels are mapped to demo keys contained in the default keystore provided with AM and mapped to the `default-keystore` secret store. Use these keys for demo and test purposes only. For production environments, replace the secrets as required and create mappings for them in a secret store configured in AM.

For details about managing secret stores and mapping secret labels to aliases, refer to [Secrets, certificates, and keys](../security/secrets-certs-keys.html).

---

---
title: /oauth2/idtokeninfo
description: Validate unencrypted OpenID Connect ID tokens and retrieve token claims using the /oauth2/idtokeninfo endpoint
component: pingam
version: 8.1
page_id: pingam:am-oidc1:rest-api-oidc-idtoken-validation
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oidc1/rest-api-oidc-idtoken-validation.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OpenID Connect (OIDC)", "Standards", "Endpoints"]
page_aliases: ["oidc1-guide:rest-api-oidc-idtoken-validation.adoc"]
section_ids:
  supported_parameters: Supported parameters
  token_validation: Token validation
  examples: Examples
  subject_claims: Subject claims
---

# /oauth2/idtokeninfo

The `/oauth2/idtokeninfo` endpoint is an AM-specific endpoint.

Use this endpoint to validate *unencrypted* ID tokens and to retrieve claims in the token.

Specify the realm in the request URL; for example:

```none
https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/idtokeninfo
```

## Supported parameters

The ID token information endpoint supports the following parameters:

| Parameter               | Description                                                                                                      | Required                                                                                        |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `claims`                | Comma-separated list of claims to return from the ID token.                                                      | Yes                                                                                             |
| `client_assertion`      | A signed JSON Web Token (JWT) to use as client credentials.                                                      | Yes, for [JWT profile](../am-oauth2/client-auth-jwt.html) authentication                        |
| `client_assertion_type` | The type of assertion, `client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer`. | Yes, for [JWT profile](../am-oauth2/client-auth-jwt.html) authentication                        |
| `client_id`             | Uniquely identifies the application making the request.                                                          | Yes, when authentication is required (default)                                                  |
| `client_secret`         | The password for a confidential client.                                                                          | Yes, when authenticating with [Form parameters (HTTP POST)](../am-oauth2/client-auth-form.html) |
| `id_token`              | The ID token to validate.                                                                                        | Yes                                                                                             |

By default, the client must authenticate to use the endpoint. Optionally disable this in the OAuth 2.0 provider configuration. In the AM admin UI, go to Realms > *realm name* > Services > OAuth2 Provider > Advanced OpenID Connect and disable Idtokeninfo Endpoint Requires Client Authentication.

## Token validation

AM validates the tokens based on rules in the [OpenID Connect Core](https://openid.net/specs/openid-connect-core-1_0.html#IDTokenValidation) specification. Token validation includes the following steps:

1. Extract the first `aud` (audience) claim from the ID token.

   This step depends on the `client_id` parameter to identify the client and validate the `aud` claim.

2. Extract the `realm` claim, if present, and use it to look up the client profile.

   Validation returns an error if no client profile exists.

3. Verify the signature of the ID token.

   This validation step depends on these client profile settings:

   ID Token Signing Algorithm (default: `RS256`)\
   Public key selector (default: `JWKs_URI`)

4. Verify the following claims:

   `aud` (audience)\
   `exp` (expiration)\
   `iat` (issued at)\
   `iss` (issuer)\
   `nbf` (not before, if set)

This endpoint does not check whether the ID token was revoked with the [/oauth2/connect/endSession](rest-api-oidc-endsession-endpoint.html) endpoint.

## Examples

The following example returns all ID token claims:

```bash
$ curl \
--request POST \
--user myClient:mySecret \
--data 'id_token=id-token' \
"https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/idtokeninfo"
{
  "at_hash": "PZg5xZsIlFtRSfg8MAWhWg",
  "sub": "a0325ea4-9d9b-4056-931b-ab64704cc3da",
  "auditTrackingId": "2e5c7611-4a61-4001-8739-f714d43e9da2-881454",
  "subname": "a0325ea4-9d9b-4056-931b-ab64704cc3da",
  "iss": "https://am.example.com:8443/am/oauth2/realms/root/realms/alpha",
  "tokenName": "id_token",
  "given_name": "Babs",
  "sid": "+buKyDp+Fbc0/Rkd0OqsfdKy7ZY0nWvcsEetikX+eTc=",
  "aud": "myClient",
  "c_hash": "FP5Nj162jgycmtEeRjVQ-A",
  "acr": "0",
  "org.forgerock.openidconnect.ops": "gkQOcZ1F3ZFdYPd6TiGIgr6scH0",
  "s_hash": "bKE9UspwyIPg8LsQHkJaiQ",
  "azp": "myClient",
  "auth_time": 1676360741,
  "name": "Babs Jensen",
  "realm": "/alpha",
  "exp": 1676364398,
  "tokenType": "JWTToken",
  "iat": 1676360798,
  "family_name": "Jensen"
}
```

Use the optional `claims` parameter to return specific claims as in the following example:

```bash
$ curl \
--request POST \
--user myClient:mySecret \
--data 'id_token=id-token' \
--data 'claims=sub,exp,realm' \
"https://am.example.com:8443/am/oauth2/idtokeninfo"
{
  "sub": "a0325ea4-9d9b-4056-931b-ab64704cc3da",
  "exp": 1676364398,
  "realm": "/alpha"
}
```

If you request a claim that does not exist, no error occurs; AM omits the claim from the response.

## Subject claims

The subject claim is in the format `(type!subject)`, where:

* `subject` is the identifier of the user/identity, or the name of the OAuth 2.0/OpenID Connect client that is the subject of the token.

* `type` can be one of the following:

  * `age`. Indicates the *subject* is an OAuth 2.0/OpenID Connect-related user-agent or client. For example, an OAuth 2.0 client, a Remote Consent Service agent, and a Web and Java Agent internal client.

  * `usr`. Indicates the *subject* is a user/identity.

For example, `(usr!bjensen)`, or `(age!myOAuth2Client)`.

The value of the `subname` claim, when provided, matches the value of the *subject* portion of the `sub` claim.

---

---
title: /oauth2/register
description: Use the /oauth2/register endpoint to create, read, update, and delete client application profiles according to OpenID Connect and OAuth 2.0 standards
component: pingam
version: 8.1
page_id: pingam:am-oidc1:rest-api-oauth2-register-endpoint
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oidc1/rest-api-oauth2-register-endpoint.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OpenID Connect (OIDC)", "Standards", "Endpoints", "Self-Service"]
page_aliases: ["oidc1-guide:rest-api-oauth2-register-endpoint.adoc"]
---

# /oauth2/register

The `/oauth2/register` endpoint is defined in:

* [OpenID Connect Dynamic Client Registration 1.0 incorporating errata set 1](https://openid.net/specs/openid-connect-registration-1_0.html)

* RFC 7591: [OAuth 2.0 Dynamic Client Registration Protocol](https://www.rfc-editor.org/rfc/rfc7591.html)

* RFC 7592: [OAuth 2.0 Dynamic Client Registration Management Protocol](https://www.rfc-editor.org/rfc/rfc7592.html)

Use this endpoint to create, read, update, and delete client application profiles.

Specify the realm in the request URL; for example:

```none
https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/register
```

The endpoint supports the following HTTP methods:

* `POST`

  Create a client profile.

* `GET`

  Read a client profile.

* `PUT`

  Update a client profile.

* `DELETE`

  Delete a client profile.

AM requires configuration to allow dynamic registration. For details, refer to [Dynamic client registration](oauth2-dynamic-client-registration.html).

---

---
title: /oauth2/userinfo
description: Use the OpenID Connect UserInfo endpoint to request claims about the authenticated end user with an access token
component: pingam
version: 8.1
page_id: pingam:am-oidc1:rest-api-oidc-userinfo-endpoint
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oidc1/rest-api-oidc-userinfo-endpoint.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OpenID Connect (OIDC)", "Standards", "Endpoints"]
page_aliases: ["oidc1-guide:rest-api-oidc-userinfo-endpoint.adoc"]
section_ids:
  subject_claims: Subject claims
  response_signing_and_encryption: Response signing and encryption
---

# /oauth2/userinfo

The `/oauth2/userinfo` endpoint is the OpenID Connect (OIDC) [UserInfo endpoint](https://openid.net/specs/openid-connect-core-1_0.html#UserInfo).

Use this endpoint to request claims about the authenticated end user.

Specify the realm in the request URL; for example:

```none
https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/userinfo
```

To access the endpoint, use an access token from an OIDC grant flow as the bearer token. The endpoint returns claims based on the scopes granted for the access token as in the following example:

```bash
$ curl \
--request GET \
--header "Authorization: Bearer <access-token>" \
"https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/userinfo"
{
  "name": "Babs Jensen",
  "family_name": "Jensen",
  "given_name": "Babs",
  "sub": "a0325ea4-9d9b-4056-931b-ab64704cc3da",
  "subname": "a0325ea4-9d9b-4056-931b-ab64704cc3da"
}
```

## Subject claims

The subject claim is in the format `(type!subject)`, where:

* `subject` is the identifier of the user/identity, or the name of the OAuth 2.0/OpenID Connect client that is the subject of the token.

* `type` can be one of the following:

  * `age`. Indicates the *subject* is an OAuth 2.0/OpenID Connect-related user-agent or client. For example, an OAuth 2.0 client, a Remote Consent Service agent, and a Web and Java Agent internal client.

  * `usr`. Indicates the *subject* is a user/identity.

For example, `(usr!bjensen)`, or `(age!myOAuth2Client)`.

The value of the `subname` claim matches the value of the *subject* portion of the `sub` claim.

## Response signing and encryption

The default response is a plain JSON object.

AM also supports responding with a signed JSON Web Token (JWT) or signed and encrypted JWT. JWT responses include the `aud` and `iss` claims.

To enable signing and encryption, follow these steps:

1. In the AM admin UI, go to Realms > *realm name* > Applications > OAuth 2.0 > Clients > *client ID* > Signing and Encryption and select the response type in the User info response format drop-down list.

2. If necessary, configure the signing and encryption properties:

   User info signed response algorithm\
   User info encrypted response algorithm\
   User info encrypted response encryption algorithm

3. Save your work.

4. To restrict the possible settings for the clients in the realm, edit the settings under Realms > *realm name* > Services > OAuth2 Provider > Advanced OpenID Connect.

5. Save your work.

For details, refer to the OAuth 2.0 provider reference documentation for [advanced OIDC settings](../setup/services-configuration.html#global-oauth-oidc-advanced-openid-connect) and to [Secret label default mappings](../security/secret-mapping.html#secret-label-mappings).

---

---
title: AM as a Temenos identity provider
description: Configure PingAM as an OpenID Provider for Temenos Quantum Fabric to authenticate end users with OAuth 2.0
component: pingam
version: 8.1
page_id: pingam:am-oidc1:use-case-temenos
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oidc1/use-case-temenos.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 10, 2025
keywords: ["Use Case"]
page_aliases: ["oidc1-guide:use-case-temenos.adoc"]
section_ids:
  temenos-goals: Goals
  temenos-process: What you'll do
  temenos-prerequisites: Before you begin
  temenos-tasks: Tasks
  temenos-task-1: "Task 1: Configure AM as an OpenID Provider"
  temenos-task-2: "Task 2: Add AM as an OAuth 2.0 identity service in Temenos"
  temenos-reference-material: Reference material
---

# AM as a Temenos identity provider

This use case shows how Temenos can use AM as an OpenID Provider (OP) to authenticate end users. Specifically, you set up AM as an OAuth 2.0 identity service in Temenos Quantum Fabric.

AM supports OAuth 2.0 and OpenID Connect (OIDC) natively, making it a good choice for integrating with Temenos and other standards-based applications.

## Goals

After completing this use case, you'll know how to do the following:

* Configure AM as an OIDC identity provider

* Configure Temenos to use AM as an OIDC identity provider

## What you'll do

* Create an OIDC application for Temenos.

* Configure a Temenos identity service to connect as the application to AM.

## Before you begin

Before you start, make sure you have:

* A basic understanding of:

  * The AM admin UI

  * OAuth 2.0

  * OIDC

* [Set up AM for evaluation](../evaluation/preface.html), including creating a test user

* Access to your AM as an administrator

* Access to a Temenos development environment as an administrator

## Tasks

|   |                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------- |
|   | This use case requires the use of third-party services. Use your environment-specific details where necessary. |

### Task 1: Configure AM as an OpenID Provider

1. Sign on to the AM admin UI as an administrator.

2. Go to the appropriate realm.

3. Go to Applications > OAuth 2.0 > Clients and click + Add Client.

4. On the New OAuth 2.0 Client page, add a client with the following configuration and click Create:

   | Field            | Value                                                                                                |
   | ---------------- | ---------------------------------------------------------------------------------------------------- |
   | Client ID        | `temenos_oidc`                                                                                       |
   | Client secret    | Enter a password for the client. Remember the password because you need it to configure Temenos.     |
   | Redirection URIs | `https://<accountID>.auth.konycloud.com/OAuth2/Callback`Here \<accountID> is the Temenos account ID. |
   | Scopes           | `openid`, `profile`, `email`, `phone`                                                                |

   The Temenos OIDC client page opens.

### Task 2: Add AM as an OAuth 2.0 identity service in Temenos

|   |                                                                                                                                                                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | These instructions include steps for a third-party product. We've verified them to the best of our ability, but third-party functionality and interfaces may change. Read [the official Temenos documentation](https://docs.kony.com/konylibrary/konyfabric/kony_fabric_user_guide/Content/Identity10_Kony_OAuth2.htm#OAuth2ID) if you notice any differences. |

1. Sign on to the Temenos development environment as an administrator.

2. Go to the Quantum Fabric identity service designer page, create a new identity service with the following configuration, and click Save:

   | Field                                                 | Value                                                                         |
   | ----------------------------------------------------- | ----------------------------------------------------------------------------- |
   | Name                                                  | `AM`                                                                          |
   | Type of Identity                                      | `OAuth 2.0`                                                                   |
   | Provider Details > Grant Type                         | `Authorization Code`                                                          |
   | Provider Details > Authorize endpoint                 | `https://am.example.com:8443/am/oauth2/realms/root/realms/realm/authorize`    |
   | Provider Details > Token endpoint                     | `https://am.example.com:8443/am/oauth2/realms/root/realms/realm/access_token` |
   | Provider Details > Scope                              | `openid`, `profile`, `email`, `phone`                                         |
   | Client Details > Client Assertion Type                | `Basic authentication`                                                        |
   | Client Details > Client ID                            | `temenos_oidc`                                                                |
   | Client Details > Client Secret                        | The password for the `temenos_oidc` client you created in the previous task.  |
   | User Profile Endpoint Details > Profile Endpoint Type | `Profile in response of URL`                                                  |
   | User Profile Endpoint Details > URL                   | `https://am.example.com:8443/am/oauth2/realms/root/realms/realm/userinfo`     |
   | User Attribute Selectors > Federation ID              | `_id`                                                                         |

3. Use the Test Login feature to test the identity service.

   Sign on as the AM test user you created when [setting up AM for evaluation](../evaluation/preface.html).

4. When the service works as expected, publish the Fabric application.

## Reference material

Find background information for the procedures in this use case in the following documentation:

* Learn how to connect any OIDC relying party to AM in [Client application registration](../am-oauth2/oauth2-register-client.html) or [Customize dynamic client registration](dynamic-client-registration-script.html).

* Learn how to configure a Quantum Fabric OAuth 2.0 Identity Service in [Temenos Quantum Fabric OAuth 2.0 Identity Service](https://docs.kony.com/konylibrary/konyfabric/kony_fabric_user_guide/Content/Identity10_Kony_OAuth2.htm#OAuth2ID).

---

---
title: AM as OpenID provider
description: Configure PingAM as an OpenID Connect provider to return ID tokens to relying parties and support user authentication and profile information sharing
component: pingam
version: 8.1
page_id: pingam:am-oidc1:oidc-am-provider
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oidc1/oidc-am-provider.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OpenID Connect (OIDC)", "Standards", "Setup &amp; Configuration", "Integration"]
page_aliases: ["oidc1-guide:oidc-am-provider.adoc"]
section_ids:
  oidc-concepts: OIDC concepts
  oauth2-vs-oidc: OAuth 2.0 or OIDC?
  am-implementation-oidc: AM and OIDC
  grant_types: Grant types
  standards: Standards
  openam-openid-session-management: Session management and logout
  openam-openid-discovery: Discovery and dynamic client registration
  mobile_connect: Mobile Connect
  configure-openid-connect-discovery: OIDC discovery
  openid-connect-security-considerations: Security considerations
  token-storage-oidc: Token storage location
---

# AM as OpenID provider

An OAuth 2.0 authentication server that implements OpenID Connect (OIDC) is referred to as an OpenID provider (OP). An OAuth 2.0 client that uses OIDC is also referred to as a relying party (RP).

In its role as an OP, AM returns ID tokens to relying parties. Because OIDC extends OAuth 2.0, when AM is configured as an OP it can also return access and refresh tokens to relying parties.

|   |                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------- |
|   | Before configuring OIDC in your environment, ensure you are familiar with the OAuth 2.0 standards and the AM implementation of OAuth 2.0. |

## OIDC concepts

[OIDC](http://openid.net/connect/) is an identity layer built on top of OAuth 2.0. It lets clients verify the identity of a user based on the authentication performed by OAuth 2.0 authorization servers. It also lets clients obtain profile information about the user over REST.

The following sequence diagram demonstrates the basic OIDC flow:

![AM can function as the authorization server and as the client.](_images/oidc-flow.svg)Figure 1. OIDC protocol flow

OIDC clients can [register](oauth2-dynamic-client-registration.html) with the OP and manage their client data dynamically.

To let clients [discover](#configure-openid-connect-discovery) an end user's OP, its endpoints and how to interact with it, AM supports the [OpenID Connect Discovery 1.0](https://openid.net/specs/openid-connect-discovery-1_0.html) specification.

## OAuth 2.0 or OIDC?

The OAuth 2.0 and OIDC standards were both created for users who need to interact with a third party service; however, they aim to solve different problems. This topic compares [OAuth 2.0 and OIDC functionality](#table-oidc-oauth2) and the [actors](#table-oidc-actors) in the implementation of both standards.

**Comparison between OAuth 2.0 and OIDC functionality**

|                    | OAuth 2.0                                                                                                                                                                                                                                                                                      | OIDC                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Purpose**        | Gives users a way to **authorize** a service to access and use a subset of their data on their behalf in a secure way.Users must agree to provide access under the service's *terms and conditions*; for example, how long the service has access to their data and what the data is used for. | Gives users a way to **authenticate** to a service by providing it with a subset of their data in a secure way.Because OIDC extends OAuth 2.0, users can authorize a relying party to collect a subset of their data (usually information stored in the user's profile) from a third party. The service then uses this data to authenticate the user and provide its services.The user can therefore use the relying party's services even if they have never created an account with the relying party.                                                 |
| **Use cases**      | Use cases are generic and can be tailored to many needs. A common example is a user allowing a photo print service access to a third-party server hosting their pictures, so the photo print service can print them.                                                                           | The most common scenario is using social media credentials to log in to a third-party service provider.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Tokens**         | Access and refresh tokens                                                                                                                                                                                                                                                                      | ID tokens                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Role of scopes** | Scopes limit the information that can be shared with the service or what the service can do with the data. For example, the `print` scope might allow a photo print service to access photos but not to edit them.OAuth 2.0 scopes are not data and are not related to user data in any way.   | Scopes can be mapped to specific user data. For example, AM maps the `profile` scope to a series of user profile attributes. Because different identity managers can present information in different attributes, profile attributes are mapped to OIDC *claims*.Claims are returned as part of the ID token. In some cases, additional claims can be requested in a call to the `oauth2/userinfo` endpoint.For more information about how AM maps user profile attributes to claims, see [Claims](understanding-openid-connect-scopes-and-claims.html). |

**Comparison between OAuth 2.0 and OIDC actors**

| OIDC actor           | OAuth 2.0 actor                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| -------------------- | --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| End user             | Resource owner (RO)                           | The owner of the information the application needs to access.The end user who wants to use an application through an existing identity provider account, without signing up to and creating credentials for yet another web service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Relying party (RP)   | Client                                        | The third-party that needs to know the identity of the end user to provide their services. For example, a delivery company or a shopping site.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| OpenID provider (OP) | Authorization server (AS)Resource server (RS) | A service that has the end user's consent to provide the RP with access to some of its user information. OIDC defines unique identification for an account (subject identifier + issuer identifier). The RP can use this identification as a key to the user profile.In the case of an online mail application, the key could be used to access the user's mailboxes and related account information. In the case of an online shopping site, the key could be used to access personalized offerings, account, shopping cart, and so on. The key makes it possible to serve users *as if they had local accounts*.AM can act as the OP to authenticate end users and provide RPs with information about the users in the form of an OIDC token. |

## AM and OIDC

This section describes AM's implementation of OIDC, including the supported grant types and standards.

### Grant types

* Authorization code

* Authorization code with PKCE

* Backchannel request

* Implicit

* Hybrid

* Hybrid with PKCE

For details, refer to [OpenID Connect grant flows](oidc-implementing-flows.html).

### Standards

This section lists the OIDC standards that AM supports. For more information, refer to the complete list of supported [OIDC](../am-reference/am-supported-standards.html#standards-oidc) and [OAuth 2.0](../am-reference/am-supported-standards.html#standards-oauth2) standards.

#### Session management and logout

Relying parties can:

* Track whether end users are logged in at the provider using an invisible iframe and the HTML 5 postMessage API.

* Initiate end user logout at the provider using an endpoint.

AM can also send *logout tokens* to relying parties when authenticated sessions linked to ID tokens become invalid. Learn more in [OIDC authenticated sessions](manage-sessions-openid-connect.html).

#### Discovery and dynamic client registration

OIDC defines how a relying party can discover the OP and the corresponding OIDC configuration for an end user. The discovery mechanism relies on [WebFinger](https://datatracker.ietf.org/doc/html/draft-ietf-appsawg-webfinger) to get the information, based on the end user's identifier. The server returns the information in JSON Resource Descriptor (JRD) format.

For details, refer to [OIDC discovery](#configure-openid-connect-discovery) and [Dynamic client registration](oauth2-dynamic-client-registration.html).

#### Mobile Connect

Mobile Connect extends OIDC to let mobile phones be used as authentication devices. This allows mobile network operators to act as identity providers.

For details, refer to [GSMA Mobile Connect](oidc-mobile-connect.html).

## OIDC discovery

To let relying parties (or clients) discover the OP for an end user, AM supports the [OpenID Connect Discovery 1.0](https://openid.net/specs/openid-connect-discovery-1_0.html) specification. In addition to discovering the OP for an end user, the relying party can request the OP *configuration*.

AM exposes the following REST endpoints for discovering the URL of the OP and its configuration:

* [/oauth2/.well-known/openid-configuration](rest-api-oidc-discovery-configuration.html)

* [/.well-known/webfinger](rest-api-oidc-discovery-webfinger.html)

Discovery relies on the [WebFinger](https://datatracker.ietf.org/doc/html/draft-ietf-appsawg-webfinger) protocol to discover information about people and other entities, using standard HTTP methods. WebFinger uses [Well-Known URIs](https://www.rfc-editor.org/info/rfc5785), which defines the path prefix `/.well-known/` for the URLs defined by OIDC discovery.

Relying parties need to find the right *host:port/deployment-uri* combination to locate the well-known endpoints. You must manage the redirection to AM using your proxies, load balancers, and others, such that a request to `http://www.example.com/.well-known/webfinger` reaches, for example, `https://am.example.com:8443/am/.well-known/webfinger`.

When the relying party has discovered the URL of the OP, it can register with the OP [dynamically](oauth2-dynamic-client-registration.html). For test purposes, or if it suits your environment better, you can also register clients [manually](../am-oauth2/oauth2-register-client.html).

The `/.well-known/webfinger` endpoint is disabled by default. To enable it, follow these steps:

1. In the AM admin UI, go to Realms > *realm name* > Services > OAuth2 Provider > OpenID Connect.

2. Enable OIDC Provider Discovery.

3. Save your changes.

   The discovery endpoint now allows searches for users *within this realm* only. Repeat these steps in other realms, as required.

## Security considerations

AM provides the following security mechanisms to ensure that OIDC ID tokens are properly protected against malicious attackers:

* TLS

* Digital signatures

* Token encryption

When you are designing a security mechanism, take into account the points developed in the section on [Security considerations](https://openid.net/specs/openid-connect-core-1_0.html#Security) in the *OpenID Connect Core 1.0 incorporating errata set 1* specification.

OIDC requires that network messages are protected with Transport Layer Security (TLS).

For information about protecting traffic to and from the web container in which AM runs, refer to [Secrets, certificates, and keys](../security/secrets-certs-keys.html).

For additional information, refer to the OAuth 2.0 [Security considerations](../am-oauth2/am-as-authz-server.html#oauth2-security-considerations).

## Token storage location

OIDC and OAuth 2.0-related services are stateless in AM, unless otherwise indicated; they do not hold any token information locally.

Access and refresh tokens can be stored in the CTS token store or presented to clients as JWTs; however, OIDC tokens and session information are managed in the following way:

* ID tokens are always presented as JWTs.

* OIDC sessions are always stored in the CTS token store.

For more information about how to configure access and refresh token storage, refer to [Token storage location](../am-oauth2/stateless-stateful-tokens.html).

---

---
title: Authentication requirements
description: Configure authentication requirements to associate authentication journeys with OpenID Connect requests and communicate honored requirements through acr and amr claims in ID tokens
component: pingam
version: 8.1
page_id: pingam:am-oidc1:oidc-authentication-requirements
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oidc1/oidc-authentication-requirements.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OpenID Connect (OIDC)", "Standards", "Setup &amp; Configuration", "Authentication"]
page_aliases: ["oidc1-guide:oidc-authentication-requirements.adoc"]
section_ids:
  acr-claim: The acr claim
  voluntary_claims: Voluntary claims
  essential_claims: Essential claims
  proc-configure-acr: Configure acr claims
  authn-reqts-request-processing: Request processing
  amr-claim: The amr claim
  proc-configure-amr-node: Configure amr claims
  configure-journey-amr: Configure an authentication journey
  config-oidc-plugin-amr: Configure the user info claims script
  allowlist-session-property-amr: Allowlist the session property
  configure-oidc-plugin-amr: Configure the provider
  configure-provider-claims-id-token-session: Configure the provider
  request-acr-example: Demonstrate authentication requirements
  auth-reqts-create-rp: Create an RP profile
  auth-reqts-try-voluntary: Request voluntary claims
  auth-reqts-try-essential: Request essential claims
---

# Authentication requirements

A relying party (RP) can have different authentication requirements for different protected resources. For example, a financial services provider accepts username and password authentication to create an account, but requires multi-factor authentication to download bank account statements.

AM lets you associate requirements with authentication journeys. RPs specify the authentication requirements in their requests, and AM uses the associations to authenticate the end user with the requested journey and honor the requirements.

AM communicates the honored requirements by optionally returning claims in ID tokens. It uses the following standard claims:

* An *authentication context class reference* (`acr`) claim holds a case-sensitive string identifying the class of authentication methods or procedures the authentication process satisfied. For example, an identifier for the authentication journey the end user completed successfully.

* An *authentication method references* (`amr`) claim holds a JSON array of strings identifying the authentication methods satisfied. For example, an indication the end user has authenticated with a username-password combination and a one-time password.

## The `acr` claim

The `acr` claim holds a case-sensitive string you configure in the OAuth 2.0 provider service. AM maps `acr` keys to authentication journeys to avoid directly exposing the journey names.

AM doesn't add the `acr` claim to ID tokens by default. The RP must request authentication contexts and AM must authenticate the end user.

The `acr` claims can be *voluntary* or *essential*.

### Voluntary claims

RPs request voluntary `acr` claims for optional authentication mechanisms to improve the user experience. They do this in one of the following ways:

* Specify the authentication mechanism in the `acr_values` parameter for a request to the `/oauth2/authorize` endpoint.

* Specify the authentication mechanisms in the JSON format `claims` parameter for a request to the `/oauth2/authorize` endpoint.

* Rather than specifying the mechanisms in the request, rely on Default ACR values in the RP client profile.

  Find the field in the AM admin UI under Realms > *realm name* > Applications > OAuth 2.0 > *client ID* > OpenID Connect.

  The default `acr` values are the keys of the mapping set when you [Configure `acr` claims](#proc-configure-acr). The JSON response from the [/oauth2/.well-known/openid-configuration](rest-api-oidc-discovery-configuration.html) endpoint lists the keys as `acr_values_supported` strings; for example:

  ```
  "acr_values_supported": ["username-password"]
  ```

  Any mechanisms the RP specifies in the request override the default `acr` values.

### Essential claims

RPs request essential `acr` claims for required authentication mechanisms.

RPs request essential `acr` claims by specifying the authentication mechanisms in the JSON format `claims` parameter for a request to the `/oauth2/authorize` endpoint.

Essential claims resemble, but are unrelated to, [step-up authentication](../am-sessions/session-upgrade.html).

### Configure `acr` claims

1. In the AM admin UI, go to Realms > *realm name* > Services > OAuth2 Provider > Advanced OpenID Connect.

2. Enable Enable "claims\_parameter\_supported" to let RPs request `acr` claims using the `claims` parameter.

3. In the OpenID Connect acr\_values to Auth Chain Mapping box, map keys to authentication journey identifiers.

   The following example maps `username-password` to the Login journey:

   ![Map \`acr\` claim strings to journeys.](_images/oidc-acr-values.png)

   The *acr-key* mapped to the journey AM uses to authenticate the end user becomes the value of the `acr` claim in the resulting ID token.

4. Save your changes.

### Request processing

When an RP requests authentication contexts, AM initially determines the requested journey. It uses the first context for which it has a valid mapping. For example, if the RP requests `push otp username-password` and AM has mappings only for `otp` and `username-password`, AM chooses `otp` to authenticate the end user.

The following table describes how AM processes the request:

| Scenario                                                           | Voluntary claims result                                                                                     | Essential claims result                                                                                     |
| ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| The end user isn't authenticated.                                  | Authenticate with the requested journey.                                                                    | Authenticate with the requested journey.                                                                    |
| The end user is authenticated with the requested journey.          | Don't reauthenticate.                                                                                       | Reauthenticate with the requested journey.On success, delete the original session and create a new session. |
| The end user is authenticated with a different journey.            | Reauthenticate with the requested journey.On success, delete the original session and create a new session. |                                                                                                             |
| The request specifies an unmapped `acr_values` or `claims` string. | Continue the grant flow without returning an error.                                                         | Return an error and redirect to the `redirect_uri`, if available.                                           |

After authenticating the end user, AM returns an ID token whose `acr` claim has one of the following values:

* `0` (zero)

  The RP requested an unmapped voluntary claim.

* `acr-key`

  The end user authenticated with the journey mapped to the *acr-key*.

  If authentication involves more than one journey, the *acr-key* reflects the last mapped journey.

## The `amr` claim

The `amr` claim holds an array of strings identifying families of authentication methods.

You can map an `amr` session property to `amr` values using the [Set Session Properties node](https://docs.pingidentity.com/auth-node-ref/8.1/set-session-properties.html). Then update the user info claims script to retrieve the `amr` values mapped to the `amr` session property.

When the end user authenticates with a journey using the node, AM includes the `amr` claim in the ID token it issues.

### Configure `amr` claims

#### Configure an authentication journey

1. Update an authentication journey to include the [Set Session Properties node](https://docs.pingidentity.com/auth-node-ref/8.1/set-session-properties.html), for example, update the `acr` claims journey.

2. On the Set Session Properties node, configure a key to identify the `amr` values, for example `amr`.

   As its value, enter a string to identify the authentication method satisfied. For example, `otp`.

   > **Collapse: Example: Configure the amr session property**
   >
   > ![amr-set-session-properties](_images/amr-set-session-properties.png)

3. Save your changes.

#### Configure the user info claims script

This task describes how to modify the default user info claims script to retrieve the `amr` values mapped to the `amr` session property.

This example uses a legacy script. Find a next-generation example [here](../am-oauth2/plugins-user-info-claims.html#example-oidc-claims-nextgen).

1. In the AM admin UI, go to Realms > *realm name* > Scripts, and click OIDC Claims Script.

2. In the Script field:

   * Groovy

   * JavaScript

   Add the `amr` claim details after the existing `computedClaims` line. For example:

   ```javascript
   computedClaims = claimsToResolve.collectEntries() { claim ->
       result = computeClaim(claim)
   }

   if (session != null) {
     def amrValues = [session.getProperty("amr")];
     computedClaims.put("amr", amrValues)
   }
   ```

   Add the `amr` claim details before the `return computedClaims;` line. For example:

   ```javascript
   if (session !== null && session !== undefined) {
     var amrValues = [session.getProperty("amr")];
     computedClaims.put("amr", amrValues)
   }

   return computedClaims;
   ```

3. Save your changes.

The default user info claims script is now amended to retrieve `amr` values mapped to the `amr` session property.

#### Allowlist the session property

Provide access to the `amr` session property to allow it to be output in the ID token.

1. In the AM admin UI, go to Realms > *realm name* > Services > Session Property Whitelist Service.

2. Add `amr` to the Allowlisted Session Property Names field.

3. Save your changes.

#### Configure the provider

Perform this task to set up an OAuth 2.0 provider to use your custom script.

1. [Configure the provider](../am-oauth2/customizing-oauth2-scopes.html#configure-scripted-oauth2-plugin) and make sure the following properties are set:

   * OIDC Claims Plugin Type to `SCRIPTED`.

   * OIDC Claims Script to the name of your custom script.

2. Save your changes.

#### Configure the provider

Perform this task to set up an OAuth 2.0 provider to use your custom script.

1. [Configure the provider](../am-oauth2/customizing-oauth2-scopes.html#configure-scripted-oauth2-plugin) and make sure the following properties are set:

   * OIDC Claims Plugin Type to `SCRIPTED`.

   * OIDC Claims Script to the name of your custom script.

2. Save your changes.

3. Switch to the Advanced OpenID Connect tab to always return scope-derived claims in the ID token.

4. Select Always Return Claims in ID Tokens.

   |   |                                                                                                                                                                                                                                                              |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | This option is disabled by default because of the security concerns of returning claims that may contain sensitive user information. Learn more in [Request claims in ID tokens](understanding-openid-connect-scopes-and-claims.html#request-claims-tokens). |

5. Save your changes.

## Demonstrate authentication requirements

Demonstrate the process with an RP that uses the [Implicit grant](../am-oauth2/oauth2-implicit-grant.html):

1. Create an end user profile and record the username and password.

2. [Create an RP profile](#auth-reqts-create-rp).

3. Duplicate the default Example journey to create a Login journey.

4. Optionally [configure `amr` claims](#proc-configure-amr-node).

5. [Configure `acr` claims](#proc-configure-acr) to map your duplicate journey to the `username-password` claim.

6. [Request voluntary claims](#auth-reqts-try-voluntary).

7. [Request essential claims](#auth-reqts-try-essential).

### Create an RP profile

[Register an OIDC application](../am-oauth2/oauth2-register-client.html) with the following settings:

| Setting                | Value                                  |
| ---------------------- | -------------------------------------- |
| Name                   | `myClient`                             |
| Redirection URIs       | `https://www.example.com:443/callback` |
| Scopes                 | `openid` `profile`                     |
| Advanced > Grant Types | Add `Implicit`                         |

### Request voluntary claims

1. Open a new tab in your browser.

2. Paste a URL with the `acr_values` parameter to request voluntary claims into the new browser tab.

   The following URL requests an ID token with the implicit grant:

   ```none
   https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/authorize?acr_values=username-password&client_id=myClient&response_type=id_token&scope=openid%20profile&redirect_uri=https://www.example.com:443/callback&nonce=abc123&state=123abc
   ```

3. Authenticate as the end user.

   AM redirects to the application sign-in URL (`redirect_uri`) with the `id_token` in the fragment.

4. Extract the ID token from the sign-in URL.

5. Decode the ID token to display the `acr` claim:

   ```json
   {
     "...": "...",
     "acr": "username-password"
   }
   ```

   The `amr` claim is also displayed in the decoded token if you configured `amr` claims, for example:

   ```json
     "amr": [
       "otp"
     ],
   ```

### Request essential claims

1. Define and URL-encode the essential claims parameter value.

   Essential claims requesting `username-password`:

   ```json
     {"id_token":{"acr":{"essential":true,"values":["username-password"]}}}
   ```

   URL-encoded value:

   ```
   %7B%22id_token%22%3A%7B%22acr%22%3A%7B%22essential%22%3Atrue%2C%22values%22%3A%5B%22username-password%22%5D%7D%7D%7D
   ```

2. Paste a URL with the encoded `claims` parameter to request essential claims into the new browser tab.

   The following URL requests an ID token with the implicit grant:

   ```none
   https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/authorize?claims=%7B%22id_token%22%3A%7B%22acr%22%3A%7B%22essential%22%3Atrue%2C%22values%22%3A%5B%22username-password%22%5D%7D%7D%7D&client_id=myClient&response_type=id_token&scope=openid%20profile&redirect_uri=https://www.example.com:443/callback&nonce=abc123&state=123abc&prompt=login
   ```

   The `prompt` setting forces the end user to authenticate explicitly regardless of any implied consent.

   When you request essential claims, AM authenticates the end user again. Learn more in [Request processing](#authn-reqts-request-processing).

   AM redirects to the application sign-in URL (`redirect_uri`) with the `id_token` in the fragment.

3. Extract the ID token from the sign-in URL.

4. Decode the ID token to display the `acr` claim:

   ```json
   {
     "...": "...",
     "acr": "username-password"
   }
   ```

---

---
title: Backchannel logout
description: Implement OpenID Connect Back-Channel Logout 1.0 to send logout tokens to relying parties when authenticated sessions become invalid
component: pingam
version: 8.1
page_id: pingam:am-oidc1:backchannel-logout
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oidc1/backchannel-logout.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OpenID Connect (OIDC)", "Standards", "Authentication", "Setup &amp; Configuration", "Integration"]
page_aliases: ["oidc1-guide:backchannel-logout.adoc"]
section_ids:
  backchannel-logout-limitations: Backchannel logout limitations
  backchannel-logout-token: The logout token
  enabling-backchannel-logout: Enable backchannel logout
  backchannel-logout-postman: The backchannel logout Postman collection
---

# Backchannel logout

[OpenID Connect Back-Channel Logout 1.0 Draft 06](https://openid.net/specs/openid-connect-backchannel-1_0.html) defines how a provider can send a *logout token* to the relevant relying parties when an authenticated session linked to an ID token becomes invalid.

When backchannel logout is enabled, AM sends a logout token to a URL configured in the relying party's client profile. This URL must be a page or application in the relying party that is capable of dealing with the token.

AM stores a list of logged in clients in the authenticated session so that, when it becomes invalid, AM has a list of URLs to which it needs to send the logout token to.

This is particularly important in scenarios where different relying parties use the same authenticated session to obtain ID tokens. By storing the URLs in the session itself, AM ensures that all the related relying parties receive a logout token.

Next, the relying party validates the logout token, and clears any state associated with the combination of session ID, user, and issuer. Finally, it sends a response to AM with the outcome of the logout, as explained in *2.8 Back-Channel Logout Response* of the draft.

Depending on which status code AM receives, it logs an audit event of the type `AM-BACK-CHANNEL-LOGOUT` in the activity log file, which resembles the following:

```json
{
  "_id":"cb52bc45-549d-4a9c-86cc-20d7500e333b-96127",
  "eventName":"AM-BACK-CHANNEL-LOGOUT",
  "transactionId":"cb52bc45-549d-4a9c-86cc-20d7500e333b-94750",
  ...
  ...
  "operation":"Sent logout request to https://rp.example.com:8443/logout, which responded with HTTP code 200.",
  ...
}
```

AM will log the HTTP code that the relying party returns, or an error if there is no response before the request times out.

The following simplified diagram illustrates a possible backchannel logout flow:

![Backchannel Logout Flow](_images/backchannel-logout.svg)Figure 1. Backchannel Logout Flow

## Backchannel logout limitations

The current implementation of backchannel logout in AM has the following limitations:

* It is only supported for [server-side](../am-sessions/cts-based-sessions.html) sessions.

* AM currently only supports backchannel logout when acting as the provider.

## The logout token

The logout token is defined in section *2.4 Logout Token* of the draft. The following is an example logout token issued by AM, and the description of its claims:

```none
{
  "aud": "backchannelConfidentialClient", (1)
  "sub": "(usr!bjensen)", (2)
  "auditTrackingId": "cb52bc45-549d-4a9c-86cc-20d7500e333b-91288", (3)
  "iss": "https://am.example.com:8443/am/oauth2/backchannelSubRealm", (4)
  "cause": "CLIENT_LOGOUT", (5)
  "exp": 1731318726, (6)
  "iat": 1614005410, (7)
  "jti": "1cd8805d-6fc0-4699-a33f-a75d45b24e9e", (8)
  "events": { (9)
    "http://schemas.openid.net/event/backchannel-logout": {}
  },
  "sid": "mTNo042FCiPkgAJKjdjgCvBWvVYTB1d+zreDBnZAqvM=" (10)
}
```

|        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1**  | The audience of the logout token. In this case, the client that requested the ID token(s) related to the user that has been logged out.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **2**  | The subject of the logout token. In this case, the user that has been logged out. The subject of the logout token matches the subject of the ID token(s).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **3**  | (AM-specific) Determines the unique audit identifier for this token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **4**  | The authorization server that issued the logout token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **5**  | (AM-specific) Documents the reason why the user was logged out, if known. Possible values are:- CLIENT\_LOGOUT. AM has received a call to the [sessions endpoint](../am-authentication/logout-using-rest.html) to end the session.

- SESSION\_TERMINATION. An administrative user has terminated the session.

- SESSION\_MAX\_TIMEOUT. AM terminated the session because it reached its maximum time-to-live.

- SESSION\_IDLE\_TIMEOUT. AM terminated the session because it reached its maximum idle time. If the reason is not known, the claim does not show in the token.                                                                                                                                                                                                                              |
| **6**  | The expiration time of the logout token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **7**  | The creation time (issued at time) of the logout token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **8**  | The unique identifier for the logout token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **9**  | A JSON object that contains the `http://schemas.openid.net/event/backchannel-logout` URL, which marks the JWT as a logout token. The value of the object is always an empty JSON object (`{}`).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **10** | A session ID that identifies the relying party's session with the provider. The `sid` in the logout token matches the `sid` in the related ID token, and therefore, the relying party can match both when doing session clean up operations. If a relying party requests several ID tokens using the same authenticated session, they all share the same `sid`. However, if several relying parties use the same authenticated session to obtain ID tokens, their \`sid\`s are different. When the authenticated session becomes invalid, AM sends logout tokens to all relying parties involved. Note that the claim is only populated in the logout token if Backchannel Logout Session Required is enabled in the client profile. Learn more in [Enable backchannel logout](#enabling-backchannel-logout). |

## Enable backchannel logout

To enable backchannel logout, first configure the OAuth 2.0 provider for the realm, and next configure the clients that will use the feature:

1. Configure the OAuth 2.0 provider:

   * In the AM admin UI, go to Realms > *realm name* > Services > OAuth2 Provider > Advanced OpenID Connect.

   * Enable OIDC Session Management , if it is not already enabled.

     |   |                                                                                                                                                                                                                                                           |
     | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | OIDC Session Management is enabled by default, and it is also required for [Session Management](session-management.html).When enabled, AM always adds a `sid` to the ID tokens, regardless of whether clients have logout URLs configured in them or not. |

   * Save your changes.

   * Review the logout token signing secret.

     AM signs logout tokens with the same secret it uses to sign ID tokens. Learn more in [Secret label mappings for signing OpenID Connect tokens](../security/secret-mapping.html#secrets-oidc-IDtoken-signing-secretIDs).

   * Configure AM to encrypt the logout tokens.

     Encryption is disabled by default. To enable it, you must configure ID token encryption as well. For more information, see [Encrypt ID tokens and backchannel logout tokens](encrypting-oidc-idtokens.html).

2. Configure the clients:

   * In the AM admin UI, go to Realms > *realm name* > Applications > OAuth 2.0 > Clients > *client ID* > OpenID Connect.

   * In the Back Channel Logout URI field, set the URL in the relying party to where AM will send the logout token during backchannel logout.

     This URL can use the http or the https schemes, and may contain a port, a path, or query parameters, depending on the implementation of the relying party. For example, `https://my-rp.example.com:8443/logout`.

   * If the logout token must contain the session ID (`sid`), enable Backchannel Logout Session Required.

   * Save your changes, and configure as many clients as required.

     |   |                                                                                          |
     | - | ---------------------------------------------------------------------------------------- |
     |   | Clients registering dynamically can provide their backchannel logout configuration, too. |

## The backchannel logout Postman collection

Use the backchannel logout [Postman](https://www.postman.com/) collection to try out the functionality. The REST calls and their prerequisites are provided as a downloadable JSON file collection.

Backchannel logout relies on a relying party that can acknowledge the logout token and send a response back to AM. To emulate this, you can send a mock server in Postman.

Perform the following steps to download, configure, and run the backchannel logout Postman collection:

1. Download and install [Postman](https://www.postman.com/downloads).

2. Download the [OpenID Connect backchannel logout collection](../_attachments/collections/ForgeRock_OIDC_Backchannel_Logout_Collection.json).

3. Import the collection in Postman:

   * Go to File > Import …​ > Upload Files.

   * Select the collection you downloaded, and click Open. Then, click Import.

4. Create a Postman mock server.

   Follow the instructions in the [Setting Up Mock Servers](https://learning.postman.com/docs/designing-and-developing-your-api/mocking-data/setting-up-mock) in the *Postman Documentation*.

   The mock server will work as the relying party. Inspect the requests sent to the mock server to see the logout tokens sent by AM.

   When you create a mock server, Postman presents you with some information and the URL you can use to call it. For example, `https://f4a08510-2f95-4990-8cb0-5a4f281a8bac.mock.pstmn.io`.

   Save this URL; you need to configure it in the following step of this procedure.

5. Configure the collection's variables to suit your environment:

   * In Postman, on the Collections tab, select the ForgeRock OpenID Connect Backchannel Logout Collection. From the more options menu (`…​`), select Edit.

   * Click on the Variables tab, and change at least the value of the following variables:

     * `URL_base`

       Configure the URL of your AM environment. For example, `https://am.example.com:8443/am`.

     * `admin_password`

       Configure the password of the administrative user, such as `amAdmin`, that the collection will use to create AM configuration objects.

     * `back_channel_logout_uri`

       Configure the backchannel logout URL of your relying party, or the URL of the Postman mock server.

   * Click Update to save your changes.

     You are ready to start running the collection.

   The collection is divided into the following folders:

   * `Prerequisites`, containing REST calls to configure a new realm containing an authorization server, and to create the clients and users required to run the collection.

   * `OpenID Connect Backchannel Logout Flow`, containing REST calls for the authorization code grant flow, and to log out the demo user.

   * `Mock Response`, containing a REST call to send AM a response when using the mock server.

6. Run the collection.

7. (Mock server only) On the mockup server window, check the request body of the `Mock Up Response` to see the logout token.

   > **Collapse: Example Postman Mock Up Server Window with the Response Body Expanded**
   >
   > ![A screenshot of the Postman mockup server window showing the response body expanded. The logout token is also visible.](_images/backchannel-logout-postman-mock-up.png)

8. Inspect the contents of the logout token.

   Tokens created by the collection are not encrypted.

9. Open the AM activity audit log.

   Check for an entry with event name `AM-BACK-CHANNEL-LOGOUT` with the logout request, and the relying party's response. For example:

   ```json
   {
    "_id":"cb52bc45-549d-4a9c-86cc-20d7500e333b-96127",
    "eventName":"AM-BACK-CHANNEL-LOGOUT",
    "transactionId":"cb52bc45-549d-4a9c-86cc-20d7500e333b-94750",
    ...
    ...
    "operation":"Sent logout request to https://f4a08510-2f95-4990-8cb0-5a4f281a8bac.mock.pstmn.io, which responded with HTTP code 200."
    ...
    }
   ```

---

---
title: Backchannel request grant
description: Implement client-initiated backchannel authentication (CIBA) in PingAM to obtain user consent without browser redirection through an authentication device
component: pingam
version: 8.1
page_id: pingam:am-oidc1:openid-connect-backchannel-request-flow
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oidc1/openid-connect-backchannel-request-flow.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OpenID Connect (OIDC)", "Standards"]
page_aliases: ["oidc1-guide:openid-connect-backchannel-request-flow.adoc"]
section_ids:
  the_backchannel_flow: The backchannel flow
  proc-prepare-for-ciba: Prepare for CIBA
  configure_the_service: Configure the service
  register_an_rp: Register an RP
  proc-auth-id-ciba: Get an auth request ID
  proc-auth-req-id-token-ciba: Exchange an auth request ID for tokens
  additional_oidc_claims: Additional OIDC claims
---

# Backchannel request grant

* Endpoints

  * [/oauth2/bc-authorize](../am-oauth2/oauth2-bc-authorize-endpoint.html)

  * [/oauth2/access\_token](../am-oauth2/oauth2-access_token-endpoint.html)

  * [/oauth2/userinfo](rest-api-oidc-userinfo-endpoint.html)

Use the backchannel request grant for [client-initiated backchannel authentication](https://openid.net/specs/openid-client-initiated-backchannel-authentication-core-1_0.html) (CIBA).

|   |                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The OIDC backchannel request grant (CIBA) described here is distinct from the AM [backchannel authentication](../am-authentication/backchannel-authentication.html) feature. |

CIBA lets a relying party (RP), the *consumption device*, get an end user's consent without redirection through the end user's browser. Instead, the end user authenticates and grants consent through an *authentication device* such as an authenticator application or a mobile banking application on the user's mobile phone.

AM applies the guidelines suggested by the OpenID [Financial-grade API (FAPI) Working Group](https://openid.net/wg/fapi/) to implement CIBA.

## The backchannel flow

![AM supports the backchannel grant flow.](_images/oidc-ciba.svg)

1. The RP has a user identifier and requires the end user's consent. It prepares a signed Json Web Token (JWT).

2. The RP sends an HTTP POST request with the signed JWT to AM, the OpenID provider (OP).

3. The OP validates the signature using the RP's public key and verifies the JWT. If the JWT is valid, the OP returns an `auth_req_id` and a polling interval.

4. The RP polls the OP with the `auth_req_id`, waiting for the end user's authorization. If the RP does not respect the polling interval, the OP returns an error.

5. The OP sends a push notification with the `binding_message` to request the end user's authorization.

6. The end user authorizes the request with the authorization gesture on their authentication device; for example, the user clicks a button in their authenticator application or provides their fingerprint.

7. The OP returns an access token and an ID token to the RP.

   The RP can use the ID token subject ID claim as the end user's identity.

8. If the RP requires additional claims, it sends a request to the [/oauth2/userinfo](rest-api-oidc-userinfo-endpoint.html) endpoint with the access token for authorization.

9. If the access token is valid, the `/oauth2/userinfo` endpoint returns any additional claims.

   The RP can use the subject ID and the additional claims to identify the end user.

## Prepare for CIBA

### Configure the service

1. Create a journey such as the following:

   ![The journey requires specific authentication nodes for CIBA.](_images/ciba-push-tree.png)

   The journey uses these nodes:

   * [Username Collector node](https://docs.pingidentity.com/auth-node-ref/8.1/am-only/username-collector.html)

   * [Push Sender node](https://docs.pingidentity.com/auth-node-ref/8.1/push-sender.html)

   * [Push Result Verifier node](https://docs.pingidentity.com/auth-node-ref/8.1/push-result-verifier.html)

   * [Polling Wait node](https://docs.pingidentity.com/auth-node-ref/8.1/polling-wait.html)

   Learn more in [Push authentication journeys](../am-authentication/push-authentication-journeys.html).

   |   |                                                                                                                                                                                                                                                                                  |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Don't configure a CIBA journey as a [transactional authentication tree](../am-authentication/configure-auth-trees.html#configure-transactional-auth-tree). If a CIBA journey is configured as transactional only, the journey won't run because CIBA isn't a transactional flow. |

2. In the AM admin UI, go to Realms > *realm name* > Services > OAuth2 Provider > Advanced and make sure the Grant Types field includes `Back Channel Request`.

   Save any changes you make.

3. Associate the journey with incoming `acr_values`:

   1. Switch to the Advanced OpenID Connect tab of the OAuth 2.0 provider configuration.

   2. In the OpenID Connect acr\_values to Auth Chain Mapping box:

      1. Set the Key to the value that will be passed in through the `acr_values` claim of the incoming CIBA request.

      2. Set the Value to the name of your journey.

      3. Click Add.

   3. Save your changes.

   For more information, refer to [The `acr` claim](oidc-authentication-requirements.html#acr-claim).

### Register an RP

1. [Register the RP as a confidential client application](../am-oauth2/oauth2-register-client.html) with the following settings:

   * Name

     `<human-readable-name>`

   * Client ID

     `<rp-client-id>` (must match the `iss` in the RP's signed JWTs)

   * Client Secret

     `<rp-client-secret>`

   * Scopes

     `openid`\
     `profile`

2. Configure access to the RP's public keys so AM can verify JWT signatures:

   1. On the Signing and Encryption tab, choose the Public key selector.

   2. Depending on the Public key selector value you chose, set one of the other fields appropriately.

   3. Save your changes.

   For example:

   * Set Public key selector `JWKs_URI` and Json Web Key URI to the URL where the RP publishes its keys.

     This method simplifies key rotation as AM rereads the keys periodically.

   * Set Public key selector to `JWKs` and set Json Web Key to a [JWK](https://www.rfc-editor.org/info/rfc7517) set similar to the following:

     ```json
     {
       "keys": [
         {
           "kty": "EC",
           "use": "sig",
           "crv": "P-256",
           "kid": "myCIBAKey",
           "x": "m0CkpWpZyGu-FLRLjCGBVGC7Fwm5vGt8Lm3HhYU4ylg",
           "y": "U8NMtO-C2c3yhu2I_ApAELttmaittfPNPQaIJxvTCHk",
           "alg": "ES256"
         }
       ]
     }
     ```

     You can store more than one key in the JWK set.

## Get an auth request ID

Follow these steps as RP to get a CIBA authentication request ID:

1. Prepare a signed [JWT](https://www.rfc-editor.org/info/rfc7523) with the required claims in the payload:

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

   For example:

   ```json
   {
     "aud": "https://am.example.com:8443/am/oauth2/realms/root/realms/alpha",
     "binding_message": "Allow ExampleBank to transfer £50 from 'Main' to 'Savings'? (EB-0246326)",
     "acr_values": "push",
     "exp": 1675681183,
     "iss": "<rp-client-id>",
     "login_hint": "<end-user-id>",
     "scope": "openid profile"
   }
   ```

   AM ignores keys specified in JWT headers, such as `jku` and `jwe` and uses the keys specified in the RP profile to verify the JWT signature.

2. Send an HTTP POST to the [/oauth2/bc-authorize](../am-oauth2/oauth2-bc-authorize-endpoint.html) endpoint with the signed JWT in the payload:

   ```bash
   $ curl \
   --request POST \
   --user '<rp-client-id>:<rp-client-secret>' \
   --data 'request=<signed-jwt>' \
   'https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/bc-authorize'
   ```

   AM returns a JSON object with the `auth_req_id` value:

   ```json
   {
     "auth_req_id": "<auth-req-id>",
     "expires_in": 600,
     "interval": 2
   }
   ```

   AM sends a push notification with the `binding_message` to the end user.

## Exchange an auth request ID for tokens

To get an access token and ID token as the RP, poll the [/oauth2/access\_token](../am-oauth2/oauth2-access_token-endpoint.html) endpoint with HTTP POST requests having the following parameters:

* `grant_type=urn:openid:params:grant-type:ciba`

* `auth_req_id=<auth-req-id>`

For example:

```bash
$ curl \
--request POST \
--user '<rp-client-id>:<rp-client-secret>' \
--data 'grant_type=urn:openid:params:grant-type:ciba' \
--data 'auth_req_id=<auth-req-id>' \
'https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/access_token'
```

The response depends on the end user and the polling interval:

* After the end user has authorized the operation, AM returns an ID token and an access token:

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

* Before the end user authorizes the operation, AM returns an HTTP 400 Bad Request status:

  ```json
  {
    "error_description": "End user has not yet been authenticated",
    "error": "authorization_pending"
  }
  ```

* The auth ID response includes a polling `interval`. The RP must wait `interval` seconds before retrying the request (default: two seconds). If the RP does not wait long enough between retries, AM returns an HTTP 400 Bad Request status:

  ```json
  {
    "error_description": "The polling interval has not elapsed since the last request",
    "error": "slow_down"
  }
  ```

## Additional OIDC claims

An RP can request additional claims about the end user with the access token at the [/oauth2/userinfo](rest-api-oidc-userinfo-endpoint.html) endpoint:

```bash
$ curl \
--request GET \
--header "Authorization Bearer <access-token>" \
"https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/userinfo"
{
  "name": "<end-user-display-name>",
  "family_name": "<end-user-family-name>",
  "given_name": "<end-user-given-name>",
  "sub": "<end-user-id>",
  "subname": "<end-user-id>"
}
```

---

---
title: Claims
description: Understand how OpenID Connect claims provide user information to relying parties and configure PingAM to map scopes and profile data to claims
component: pingam
version: 8.1
page_id: pingam:am-oidc1:understanding-openid-connect-scopes-and-claims
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oidc1/understanding-openid-connect-scopes-and-claims.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OpenID Connect (OIDC)", "Standards"]
page_aliases: ["oidc1-guide:understanding-openid-connect-scopes-and-claims.adoc"]
---

# Claims

OpenID Connect relies on claims to provide information about the end user to the relying parties.

> **Collapse: What are claims?**
>
> A claim is a piece of information about the end user that the relying party or client can use to provide them a service.
>
> Consider a page that lets the end user register using their Google account information instead of providing the information themselves. The page requests a set of *claims* about the end user *from Google* and uses the information on the claims to set up the account without user interaction.
>
> If the end user agrees to share access to their claims, OpenID providers can return them in two ways: either as key pairs in the ID token, or by making them available at the `userinfo` endpoint. Part of implementing OpenID Connect in your environment is deciding which claims are safe to travel in the ID token, and which ones require the client to access the endpoint.
>
> ID tokens contain additional claims that are not related to user information directly, but that are relevant to the flow, the relying party, or the authorization server. These are similar to those contained in access tokens; for example, `iss`, `aud`, `exp`, and others.
>
> Read more:
>
> * [Section 2](https://openid.net/specs/openid-connect-core-1_0.html#IDToken) of the OpenID Connect specification
>
> * [Section 5](https://openid.net/specs/openid-connect-core-1_0.html#Claims) of the OpenID Connect specification

|   |                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | AM supports *Normal Claims*, as specified in section 5.6 of the specification. AM does not support the optional *Aggregated Claims* and *Distributed Claims* representations. |

When AM is configured as an authorization server, a scope is a concept. For example, Facebook has an OAuth 2.0 scope named `read_stream`. AM returns allowed scopes in the access token, but it does not associate any data with them.

When AM is configured as an OpenID provider, scopes can relate to data in a user profile by making use of one or more claims.

As each claim represents a piece of information from the user profile, AM displays the actual data the relying party will receive if the end user consents to sharing it:

![The OpenID Connect consent page can show the values associated with the claims that make up the requested scopes.](_images/oidc-consent.png)Figure 1. OpenID Connect Consent Page

AM maps scopes and profile data to claims using a script configured in the OAuth2 provider service. By default, the script maps several user profile attributes to the `profile` scope:

**OpenID Connect Scope Default Claim Mappings**

| Claim         | User profile attribute |
| ------------- | ---------------------- |
| `given_name`  | `givenname`            |
| `zoneinfo`    | `preferredtimezone`    |
| `family_name` | `sn`                   |
| `locale`      | `preferredlocale`      |
| `name`        | `cn`                   |

After a successful flow, the OpenID provider returns an ID token with the relevant claims. However, for security reasons, AM does not return scope-derived claims in the ID token by default.

> **Collapse: Request claims in ID tokens**
>
> Sometimes you may need the provider to return scope-derived claims in the ID token. For example, when claims are related to authentication conditions or rules the end user needs to satisfy before being redirected to particular resources.
>
> You can configure AM to either return all scope-derived claims in the ID token, or just the ones specified in the request:
>
> * To configure the provider to always return scope-derived claims in the ID token, enable Always Return Claims in ID Tokens (Realms > *realm name* > Services > OAuth2 Provider > Advanced OpenID Connect).
>
>   This option is disabled by default because of the security concerns of returning claims that may contain sensitive user information.
>
> * To request that the provider only include certain scope-derived claims in the ID token, enable the property Enable "claims\_parameter\_supported" (Realms > *realm name* > Services > OAuth2 Provider > Advanced OpenID Connect) and request said claims in the `claims` parameter.
>
> > **Collapse: Voluntary and essential claims in the claims parameter**
> >
> > Claims specified using the `claims` parameter can be voluntary or essential:
> >
> > * **Essential**. The relying party specifies a number of claims that are necessary to ensure a good experience to the end user.
> >
> >   For example, to provide personalized services, the relying party may require the end user's phone number to send them an SMS.
> >
> > * **Voluntary**. The relying party specifies a number of claims that are useful but not required to provide services to the end user.
> >
> > For an example on requesting voluntary and essential claims, refer to [Demonstrate authentication requirements](oidc-authentication-requirements.html#request-acr-example).
>
> Clients can still retrieve additional claims from the `/oauth2/userinfo` endpoint.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The OAuth 2.0 provider's Supported Claims field restricts the claims that can be granted in ID tokens, but not the claims a client can register with during dynamic client registration.You can also use this field to configure how AM presents the claims in the AM consent screen. By default, scope-derived claims are not configured to display in the consent screen. You can either configure clients to use [implied consent](../am-oauth2/oauth2-manage-consent.html#skip-consent), or manually configure the claims to display.> **Collapse: How to configure claims in the AM consent screen**
>
> Configure how claims appear in the consent screen by client or by realm (in the OAuth 2.0 provider service). For examples, see the Supported Claims field in the provider's [Advanced](../setup/services-configuration.html#global-oauth-oidc-advanced) reference, or the Claim(s) field in [Core properties](../am-oauth2/oauth2-register-client.html#configure-oauth2-oidc-client).
>
> Claims may be entered as simple strings or pipe-separated strings representing the internal claim name, locale, and localized description. For example: `name\|en\|Your full name`.
>
> If the description is omitted, the claim is not displayed in the consent page. This may be useful when the client requires claims that are not meaningful for the end user.
>
> Client-level configuration overrides that at provider level. |

---

---
title: Customize claims with the OpenID Connect 1.0 claims script
description: Use the OIDC Claims script to customize claims issued in ID tokens and returned from the userinfo endpoint in PingAM
component: pingam
version: 8.1
page_id: pingam:am-oidc1:scripted-oidc-claims
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oidc1/scripted-oidc-claims.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OpenID Connect (OIDC)", "Standards", "Customization", "Extensibility"]
page_aliases: ["oidc1-guide:scripted-oidc-claims.adoc"]
---

# Customize claims with the OpenID Connect 1.0 claims script

The `OIDC Claims` script is part of the user info claims plugin, one of the OAuth 2.0 plugin extension points provided by AM. Use this extension point when issuing an ID token or during a request to the `/userinfo` OpenID Connect endpoint.

To configure a different script of the type `OIDC Claims`, go to Realms > *realm name* > Services > OAuth 2.0 Provider > Plugins, and select it in the OIDC Claims Script drop-down menu.

Alternatively, to configure a different script as the default for all new OAuth2 providers, update the setting in Configure > Global Services > OAuth2 Provider > Plugins.

To examine the contents of the default OIDC claims script and to view the available script properties, go to Realms > *realm name* > Scripts, and select the OIDC Claims Script.

|   |                                                                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For information about how to configure OAuth 2.0 plugins, see [Customize OAuth 2.0](../am-oauth2/customizing-oauth2-scopes.html).For details about the user info claims plugin, see [OIDC claims](../am-oauth2/plugins-user-info-claims.html). |

---

---
title: Customize dynamic client registration
description: Configure PingAM to run custom scripts after dynamic client registration requests to modify client profiles and perform custom actions
component: pingam
version: 8.1
page_id: pingam:am-oidc1:dynamic-client-registration-script
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oidc1/dynamic-client-registration-script.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OpenID Connect (OIDC)", "Setup &amp; Configuration", "Scripts"]
page_aliases: ["oidc1-guide:dynamic-client-registration-script.adoc"]
section_ids:
  dcr-create-script: Create a script
  dcr-configure-provider: Configure OAuth 2.0 provider to use the script
  dcr-test: Test your changes
---

# Customize dynamic client registration

You can configure AM to run a script after it has processed a dynamic client registration request. This scripted extension point lets you perform custom actions to modify the client profile, for example, by updating client attributes or manipulating PingIDM data to create client relationships.

The script is called after the following dynamic client registration operations:

* [Create](oauth2-dynamic-client-registration.html#dynamic-registration-options)

* [Update](oauth2-dynamic-client-registration.html#dynamic-management-update)

* [Delete](oauth2-dynamic-client-registration.html#dynamic-management-delete)

## Create a script

AM includes [a sample script](../am-scripting/sample-scripts.html#oauth2-dynamic-client-registration-js) that updates client attributes with values from the request.

You can use this as a template to create your own custom script.

1. In the AM admin UI, [create a script](../am-scripting/manage-scripts-console.html#create-scripts-with-console) with the Script Type set to `OAuth2 Dynamic Client Registration`.

2. Write your own or copy the sample script into the Script field.

   A dynamic client registration script is a [next-generation](../am-scripting/next-generation-scripts.html) script. You have access to all [common](../am-scripting/script-bindings.html) next-generation bindings, such as `openidm`, `httpClient`, and `utils`, to help you modify the client profile.

   |   |                                                                                                                        |
   | - | ---------------------------------------------------------------------------------------------------------------------- |
   |   | Learn about the bindings you can use in the [Dynamic client registration scripting API](../am-scripting/dcr-api.html). |

3. Save your changes.

## Configure OAuth 2.0 provider to use the script

After creating your script, you must configure AM to use it.

1. In the AM admin UI, go to Realms > *realm name* > Services > OAuth2 Provider > Client Dynamic Registration to configure a specific OAuth 2.0 provider.

   To set your script as the default for all new OAuth 2.0 providers, go to Configure > Global Services > OAuth2 Provider > Client Dynamic Registration.

2. Set Dynamic Client Registration Script to the script name you want to use.

3. Save your changes.

## Test your changes

1. Perform a request to register, update, or delete a client profile dynamically.

2. The provider runs the script after the operation completes successfully.

   *The script isn't invoked if the operation fails.*

3. Verify that the script makes the changes as expected.

   For the sample script, check for the following modifications depending on the type of request:

   * `CREATE` operation

     The script makes the following changes:

     * Sets the client attribute `com.forgerock.openam.oauth2provider.grantTypes` to `authorization_code` and the grant type for the request

     * Sets the client type to `Public`

     * Sets the client scopes to `read` and `write`

   * `UPDATE` operation

     The script adds the software statement's `redirect_uris` property to the client attribute `com.forgerock.openam.oauth2provider.redirectionURIs`.

   * `DELETE operation`

     The script makes no changes.

|   |                                                                                                                                                                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | You can find the property names used to update client attributes, such as `com.forgerock.openam.oauth2provider.grantTypes` by querying the [/realm-config/agents/OAuth2Client](../am-oauth2/rest-api-oauth2-client-admin-endpoint.html#query-oauth2-clients) endpoint.For backward compatibility, PingDS property names are also accepted. |

---

---
title: Dynamic client registration
description: Set up client applications programmatically using OAuth 2.0 and OpenID Connect dynamic client registration protocols
component: pingam
version: 8.1
page_id: pingam:am-oidc1:oauth2-dynamic-client-registration
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oidc1/oauth2-dynamic-client-registration.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OpenID Connect (OIDC)", "Standards", "Self-Service", "Setup &amp; Configuration"]
page_aliases: ["oidc1-guide:oauth2-dynamic-client-registration.adoc"]
section_ids:
  dynamic-registration-options: Dynamic registration options
  registration-open: Open registration
  registration-mtls-auth: Registration with mutual TLS authentication
  registration-access-token: Registration with an access token
  registration-software-statement: Registration with a software statement
  register-oauth2-client-dynamic: Enable dynamic client registration
  dynamic-registration-oauth2-provider: Update OAuth 2.0 provider settings
  dynamic-registration-registration-client: Register a client profile for access tokens
  dynamic-registration-software-publisher: Register a software publisher profile
  registration_examples: Registration examples
  register-oauth2-client-dynamic-open-example: Open registration
  register-oauth2-client-dynamic-mTLS: Registration with mutual TLS authentication
  register-oauth2-client-dynamic-access-token-example: Registration with an access token
  register-oauth2-client-dynamic-software-statement-example: Registration with a software statement
  dynamic-client-registration-management: Manage client profiles
  dynamic-management-read: Read a client profile
  dynamic-management-update: Update a client profile
  dynamic-management-delete: Delete a client profile
---

# Dynamic client registration

Dynamic client registration lets you set up a client application profile programmatically.

|   |                                                                                                                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To create and manage large numbers of clients without impacting system performance, use [Scalable OAuth 2.0 clients](../am-oauth2/oauth2-scalable-clients.html).To customize dynamic client registration, [configure a script](dynamic-client-registration-script.html) to run after a successful create, update, or delete operation. |

## Dynamic registration options

AM supports dynamic registration as defined by RFC 7591 [OAuth 2.0 Dynamic Client Registration Protocol](https://www.rfc-editor.org/rfc/rfc7591.html) and [OpenID Connect (OIDC) Dynamic Client Registration 1.0](https://openid.net/specs/openid-connect-registration-1_0.html). The specifications describe the dynamic registration options for OAuth 2.0 and OIDC client applications.

|   |                                                                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | AM returns an error when a dynamic client registration request payload includes incorrect information or specifies unsupported signing and encryption algorithms.For example, if a public client requests symmetric signing or encryption, the request results in an error because public clients can't have a client secret to use for symmetric encryption. |

### Open registration

The application registers its profile without an access token.

AM generates `client_id` and `client_secret` values. AM ignores any values provided in the profile for these properties.

You can use this method to develop and test client registration. This method doesn't limit the number of client registrations. If you use it in production, also require a software statement.

Learn more in the [example open registration](#register-oauth2-client-dynamic-open-example).

### Registration with mutual TLS authentication

The application provides a self-signed or a CA-signed X.509 certificate for authentication, as defined in the Internet-Draft [OAuth 2.0 Mutual TLS Client Authentication and Certificate Bound Access Tokens](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-mtls-12).

Learn more in the [example registration with a mutual TLS authentication](#register-oauth2-client-dynamic-mTLS).

### Registration with an access token

The application registers its profile with an access token for authorization.

The specification does not describe how the client obtains the access token. In AM, you register an initial OAuth 2.0 client application manually, and use this application to obtain the access token on behalf of the client requesting registration.

To register the `logo_uri`, `client_uri`, and `policy_uri` the access token must include a special scope; default: `dynamic_client_registration`.

Learn more in the [example registration with an access token](#register-oauth2-client-dynamic-access-token-example).

### Registration with a software statement

The application registers its profile with a *software statement*.

A software statement is a JSON Web Token (JWT) that holds registration claims about the client, such as its issuer and redirection URIs.

A software statement is issued by a *software publisher*. The software publisher encrypts and signs the claims in the software statement.

You store software publisher details in a software publisher profile. The software publisher profile identifies the issuer included in software statements. It provides access to the secret or the keys to decrypt software statement JWTs and to verify their signatures. When the client registers dynamically with a software statement, AM uses the software publisher profile to determine whether it can trust the software statement.

The protocol specification doesn't describe how the client obtains the software statement JWT. AM expects the software publisher to construct the JWT according to the settings in its profile.

Learn more in the [example registration with a software statement](#register-oauth2-client-dynamic-software-statement-example).

## Enable dynamic client registration

| Option                                         | Task                                                                                                                                                                                  |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Open registration                              | [Update OAuth 2.0 provider settings](#dynamic-registration-oauth2-provider)                                                                                                           |
| Registration with a certificate                | [Update OAuth 2.0 provider settings](#dynamic-registration-oauth2-provider)Find example steps in [Registration with mutual TLS authentication](#register-oauth2-client-dynamic-mTLS). |
| Registration with an access token              | [Register a client profile for access tokens](#dynamic-registration-registration-client)                                                                                              |
| Registration requires a software statement JWT | [Update OAuth 2.0 provider settings](#dynamic-registration-oauth2-provider)[Register a software publisher profile](#dynamic-registration-software-publisher)                          |

### Update OAuth 2.0 provider settings

To enable open registration and registration with a software statement, update the OAuth 2.0 provider configuration for the realm:

1. In the AM admin UI, go to Realms > *realm name* > Services > OAuth2 Provider and switch to the Client Dynamic Registration tab.

2. To allow open registration without an access token, enable Allow Open Dynamic Client Registration.

3. To require a software statement to register, enable Require Software Statement for Dynamic Client Registration, and edit the Required Software Statement Attested Attributes list to include all the required claims.

4. Save your work.

5. To change the scopes a client can register, switch to the Advanced tab and update the Client Registration Scope Allowlist field.

6. Save your work.

Learn more in the [Client dynamic registration](../setup/services-configuration.html#global-oauth-oidc-client-dynamic-registration) reference.

### Register a client profile for access tokens

To enable dynamic registration with an access token, manually register a service application to provide the access tokens:

1. In the AM admin UI, go to Realms > *realm name* > Applications > OAuth 2.0 > Clients and click + Add Client.

2. Provide the client application details; for example:

   * Client ID

     `registration-service`

   * Client Secret

     `mySecret`

   * Scopes

     `dynamic_client_registration`

   If the string for the special scope is not the default, use the scope specified in the OAuth 2.0 provider configuration Client Dynamic Registration > Scope to give access to dynamic client registration field.

3. Save your work.

### Register a software publisher profile

To enable dynamic registration with a software statement JWT, register a software publisher:

1. In the AM admin UI, go to Realms > *realm name* > Applications > OAuth 2.0 > Software Publisher and click [icon: plus, set=fa]Add Software Publisher Agent.

2. Add the basic settings as necessary before you click Create:

   * Agent ID

     Required identifier for the profile.

   * Software publisher secret

     Secret required when the publisher uses HMAC symmetric encryption for the JWTs.

   * Software publisher issuer

     Required issuer identifier to match the `iss` claim in JWTs.

3. Configure the appropriate security settings:

   * If you provide the JSON Web Key (JWK) by URI rather than by value, where the Public key selector is `JWKs_URI`, AM must access the JWKs when processing registration requests.

   * If the publisher uses symmetric encryption, where the Software statement signing Algorithm is `HS256`, `HS384`, or `HS512`, the Software publisher secret must match the `k` value in the JWK.

4. Save your work.

The software publisher provides client applications using dynamic registration with a valid software statement JWT. Valid software statement JWTs must have:

* All the required claims listed in the OAuth 2.0 provider's Required Software Statement Attested Attributes.

* An issuer (`iss`) claim matching a publisher profile's Software publisher issuer.

These constraints apply to software statement JWTs:

* Compressed JWTs must not be larger than 32 KiB (32768 bytes) when uncompressed.

* AM ignores keys specified in JWT headers, such as `jku` and `jwe`.

## Registration examples

Review the following dynamic client registration examples.

The client must read and store the dynamic registration response. The response includes important information about the client, such as:

* The generated client ID and the generated client secret for confidential clients.

  You can't choose the client ID or client secret when registering an application dynamically.

* The URL and access token required to [update the client profile](#dynamic-client-registration-management).

### Open registration

The following example assumes you have completed the task to [Update OAuth 2.0 provider settings](#dynamic-registration-oauth2-provider).

When you have enabled Allow Open Dynamic Client Registration, register a client dynamically.

Include a `client_name` in the payload as the human-readable name to display to resource owners:

```bash
$ curl \
--request POST \
--header 'Content-Type: application/json' \
--data '{
  "redirect_uris": ["https://client.example.com/callback"],
  "client_name#en": "My Client",
  "client_name#ja-Jpan-JP": "\u30AF\u30E9\u30A4\u30A2\u30F3\u30C8\u540D",
  "client_uri": "https://client.example.com/"
}' \
'https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/register'
```

> **Collapse: Show the response**
>
> ```json
> {
>   "authorization_signed_response_alg": "RS256",
>   "request_object_encryption_alg": "",
>   "introspection_encrypted_response_alg": "RSA-OAEP-256",
>   "client_uri": "https://client.example.com/",
>   "default_max_age": 1,
>   "application_type": "web",
>   "introspection_encrypted_response_enc": "A128CBC-HS256",
>   "introspection_signed_response_alg": "RS256",
>   "client_name#en": "My Client",
>   "userinfo_encrypted_response_enc": "",
>   "registration_client_uri": "https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/register?client_id=<generated-client-id>",
>   "client_type": "Confidential",
>   "userinfo_encrypted_response_alg": "",
>   "registration_access_token": "<generated-registration-access-token>",
>   "client_id": "<generated-client-id>",
>   "token_endpoint_auth_method": "client_secret_basic",
>   "userinfo_signed_response_alg": "",
>   "public_key_selector": "x509",
>   "scope": "address phone openid profile email",
>   "require_pushed_authorization_requests": false,
>   "authorization_code_lifetime": 0,
>   "client_secret": "<generated-client-secret>",
>   "user_info_response_format_selector": "JSON",
>   "tls_client_certificate_bound_access_tokens": false,
>   "backchannel_logout_session_required": false,
>   "id_token_signed_response_alg": "RS256",
>   "default_max_age_enabled": false,
>   "token_intro_response_format_selector": "JSON",
>   "subject_type": "public",
>   "grant_types": ["authorization_code"],
>   "jwt_token_lifetime": 0,
>   "id_token_encryption_enabled": false,
>   "redirect_uris": ["https://client.example.com/callback"],
>   "jwks_cache_miss_cache_time": 60000,
>   "jwks_cache_timeout": 3600000,
>   "client_name#ja-jpan-jp": "クライアント名",
>   "id_token_encrypted_response_alg": "RSA-OAEP-256",
>   "id_token_encrypted_response_enc": "A128CBC-HS256",
>   "client_secret_expires_at": 0,
>   "access_token_lifetime": 0,
>   "refresh_token_lifetime": 0,
>   "scopes": ["address", "phone", "openid", "profile", "email"],
>   "request_object_signing_alg": "",
>   "response_types": ["code"]
> }
> ```

OIDC clients must include these claims in the JSON registration data:

* The `openid` scope; for example, `"scopes": ["profile", "openid"]`.

* The `id_token` response type; for example, `"response_types": ["code", "id_token code"]`.

### Registration with mutual TLS authentication

The following example shows the use of mutual TLS (mTLS) for authentication. The configuration depends on the type of certificate:

* CA-signed X.509 certificates (PKI)

  If applications use CA-signed certificates, configure AM to trust the certificate authorities.

  Learn more in [Mutual TLS using public key infrastructure](../am-oauth2/client-auth-mtls.html#pki-mtls).

  On registration, the client includes the following properties in its profile data:

  * `"token_endpoint_auth_method": "tls_client_auth"`.

  * `"tls_client_auth_subject_dn": "<certificate-subject-DN>"`; for example, `"tls_client_auth_subject_dn": "CN=myOAuth2Client"`.

* Self-signed X.509 certificates

  If applications use self-signed certificates, they can provide their certificates as:

  * A JSON Web Key Set (JWKS).

    On registration, the client includes the following properties in its profile data:

    * `"token_endpoint_auth_method": "self_signed_tls_client_auth"`.

    * The JWKS containing the certificate and prepared according to [RFC 7517](https://www.rfc-editor.org/info/rfc7517).

  * A JWKS URI, which AM reads to retrieve the certificate.

    On registration, the client includes the following properties in its profile data:

    * `"token_endpoint_auth_method": "self_signed_tls_client_auth"`.

    * `"jwks_uri": "<uri>"`; for example, `"jwks_uri": "https://www.example.com/mysecureapps/certs"`.

  * A single X.509 certificate in PEM format.

    On registration, the client includes the following properties in its profile data:

    * `"token_endpoint_auth_method": "self_signed_tls_client_auth"`.

    * `"tls_client_auth_x509_cert": "<pem-format-cert>"`.

      The `<pem-format-cert>` can omit the `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` labels.

The following example shows dynamic registration with a self-signed ECDSA P-256 certificate in a JWKS:

> **Collapse: Show the example**
>
> ```bash
> $ curl \
>  --request POST \
>  --header "Content-Type: application/json" \
>  --data '{
>     "jwks": {
>         "keys": [{
>             "kty": "EC",
>             "crv": "P-256",
>             "x": "9BmRru-6AYQ8U_9tUFhMGVG-BvC4vRthzLJTntfSdBA",
>             "y": "MqPzVSeVNzzgcR-zZeLGog3GJ4d-doRE9eiGkCKrB48",
>             "kid": "a4:68:90:1c:f6:c1:43:c0",
>             "x5c": [
>                 "MIIBZTCCAQugAwIB…​..xgASSpAQC83FVBawjmbv6k4CN95G8zHsA=="
>             ]
>         }]
>     },
>     "client_type": "Confidential",
>     "grant_types": ["authorization_code", "client_credentials"],
>     "response_types": ["code", "token"],
>     "redirect_uris": ["https://client.example.com:8443/callback"],
>     "token_endpoint_auth_method": "self_signed_tls_client_auth",
>     "tls_client_auth_subject_dn": "CN=myOauth2Client",
>     "tls_client_certificate_bound_access_tokens": true
> }' \
>  "https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/register"
> {
>   "request_object_encryption_alg": "",
>   "default_max_age": 1,
>   "jwks": {
>     "keys": [
>       {
>         "kty": "EC",
>         "crv": "P-256",
>         "x": "9BmRru-6AYQ8U_9tUFhMGVG-BvC4vRthzLJTntfSdBA",
>         "y": "MqPzVSeVNzzgcR-zZeLGog3GJ4d-doRE9eiGkCKrB48",
>         "kid": "a4:68:90:1c:f6:c1:43:c0",
>         "x5c": [
>           "MIIBZTCCAQugAwIB…​..xgASSpAQC83FVBawjmbv6k4CN95G8zHsA=="
>         ]
>       }
>     ]
>   },
>   "application_type": "web",
>   "tls_client_auth_subject_dn": "CN=myOauth2Client",
>   "registration_client_uri": "https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/register?client_id=83635999-2794-4fcd-b6b3-67e2d86c1952",
>   "client_type": "Confidential",
>   "userinfo_encrypted_response_alg": "",
>   "registration_access_token": "tu4KR0jO3iGn0ubOOY0YCSfyPmk",
>   "client_id": "83635999-2794-4fcd-b6b3-67e2d86c1952",
>   "token_endpoint_auth_method": "self_signed_tls_client_auth",
>   "userinfo_signed_response_alg": "",
>   "public_key_selector": "jwks",
> …​
> }
> ```

The example sets `"tls_client_certificate_bound_access_tokens": true`. This lets the client obtain certificate-bound access tokens. Find more information in [Certificate-bound proof-of-possession](../am-oauth2/oauth2-PoP-Cert.html).

### Registration with an access token

The following example assumes you have completed the task to [Register a client profile for access tokens](#dynamic-registration-registration-client).

1. Use the registration service client to get an access token:

   ```bash
   $ curl \
   --request POST \
   --user 'registration-service:mySecret' \
   --data 'grant_type=client_credentials' \
   --data 'scope=dynamic_client_registration' \
   'https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/access_token'
   {
     "access_token": "<access-token>",
     "scope": "dynamic_client_registration",
     "token_type": "Bearer",
     "expires_in": 3596
   }
   ```

2. Register a client dynamically with the access token as authorization.

   Include a `client_name` in the payload as the human-readable name to display to resource owners.

   ```bash
   $ curl \
   --request POST \
   --header 'Content-Type: application/json' \
   --header 'Authorization: Bearer <access-token>' \
   --data '{
     "redirect_uris": ["https://client.example.com/callback"],
     "client_name#en": "My Client",
     "client_name#ja-Jpan-JP": "\u30AF\u30E9\u30A4\u30A2\u30F3\u30C8\u540D",
     "client_uri": "https://client.example.com/"
   }' \
   'https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/register'
   ```

   > **Collapse: Show the response**
   >
   > ```json
   > {
   >      "request_object_encryption_alg": "",
   >      "default_max_age": 1,
   >      "application_type": "web",
   >      "client_name#en": "My Client",
   >      "registration_client_uri": "https://am.example.com:8443/am/oauth2/register?client_id=<generated-client-id>",
   >      "client_type": "Confidential",
   >      "userinfo_encrypted_response_alg": "",
   >      "registration_access_token": "<generated-registration-access-token>",
   >      "client_id": "<generated-client-id>",
   >      "token_endpoint_auth_method": "client_secret_basic",
   >      "userinfo_signed_response_alg": "",
   >      "public_key_selector": "x509",
   >      "authorization_code_lifetime": 0,
   >      "client_secret": "<generated-client-secret>",
   >      "user_info_response_format_selector": "JSON",
   >      "id_token_signed_response_alg": "HS256",
   >      "default_max_age_enabled": false,
   >      "subject_type": "public",
   >      "jwt_token_lifetime": 0,
   >      "id_token_encryption_enabled": false,
   >      "redirect_uris": ["https://client.example.com/callback"],
   >      "client_name#ja-jpan-jp": "クライアント名",
   >      "id_token_encrypted_response_alg": "RSA1_5",
   >      "id_token_encrypted_response_enc": "A128CBC_HS256",
   >      "client_secret_expires_at": 0,
   >      "access_token_lifetime": 0,
   >      "refresh_token_lifetime": 0,
   >      "request_object_signing_alg": "",
   >      "response_types": ["code"]
   >  }
   > ```

   OIDC clients must include these claims in the JSON registration data:

   * The `openid` scope; for example, `"scopes": ["profile", "openid"]`.

   * The `id_token` response type; for example, `"response_types": ["code", "id_token code"]`.

### Registration with a software statement

This example assumes you have completed the following tasks:

* [Update OAuth 2.0 provider settings](#dynamic-registration-oauth2-provider)

* [Register a software publisher profile](#dynamic-registration-software-publisher)

* Acquired an encrypted software statement JWT

To register with a software statement:

1. Configure the OAuth 2.0 provider:

   This example uses open registration with a software statement. The OAuth 2.0 provider has these settings enabled:

   * Allow Open Dynamic Client Registration

   * Require Software Statement for Dynamic Client Registration

   If you leave Allow Open Dynamic Client Registration disabled, use an access token as authorization for the registration request, as demonstrated in [Registration with an access token](#register-oauth2-client-dynamic-access-token-example).

2. Configure the software publisher account.

   The software publisher for this example has the following profile settings:

   * Agent ID

     `My Software Publisher`

   * Software publisher secret

     `secret`

   * Software publisher issuer

     `https://publisher.example.com`

   * Software statement signing Algorithm

     `HS256`

   * Public key selector

     `JWKs`

   * Json Web Key

     `{"keys":[{"kty":"oct","k":"secret","alg":"HS256"}]}`

     Notice that the value is a key set rather than a single key.

3. Prepare the software statement.

   The plaintext payload of the software statement JWT in this example is the following:

   ```json
   {
     "sub": "registrar@example.com",
     "name": "My Client",
     "iat": 1675246194,
     "exp": 1675249794,
     "iss": "https://publisher.example.com",
     "redirect_uris": ["https://client.example.com/callback"]
   }
   ```

   When you try the example, use current values for the `iat` (issued at) and `exp` (expiration time) claims.

   The JWT header is `{"alg":"HS256","typ":"JWT"}`, and the secret is `secret`.

   The resulting encrypted JWT is as follows with lines folded for readability:

   ```none
   eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
   .eyJzdWIiOiJyZWdpc3RyYXJAZXhhbXBsZS5jb20iLCJuYW1lIjoiSm9obiBE
   b2UiLCJpYXQiOjE2NzUyNDYxOTQsImV4cCI6MTY3NTI0OTc5NCwiaXNzIjoia
   HR0cHM6Ly9wdWJsaXNoZXIuZXhhbXBsZS5jb20iLCJyZWRpcmVjdF91cmlzIj
   pbImh0dHBzOi8vY2xpZW50LmV4YW1wbGUuY29tL2NhbGxiYWNrIl19
   .7_3nu39GtTTz_RPKZMjj1JuwWWTgeE4Iqx7p3-cfiPg
   ```

4. Register a client dynamically with the software statement JWT:

   ```bash
   $ curl \
   --request POST \
   --header 'Content-Type: application/json' \
   --data '{
     "redirect_uris": ["https://client.example.com/callback"],
     "client_name#en": "My Client",
     "client_name#ja-Jpan-JP": "\u30AF\u30E9\u30A4\u30A2\u30F3\u30C8\u540D",
     "client_uri": "https://client.example.com/",
     "software_statement": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJyZWdpc3RyYXJAZXhhbXBsZS5jb20iLCJuYW1lIjoiSm9obiBEb2UiLCJpYXQiOjE2NzUyNDYxOTQsImV4cCI6MTY3NTI0OTc5NCwiaXNzIjoiaHR0cHM6Ly9wdWJsaXNoZXIuZXhhbXBsZS5jb20iLCJyZWRpcmVjdF91cmlzIjpbImh0dHBzOi8vY2xpZW50LmV4YW1wbGUuY29tL2NhbGxiYWNrIl19.7_3nu39GtTTz_RPKZMjj1JuwWWTgeE4Iqx7p3-cfiPg"
   }' \
   'https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/register'
   ```

   > **Collapse: Show the response**
   >
   > ```json
   > {
   >   "authorization_signed_response_alg": "RS256",
   >   "request_object_encryption_alg": "",
   >   "introspection_encrypted_response_alg": "RSA-OAEP-256",
   >   "client_uri": "https://client.example.com/",
   >   "default_max_age": 1,
   >   "application_type": "web",
   >   "introspection_encrypted_response_enc": "A128CBC-HS256",
   >   "introspection_signed_response_alg": "RS256",
   >   "client_name#en": "My Client",
   >   "userinfo_encrypted_response_enc": "",
   >   "registration_client_uri": "https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/register?client_id=<generated-client-id>",
   >   "client_type": "Confidential",
   >   "userinfo_encrypted_response_alg": "",
   >   "registration_access_token": "<generated-registration-access-token>",
   >   "client_id": "<generated-client-id>",
   >   "token_endpoint_auth_method": "client_secret_basic",
   >   "userinfo_signed_response_alg": "",
   >   "software_statement": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJyZWdpc3RyYXJAZXhhbXBsZS5jb20iLCJuYW1lIjoiSm9obiBEb2UiLCJpYXQiOjE2NzUyNDYxOTQsImV4cCI6MTY3NTI0OTc5NCwiaXNzIjoiaHR0cHM6Ly9wdWJsaXNoZXIuZXhhbXBsZS5jb20iLCJyZWRpcmVjdF91cmlzIjpbImh0dHBzOi8vY2xpZW50LmV4YW1wbGUuY29tL2NhbGxiYWNrIl19.7_3nu39GtTTz_RPKZMjj1JuwWWTgeE4Iqx7p3-cfiPg",
   >   "public_key_selector": "x509",
   >   "scope": "address phone openid profile email",
   >   "require_pushed_authorization_requests": false,
   >   "authorization_code_lifetime": 0,
   >   "client_secret": "<generated-client-secret>",
   >   "user_info_response_format_selector": "JSON",
   >   "tls_client_certificate_bound_access_tokens": false,
   >   "backchannel_logout_session_required": false,
   >   "id_token_signed_response_alg": "RS256",
   >   "default_max_age_enabled": false,
   >   "token_intro_response_format_selector": "JSON",
   >   "subject_type": "public",
   >   "grant_types": ["authorization_code"],
   >   "jwt_token_lifetime": 0,
   >   "id_token_encryption_enabled": false,
   >   "redirect_uris": ["https://client.example.com/callback"],
   >   "jwks_cache_miss_cache_time": 60000,
   >   "jwks_cache_timeout": 3600000,
   >   "client_name#ja-jpan-jp": "クライアント名",
   >   "id_token_encrypted_response_alg": "RSA-OAEP-256",
   >   "id_token_encrypted_response_enc": "A128CBC-HS256",
   >   "client_secret_expires_at": 0,
   >   "access_token_lifetime": 0,
   >   "refresh_token_lifetime": 0,
   >   "scopes": ["address", "phone", "openid", "profile", "email"],
   >   "request_object_signing_alg": "",
   >   "response_types": ["code"]
   > }
   > ```

   OIDC clients must include these claims in the JSON registration data:

   * The `openid` scope; for example, `"scopes": ["profile", "openid"]`.

   * The `id_token` response type; for example, `"response_types": ["code", "id_token code"]`.

## Manage client profiles

The JSON response to a successful dynamic registration request contains the following fields:

* `registration_client_uri`

  The endpoint for reading and updating the client profile, including the generated client ID as a query parameter.

* `registration_access_token`

  The generated access token to authorize reading and updating the client profile.

Make sure your client application stores the dynamic registration response, including these values. Your application needs them to read and update its client profile.

|   |                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To manage large numbers of clients without impacting system performance, use [Scalable OAuth 2.0 clients](../am-oauth2/oauth2-scalable-clients.html). |

### Read a client profile

To read a client profile, send an HTTP GET request to the `registration_client_uri` with the `registration_access_token` for authorization:

```bash
$ curl \
--request GET \
--header 'Authorization: Bearer <generated-registration-access-token>' \
"https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/register?client_id=<generated-client-id>"
```

> **Collapse: Show the response**
>
> ```json
> {
>   "authorization_signed_response_alg": "RS256",
>   "request_object_encryption_alg": "",
>   "introspection_encrypted_response_alg": "RSA-OAEP-256",
>   "client_uri": "https://client.example.com/",
>   "default_max_age": 1,
>   "application_type": "web",
>   "introspection_encrypted_response_enc": "A128CBC-HS256",
>   "introspection_signed_response_alg": "RS256",
>   "client_name#en": "My Client",
>   "userinfo_encrypted_response_enc": "",
>   "client_type": "Confidential",
>   "userinfo_encrypted_response_alg": "",
>   "token_endpoint_auth_method": "client_secret_basic",
>   "userinfo_signed_response_alg": "",
>   "client_id": "<generated-client-id>",
>   "public_key_selector": "x509",
>   "scope": "openid address phone email profile",
>   "require_pushed_authorization_requests": false,
>   "authorization_code_lifetime": 0,
>   "client_secret": "<generated-client-secret>",
>   "user_info_response_format_selector": "JSON",
>   "tls_client_certificate_bound_access_tokens": false,
>   "backchannel_logout_session_required": false,
>   "id_token_signed_response_alg": "RS256",
>   "default_max_age_enabled": false,
>   "token_intro_response_format_selector": "JSON",
>   "subject_type": "public",
>   "grant_types": ["authorization_code"],
>   "jwt_token_lifetime": 0,
>   "id_token_encryption_enabled": false,
>   "redirect_uris": ["https://client.example.com/callback"],
>   "jwks_cache_miss_cache_time": 60000,
>   "jwks_cache_timeout": 3600000,
>   "client_name#ja-jpan-jp": "クライアント名",
>   "id_token_encrypted_response_alg": "RSA-OAEP-256",
>   "id_token_encrypted_response_enc": "A128CBC-HS256",
>   "client_secret_expires_at": 0,
>   "access_token_lifetime": 0,
>   "refresh_token_lifetime": 0,
>   "scopes": ["openid", "address", "phone", "email", "profile"],
>   "request_object_signing_alg": "",
>   "response_types": ["code"]
> }
> ```

The response does not contain the `registration_client_uri` or the `registration_access_token`.

### Update a client profile

When an application updates its client profile rather than registering again dynamically, it retains the current client ID and client secret.

The update request body replaces the current client profile settings subject to these conditions:

* Updates cannot change any of the following settings:

  * `client_id_issued_at`

  * `client_secret`

  * `client_secret_expires_at`

  * `registration_access_token`

  * `registration_client_uri`

* Missing settings are set to their default values.

* Settings with unrecognized names are silently ignored.

* If the client profile includes a software statement JWT, it must be valid and current.

* A successful update returns a new registration access token to use going forward.

To update a client profile, send an HTTP PUT request to the `registration_client_uri` with the `registration_access_token` for authorization and the request body specifying the new settings.

The following example updates the `scope` and `grant_types` settings:

```bash
$ curl \
--request PUT \
--header 'Authorization: Bearer <generated-registration-access-token>' \
--data '{
  "client_name#en": "My Client",
  "client_name#ja-jpan-jp": "クライアント名",
  "client_id": "<generated-client-id>",
  "client_secret": "<generated-client-secret>",
  "client_uri": "https://client.example.com/",
  "scope": "openid profile",
  "grant_types": ["authorization_code", "implicit"],
  "redirect_uris": ["https://client.example.com/callback"]
}' \
'https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/register?client_id=<generated-client-id>'
```

> **Collapse: Show the response**
>
> ```json
> {
>   "authorization_signed_response_alg": "RS256",
>   "request_object_encryption_alg": "",
>   "introspection_encrypted_response_alg": "RSA-OAEP-256",
>   "client_uri": "https://client.example.com/",
>   "default_max_age": 1,
>   "application_type": "web",
>   "introspection_encrypted_response_enc": "A128CBC-HS256",
>   "introspection_signed_response_alg": "RS256",
>   "client_name#en": "My Client",
>   "userinfo_encrypted_response_enc": "",
>   "client_type": "Confidential",
>   "userinfo_encrypted_response_alg": "",
>   "registration_access_token": "<generated-registration-access-token>",
>   "client_id": "<generated-client-id>",
>   "token_endpoint_auth_method": "client_secret_basic",
>   "userinfo_signed_response_alg": "",
>   "public_key_selector": "x509",
>   "scope": "openid profile",
>   "require_pushed_authorization_requests": false,
>   "authorization_code_lifetime": 0,
>   "client_secret": "<generated-client-secret>",
>   "user_info_response_format_selector": "JSON",
>   "tls_client_certificate_bound_access_tokens": false,
>   "backchannel_logout_session_required": false,
>   "id_token_signed_response_alg": "RS256",
>   "default_max_age_enabled": false,
>   "token_intro_response_format_selector": "JSON",
>   "subject_type": "public",
>   "grant_types": ["authorization_code", "implicit"],
>   "jwt_token_lifetime": 0,
>   "id_token_encryption_enabled": false,
>   "redirect_uris": ["https://client.example.com/callback"],
>   "jwks_cache_miss_cache_time": 60000,
>   "jwks_cache_timeout": 3600000,
>   "client_name#ja-jpan-jp": "クライアント名",
>   "id_token_encrypted_response_alg": "RSA-OAEP-256",
>   "id_token_encrypted_response_enc": "A128CBC-HS256",
>   "access_token_lifetime": 0,
>   "refresh_token_lifetime": 0,
>   "scopes": ["openid", "profile"],
>   "request_object_signing_alg": "",
>   "response_types": ["code"]
> }
> ```

The `registration_access_token` in the response reflects the new value to use going forward.

### Delete a client profile

To remove a client profile, send an HTTP DELETE request to the `registration_client_uri` with the `registration_access_token` for authorization:

```bash
$ curl \
--request DELETE \
--header 'Authorization: Bearer <generated-registration-access-token>' \
'https://am.example.com:8443/am/oauth2/realms/root/realms/alpha/register?client_id=<generated-client-id>'
```

A successful request returns an HTTP 204 No Content response.

Authorization grants and active tokens associated with the client remain valid until they expire.

---

---
title: Encrypt ID tokens and backchannel logout tokens
description: Configure PingAM to encrypt OpenID Connect ID tokens and backchannel logout tokens using algorithms such as RSA, ECDH-ES, AES Key Wrapping, or direct encryption
component: pingam
version: 8.1
page_id: pingam:am-oidc1:encrypting-oidc-idtokens
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oidc1/encrypting-oidc-idtokens.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OpenID Connect (OIDC)", "Standards", "Security"]
page_aliases: ["oidc1-guide:encrypting-oidc-idtokens.adoc"]
---

# Encrypt ID tokens and backchannel logout tokens

AM supports encrypting ID tokens and backchannel logout tokens to protect them against *tampering attacks*, outlined in the JSON Web Encryption specification ([RFC 7516](https://www.rfc-editor.org/info/rfc7516)).

ID tokens and backchannel logout tokens share the same encryption configuration. You either encrypt both or none.

1. Go to Realms > *realm name* > Applications > OAuth 2.0 > Clients > *client ID*.

2. On the Signing and Encryption tab, select Enable ID Token Encryption.

3. In the Id Token Encryption Algorithm field, enter the algorithm AM will use to encrypt ID tokens and backchannel logout tokens:

   > **Collapse: Supported encryption algorithms**
   >
   > * `A128KW` - AES Key Wrapping with 128-bit key derived from the client secret.
   >
   > * `A192KW` - AES Key Wrapping with 192-bit key derived from the client secret.
   >
   > * `A256KW` - AES Key Wrapping with 256-bit key derived from the client secret.
   >
   > * `RSA-OAEP` - RSA with Optimal Asymmetric Encryption Padding (OAEP) with SHA-1 and MGF-1.
   >
   > * `RSA-OAEP-256` - RSA with OAEP with SHA-256 and MGF-1.
   >
   > * `RSA1_5` - RSA with PKCS#1 v1.5 padding (not recommended).
   >
   > * `dir` - Direct encryption with AES using the hashed client secret.
   >
   > * `ECDH-ES` - Elliptic Curve Diffie-Hellman
   >
   > * `ECDH-ES+A128KW` - Elliptic Curve Diffie-Hellman + AES Key Wrapping with 128-bit key.
   >
   > * `ECDH-ES+A192KW` - Elliptic Curve Diffie-Hellman + AES Key Wrapping with 192-bit key.
   >
   > * `ECDH-ES+A256KW` - Elliptic Curve Diffie-Hellman + AES Key Wrapping with 256-bit key.
   >
   > * `X25519` - Elliptic Curve Diffie-Hellman with Curve25519.
   >
   > * `X448` - Elliptic Curve Diffie-Hellman with Curve448.
   >
   > Only the `P-256`, `P-384`, and `P-521` curves are supported.

4. In the ID Token Encryption Method field, enter the method AM will use to encrypt ID tokens and backchannel logout tokens:

   > **Collapse: Supported encryption methods**
   >
   > * `A128CBC-HS256` - AES 128-bit in CBC mode using HMAC-SHA-256-128 hash (HS256 truncated to 128 bits)
   >
   > * `A192CBC-HS384` - AES 192-bit in CBC mode using HMAC-SHA-384-192 hash (HS384 truncated to 192 bits)
   >
   > * `A256CBC-HS512` - AES 256-bit in CBC mode using HMAC-SHA-512-256 hash (HS512 truncated to 256 bits)
   >
   > * `A128GCM` - AES 128-bit in GCM mode
   >
   > * `A192GCM` - AES 192-bit in GCM mode
   >
   > * `A256GCM` - AES 256-bit in GCM mode

5. If you select an RSA encryption algorithm, perform one of the following actions:

   * Enter the RSA public key in X.509 PEM format in the ID Token Encryption Public Key field.

   * Enter a JWK set in the Json Web Key field.

   * Enter a URI containing the public key in the Json Web Key URI field.

6. If you select an ECDH-ES encryption algorithm, perform one of the following actions:

   * Enter a JWK set in the Json Web Key field.

   * Enter a URI containing the public key in the Json Web Key URI field.

7. If you select an algorithm other than RSA or ECDH-ES, select the Core tab and do either of the following:

   * Store the private key/secret in the Client secret field.

   * Set a Secret Label Identifier and store the secret in a secret store.

     AM uses the Secret Label Identifier to create a specific secret label for each OAuth 2.0 client. The secret label takes the form `am.applications.oauth2.client.identifier.secret` where identifier is the value of Secret Label Identifier.

     The identifier can only contain alphanumeric characters `a-z`, `A-Z`, `0-9`, and periods (`.`). It can't start or end with a period.

     If you set a Secret Label Identifier and AM finds a matching secret in a secret store, the Client secret is ignored.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * Several features of OAuth 2.0 use the string stored in the Client secret field to sign/encrypt tokens or parameters when you configure specific algorithms. For example, signing ID tokens with HMAC algorithms, encrypting ID tokens with AES or direct algorithms, or encrypting OpenID Connect parameters with AES or direct algorithms.

  These features must share the key/secret stored in the Client secret field, and you must ensure that they're configured with the same algorithm.

* If you set a Secret Label Identifier instead of a Client secret field, you can have *multiple* OAuth 2.0 client secrets in the secret store. This lets you rotate and retire secrets as necessary.

  AM uses the *active* secret in the secret store to encrypt or sign an ID Token. However, the relying party (RP) can initiate an OAuth 2.0 request with *any one* of the valid secrets in the secret store. Therefore, the *active* secret might not be the same secret that the RP used to initiate the request.

  For example, an OAuth 2.0 request might come in with a valid, non-active secret. AM encrypts the ID Token with the *active* secret. Regardless of the secret that the RP used to initiate the flow, the RP can only decrypt the token using the active secret (the secret with which AM encrypted the token). |

---

---
title: GSMA Mobile Connect
description: Implement GSMA Mobile Connect as an OIDC application to enable mobile network operators to serve as identity providers with configurable levels of assurance
component: pingam
version: 8.1
page_id: pingam:am-oidc1:oidc-mobile-connect
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-oidc1/oidc-mobile-connect.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OpenID Connect (OIDC)", "Standards", "Integration"]
page_aliases: ["oidc1-guide:oidc-mobile-connect.adoc"]
section_ids:
  mobile_connect_roles: Mobile Connect roles
  loa_support: LoA support
  mobile-connect-configure: Configure Mobile Connect
  mobile-connect-table-auth-request-params: Authorization parameters
---

# GSMA Mobile Connect

[GSMA Mobile Connect](https://www.gsma.com/solutions-and-impact/technologies/mobile-identity/mobile-connect/) is an application of OpenID Connect (OIDC). It enables mobile phones to serve as authentication devices independently of the service and the device.

Mobile Connect offers a standard way for Mobile Network Operators (MNOs) to act as general-purpose identity providers. It offers a range of Levels of Assurance (LoAs) and profile data to Mobile Connect-compliant service providers.

## Mobile Connect roles

In a Mobile Connect deployment, AM can play the following roles:

* The OpenID provider

  The provider implements the Mobile Connect Profile as part of the Service Provider (Identity Gateway interface).

  The OpenID provider responds to a successful authorization request with all the required fields and the optional `expires_in` field. AM supports the mandatory ID Token properties. The relying party must use the `expires_in` value instead of specifying `max_age` as a request parameter.

  AM returns the standard `userinfo` claims and the `updated_at` property. The `updated_at` property holds the time last updated as seconds since January 1, 1970 UTC.

* The authenticator

  The authenticator implements the Mobile Connect Profile as part of the Identity Gateway (Authenticators interface).

  The authenticator makes users authenticate at the appropriate LoA. A service provider can request LoAs without regard to the implementation. The Identity Gateway includes a claim in the ID Token to indicate the LoA achieved.

## LoA support

AM maps LoAs to an authentication mechanism:

* A service provider acting as a relying party requests an LoA with the `acr_values` parameter.

* AM returns the corresponding `acr` claim in the ID token.

LoA support:

* `1` (low—​little or no confidence)

* `2` (medium—​some confidence, as in single-factor authentication)

* `3` (high—​high confidence, as in multi-factor authentication)

LoA support does not include support for `4`, which involves digital signatures. The `dtbs` authorization parameter is not supported.

## Configure Mobile Connect

1. Configure the OAuth 2.0 provider OIDC authentication context settings to return `acr` and `amr` claims in the ID tokens.

   For details, refer to [Authentication requirements](oidc-authentication-requirements.html).

2. Update the identity store user configuration.

   The `userinfo` endpoint returns `updated_at` values in the ID token. If the user profile has never been updated `updated_at` reflects creation time.

   When using DS as an identity store, AM takes `updated_at` from the `modifyTimestamp` attribute if it exists, and the `createTimestamp` attribute if not.

   In the AM admin UI, go to Realms > *realm name* > Identity Stores > *identity store name* > User Configuration and add the relevant attributes to the LDAP User Attributes list.

3. Save your work.

## Authorization parameters

You must use the authorization code grant to request ID tokens.

| Request parameter | Supported? | Description                                                                                                                                                                                         |
| ----------------- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `acr_values`      | Yes        | The OpenID Connect authentication context class reference values.For details, refer to [The `acr` claim](oidc-authentication-requirements.html#acr-claim).                                          |
| `client_id`       | Yes        | A unique string identifier for the application making the request.                                                                                                                                  |
| `display`         | Yes        | A string value specifying the user interface display.                                                                                                                                               |
| `dtbs`            | No         | Data to be signed.LoA 4 is not supported.                                                                                                                                                           |
| `login_hint`      | Yes        | A string specifying the ID used to log in.Set the `login_hint` to the value of the `oidcLoginHint` cookie. This is an HttpOnly cookie (only sent over HTTPS).                                       |
| `nonce`           | Yes        | A string linking the client session with the ID token to mitigate against replay attacks.Required for Mobile Connect.                                                                               |
| `redirect_uri`    | Yes        | The URI to return the end user to after authorization is complete; must match the `redirect_uri` in the client application profile.                                                                 |
| `response_type`   | Yes        | A string specifying the response expected from the authorization server; use `response_type=code`.                                                                                                  |
| `scope`           | Yes        | A string specifying the permissions the client application requests from the end user. Separate scopes with spaces.Required: `openid`Optional: `address` `email` `offline_access` `phone` `profile` |
| `state`           | Yes        | A string value to maintain state between the request and the callback.Required for Mobile Connect.                                                                                                  |