---
title: Configure Advanced Identity Cloud as an authorization server
description: Configure Advanced Identity Cloud as an OAuth 2.0 authorization server for client and admin endpoints
component: pingoneaic
page_id: pingoneaic:authorization:oauth2-provider
canonical_url: https://docs.pingidentity.com/pingoneaic/authorization/oauth2-provider.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "Endpoints", "Authorization", "Setup &amp; Configuration"]
page_aliases: ["oauth2-guide:oauth2-configure-authz.adoc", "am-oauth2:oauth2-configure-authz.adoc"]
section_ids:
  core-behavior-and-lifetimes: Core behavior and lifetimes
  grant-types: Grant types
  token-and-code-lifetimes: Token and code lifetimes
  persistence: Persistence
  scopes-and-consent-model: Scopes and consent model
  consent-behavior: Consent behavior
  token-storage: Token storage (client-side or server-side)
  oidc-specific-settings: OIDC-specific settings
  subject-type-and-hash-salt: Subject type and hash salt
  claims-mapping-and-scripts: Claims mapping and scripts
  dynamic-client-registration: Dynamic client registration (DCR)
  scripted-jwt-issuers: Scripted JWT issuers
---

# Configure Advanced Identity Cloud as an authorization server

The OAuth2 Provider configures Advanced Identity Cloud as an OAuth 2.0 authorization server for a realm. It exposes the [OAuth 2.0 endpoints](../am-oauth2/oauth2-client-endpoints.html) and [OAuth 2.0 administration endpoints](../am-oauth2/oauth2-admin-endpoints.html), providing a centralized, standards-compliant location to handle access tokens and authorization decisions for your applications and APIs.

Learn more about [how Advanced Identity Cloud works as an authorization server](../am-oauth2/am-as-authz-server.html).

The OAuth2 Provider is highly configurable, but if you're just getting started with your Advanced Identity Cloud tenant, most defaults are safe to use as-is. It follows a simple inheritance model:

* **Realm-wide defaults**: Client applications inherit baseline settings directly from the provider.

* **Shared overrides**: You can use client groups to share custom settings across multiple clients.

* **Client-specific overrides**: You can override settings on individual clients when specific parameters (such as token lifetimes, scripts, token storage, or consent behavior) must diverge from the provider default.

To configure the OAuth2 Provider:

1. In the Advanced Identity Cloud admin console, go to [icon: vpn_key, set=material, size=inline] Authorization > OAuth2 Provider.

2. Update the OAuth 2.0 settings as needed.

3. Click [icon: add, set=material, size=inline] Save.

