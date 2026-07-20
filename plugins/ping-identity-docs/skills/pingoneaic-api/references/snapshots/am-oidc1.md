---
title: /.well-known/webfinger
description: The /.well-known/webfinger endpoint is described in OpenID Connect Discovery 1.0 incorporating errata set 1.
component: pingoneaic-api
page_id: pingoneaic-api:am-oidc1:rest-api-oidc-discovery-webfinger
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-oidc1/rest-api-oidc-discovery-webfinger.html
keywords: ["OpenID Connect (OIDC)", "Standards", "Endpoints"]
section_ids:
  supported-parameters: Supported parameters
  example: Example
---

# /.well-known/webfinger

The `/.well-known/webfinger` endpoint is described in [OpenID Connect Discovery 1.0 incorporating errata set 1](https://openid.net/specs/openid-connect-discovery-1_0.html).

Use it to discover the OpenID provider for an end user.

*Do not* specify the realm in the request URL; for example:

```none
https://<tenant-env-fqdn>/am/.well-known/webfinger
```

This endpoint is disabled by default. Learn more in [OIDC discovery](https://docs.pingidentity.com/pingoneaic/latest/am-oidc1/oidc-am-provider.html#configure-openid-connect-discovery).

## Supported parameters

The discovery endpoint supports the following parameters:

| Parameter  | Description                                                                                                                                                                                                                                                                                                                                                                  | Required                                              |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| `realm`    | The Advanced Identity Cloud realm to query for the user profile.                                                                                                                                                                                                                                                                                                             | No                                                    |
| `rel`      | The URI identifying the type of service.                                                                                                                                                                                                                                                                                                                                     | Yes; use `http://openid.net/specs/connect/1.0/issuer` |
| `resource` | The URL-encoded subject of the request.; one of:`acct:user-email` `acct:user-email@host` `http(s)://host/username` `http(s)://host:port`The `host` relates to the discovery URL. For example, if the endpoint is `http://server.example.com/am/.well-known/webfinger`, the host is `server.example.com`.The `resource` parameter does not support wildcard characters (`*`). | Yes                                                   |

## Example

```bash
$ curl \
'https://<tenant-env-fqdn>/am/.well-known/webfinger?resource=acct%3Abjensen%40example.com&rel=http%3A%2F%2Fopenid.net%2Fspecs%2Fconnect%2F1.0%2Fissuer'
{
  "subject": "acct:bjensen@example.com",
  "links": [{
    "rel": "http://openid.net/specs/connect/1.0/issuer",
    "href": "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha"
  }]
}
```

---

---
title: /oauth2/.well-known/openid-configuration
description: The OpenID provider configuration endpoint is defined in OpenID Connect Discovery 1.0.
component: pingoneaic-api
page_id: pingoneaic-api:am-oidc1:rest-api-oidc-discovery-configuration
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-oidc1/rest-api-oidc-discovery-configuration.html
keywords: ["OpenID Connect (OIDC)", "Standards", "Endpoints", "Setup &amp; Configuration"]
---

# /oauth2/.well-known/openid-configuration

The OpenID provider configuration endpoint is defined in [OpenID Connect Discovery 1.0](https://openid.net/specs/openid-connect-discovery-1_0.html).

Use this to discover the provider settings. Learn more in [OIDC discovery](https://docs.pingidentity.com/pingoneaic/latest/am-oidc1/oidc-am-provider.html#configure-openid-connect-discovery).

Specify the realm in the request URL; for example:

```bash
$ curl https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/.well-known/openid-configuration
```

> **Collapse: Show output**
>
> ```json
> {
>   "request_parameter_supported": true,
>   "pushed_authorization_request_endpoint": "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/par",
>   "introspection_encryption_alg_values_supported": ["ECDH-ES+A256KW", "ECDH-ES+A192KW", "RSA-OAEP", "ECDH-ES+A128KW", "RSA-OAEP-256", "A128KW", "A256KW", "ECDH-ES", "dir", "A192KW"],
>   "claims_parameter_supported": false,
>   "introspection_endpoint": "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/introspect",
>   "issuer": "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha",
>   "id_token_encryption_enc_values_supported": ["A256GCM", "A192GCM", "A128GCM", "A128CBC-HS256", "A192CBC-HS384", "A256CBC-HS512"],
>   "userinfo_encryption_enc_values_supported": ["A256GCM", "A192GCM", "A128GCM", "A128CBC-HS256", "A192CBC-HS384", "A256CBC-HS512"],
>   "authorization_endpoint": "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/authorize",
>   "authorization_encryption_alg_values_supported": ["ECDH-ES+A256KW", "ECDH-ES+A192KW", "RSA-OAEP", "ECDH-ES+A128KW", "RSA-OAEP-256", "A128KW", "A256KW", "ECDH-ES", "dir", "A192KW"],
>   "introspection_encryption_enc_values_supported": ["A256GCM", "A192GCM", "A128GCM", "A128CBC-HS256", "A192CBC-HS384", "A256CBC-HS512"],
>   "claims_supported": [],
>   "rcs_request_signing_alg_values_supported": ["PS384", "ES384", "RS384", "HS256", "HS512", "ES256", "RS256", "HS384", "ES512", "PS256", "PS512", "RS512"],
>   "token_endpoint_auth_methods_supported": ["client_secret_post", "private_key_jwt", "self_signed_tls_client_auth", "tls_client_auth", "none", "client_secret_basic"],
>   "tls_client_certificate_bound_access_tokens": true,
>   "response_modes_supported": ["fragment", "jwt", "form_post.jwt", "form_post", "fragment.jwt", "query", "query.jwt"],
>   "backchannel_logout_session_supported": true,
>   "token_endpoint": "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/access_token",
>   "response_types_supported": ["code token id_token", "code", "code id_token", "device_code", "id_token", "code token", "token", "token id_token"],
>   "authorization_encryption_enc_values_supported": ["A256GCM", "A192GCM", "A128GCM", "A128CBC-HS256", "A192CBC-HS384", "A256CBC-HS512"],
>   "revocation_endpoint_auth_methods_supported": ["client_secret_post", "private_key_jwt", "self_signed_tls_client_auth", "tls_client_auth", "none", "client_secret_basic"],
>   "request_uri_parameter_supported": true,
>   "grant_types_supported": ["implicit", "urn:ietf:params:oauth:grant-type:saml2-bearer", "refresh_token", "password", "client_credentials", "urn:ietf:params:oauth:grant-type:device_code", "authorization_code", "urn:openid:params:grant-type:ciba", "urn:ietf:params:oauth:grant-type:uma-ticket", "urn:ietf:params:oauth:grant-type:jwt-bearer"],
>   "version": "3.0",
>   "userinfo_endpoint": "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/userinfo",
>   "require_request_uri_registration": true,
>   "code_challenge_methods_supported": ["plain", "S256"],
>   "id_token_encryption_alg_values_supported": ["ECDH-ES+A256KW", "ECDH-ES+A192KW", "RSA-OAEP", "ECDH-ES+A128KW", "RSA-OAEP-256", "A128KW", "A256KW", "ECDH-ES", "dir", "A192KW"],
>   "authorization_signing_alg_values_supported": ["PS384", "RS384", "EdDSA", "ES384", "HS256", "HS512", "ES256", "RS256", "HS384", "ES512", "PS256", "PS512", "RS512"],
>   "request_object_signing_alg_values_supported": ["PS384", "ES384", "RS384", "HS256", "HS512", "ES256", "RS256", "HS384", "ES512", "PS256", "PS512", "RS512"],
>   "request_object_encryption_alg_values_supported": ["ECDH-ES+A256KW", "ECDH-ES+A192KW", "ECDH-ES+A128KW", "RSA-OAEP", "RSA-OAEP-256", "A128KW", "A256KW", "ECDH-ES", "dir", "A192KW"],
>   "rcs_response_signing_alg_values_supported": ["PS384", "ES384", "RS384", "HS256", "HS512", "ES256", "RS256", "HS384", "ES512", "PS256", "PS512", "RS512"],
>   "introspection_signing_alg_values_supported": ["PS384", "RS384", "EdDSA", "ES384", "HS256", "HS512", "ES256", "RS256", "HS384", "ES512", "PS256", "PS512", "RS512"],
>   "check_session_iframe": "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/connect/checkSession",
>   "scopes_supported": ["address", "phone", "openid", "profile", "fr:idm:*", "am-introspect-all-tokens", "email"],
>   "backchannel_logout_supported": true,
>   "acr_values_supported": [],
>   "request_object_encryption_enc_values_supported": ["A256GCM", "A192GCM", "A128GCM", "A128CBC-HS256", "A192CBC-HS384", "A256CBC-HS512"],
>   "rcs_request_encryption_alg_values_supported": ["ECDH-ES+A256KW", "ECDH-ES+A192KW", "RSA-OAEP", "ECDH-ES+A128KW", "RSA-OAEP-256", "A128KW", "A256KW", "ECDH-ES", "dir", "A192KW"],
>   "userinfo_signing_alg_values_supported": ["ES384", "HS256", "HS512", "ES256", "RS256", "HS384", "ES512"],
>   "require_pushed_authorization_requests": false,
>   "rcs_response_encryption_enc_values_supported": ["A256GCM", "A192GCM", "A128GCM", "A128CBC-HS256", "A192CBC-HS384", "A256CBC-HS512"],
>   "userinfo_encryption_alg_values_supported": ["ECDH-ES+A256KW", "ECDH-ES+A192KW", "RSA-OAEP", "ECDH-ES+A128KW", "RSA-OAEP-256", "A128KW", "A256KW", "ECDH-ES", "dir", "A192KW"],
>   "end_session_endpoint": "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/connect/endSession",
>   "rcs_request_encryption_enc_values_supported": ["A256GCM", "A192GCM", "A128GCM", "A128CBC-HS256", "A192CBC-HS384", "A256CBC-HS512"],
>   "revocation_endpoint": "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/token/revoke",
>   "rcs_response_encryption_alg_values_supported": ["ECDH-ES+A256KW", "ECDH-ES+A192KW", "ECDH-ES+A128KW", "RSA-OAEP", "RSA-OAEP-256", "A128KW", "A256KW", "ECDH-ES", "dir", "A192KW"],
>   "token_endpoint_auth_signing_alg_values_supported": ["PS384", "ES384", "RS384", "HS256", "HS512", "ES256", "RS256", "HS384", "ES512", "PS256", "PS512", "RS512"],
>   "jwks_uri": "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/connect/jwk_uri",
>   "subject_types_supported": ["public", "pairwise"],
>   "id_token_signing_alg_values_supported": ["PS384", "ES384", "RS384", "HS256", "HS512", "ES256", "RS256", "HS384", "ES512", "PS256", "PS512", "RS512"],
>   "registration_endpoint": "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/register"
> }
> ```

---

---
title: /oauth2/connect/checkSession
description: Use this endpoint to retrieve session state. Learn more in Session management.
component: pingoneaic-api
page_id: pingoneaic-api:am-oidc1:rest-api-oidc-checksession-endpoint
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-oidc1/rest-api-oidc-checksession-endpoint.html
keywords: ["OpenID Connect (OIDC)", "Standards", "Endpoints", "Sessions"]
---

# /oauth2/connect/checkSession

Use this endpoint to retrieve session state. Learn more in [Session management](https://docs.pingidentity.com/pingoneaic/latest/am-oidc1/session-management.html).

A relying party client creates an invisible iframe with the URL to the endpoint as the `src` attribute of the `iframe` tag. Use the endpoint to accept HTML5 `postMessage` requests from the `iframe`, and to generate `postMessage` requests to the `iframe` with the end user's login status.

*Don't* specify the realm in the request URL; for example:

```none
https://<tenant-env-fqdn>/am/oauth2/connect/checkSession
```

---

---
title: /oauth2/connect/endSession
description: Use this endpoint to terminate authenticated sessions. Learn more in Session management.
component: pingoneaic-api
page_id: pingoneaic-api:am-oidc1:rest-api-oidc-endsession-endpoint
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-oidc1/rest-api-oidc-endsession-endpoint.html
keywords: ["OpenID Connect (OIDC)", "Standards", "Endpoints", "Sessions"]
section_ids:
  supported-parameters: Supported parameters
  example: Example
---

# /oauth2/connect/endSession

Use this endpoint to terminate authenticated sessions. Learn more in [Session management](https://docs.pingidentity.com/pingoneaic/latest/am-oidc1/session-management.html).

To find the URL for this endpoint, read the `end_session_endpoint` field of the [well-known configuration endpoint](rest-api-oidc-discovery-configuration.html) for the realm:

```bash
$ curl https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/.well-known/openid-configuration
{
  "...": "...",
  "end_session_endpoint": "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/connect/endSession",
  "...": "..."
}
```

## Supported parameters

The end session endpoint supports the following query parameters:

| Parameter                  | Description                                                                                                                                                                                                                                                                       | Required                            |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| `client_id`                | Uniquely identifies the application making the request.This parameter is *not* compliant with the specification.                                                                                                                                                                  | Yes, when the ID token is encrypted |
| `id_token_hint`            | Previously issued ID token identifying the authenticated session.                                                                                                                                                                                                                 | Yes                                 |
| `post_logout_redirect_uri` | Redirect to this URI after logout.This must match one of the values in the Sign-out URLs setting of the client profile.By default, this profile setting is empty. To update the setting in the Advanced Identity Cloud admin console, go to Applications > *Client ID* > Sign On. | No                                  |

The `post_logout_redirect_uri` parameter determines the result on successful logout:

* If included, Advanced Identity Cloud redirects to the specified location.

  Find more information in [Redirect users to a specific URL after they sign out](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/plugins-user-info-claims.html#example-redirect-users-after-logout).

* If omitted, Advanced Identity Cloud returns HTTP 204 No Content to indicate the end user logged out.

## Example

Advanced Identity Cloud deletes the authenticated session when the user successfully logs out and is redirected to the post logout URL:

```bash
$ curl \
--dump-header - \
--request GET \
'https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/connect/endSession?id_token_hint=id-token&post_logout_redirect_uri=https://www.example.com/signout'
HTTP/2 302
...
location: https://www.example.com/signout
content-length: 0
...
```

---

---
title: /oauth2/connect/jwk_uri
description: This endpoint is defined in OpenID Connect Discovery 1.0.
component: pingoneaic-api
page_id: pingoneaic-api:am-oidc1:managing-jwk_uri
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-oidc1/managing-jwk_uri.html
keywords: ["OpenID Connect (OIDC)", "Standards", "Setup &amp; Configuration", "Security", "Endpoints"]
section_ids:
  obtaining-public-signing-key: Get the public keys
  kid-multiple-keys: Display all algorithms and key types
  map-custom-kids: Map custom key IDs to secrets
---

# /oauth2/connect/jwk\_uri

This endpoint is defined in [OpenID Connect Discovery 1.0](https://openid.net/specs/openid-connect-discovery-1_0.html).

Use it to get the OpenID provider's public keys as a JSON Web Key (JWK) document. Public keys are for asymmetric encryption. *Symmetric* key algorithms, such as direct encryption and AES key wrapping encryption, use the client secret, and HMAC-based algorithms use the secret mapped to the `am.services.oauth2.stateless.signing.HMAC` label. Clients don't need to check the JWK URI endpoint for these algorithms.

Use the public keys to:

* Verify [client-side](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/client-side-tokens.html) token and ID token signatures.

* Encrypt JWTs in requests to the OpenID provider.

## Get the public keys

1. Find the JWK URI for the realm:

   ```bash
   $ curl https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/.well-known/openid-configuration
   {
     "...": "...",
     "jwks_uri": "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/connect/jwk_uri",
     "...": "..."
   }
   ```

   You can configure this URL under Native Consoles > Access Management for environments that centralize secrets. Go to Realms > *Realm Name* > Services > OAuth2 Provider > Advanced OpenID Connect and refer to the Remote JSON Web Key URL setting.

2. Get the JWK document from the URL:

   ```bash
   $ curl https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/connect/jwk_uri
   ```

   > **Collapse: Show output**
   >
   > ```json
   > {
   >   "keys": [{
   >     "kty": "RSA",
   >     "kid": "MYv/TlhD38w0GVgX3sohEWb6th0=",
   >     "use": "sig",
   >     "x5t": "k9hH5MSeIX4uJel1Fm9sCj3dzL4",
   >     "x5c": ["MIIDXzCCAkegAwIBAgIEQd+MMTANBgkqhkiG9w0BAQsFADBgMQswCQYDVQQGEwJVSzEQMA4GA1UECBMHQnJpc3RvbDEQMA4GA1UEBxMHQnJpc3RvbDESMBAGA1UEChMJRm9yZ2VSb2NrMRkwFwYDVQQDExByc2Fqd3RzaWduaW5na2V5MB4XDTIzMDExOTEyMjgyOVoXDTMzMDExNjEyMjgyOVowYDELMAkGA1UEBhMCVUsxEDAOBgNVBAgTB0JyaXN0b2wxEDAOBgNVBAcTB0JyaXN0b2wxEjAQBgNVBAoTCUZvcmdlUm9jazEZMBcGA1UEAxMQcnNhand0c2lnbmluZ2tleTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAJJQEAULAN7o/KE5Z5UYdYx/ygiEZBFidklr4UsZM3kePNvtCj07sGWQN1+z0vKQhdY+SCZoamCvUEGWZWyd0vJ8nCLBkNBJ33IFyDCsNMUlV9dEG+POYCrZ3TIshacyRBd7P/BJnTkdMItDrHHBD3l0xuDMKg+9AYJ0VN5AQXo7QJeLaEF1y0zu7C7CcjWgNjcaeZv6xgHzIt8ymKhd16zYXNIQBEvTWogHpBSpgTJcfUSymwAsTzrp+58ajqoTqQVRVr5I7rm3UiSnbZhU6Jo3H9QTZmIfAcDachTPHoG+nv7C+P7wK3EekJZ73Ur9CFjdIoS39fsLWth+LVLOTC8CAwEAAaMhMB8wHQYDVR0OBBYEFOGC/Ohfg0Cm5zVeQimMP3De6ZUbMA0GCSqGSIb3DQEBCwUAA4IBAQCNBeB9lpisaYBQdt3cM9F1PeA99llbqPVLpiZOOhSX+iPMjfijhr7Y/f23YRMRiLVSTuMzJrNCX2CZhUqBCF8TkbWz4/ahyEKJ3VbdJOde3LfZqzw0Jjh3fnWqOa2L0IehvKd4F+m7iRpZ8T6bYaKMU/t0TLQraOiO3w7zKLY1AlQxlXq4yMVqCuwvpAEF/eT7sKrjR8fE7o8NMnpU/Kc7hxi1GiUZHyqSBKKpAYRlJnDgc0+4jw/UUZW4fK0xcnHlZMntAGevTIMQ+r9GrRZAB2L3gqnlyBp1DIQnnm71wZk4AtpNm5xAS7rETdUlqkFn+LjoR+oIogI9RG25/wir"],
   >     "n": "klAQBQsA3uj8oTlnlRh1jH_KCIRkEWJ2SWvhSxkzeR482-0KPTuwZZA3X7PS8pCF1j5IJmhqYK9QQZZlbJ3S8nycIsGQ0EnfcgXIMKw0xSVX10Qb485gKtndMiyFpzJEF3s_8EmdOR0wi0OsccEPeXTG4MwqD70BgnRU3kBBejtAl4toQXXLTO7sLsJyNaA2Nxp5m_rGAfMi3zKYqF3XrNhc0hAES9NaiAekFKmBMlx9RLKbACxPOun7nxqOqhOpBVFWvkjuubdSJKdtmFTomjcf1BNmYh8BwNpyFM8egb6e_sL4_vArcR6QlnvdSv0IWN0ihLf1-wta2H4tUs5MLw",
   >     "e": "AQAB"
   >   }, {
   >     "kty": "RSA",
   >     "kid": "DrIvwoQHwRVcHHRFbSL9ZmhzjyU=",
   >     "use": "sig",
   >     "x5t": "fbzc7G87EHyhLjU-2y9Dpe_kN64",
   >     "x5c": ["MIIDZzCCAk+gAwIBAgIEO1Q8YDANBgkqhkiG9w0BAQsFADBkMQswCQYDVQQGEwJVSzEQMA4GA1UECBMHQnJpc3RvbDEQMA4GA1UEBxMHQnJpc3RvbDESMBAGA1UEChMJRm9yZ2VSb2NrMR0wGwYDVQQDExRyb290cnNhand0c2lnbmluZ2tleTAeFw0yMzAxMTkxMjI4MzdaFw0zMzAxMTYxMjI4MzdaMGQxCzAJBgNVBAYTAlVLMRAwDgYDVQQIEwdCcmlzdG9sMRAwDgYDVQQHEwdCcmlzdG9sMRIwEAYDVQQKEwlGb3JnZVJvY2sxHTAbBgNVBAMTFHJvb3Ryc2Fqd3RzaWduaW5na2V5MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAoLZ/A+akMJya3gKesHQNYP80rd8zSY6bpXqyMiWruTtnZ46KzWva1TlT384G0OvufMlILsx7j+/0uzkn9QwIb9RGYsJBy5zM+kS8N4m2qesoCBjWPFVqHqh/aCs4T2P78JvRyNq3hZ6lKJBgbsjzZNbFBxIReXjdJjSb85Wzivxn+bvVIrxUWHmeOznBR4yc5qeHEHef/l+ohD0mTn5dfsGJAXHNUpnqumvODQIU44BCnjpESoPauXGmkUKvJEQNFsTpA/npNHQHaHFQ5ZG/qjYBIo+LIX1TByZDo2Wsy/SkkXRnirUAZAZBRvg9NnLhk1gW0rCmK/hiQUfnjGORzQIDAQABoyEwHzAdBgNVHQ4EFgQUYfATQgXWdJzrvZqUzYhSZ31GEigwDQYJKoZIhvcNAQELBQADggEBAC92yt/0VP2jYXlSnNxSUAOyi7CwpwRXvkaPLgoDtNcuLHcQ8gcDpf8KjfLgc/cntBQAx3GBzAmtZmWBLRezioZMpcOtHyr+QC+TAtXwgM9t0LJZs1d0G8DOlgutItUIj5XRGfdedWOfFTbZpcqPxyTrDMN/TJ2+vMTxeLNiknxXMxIfUhMPJxRGCouppjeS1iMScNEHz4+zLdZUUngVwDvyB7qiqCHVcga8Mjy0S/weSnhwygL9tIB2yMLP9SR/R6Levy7FlMN5PUo0OzosAXgW+T5sGdXNV1AEOm47CDPm18sKsFCfTE+bS7ocUDka9y1XUNOMF/5l8f3EdyeTuUU="],
   >     "n": "oLZ_A-akMJya3gKesHQNYP80rd8zSY6bpXqyMiWruTtnZ46KzWva1TlT384G0OvufMlILsx7j-_0uzkn9QwIb9RGYsJBy5zM-kS8N4m2qesoCBjWPFVqHqh_aCs4T2P78JvRyNq3hZ6lKJBgbsjzZNbFBxIReXjdJjSb85Wzivxn-bvVIrxUWHmeOznBR4yc5qeHEHef_l-ohD0mTn5dfsGJAXHNUpnqumvODQIU44BCnjpESoPauXGmkUKvJEQNFsTpA_npNHQHaHFQ5ZG_qjYBIo-LIX1TByZDo2Wsy_SkkXRnirUAZAZBRvg9NnLhk1gW0rCmK_hiQUfnjGORzQ",
   >     "e": "AQAB"
   >   }, {
   >     "kty": "EC",
   >     "kid": "s7OzLXANBDUW8Myo0I1yQeCcuAc=",
   >     "use": "sig",
   >     "x5t": "CtmuzY0XUHBnGM7DAkY20Jgs9RU",
   >     "x5c": ["MIIByTCCAW2gAwIBAgIERJnPgjAMBggqhkjOPQQDAgUAMFkxCzAJBgNVBAYTAlVLMRAwDgYDVQQIEwdCcmlzdG9sMRAwDgYDVQQHEwdCcmlzdG9sMRIwEAYDVQQKEwlGb3JnZVJvY2sxEjAQBgNVBAMTCXJvb3RlczI1NjAeFw0yMzAxMTkxMjI4MzhaFw0zMzAxMTYxMjI4MzhaMFkxCzAJBgNVBAYTAlVLMRAwDgYDVQQIEwdCcmlzdG9sMRAwDgYDVQQHEwdCcmlzdG9sMRIwEAYDVQQKEwlGb3JnZVJvY2sxEjAQBgNVBAMTCXJvb3RlczI1NjBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABDV9wD5qzexs4+d9V6lCpr2125aa0sBBKSI0rOke5qH59jjNumIqdE3Jkl1JD3Z7+T97Ks9yLpOGdMyuDGD7Lw2jITAfMB0GA1UdDgQWBBQgb74nT1QSaZTfNEcP+V9HtwvecTAMBggqhkjOPQQDAgUAA0gAMEUCIDFIRiNz/MYoiTt6ekzhJkfcTqoxGaI3KSXdi4kpe/CKAiEAmHH3RmJvvzDU2wL3gfmz6Dbh/z12dM2pHuKfx5Oxng8="],
   >     "x": "NX3APmrN7Gzj531XqUKmvbXblprSwEEpIjSs6R7mofk",
   >     "y": "9jjNumIqdE3Jkl1JD3Z7-T97Ks9yLpOGdMyuDGD7Lw0",
   >     "crv": "P-256"
   >   }, {
   >     "kty": "EC",
   >     "kid": "Vk1FaV5otMm1mCT0KV11xT8FcOE=",
   >     "use": "sig",
   >     "x5t": "-rTXPQRN3T911Ptndy0mEYzIiUM",
   >     "x5c": ["MIIByjCCAW2gAwIBAgIELtQUtjAMBggqhkjOPQQDAgUAMFkxCzAJBgNVBAYTAlVLMRAwDgYDVQQIEwdCcmlzdG9sMRAwDgYDVQQHEwdCcmlzdG9sMRIwEAYDVQQKEwlGb3JnZVJvY2sxEjAQBgNVBAMTCWVzMjU2dGVzdDAeFw0yMzAxMTkxMjI4MzNaFw0zMzAxMTYxMjI4MzNaMFkxCzAJBgNVBAYTAlVLMRAwDgYDVQQIEwdCcmlzdG9sMRAwDgYDVQQHEwdCcmlzdG9sMRIwEAYDVQQKEwlGb3JnZVJvY2sxEjAQBgNVBAMTCWVzMjU2dGVzdDBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABIN/4K0xJ9/pbB4c9FrFaof+Qn3LB0FSk+HX74QlZCQV56HVQX/EKYybQ6Obxh3u+2d6nXtZaefT3i8wr2eHXQejITAfMB0GA1UdDgQWBBRldniKHv9Iw5blbdv83JwG4PVUJDAMBggqhkjOPQQDAgUAA0kAMEYCIQCjr6KY7x8UCC64WFUPI/aP29fVRxU+eAr3NEcfjhcLFwIhAJJN84FQ1zfwv3OWTO8LgGVRs1vnJk+KnFqNiCR78TKF"],
   >     "x": "g3_grTEn3-lsHhz0WsVqh_5CfcsHQVKT4dfvhCVkJBU",
   >     "y": "56HVQX_EKYybQ6Obxh3u-2d6nXtZaefT3i8wr2eHXQc",
   >     "crv": "P-256"
   >   }, {
   >     "kty": "EC",
   >     "kid": "zNgTfu5cYR6ZSbHLPGvukpGxwcY=",
   >     "use": "sig",
   >     "x5t": "AgVJFiiEJ_mvdlHua8ln7GdsvFc",
   >     "x5c": ["MIICBzCCAYqgAwIBAgIELvvnwTAMBggqhkjOPQQDAgUAMFkxCzAJBgNVBAYTAlVLMRAwDgYDVQQIEwdCcmlzdG9sMRAwDgYDVQQHEwdCcmlzdG9sMRIwEAYDVQQKEwlGb3JnZVJvY2sxEjAQBgNVBAMTCXJvb3RlczM4NDAeFw0yMzAxMTkxMjI4MzhaFw0zMzAxMTYxMjI4MzhaMFkxCzAJBgNVBAYTAlVLMRAwDgYDVQQIEwdCcmlzdG9sMRAwDgYDVQQHEwdCcmlzdG9sMRIwEAYDVQQKEwlGb3JnZVJvY2sxEjAQBgNVBAMTCXJvb3RlczM4NDB2MBAGByqGSM49AgEGBSuBBAAiA2IABN6cQkzM/6Os4RyVhYkbDi0jxdWxArduHofBvBylM9WZDhz5/U8bTXj6UhiRhdK04rLxmHlC7MUEZqAMsfh946mHzYEYO/nx9d3D1UNnVOaQLZljHAAhPgvekGw5IsE/m6MhMB8wHQYDVR0OBBYEFNaDy6uHT0Ibd4LXw2u0vpIjQ7IBMAwGCCqGSM49BAMCBQADaQAwZgIxAJ/1IPrcke2l3syjXfNQ29/6RGDGXcUrHrJZlVdukyz4agFmN45Tu8W9bSy0FRDLSwIxAMrJ8qPxXnEaByOo/sD+t5GkyKlCu9xlNs7p8beAnREWeSM5u9uMdO6uqXOC7WCstg=="],
   >     "x": "3pxCTMz_o6zhHJWFiRsOLSPF1bECt24eh8G8HKUz1ZkOHPn9TxtNePpSGJGF0rTi",
   >     "y": "svGYeULsxQRmoAyx-H3jqYfNgRg7-fH13cPVQ2dU5pAtmWMcACE-C96QbDkiwT-b",
   >     "crv": "P-384"
   >   }, {
   >     "kty": "EC",
   >     "kid": "igSqgQx2wx1F187ufOGT5wWM8j0=",
   >     "use": "sig",
   >     "x5t": "tVMwgfvP7QHEExZdxthK7koyO-Q",
   >     "x5c": ["MIICBzCCAYqgAwIBAgIEe8AuITAMBggqhkjOPQQDAgUAMFkxCzAJBgNVBAYTAlVLMRAwDgYDVQQIEwdCcmlzdG9sMRAwDgYDVQQHEwdCcmlzdG9sMRIwEAYDVQQKEwlGb3JnZVJvY2sxEjAQBgNVBAMTCWVzMzg0dGVzdDAeFw0yMzAxMTkxMjI4MzRaFw0zMzAxMTYxMjI4MzRaMFkxCzAJBgNVBAYTAlVLMRAwDgYDVQQIEwdCcmlzdG9sMRAwDgYDVQQHEwdCcmlzdG9sMRIwEAYDVQQKEwlGb3JnZVJvY2sxEjAQBgNVBAMTCWVzMzg0dGVzdDB2MBAGByqGSM49AgEGBSuBBAAiA2IABAXFfBc3njCvEMTpJ1V9Z4gNFpPrQ5PvXMrrwkudfZFtHKX5yh+1jXvluzVjyE8bYyGrGdI15I43p2M8ndkc172b6JFXObe3UTDGBQ6wgLlQId/lINg2/b07dBKihMYNyKMhMB8wHQYDVR0OBBYEFJRHSSDilIKZJSrApiChJYdCD35QMAwGCCqGSM49BAMCBQADaQAwZgIxAJz/Ly5iwXU86LEG21d8Flc2x5kYplEMp6LNVryrkHl8MZtqyOi8FN9o4AEO+NBgWgIxAO7N/feVYcf/z/fr7itPh36jXwfgrwuBTjkeD6Z7FOxjcBW/4bv+YvU5FLkfMk/5sw=="],
   >     "x": "BcV8FzeeMK8QxOknVX1niA0Wk-tDk-9cyuvCS519kW0cpfnKH7WNe-W7NWPITxtj",
   >     "y": "IasZ0jXkjjenYzyd2RzXvZvokVc5t7dRMMYFDrCAuVAh3-Ug2Db9vTt0EqKExg3I",
   >     "crv": "P-384"
   >   }, {
   >     "kty": "EC",
   >     "kid": "kEhluv9X13opjgFSKMBRE4EEjXk=",
   >     "use": "sig",
   >     "x5t": "p7w9otFuu1-ENpumFYLFHVG984o",
   >     "x5c": ["MIICUTCCAbCgAwIBAgIEBg1ErTAMBggqhkjOPQQDAgUAMFkxCzAJBgNVBAYTAlVLMRAwDgYDVQQIEwdCcmlzdG9sMRAwDgYDVQQHEwdCcmlzdG9sMRIwEAYDVQQKEwlGb3JnZVJvY2sxEjAQBgNVBAMTCXJvb3RlczUxMjAeFw0yMzAxMTkxMjI4MzlaFw0zMzAxMTYxMjI4MzlaMFkxCzAJBgNVBAYTAlVLMRAwDgYDVQQIEwdCcmlzdG9sMRAwDgYDVQQHEwdCcmlzdG9sMRIwEAYDVQQKEwlGb3JnZVJvY2sxEjAQBgNVBAMTCXJvb3RlczUxMjCBmzAQBgcqhkjOPQIBBgUrgQQAIwOBhgAEAJXY9YQASxZOEd+wCcLqv8tgUAgON441OMkw2jrwRLUFJI1Ea0OH7T+d5NBvAaBaQVtnTSz5vKF1CkBmJ0bEjPi5AWQKhmiYasEe10leO9JHCAjkCdzOmyywBSP1xcmtj4FnAG37m4xBS280bne9JRDxLIB9xUbU2EtdMm4ACVVmAmF7oyEwHzAdBgNVHQ4EFgQU1uoPEjS5YEokAunQ5bjKfG6pH58wDAYIKoZIzj0EAwIFAAOBjAAwgYgCQgCpY3EmdV2gc7ueaR4PeAIUSp1oKZOA1F2oCwIhsCMdhZQ0MX3g417EiZNEuw1BXw/X09parjlmRcIJYF1xqrNyewJCAX1g6Hr+er5EemcibCroG6iTZWwKP5wtsMwez3IUNJvL1y7M/9e4hMlavoH5YH8qwMUx3jW9IK97wgfYjF660+5l"],
   >     "x": "AJXY9YQASxZOEd-wCcLqv8tgUAgON441OMkw2jrwRLUFJI1Ea0OH7T-d5NBvAaBaQVtnTSz5vKF1CkBmJ0bEjPi5",
   >     "y": "AWQKhmiYasEe10leO9JHCAjkCdzOmyywBSP1xcmtj4FnAG37m4xBS280bne9JRDxLIB9xUbU2EtdMm4ACVVmAmF7",
   >     "crv": "P-521"
   >   }, {
   >     "kty": "EC",
   >     "kid": "Rrrq9yW/SWBRaUu8b/Y1XE8sTJo=",
   >     "use": "sig",
   >     "x5t": "nknxGS3FgRImILz7D9WkLtUjw8E",
   >     "x5c": ["MIICUDCCAbCgAwIBAgIEfalB2jAMBggqhkjOPQQDAgUAMFkxCzAJBgNVBAYTAlVLMRAwDgYDVQQIEwdCcmlzdG9sMRAwDgYDVQQHEwdCcmlzdG9sMRIwEAYDVQQKEwlGb3JnZVJvY2sxEjAQBgNVBAMTCWVzNTEydGVzdDAeFw0yMzAxMTkxMjI4MzRaFw0zMzAxMTYxMjI4MzRaMFkxCzAJBgNVBAYTAlVLMRAwDgYDVQQIEwdCcmlzdG9sMRAwDgYDVQQHEwdCcmlzdG9sMRIwEAYDVQQKEwlGb3JnZVJvY2sxEjAQBgNVBAMTCWVzNTEydGVzdDCBmzAQBgcqhkjOPQIBBgUrgQQAIwOBhgAEAK5lS4amgq+TTYzzRAT3FqNx6tekRYk+26Y0p1cHSVV8a/ity0id860YwfUDYmrHE2jqAWJcw/dUt/mTlkMNo5SiAUOr2lANh8oklFBpHxT0PZFnDIj7pJZh634LJLP6wJBS60rgkQJgautJFWi1TubsJSBUfF4A/eWnljnZ0ZBJk5oyEwHzAdBgNVHQ4EFgQUAv5x0hRmIlGMvE9LR/SFUokpUIswDAYIKoZIzj0EAwIFAAOBiwAwgYcCQgCyoKbFcDPVne7z6SNEOIF4+sgjPmKuA3ldnno7UGLFiOaQD2MOs4YeZxBRjoyuKkdE0af1NUwgE7BhpcoHPHaGSQJBPeqfWxeUwiVSWLX4w5vTQ52z5GZTiJ0CcJR+9IxGLfvmOX1vEcf1eLEbFvSl9QDPdMEVCdCkFiOwl7xXI4rFttw="],
   >     "x": "AK5lS4amgq-TTYzzRAT3FqNx6tekRYk-26Y0p1cHSVV8a_ity0id860YwfUDYmrHE2jqAWJcw_dUt_mTlkMNo5Si",
   >     "y": "AUOr2lANh8o--klFBpHxT0PZFnDIj7pJZh634LJLP6wJBS60rgkQJgautJFWi1TubsJSBUfF4A_eWnljnZ0ZBJk5",
   >     "crv": "P-521"
   >   }, {
   >     "kty": "RSA",
   >     "kid": "VDxi9hGYuVbDoq51t5IwcQFABGc=",
   >     "use": "enc",
   >     "x5t": "6_iP-K76eLLL-uYQxf354ab_4Zg",
   >     "x5c": ["MIIDTTCCAjWgAwIBAgIEGpMm4jANBgkqhkiG9w0BAQsFADBXMQswCQYDVQQGEwJVSzEQMA4GA1UECBMHQnJpc3RvbDEQMA4GA1UEBxMHQnJpc3RvbDESMBAGA1UEChMJRm9yZ2VSb2NrMRAwDgYDVQQDEwdyb290cnNhMB4XDTIzMDExOTEyMjg0MloXDTMzMDExNjEyMjg0MlowVzELMAkGA1UEBhMCVUsxEDAOBgNVBAgTB0JyaXN0b2wxEDAOBgNVBAcTB0JyaXN0b2wxEjAQBgNVBAoTCUZvcmdlUm9jazEQMA4GA1UEAxMHcm9vdHJzYTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAJ4T8vYf5PNvXr24MxUBCvoL6XHDAQATdCsFc9MTRwYXZq91OzkSuSUi8yyPbgWBVA28UWdZ7WILAFYdPYH7MdVuBQtFnLTrAc2CkkHRmRGgTXfXu9bB4cdKO5Mu+q8fsXVSjW07dQdTH2gPmzFCRa6nZt3WgXOy6v92wrf3IlcRPkcVPSFstBVA+8NtsCbTx+cx8weI8b19BPvk48rWY1wMWDuFMr7ZdNKT2TBgrW9WJWl0hItBmFBP6ocCWW/2/kD4kibzlL0Sh8bjkdDHfUti/o8XautqA6E4Eq/qukSWLpyS+O7O0SoFoRaaK2runKePdwZYJO1hcTj2PUjE3M8CAwEAAaMhMB8wHQYDVR0OBBYEFFk7PS1vpDxAQkEpQq/CaNONbVJ/MA0GCSqGSIb3DQEBCwUAA4IBAQCZ0g9sshKzqbQzeEpvDvV1u+Pb8lvUu/Vsc0Xzv75sDFzwO23EdocaSb5l4lmQrtOxXlntgqcrOHNjGSvh7dMzBfoWdz2HE58m7w0mBWMGo5MxwUL3AW1R3tj+0I//18zd7COtg5h+xd+LlVgIdilu5CzL+vpr4jzq/073iFS2l6n3rE+48AM5sa/6B/vWDl06PPrtKHQeKb2Cv/6NoLIMGQ9rMeIgts9yBCu9wj5JvhAhIqd8JbmiLEVEKsQsIDtGlZxjmEAL5vx7Y2OxYzzv5H5HCAoQ/2YuXtiy3sPKmfnrlgNS6dfslzbqNAKWypwV0GArA7p9rF3pqpiZEvyJ"],
   >     "n": "nhPy9h_k829evbgzFQEK-gvpccMBABN0KwVz0xNHBhdmr3U7ORK5JSLzLI9uBYFUDbxRZ1ntYgsAVh09gfsx1W4FC0WctOsBzYKSQdGZEaBNd9e71sHhx0o7ky76rx-xdVKNbTt1B1MfaA-bMUJFrqdm3daBc7Lq_3bCt_ciVxE-RxU9IWy0FUD7w22wJtPH5zHzB4jxvX0E--TjytZjXAxYO4Uyvtl00pPZMGCtb1YlaXSEi0GYUE_qhwJZb_b-QPiSJvOUvRKHxuOR0Md9S2L-jxdq62oDoTgSr-q6RJYunJL47s7RKgWhFporau6cp493Blgk7WFxOPY9SMTczw",
   >     "e": "AQAB"
   >   }, {
   >     "kty": "RSA",
   >     "kid": "psCC6uRbKBVcNTyFtuJFVNb26rI=",
   >     "use": "enc",
   >     "x5t": "KtkFu6I45dMRcibibl1-IQn2Jvw",
   >     "x5c": ["MIIDRzCCAi+gAwIBAgIELhfI4zANBgkqhkiG9w0BAQsFADBUMQswCQYDVQQGEwJVSzEQMA4GA1UECBMHQnJpc3RvbDEQMA4GA1UEBxMHQnJpc3RvbDESMBAGA1UEChMJRm9yZ2VSb2NrMQ0wCwYDVQQDEwR0ZXN0MB4XDTIzMDExOTEyMjgzMFoXDTMzMDExNjEyMjgzMFowVDELMAkGA1UEBhMCVUsxEDAOBgNVBAgTB0JyaXN0b2wxEDAOBgNVBAcTB0JyaXN0b2wxEjAQBgNVBAoTCUZvcmdlUm9jazENMAsGA1UEAxMEdGVzdDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAI4aa02Lgy7sHkkJj+8wSUuruq1dZTAHujNSaDRXVoFVDQgQOeYTrc1VoN0GK2Q7nn3kib1mohzaW7rlD9LB7cP2e2e56dHi1VViPBowZ2uCQZ09sA4yqzH8ed8HlpgwHeBLp/ahFU9WyA+TnYqRsaGe0EMj2q3QQ78fte1AIkWSiscTiR2X0A9xU0fnxy0okomECosEmFEFA7xOTEmy2Nov4VdrScGAemf6xO3U3jHqxbpAG2Yrm+1YZ6DMfXlXChgncmZuL2eY7X9Ng5N9swjxpXQPhDBm7qjNbUmFPwNACrmT19lc3dm3R1LqIsJK/sr/rFUOOTI1BfdVSSKLcCAwEAAaMhMB8wHQYDVR0OBBYEFFWUtlIpEssnvClgxK458NUc+SVLMA0GCSqGSIb3DQEBCwUAA4IBAQBrRsjifKGxL3wjVh2Fh8ilMHpf3rfOcDQqehokVvnCZFGabCGX818s9jRJVU61AnOqqgw3tBRSzr1VzEz/LvMHBqXvtZdrZgtO4EyD2qK/+aFj5DZRZeCS3v+5BPJbwLN9fPixJ+LqtQRw98aiWhOVaVLOWZDb7Nli1HOBfCatkeXuOw8ZwOhN4fVNkidwzGka3tng1OzU5fjLUBx1IFhDJaRw0nOOcOBaT51+4Ac+bbjXtt+UzGYCmZT0kOa7wK0MQtl783s/VGf2LCme5GGzqoDEbvyR1fxvtM8/h/WDw8xr+QF+i0GddYMOxRIyHpl1TM8YhN9W1nVGsdXg4HQs"],
   >     "n": "jhprTYuDLuweSQmP7zBJS6u6rV1lMAe6M1JoNFdWgVUNCBA55hOtzVWg3QYrZDuefeSJvWaiHNpb77uuUP0sHtw_Z7Z7np0eLVVWI8GjBna4JBnT2wDjKrMfx53weWmDAd4Eun9qEVT1bID5OdipGxoZ7QQyPardBDvx-17UAiRZKKxxOJHZfQD3FTR-fHLSiSiYQKiwSYUQUDvE5MSbLY2i_hV2tJwYB6Z_rE7dTeMerFukAbZiub7VhnoMx9eVcKGCdyZm4vZ5jtf02Dk32zCPGldA-EMGbuqM1tSYU_A0AKuZPX2Vzd2bdHUuoiwkr-yv-sVQ45MjUF91VJIotw",
   >     "e": "AQAB"
   >   }]
   > }
   > ```

## Display all algorithms and key types

By default, as recommended by the *JSON Web Key* specification, each [key ID (`kid`)](https://www.rfc-editor.org/rfc/rfc7517.html#section-4.5) in the JWK matches a unique secret. Each `kid` has one key type and one associated algorithm.

You can configure the endpoint to display multiple keys for a `kid` as different keys in the JWK. With this setting, a `kid` no longer uniquely identifies a secret:

1. Under Native Consoles > Access Management, go to Realms > *Realm Name* > Services > OAuth2 Provider > Advanced OpenID Connect.

2. Enable Include all kty and alg combinations in jwks\_uri.

3. Save your changes.

4. Verify the results by [getting the JWK document](#obtaining-public-signing-key).

## Map custom key IDs to secrets

If your deployment requires custom key IDs provided by a third party, you can map those key IDs to Advanced Identity Cloud [secrets](https://docs.pingidentity.com/pingoneaic/latest/tenants/esvs.html#secrets).

When Advanced Identity Cloud signs a JWT using the secret, the `kid` header parameter in the JWT is the custom `kid`.

1. Under Native Consoles > Access Management, go to Realms > *Realm Name* > Services > OAuth2 Provider > Advanced OpenID Connect.

2. Make sure Remote JSON Web Key URL contains the URI of your secrets API.

3. Under JWT Signing kid Header Mappings, add mappings from the secret aliases of the key used to sign JWTs to the custom `kid` header values.

   * Key is the secret alias of the key used to sign the given JWT.

   * Value is the custom `kid` value.

4. Click + Add for each mapping.

5. Save your changes.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | * The custom `kid` is applied for any signed JWT that's part of communication between the OAuth 2.0 client application and Advanced Identity Cloud. This includes:

  * Stateless access tokens

  * Stateless refresh tokens

  * Device code JWTs

  * OIDC ID tokens

  * Token introspection responses when the format is JWT

  * User info responses when the format is JWT

  * Authorization response JWTs

* If the same alias is mapped to the same secret label across different keystores, the custom `kid` will apply for *all* secrets that share that alias.

  You should map each secret label only once per realm. |

---

---
title: /oauth2/connect/rp/jwk_uri
description: This endpoint is similar to the /oauth2/connect/jwk_uri endpoint defined in OpenID Connect Discovery 1.0. It exposes the public keys for Advanced Identity Cloud acting as a relying party; for example, in a social authentication scenario.
component: pingoneaic-api
page_id: pingoneaic-api:am-oidc1:managing-rp-jwk_uri
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-oidc1/managing-rp-jwk_uri.html
keywords: ["OpenID Connect (OIDC)", "Standards", "Setup &amp; Configuration", "Security", "Endpoints"]
---

# /oauth2/connect/rp/jwk\_uri

This endpoint is similar to the [/oauth2/connect/jwk\_uri](managing-jwk_uri.html) endpoint defined in [OpenID Connect Discovery 1.0](https://openid.net/specs/openid-connect-discovery-1_0.html). It exposes the public keys for Advanced Identity Cloud acting as a relying party; for example, in a [social authentication](https://docs.pingidentity.com/pingoneaic/latest/self-service/social-registration.html) scenario.

Use this endpoint to get the relying party public keys as a JSON Web Key (JWK) document. For details about how to use this endpoint at your OpenID provider, refer to the provider's documentation.

The provider can use the public keys to:

* Encrypt ID tokens issued to Advanced Identity Cloud.

* Verify signatures on JWTs in requests from Advanced Identity Cloud.

* Decrypt client authentication JWTs from Advanced Identity Cloud.

Specify the realm in the request URL; for example:

```bash
$ curl https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/connect/rp/jwk_uri
```

> **Collapse: Show output**
>
> ```json
> {
>   "keys": [{
>     "kty": "RSA",
>     "kid": "VDxi9hGYuVbDoq51t5IwcQFABGc=",
>     "use": "enc",
>     "x5t": "6_iP-K76eLLL-uYQxf354ab_4Zg",
>     "x5c": ["MIIDTTCCAjWgAwIBAgIEGpMm4jANBgkqhkiG9w0BAQsFADBXMQswCQYDVQQGEwJVSzEQMA4GA1UECBMHQnJpc3RvbDEQMA4GA1UEBxMHQnJpc3RvbDESMBAGA1UEChMJRm9yZ2VSb2NrMRAwDgYDVQQDEwdyb290cnNhMB4XDTIzMDExOTEyMjg0MloXDTMzMDExNjEyMjg0MlowVzELMAkGA1UEBhMCVUsxEDAOBgNVBAgTB0JyaXN0b2wxEDAOBgNVBAcTB0JyaXN0b2wxEjAQBgNVBAoTCUZvcmdlUm9jazEQMA4GA1UEAxMHcm9vdHJzYTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAJ4T8vYf5PNvXr24MxUBCvoL6XHDAQATdCsFc9MTRwYXZq91OzkSuSUi8yyPbgWBVA28UWdZ7WILAFYdPYH7MdVuBQtFnLTrAc2CkkHRmRGgTXfXu9bB4cdKO5Mu+q8fsXVSjW07dQdTH2gPmzFCRa6nZt3WgXOy6v92wrf3IlcRPkcVPSFstBVA+8NtsCbTx+cx8weI8b19BPvk48rWY1wMWDuFMr7ZdNKT2TBgrW9WJWl0hItBmFBP6ocCWW/2/kD4kibzlL0Sh8bjkdDHfUti/o8XautqA6E4Eq/qukSWLpyS+O7O0SoFoRaaK2runKePdwZYJO1hcTj2PUjE3M8CAwEAAaMhMB8wHQYDVR0OBBYEFFk7PS1vpDxAQkEpQq/CaNONbVJ/MA0GCSqGSIb3DQEBCwUAA4IBAQCZ0g9sshKzqbQzeEpvDvV1u+Pb8lvUu/Vsc0Xzv75sDFzwO23EdocaSb5l4lmQrtOxXlntgqcrOHNjGSvh7dMzBfoWdz2HE58m7w0mBWMGo5MxwUL3AW1R3tj+0I//18zd7COtg5h+xd+LlVgIdilu5CzL+vpr4jzq/073iFS2l6n3rE+48AM5sa/6B/vWDl06PPrtKHQeKb2Cv/6NoLIMGQ9rMeIgts9yBCu9wj5JvhAhIqd8JbmiLEVEKsQsIDtGlZxjmEAL5vx7Y2OxYzzv5H5HCAoQ/2YuXtiy3sPKmfnrlgNS6dfslzbqNAKWypwV0GArA7p9rF3pqpiZEvyJ"],
>     "n": "nhPy9h_k829evbgzFQEK-gvpccMBABN0KwVz0xNHBhdmr3U7ORK5JSLzLI9uBYFUDbxRZ1ntYgsAVh09gfsx1W4FC0WctOsBzYKSQdGZEaBNd9e71sHhx0o7ky76rx-xdVKNbTt1B1MfaA-bMUJFrqdm3daBc7Lq_3bCt_ciVxE-RxU9IWy0FUD7w22wJtPH5zHzB4jxvX0E—​TjytZjXAxYO4Uyvtl00pPZMGCtb1YlaXSEi0GYUE_qhwJZb_b-QPiSJvOUvRKHxuOR0Md9S2L-jxdq62oDoTgSr-q6RJYunJL47s7RKgWhFporau6cp493Blgk7WFxOPY9SMTczw",
>     "e": "AQAB"
>   }, {
>     "kty": "RSA",
>     "kid": "DrIvwoQHwRVcHHRFbSL9ZmhzjyU=",
>     "use": "sig",
>     "x5t": "fbzc7G87EHyhLjU-2y9Dpe_kN64",
>     "x5c": ["MIIDZzCCAk+gAwIBAgIEO1Q8YDANBgkqhkiG9w0BAQsFADBkMQswCQYDVQQGEwJVSzEQMA4GA1UECBMHQnJpc3RvbDEQMA4GA1UEBxMHQnJpc3RvbDESMBAGA1UEChMJRm9yZ2VSb2NrMR0wGwYDVQQDExRyb290cnNhand0c2lnbmluZ2tleTAeFw0yMzAxMTkxMjI4MzdaFw0zMzAxMTYxMjI4MzdaMGQxCzAJBgNVBAYTAlVLMRAwDgYDVQQIEwdCcmlzdG9sMRAwDgYDVQQHEwdCcmlzdG9sMRIwEAYDVQQKEwlGb3JnZVJvY2sxHTAbBgNVBAMTFHJvb3Ryc2Fqd3RzaWduaW5na2V5MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAoLZ/A+akMJya3gKesHQNYP80rd8zSY6bpXqyMiWruTtnZ46KzWva1TlT384G0OvufMlILsx7j+/0uzkn9QwIb9RGYsJBy5zM+kS8N4m2qesoCBjWPFVqHqh/aCs4T2P78JvRyNq3hZ6lKJBgbsjzZNbFBxIReXjdJjSb85Wzivxn+bvVIrxUWHmeOznBR4yc5qeHEHef/l+ohD0mTn5dfsGJAXHNUpnqumvODQIU44BCnjpESoPauXGmkUKvJEQNFsTpA/npNHQHaHFQ5ZG/qjYBIo+LIX1TByZDo2Wsy/SkkXRnirUAZAZBRvg9NnLhk1gW0rCmK/hiQUfnjGORzQIDAQABoyEwHzAdBgNVHQ4EFgQUYfATQgXWdJzrvZqUzYhSZ31GEigwDQYJKoZIhvcNAQELBQADggEBAC92yt/0VP2jYXlSnNxSUAOyi7CwpwRXvkaPLgoDtNcuLHcQ8gcDpf8KjfLgc/cntBQAx3GBzAmtZmWBLRezioZMpcOtHyr+QC+TAtXwgM9t0LJZs1d0G8DOlgutItUIj5XRGfdedWOfFTbZpcqPxyTrDMN/TJ2+vMTxeLNiknxXMxIfUhMPJxRGCouppjeS1iMScNEHz4+zLdZUUngVwDvyB7qiqCHVcga8Mjy0S/weSnhwygL9tIB2yMLP9SR/R6Levy7FlMN5PUo0OzosAXgW+T5sGdXNV1AEOm47CDPm18sKsFCfTE+bS7ocUDka9y1XUNOMF/5l8f3EdyeTuUU="],
>     "n": "oLZ_A-akMJya3gKesHQNYP80rd8zSY6bpXqyMiWruTtnZ46KzWva1TlT384G0OvufMlILsx7j-_0uzkn9QwIb9RGYsJBy5zM-kS8N4m2qesoCBjWPFVqHqh_aCs4T2P78JvRyNq3hZ6lKJBgbsjzZNbFBxIReXjdJjSb85Wzivxn-bvVIrxUWHmeOznBR4yc5qeHEHef_l-ohD0mTn5dfsGJAXHNUpnqumvODQIU44BCnjpESoPauXGmkUKvJEQNFsTpA_npNHQHaHFQ5ZG_qjYBIo-LIX1TByZDo2Wsy_SkkXRnirUAZAZBRvg9NnLhk1gW0rCmK_hiQUfnjGORzQ",
>     "e": "AQAB"
>   }, {
>     "kty": "RSA",
>     "kid": "MYv/TlhD38w0GVgX3sohEWb6th0=",
>     "use": "sig",
>     "x5t": "k9hH5MSeIX4uJel1Fm9sCj3dzL4",
>     "x5c": ["MIIDXzCCAkegAwIBAgIEQd+MMTANBgkqhkiG9w0BAQsFADBgMQswCQYDVQQGEwJVSzEQMA4GA1UECBMHQnJpc3RvbDEQMA4GA1UEBxMHQnJpc3RvbDESMBAGA1UEChMJRm9yZ2VSb2NrMRkwFwYDVQQDExByc2Fqd3RzaWduaW5na2V5MB4XDTIzMDExOTEyMjgyOVoXDTMzMDExNjEyMjgyOVowYDELMAkGA1UEBhMCVUsxEDAOBgNVBAgTB0JyaXN0b2wxEDAOBgNVBAcTB0JyaXN0b2wxEjAQBgNVBAoTCUZvcmdlUm9jazEZMBcGA1UEAxMQcnNhand0c2lnbmluZ2tleTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAJJQEAULAN7o/KE5Z5UYdYx/ygiEZBFidklr4UsZM3kePNvtCj07sGWQN1+z0vKQhdY+SCZoamCvUEGWZWyd0vJ8nCLBkNBJ33IFyDCsNMUlV9dEG+POYCrZ3TIshacyRBd7P/BJnTkdMItDrHHBD3l0xuDMKg+9AYJ0VN5AQXo7QJeLaEF1y0zu7C7CcjWgNjcaeZv6xgHzIt8ymKhd16zYXNIQBEvTWogHpBSpgTJcfUSymwAsTzrp+58ajqoTqQVRVr5I7rm3UiSnbZhU6Jo3H9QTZmIfAcDachTPHoG+nv7C+P7wK3EekJZ73Ur9CFjdIoS39fsLWth+LVLOTC8CAwEAAaMhMB8wHQYDVR0OBBYEFOGC/Ohfg0Cm5zVeQimMP3De6ZUbMA0GCSqGSIb3DQEBCwUAA4IBAQCNBeB9lpisaYBQdt3cM9F1PeA99llbqPVLpiZOOhSX+iPMjfijhr7Y/f23YRMRiLVSTuMzJrNCX2CZhUqBCF8TkbWz4/ahyEKJ3VbdJOde3LfZqzw0Jjh3fnWqOa2L0IehvKd4F+m7iRpZ8T6bYaKMU/t0TLQraOiO3w7zKLY1AlQxlXq4yMVqCuwvpAEF/eT7sKrjR8fE7o8NMnpU/Kc7hxi1GiUZHyqSBKKpAYRlJnDgc0+4jw/UUZW4fK0xcnHlZMntAGevTIMQ+r9GrRZAB2L3gqnlyBp1DIQnnm71wZk4AtpNm5xAS7rETdUlqkFn+LjoR+oIogI9RG25/wir"],
>     "n": "klAQBQsA3uj8oTlnlRh1jH_KCIRkEWJ2SWvhSxkzeR482-0KPTuwZZA3X7PS8pCF1j5IJmhqYK9QQZZlbJ3S8nycIsGQ0EnfcgXIMKw0xSVX10Qb485gKtndMiyFpzJEF3s_8EmdOR0wi0OsccEPeXTG4MwqD70BgnRU3kBBejtAl4toQXXLTO7sLsJyNaA2Nxp5m_rGAfMi3zKYqF3XrNhc0hAES9NaiAekFKmBMlx9RLKbACxPOun7nxqOqhOpBVFWvkjuubdSJKdtmFTomjcf1BNmYh8BwNpyFM8egb6e_sL4_vArcR6QlnvdSv0IWN0ihLf1-wta2H4tUs5MLw",
>     "e": "AQAB"
>   }]
> }
> ```

---

---
title: /oauth2/idtokeninfo
description: The /oauth2/idtokeninfo endpoint is an Advanced Identity Cloud-specific endpoint.
component: pingoneaic-api
page_id: pingoneaic-api:am-oidc1:rest-api-oidc-idtoken-validation
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-oidc1/rest-api-oidc-idtoken-validation.html
keywords: ["OpenID Connect (OIDC)", "Standards", "Endpoints"]
section_ids:
  supported-parameters: Supported parameters
  token-validation: Token validation
  examples: Examples
---

# /oauth2/idtokeninfo

The `/oauth2/idtokeninfo` endpoint is an Advanced Identity Cloud-specific endpoint.

Use this endpoint to validate *unencrypted* ID tokens and to retrieve claims in the token.

Specify the realm in the request URL; for example:

```none
https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/idtokeninfo
```

## Supported parameters

The ID token information endpoint supports the following parameters:

| Parameter               | Description                                                                                                      | Required                                                                                                                                     |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `claims`                | Comma-separated list of claims to return from the ID token.                                                      | Yes                                                                                                                                          |
| `client_assertion`      | A signed JSON Web Token (JWT) to use as client credentials.                                                      | Yes, for [JWT profile](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/client-auth-jwt.html) authentication                        |
| `client_assertion_type` | The type of assertion, `client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer`. | Yes, for [JWT profile](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/client-auth-jwt.html) authentication                        |
| `client_id`             | Uniquely identifies the application making the request.                                                          | Yes, when authentication is required (default)                                                                                               |
| `client_secret`         | The password for a confidential client.                                                                          | Yes, when authenticating with [Form parameters (HTTP POST)](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/client-auth-form.html) |
| `id_token`              | The ID token to validate.                                                                                        | Yes                                                                                                                                          |

By default, the client must authenticate to use the endpoint. Optionally disable this in the OAuth 2.0 provider configuration. Under Native Consoles > Access Management, go to Realms > *Realm Name* > Services > OAuth2 Provider > Advanced OpenID Connect and disable Idtokeninfo Endpoint Requires Client Authentication.

## Token validation

Advanced Identity Cloud validates the tokens based on rules in the [OpenID Connect Core](https://openid.net/specs/openid-connect-core-1_0.html#IDTokenValidation) specification. Token validation includes the following steps:

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
"https://<tenant-env-fqdn>/am/oauth2/idtokeninfo"
{
  "at_hash": "PZg5xZsIlFtRSfg8MAWhWg",
  "sub": "a0325ea4-9d9b-4056-931b-ab64704cc3da",
  "auditTrackingId": "2e5c7611-4a61-4001-8739-f714d43e9da2-881454",
  "subname": "a0325ea4-9d9b-4056-931b-ab64704cc3da",
  "iss": "https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha",
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
"https://<tenant-env-fqdn>/am/oauth2/idtokeninfo"
{
  "sub": "a0325ea4-9d9b-4056-931b-ab64704cc3da",
  "exp": 1676364398,
  "realm": "/alpha"
}
```

If you request a claim that does not exist, no error occurs; Advanced Identity Cloud omits the claim from the response.

---

---
title: /oauth2/register
description: The /oauth2/register endpoint is defined in:
component: pingoneaic-api
page_id: pingoneaic-api:am-oidc1:rest-api-oauth2-register-endpoint
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-oidc1/rest-api-oauth2-register-endpoint.html
keywords: ["OpenID Connect (OIDC)", "Standards", "Endpoints", "Self-Service"]
---

# /oauth2/register

The `/oauth2/register` endpoint is defined in:

* [OpenID Connect Dynamic Client Registration 1.0 incorporating errata set 1](https://openid.net/specs/openid-connect-registration-1_0.html)

* RFC 7591: [OAuth 2.0 Dynamic Client Registration Protocol](https://www.rfc-editor.org/rfc/rfc7591.html)

* RFC 7592: [OAuth 2.0 Dynamic Client Registration Management Protocol](https://www.rfc-editor.org/rfc/rfc7592.html)

Use this endpoint to create, read, update, and delete client application profiles.

Specify the realm in the request URL; for example:

```none
https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/register
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

Advanced Identity Cloud requires configuration to allow dynamic registration. Learn more in [Dynamic client registration](https://docs.pingidentity.com/pingoneaic/latest/am-oidc1/oauth2-dynamic-client-registration.html).

---

---
title: /oauth2/userinfo
description: The /oauth2/userinfo endpoint is the OpenID Connect (OIDC) UserInfo endpoint.
component: pingoneaic-api
page_id: pingoneaic-api:am-oidc1:rest-api-oidc-userinfo-endpoint
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-oidc1/rest-api-oidc-userinfo-endpoint.html
keywords: ["OpenID Connect (OIDC)", "Standards", "Endpoints"]
section_ids:
  response-signing-and-encryption: Response signing and encryption
---

# /oauth2/userinfo

The `/oauth2/userinfo` endpoint is the OpenID Connect (OIDC) [UserInfo endpoint](https://openid.net/specs/openid-connect-core-1_0.html#UserInfo).

Use this endpoint to request claims about the authenticated end user.

Specify the realm in the request URL; for example:

```none
https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/userinfo
```

To access the endpoint, use an access token from an OIDC grant flow as the bearer token. The endpoint returns claims based on the scopes granted for the access token as in the following example:

```bash
$ curl \
--request GET \
--header "Authorization: Bearer <access-token>" \
"https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/userinfo"
{
  "name": "Babs Jensen",
  "family_name": "Jensen",
  "given_name": "Babs",
  "sub": "a0325ea4-9d9b-4056-931b-ab64704cc3da",
  "subname": "a0325ea4-9d9b-4056-931b-ab64704cc3da"
}
```

## Response signing and encryption

The default response is a plain JSON object.

Advanced Identity Cloud also supports responding with a signed JSON Web Token (JWT) or signed and encrypted JWT. JWT responses include the `aud` and `iss` claims.

To enable signing and encryption, follow these steps:

1. In the Advanced Identity Cloud admin console, go to Applications > *Client ID* > Sign On > General Settings > Show advanced settings > Endpoint Response Formats and select the response type in the User info response format drop-down list.

2. Save your work.

Configure signing and encryption under Native Consoles > Access Management:

1. To add settings for a single client application, go to Realms > *Realm Name* > Applications > OAuth 2.0 > Clients > *Client ID* > Signing and Encryption and configure the following properties:

   * User info signed response algorithm

     No default

   * User info encrypted response algorithm

     No default

   * User info encrypted response encryption algorithm

     Default: `A128CBC-HS256`

2. To restrict the possible settings for the clients in the realm, edit the settings under Realms > *Realm Name* > Services > OAuth2 Provider > Advanced OpenID Connect.

3. Save your work.

Learn more in the OAuth 2.0 provider reference documentation for [advanced OIDC settings](https://docs.pingidentity.com/pingoneaic/latest/am-reference/realm-services-configuration.html#realm-oauth-oidc-advanced-openid-connect).

---

---
title: OIDC 1.0 endpoints
description: Your applications can use the following OpenID Connect (OIDC) endpoints:
component: pingoneaic-api
page_id: pingoneaic-api:am-oidc1:oidc-client-endpoints
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-oidc1/oidc-client-endpoints.html
keywords: ["OpenID Connect (OIDC)", "Standards", "Endpoints"]
---

# OIDC 1.0 endpoints

Your applications can use the following OpenID Connect (OIDC) endpoints:

| Endpoint                                   | Description                                                                                                                                                                                          | Advanced Identity Cloud is the |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| `/oauth2/userinfo`                         | Retrieve information about an authenticated end user ([UserInfo endpoint](https://openid.net/specs/openid-connect-core-1_0.html#UserInfo)); requires a valid token with at least the `openid` scope. | Provider                       |
| `/oauth2/idtokeninfo`                      | Validate an unencrypted ID token (Advanced Identity Cloud-specific endpoint).                                                                                                                        | Provider                       |
| `/oauth2/connect/checkSession`             | Retrieve OpenID Connect session information ([session management](https://docs.pingidentity.com/pingoneaic/latest/am-oidc1/session-management.html) endpoint).                                       | Provider                       |
| `/oauth2/connect/endSession`               | Terminate an OpenID Connect session ([session management](https://docs.pingidentity.com/pingoneaic/latest/am-oidc1/session-management.html) endpoint).                                               | Provider                       |
| `/oauth2/register`                         | Register, read, or delete a client profile ([dynamic client registration](https://docs.pingidentity.com/pingoneaic/latest/am-oidc/oauth2-dynamic-client-registration.html) endpoint)                 | Provider                       |
| `/.well-known/webfinger`                   | Let a client application discover the OpenID provider URL of an end user ([WebFinger discovery](https://openid.net/specs/openid-connect-discovery-1_0.html#IssuerDiscovery) endpoint).               | Provider                       |
| `/oauth2/.well-known/openid-configuration` | Let a relying party discover the OpenID provider configuration.                                                                                                                                      | Provider                       |
| `/oauth2/connect/jwk_uri`                  | Retrieve the OpenID provider's public keys to verify client-side token signatures or to encrypt OIDC JWTs in requests.                                                                               | Provider                       |
| `/oauth2/connect/rp/jwk_uri`               | Retrieve Advanced Identity Cloud client public keys for providers to encrypt ID tokens and verify signatures.                                                                                        | Relying party                  |

Many OAuth 2.0 endpoints also support OIDC. Find reference documentation in:

* [OAuth 2.0 client endpoints](../am-oauth2/oauth2-client-endpoints.html)

* [OAuth 2.0 administration endpoints](../am-oauth2/oauth2-admin-endpoints.html)