Find a comprehensive list of configuration options in [OAuth 2.0 provider](../am-reference/services-configuration.html#realm-oauth-oidc). Consider the following key areas when configuring your settings.

## Core behavior and lifetimes

### Grant types

Go to [icon: vpn_key, set=material, size=inline] Authorization > OAuth2 Provider > Advanced to find these settings.

Select the Grant Types that client applications can use to request access, refresh, and ID tokens. Select only the grant types you plan to use, for example, Authorization Code, Refresh Token, Client Credentials, Token Exchange, and Device Code.

Find a list of supported grant types in [OAuth 2.0 grant flows](../am-oauth2/oauth2-implementing-flows.html) and [OpenID Connect grant flows](../am-oidc1/oidc-implementing-flows.html).

|   |                                                                                |
| - | ------------------------------------------------------------------------------ |
|   | UMA is listed but isn't supported in Advanced Identity Cloud. Don't select it. |

### Token and code lifetimes

Go to [icon: vpn_key, set=material, size=inline] Authorization > OAuth2 Provider > Core to find these settings.

* Authorization Code Lifetime (seconds)

  Keep the authorization code lifetime short (less than 10 minutes per [RFC 6749](https://www.rfc-editor.org/info/rfc6749/)). The default value is 2 minutes.

* Refresh Token Lifetime and Access Token Lifetime

  Set access and refresh token lifetimes to match your risk posture. The defaults are usually fine to start with, but assess these values with your security team.

* Issue Refresh Tokens

  If you plan to use refresh tokens, configure the provider to issue them and make sure your selected grant types support them.

  Learn why refresh tokens are useful in your environment, and how to request them in [Refresh tokens](../am-oauth2/oauth2-refresh-tokens.html).

### Persistence

Go to [icon: vpn_key, set=material, size=inline] Authorization > OAuth2 Provider > Advanced to find these settings.

*Persistence* lets you retain custom claims when you refresh an access token.

In the Persistent Claims field, enter the claims that must be persisted between tokens. When an access token is refreshed, any claims that are listed here will be on the new token.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * These claims are added before the access token modification script, allowing you to manipulate them in the modification script. For example, if a token has a claim called `hostname` that you want to be persisted when the token is refreshed, you could add that claim to the Persistent Claims list. You could then modify the script to persist that `hostname` in the new token, if it exists, or to add a hostname to the new token, if it doesn't exist.

* Only custom, non-standard claims can be persisted. Standard claims, such as `scope` (defined in the OAuth 2.0 specification) and `auditTrackingId` (defined by default in Advanced Identity Cloud) can't be persisted. |

## Scopes and consent model

Go to [icon: vpn_key, set=material, size=inline] Authorization > OAuth2 Provider > Advanced to find these settings.

* Client Registration Scope Allowlist

  If you plan to use [Dynamic client registration (DCR)](#dynamic-client-registration), enter the set of scopes allowed when clients register dynamically. This list also controls which scopes can appear in consent and discovery metadata.

* Default Client Scopes

  Decide which scopes should be default at the provider level. If a client application doesn't request any scope, the provider defaults apply. If no provider defaults are set, the client defaults are used.

### Consent behavior

Go to [icon: vpn_key, set=material, size=inline] Authorization > OAuth2 Provider > Consent to find these settings. The settings control whether:

* Your end users are asked for [consent](../am-oauth2/oauth2-manage-consent.html).

* Your end users can save consent so the OAuth 2.0 provider remembers their consented scopes.

* Client applications can skip consent so no consent page is displayed to resource owners.

* Client applications can revoke consent.

* Consent is handed off to a [Remote Consent Service](remote-consent-service.html).

## Token storage (client-side or server-side)

By default, Advanced Identity Cloud stores OAuth 2.0 tokens client-side. If you need server-side (CTS) storage (for operational, revocation, or audit reasons), go to [icon: vpn_key, set=material, size=inline] Authorization > OAuth2 Provider > Core and deselect Use Client-Side Access & Refresh Tokens.

If you don't have a strong requirement, leave the default client-side setting.

|   |                                                       |
| - | ----------------------------------------------------- |
|   | You can override this setting per client application. |

## OIDC-specific settings

You configure Advanced Identity Cloud as an OpenID Provider (OP) when you want it to be the central identity service that authenticates users and tells applications *who* the user is, not just whether they can get an access token.

If you're using Advanced Identity Cloud as an OpenID Provider:

### Subject type and hash salt

Go to [icon: vpn_key, set=material, size=inline] Authorization > OAuth2 Provider > Advanced to find these settings.

* Subject Types supported

  Ensure this setting includes `pairwise` (default).

  When a client application is configured to use `pairwise`, the OP (Advanced Identity Cloud) returns a different, opaque subject value per client instead of a single global value. This prevents different clients from easily correlating the same end user across applications, improving privacy.

  For a client application to use `pairwise`, its subject type must be included in this list. Otherwise, you'll see the error `Server does not support this client's subject type.`

* Subject Identifier Hash Salt

  By default, this field is set to `&{am.oidc.client.subject.identifier.hash.salt}`.

  If you're supporting `pairwise` subject types, you must change this value from the default to a tenant-specific value for privacy-preserving pairwise subject IDs. Because the hash salt is part of how pairwise `sub` values are computed, leaving it at the default effectively breaks the privacy guarantees of pairwise subjects.

### Claims mapping and scripts

Go to [icon: vpn_key, set=material, size=inline] Authorization > OAuth2 Provider > Advanced OpenID Connect to find these settings.

* Always Return Claims in ID Tokens

  This option is enabled by default and enables scope-derived claims in ID tokens. This is useful if your relying parties need user profile data immediately at sign-in, without extra calls to `/userinfo`.

  If you keep this option enabled, you must also configure how Advanced Identity Cloud maps scopes to claims and user profile attributes. Find more information in [Claims](../am-oidc1/understanding-openid-connect-scopes-and-claims.html) and [OIDC claims](../am-oauth2/plugins-user-info-claims.html).

## Dynamic client registration (DCR)

If you plan to onboard clients dynamically, configure the settings on the Client Dynamic Registration tab.

Decide on the following:

* If your client applications can register without an access token, set Allow Open Dynamic Client Registration.

  Allowing open dynamic client registration is a trade-off between ease of onboarding and control. The advantages are zero-bootstrap onboarding and a more open self-service ecosystem. The disadvantages are security exposure of the registration endpoint, need for extra protections, and weaker governance and auditability.

  In most production Advanced Identity Cloud deployments you keep open registration disabled and use access-token-protected DCR, reserving open registration for tightly controlled test or demo environments with strong rate limiting and monitoring.

* If you require a software statement JWT, set Require Software Statement for Dynamic Client Registration.

  * Enable this option if third-party or high-risk clients register or if you need strong provenance and policy-controlled metadata (for example, open banking and FAPI-style ecosystems).

  * Leave this option disabled for internal or low-risk environments where you already trust registrants and want simpler, faster self-service DCR without managing software statements.

  * If you enable this option, also set the Required Software Statement Attested Attributes to the list of claims that must be present in the software statement JWT.

Learn more in [Dynamic client registration](../am-oidc1/oauth2-dynamic-client-registration.html) (DCR).

## Scripted JWT issuers

Scripted JWT issuers let a script represent a trusted JWT issuer, so Advanced Identity Cloud can dynamically retrieve the issuer's details during the JWT profile for authorization grant.

Learn more in [Configure a scripted JWT issuer^](../am-oauth2/oauth2-jwt-bearer-grant.html#configure-scripted-jwt-issuer).

---

---
title: OAuth 2.0 provider settings
description: Configure the following settings on the Core tab:
component: pingoneaic
page_id: pingoneaic:authorization:oauth2-provider-settings
canonical_url: https://docs.pingidentity.com/pingoneaic/authorization/oauth2-provider-settings.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  realm-oauth-oidc-core: Core
  realm-oauth-oidc-advanced: Advanced
  realm-oauth-oidc-client-dynamic-registration: Client Dynamic Registration
  realm-oauth-oidc-openid-connect: OpenID Connect
  realm-oauth-oidc-advanced-openid-connect: Advanced OpenID Connect
  realm-oauth-oidc-device-flow: Device Flow
  realm-oauth-oidc-consent: Consent
  realm-oauth-oidc-ciba: CIBA
  realm-oauth-oidc-plugins: Plugins
  realm-oauth-oidc-ai-agents: AI Agents
  scripted_jwt_issuers: Scripted JWT Issuers
---

# OAuth 2.0 provider settings

|   |                                                                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Configure the OAuth 2.0 provider in the Advanced Identity Cloud admin console at Authorization > OAuth2 Provider. Learn more in [Configure Advanced Identity Cloud as an authorization server](oauth2-provider.html). |

## Core

Configure the following settings on the Core tab:

* Use Client-Side Access & Refresh Tokens

  When enabled, Advanced Identity Cloud issues access and refresh tokens that can be inspected by resource servers.

  You can override this setting for individual clients. To access client application settings, go to Native Consoles > Access Management > Realms > *Realm Name* > Applications > OAuth 2.0 > Clients > *Client ID*.

* Use Macaroon Access and Refresh Tokens

  When enabled, Advanced Identity Cloud issues access and refresh tokens as Macaroons with caveats.

* Authorization Code Lifetime (seconds)

  The time an authorization code is valid for, in seconds.

* Refresh Token Lifetime (seconds)

  The time in seconds a refresh token is valid for. If this field is set to `-1`, the refresh token will never expire.

  Default value: `604800`

* Access Token Lifetime (seconds)

  The time an access token is valid for, in seconds. Note that if you set the value to `0`, the access token won't be valid. A maximum lifetime of 600 seconds is recommended.

* Issue Refresh Tokens

  Whether to issue a refresh token when returning an access token.

  You can override this setting for individual clients. To access client application settings, go to Native Consoles > Access Management > Realms > *Realm Name* > Applications > OAuth 2.0 > Clients > *Client ID*.

* Issue Refresh Tokens on Refreshing Access Tokens

  Whether to issue a refresh token when refreshing an access token.

  You can override this setting for individual clients. To access client application settings, go to Native Consoles > Access Management > Realms > *Realm Name* > Applications > OAuth 2.0 > Clients > *Client ID*.

* Use Policy Engine for Scope decisions

  With this setting enabled, the policy engine is consulted for each scope value that's requested.

  Scope decisions are made in the following way when based on the policy engine:

  * If a policy returns a GRANT action of `true`, the scope is consented automatically and the user isn't consulted in a user-interaction flow.

  * If a policy returns a GRANT action of `false`, the scope isn't added to any resulting token and the user doesn't refer to it in a user-interaction flow.

  * If no policy returns a value for the GRANT action:

    * For user-facing grant types, such as the authorization or device code flows, the user is asked for consent or saved consent is used.

    * For grant types that are not user-facing, such as those using password or client credentials, the scope isn't added to any resulting token.

  You can override this setting for individual clients. To access client application settings, go to Native Consoles > Access Management > Realms > *Realm Name* > Applications > OAuth 2.0 > Clients > *Client ID*.

* Scopes Policy Set

  The policy set that defines the context in which policy evaluations occur when `Use Policy Engine for Scope decisions` is enabled on the OAuth 2.0 provider. Leave this field blank, or set it to `oauth2Scopes` to use the default policy set.

  You can override this setting for individual clients. To access client application settings, go to Native Consoles > Access Management > Realms > *Realm Name* > Applications > OAuth 2.0 > Clients > *Client ID*.

  Default value: `[Empty]`

* OAuth2 Access Token May Act Script

  The script that is executed when issuing an access token explicitly to modify the `may_act` claim placed on the token.

  To define the script, go to [icon: code, set=material, size=inline] Extensions > Scripts > + New Script > OAuth2 / OIDC > OAuth2 May Act.

  You can override this setting for individual clients. To access client application settings, go to Native Consoles > Access Management > Realms > *Realm Name* > Applications > OAuth 2.0 > Clients > *Client ID*.

* OIDC ID Token May Act Script

  The script that is executed when issuing an OIDC ID Token explicitly to modify the `may_act` claim placed on the token.

  To define the script, go to [icon: code, set=material, size=inline] Extensions > Scripts > + New Script > OAuth2 / OIDC > OAuth2 May Act in the Advanced Identity Cloud admin console.

  You can override this setting for individual clients. To access client application settings, go to Native Consoles > Access Management > Realms > *Realm Name* > Applications > OAuth 2.0 > Clients > *Client ID*.

## Advanced

Configure the following settings on the Advanced tab:

* Custom Login URL Template

  Custom URL for handling login, to override the default Advanced Identity Cloud login page.

  Supports Freemarker syntax, with the following variables:

  | Variable    | Description                                                                                                                    |
  | ----------- | ------------------------------------------------------------------------------------------------------------------------------ |
  | `gotoUrl`   | The URL to redirect to after login.                                                                                            |
  | `acrValues` | The Authentication Context Class Reference (acr) values for the authorization request.                                         |
  | `realm`     | The Advanced Identity Cloud realm the authorization request was made on.                                                       |
  | `service`   | The name of the authentication journey requested to perform resource owner authentication.                                     |
  | `locale`    | A space-separated list of locales, ordered by preference.                                                                      |
  | `ForceAuth` | Set to `true` when forced reauthentication is required. Use this variable to include `ForceAuth=true` in the custom login URL. |

  The following example template redirects users to a custom page to handle login. This page redirects to the `/oauth2/authorize` endpoint with any required parameters:

  `http://mylogin.com/login?goto=${goto}<#if acrValues??>&acr_values=${acrValues}</#if><#if realm??>&realm=${realm}</#if><#if service??>&service=${service}</#if><#if locale??>&locale=${locale}</#if>`

  |   |                                                                                                                                                               |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The default Advanced Identity Cloud login page is constructed using the [Base URL Source](../am-reference/services-configuration.html#realm-baseurl) service. |

  You can override this setting for individual clients. To access client application settings, go to Native Consoles > Access Management > Realms > *Realm Name* > Applications > OAuth 2.0 > Clients > *Client ID*.

* Persistent Claims

  Enter the claims that must be persisted between tokens. When an access token is refreshed, any claims that are listed here will be on the new token.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | * These claims are added before the access token modification script, allowing you to manipulate them in the modification script. For example, if a token has a claim called `hostname` that you want to be persisted when the token is refreshed, you could add that claim to the Persistent Claims list. You could then modify the script to persist that `hostname` in the new token, if it exists, or to add a hostname to the new token, if it doesn't exist.

  * Only custom, non-standard claims can be persisted. Standard claims, such as `scope` (defined in the OAuth 2.0 specification) and `auditTrackingId` (defined by default in Advanced Identity Cloud) can't be persisted. |

* Response Type Plugins

  Response type plugins support each OAuth 2.0/OIDC `response_type` on the `/oauth2/authorize` endpoint.

  For regular OAuth 2.0 and OIDC usage leaving the defaults is usually sufficient. You must add or verify additional plugins if you need specific behaviors, for example:

  * OIDC session management using `response_type=none` requires the `none|org.forgerock.oauth2.core.NoneResponseTypeHandler` plugin on the provider, and `none` in the client's Response Types.

  * To disallow certain flows. For example, remove `token` to forbid the [Implicit grant](../am-oauth2/oauth2-implicit-grant.html).

- Additional Audience Values

  The additional audience values that will be permitted when verifying Client Authentication JWTs.

  These audience values will be in addition to the AS base, issuer and endpoint URIs.

- Token Exchanger Plugins

  Token exchanger plugins control which token-type conversions are allowed when you use the [Token exchange](../am-oauth2/token-exchange.html) grant, and which Java handlers perform those conversions.

  If your tenant uses standard [RFC 8693](https://www.rfc-editor.org/info/rfc8693) token exchange (impersonation or delegation between access tokens and ID tokens), the defaults are usually sufficient.

- Token Validator Plugins

  Token validator plugins control which validation steps are run on `subject_token` and `actor_token` during [Token exchange](../am-oauth2/token-exchange.html).

  For almost all Advanced Identity Cloud deployments, the defaults are sufficient and should be left alone. Only change them if you have a very specific need to relax or replace some of those validations.

- User Profile Attribute(s) the Resource Owner is Authenticated On

  Names of profile attributes that resource owners use to log in. You can add others to the default, for example `mail`.

- User Display Name attribute

  The profile attribute that contains the name to be displayed for the user on the consent page.

* Client Registration Scope Allowlist

  The set of scopes allowed when registering clients dynamically, with translations.

  Scopes may be entered as simple strings or pipe-separated strings representing the internal scope name, locale, and localized description.

  For example: `read|en|Permission to view email messages in your account`

  Locale strings are in the format: `language_country_variant`, for example `en`, `en_GB`, or `en_US_WIN`.

  If the locale and pipe is omitted, the description is displayed to all users that have undefined locales.

  If the description is also omitted, nothing is displayed on the consent page for the scope. For example specifying `read|` would allow the scope read to be used by the client, but would not display it to the user on the consent page when requested.

* Subject Types supported

  List of subject types supported. Valid values are:

  * `public` - Each client receives the same subject (`sub`) value.

  * `pairwise` - Each client receives a different subject (`sub`) value, to prevent correlation between clients.

* Default Client Scopes

  List of scopes a client is granted if they request registration without specifying the scopes they want. Default scopes are NOT granted automatically to clients created through the UI.

- Enable Rich Authorization Requests with RCS

  If you've set **[Enable Remote Consent](#enable-remote-consent)** for the realm, this setting does the following:

  * Lets Advanced Identity Cloud process `authorization_details` from [RFC 9396: OAuth 2.0 Rich Authorization Requests](https://www.rfc-editor.org/rfc/rfc9396.html).

  * Advertises the `authorization_details_types_supported` metadata parameter in the well-known endpoint, populated from the consent service's [Metadata URL](../am-oauth2/oauth2-remote-consent.html#metadata-url).

  * Controls whether Advanced Identity Cloud processes the `authorization_details_types` parameter in dynamic client registration requests. Learn more in [Remote consent](../am-oauth2/oauth2-remote-consent.html) and [Register authorization detail types](../am-oidc1/oauth2-dynamic-client-registration.html#dynamic-registration-authorization-details-types).

  Default value: `false`

- OAuth2 Token Signing Algorithm

  Algorithm used to sign client-side OAuth 2.0 tokens in order to detect tampering.

  Advanced Identity Cloud supports the signing algorithms listed in JSON Web Algorithms (JWA): ["alg" (Algorithm) Header Parameter Values for JWS](https://www.rfc-editor.org/rfc/rfc7518.html#section-3.1):

  * `HS256` - HMAC with SHA-256.

  * `HS384` - HMAC with SHA-384.

  * `HS512` - HMAC with SHA-512.

  * `ES256` - ECDSA with SHA-256 and NIST standard P-256 elliptic curve.

  * `ES384` - ECDSA with SHA-384 and NIST standard P-384 elliptic curve.

  * `ES512` - ECDSA with SHA-512 and NIST standard P-521 elliptic curve.

  * `RS256` - RSASSA-PKCS-v1_5 using SHA-256.

  The possible values for this property are:

  * `HS256`

  * `HS384`

  * `HS512`

  * `RS256`

  * `RS384`

  * `RS512`

  * `ES256`

  * `ES384`

  * `ES512`

  * `PS256`

  * `PS384`

  * `PS512`

- Client-Side Token Compression

  Whether client-side access and refresh tokens should be compressed.

- Encrypt Client-Side Tokens

  Whether client-side access and refresh tokens should be encrypted.

  Enabling token encryption will disable token signing as encryption is performed using direct symmetric encryption.

  You can override this setting for individual clients. To access client application settings, go to Native Consoles > Access Management > Realms > *Realm Name* > Applications > OAuth 2.0 > Clients > *Client ID*.

- Subject Identifier Hash Salt

  If *pairwise* subject types are supported, it is *STRONGLY RECOMMENDED* to change this value. It is used in the salting of hashes for returning specific `sub` claims to individuals using the same `request_uri` or `sector_identifier_uri`.

  |   |                                                                                                                                                                                                                                                                                              |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If you map `am.services.oauth2.provider.hash.salt.secret` to a secret in a secret store, Advanced Identity Cloud ignores this value.Learn more about secret labels in [OAuth 2.0 and OpenID Connect provider secrets](../am-reference/secret-id-mappings.html#oauth2-default-secret-labels). |

- Code Verifier Parameter Required

  If enabled, requests using the authorization code grant or device flow require a `code_challenge` attribute to comply with the PKCE standard.

  For more information, read the [PKCE specification](https://www.rfc-editor.org/info/rfc7636).

  Note that if a client specifies a `code_challenge` parameter in the authorization request, PKCE is enabled regardless of the value of this attribute.

  The possible values for this property are:

  * `true`. All requests

  * `public`. Requests from all public clients

  * `passwordless`. Requests from all passwordless public clients

  * `false`. No requests

- Modified Timestamp Attribute Name

  The identity Data Store attribute used to return modified timestamp values.

  This attribute is paired together with the *Created Timestamp Attribute Name* attribute (`createdTimestampAttribute`). You can leave both attributes unset (default) or set them both. If you set only one attribute and leave the other blank, the access token fails with a 500 error.

  For example, when you configure Advanced Identity Cloud as an OIDC Provider in a Mobile Connect application, the client accesses the `userinfo` endpoint to obtain the `updated_at` claim value in the ID token. The `updated_at` claim gets its value from the `modifiedTimestampAttribute` attribute in the user profile. If the profile has never been modified, the `updated_at` claim uses the `createdTimestampAttribute` attribute.

- Created Timestamp Attribute Name

  The identity Data Store attribute used to return created timestamp values.

- Password Grant Authentication Service

  The journey used to authenticate the username and password for the [Resource owner password credentials grant](../am-oauth2/oauth2-ropc-grant.html).

  The list of possible values for this property reflects the list of configured authentication journeys.

  Don't change the default value (`Login`) unless you have configured a suitable replacement journey.

- Grant Types

  The set of Grant Types (OAuth 2.0 flows) this client can use.

  If you don't set any Grant Types here, the client can't use any OAuth 2.0 flows.

- Trusted TLS Client Certificate Header

  HTTP Header to receive TLS client certificates when TLS is terminated at a proxy.

  Leave blank if not terminating TLS at a proxy. Configure the proxy to strip this header from incoming requests. Best practice is to use a random string.

- TLS Client Certificate Chain Validation Enabled

  If enabled, validate the entire certificate chain from the header. If not enabled, validate only the leaf certificate.

- Trusted TLS Client Certificate Chain Header

  HTTP Header to receive TLS client certificate chains when TLS is terminated at a proxy.

Leave blank if not terminating TLS at a proxy. Ensure that the proxy is configured to strip this header from incoming requests. Best practice is to use a random string.

* TLS Client Certificate Header Format

  Format of the HTTP header used to communicate a client certificate from a reverse proxy.

  |   |                                                                         |
  | - | ----------------------------------------------------------------------- |
  |   | The default value (`BASE64_ENCODED_CERT`) is the only supported format. |

  For client authentication, Advanced Identity Cloud accepts only URL-encoded DER format certificates and infers the certificate type from the contents of the certificate. For example, a certificate that starts and ends with a `:` is inferred to be a DER format certificate.

* Support TLS Certificate-Bound Access Tokens

  Whether to bind access tokens to the client certificate when using TLS client certificate authentication.

* Check TLS Certificate Revocation Status

  Whether to check if TLS client certificates have been revoked.

  If enabled, Advanced Identity Cloud checks if TLS client certificates used for client authentication have been revoked using either OCSP (preferred) or CRL.

  Advanced Identity Cloud implements "soft fail" semantics. If the revocation status can't be established due to a temporary error, such as a network error, the certificate is assumed to be valid.

* OCSP Responder URI

  URI of the OCSP responder service to use for checking certificate revocation status.

  If specified this value overrides any OCSP or CRL mechanisms specified in individual certificates.

* OCSP Responder Certificate

  Base64-encoded X.509 certificate, in PEM or DER format, used to verify OCSP responses.

  If specified, Advanced Identity Cloud uses this certificate to verify the signature on all OCSP responses. If this field is empty, the appropriate certificate is determined from the trusted CA certificates.

* Macaroon Token Format

  The format to use when serializing and parsing Macaroons. V1 is bulky and should only be used when compatibility with older Macaroon libraries is required.

  The possible values for this property are:

  * `V1`

  * `V2`

* Require exp claim in Request Object

  If enabled, the `exp` claim must be included in JWT request objects specified at [/oauth2/authorize](../am-oauth2/oauth2-authorize-endpoint.html) or [/oauth2/par](../am-oauth2/oauth2-par-endpoint.html).

  The `exp` (expiration time) claim defines the lifetime of the JWT, after which the JWT is no longer valid.

  To comply with the [FAPI](https://openid.net/specs/openid-financial-api-part-2-1_0-final.html#authorization-server) security profile, this setting must be enabled.

  Default value: `false`

* Require nbf claim in Request Object

  If enabled, the `nbf` claim must be included in JWT request objects specified at [/oauth2/authorize](../am-oauth2/oauth2-authorize-endpoint.html) or [/oauth2/par](../am-oauth2/oauth2-par-endpoint.html).

  The `nbf` (not before) claim defines the earliest time that the JWT can be accepted for processing.

  To comply with the [FAPI](https://openid.net/specs/openid-financial-api-part-2-1_0-final.html#authorization-server) security profile, this setting must be enabled.

  Default value: `false`

* Max nbf and exp difference

  The maximum permitted difference, in minutes, between the `nbf` and `exp` claims, as defined in the request object JWT.

  A value of 0 indicates that there is no maximum time requirement.

  If set to a value greater than 0, and either `nbf` or `exp` isn't defined, the JWT is validated successfully, providing the claims are not required.

  If set to a value greater than 0, and both claims are present, the JWT is validated accordingly, even when not required.

  To comply with the [FAPI](https://openid.net/specs/openid-financial-api-part-2-1_0-final.html#authorization-server) security profile, this setting must be 60 (minutes) or less.

  Default value: `0`

* Max nbf age

  The maximum permitted age, in minutes, of the `nbf` claim.

  A value of 0 indicates that there is no maximum time requirement.

  If set to a value greater than 0, and `nbf` is neither required nor specified, the JWT is validated successfully.

  If set to a value greater than 0, and `nbf` is present, the JWT is validated accordingly, even when not required.

  To comply with the [FAPI](https://openid.net/specs/openid-financial-api-part-2-1_0-final.html#authorization-server) security profile, this setting must be 60 (minutes) or less.

  Default value: `0`

- Request Object Processing Specification

  This setting determines which specification Advanced Identity Cloud uses to validate request object JWTs, provided in the `request` or `request_uri` parameters:

  * `OIDC`: Advanced Identity Cloud uses the [OIDC specification](https://openid.net/specs/openid-connect-core-1_0.html) for JWT processing

  * `JAR`: Advanced Identity Cloud uses the [JAR specification](https://www.rfc-editor.org/rfc/rfc9101.html) for JWT processing

  For example, the following OIDC request specifies a request object JWT. It could be validated according to the JAR specification *or* as a standard OIDC request:

  `/authorize?client_id=myClient&request={JWT with scope=openid, response_type=id_token}`

  This table summarizes how Advanced Identity Cloud validates the request object JWT, depending on the specification:

  **Specification Rules**

  |                                      | OIDC specification                                                                                                                                                                                                                                     | JAR specification                                                                                                                          |
  | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
  | **Request object**                   | *May* be unsigned.                                                                                                                                                                                                                                     | *Must* be [signed](https://www.rfc-editor.org/rfc/rfc7515.html) and, optionally, [encrypted](https://www.rfc-editor.org/rfc/rfc7516.html). |
  | **Authorization request parameters** | Advanced Identity Cloud assembles parameters from the request object *and* the query parameters.If the same parameter exists in the request object and in the authorization request, Advanced Identity Cloud uses the parameter in the request object. | Advanced Identity Cloud assembles parameters from the request object ONLY and ignores duplicates defined as query parameters.              |
  | **Required request parameters**      | * `client_id`

  * `response_type`

  * `scope`, including `openid` scope value The `response_type` and `scope` must be specified outside the request object.                                                                                              | - `client_id`

  - `request` OR `request_uri`                                                                                                |

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | * By default, Advanced Identity Cloud consults this field *only* if it can't determine the rules to apply based on the incoming request. To override this behavior and ***force*** Advanced Identity Cloud to use the specification selected here, regardless of the request object contents, create an [ESV](../tenants/esvs-manage-ui.html) as follows:

    * Name: `esv-oauth2-provider-request-object-processing-enforced`

    * Type: `bool`

    * Value: `true`

  * If you set `esv-oauth2-provider-request-object-processing-enforced` to `true`, Advanced Identity Cloud uses the specification selected here to process all JWT requests, regardless of whether the requests are OIDC. |

  Find more information on JWT validation rules in the [`request`](../am-oauth2/oauth2-parameters.html#the-request-parameter) parameter.

  Default value: `OIDC`

* PAR Request URI Lifetime (seconds)

  The length of time that the PAR Request URI is valid, in seconds.

  It is strongly recommended to set this value to a short interval; for example, between 5 and 150 seconds. Setting this attribute to a higher value increases the load on the CTS, and may even result in denial of service if the requests are large and consume the available storage capacity.

  Learn more in [Authorization code grant with PAR](../am-oauth2/oauth2-authz-grant-par.html).

  Default value: `90`

- Require Pushed Authorization Requests

  If enabled, clients must use the PAR endpoint to initiate authorization requests, otherwise Advanced Identity Cloud returns an error indicating a missing or invalid request object.

  This applies to *all* clients, including clients that aren't configured to require PAR.

  You can also set this independently for individual clients under Native Consoles > Access Management. Go to Realms > *Realm Name* > Applications > OAuth 2.0 > Clients > *Client ID*.

  Default value: `false`

* Refresh Token Grace Period (seconds)

  The time, in seconds, that a refresh token can be reused. This grace period lets OAuth 2.0 clients recover seamlessly if the response from an original refresh token request isn't received because of a network problem or other transient issue. During the grace period, the refresh token can be reused multiple times, if the network problem persists. When the grace period ends, the refresh token is revoked.

  The refresh token grace period applies only to tokens in a one-to-one storage scheme.

  |   |                                                                                                                                    |
  | - | ---------------------------------------------------------------------------------------------------------------------------------- |
  |   | A long grace period poses a security risk, so keep the grace period as small as possible. The maximum grace period is 120 seconds. |

  The default value is `0`, which results is no grace period.

  You can override this setting for individual clients. To access client application settings, go to Native Consoles > Access Management > Realms > *Realm Name* > Applications > OAuth 2.0 > Clients > *Client ID*.

- Allow Client Credentials in Token Endpoint Query Parameters

  When this setting is `true`, you can include client credentials in token endpoint requests as query parameters.

  Previously, you could supply client credentials (the `client_id` and `client_secret`) as query parameters in POST requests to the `/oauth2/access_token` endpoint. This is now prohibited by default and you must include the credentials within the POST request body.

  The Allow Client Credentials in Token Endpoint Query Parameters setting controls this behavior. For security reasons, ForgeRock recommends you keep this property disabled to prevent client credentials from being included as query parameters.

  If you set this property to `true` to support existing scripts and clients, you should update your scripts and clients as soon as possible then set the property back to `false`.

  Default value: `false`

* Include subname claim in tokens issued by the OAuth2 Provider

  When this setting is `true`, Advanced Identity Cloud adds the `subname` claim to access tokens and ID tokens by default.

  The value of the `subname` claim is the name of the token's subject, for example, `bjensen`, or `myOAuth2Client`.

  Default value: `true`

- Include Client ID Claim In Stateless Access & Refresh Tokens

  When this setting is enabled, Advanced Identity Cloud includes the `client_id` claim in new stateless access and refresh tokens and reads it from existing tokens if present.

  Default value: `true`

* Enable Application Context

  When enabled, this setting makes the application context available in all OAuth 2.0 / OIDC flows through the `oauthApplication` binding in [Scripted Decision node scripts](../am-scripting/scripting-api-node.html#oauthapp-binding).

  To override this setting at the client level, under Native Consoles > Access Management, go to Realms > *realm* > Applications > OAuth 2.0 > Clients > *client* > OAuth2 Provider Overrides and update Enable Application Context.

- Accept Audience Parameters in Token Exchange Requests

  If this setting is `false` (default), Advanced Identity Cloud ignores audience parameter values in token exchange requests.

  If this setting is `true`, Advanced Identity Cloud validates audience parameter values in token exchange requests against the values defined in Allowed Resource Server Audience Values on the client.

  If validation fails, the token exchange request is rejected.

  Find more information in [The `aud` claim](../am-oauth2/token-exchange.html#aud-claim).

* Use token_introspection claim for JWT

  Specifies whether Advanced Identity Cloud wraps the introspected token's claims inside a `token_introspection` claim in the JWT introspection response, as required by RFC 9701.

  If enabled, Advanced Identity Cloud separates the JWT's own top-level claims (`iss`, `aud`, `iat`) from the introspected token's claims, which appear inside `token_introspection`. The `aud` claim of the introspected token is always included in the JWT response, including for client-side tokens. The JSON introspection response also includes the `aud` claim of the introspected token, if present.

  If not enabled, Advanced Identity Cloud returns a flat JWT structure. For client-side tokens, the `aud` claim is omitted from both the JWT response and the JSON response.

  Learn more in [RFC 9701 token_introspection claim](../am-oauth2/oauth2-introspect-endpoint.html#rfc-9701-token-introspection-claim).

  Default: Not enabled

- Allow audience members to introspect tokens

  If enabled, any client whose `client_id` appears anywhere in a token's `aud` (audience) claim can introspect that token, including clients that aren't the issuing client.

  Enable this setting if tokens can have multiple `aud` values, or if you use token exchange with the `audience` request parameter. Resource servers listed in the `aud` claim can then validate tokens presented to them.

  If not enabled, only the issuing client can introspect a token (unless the client has a [special introspection scope](../am-oauth2/oauth2-scopes.html#special-oauth2-scopes)).

  Default: Not enabled

## Client Dynamic Registration

Configure the following settings on the Client Dynamic Registration tab:

* Require Software Statement for Dynamic Client Registration

  When enabled, a software statement JWT containing at least the `iss` (issuer) claim must be provided when registering an OAuth 2.0 client dynamically.

* Required Software Statement Attested Attributes

  The client attributes that must be present in the software statement JWT when registering an OAuth 2.0 client dynamically. Applies only if you enable Require Software Statements for Dynamic Client Registration.

  Leave blank to allow any attributes to be present.

- Store Software Statement in OAuth2 Client

  When enabled, Advanced Identity Cloud stores the software statement JWT provided in dynamic registration create and update requests on the client. Advanced Identity Cloud returns the stored JWT in client profile read responses.

  Enabling this option can significantly increase the memory footprint of dynamically registered clients because software statement JWTs can be large.

  Existing clients must send an update request that includes their software statement JWT before Advanced Identity Cloud stores their software statements.

  Default value: `false`

- Allow Open Dynamic Client Registration

  Allow clients to register without an access token. If enabled, consider adding some form of rate limiting. Learn more in [Client Registration](https://openid.net/specs/openid-connect-registration-1_0.html#ClientRegistration) in the OIDC specification.

- Generate Registration Access Tokens

  Whether to generate Registration Access Tokens for clients that register by using open dynamic client registration. Such tokens let the client access the [Client Configuration Endpoint](https://openid.net/specs/openid-connect-registration-1_0.html#ClientConfigurationEndpoint) as per the OpenID Connect specification. This setting has no effect if Allow Open Dynamic Client Registration is disabled.

- Scope to give access to dynamic client registration

  Mandatory scope required when registering a new OAuth2 client.

- Dynamic Client Registration Script

  Provide a script to customize dynamic client registration after a successful create, update, or delete operation.

## OpenID Connect

Configure the following settings on the OpenID Connect tab:

* Overrideable Id_Token Claims

  List of claims in the ID token that can be overridden in the OIDC claims script. These should be the subset of the core OIDC claims, such as `aud` or `azp`.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | * Find information about the core OIDC claims in the [ID Token data structure](https://openid.net/specs/openid-connect-core-1_0.html#IDToken).

  * Find details of the OIDC script and how to implement a custom scripted plugin in [OIDC claims](../am-oauth2/plugins-user-info-claims.html).

    To override claims, follow the steps described in [Override the audience and issuer claims](../am-oauth2/plugins-user-info-claims.html#example-override-issuer-audience). |

  You can override this setting for individual clients. To access client application settings, go to Native Consoles > Access Management > Realms > *Realm Name* > Applications > OAuth 2.0 > Clients > *Client ID*.

* ID Token Signing Algorithms supported

  Algorithms supported to sign OIDC `id_tokens`.

  Advanced Identity Cloud supports signing algorithms listed in JSON Web Algorithms (JWA): ["alg" (Algorithm) Header Parameter Values for JWS](https://www.rfc-editor.org/rfc/rfc7518.html#section-3.1):

  * `HS256` - HMAC with SHA-256.

  * `HS384` - HMAC with SHA-384.

  * `HS512` - HMAC with SHA-512.

  * `ES256` - ECDSA with SHA-256 and NIST standard P-256 elliptic curve.

  * `ES384` - ECDSA with SHA-384 and NIST standard P-384 elliptic curve.

  * `ES512` - ECDSA with SHA-512 and NIST standard P-521 elliptic curve.

  * `RS256` - RSASSA-PKCS-v1_5 using SHA-256.

  * `RS384` - RSASSA-PKCS-v1_5 using SHA-384.

  * `RS512` - RSASSA-PKCS-v1_5 using SHA-512.

  * `PS256` - RSASSA-PSS using SHA-256.

  * `PS384` - RSASSA-PSS using SHA-384.

  * `PS512` - RSASSA-PSS using SHA-512.

* ID Token Encryption Algorithms supported

  Encryption algorithms supported to encrypt OIDC ID tokens to hide their contents.

  Advanced Identity Cloud supports the following ID token encryption algorithms:

  * `RSA-OAEP` - RSA with Optimal Asymmetric Encryption Padding (OAEP) with SHA-1 and MGF-1.

  * `RSA-OAEP-256` - RSA with OAEP with SHA-256 and MGF-1.

  * `A128KW` - AES Key Wrapping with 128-bit key derived from the client secret.

  * `RSA1_5` - RSA with PKCS#1 v1.5 padding.

  * `A256KW` - AES Key Wrapping with 256-bit key derived from the client secret.

  * `dir` - Direct encryption with AES using the hashed client secret.

  * `A192KW` - AES Key Wrapping with 192-bit key derived from the client secret.

* ID Token Encryption Methods supported

  Encryption methods supported to encrypt OpenID Connect ID tokens in order to hide its contents.

  Advanced Identity Cloud supports the following ID token encryption algorithms:

  * `A128GCM`, `A192GCM`, and `A256GCM` - AES in Galois Counter Mode (GCM) authenticated encryption mode.

  * `A128CBC-HS256`, `A192CBC-HS384`, and `A256CBC-HS512` - AES encryption in CBC mode, with HMAC-SHA-2 for integrity.

- Supported Claims

  Set of claims supported by the OIDC `/oauth2/userinfo` endpoint, with translations.

  You can enter claims as simple strings or pipe-separated strings representing the internal claim name, locale, and localized description.

  For example: `name|en|Your full name`.

  Locale strings are in the format: `language + "" + country + "" + variant`, for example `en`, `en_GB`, or `en_US_WIN`. If the locale and pipe is omitted, the description is displayed to all users that have undefined locales.

  If the description is also omitted, nothing is displayed on the consent page for the claim. For example specifying `family_name|` would allow the claim `family_name` to be used by the client, but would not display it to the user on the consent page when requested.

- OpenID Connect JWT Token Lifetime (seconds)

  The amount of time the JWT will be valid for, in seconds.

- OIDC Provider Discovery

  Unset to remove access to the OIDC Discovery endpoint:

  ```none
  https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/realm/.well-known/openid-configuration
  ```

## Advanced OpenID Connect

Configure the following settings on the Advanced OpenID Connect tab:

* Remote JSON Web Key URL

  The Remote URL where the provider's JSON Web Key can be retrieved.

  If this setting isn't configured, Advanced Identity Cloud provides a local URL to access the public key of the private key used to sign ID tokens.

* JWT Signing kid Header Mappings

  Map custom `kid` header values for JWTs signed with the signing key to the specified secret alias.

  * Key is the secret alias of the key used to sign the given JWT.

  * Value is the custom `kid` value.

  Advanced Identity Cloud only applies custom `kid` mappings if you set a value for Remote JSON Web Key URL. Use these mappings to guarantee that the `kid` header of a signed JWT references the correct key in a remote JWKS.

  If you don't configure a custom `kid` for a JWT signing key, Advanced Identity Cloud generates a default `kid` value.

  Find more information in [Map custom key IDs to secrets](../am-oidc1/managing-jwk_uri.html#map-custom-kids).

* Idtokeninfo Endpoint Requires Client Authentication

  When enabled, the `/oauth2/idtokeninfo` endpoint requires client authentication if the signing algorithm is set to `HS256`, `HS384`, or `HS512`.

* Enable "claims_parameter_supported"

  If enabled, clients will be able to request individual claims using the `claims` request parameter, as per [section 5.5 of the OpenID Connect specification](http://openid.net/specs/openid-connect-core-1_0.html#ClaimsParameter).

* OpenID Connect acr_values to Auth Mapping

  Maps OIDC ACR values to authentication journeys. Find more information in [acr_values parameter](http://openid.net/specs/openid-connect-core-1_0.html#AuthRequest) in the OIDC authentication request specification.

  |   |                                                                                                                                                                       |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Don't configure more than one ACR mapping to the same authentication journey. Doing so can result in misrepresentation of the ACR information in the issued ID token. |

* Default ACR values

  Default requested Authentication Context Class Reference values.

  List of strings that specifies the default acr values that the OP is being requested to use for processing requests from this Client, with the values appearing in order of preference. The Authentication Context Class satisfied by the authentication performed is returned as the acr Claim Value in the issued ID Token. The acr Claim is requested as a Voluntary Claim by this parameter. The acr_values_supported discovery element contains a list of the acr values supported by this server. Values specified in the acr_values request parameter or an individual acr Claim request override these default values.

* Always Return Claims in ID Tokens

  If enabled, include scope-derived claims in the `id_token`, even if an access token is also returned that could provide access to get the claims from the `userinfo` endpoint.

  If not enabled, if an access token is requested the client must use it to access the `userinfo` endpoint for scope-derived claims, as they will not be included in the ID token.

* Enable Session Management

  If this is disabled, OIDC session management related-endpoints are disabled. When enabled Advanced Identity Cloud stores *ops* tokens corresponding to OIDC sessions in the CTS store and an OIDC session ID in the session.

* Request Parameter Signing Algorithms Supported

  Algorithms supported to verify signature of Request parameter. Advanced Identity Cloud supports signing algorithms listed in JSON Web Algorithms (JWA): ["alg" (Algorithm) Header Parameter Values for JWS](https://www.rfc-editor.org/rfc/rfc7518.html#section-3.1):

  * `HS256` - HMAC with SHA-256.

  * `HS384` - HMAC with SHA-384.

  * `HS512` - HMAC with SHA-512.

  * `ES256` - ECDSA with SHA-256 and NIST standard P-256 elliptic curve.

  * `ES384` - ECDSA with SHA-384 and NIST standard P-384 elliptic curve.

  * `ES512` - ECDSA with SHA-512 and NIST standard P-521 elliptic curve.

  * `RS256` - RSASSA-PKCS-v1_5 using SHA-256.

* Request Parameter Encryption Algorithms Supported

  Encryption algorithms supported to decrypt Request parameter.

  Advanced Identity Cloud supports the following ID token encryption algorithms:

  * `RSA-OAEP` - RSA with Optimal Asymmetric Encryption Padding (OAEP) with SHA-1 and MGF-1.

  * `RSA-OAEP-256` - RSA with OAEP with SHA-256 and MGF-1.

  * `A128KW` - AES Key Wrapping with 128-bit key derived from the client secret.

  * `RSA1_5` - RSA with PKCS#1 v1.5 padding.

  * `A256KW` - AES Key Wrapping with 256-bit key derived from the client secret.

  * `dir` - Direct encryption with AES using the hashed client secret.

  * `A192KW` - AES Key Wrapping with 192-bit key derived from the client secret.

* Request Parameter Encryption Methods Supported

  Encryption methods supported to decrypt Request parameter.

  Advanced Identity Cloud supports the following Request parameter encryption algorithms:

  * `A128GCM`, `A192GCM`, and `A256GCM` - AES in Galois Counter Mode (GCM) authenticated encryption mode.

  * `A128CBC-HS256`, `A192CBC-HS384`, and `A256CBC-HS512` - AES encryption in CBC mode, with HMAC-SHA-2 for integrity.

* Supported Token Endpoint JWS Signing Algorithms.

  Supported JWS Signing Algorithms for 'private_key_jwt' JWT based authentication method.

* Authorized OIDC SSO Clients

  Clients authorized to use OpenID Connect ID tokens as SSO Tokens.

  Allows clients to act with the full authority of the user. Grant this permission only to trusted clients.

* UserInfo Signing Algorithms Supported

  Algorithms supported to verify signature of the UserInfo endpoint. Advanced Identity Cloud supports the signing algorithms listed in JSON Web Algorithms (JWA): ["alg" (Algorithm) Header Parameter Values for JWS](https://www.rfc-editor.org/rfc/rfc7518.html#section-3.1):

  * `HS256` - HMAC with SHA-256.

  * `HS384` - HMAC with SHA-384.

  * `HS512` - HMAC with SHA-512.

  * `ES256` - ECDSA with SHA-256 and NIST standard P-256 elliptic curve.

  * `ES384` - ECDSA with SHA-384 and NIST standard P-384 elliptic curve.

  * `ES512` - ECDSA with SHA-512 and NIST standard P-521 elliptic curve.

  * `RS256` - RSASSA-PKCS-v1_5 using SHA-256.

* UserInfo Encryption Algorithms Supported

  Encryption algorithms supported by the UserInfo endpoint.

  Advanced Identity Cloud supports the following UserInfo endpoint encryption algorithms:

  * `RSA-OAEP` - RSA with Optimal Asymmetric Encryption Padding (OAEP) with SHA-1 and MGF-1.

  * `RSA-OAEP-256` - RSA with OAEP with SHA-256 and MGF-1.

  * `A128KW` - AES Key Wrapping with 128-bit key derived from the client secret.

  * `RSA1_5` - RSA with PKCS#1 v1.5 padding.

  * `A256KW` - AES Key Wrapping with 256-bit key derived from the client secret.

  * `dir` - Direct encryption with AES using the hashed client secret.

  * `A192KW` - AES Key Wrapping with 192-bit key derived from the client secret.

* UserInfo Encryption Methods Supported

  Encryption methods supported by the UserInfo endpoint.

  Advanced Identity Cloud supports the following UserInfo endpoint encryption methods:

  * `A128GCM`, `A192GCM`, and `A256GCM` - AES in Galois Counter Mode (GCM) authenticated encryption mode.

  * `A128CBC-HS256`, `A192CBC-HS384`, and `A256CBC-HS512` - AES encryption in CBC mode, with HMAC-SHA-2 for integrity.

* Token Introspection Response Signing Algorithms Supported

  Algorithms that are supported for signing the Token Introspection endpoint JWT response.

  Advanced Identity Cloud supports the signing algorithms listed in JSON Web Algorithms (JWA): ["alg" (Algorithm) Header Parameter Values for JWS](https://www.rfc-editor.org/rfc/rfc7518.html#section-3.1):

  * `HS256` - HMAC with SHA-256.

  * `HS384` - HMAC with SHA-384.

  * `HS512` - HMAC with SHA-512.

  * `ES256` - ECDSA with SHA-256 and NIST standard P-256 elliptic curve.

  * `ES384` - ECDSA with SHA-384 and NIST standard P-384 elliptic curve.

  * `ES512` - ECDSA with SHA-512 and NIST standard P-521 elliptic curve.

  * `RS256` - RSASSA-PKCS-v1_5 using SHA-256.

  * `RS384` - RSASSA-PKCS-v1_5 using SHA-384.

  * `RS512` - RSASSA-PKCS-v1_5 using SHA-512.

  * `EdDSA` - EdDSA with SHA-512.

* Token Introspection Response Encryption Algorithms Supported

  Encryption algorithms supported by the Token Introspection endpoint JWT response.

  Advanced Identity Cloud supports the following UserInfo endpoint encryption algorithms:

  * `RSA-OAEP` - RSA with Optimal Asymmetric Encryption Padding (OAEP) with SHA-1 and MGF-1.

  * `RSA-OAEP-256` - RSA with OAEP with SHA-256 and MGF-1.

  * `A128KW` - AES Key Wrapping with 128-bit key derived from the client secret.

  * `RSA1_5` - RSA with PKCS#1 v1.5 padding.

  * `A256KW` - AES Key Wrapping with 256-bit key derived from the client secret.

  * `dir` - Direct encryption with AES using the hashed client secret.

  * `A192KW` - AES Key Wrapping with 192-bit key derived from the client secret.

* Token Introspection Response Encryption Methods Supported

  Encryption methods supported by the Token Introspection endpoint JWT response.

  Advanced Identity Cloud supports the following encryption methods:

  * `A128GCM`, `A192GCM`, and `A256GCM` - AES in Galois Counter Mode (GCM) authenticated encryption mode.

  * `A128CBC-HS256`, `A192CBC-HS384`, and `A256CBC-HS512` - AES encryption in CBC mode, with HMAC-SHA-2 for integrity.

- Authorization Response Signing Algorithms Supported

  Algorithms supported for signing the [/oauth2/authorize](../am-oauth2/oauth2-authorize-endpoint.html) endpoint JWT response.

  Advanced Identity Cloud supports the signing algorithms listed in JSON Web Algorithms (JWA): ["alg" (Algorithm) Header Parameter Values for JWS](https://www.rfc-editor.org/rfc/rfc7518.html#section-3.1):

  * `HS256` - HMAC with SHA-256

  * `HS384` - HMAC with SHA-384

  * `HS512` - HMAC with SHA-512

  * `RS256` - RSASSA-PKCS-v1_5 using SHA-256

  * `RS384` - RSASSA-PKCS1-v1_5 using SHA-384

  * `RS512` - RSASSA-PKCS1-v1_5 using SHA-512

  * `ES256` - ECDSA with SHA-256 and NIST standard P-256 elliptic curve

  * `ES384` - ECDSA with SHA-384 and NIST standard P-384 elliptic curve

  * `ES512` - ECDSA with SHA-512 and NIST standard P-521 elliptic curve

  * `PS256` - RSASSA-PSS using SHA-256 and MGF1 with SHA-256

  * `PS384` - RSASSA-PSS using SHA-384 and MGF1 with SHA-384

  * `PS512` - RSASSA-PSS using SHA-512 and MGF1 with SHA-512

  Default value:

  ```
  PS384
  ES384
  RS384
  HS256
  HS512
  ES256
  RS256
  HS384
  ES512
  PS256
  PS512
  RS512
  ```

* Authorization Response Encryption Algorithms Supported

  Algorithms supported for encrypting the [/oauth2/authorize](../am-oauth2/oauth2-authorize-endpoint.html) JWT response.

  Advanced Identity Cloud supports the following Token Introspection endpoint encryption algorithms:

  * `RSA1_5` - RSA with PKCS#1 v1.5 padding.

  * `RSA-OAEP` - RSA with Optimal Asymmetric Encryption Padding (OAEP) with SHA-1 and MGF-1.

  * `RSA-OAEP-256` - RSA with OAEP with SHA-256 and MGF-1.

  * `A128KW` - AES Key Wrapping with 128-bit key derived from the client secret.

  * `A192KW` - AES Key Wrapping with 192-bit key derived from the client secret.

  * `A256KW` - AES Key Wrapping with 256-bit key derived from the client secret.

  * `dir` - Direct encryption with AES using the hashed client secret.

  * `ECDH-ES` - Elliptic Curve Diffie-Hellman Ephemeral Static key agreement using Concat KDF.

  * `ECDH-ES+A128KW` - ECDH-ES using Concat KDF and CEK wrapped with `A128KW`.

  * `ECDH-ES+A192KW` - ECDH-ES using Concat KDF and CEK wrapped with `A192KW`.

  * `ECDH-ES+A256KW` - ECDH-ES using Concat KDF and CEK wrapped with `A256KW`.

  Default value:

  ```
  ECDH-ES+A256KW
  ECDH-ES+A192KW
  RSA-OAEP
  ECDH-ES+A128KW
  RSA-OAEP-256
  A128KW
  A256KW
  ECDH-ES
  dir
  A192KW
  ```

- Authorization Response Encryption Methods Supported

  Methods supported for encrypting the [/oauth2/authorize](../am-oauth2/oauth2-authorize-endpoint.html) JWT response.

  Advanced Identity Cloud supports the following encryption methods:

  * `A128GCM`, `A192GCM`, and `A256GCM` - AES in Galois Counter Mode (GCM) authenticated encryption mode.

  * `A128CBC-HS256`, `A192CBC-HS384`, and `A256CBC-HS512` - AES encryption in CBC mode, with HMAC-SHA-2 for integrity.

  Default value:

  ```
  A256GCM
  A192GCM
  A128GCM
  A128CBC-HS256
  A192CBC-HS384
  A256CBC-HS512
  ```

- Include all kty and alg combinations in jwks_uri

  By default, only distinct `kid` entries are returned in the `jwks_uri`. The `alg` property isn't included. Enabling this flag results in duplicate `kid` entries, each one specifying a different `kty` and `alg` combination. Find more information in [RFC 7517 - "kid" (Key ID) Parameter](https://www.rfc-editor.org/rfc/rfc7517.html#section-4.5).

* Use Force Authentication for prompt=login

  If you specify the `prompt=login` parameter in the URL, Advanced Identity Cloud forces the end user to authenticate even if they already have a valid session. Set the Use Force Authentication for prompt=login property to control how the end user's existing session is handled after reauthentication.

  If you set this property to `false` (the default), Advanced Identity Cloud destroys the existing session and creates a new session on reauthentication.

  If you set this property to `true`, Advanced Identity Cloud performs a [session upgrade](../am-sessions/session-upgrade.html) on reauthentication.

* Use Force Authentication for max_age

  This property applies only to reauthentication triggered by the Default Max Age property of an OAuth 2.0 client.

  If the age of an end user's session reaches the value set in the Default Max Age property of the client, Advanced Identity Cloud forces the end user to reauthenticate. Set the Use Force Authentication for max_age property to control how the end user's existing session is handled after reauthentication.

  If this property is `false` (the default) and the user requests authorization after the `max_age` has passed, Advanced Identity Cloud destroys the existing session and creates a new session after reauthentication.

  If this property is `true` and the user requests authorization after the `max_age` has passed, Advanced Identity Cloud performs a [session upgrade](../am-sessions/session-upgrade.html) on reauthentication.

* Minimum max_age for Authorize Requests

  The minimum `max_age` value that's permitted in an authorization request, in seconds.

  If this property is set too low, it can cause repeated authentication requests if the OIDC flow takes longer to complete than the specified `max_age`.

  Default value: `60`

## Device Flow

Configure the following settings on the Device Flow tab:

* Verification URL

  The URL that the user will be instructed to visit to complete their OAuth 2.0 login and consent when using the device code flow.

* Device Completion URL

  The URL that the user will be sent to on completion of their OAuth 2.0 login and consent when using the device code flow.

* Device Code Lifetime (seconds)

  The lifetime of the device code, in seconds.

  Default value: `300`

* Device Polling Interval

  The polling frequency, in seconds, for devices waiting for tokens when using the device code flow.

  Default value: `5`

* User Code Character Length

  The number of characters in the generated user code.

  Default value: `8`

* User Code Character Set

  The set of characters to be used to generate a user code.

  Consider the limitations of low resolution mobile devices when defining a character set. For example, the OAuth 2.0 Device Grant specification recommends removing characters that can be easily confused, such as "0" and "O" or "1", "l" and "I". Find more examples in [RFC 8628](https://www.rfc-editor.org/rfc/rfc8628.html#section-6.1).

  Default value: `234567ACDEFGHJKLMNPQRSTWXYZabcdefhijkmnopqrstwxyz`

* Allow unauthenticated user code entry

  If enabled, during an OAuth 2.0 device code authentication flow, users can access and input a user code without first logging in.

  Default value: `false`

## Consent

Configure the following settings on the Consent tab:

* Saved Consent Attribute Name

  Name of a multi-valued attribute on resource owner profiles where Advanced Identity Cloud can save authorization consent decisions.

  When the resource owner chooses to save the decision to authorize access for a client application, Advanced Identity Cloud updates the resource owner's profile to avoid having to prompt the resource owner to grant authorization when the client issues subsequent authorization requests.

* Allow Clients to Skip Consent

  If enabled, clients may be configured so that the resource owner will not be asked for consent during authorization flows.

  You can override this setting for individual clients. To access client application settings, go to Native Consoles > Access Management > Realms > *Realm Name* > Applications > OAuth 2.0 > Clients > *Client ID*.

Enables consent to be gathered by a separate service.

\+ You can override this setting for individual clients. To access client application settings, go to Native Consoles > Access Management > Realms > *Realm Name* > Applications > OAuth 2.0 > Clients > *Client ID*.

* Remote Consent Service ID

  The ID of an existing remote consent service agent.

  You can override this setting for individual clients. To access client application settings, go to Native Consoles > Access Management > Realms > *Realm Name* > Applications > OAuth 2.0 > Clients > *Client ID*.

  The possible values for this property are:

  * `[Empty]`

* Remote Consent Service Request Signing Algorithms Supported

  Algorithms supported to sign consent_request JWTs for Remote Consent Services.

  Advanced Identity Cloud supports the signing algorithms listed in JSON Web Algorithms (JWA): ["alg" (Algorithm) Header Parameter Values for JWS](https://www.rfc-editor.org/rfc/rfc7518.html#section-3.1):

  * `HS256` - HMAC with SHA-256.

  * `HS384` - HMAC with SHA-384.

  * `HS512` - HMAC with SHA-512.

  * `ES256` - ECDSA with SHA-256 and NIST standard P-256 elliptic curve.

  * `ES384` - ECDSA with SHA-384 and NIST standard P-384 elliptic curve.

  * `ES512` - ECDSA with SHA-512 and NIST standard P-521 elliptic curve.

  * `RS256` - RSASSA-PKCS-v1_5 using SHA-256.

* Remote Consent Service Request Encryption Algorithms Supported

  Encryption algorithms supported to encrypt Remote Consent Service requests.

  Advanced Identity Cloud supports the following encryption algorithms:

  * `RSA1_5` - RSA with PKCS#1 v1.5 padding.

  * `RSA-OAEP` - RSA with Optimal Asymmetric Encryption Padding (OAEP) with SHA-1 and MGF-1.

  * `RSA-OAEP-256` - RSA with OAEP with SHA-256 and MGF-1.

  * `A128KW` - AES Key Wrapping with 128-bit key derived from the client secret.

  * `A192KW` - AES Key Wrapping with 192-bit key derived from the client secret.

  * `A256KW` - AES Key Wrapping with 256-bit key derived from the client secret.

  * `dir` - Direct encryption with AES using the hashed client secret.

* Remote Consent Service Request Encryption Methods Supported

  Encryption methods supported to encrypt Remote Consent Service requests.

  Advanced Identity Cloud supports the following encryption methods:

  * `A128GCM`, `A192GCM`, and `A256GCM` - AES in Galois Counter Mode (GCM) authenticated encryption mode.

  * `A128CBC-HS256`, `A192CBC-HS384`, and `A256CBC-HS512` - AES encryption in CBC mode, with HMAC-SHA-2 for integrity.

* Remote Consent Service Response Signing Algorithms Supported

  Algorithms supported to verify signed consent_response JWT from Remote Consent Services.

  Advanced Identity Cloud supports the signing algorithms listed in JSON Web Algorithms (JWA): ["alg" (Algorithm) Header Parameter Values for JWS](https://www.rfc-editor.org/rfc/rfc7518.html#section-3.1):

  * `HS256` - HMAC with SHA-256.

  * `HS384` - HMAC with SHA-384.

  * `HS512` - HMAC with SHA-512.

  * `ES256` - ECDSA with SHA-256 and NIST standard P-256 elliptic curve.

  * `ES384` - ECDSA with SHA-384 and NIST standard P-384 elliptic curve.

  * `ES512` - ECDSA with SHA-512 and NIST standard P-521 elliptic curve.

  * `RS256` - RSASSA-PKCS-v1_5 using SHA-256.

* Remote Consent Service Response Encryption Algorithms Supported

  Encryption algorithms supported to decrypt Remote Consent Service responses.

  Advanced Identity Cloud supports the following encryption algorithms:

  * `RSA1_5` - RSA with PKCS#1 v1.5 padding.

  * `RSA-OAEP` - RSA with Optimal Asymmetric Encryption Padding (OAEP) with SHA-1 and MGF-1.

  * `RSA-OAEP-256` - RSA with OAEP with SHA-256 and MGF-1.

  * `A128KW` - AES Key Wrapping with 128-bit key derived from the client secret.

  * `A192KW` - AES Key Wrapping with 192-bit key derived from the client secret.

  * `A256KW` - AES Key Wrapping with 256-bit key derived from the client secret.

  * `dir` - Direct encryption with AES using the hashed client secret.

* Remote Consent Service Response Encryption Methods Supported

  Encryption methods supported to decrypt Remote Consent Service responses.

  Advanced Identity Cloud supports the following encryption methods:

  * `A128GCM`, `A192GCM`, and `A256GCM` - AES in Galois Counter Mode (GCM) authenticated encryption mode.

  * `A128CBC-HS256`, `A192CBC-HS384`, and `A256CBC-HS512` - AES encryption in CBC mode, with HMAC-SHA-2 for integrity.

## CIBA

Configure the following settings on the CIBA tab:

* Back Channel Authentication ID Lifetime (seconds)

  How long the backchannel authentication request ID is valid, in seconds.

  Default value: `600`

* Polling Wait Interval (seconds)

  The minimum time period, in seconds, the Client should wait between polling requests to the token endpoint.

  Default value: `2`

* Signing Algorithms Supported

  Algorithms supported to sign the CIBA request parameter.

  Advanced Identity Cloud supports the signing algorithms listed in JSON Web Algorithms (JWA): ["alg" (Algorithm) Header Parameter Values for JWS](https://www.rfc-editor.org/rfc/rfc7518.html#section-3.1):

  * `ES256` - ECDSA with SHA-256 and NIST standard P-256 elliptic curve.

  * `PS256` - RSASSA-PSS using SHA-256.

## Plugins

You can script extensions in JavaScript to customize the following functionality in your OAuth 2.0 authorization server:

* [Access token modification](../am-oauth2/modifying-access-tokens-scripts.html)

* [OIDC claims](../am-oauth2/plugins-user-info-claims.html)

* [Scope evaluation](../am-oauth2/plugins-scope-evaluator.html)

* [Scope validation](../am-oauth2/plugins-scope-validator.html)

* [Authorize endpoint data provider](../am-oauth2/plugins-auth-endpoint-data-provider.html)

Find more information in [Customize OAuth 2.0 using JavaScript extensions](../am-oauth2/plugins-customize.html).

Plugins have the following configurable attributes:

* `Plugin Type`:

  * `SCRIPTED` to run a custom script

  * `JAVA` for the default Java implementation. Advanced Identity Cloud doesn't support custom Java plugins.

* `Script`:

  The script that is run for `SCRIPTED` plugin types.

* `Implementation Class`:

  The default Java class invoked for `JAVA` plugin types.

  |   |                                                                                                                                                                                                                    |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | You can override this setting for individual clients. To access client application settings, go to Native Consoles > Access Management > Realms > *Realm Name* > Applications > OAuth 2.0 > Clients > *Client ID*. |

Set the following properties to customize OAuth 2.0 behavior:

* Access Token Modification Plugin Type

  Default value: `SCRIPTED`

* Access Token Modification Script

  This script is run when issuing an access token. The script lets you modify the token, for example, by altering the data fields, before it is persisted or returned to the client.

  The script is run if `Access Token Modification Plugin Type` is set to `SCRIPTED`.

  Learn more in [Access tokens](../am-oauth2/modifying-access-tokens-scripts.html).

  Default value: `Alpha OAuth2 Access Token Modification Script`

* Access Token Modifier Plugin Implementation Class

  The Java class that provides the custom implementation for the access token modifier plugin interface, `org.forgerock.oauth2.core.plugins.AccessTokenModifier`. This class is invoked when `Access Token Modification Plugin Type` is set to `JAVA`.

  Default value: `org.forgerock.openam.oauth2.OpenAMScopeValidator`

* OIDC Claims Plugin Type

  Default value: `SCRIPTED`

* OIDC Claims Script

  This script is run when issuing an ID token or during a request to the `/userinfo` OpenID Connect endpoint. Use this script to retrieve claim values based on an issued access token.

  The script is run if `OIDC Claims Plugin Type` is set to `SCRIPTED`.

  Default value: `Alpha OIDC Claims Script`

* OIDC Claims Plugin Implementation Class

  The Java class that provides the custom implementation for the OIDC claims plugin interface, `org.forgerock.oauth2.core.plugins.UserInfoClaimsPlugin`. This class is invoked when `OIDC Claims Plugin Type` is set to `JAVA`.

  Default value: `org.forgerock.openam.oauth2.OpenAMScopeValidator`

* Scope Evaluation Plugin Type

  Default value: `JAVA`

* Scope Evaluation Script

  This script retrieves and evaluates the scope information for an OAuth2 access token.

  The script lets you populate the scopes with profile attribute values. For example, if one of the scopes is `mail`, Advanced Identity Cloud sets `mail` to the resource owner's email address in the token information returned.

  Default value: `--- Select a script ---`

* Scope Evaluation Plugin Implementation Class

  The Java class that provides the custom implementation for the evaluate scope plugin interface: `org.forgerock.oauth2.core.plugins.ScopeEvaluator`.

  Default value: `org.forgerock.openam.oauth2.OpenAMScopeValidator`

* Scope Validation Plugin Type

  Default value: `JAVA`

* Scope Validation Script

  This script validates and customizes the set of requested scopes for authorize, access token, refresh token, and backchannel authorize requests.

  Default value: `--- Select a script ---`

* Scope Validation Plugin Implementation Class

  The Java class that provides the custom implementation for the evaluate scope plugin interface: `org.forgerock.oauth2.core.plugins.ScopeValidator`.

  Default value: `org.forgerock.openam.oauth2.OpenAMScopeValidator`

* Authorize Endpoint Data Provider Plugin Type

  Default value: `JAVA`

* Authorize Endpoint Data Provider Script

  Use this script to retrieve additional data from an authorization request, such as data from the user's session or from an external service.

  Default value: `--- Select a script ---`

* Authorize Endpoint Data Provider Plugin Implementation Class

  The Java class that provides the custom implementation for the authorize endpoint data provider plugin interface: `org.forgerock.oauth2.core.plugins.AuthorizeEndpointDataProvider`.

  Default value: `org.forgerock.openam.oauth2.OpenAMScopeValidator`

* Access Token Enricher Plugin Implementation Class

  The class that provides the custom implementation for the access token enricher plugin interface.

  The access token enricher plugin interface is deprecated and will be removed in a future release.

  Default value: `org.forgerock.openam.oauth2.OpenAMScopeValidator`

## AI Agents

Configure the following settings on the AI Agents tab:

* Enable AI Agents

  Enables AI Agents support. When this option is enabled, Advanced Identity Cloud exposes AI Agents–specific configuration and endpoints for the realm.

  Use this when you plan to create or onboard AI Agents that call this realm's OAuth 2.0 endpoints Disable it in realms that don't host AI Agents.

* AI Agent Managed Object Name

  The managed object type that represents AI Agent identities, for example `managed/alpha_AIAgent`.

  Advanced Identity Cloud uses this value when it creates or updates AI Agent records during onboarding and dynamic client registration flows.

  For most deployments, a good value is `managed/realm_AIAgent`, such as `managed/alpha_AIAgent` in the `alpha` realm.

* AI Agent Privilege Managed Object Name

  The managed object type that represents AI Agent privileges, for example `managed/alpha_AIAgentPrivilege`.

  Advanced Identity Cloud uses this value when it creates or updates AI Agent privilege records during onboarding and dynamic client registration flows.

  As with the AI Agent object, a sensible value usually follows the pattern `managed/realm_AIAgentPrivilege`, such as `managed/alpha_AIAgentPrivilege` for the `alpha` realm.

* AI Agent DCR Managed Object Mapping

  Defines how attributes from dynamically registered AI Agent OAuth 2.0 clients are mapped to the AI Agent managed object in Advanced Identity Cloud.

  This mapping applies only to **dynamically registered** AI Agents (DCR clients). Manually registered clients must provide their attributes explicitly in the `aiAgentIdentityAttributes` request attribute.

  Each entry uses the syntax:

  `client-metadata-key`|`managed-object-attribute-path`

  * The key must be a client metadata field defined in RFC 7591 (for example `client_id`, `client_name`, or a locale-specific key like `client_name#en`).

  * The value is a pointer-style path to the IDM attribute on the managed object (for example `name` or `/customAttributes/name`).

  When multiple client metadata keys map to the same IDM attribute, Advanced Identity Cloud evaluates them in order and uses the first one present in the registration request. For example, this mapping:

  ```none
  client_id|oauth2ClientId
  client_name#en|name
  client_name|name
  client_id|name
  ```

  does the following:

  * Stores the OAuth 2.0 client ID in `oauth2ClientId`.

  * Sets the AI Agent's `name` from `client_name#en` if present.

  * Falls back to `client_name` if no localized name is provided.

  * Falls back to `client_id` if no name fields are present.

  Use this setting to keep AI Agent managed objects aligned with the metadata your AI Agents send at registration time. Adjust the mapping when:

  * Your AI Agent managed object uses different attribute names (for example, you store the label under `customAttributes/name/en`), or

  * Your clients send additional metadata that you want to persist on the AI Agent record.

  A sensible starting point is to map `client_id` to a dedicated identifier field (such as `oauth2ClientId`), and to map `client_name#<locale>` and `client_name` to a human-readable `name` attribute, in descending order of specificity.

## Scripted JWT Issuers

Create scripted JWT issuers so that Advanced Identity Cloud service accounts (and other JWT issuers) can be managed as data. Advanced Identity Cloud dynamically trusts them at token-grant time, with no per-issuer static configuration.

Find more information in [Configure a scripted JWT issuer](../am-oauth2/oauth2-jwt-bearer-grant.html#configure-scripted-jwt-issuer).

---

---
title: Remote consent service
description: Configure the example Advanced Identity Cloud remote consent service to demonstrate and test remote consent.
component: pingoneaic
page_id: pingoneaic:authorization:remote-consent-service
canonical_url: https://docs.pingidentity.com/pingoneaic/authorization/remote-consent-service.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "Authorization", "Setup &amp; Configuration"]
section_ids:
  configure-consent-service: Configure the consent service
  test-the-example-consent-service: Test the example consent service
  delete_the_consent_service: Delete the consent service
---

# Remote consent service

Advanced Identity Cloud supports OAuth 2.0 remote consent, allowing you to delegate the user consent-gathering process to an external service.

Advanced Identity Cloud includes a built-in example remote consent service designed for testing and evaluation. This allows you to quickly demonstrate how Advanced Identity Cloud integrates with external consent applications without setting up custom infrastructure first.

|   |                                                                                                                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The example consent service is for demonstration and testing purposes only and isn't suitable for production use because you can't configure the encryption and signing algorithms.Find information about configuring remote consent in production environments in [Remote consent](../am-oauth2/oauth2-remote-consent.html). |

## Configure the consent service

1. In the Advanced Identity Cloud admin console, go to [icon: vpn_key, set=material, size=inline] Authorization > Remote Consent Service.

2. If the service isn't already enabled, click Enable Remote Consent Service.

3. Configure the following settings:

   * Client Name

     The name used to identify this OAuth 2.0 consent service when referenced from other services.

   * Authorization Server jwk_uri

     The `jwk_uri` for retrieving the authorization server signing and encryption keys.

   * JWK Store Cache Timeout (in minutes)

     The cache timeout for the JWK store of the authorization server, in minutes.

   * JWK Store Cache Miss Cache Time (in minutes)

     The length of time a cache miss is cached, in minutes.

   * Consent Response Time Limit (in minutes)

     The time limit set on the consent response JWT before it expires, in minutes.

4. Click Save.

## Test the example consent service

The following example uses the same Advanced Identity Cloud tenant as both the authorization server and the consent service.

1. In the Advanced Identity Cloud admin console, go to [icon: vpn_key, set=material, size=inline] Authorization > Remote Consent Service and configure the consent service as follows:

   1. In Client Name, enter the agent ID of the remote consent agent profile.

      For example, `myConsentAgent`.

   2. In Authorization Server jwk_uri, enter the URI where the consent service retrieves the keys the authorization server uses to sign and encrypt the consent request. These keys include:

      * The public signing key the consent service uses to verify the signature of the consent request.

      * The public encryption key for the consent response, so that the response can be encrypted (if encryption is enabled).

      The default JWKs URI for remote consent clients is `/oauth2/consent_agents/jwk_uri`.

      For example, `https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/consent_agents/jwk_uri`.

   3. Click Save.

2. [Map the following secret labels to ESV secrets](../tenants/esvs-signing-encryption.html#map-esv-secrets-to-secret-labels):

   * `am.services.oauth2.remote.consent.response.signing.RSA`: create an ESV secret named `esv-remote-consent-response-signing-rsa` containing an RSA key pair (an RS256 signing key).

   * `am.services.oauth2.remote.consent.request.encryption`: create an ESV secret named `esv-remote-consent-request-encryption` containing a second RSA key pair (an RSA-OAEP-256 encryption key).

   Each secret must be a PEM-encoded secret containing an RSA key pair. When a certificate is included, the public key is taken from the certificate and must correspond to the private key.

   These keys must match the configuration of the consent service agent profile you create in the next step.

3. Create a remote consent agent profile by performing the steps in [Remote consent agent profile](../am-oauth2/oauth2-remote-consent.html#proc-oauth2-rcs-agent).

   Make sure the following fields are configured correctly for the example consent service:

   * Json Web Key URI: The example consent service provides a realm-specific `/oauth2/realms/root/realms/<realm>/consent/jwk_uri` path to supply its public keys to the authorization server. For example, `https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/consent/jwk_uri`.

     |   |                                                                                                                                                                                                                                                                                                                                       |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | You can verify the ESV secrets configuration before performing an OAuth 2.0 flow by sending a GET request to the `jwk_uri` endpoint. You should get a successful response with a `keys` array of two RSA keys. If you get a `500` response ("An error occurred while producing JWK"), ensure the ESVs are valid and correctly mapped. |

   * Redirect URL: The example consent service provides a realm-specific consent page. For example, `https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/consent`.

4. Enable remote consent on the OAuth 2.0 provider by performing the steps in [Use the profile](../am-oauth2/oauth2-remote-consent.html#proc-oauth2-provider-rcs).

5. Perform an OAuth 2.0 flow that requires consent. Advanced Identity Cloud renders the consent page using the example consent service.

## Delete the consent service

Deleting the service removes all the consent service configuration.

To delete the service:

1. In the Advanced Identity Cloud admin console, go to [icon: vpn_key, set=material, size=inline] Authorization > Remote Consent Service.

2. At the bottom of the page, click Delete Remote Consent Service.