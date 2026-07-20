---
title: Deprecated
description: PingGateway deprecated features and properties by version, with replacement settings and removal timelines.
component: pinggateway
version: release-notes
page_id: pinggateway::deprecated
canonical_url: https://docs.pingidentity.com/pinggateway/release-notes/deprecated.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-09T12:00:00Z
section_ids:
  2026_6: 2026.6
  2026_3: 2026.3
  2025_11: 2025.11
  2025_9: 2025.9
  2025_6: 2025.6
  2025_3: 2025.3
  2024_11: 2024.11
  2024_9: 2024.9
  2024_6: 2024.6
  2024_3: 2024.3
  2023_11: 2023.11
  2023_9: 2023.9
  2023_6: 2023.6
  2023_4: 2023.4
  2023_2: 2023.2
  7_2: 7.2
---

# Deprecated

Features and properties are deprecated and removed as defined in [Product stability labels](stability.html#interface-stability).

Unless otherwise stated, when a deprecated setting and its replacement setting are both provided, the replacement setting is used.

## 2026.6

No new deprecations.

## 2026.3

| Feature or property                | Setting            | Replacement setting                                                                                                                                                                                                                            | Removed in      |
| ---------------------------------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| `PingOneApiAccessManagementFilter` | The entire object. | Use a `PingAuthorizeFilter` instead.For this release, it's enough to change the filter `"type": "PingAuthorizeFilter"` in the configuration. At present, the new filter is fully compatible with the older `PingOneApiAccessManagementFilter`. | Not yet removed |

## 2025.11

| Feature or property | Setting                     | Replacement setting                                                    | Removed in      |
| ------------------- | --------------------------- | ---------------------------------------------------------------------- | --------------- |
| Properties          | URLs in `$location` values. | Use absolute paths or expressions resolving to absolute paths instead. | Not yet removed |

## 2025.9

| Feature or property                                                                                                           | Setting                                                              | Replacement setting                                                                                                                                    | Removed in      |
| ----------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------- |
| Fields defined as `"properties"` in `admin.json`, `config.json`, and route configuration files using `$location` expressions. | Use of ISO-8859-1 encoded text.                                      | Use UTF-8 encoded text instead.To use UTF-8 encoded text now, set the system property `org.forgerock.config.resolvers.properties.encoding` to `UTF-8`. | 2026.3          |
| The `IG_ENVCONFIG_DIRS` environment variable and the `ig.envconfig.dirs` system property.                                     |                                                                      |                                                                                                                                                        |                 |
| Any `.properties` files accessed with the `readProperties()` function.                                                        |                                                                      |                                                                                                                                                        |                 |
| The liveness and readiness endpoints                                                                                          | Deprecated endpoints:- `health/liveness`

- `health/readiness`       | Use these endpoints instead:- `health/live`

- `health/ready`                                                                                          | 2026.3          |
| Router                                                                                                                        | Reusing the `"directory"` setting in multiple Router configurations. | Use different directories for each Router configuration.                                                                                               | Not yet removed |

## 2025.6

| Feature or property                       | Setting                                                                 | Replacement setting                                                                                               | Removed in      |
| ----------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | --------------- |
| AdminHttpApplication (`admin.json`)       | `ping` endpoint                                                         | `health/startup` endpoint                                                                                         | Not yet removed |
| Duration in custom components and scripts | `org.forgerock.util.time.Duration`                                      | `java.time.Duration`                                                                                              | Not yet removed |
| JmsAuditEventHandler                      | The entire object.                                                      | Use an alternative audit event handler.                                                                           | Not yet removed |
| Prometheus metrics                        | * `ig_http_client_queue_pending`

* `ig_http_client_queue_time_seconds` | - `ig_pool_queue_pending` with tag `pool_type="http"`

- `ig_pool_queue_time_seconds` with tag `pool_type="http"` | Not yet removed |

## 2025.3

| Feature or property | Setting | Replacement setting | Removed in |
| ------------------- | ------- | ------------------- | ---------- |
| Java support        | Java 17 | Java 21             | 2026.3     |

## 2024.11

| Feature or property                    | Setting                                                                                                                                                 | Replacement setting                                                                                                                                                                                                             | Removed in      |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| AdminHttpApplication (`admin.json`)    | Provided objects you can override by defining objects with the same name:`"ApiProtectionFilter"` `"MetricsProtectionFilter"` `"StudioProtectionFilter"` | Override defaults by defining filters for the new settings:`"apiProtectionFilter"` `"metricsProtectionFilter"` `"studioProtectionFilter"`                                                                                       | Not yet removed |
|                                        | The `"Session"` key.                                                                                                                                    | Define a `"session"` property instead.                                                                                                                                                                                          | Not yet removed |
|                                        | Define a `"session"` property without using a session manager.                                                                                          | The `"session"` value is an InMemorySessionManager or JwtSessionManager.                                                                                                                                                        | Not yet removed |
| AuthorizationCodeOAuth2ClientFilter    | The `"issuerRepository"` and `"useDeprecatedIssuerRepository"` properties.                                                                              | Each AuthorizationCodeOAuth2ClientFilter will have its own private list of issuers.                                                                                                                                             | Not yet removed |
| GatewayHttpApplication (`config.json`) | The `"Session"` key.                                                                                                                                    | Define a `"session"` property instead.                                                                                                                                                                                          | Not yet removed |
|                                        | Define a `"session"` property without using a session manager.                                                                                          | The `"session"` value is an InMemorySessionManager or JwtSessionManager.                                                                                                                                                        | Not yet removed |
|                                        | The session settings will no longer default to those defined in `admin.json`.                                                                           | If no `"session"` is defined, PingGateway will use an InMemorySessionManager with default values.                                                                                                                               | Not yet removed |
| Issuer                                 | The `"issuerRepository"` and `"useDeprecatedIssuerRepository"` properties.                                                                              | Each AuthorizationCodeOAuth2ClientFilter will have its own private list of issuers.                                                                                                                                             | Not yet removed |
| IssuerRepository                       | The entire object and the default `"IssuerRepository"` defined in the AdminHttpApplication or GatewayHttpApplication heap.                              | For issuers known in advance, add their settings to the `ClientRegistration`.For discovery, if the `IssuerRepository` had an `"issueHandler"`, configure an `AuthorizationCodeOAuth2ClientFilter` `"discoveryHandler"` instead. | Not yet removed |
| JwtSession                             | The entire object.                                                                                                                                      | Use a `JwtSessionManager` for the `"session"` in `admin.json`, `config.json`, or individual `Route` configuration.                                                                                                              | Not yet removed |
| Prometheus metrics                     | The `parentId` and `parentKind` metric dimensions are deprecated.                                                                                       | Use the `parent_id` and `parent_kind` dimensions instead.                                                                                                                                                                       | Not yet removed |
| Router                                 | The default path for the `"directory"` setting.                                                                                                         | Set the `"directory"` explicitly.                                                                                                                                                                                               | Not yet removed |

## 2024.9

| Feature or property                                          | Setting                                                                 | Replacement setting                              | Removed in      |
| ------------------------------------------------------------ | ----------------------------------------------------------------------- | ------------------------------------------------ | --------------- |
| AdminHttpApplication (`admin.json`)                          | Allow administrative connections on gateway endpoints (current default) | Configure a separate `"adminConnector"` endpoint | Not yet removed |
|                                                              | `"prefix"` setting                                                      | -                                                | Not yet removed |
|                                                              | `"vertx"` > `"host"` setting                                            | `"host"`                                         | Not yet removed |
| Lazy loading in FileAttributesFilter and SqlAttributesFilter | `target` field                                                          | FileAttributesContext and SqlAttributesContext   | Not yet removed |
| RouterHandler alias                                          | `RouterHandler`                                                         | `Router`                                         | Not yet removed |

## 2024.6

| Feature or property                                                                                                                                       | Setting                                                       | Replacement setting                                                | Removed in      |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------ | --------------- |
| Prometheus endpoint                                                                                                                                       | `…​/openig/metrics/prometheus`                                | `…​/openig/metrics/prometheus/0.0.4`                               | Not yet removed |
| Prometheus metrics:- `org.forgerock.monitoring.api.instrument.DistributionSummary`

- `org.forgerock.monitoring.api.instrument.Timer`                     | `…​_count{…​} …​` `…​_seconds_count{…​} …​` `…​_total{…​} …​` | `…​_seconds_count{…​} …​` `…​_seconds_sum{…​} …​` `…​_sum{…​} …​`  | Not yet removed |
| Prometheus metrics:- `ig_route_response_time`

- `ig_route_response_time_seconds`

- `ig_cache_loads`

- `ig_cache_loads_seconds`

- `ig_cache_evictions` | `…​_count{…​} …​` `…​_seconds_total{…​} …​`                   | `…​_seconds_count{…​} …​` `…​_seconds_sum{…​} …​`                  | Not yet removed |
| TokenResolver class used as follows:- `_token('property','default'}`

- `_t('property','default'}`                                                        | Whole class                                                   | Not replaced. Use the following expression format instead: `&{…​}` | Not yet removed |

## 2024.3

| Feature or property             | Setting                                                                                                                                      | Replacement setting                                                                                      | Removed in      |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | --------------- |
| Vert.x                          | Options described in [4.5.0 Deprecations and breaking changes](https://github.com/vert-x3/wiki/wiki/4.5.0-Deprecations-and-breaking-changes) | Options described in [VertxOptions](https://vertx.io/docs/4.5.0/apidocs/io/vertx/core/VertxOptions.html) | Not yet removed |
| Common REST Monitoring Endpoint | Whole feature                                                                                                                                | Prometheus Scrape Endpoint                                                                               | Not yet removed |

## 2023.11

| Feature or property                 | Setting  | Replacement setting | Removed in |
| ----------------------------------- | -------- | ------------------- | ---------- |
| AuthorizationCodeOAuth2ClientFilter | `target` | Not yet defined     | 2026.3     |
| Java support                        | Java 11  | Java 17             | 2024.3     |

## 2023.9

| Feature or property                                                | Setting                                            | Replacement setting      | Removed in |
| ------------------------------------------------------------------ | -------------------------------------------------- | ------------------------ | ---------- |
| Retrieval of the target URI in AuthorizationCodeOAuth2ClientFilter | `request.uri` or `originalUri` in UriRouterContext | IdpSelectionLoginContext | 2026.3     |

## 2023.6

| Feature or property     | Setting                                            | Replacement setting                                      | Removed in |
| ----------------------- | -------------------------------------------------- | -------------------------------------------------------- | ---------- |
| Vert.x                  | `maxHeaderSize``initialSettings.maxHeaderListSize` | `connectors:maxTotalHeadersSize` in AdminHttpApplication | 2026.3     |
| PolicyEnforcementFilter | `useLegacyAdviceEncoding`                          | Advice encoding with the encoder used by the AM version. | 2026.3     |

## 2023.4

| Feature or property   | Setting                                                                                                                      | Replacement setting  | Removed in |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------- | -------------------- | ---------- |
| CookieFilter          | Use of the Set-Cookie2 HTTP header, obsoleted by [RFC 6265: Set-Cookie2](https://www.rfc-editor.org/rfc/rfc6265#section-9.4) | Not replaced         | 2026.3     |
| SamlFederationHandler | Whole object                                                                                                                 | SamlFederationFilter | 2026.3     |

## 2023.2

| Feature or property                 | Setting                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Replacement setting                                                                                                                                                                                                                         | Removed in      |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| Studio                              | Structured Editor                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Not replaced                                                                                                                                                                                                                                | Not yet removed |
| KeyStoreSecretStore                 | Required property `storePassword` Optional property `keyEntryPassword`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Optional property `storePasswordSecretId` Optional property `entryPasswordSecretId`                                                                                                                                                         | 2026.3          |
| HsmSecretStore                      | property `storePassword`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | property `storePasswordSecretId`                                                                                                                                                                                                            | 2026.3          |
| Names of Prometheus counter metrics | `request` `response.error` `response.null` `response.status.client_error` `response.status.informational` `response.status.redirection` `response.status.server_error` `response.status.successful` `response.status.unknown`                                                                                                                                                                                                                                                                                                                                                                                        | In a future release, the deprecated names are expected to be replaced with names ending in `_total`.Only the metric name is deprecated; the information provided by the metric is not deprecated. Other Prometheus metrics aren't affected. | 2026.3          |
| Names of Vert.x counter metrics     | `vertx_net_client_bytes_read` `vertx_net_client_bytes_written` `vertx_net_client_errors` `vertx_http_client_bytes_read` `vertx_http_client_bytes_written` `vertx_http_client_errors` `vertx_net_server_bytes_read` `vertx_net_server_bytes_written` `vertx_net_server_errors` `vertx_http_server_bytes_read` `vertx_http_server_bytes_written` `vertx_http_server_errors` `vertx_datagram_errors` `vertx_eventbus_processed` `vertx_eventbus_published` `vertx_eventbus_discarded` `vertx_eventbus_sent` `vertx_eventbus_received` `vertx_eventbus_delivered` `vertx_eventbus_reply_failures` `vertx_pool_completed` | In a future release, the deprecated names are expected to be replaced with names ending in `_total`.Only the metric name is deprecated; the information provided by the metric isn't deprecated. Other Vert.x metrics aren't affected.      | 2026.3          |
| KeyStore                            | Whole object                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | KeyStoreSecretsStoreThere will be no replacement for keystore loading from a URL.                                                                                                                                                           | 2026.3          |
| KeyManager                          | Whole object                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | SecretsKeyManager                                                                                                                                                                                                                           | 2026.3          |
| TrustManager                        | Whole object                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | SecretsTrustManagerFind examples in the [SecretsTrustManager reference](https://docs.pingidentity.com/pinggateway/2026/reference/SecretsTrustManager.html#SecretsTrustManager-example).                                                     | 2026.3          |
| CapturedUserPasswordFilter          | A `GenericSecret` shared key                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | A `CryptoKey` shared key.After removal, it will no longer be possible to store the shared key in a Base64SecretStore.                                                                                                                       | 2026.3          |

## 7.2

| Feature or property                 | Setting                                                                                                | Replacement setting                                                                                                                                                                                                   | Removed in |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| CapturedUserPasswordFilter          | `keyType` value `DES`                                                                                  | `AES`                                                                                                                                                                                                                 | 2025.3     |
| ClientCredentialsOAuth2ClientFilter | `clientId`, `clientSecretId`, `handler`                                                                | `endpointHandler`, which uses ClientSecretBasicAuthenticationFilter or ClientSecretPostAuthenticationFilter                                                                                                           | 2025.3     |
| ClientHandler                       | `proxy`, `systemProxy`                                                                                 | `proxyOptions`                                                                                                                                                                                                        | 2025.3     |
|                                     | `hostnameVerifier`                                                                                     | ClientTlsOptions property `hostnameVerifier`                                                                                                                                                                          | 2025.3     |
| ClientRegistration                  | `tokenEndpointAuthMethod` `tokenEndpointAuthSigningAlg` `privateKeyJwtSecretId` `jwtExpirationTimeout` | `authenticatedRegistrationHandler`                                                                                                                                                                                    | 2025.3     |
| OAuth2ClientFilter                  | Filter name                                                                                            | AuthorizationCodeOAuth2ClientFilter                                                                                                                                                                                   | 2025.3     |
| ReverseProxyHandler                 | `proxy`, `systemProxy`                                                                                 | `proxyOptions`                                                                                                                                                                                                        | 2025.3     |
|                                     | `hostnameVerifier`                                                                                     | ClientTlsOptions property `hostnameVerifier` If a ReverseProxyHandler includes the deprecated `"hostnameVerifier": "ALLOW_ALL"` configuration, it takes precedence, and deprecation warnings are written to the logs. | 2025.3     |

---

---
title: Fixes
description: PingGateway important bug fixes by version for major and minor releases.
component: pinggateway
version: release-notes
page_id: pinggateway::fixes
canonical_url: https://docs.pingidentity.com/pinggateway/release-notes/fixes.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-09T12:00:00Z
section_ids:
  fix-in-2026.6: Fixed in PingGateway 2026.6
  fix-in-2026.3: Fixed in PingGateway 2026.3
  fix-in-2025.11.2: Fixed in PingGateway 2025.11.2
  fix-in-2025.11.1: Fixed in PingGateway 2025.11.1
  fix-in-2025.11: Fixed in PingGateway 2025.11
  fix-in-2025.9: Fixed in PingGateway 2025.9
  fix-in-2025.6: Fixed in PingGateway 2025.6
  fix-in-2025.3: Fixed in PingGateway 2025.3
  fix-in-2024.11.2: Fixed in PingGateway 2024.11.2
  fix-in-2024.11.1: Fixed in PingGateway 2024.11.1
  fix-in-2024.11: Fixed in PingGateway 2024.11
  fix-in-2024.9: Fixed in PingGateway 2024.9
  fix-in-2024.6: Fixed in PingGateway 2024.6
  fix-in-2024.3: Fixed in IG 2024.3
  fix-in-2023.11.2: Fixed in IG 2023.11.2
  fix-in-2023.11.1: Fixed in IG 2023.11.1
  fix-in-2023.11: Fixed in IG 2023.11
  fix-in-2023.9: Fixed in IG 2023.9
  fix-in-2023.6: Fixed in IG 2023.6
  fix-in-2023.4: Fixed in IG 2023.4
  fix-in-2023.2: Fixed in IG 2023.2
  fix-in-7.2: Fixed in IG 7.2
  security-advisories: Security advisories
---

# Fixes

The following pages list important fixes in major or minor versions.

## Fixed in PingGateway 2026.6

No new fixes.

## Fixed in PingGateway 2026.3

* OPENIG-9996: Java properties file which is no longer used by location property is not released on Windows

* OPENIG-9952: Location property: usage of `$location:props` does not work on Windows

* OPENIG-9882: Large multipart uploads fail to complete (streaming mode)

## Fixed in PingGateway 2025.11.2

No new fixes.

## Fixed in PingGateway 2025.11.1

No new fixes.

## Fixed in PingGateway 2025.11

* OPENIG-9543: Welcome page is out of date

## Fixed in PingGateway 2025.9

* OPENIG-9594: Gateway log shows warning message even though maxBodyLength is not set

* OPENIG-9501: Expressions are no longer evaluated before using the openTelemetry configuration

* OPENIG-9483: ig\_route\_request\_active doesn't decrement in case of RuntimeException

## Fixed in PingGateway 2025.6

* OPENIG-9141: Tracing: if proxyOptions uri has no port number, it fails with `port out of range:-1`

## Fixed in PingGateway 2025.3

* OPENIG-9015: PingGateway throws IllegalArgumentException with JwtSession and 'sessionIdleRefresh: true' in AmService

* OPENIG-8900: Existing query parameters should not be decoded when working with the marker parameter in the DataPreservationFilter

* OPENIG-8211: OAuth2ResourceServerFilter: default value for realm should be empty

* OPENIG-6608: Can't set cookie domain in session cookies

## Fixed in PingGateway 2024.11.2

No new fixes.

## Fixed in PingGateway 2024.11.1

* OPENIG-9015: PingGateway throws IllegalArgumentException with JwtSession and 'sessionIdleRefresh: true' in AmService

## Fixed in PingGateway 2024.11

* OPENIG-8853: Welcome page doesn't display the current year in the copyright section

## Fixed in PingGateway 2024.9

* OPENIG-8544: PingOneApiAccessManagementFilter `"includeBody": false` isn't a possible value

* OPENIG-8489: Attempting to create the default router directory can fail when filesystem is read-only even when the directory exists

* OPENIG-8325: Fix undelivered connection closures found in performance test

* OPENIG-8259: `ig_http_server_active_requests` metric shows negative values

* OPENIG-7296: In Studio, switching deployment status of a route makes it out of sync

## Fixed in PingGateway 2024.6

* OPENIG-8432: Config expression doesn't work in audit service's event handler configuration

* OPENIG-8370: IG standalone 2023.11 and above throws NPE and return response 500

* OPENIG-8340: RouterHandler should validate the directory being set in the config

* OPENIG-8295: When a trailing header is used in a StaticResponseHandler the HTTP response doesn't conform to the HTTP spec

## Fixed in IG 2024.3

* OPENIG-7557: Inline named object declarations in IG config interactions with heap objects are misleading

* OPENIG-7633: Http endRequest metrics should check if handler is null

* OPENIG-7674: Misleading deprecation notice in ClientRegistration without secretsProvider

* OPENIG-7680: GzipFlowableTransformer fails when there is empty bytebuffer after actual gzip content

* OPENIG-7736: IG drops some bytes during POST and PUT of large data/images

* OPENIG-7738: readWithCharset method doesn't return the content of the file as a plain string.

* OPENIG-7790: HTTP Client Active Request Gauge can display negative values

* OPENIG-7859: org.forgerock.openig.filter.oauth2.client.ClientRegistration#revokeToken logs incorrect endpoint when revocation fails

* OPENIG-7978: PEF should return 401 when no subjects can be found instead of 500

* OPENIG-8069: Vertx threads are getting locked on org.forgerock.http.vertx.monitoring.meters.Gauges.get(Tags)

* OPENIG-8070: vert.x threads are getting locked on SessionInfoCache$IndexTable

## Fixed in IG 2023.11.2

* OPENIG-9015: PingGateway throws IllegalArgumentException with JwtSession and 'sessionIdleRefresh: true' in AmService

## Fixed in IG 2023.11.1

* OPENIG-7633: Http endRequest metrics should check if handler is null

* OPENIG-7736: IG drops some bytes during POST and PUT of large data/images

## Fixed in IG 2023.11

* OPENIG-7453: SecretsTrustManager fails to load CA-signed certificates due to restrictive KeyUsage

* OPENIG-7768: Declaring JwtSession named 'Session' in config.json fails

* OPENIG-7774: CorsFilter should handle invalid policies better instead of throwing NPE

* OPENIG-4817: Can't specify any host information for HTTP/2 request

## Fixed in IG 2023.9

* OPENIG-5294: Clear Issuer cache on exception

## Fixed in IG 2023.6

* OPENIG-7429: IG can't handle requests with IPv6 URL

* OPENIG-7474: SwitchFilter's handler fails to send original POST request entity

## Fixed in IG 2023.4

* OPENIG-5913: (UI) Route configuration lost sometime after un-deploy from route list

## Fixed in IG 2023.2

* OPENIG-6911: Failed agent authentication isn't clear from the IG logs

## Fixed in IG 7.2

* OPENIG-6911: Failed agent authentication isn't clear from the IG logs

* OPENIG-6394: Stack traces are printed twice in the log files

* OPENIG-6206: When checking for peer certificates in a request, validate that the SSLSession is available

  PingGateway logs a TRACE-level message from ChfApplicationWebHandler if this hasn't been resolved. The message includes the following text:

  ```
  No client certificates found, check the exception trace if this was not expected
  javax.net.ssl.SSLPeerUnverifiedException: peer not authenticated
  ```

* OPENIG-5872: Stop Tyrus WebSocket connection retry when Websocket Client is closed

* OPENIG-5868: WebSocketClientHandshakeException: Invalid subprotocol seen when using IG standalone to proxy WebSocket requests

* OPENIG-5805: The notification service should attempt to refresh the caller token when receiving a 401 on WebSocket connections

* OPENIG-5793: Unexpected behaviour of EL function matches

* OPENIG-5778: sessionInfo requests can lead to a build up of agent tokens being created

* OPENIG-5743: Standalone: Possible OOME for large requests

* OPENIG-5725: Add SNI configuration

* OPENIG-5683: HTTP/2 : set max connections

* OPENIG-5610: Null Pointer Exception when using ForwardedRequestFilter with ResourceHandler

* OPENIG-5540: PEM secret format fails to decode some EC private keys

* OPENIG-5539: The ForwardedRequestFilter shouldn't change original URI parameter values when rebasing

* OPENIG-5425: JwkSetHandler: No error displayed when using an invalid configuration such as a public key exported -as jwk- for decryption usage

* OPENIG-4956: Inbound WebSocket connection isn't closed when outbound connection is closed abruptly

## Security advisories

Ping Identity issues security advisories in collaboration with our customers to address any security vulnerabilities transparently and rapidly.

Ping Identity's security advisory policy governs the process on how security issues are submitted, received, and evaluated as well as the timeline for the issuance of security advisories and patches.

You can find security advisories in the Ping Identity [support portal](https://support.pingidentity.com/s/product-roadmap?product=pinggateway\&tabset-84e58=3) (requires sign-on).

---

---
title: Getting support
description: How to get support from Ping Identity, including support services, professional services, and documentation links.
component: pinggateway
version: release-notes
page_id: pinggateway::support
canonical_url: https://docs.pingidentity.com/pinggateway/release-notes/support.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-03-02T12:00:00Z
---

# Getting support

Ping Identity provides support services, professional services, training, and partner services to assist you in setting up and maintaining your deployments. Find a general overview of these services at <https://www.pingidentity.com>.

Ping Identity has staff members around the globe who support our international customers and partners. Learn about Ping Identity's support offering at <https://www.pingidentity.com/support>.

Ping Identity publishes comprehensive documentation online:

* The Ping Identity [Knowledge Base](https://support.pingidentity.com/s/knowledge-base) offers a large and increasing number of up-to-date, practical articles that help you deploy and manage Ping Identity Platform software.

  While many articles are visible to everyone, Ping Identity customers have access to much more, including advanced information for customers using Ping Identity Platform software in a mission-critical capacity.

* Ping Identity product documentation, such as this document, aims to be technically accurate and complete with respect to the software documented. It is visible to everyone and covers all product features and examples of how to use them.

---

---
title: Groovy support
description: Groovy versions supported by PingGateway for scripting, listed by PingGateway version.
component: pinggateway
version: release-notes
page_id: pinggateway::groovy-for-scripting
canonical_url: https://docs.pingidentity.com/pinggateway/release-notes/groovy-for-scripting.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-09T12:00:00Z
---

# Groovy support

PingGateway supports these versions of the Groovy programming language for scripting:

| PingGateway version | 7.2    | 2023.11.x | 2024.11.x | 2025.3 - 2025.9 | 2025.11.x | 2026.x |
| ------------------- | ------ | --------- | --------- | --------------- | --------- | ------ |
| Groovy version      | 3.0.10 | 4.0.12    | 4.0.19    | 4.0.25          | 4.0.28    | 4.0.28 |

---

---
title: Incompatible changes
description: PingGateway incompatible changes by version — review before upgrading to update your scripts and plugins.
component: pinggateway
version: release-notes
page_id: pinggateway::changes
canonical_url: https://docs.pingidentity.com/pinggateway/release-notes/changes.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-23T12:00:00Z
section_ids:
  2026_6: 2026.6
  2026_3: 2026.3
  2025_11: 2025.11
  2025_9: 2025.9
  2025_6: 2025.6
  2025_3: 2025.3
  new_default_port_and_paths_for_administrative_endpoints: New default port and paths for administrative endpoints
  prometheus_scrape_endpoint_changes: Prometheus Scrape Endpoint changes
  pinggateway_now_validates_id_token_signatures_by_default: PingGateway now validates ID token signatures by default
  oauth2resourceserverfilter_no_longer_sets_a_realm_by_default: OAuth2ResourceServerFilter no longer sets a realm by default
  usedeprecatedissuerrepository_is_now_false_by_default: useDeprecatedIssuerRepository is now false by default
  2024_11: 2024.11
  2024_9: 2024.9
  zero_valued_prometheus_metrics: Zero-valued Prometheus metrics
  2024_6: 2024.6
  router_now_checks_for_directory: Router now checks for directory
  clientregistration_configurations: ClientRegistration configurations
  issuer_configurations: Issuer configurations
  2024_3: 2024.3
  ig_war_file: IG .war file
  secretsprovider_property_changes_from_optional_to_required: secretsProvider property changes from optional to required
  scripts: Scripts
  java_17: Java 17
  vert_x: Vert.x
  handling_of_failed_http_responses: Handling of failed HTTP responses
  jwt_must_be_signed_or_encrypted: JWT must be signed or encrypted
  improved_security_for_crossdomainsinglesignonfilter: Improved security for CrossDomainSingleSignOnFilter
  ig_zip_file: IG .zip file
  treatment_of_http_500_errors: Treatment of HTTP 500 errors
  inline_objects_cant_be_referenced_from_the_configuration: Inline objects can't be referenced from the configuration
  2023_11: 2023.11
  change_to_host_header_capitalization_for_http2: Change to host header capitalization for HTTP/2
  safeguard_against_accidental_exposure_of_private_keys_with_jwksethandler: Safeguard against accidental exposure of private keys with JwkSetHandler
  2023_9: 2023.9
  2023_6: 2023.6
  improved_security_for_scripts: Improved security for scripts
  2023_4: 2023.4
  2023_2: 2023.2
  7_2: 7.2
  scriptableresourceuriprovider_accepts_returned_values_only_as_a_string: ScriptableResourceUriProvider accepts returned values only as a String
  am_5_x_x_eol: AM 5.x.x EOL
  keytype_for_captureduserpasswordfilter_is_required: keyType for CapturedUserPasswordFilter is required
  jwt_classes_relocated_to_new_packages: JWT classes relocated to new packages
  cdsso_requires_session_cookies_with_samesitenone_securetrue: CDSSO requires session cookies with SameSite=None, Secure=True
---

# Incompatible changes

*Incompatible changes* are changes affecting existing functionality and migration from a previous release. Before you upgrade, make appropriate changes to your scripts and plugins.

## 2026.6

* When using a [TracingDecorator](https://docs.pingidentity.com/pinggateway/2026/reference/TracingDecorator.html) with an [AuditService](https://docs.pingidentity.com/pinggateway/2026/reference/AuditService.html), note the following field name changes:

  * `code.function` is now `code.function.name`.

    This field records the audit function triggered, such as `handleCreate`.

  * `code.namespace` is now `code.file.path`. This field records the path of the JSON resource.

## 2026.3

* The `PingGateway-2026.6.0.zip` now unpacks to a directory named `ping-gateway-version` instead of `identity-gateway-version`.

  For example, this release unpacks to `/path/to/ping-gateway-2026.3.0`.

- The directories used in the PingGateway Dockerfile have also been renamed:

  | Description               | Old location | New location   | Environment variable |
  | ------------------------- | ------------ | -------------- | -------------------- |
  | PingGateway binaries      | `/opt/ig`    | `/opt/gateway` | `INSTALL_DIR`        |
  | PingGateway configuration | `/var/ig`    | `/var/gateway` | `IG_INSTANCE_DIR`    |

  |   |                                                                                              |
  | - | -------------------------------------------------------------------------------------------- |
  |   | You should use the environment variables in your Dockerfiles instead of the directory paths. |

* The default session cookie name for administrative connections has changed.

  The default name for administrative session cookies is now `IG_ADMIN_SESSIONID`. The default name for all other connections remains `IG_SESSIONID`.

  By default, PingGateway no longer shares the session manager between administrative and non-administrative connections. If you have a session manager configured with the `"session"` property only in `admin.json`, also configure a session manager with the `"session"` property in `config.json`. Use different cookie names for each session manager.

- If any components defined in `config.json` or `admin.json` fail to load, PingGateway now fails to start and logs an appropriate startup error.

  Previously, if a component failed to load, PingGateway would start successfully but would respond to subsequent requests with a `500 Internal Server Error`.

  When the `failOnRouteError` router setting is set to `true`, any invalid routes loaded by that router prevents the router component from starting. If there are nested routers and they're all configured with `failOnRouteError`, the failure cascades up and prevents PingGateway from starting.

* The `stop.sh` and `stop.bat` scripts now let the PingGateway process terminate gracefully by default.

  Each script now takes at most two optional arguments:

  1. The PingGateway instance directory

  2. A time limit specifying how long to wait before forcing the process to terminate

  Learn more in [Forcible shutdown](https://docs.pingidentity.com/pinggateway/2026/installation-guide/start-stop.html#forcible-shutdown).

* When rotating audit files, PingGateway continues to add a timestamp as the rotation filename suffix by default.

  Previously, the timestamps reflected local time. The timestamps now reflect Coordinated Universal Time (UTC) instead. This can cause an offset of several hours in the timestamps depending on your time zone. Newly rotated audit files can temporarily have timestamps earlier than existing files.

* The JSON log message format for the base PingGateway Docker image has changed.

  For example, log messages now show:

  * Timestamps in milliseconds and a separate `"nanoseconds"` field.

  * Stack traces as JSON objects rather than strings.

  Adapt your log processing to accommodate these changes.

- When configuring the `openDuration` property in the CircuitBreakerFilter, the maximum permitted duration is now `1 day`.

  Previously, there wasn't a maximum duration.

## 2025.11

No new incompatible changes.

## 2025.9

No new incompatible changes.

## 2025.6

No new incompatible changes.

## 2025.3

### New default port and paths for administrative endpoints

When you don't explicitly define `admin.json` settings, PingGateway now listens for HTTP administrative requests on port 8085 and omits the deprecated `/openig` path prefix from the paths to administrative endpoints.

Examples in the documentation reflect these new default settings.

You can change the port and related settings by configuring an [adminConnector](https://docs.pingidentity.com/pinggateway/2026/reference/AdminHttpApplication.html#AdminHttpApplication-adminConnector) in `admin.json`.

### Prometheus Scrape Endpoint changes

* The `/metrics/prometheus` endpoint is no longer served by default. If possible, use `/metrics/prometheus/0.0.4` instead.

  The `admin.json` [serveDeprecatedPrometheusEndpoint](https://docs.pingidentity.com/pinggateway/2026/reference/AdminHttpApplication.html#AdminHttpApplication-serveDeprecatedPrometheusEndpoint) setting now defaults to `false`. Set it to `true` and restart PingGateway if you must use the old endpoint.

* The metric `ig_jvm_free_used_memory_bytes` has been renamed `ig_jvm_free_memory_bytes`.

### PingGateway now validates ID token signatures by default

The `ClientRegistration` [skipSignatureVerification](https://docs.pingidentity.com/pinggateway/2026/reference/ClientRegistration.html#ClientRegistration-skipSignatureVerification) setting now defaults to `true` meaning PingGateway now validates OpenID Connect ID token signatures by default.

### OAuth2ResourceServerFilter no longer sets a realm by default

The `OAuth2ResourceServerFilter` optional [realm](https://docs.pingidentity.com/pinggateway/2026/reference/OAuth2ResourceServerFilter.html#OAuth2ResourceServerFilter-realm) setting no longer sets an HTTP authentication realm by default.

### useDeprecatedIssuerRepository is now false by default

The `useDeprecatedIssuerRepository` settings for the [AuthorizationCodeOAuth2ClientFilter](https://docs.pingidentity.com/pinggateway/2026/reference/AuthorizationCodeOAuth2ClientFilter.html#AuthorizationCodeOAuth2ClientFilter-useDeprecatedIssuerRepository) and [Issuer](https://docs.pingidentity.com/pinggateway/2026/reference/Issuer.html#Issuer-useDeprecatedIssuerRepository) configurations are now `false` by default.

## 2024.11

No new incompatible changes.

## 2024.9

### Zero-valued Prometheus metrics

Following a performance improvement, the Prometheus output shows many new WebSocket proxy metrics with `0.0` values.

This could affect existing dashboards and reports.

## 2024.6

### Router now checks for directory

The [Router](https://docs.pingidentity.com/pinggateway/2026/reference/Handlers.html#Router) handler now checks the `directory` in its configuration is an existing directory PingGateway can read. If not, PingGateway throws an exception.

### ClientRegistration configurations

To enable OpenID Connect ID token signature validation and the provider uses HMAC-based signatures, ClientRegistration configurations now require settings to access the client secret used for signature validation:

* `"skipSignatureVerification"`: must be `false` to enable ID token signature validation

* `"clientSecretUsage"`: must be `ID_TOKEN_VALIDATION_AND_CLIENT_AUTHENTICATION` or `ID_TOKEN_VALIDATION_ONLY`

* `"clientSecretId"`: must identify the client secret

* `"secretsProvider"`: must provide for the client secret for signature validation

Learn more in [ClientRegistration](https://docs.pingidentity.com/pinggateway/2026/reference/MiscellaneousConfigurationObjects.html#ClientRegistration).

The Issuer for [AuthorizationCodeOAuth2ClientFilter](https://docs.pingidentity.com/pinggateway/2026/reference/Filters.html#AuthorizationCodeOAuth2ClientFilter) now uses asymmetric signature validation by default.

### Issuer configurations

When you enable OpenID Connect ID token signature validation, update these properties of your Issuer configurations:

* `"issuer"`: must match the `iss` claim value in the ID token (*required* unless it's obtained from the provider's well-known configuration URL)

* `"idTokenVerificationSecretId"`: (optional) identifies the provider's public key for signature validation

* `"secretsProvider"`: (optional) provides the public key for signature validation

* `"idTokenSkewAllowance"`: (optional) permits clock skew during signature validation

Learn more in [Issuer](https://docs.pingidentity.com/pinggateway/2026/reference/MiscellaneousConfigurationObjects.html#Issuer).

The Issuer for [AuthorizationCodeOAuth2ClientFilter](https://docs.pingidentity.com/pinggateway/2026/reference/Filters.html#AuthorizationCodeOAuth2ClientFilter) now uses asymmetric signature validation by default.

## 2024.3

### IG .war file

The IG .war file is no longer created. It was deprecated in IG 6 and stopped being delivered in IG 2023.2. Learn about migration in [Migrate from web container mode to standalone mode](https://docs.pingidentity.com/pinggateway/2024.11/upgrade/upgrade-war-to-zip.html).

### `secretsProvider` property changes from optional to required

Because the default secret service has been removed, you must configure a `secretsProvider` for the following:

* [AmService](https://docs.pingidentity.com/pinggateway/2026/reference/AmService.html)

* [CapturedUserPasswordFilter](https://docs.pingidentity.com/pinggateway/2026/reference/CapturedUserPasswordFilter.html)

* [ClientHandler](https://docs.pingidentity.com/pinggateway/2026/reference/ClientHandler.html), `proxy` property

* [ClientRegistration](https://docs.pingidentity.com/pinggateway/2026/reference/ClientRegistration.html)

* [HsmSecretStore](https://docs.pingidentity.com/pinggateway/2026/reference/HsmSecretStore.html)

* [IdentityAssertionHandlerTechPreview](https://docs.pingidentity.com/pinggateway/2024.11/reference/IdentityAssertionHandlerTechPreview.html)

* [JdbcDataSource](https://docs.pingidentity.com/pinggateway/2026/reference/JdbcDataSource.html)

* [JwkSetHandler](https://docs.pingidentity.com/pinggateway/2026/reference/JwkSetHandler.html)

* [JwtBuilderFilter](https://docs.pingidentity.com/pinggateway/2026/reference/JwtBuilderFilter.html)

* [JwtSessionFilter](https://docs.pingidentity.com/pinggateway/2026/reference/JwtSessionManager.html)

* [KeyManager](https://docs.pingidentity.com/pinggateway/2024.11/reference/KeyManager.html)

* [KeyStore](https://docs.pingidentity.com/pinggateway/2024.11/reference/KeyStore.html)

* [KeyStoreSecretStore](https://docs.pingidentity.com/pinggateway/2026/reference/KeyStoreSecretStore.html)

* [PemPropertyFormat](https://docs.pingidentity.com/pinggateway/2026/reference/PemPropertyFormat.html)

* [ResourceOwnerOAuth2ClientFilter](https://docs.pingidentity.com/pinggateway/2026/reference/ResourceOwnerOAuth2ClientFilter.html)

* [ReverseProxyHandler](https://docs.pingidentity.com/pinggateway/2026/reference/ReverseProxyHandler.html), `proxy` property

* [StatelessAccessTokenResolver](https://docs.pingidentity.com/pinggateway/2026/reference/StatelessAccessTokenResolver.html)

### Scripts

Groovy scripts used in the IG configuration must now use the UTF-8 character set. In previous releases, Groovy files referenced in the IG configuration could rely on default encoding or system properties.

### Java 17

IG no longer supports Java 11. You must upgrade to Java 17.

### Vert.x

Upgrade to Vert.x 4.5 renames and removes Vert.x options used by WebSocket connections to AM and accessed through the `vertx` setting of an [AmService](https://docs.pingidentity.com/pinggateway/2024.11/reference/AmService.html).

Learn more about Vert.x changes in [4.5.0 Deprecations and breaking changes](https://github.com/vert-x3/wiki/wiki/4.5.0-Deprecations-and-breaking-changes).

Use the Vert.x options described in [VertxOptions](https://vertx.io/docs/4.5.0/apidocs/io/vertx/core/VertxOptions.html).

### Handling of failed HTTP responses

IG now fails an HTTP response promise when:

* Streaming is disabled by the `streamingEnabled` property of [admin.json](https://docs.pingidentity.com/pinggateway/2026/reference/AdminHttpApplication.html). This is the default setting.

* The response provides response headers but not the entire response body.

In previous releases, IG completed the response promise but the response was unreadable.

### JWT must be signed or encrypted

The following filters must now be configured with a SecretsProvider and signature or encryption:

* [JwtBuilderFilter](https://docs.pingidentity.com/pinggateway/2026/reference/JwtBuilderFilter.html)

* [GrantSwapJwtAssertionOAuth2ClientFilter](https://docs.pingidentity.com/pinggateway/2026/reference/GrantSwapJwtAssertionOAuth2ClientFilter.html)

### Improved security for CrossDomainSingleSignOnFilter

When `verificationSecretId` in CrossDomainSingleSignOnFilter is configured, IG uses it to verify the signature of AM session tokens. When `verificationSecretId` isn't configured, IG discovers and uses the AM JWK set to verify the signature of AM session tokens.

From this release, if `verificationSecretId` isn't configured **and** IG can't use the AM JWK set, the CrossDomainSingleSignOnFilter fails to start.

In previous releases, the CrossDomainSingleSignOnFilter accepted unsigned tokens.

### IG .zip file

To prevent confusion during upgrade, PingGateway-2026.6.0.zip now unpacks to a directory containing the IG version number. For example, this release unpacks to `/path/to/identity-gateway-2024.3.0`.

In previous releases, PingGateway-2026.6.0.zip unpacked to `/path/to/identity-gateway`.

### Treatment of HTTP 500 errors

HTTP 500 errors are no longer computed in Handlers or Filters. Instead, they fail the response promise with the Runtime exception that caused the failure.

### Inline objects can't be referenced from the configuration

In previous releases, other objects in a configuration could refer to an inline object through its `name` property. Inline objects can no longer be referenced by other objects; only named heap objects can be referenced by other objects.

## 2023.11

### Change to host header capitalization for HTTP/2

For HTTP/2, PingGateway pseudo-headers and `host` response headers are now lowercase.

This isn't a breaking change. [RFC 2616, 4.2 Message Headers](https://www.rfc-editor.org/rfc/rfc2616#section-4.2) explains, "Field names are case-insensitive."

Some applications expect case-sensitive header names, such as `Host`, however. Update these applications to accept case-insensitive headers.

### Safeguard against accidental exposure of private keys with JwkSetHandler

A new `exposePrivateSecrets` property is available in [JwkSetHandler](https://docs.pingidentity.com/pinggateway/2023.11/reference/JwkSetHandler.html) to safeguard against the accidental exposure of private keys in a JWK set.

The property is `false` by default to prevent exposure of private keys. To expose private keys, you must now explicitly set the property to `true`.

## 2023.9

No new incompatible changes.

## 2023.6

### Improved security for scripts

To improve security, IG now runs scripts only from an absolute path, or from a path relative to the base script directory. Routes that refer to scripts otherwise, such as through a URL, fail to deploy.

Learn more in the documentation about the `file` property of scripts.

## 2023.4

No new incompatible changes.

## 2023.2

The IG .war file is no longer delivered.

## 7.2

### ScriptableResourceUriProvider accepts returned values only as a `String`

ScriptableResourceUriProvider accepts returned values only as a `String`. In previous releases, it accepted returned values as a `String` or `Promise<String>`. Learn more in the documentation for `ScriptableResourceUriProvider` in [PolicyEnforcementFilter](https://docs.pingidentity.com/pinggateway/7.2/reference/PolicyEnforcementFilter.html).

### AM 5.x.x EOL

AM 5.x.x has reached product end of life and is no longer supported. The default value of the AmService property `version` has changed to `6`. Learn more in [Ping Identity End of Life (EOL) Software Tracker](https://support.pingidentity.com/s/article/Ping-Identity-EOL-Tracker#pgateway).

### `keyType` for CapturedUserPasswordFilter is required

For better security, the `keyType` for CapturedUserPasswordFilter is now required and the use of `DES` is deprecated.

### JWT classes relocated to new packages

Classes related to JWT-based sessions have moved from the `org.forgerock.openig.jwt` package to the `org.forgerock.openig.session.jwt` package.

Classes and functions used to validate a JWT with a JwtValidatorCustomizer in a JwtValidationFilter have moved from the `org.forgerock.openig.tools.jwt` package to the `org.forgerock.openig.tools.jwt.validation` package.

The IG scripting engine has been updated to incorporate the changes automatically.

### CDSSO requires session cookies with `SameSite=None`, `Secure=True`

To improve privacy, browsers have recently changed third-party cookie policies to require the following settings for session cookies: `SameSite=None`, `Secure=True`.

Depending on your deployment and route configuration, configure session cookies as follows:

* For in-memory sessions in standalone mode, by[admin.json](https://docs.pingidentity.com/pinggateway/7.2/reference/AdminHttpApplication.html).

* For in-memory sessions in web container mode, by the web container:

  * For Tomcat, learn more in [Configure SameSite for HTTP session cookies in Tomcat](https://docs.pingidentity.com/pinggateway/7.2/installation-guide/install-tomcat.html#tomcat-samesite) and [Configure IG for HTTPS (server-side) in Tomcat](https://docs.pingidentity.com/pinggateway/7.2/installation-guide/install-tomcat.html#tomcat-https).

  * For Jetty, learn more in [Configure SameSite for HTTP session cookies in Jetty](https://docs.pingidentity.com/pinggateway/7.2/installation-guide/install-jetty.html#jetty-samesite) and [Configure IG for HTTPS (server-side) in Jetty](https://docs.pingidentity.com/pinggateway/7.2/installation-guide/install-jetty.html#jetty-https).

  * For JBoss, learn more in [Configure SameSite for HTTP session cookies in JBoss](https://docs.pingidentity.com/pinggateway/7.2/installation-guide/install-jboss.html#jboss-samesite) and [Configure IG for HTTPS (server-side) in JBoss](https://docs.pingidentity.com/pinggateway/7.2/installation-guide/install-jboss.html#jboss-https).

* For JWT-based sessions in standalone mode and web container mode, by JwtSession.

---

---
title: Known issues
description: PingGateway known issues open at the time of each release, listed by version.
component: pinggateway
version: release-notes
page_id: pinggateway::known-issues
canonical_url: https://docs.pingidentity.com/pinggateway/release-notes/known-issues.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-22T12:00:00Z
section_ids:
  pinggateway_2026_6: PingGateway 2026.6
  pinggateway_2026_3: PingGateway 2026.3
  pinggateway_2025_11_2: PingGateway 2025.11.2
  pinggateway_2025_9: PingGateway 2025.9
  pinggateway_2025_6: PingGateway 2025.6
  pinggateway_2025_3: PingGateway 2025.3
  pinggateway_2024_11_2: PingGateway 2024.11.2
  pinggateway_2024_9: PingGateway 2024.9
  pinggateway_2024_6: PingGateway 2024.6
  ig_2024_3: IG 2024.3
  ig_2023_11_x: IG 2023.11.x
  ig_2023_11_2: IG 2023.11.2
  ig_2023_11_0: IG 2023.11.0
  ig_2023_9: IG 2023.9
  ig_2023_6: IG 2023.6
  ig_2023_4: IG 2023.4
  ig_2023_2: IG 2023.2
  ig_7_2_0: IG 7.2.0
---

# Known issues

The following important issues remained open at the time of the latest release for each version:

## PingGateway 2026.6

| Issue                                                                       | Comment                                                                                                                                                                                                                                          |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| OPENIG-10535: Startup prints "Failed to create the AnsiPrintStream" warning | PingGateway no longer supports Jansi in Logback to print colored log output on Windows systems. If `logback.xml` includes `<withJansi>true</withJansi>`, PingGateway now displays a warning on startup. Remove the setting to avoid the warning. |

## PingGateway 2026.3

No known issues at the time of release.

## PingGateway 2025.11.2

No known issues at the time of release.

## PingGateway 2025.9

No known issues at the time of release.

## PingGateway 2025.6

No known issues at the time of release.

## PingGateway 2025.3

No known issues at the time of release.

## PingGateway 2024.11.2

No known issues at the time of release.

## PingGateway 2024.9

No known issues at the time of release.

## PingGateway 2024.6

| Issue                                                                               | Comment         |
| ----------------------------------------------------------------------------------- | --------------- |
| OPENIG-8259: `ig_http_server_active_requests` metric shows negative values          | Fixed in 2024.9 |
| OPENIG-7296: In Studio, switching deployment status of a route makes it out of sync | Fixed in 2024.9 |

## IG 2024.3

| Issue                                                                               | Comment         |
| ----------------------------------------------------------------------------------- | --------------- |
| OPENIG-7296: In Studio, switching deployment status of a route makes it out of sync | Fixed in 2024.9 |

## IG 2023.11.x

### IG 2023.11.2

| Issue                                                                               | Comment         |
| ----------------------------------------------------------------------------------- | --------------- |
| OPENIG-7296: In Studio, switching deployment status of a route makes it out of sync | Fixed in 2024.9 |

### IG 2023.11.0

| Issue                                                                                               | Comment                    |
| --------------------------------------------------------------------------------------------------- | -------------------------- |
| OPENIG-7736: IG drops some bytes during POST and PUT of large data/images                           | Fixed in 2024.3, 2023.11.1 |
| OPENIG-7680: GzipFlowableTransformer fails when there is empty bytebuffer after actual gzip content | Fixed in 2024.3, 2023.11.1 |
| OPENIG-7296: In Studio, switching deployment status of a route makes it out of sync                 | Fixed in 2024.9            |

## IG 2023.9

| Issue                                                                                               | Comment          |
| --------------------------------------------------------------------------------------------------- | ---------------- |
| OPENIG-7736: IG drops some bytes during POST and PUT of large data/images                           | Fixed in 2024.3  |
| OPENIG-7680: GzipFlowableTransformer fails when there is empty bytebuffer after actual gzip content | Fixed in 2024.3  |
| OPENIG-7296: In Studio, switching deployment status of a route makes it out of sync                 | Fixed in 2024.9  |
| OPENIG-4817: Can't specify any host information for HTTP/2 request                                  | Fixed in 2023.11 |

## IG 2023.6

| Issue                                                                                               | Comment          |
| --------------------------------------------------------------------------------------------------- | ---------------- |
| OPENIG-7736: IG drops some bytes during POST and PUT of large data/images                           | Fixed in 2024.3  |
| OPENIG-7680: GzipFlowableTransformer fails when there is empty bytebuffer after actual gzip content | Fixed in 2024.3  |
| OPENIG-7296: In Studio, switching deployment status of a route makes it out of sync                 | Fixed in 2024.9  |
| OPENIG-5294: Clear Issuer cache on exception                                                        | Fixed in 2023.9  |
| OPENIG-4817: Can't specify any host information for HTTP/2 request                                  | Fixed in 2023.11 |

## IG 2023.4

| Issue                                                                               | Comment          |
| ----------------------------------------------------------------------------------- | ---------------- |
| OPENIG-7429: IG can't handle requests with IPv6 URL                                 | Fixed in 2023.6  |
| OPENIG-7296: In Studio, switching deployment status of a route makes it out of sync | Fixed in 2024.9  |
| OPENIG-5294: Clear Issuer cache on exception                                        | Fixed in 2023.9  |
| OPENIG-4817: Can't specify any host information for HTTP/2 request                  | Fixed in 2023.11 |

## IG 2023.2

| Issue                                                                              | Comment          |
| ---------------------------------------------------------------------------------- | ---------------- |
| OPENIG-5913 (UI) Route configuration lost sometime after un-deploy from route list | Fixed in 2023.4  |
| OPENIG-5294: Clear Issuer cache on exception                                       | Fixed in 2023.9  |
| OPENIG-4817: Can't specify any host information for HTTP/2 request                 | Fixed in 2023.11 |

## IG 7.2.0

| Issue                                                                              | Comment          |
| ---------------------------------------------------------------------------------- | ---------------- |
| OPENIG-5913 (UI) Route configuration lost sometime after un-deploy from route list | Fixed in 2023.4  |
| OPENIG-5294: Clear Issuer cache on exception                                       | Fixed in 2023.9  |
| OPENIG-4817: Can't specify any host information for HTTP/2 request                 | Fixed in 2023.11 |

---

---
title: Limitations
description: PingGateway inherent design limitations, including audit event handling and scripting constraints.
component: pinggateway
version: release-notes
page_id: pinggateway::limitations
canonical_url: https://docs.pingidentity.com/pinggateway/release-notes/limitations.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-09-08T10:08:23Z
section_ids:
  audit_events: Audit events
  filters: Filters
  handlers: Handlers
  http: HTTP
  saml: SAML
  scripts: Scripts
  streaming: Streaming
  studio: Studio
  uma: UMA
---

# Limitations

Limitations are inherent to the design, not bugs to be fixed.

## Audit events

* The log file of audit events can be overwritten when the log file is rotated.

  When a `CsvAuditEventHandler` is used to log audit events, PingGateway overwrites the log file if it is rotated before the `rotationFileSuffix` changes. By default, `rotationFileSuffix` is defined as a date in `_yyyy-MM-dd` format.

  PingGateway rotates log files when a `maxFileSize`, `rotationInterval`, or `rotationTimes` limit is reached.

  Set the log rotation parameters so the log isn't likely to rotate before `rotationFileSuffix` changes.

## Filters

* The `CookieFilter` isn't `JwtSession` compatible.

- The JWT created by `JwtBuilderFilter` isn't encrypted.

  Carefully consider the security of your configuration when using this filter.

* Filters can't use the value of `System.currentTimeMillis()`.

  This applies to `JwtBuilderFilter` for claims such as `exp` and `iat`.

- When a user has a pre-existing fragment cookie during authentication—​for example, from a previous, incomplete authentication attempt—​the pre-existing fragment overwrites the current fragment.

  To minimize the effect of this limitation, the `FragmentFilter` cookie has a `maxAge` property you can use to configure the maximum duration it can remain valid.

## Handlers

* ClientHandler blocks with asynchronous HTTP clients.

  |   |                                                                                                                                                 |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | This limitation applies only to the IG 7.2 and earlier deployments using the .war file. It doesn't apply to PingGateway standalone deployments. |

  PingGateway processes responses from asynchronous HTTP clients with two thread pools of the same size:

  * The first thread pool receives the response headers.

  * The second thread pool completes the promise by executing the callback and writing the response content to the stream. Reading and writing to the stream are synchronous, blocking operations.

  Synchronous operation can cause routes to declare a blocked ClientHandler. To recover from blocking, restart the route or, if the route is `config.json`, restart the server. To prevent blocking, increase the number of worker threads.

- The `ClientHandler` and `ReverseProxyHandler` property `systemProxy` can't be used with a proxy that requires a username and password. Use the handler's `proxy` property instead.

## HTTP

* PingGateway doesn't forward host information for HTTP/2 requests.

  When acting as a reverse proxy and receiving HTTP/2 requests, PingGateway doesn't forward the host information in the HTTP/2 `:authority:` pseudo-header to the protected application.

  If the protected application uses the HTTP/1.1 `Host` header or HTTP/2 `:authority:` pseudo-header to route requests, an error occurs.

- When acting as a client for HTTPS mutual authentication, the PingGateway client certificate isn't configurable.

  The client certificate must be the first in the `ClientHandler` or `ReverseProxyHandler` keystore.

## SAML

* When SAML is used with an AM policy agent, class cast exceptions occur.

- The `SamlFederationHandler` doesn't support filtering.

  |   |                                                                                                      |
  | - | ---------------------------------------------------------------------------------------------------- |
  |   | This limitation is mitigated by the SAML 2.0 requests processed with the original URI value feature. |

  Don't use a `SamlFederationHandler` as the handler for a `Chain`.

  More generally, don't use a `SamlFederationHandler` when its use depends on something in the response. The response can be handled independently of PingGateway and can be null when control returns to PingGateway. For example, don't use this handler in a `SequenceHandler` where the post-condition depends on the response.

* When the user defined mapping is incorrectly set, missing SAML assertions produce an infinite loop during authentication attempts.

## Scripts

* PingGateway scripts aren't sandboxed. They can access anything in their environment.

  Make sure all scripts PingGateway loads are safe.

## Streaming

* PingGateway requires you set the `admin.json` property `streamingEnabled` set to `true` to process files bigger than 2 GB and Server Sent Events.

## Studio

* Studio deploys and undeploys routes through a main router named `_router`, the name of the main router in the default configuration.

  If you use a custom `config.json`, make sure that it contains a main router named `_router`.

- To avoid undesirable side effects, Studio only lets you deploy or undeploy routes created and modified using Studio.

## UMA

* Shared resources don't persist across PingGateway restarts. They must be shared each time PingGateway restarts.

---

---
title: PingGateway release notes
description: PingGateway release notes covering multiple versions — quick links to new features, fixes, and upgrade information.
component: pinggateway
version: release-notes
page_id: pinggateway::preface
canonical_url: https://docs.pingidentity.com/pinggateway/release-notes/preface.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-09-08T10:08:23Z
keywords: ["Evaluation"]
section_ids:
  name_changes_for_forgerock_products: Name changes for ForgeRock products
---

# PingGateway release notes

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | These release notes cover multiple versions of PingGateway software. They make it easier to upgrade, especially when you are skipping releases.Some older versions have reached the end of support (EOS) or end of life (EOL). Learn more in [Ping Identity End of Life (EOL) Software Tracker](https://support.pingidentity.com/s/article/Ping-Identity-EOL-Tracker#pgateway). If you are still running an EOL version, upgrade as soon as possible to an actively maintained version. |

PingGateway integrates web applications, APIs, and microservices with the Ping Identity Platform. Based on reverse proxy architecture, PingGateway enforces security and access control.

[icon: newspaper, set=fad, size=3x]

#### [What's New](whats-new.html)

Discover new features.

[icon: cogs, set=fad, size=3x]

#### [Requirements](requirements.html)

Check prerequisites.

[icon: check-square, set=fad, size=3x]

#### [Compatibility](changes.html)

Review incompatible changes.

[icon: bug, set=fad, size=3x]

#### [Fixes](fixes.html)

Review bug fixes, limitations, known issues.

[icon: life-ring, set=fad, size=3x]

#### [Support](support.html)

Get support and training.

## Name changes for ForgeRock products

Product names changed when ForgeRock became part of Ping Identity.

The following name changes have been in effect since early 2024:

| Old name                      | New name                        |
| ----------------------------- | ------------------------------- |
| ForgeRock Identity Cloud      | PingOne Advanced Identity Cloud |
| ForgeRock Access Management   | PingAM                          |
| ForgeRock Directory Services  | PingDS                          |
| ForgeRock Identity Management | PingIDM                         |
| ForgeRock Identity Gateway    | PingGateway                     |

Learn more about the name changes in [New names for ForgeRock products](https://support.pingidentity.com/s/article/New-names-for-ForgeRock-products) in the Knowledge Base.

---

---
title: Release levels and interface stability
description: PingGateway release levels and interface stability labels — understand the stability guarantees for each interface.
component: pinggateway
version: release-notes
page_id: pinggateway::stability
canonical_url: https://docs.pingidentity.com/pinggateway/release-notes/stability.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-09-08T10:08:23Z
section_ids:
  interface-stability: Product stability labels
---

# Release levels and interface stability

Learn more about release levels in [Ping Identity End of Life (EOL) Software Tracker](https://support.pingidentity.com/s/article/Ping-Identity-EOL-Tracker#pgateway).

## Product stability labels

Ping Identity Platform software supports many features, protocols, APIs, GUIs, and command-line interfaces. Some of these are standard and very stable. Others offer new functionality that is continuing to evolve.

Ping Identity acknowledges you invest in these features and interfaces and so need to understand when they are expected to change. For that reason, we define stability labels and use these definitions in Ping Identity Platform products.

**Stability label definitions**

| Stability Label       | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Stable                | This documented feature or interface is expected to undergo backwards-compatible changes only for major releases.Changes may be announced at least one minor release before they take effect.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Evolving              | This documented feature or interface is continuing to evolve and so is expected to change, potentially in backwards-incompatible ways even in a minor release. Changes are documented at the time of product release.While new protocols and APIs are still in the process of standardization, they are Evolving. This applies, for example, to recent Internet-Draft implementations and to newly developed functionality.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Legacy                | This feature or interface has been replaced with an improved version, and is no longer receiving development effort from Ping Identity.You should migrate to the newer version, however the existing functionality will remain.Legacy features or interfaces will be marked as *Deprecated* if they are scheduled to be removed from the product.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Deprecated            | This feature or interface is deprecated, and likely to be removed in a future release.For previously stable features or interfaces, the change was likely announced in a previous release.Deprecated features or interfaces will be removed from Ping Identity products.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Removed               | This feature or interface was deprecated in a previous release, and has now been removed from the product.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Technology Preview    | Technology previews provide access to new features that are considered as new technology that is not yet supported. Technology preview features may be functionally incomplete, and the function as implemented is subject to change without notice.*DO NOT DEPLOY A TECHNOLOGY PREVIEW INTO A PRODUCTION ENVIRONMENT.*Customers are encouraged to test drive the technology preview features in a non-production environment, and are welcome to make comments and suggestions about the features in the associated forums.Ping Identity does not guarantee that a technology preview feature will be present in future releases, the final complete version of the feature is liable to change between preview and the final version. Once a technology preview moves into the completed version, said feature will become part of Ping Identity Platform.Technology previews are provided on an "AS-IS" basis for evaluation purposes only, and Ping Identity accepts no liability or obligations for the use thereof. |
| Internal/Undocumented | Internal and undocumented features or interfaces can change without notice.If you depend on one of these features or interfaces, contact support to discuss your needs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

---

---
title: Release timeline
description: PingGateway release timeline showing release dates, versions, and release types across major and maintenance releases.
component: pinggateway
version: release-notes
page_id: pinggateway::timeline
canonical_url: https://docs.pingidentity.com/pinggateway/release-notes/timeline.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-09T12:00:00Z
---

# Release timeline

| Release date | Version               | Release type(1) |
| ------------ | --------------------- | --------------- |
| 2026-06      | PingGateway 2026.6.0  | Minor           |
| 2026-05      | PingGateway 2025.11.2 | Maintenance     |
| 2026-05      | PingGateway 2024.11.2 | Maintenance     |
| 2026-03      | PingGateway 2026.3.0  | Major           |
| 2026-01      | PingGateway 2025.11.1 | Maintenance     |
| 2025-12      | PingGateway 2024.11.1 | Maintenance     |
| 2025-12      | PingGateway 2023.11.2 | Maintenance     |
| 2025-11      | PingGateway 2025.11.0 | Minor           |
| 2025-09      | PingGateway 2025.9.0  | Minor           |
| 2025-08      | PingGateway 2025.6.2  | Maintenance     |
| 2025-07      | PingGateway 2025.6.1  | Maintenance     |
| 2025-06      | PingGateway 2025.6.0  | Minor           |
| 2025-03      | PingGateway 2025.3.0  | Major           |
| 2024-11      | PingGateway 2024.11.0 | Minor           |
| 2024-09      | PingGateway 2024.9.0  | Minor           |
| 2024-06      | PingGateway 2024.6.0  | Minor           |
| 2024-04      | IG 2023.11.1          | Maintenance     |
| 2024-03      | IG 2024.3.0           | Major           |
| 2023-11      | IG 2023.11.0          | Minor           |
| 2023-09      | IG 2023.9.0           | Minor           |
| 2023-06      | IG 2023.6.0           | Minor           |
| 2023-04-25   | IG 2023.4.0           | Minor           |
| 2023-02-21   | IG 2023.2.0           | Major           |
| 2022-06-28   | IG 7.2.0              | Minor           |
| 2022-04-06   | IG 7.1.2              | Maintenance     |
| 2021-09-24   | IG 7.1.1              | Maintenance     |
| 2022-05-11   | IG 7.1.0              | Minor           |
| 2021-03-16   | IG 7.0.2              | Maintenance     |
| 2021-03-12   | IG 6.5.4              | Maintenance     |
| 2020-10-27   | IG 7.0.1              | Maintenance     |
| 2020-09-24   | IG 6.5.3              | Maintenance     |
| 2020-08-07   | IG 7.0.0              | Major           |
| 2019-11-27   | IG 6.5.2              | Maintenance     |
| 2019-11-18   | IG 5.5.2              | Maintenance     |
| 2019-04-07   | IG 6.5.1              | Maintenance     |
| 2018-12-18   | IG 5.5.1              | Maintenance     |
| 2018-11-28   | IG 6.5.0              | Minor           |
| 2018-06-15   | IG 6.1.0              | Minor           |
| 2018-05-08   | IG 6.0.0              | Major           |
| 2017-10-19   | IG 5.5.0              | Minor           |
| 2017-04-03   | OpenIG 5              | Major           |
| 2016-01-27   | OpenIG 4              | Major           |
| 2014-08-11   | OpenIG 3              | Major           |
| 2012-05-15   | OpenIG 2.1            | Minor           |

(1) Learn about the scope of expected changes for different release types [Ping Identity End of Life (EOL) Software Tracker](https://support.pingidentity.com/s/article/Ping-Identity-EOL-Tracker#pgateway).

---

---
title: Removed
description: PingGateway removed features and properties by version, with deprecation versions and replacement settings.
component: pinggateway
version: release-notes
page_id: pinggateway::removed
canonical_url: https://docs.pingidentity.com/pinggateway/release-notes/removed.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-09T12:00:00Z
section_ids:
  2026_6: 2026.6
  2026_3: 2026.3
  2025_11: 2025.11
  2025_9: 2025.9
  2025_6: 2025.6
  2025_3: 2025.3
  2024_11: 2024.11
  2024_9: 2024.9
  2024_6: 2024.6
  2024_3: 2024.3
  2023_11: 2023.11
  2023_9: 2023.9
  2023_6: 2023.6
  2023_4: 2023.4
  2023_2: 2023.2
  7_2: 7.2
---

# Removed

The listed features and properties have been removed.

## 2026.6

No removals.

## 2026.3

**PingGateway features**

| Feature or property                                                                                                           | Setting                                                                                                                        | Replacement setting                                                                                                                                                                     | Deprecated in |
| ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| Fields defined as `"properties"` in `admin.json`, `config.json`, and route configuration files using `$location` expressions. | Use of ISO-8859-1 encoded text by default.                                                                                     | Use UTF-8 encoded text instead.To use deprecated ISO-8859-1 encoding, set the deprecated system property `org.forgerock.config.resolvers.properties.encoding` to `ISO-8859-1`.          | 2025.9        |
| The `IG_ENVCONFIG_DIRS` environment variable and the `ig.envconfig.dirs` system property.                                     |                                                                                                                                |                                                                                                                                                                                         |               |
| Any `.properties` files accessed with the `readProperties()` function.                                                        |                                                                                                                                |                                                                                                                                                                                         |               |
| The liveness and readiness endpoints                                                                                          | Deprecated endpoints:- `health/liveness`

- `health/readiness`                                                                 | Use these endpoints instead:- `health/live`

- `health/ready`                                                                                                                           | 2025.9        |
| AuthorizationCodeOAuth2ClientFilter                                                                                           | `target` (default: `${attributes.openid}`)                                                                                     | Use [${contexts.oauth2Info}](https://docs.pingidentity.com/pinggateway/2026/reference/OAuth2InfoContext.html) instead.                                                                  | 2023.11       |
|                                                                                                                               | Getting the target URI from `request.uri` or `contexts.router.originalUri`                                                     | `contexts.idpSelectionLogin.originalUri`                                                                                                                                                | 2023.9        |
| CapturedUserPasswordFilter                                                                                                    | A `GenericSecret` shared key                                                                                                   | A `CryptoKey` shared key                                                                                                                                                                | 2023.2        |
| CookieFilter                                                                                                                  | Use of the `Set-Cookie2` HTTP header, obsoleted by [RFC 6265: Set-Cookie2](https://www.rfc-editor.org/rfc/rfc6265#section-9.4) | None                                                                                                                                                                                    | 2023.4        |
| FapiAuditContext                                                                                                              | Whole object                                                                                                                   | AccessAuditExtensionContext                                                                                                                                                             | -             |
| HsmSecretStore                                                                                                                | property `storePassword`                                                                                                       | property `storePasswordSecretId`                                                                                                                                                        | 2023.2        |
| Java support                                                                                                                  | Java 17                                                                                                                        | Java 21                                                                                                                                                                                 | 2025.3        |
| KeyManager                                                                                                                    | Whole object                                                                                                                   | SecretsKeyManager                                                                                                                                                                       | 2023.2        |
| KeyStore                                                                                                                      | Whole object                                                                                                                   | KeyStoreSecretsStore                                                                                                                                                                    | 2023.2        |
| KeyStoreSecretStore                                                                                                           | Required property `storePassword` Optional property `keyEntryPassword`                                                         | Optional property `storePasswordSecretId` Optional property `entryPasswordSecretId`                                                                                                     | 2023.2        |
| Names of Prometheus counter metrics                                                                                           | Counter metrics with names not ending in `_total`.                                                                             | Use the new names, which end in `_total`.                                                                                                                                               | 2023.2        |
| Names of Vert.x counter metrics                                                                                               | Counter metrics with names not ending in `_total`.                                                                             | Use the new names, which end in `_total`.                                                                                                                                               | 2023.2        |
| PolicyEnforcementFilter                                                                                                       | `useLegacyAdviceEncoding`                                                                                                      | No replacement necessary                                                                                                                                                                | 2023.6        |
| Router                                                                                                                        | `scanInterval` as an integer                                                                                                   | Set `scanInterval` as a duration.                                                                                                                                                       | 5.0           |
| SamlFederationHandler                                                                                                         | Whole object                                                                                                                   | SamlFederationFilter                                                                                                                                                                    | 2023.4        |
| TrustManager                                                                                                                  | Whole object                                                                                                                   | SecretsTrustManagerFind examples in the [SecretsTrustManager reference](https://docs.pingidentity.com/pinggateway/2026/reference/SecretsTrustManager.html#SecretsTrustManager-example). | 2023.2        |
| Vert.x                                                                                                                        | In `admin.json`: `vertx` > `maxHeaderSize` `vertx` > `initialSettings` > `maxHeaderListSize`                                   | Use `adminConnector` > `maxTotalHeadersSize` or `connectors` > `maxTotalHeadersSize` instead.                                                                                           | 2023.6        |

## 2025.11

No removals.

## 2025.9

No removals.

## 2025.6

No removals.

## 2025.3

This release no longer supports AM 7.1 and earlier (deprecated in 2023.2).

**PingGateway features**

| Feature or property                          | Setting                                                                                                                    | Replacement setting                                                      | Deprecated in |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | ------------- |
| CapturedUserPasswordFilter                   | `keyType`                                                                                                                  | None; the filter expects a password encrypted with AES                   | 7.2           |
| ClientCredentialsOAuth2ClientFilter          | `clientId`, `clientSecretId`, `handler`                                                                                    | `endpointHandler`                                                        | 7.2           |
| ClientHandler                                | `hostnameVerifier`                                                                                                         | Set the `hostnameVerifier` in the ClientTlsOptions of the `tls` setting. | 7.2           |
|                                              | `proxy` and `systemProxy`                                                                                                  | `proxyOptions`                                                           | 7.2           |
| ClientRegistration                           | `clientSecretUsage` `jwtExpirationTimeout` `privateKeyJwtSecretId` `tokenEndpointAuthMethod` `tokenEndpointAuthSigningAlg` | `authenticatedRegistrationHandler`                                       | 7.2           |
| CorsFilter                                   | `origins`                                                                                                                  | `acceptedOrigins`                                                        | 7.1           |
| CsvAuditEventHandler                         | `security`                                                                                                                 | None                                                                     | -             |
| ElasticsearchAuditEventHandler               | Whole object                                                                                                               | None                                                                     | 7.1           |
| Functions                                    | `matches()` and `matchingGroups()`                                                                                         | None                                                                     | 7.1           |
| IdentityAssertionHandlerTechPreview          | Whole object                                                                                                               | IdentityAssertionHandler                                                 | -             |
| OAuth2ClientFilter                           | Whole object                                                                                                               | AuthorizationCodeOAuth2ClientFilter                                      | 7.2           |
| ReverseProxyHandler                          | `hostnameVerifier`                                                                                                         | Set the `hostnameVerifier` in the ClientTlsOptions of the `tls` setting. | 7.2           |
|                                              | `proxy` and `systemProxy`                                                                                                  | `proxyOptions`                                                           | 7.2           |
| ScriptableIdentityAssertionPluginTechPreview | Whole object                                                                                                               | ScriptableIdentityAssertionPlugin                                        | -             |
| SplunkAuditEventHandler                      | Whole object                                                                                                               | None                                                                     | 7.1           |

The following filters and handlers are no longer instantiable in PingGateway scripts. If you can't configure them the way you want to, write your own similar `ScriptableFilter` or `ScriptableHandler`:

* `AssignmentFilter`

* `EntityExtractFilter`

* `HeaderFilter`

* `LocationHeaderFilter`

* `StaticRequestFilter`

* `SwitchFilter`

* `DispatchHandler`

* `SequenceHandler`

* `StaticResponseHandler`

## 2024.11

No removals.

## 2024.9

No removals.

## 2024.6

No removals

## 2024.3

| Feature or property                     | Setting                                                                                                                | Replacement setting                                                                        | Deprecated in  |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | -------------- |
| IG product                              | Creation of a .war file                                                                                                | .zip file                                                                                  | 6              |
| SingleSignOnFilter                      | `logoutEndpoint`                                                                                                       | `logoutExpression`                                                                         | 7              |
| Java support                            | Java 11                                                                                                                | Java 17                                                                                    | 2023.11        |
| JwtSession                              | `encryptionSecretId`, `signatureSecretId`,`cookieName`, `cookieDomain`,`password`, `alias`, `keystore`, `sharedSecret` | `authenticatedEncryptionSecretId`, `encryptionMethod`, `cookie`                            | 7, 6.5         |
| OpenAmAccessTokenResolver               | Whole object                                                                                                           | None                                                                                       | 7              |
| JwtBuilderFilter                        | Use of unsigned or unencrypted JWTs                                                                                    | Use of signed or encrypted JWTs                                                            | 7              |
| GrantSwapJwtAssertionOAuth2ClientFilter | Use of unsigned or unencrypted JWTs                                                                                    | Use of signed or encrypted JWTs                                                            | Not deprecated |
| CryptoHeaderFilter                      | Whole object                                                                                                           | JwtBuilderFilter                                                                           | 7              |
| Ldap                                    | `LdapClient` class and the `ldap` script binding                                                                       | None                                                                                       | 7.1            |
| KeyManager                              | `password`                                                                                                             | `passwordSecretId`                                                                         | 6.5            |
| CapturedUserPasswordFilter              | `key`                                                                                                                  | `keySecretId`                                                                              | 7              |
| PasswordReplayFilter                    | `headerDecryption`                                                                                                     | PasswordReplayFilter's `credentials` property configured with a CapturedUserPasswordFilter | 7              |
| KeyStore                                | `password`                                                                                                             | `passwordSecretId`                                                                         | 7              |
| DesKeyGenHandler                        | Whole object                                                                                                           | None                                                                                       | 7              |
| SqlAttributesFilter                     | `dataSource` as a JNDI lookup name                                                                                     | `dataSource` as a `JdbcDataSource` configuration object                                    | 7              |
| AmService                               | `agent` subproperty `password`                                                                                         | `agent` subproperty `passwordSecretId`                                                     | 6.5            |
| TlsOptions                              | Whole object                                                                                                           | ClientTlsOptions                                                                           | 7              |
| ClientHandler and ReverseProxyHandler   | `proxy` subproperty `password`                                                                                         | `proxy` subproperty `passwordSecretId`                                                     | 7              |
| JwtBuilderFilter                        | `signature` subproperties:- `keystore`

- `alias`

- `password`                                                        | `signature` subproperty `secretId`                                                         | 6.5            |
| AuditService                            | `event-handlers`                                                                                                       | `eventHandlers`                                                                            | 7              |
| ClientRegistration                      | `keystore` `privateKeyJwtAlias` `privateKeyJwtPassword`                                                                | `privateKeyJwtSecretId`                                                                    | 7              |
|                                         | `clientSecret`                                                                                                         | `clientSecretId`                                                                           | 7              |
|                                         | The name of the ClientRegistration heaplet to identify a client registration when a user initiates a login             | The `clientId` property of ClientRegistration                                              | 7              |
| Route                                   | `secrets`                                                                                                              | A `secretsProvider` configuration in each affected object                                  | 7              |

## 2023.11

No removals.

## 2023.9

No removals.

## 2023.6

No removals.

## 2023.4

No removals.

## 2023.2

| Feature or property                      | Setting                                                                                   | Replacement setting                                  | Deprecated in |
| ---------------------------------------- | ----------------------------------------------------------------------------------------- | ---------------------------------------------------- | ------------- |
| IG product                               | Delivery of a .war file                                                                   | .zip file                                            | 6             |
| Environment variable and system property | `OPENIG_BASE` `openig.base`                                                               | `IG_INSTANCE_DIR` `ig.instance.dir`                  | 6             |
| PolicyEnforcementFilter                  | `executor`                                                                                | `cache` subproperty `executor`                       | 6             |
| ClientHandler and ReverseProxyHandler    | `keyManager` `sslCipherSuites` `sslContextAlgorithm` `sslEnabledProtocols` `trustManager` | `tls` property to define a ClientTlsOptions object   | 6.5           |
| UserProfileFilter                        | `ssoToken`                                                                                | `username`                                           | 6.5           |
|                                          | `profileAttributes`                                                                       | `userProfileService` subproperty `profileAttributes` | 6.5           |
|                                          | `amService`                                                                               | `userProfileService` subproperty `amService`         | 6.5           |
| StatelessAccessTokenResolver             | `signatureSecretId`                                                                       | `verificationSecretId`                               | 6.5.1         |
|                                          | `encryptionSecretId`                                                                      | `decryptionSecretId`                                 | 6.5.1         |

## 7.2

| Feature or property   | Setting   | Replacement setting | Deprecated in  |
| --------------------- | --------- | ------------------- | -------------- |
| StaticResponseHandler | `version` | Not replaced        | Not deprecated |

---

---
title: Requirements
description: PingGateway system requirements including supported Java versions, operating systems, and browser compatibility.
component: pinggateway
version: release-notes
page_id: pinggateway::requirements
canonical_url: https://docs.pingidentity.com/pinggateway/release-notes/requirements.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-30T12:00:00Z
page_aliases: ["before-you-install.adoc"]
section_ids:
  prerequisites-download: Downloads
  prerequisites-operating-systems: Operating systems
  prerequisites-java: Java
  prerequisites-http-protocol: HTTP protocol
  prerequisites-fqdn: FQDNs
  prerequisites-ssl: Certificates
  prerequisites-third-party-encry-sw: Third-party software for encryption
  commons-third-party: Third-party software
  prerequisites-browser: Studio browser
  prerequisites-minimum-supported-versions: Minimum supported versions
  prerequisites-am-features: Features requiring later versions of PingAM
---

# Requirements

|   |                                                                                                                                                                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Ping Identity supports customers who use the versions specified here. Other versions and alternative environments might work as well. When opening a support ticket for an issue, however, make sure you can also reproduce the problem on a combination covered here. |

## Downloads

Download product software from the [Ping Identity Download Center](https://product-downloads.pingidentity.com/):

| File                                          | Description                                                    |
| --------------------------------------------- | -------------------------------------------------------------- |
| `PingGateway-2026.6.0.zip`                    | Cross-platform distribution including all software components. |
| `PingGateway-sample-application-2026.6.0.jar` | Web application for testing PingGateway configurations         |

Learn more about using the Docker image provided with the product software in [Deploy with Docker](https://docs.pingidentity.com/pinggateway/2026/devops-guide/preface.html).

## Operating systems

**PingGateway 2025.x and 2026.x** software is supported on actively maintained versions of the following Linux operating systems:

* Amazon Linux

* Debian

* Red Hat Enterprise Linux

* Rocky Linux

* SUSE Linux Enterprise

* Ubuntu Linux

**PingGateway 2025.x and 2026.x** software is supported on Microsoft Windows Server 2016, 2019, and 2022.

**PingGateway 2024.11 and earlier** software is supported on the following operating systems:

|                          | PingGateway version |              |                  |
| ------------------------ | ------------------- | ------------ | ---------------- |
| Vendor                   | 7.2                 | 2023.x       | 2024.x           |
| Amazon Linux             | (Not supported)     | 2, 2023      |                  |
| Red Hat Enterprise Linux | 7, 8                | 7, 8, 9      |                  |
| Centos OS                | 7                   |              |                  |
| Ubuntu LTS               | 20.04               | 22.04, 20.04 |                  |
| Windows Server           | 2016, 2019          |              | 2016, 2019, 2022 |
| SUSE Linux Enterprise    | 12, 15              |              |                  |
| Rocky Linux              | (Not supported)     |              | 9.x              |

## Java

PingGateway supports OpenJDK, including OpenJDK-based distributions:

* AdoptOpenJDK/Eclipse Adoptium

* Amazon Corretto

* Azul Zulu

* Oracle Java

* Red Hat OpenJDK

Ping Identity tests PingGateway the most extensively with Eclipse Adoptium.

**Supported Java versions**

| PingGateway version | 7.2 | 2023.x | 2024.x | 2025.x    | 2026.x |
| ------------------- | --- | ------ | ------ | --------- | ------ |
| Java version        | 11  | 17, 11 | 21, 17 | 21, 17(1) | 25, 21 |

(1) Java 17 is deprecated in 2025.3.

Recommendations:

* Use the HotSpot JVM.

* Keep your Java installation updated with the latest security fixes.

* Java 11 is the earliest long-term supported (LTS) Java version for IG 2023.11 and earlier versions. Earlier versions of Java don't contain required cryptography fixes. If you are using an earlier version of Java, secure your installation.

## HTTP protocol

HTTP/1.1 and HTTP/2.0 are supported. HTTP/1.0 isn't supported.

## FQDNs

When applications access PingGateway directly without going through a load balancer, use a fully qualified domain name (FQDN) like `gateway.example.com`. The applications use the FQDN, for example, when redirecting for OAuth 2.0 or CDSSO. Browser cookies can use the FQDN as well.

When using an FQDN in production, ensure DNS correctly provides it. Alternatively, update the hosts files on all the systems that access PingGateway to (`/etc/hosts` or `C:\Windows\System32\drivers\etc\hosts`) to set the PingGateway FQDN.

## Certificates

For secure network communications with client applications you don't control, install a properly signed digital certificate that your client applications recognize, such as one that works with your organization's PKI or one signed by a recognized CA.

To use the certificate during installation, include the certificate in a file-based keystore supported by the JVM (JKS, JCEKS, PKCS#12) or on a PKCS#11 token. To import a signed certificate into the server keystore, use the Java `keytool` command.

## Third-party software for encryption

Bouncy Castle is required for signature encryption with RSASSA-PSS or Deterministic ECDSA. Learn more at [The Legion of the Bouncy Castle](https://www.bouncycastle.org).

## Third-party software

Ping Identity provides support for using the following third-party software when logging common audit events:

| Software                      | Version              |
| ----------------------------- | -------------------- |
| Java Message Service (JMS)    | 2.0 API              |
| MySQL JDBC Driver Connector/J | 8 (at least 8.0.19)  |
| Splunk                        | 8.0 (at least 8.0.2) |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Elasticsearch and Splunk have native or third-party tools to collect, transform, and route logs. Examples include [Logstash](https://www.elastic.co/logstash) and [Fluentd](https://www.fluentd.org/).Use these alternatives if possible. These tools have advanced, specialized features focused on getting log data into the target system. They decouple the solution from the Ping Identity Platform systems and version, and provide inherent persistence and reliability. You can configure the tools to avoid losing audit messages if a Ping Identity Platform service goes offline, or delivery issues occur.These tools can work with common audit logging:- Configure the server to log messages to standard output, and route from there.

- Configure the server to log to files, and use log collection and routing for the log files. |

Ping Identity provides support for using the following third-party software when monitoring servers:

| Software   | Version            |
| ---------- | ------------------ |
| Grafana    | 5 (at least 5.0.2) |
| Graphite   | 1                  |
| Prometheus | 2.0                |

For hardware security module (HSM) support, Ping Identity Platform software requires a client library that conforms to the PKCS#11 standard v2.20 or later.

## Studio browser

Ping Identity tests Studio with many browsers, including the latest stable version of Chrome.

## Minimum supported versions

| Software     | Minimum supported version |
| ------------ | ------------------------- |
| PingAM       | 7.2                       |
| PingFederate | 13                        |

## Features requiring later versions of PingAM

| Feature                                                                                                                 | Minimum version of AM |
| ----------------------------------------------------------------------------------------------------------------------- | --------------------- |
| [Session cache eviction](https://docs.pingidentity.com/pinggateway/2026/gateway-guide/sso-cdsso.html#session-eviction). | AM 7.3                |

---

---
title: What&#8217;s new
description: New features and enhancements in PingGateway, listed by version from 7.2 onwards.
component: pinggateway
version: release-notes
page_id: pinggateway::whats-new
canonical_url: https://docs.pingidentity.com/pinggateway/release-notes/whats-new.html
llms_txt: https://docs.pingidentity.com/pinggateway/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-04-21T12:00:00Z
section_ids:
  whats-new-2026.6: PingGateway 2026.6
  support_for_oauth_2_0_as_issuer_identification_and_mix_up_mitigation: Support for OAuth 2.0 AS issuer identification and mix-up mitigation
  support_for_mcp_version_2025_11_25: Support for MCP version 2025-11-25
  improved_mcp_audit_events: Improved MCP audit events
  pingam_sessions_traced_in_audit_logs: PingAM sessions traced in audit logs
  documentation_for_using_pinggateway_with_pingfederate: Documentation for using PingGateway with PingFederate
  kubernetes_and_helm_deployment_for_fapi: Kubernetes and Helm deployment for FAPI
  whats-new-2026.3: PingGateway 2026.3
  pingauthorize_support: PingAuthorize support
  auditing_for_administrative_endpoints: Auditing for administrative endpoints
  opentelemetry_logging: OpenTelemetry logging
  custom_login_pages: Custom login pages
  fapi_and_custom_data_audit_logging: FAPI and custom data audit logging
  file_permissions_in_jsonauditeventhandler: File permissions in JsonAuditEventHandler
  whats-new-2025.11: PingGateway 2025.11.x
  2025_11_2: 2025.11.2
  file_permissions_in_jsonauditeventhandler_2: File permissions in JsonAuditEventHandler
  additional_filter_support_for_well_known_endpoints_with_mcp: Additional filter support for well-known endpoints with MCP
  2025_11_1: 2025.11.1
  mcp_support: MCP support
  2025_11_0: 2025.11.0
  improvements_to_fapi_support: Improvements to FAPI support
  help_switching_to_pingone_advanced_identity_cloud: Help switching to PingOne Advanced Identity Cloud
  reloadable_route_properties: Reloadable route properties
  ensure_all_routes_load_successfully: Ensure all routes load successfully
  configurable_maximum_for_websocket_connections: Configurable maximum for WebSocket connections
  whats-new-2025.9: PingGateway 2025.9
  fapi_support: FAPI support
  graceful_shutdown: Graceful shutdown
  custom_algorithm_setting_for_jwksethandler: Custom algorithm setting for JwkSetHandler
  configuration_conditions: Configuration conditions
  whats-new-2025.6: PingGateway 2025.6.x
  pinggateway_2025_6_2: PingGateway 2025.6.2
  pinggateway_2025_6_1: PingGateway 2025.6.1
  pinggateway_2025_6: PingGateway 2025.6
  new_startup_readiness_endpoint: New startup readiness endpoint
  specify_the_journey_to_authenticate_to_am: Specify the journey to authenticate to AM
  audit_session_cache_clearing_events: Audit session cache clearing events
  limit_http_request_body_size: Limit HTTP request body size
  whats-new-2025.3: PingGateway 2025.3
  use_bouncy_castle_fips: Use Bouncy Castle FIPS
  offload_tls_handshakes: Offload TLS handshakes
  close_connections_gracefully: Close connections gracefully
  custom_unauthorized_responses_for_kerberos: Custom unauthorized responses for Kerberos
  opentelemetry_now_supported: OpenTelemetry now supported
  whats-new-2024.11: PingGateway 2024.11.x
  pinggateway_2024_11_2: PingGateway 2024.11.2
  pinggateway_2024_11_1: PingGateway 2024.11.1
  pinggateway_2024_11_0: PingGateway 2024.11.0
  device_profile_support_for_risk_evaluation: Device profile support for risk evaluation
  pkce_support_for_oauth_2_0_clients: PKCE support for OAuth 2.0 clients
  graceful_shutdown_2: Graceful shutdown
  lifetime_for_cdsso_sessions: Lifetime for CDSSO sessions
  propagate_disconnections: Propagate disconnections
  support_for_der_certificates: Support for DER certificates
  more_flexible_amsessionidletimeoutfilter_settings: More flexible AmSessionIdleTimeoutFilter settings
  whats-new-2024.9: PingGateway 2024.9
  opentelemetry_capabilities: OpenTelemetry capabilities
  multiple_versions_of_a_secret_with_filesystemsecretstore: Multiple versions of a secret with FileSystemSecretStore
  replace_setting_for_headerfilter: Replace setting for HeaderFilter
  runtime_exception_condition_for_retries: Runtime exception condition for retries
  security_provider_setting_for_keystores: Security provider setting for keystores
  delayed_route_metrics_creation: Delayed route metrics creation
  separate_endpoint_for_administration: Separate endpoint for administration
  new_pingone_authorize_example: New PingOne Authorize example
  asynchronous_reads_in_fileattributesfilter_and_sqlattributesfilter: Asynchronous reads in FileAttributesFilter and SqlAttributesFilter
  whats-new-2024.6: PingGateway 2024.6
  ig_becomes_pinggateway: IG becomes PingGateway
  pingone_protect_integration: PingOne Protect integration
  changes_to_the_prometheus_scrape_endpoint: Changes to the Prometheus Scrape Endpoint
  new_metrics_at_the_prometheus_scrape_endpoint: New metrics at the Prometheus Scrape Endpoint
  pingoneapiaccessmanagementfilter_now_supported: PingOneApiAccessManagementFilter now supported
  hardened_security_for_openid_connect_id_tokens: Hardened security for OpenID Connect ID tokens
  whats-new-2024.3: IG 2024.3
  local_authentication_on_behalf_of_pingone_advanced_identity_cloud_and_kerberos_validation: Local authentication on behalf of PingOne Advanced Identity Cloud and Kerberos validation
  monitoring_of_caches: Monitoring of caches
  use_of_secrets_in_studio: Use of secrets in Studio
  use_of_splunk_or_elasticsearch_audit_event_handlers_in_studio: Use of Splunk or ElasticSearch audit event handlers in Studio
  hardened_security_for_secrets: Hardened security for secrets
  issuerrepository: IssuerRepository
  dedicated_filter_for_pingones_api_access_management_technology_preview: Dedicated filter for PingOne's API Access Management (Technology preview)
  whats-new-2023.111: IG 2023.11.x
  ig_2023_11_2: IG 2023.11.2
  ig_2023_11_1: IG 2023.11.1
  ig_2023_11_0: IG 2023.11.0
  general_features: General features
  harden_oauth_2_0_access_token_requests: Harden OAuth 2.0 access token requests
  include_key_id_in_jwt_header: Include key ID in JWT header
  local_processing_on_behalf_of_pingone_advanced_identity_cloud_technology_preview: Local processing on behalf of PingOne Advanced Identity Cloud (Technology preview)
  secret_format_jwkpropertyformat: Secret format JwkPropertyFormat
  more_flexible_use_of_ca_certificates_in_mutual_tls: More flexible use of CA-certificates in mutual TLS
  safeguard_against_accidental_exposure_of_private_keys_with_jwksethandler: Safeguard against accidental exposure of private keys with JwkSetHandler
  saml: SAML
  prevention_of_redirect_loops_when_session_cookies_arent_present_in_the_saml_flow: Prevention of redirect loops when session cookies aren't present in the SAML flow
  whats-new-2023.9: IG 2023.9
  revocation_of_access_tokens_initiated_by_oauth_2_0_resource_servers: Revocation of access tokens initiated by OAuth 2.0 Resource Servers
  logout_initiated_by_openid_connect_relying_parties: Logout initiated by OpenID Connect relying parties
  option_to_require_the_authorization_server_to_prompt_the_end_user_to_reauthenticate_and_consent: Option to require the Authorization Server to prompt the end-user to reauthenticate and consent
  improved_error_handling_for_authorizationcodeoauth2clientfilter: Improved error handling for AuthorizationCodeOAuth2ClientFilter
  new_context_for_use_with_authorizationcodeoauth2clientfilter: New context for use with AuthorizationCodeOAuth2ClientFilter
  improved_security_for_crossdomainsinglesignonfilter: Improved security for CrossDomainSingleSignOnFilter
  whats-new-2023.6: IG 2023.6
  large_jwt_session_cookies_are_automatically_split: Large JWT session cookies are automatically split
  jwt_session_cookies_not_compressed_by_default: JWT session cookies not compressed by default
  startup_allowed_if_there_is_an_existing_pid_file: Startup allowed if there is an existing PID file
  prevention_of_redirect_loops_when_session_cookies_arent_present_in_the_cdsso_flow: Prevention of redirect loops when session cookies aren't present in the CDSSO flow
  regex_based_alias_selection_in_keystoresecretstore_and_hsmsecretstore: Regex-based alias selection in KeyStoreSecretStore and HsmSecretStore
  entity_of_staticresponsehandler_can_be_an_array_of_strings: Entity of StaticResponseHandler can be an array of strings
  maximum_size_for_the_sum_of_all_request_headers: Maximum size for the sum of all request headers
  support_for_unencoded_policy_advices: Support for unencoded policy advices
  configure_forward_proxies_for_websocket_connections: Configure forward proxies for WebSocket connections
  improved_control_of_websocket_connections_to_am: Improved control of WebSocket connections to AM
  whats-new-2023.4: IG 2023.4
  authentication_of_ig_agent_to_pingone_advanced_identity_cloud_and_am: Authentication of IG agent to PingOne Advanced Identity Cloud and AM
  policy_advices_from_pingone_advanced_identity_cloud_and_am_available_in_a_header: Policy advices from PingOne Advanced Identity Cloud and AM available in a header
  saml_2: SAML
  websocket_connection_renewal: WebSocket connection renewal
  limit_side_effects_when_backend_applications_are_slow: Limit side effects when backend applications are slow
  route_id_included_access_audit_events: Route ID included access audit events
  whats-new-2023.2: IG 2023.2
  session_eviction: Session eviction
  preserve_post_data_during_authentication: Preserve POST data during authentication
  prevent_unnecessary_session_expiry: Prevent unnecessary session expiry
  captureduserpasswordfilter_supports_secret_rotation: CapturedUserPasswordFilter supports secret rotation
  keystoresecretstore_allows_unprotected_keystores: KeyStoreSecretStore allows unprotected KeyStores
  delay_destroying_httpclienthandlerheaplets_during_shutdown: Delay destroying HttpClientHandlerHeaplets during shutdown
  automatic_reload_of_filesystemsecretstore_and_keystoresecretstore: Automatic reload of FileSystemSecretStore and KeystoreSecretStore
  groovy_4: Groovy 4
  expression_binding_now: Expression binding now
  whats-new-7.2: IG 7.2
  Token-exchange: Token exchange
  Authentication: Connectivity with OAuth 2.0-protected third-party services
  oauth2clientfilter_renamed_as_authorizationcodeoauth2clientfilter: OAuth2ClientFilter renamed as AuthorizationCodeOAuth2ClientFilter
  clientcredentialsoauth2clientfilter_uses_client_secret_basic_or_client_secret_post: ClientCredentialsOAuth2ClientFilter uses client_secret_basic or client_secret_post
  resourceowneroauth2clientfilter_for_services_to_access_resources_protected_by_oauth_2_0: ResourceOwnerOAuth2ClientFilter for services to access resources protected by OAuth 2.0
  filters_to_support_oauth_2_0_client_authentication: Filters to support OAuth 2.0 client authentication
  oauth_2_0_session_sharing_across_routes: OAuth 2.0 session sharing across routes
  Circuit-breaking: Circuit breaking
  circuitbreakerfilter: CircuitBreakerFilter
  circuit_breaker_in_clienthandler_and_reverseproxyhandler: Circuit breaker in ClientHandler and ReverseProxyHandler
  stability: Stability
  jwtbuilderfilter_produces_encrypted_jwt: JwtBuilderFilter produces encrypted JWT
  jwtsession_cookie_compression: JwtSession cookie compression
  other: Other
  windows_start_script_for_ig_in_standalone_mode: Windows start script for IG in standalone mode
  stop_scripts_for_ig_in_standalone_mode: Stop scripts for IG in standalone mode
  ig_opts_environment_variables_for_startup: IG_OPTS environment variables for startup
  sni_to_serve_different_certificates_for_tls_connections_to_different_server_names: SNI to serve different certificates for TLS Connections to different server names
  ig_proxies_all_websocket_subprotocols_by_default: IG proxies all WebSocket subprotocols by default
  configurable_conditions_for_retries_in_clienthandler_and_reverseproxyhandler: Configurable conditions for retries in ClientHandler and ReverseProxyHandler
  user_id_in_audit_logs: User ID in audit logs
  tracking_id_logged_in_access_audit_events: Tracking ID logged in access audit events
  transformation_from_string_to_placeholder_string: Transformation from string to placeholder string
  use_expressions_to_configure_paths_in_uripathrewritefilter: Use expressions to configure paths in UriPathRewriteFilter
  policydecisioncontext_includes_actions_from_the_policy_decision_response: PolicyDecisionContext includes actions from the policy decision response
  amservice_detects_am_version: AmService detects AM version
  certificate_issued_by_a_trusted_ca_for_any_hostname_or_domain_is_accepted_for_a_connection_to_any_domain: Certificate issued by a trusted CA for any hostname or domain is accepted for a connection to any domain
  product_information_in_startup_logs: Product information in startup logs
  improved_error_handling_in_scriptablefilter_and_scriptablehandler: Improved error handling in ScriptableFilter and ScriptableHandler
  amservice_websocket_connections_protected_from_timeout: AmService Websocket connections protected from timeout
  timeout_of_idle_am_sessions: Timeout of idle AM sessions
  proxy_configuration_can_be_created_in_the_heap_and_used_for_am_notifications: Proxy configuration can be created in the heap and used for AM notifications
---

# What's new

## PingGateway 2026.6

### Support for OAuth 2.0 AS issuer identification and mix-up mitigation

When OAuth 2.0 client applications interact with multiple authorization servers (AS), mix-up attacks are a potential threat. In a mix-up attack, an attacker tricks the client into sending authorization responses to the wrong AS, potentially leading to unauthorized access.

To protect against these threats, PingGateway now supports [RFC 9207: OAuth 2.0 Authorization Server Issuer Identification](https://www.rfc-editor.org/rfc/rfc9207.html) and [OAuth 2.0 Mix-Up Mitigation](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-mix-up-mitigation-01) (draft 1).

As an OAuth 2.0 client, PingGateway supports RFC 9207 by default when the AS metadata has `authorization_response_iss_parameter_supported` set to `true`. You can optionally configure this explicitly in the `Issuer` configuration with the [issParameterSupported](https://docs.pingidentity.com/pinggateway/2026/reference/Issuer.html#Issuer-issParameterSupported) property.

When the AS, such as PingOne Advanced Identity Cloud or PingAM supports the mix-up mitigation Internet-Draft, you must explicitly enable support in the PingGateway `AuthorizationCodeOAuth2ClientFilter` configuration. Use the [draftMixUpMitigation](https://docs.pingidentity.com/pinggateway/2026/reference/AuthorizationCodeOAuth2ClientFilter.html#AuthorizationCodeOAuth2ClientFilter-draftMixUpMitigation) property.

### Support for MCP version 2025-11-25

PingGateway now supports MCP version 2025-11-25 in addition to version 2025-06-18.

You can set the preferred server protocol version using the `"preferredServerVersion"` property of the [McpValidationFilter](https://docs.pingidentity.com/pinggateway/2026/reference/McpValidationFilter.html).

### Improved MCP audit events

The [McpAuditFilter](https://docs.pingidentity.com/pinggateway/2026/reference/McpAuditFilter.html) now records client and server information present in initialize requests.

Find an example showing how to use an `McpAuditFilter` in context in [MCP security gateway](https://docs.pingidentity.com/pinggateway/2026/mcp/index.html).

### PingAM sessions traced in audit logs

To simplify correlating audit events between PingGateway and AM, PingGateway now includes the AM session tracking ID in audit logs.

The ID shows up in an audit event as the value of the `"ext"` > `"am-sessionuid"` property. The value corresponds to one of the `"trackingIds"` array items in PingAM audit log events.

### Documentation for using PingGateway with PingFederate

The PingGateway documentation now includes examples showing how to use PingFederate as an Authorization Server. Learn more in:

* [Protect an MCP server with PingFederate](https://docs.pingidentity.com/pinggateway/2026/reference/McpProtectionFilter.html#McpProtectionFilter-example-pingfederate)

* [Validate access tokens with PingFederate](https://docs.pingidentity.com/pinggateway/2026/reference/OAuth2ResourceServerFilter.html#OAuth2ResourceServerFilter-example-pingfederate)

### Kubernetes and Helm deployment for FAPI

Evaluation Docker images and sample Helm charts are now available for deploying the PingGateway FAPI components on Kubernetes. You can optionally use Helm charts to deploy the FAPI PEP AS, the FAPI PEP RS, and the sample trusted directory in containers rather than configuring them manually.

Learn more in [Deploy FAPI with Kubernetes and Helm](https://docs.pingidentity.com/pinggateway/2026/fapi/kubernetes.html).

## PingGateway 2026.3

### PingAuthorize support

PingGateway now supports integration with PingAuthorize software for self-managed and on-premise deployments. Use the same filter as for PingOne Authorize with settings applicable to your PingAuthorize deployment.

Learn more in the [PingAuthorizeFilter](https://docs.pingidentity.com/pinggateway/2026/reference/PingAuthorizeFilter.html) reference.

### Auditing for administrative endpoints

PingGateway now supports auditing for administrative endpoints such as `/api/info` or `/metrics/prometheus/0.0.4`.

Learn more in the `admin.json` reference about the new configuration property, [auditService](https://docs.pingidentity.com/pinggateway/2026/reference/AdminHttpApplication.html#AdminHttpApplication-auditService).

### OpenTelemetry logging

PingGateway now supports logging events to an OpenTelemetry service.

Learn more in [Log to an OpenTelemetry service](https://docs.pingidentity.com/pinggateway/2026/maintenance-guide/monitoring.html#monitoring-otlp-logging).

### Custom login pages

If you use a custom login page instead of the PingOne Advanced Identity Cloud or AM default pages for authentication journeys, you have configured a Login URL Template for CDSSO in the PingGateway agent profile.

In PingOne Advanced Identity Cloud and AM 8.1 and later, the URL template now supports a `${gotoOnFail}` parameter.

If you have a custom login page:

* Add the `${gotoOnFail}` parameter to the existing URL template in the PingGateway agent profile.

  For example, `&gotoOnFail=${gotoOnFail}` or `&failureUrl=${gotoOnFail}`.

* Update the custom login page to use the new parameter, verify its value is valid to protect against open redirect attacks, and redirect the user-agent when authentication fails.

By adding the `${gotoOnFail}` parameter, you ensure PingOne Advanced Identity Cloud or AM notifies PingGateway on failure, too. PingGateway uses the notification to remove stale session data. This parameter also allows PingGateway to redirect the user-agent on failure to an appropriate page. It is particularly helpful in headless authentication use cases like Windows Desktop SSO, where the user must decide how to authenticate on failure but isn't notified unless you provide a failure URL.

Find out where to configure the URL template in:

* [Register PingGateway with PingOne Advanced Identity Cloud](https://docs.pingidentity.com/pinggateway/2026/aic/preface.html#register-agent-idc)

* [Register PingGateway with PingAM](https://docs.pingidentity.com/pinggateway/2026/gateway-guide/preface.html#register-agent-am)

### FAPI and custom data audit logging

PingGateway now provides an `accessAuditExtension` context, which lets you log custom data in access audit logs using filters or Groovy. When this context is present, PingGateway logs `key:value` pairs with custom data in an extension object (`ext`) under the `ig` section of the event in access audit logs.

The existing FAPI audit log has been migrated to use this new `accessAuditExtension` context. FAPI-specific audit attributes are now logged in the `ext` object for FAPI requests.

Learn more in [Extend audit events with custom data](https://docs.pingidentity.com/pinggateway/2026/maintenance-guide/auditing.html#extend-audit-events-custom-data).

### File permissions in JsonAuditEventHandler

PingGateway now supports configuring file permissions for log files generated by the [JsonAuditEventHandler](https://docs.pingidentity.com/pinggateway/2026/reference/JsonAuditEventHandler.html).

The default file permission is `644`. This allows the owner to read and write the file, while group members and all other users can only read it.

## PingGateway 2025.11.x

### 2025.11.2

#### File permissions in JsonAuditEventHandler

PingGateway now supports configuring file permissions for log files generated by the [JsonAuditEventHandler](https://docs.pingidentity.com/pinggateway/2025.11/reference/JsonAuditEventHandler.html).

The default file permission is `644`. This allows the owner to read and write the file, while group members and all other users can only read it.

#### Additional filter support for well-known endpoints with MCP

PingGateway now supports specifying a filter for requests targeting the well-known endpoint. For example, use a `CorsFilter` to allow preflight requests in the browser.

Learn more about the `"wellKnownFilter"` setting in the [McpProtectionFilter](https://docs.pingidentity.com/pinggateway/2025.11/reference/McpProtectionFilter.html) reference.

### 2025.11.1

#### MCP support

PingGateway now helps you protect [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro) services.

|   |                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This feature has [Evolving](stability.html#interface-stability) interface stability. It's subject to change without notice, even in a minor or maintenance release. |

Find a tutorial you can try in [MCP security gateway](https://docs.pingidentity.com/pinggateway/2025.11/mcp/index.html).

Learn more in these reference pages:

* [McpAuditFilter](https://docs.pingidentity.com/pinggateway/2025.11/reference/McpAuditFilter.html)

* [McpProtectionFilter](https://docs.pingidentity.com/pinggateway/2025.11/reference/McpProtectionFilter.html)

* [McpValidationFilter](https://docs.pingidentity.com/pinggateway/2025.11/reference/McpValidationFilter.html)

### 2025.11.0

#### Improvements to FAPI support

PingGateway includes a number of improvements related to [FAPI support](https://docs.pingidentity.com/pinggateway/2025.11/fapi/).

|   |                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------- |
|   | If you're configuring a self-managed PingAM deployment, FAPI functionality requires AM version 8.0.2 or later. |

#### Help switching to PingOne Advanced Identity Cloud

PingGateway can help you switch from a self-managed or on-premise AM deployment to PingOne Advanced Identity Cloud. Use it to redirect requests for OAuth 2.0 and OpenID Connect (OIDC) clients and for Security Assertion Markup Language (SAML) V2.0 service providers.

Learn more in [Move to PingOne Advanced Identity Cloud](https://docs.pingidentity.com/pinggateway/2025.11/aic/switch-to-saas.html).

#### Reloadable route properties

PingGateway now supports reloading local properties files and the routes that depend on them. This allows you to update route configurations without changing the route files.

Use this when you deploy PingGateway in an environment with locked-down route configurations, for example, with a read-only file system or a PingGateway `Router` setting of `"scanInterval": "disabled"`. This is common in Docker deployments that nevertheless need to support some updates.

Learn more in the [Properties](https://docs.pingidentity.com/pinggateway/2025.11/reference/Properties.html) reference sections about `"$location:<_id>"` settings.

#### Ensure all routes load successfully

PingGateway now lets you configure a router to add its routes only when *all* routes load successfully.

To do so, set `"failOnRouteError": true` in the [Router](https://docs.pingidentity.com/pinggateway/2025.11/reference/Router.html) configuration.

#### Configurable maximum for WebSocket connections

PingGateway `ReverseProxyHandler` configurations now support a setting to change the maximum number of pooled WebSocket connections through the handler.

Learn more in the [ReverseProxyHandler](https://docs.pingidentity.com/pinggateway/2025.11/reference/ReverseProxyHandler.html#ReverseProxyHandler-websocket-maxConnections) reference.

## PingGateway 2025.9

### FAPI support

PingGateway now provides full support for the Financial-grade API (FAPI) standards, simplifying implementation of FAPI-compliant client registration, authorization services, and resource servers.

Learn more in the tutorial for [evaluating FAPI support](https://docs.pingidentity.com/pinggateway/2025.9/fapi/) and in the [FAPI reference documentation](https://docs.pingidentity.com/pinggateway/2025.9/reference/Fapi.html).

### Graceful shutdown

PingGateway now supports graceful shutdown, refusing new connections and waiting a configurable grace period before forcing existing connections to close.

In `admin.json`, you can configure separate `"gracePeriod"` settings for [administrative connections](https://docs.pingidentity.com/pinggateway/2025.9/reference/AdminHttpApplication.html#AdminHttpApplication-adminConnector-gracePeriod) and [client application connections](https://docs.pingidentity.com/pinggateway/2025.9/reference/AdminHttpApplication.html#AdminHttpApplication-connectors-gracePeriod).

### Custom algorithm setting for JwkSetHandler

The `JwkSetHandler` now supports a `"jwkAlgorithm"` setting to specify the algorithm to include in the generated JWK `alg` parameter.

Learn more in [JwkSetHandler](https://docs.pingidentity.com/pinggateway/2025.9/reference/JwkSetHandler.html).

### Configuration conditions

PingGateway now supports runtime conditions. Conditions extend PingGateway expressions, taking an optional label.

Learn more in the reference page on [Conditions](https://docs.pingidentity.com/pinggateway/2025.9/reference/Conditions.html) and in the reference documentation for configuration elements that support conditions.

## PingGateway 2025.6.x

### PingGateway 2025.6.2

PingGateway 2025.6.2 is a maintenance release with no externally visible features or fixes.

### PingGateway 2025.6.1

PingGateway 2025.6.1 is a maintenance release to fix a third-party dependency issue. It includes no new features or other fixes.

### PingGateway 2025.6

#### New startup readiness endpoint

PingGateway now exposes these health check administrative endpoints:

* `health/liveness` (Interface stability: [Evolving](stability.html#interface-stability))

* `health/readiness` (Interface stability: [Evolving](stability.html#interface-stability))

* `health/startup`

The `health/startup` endpoint replaces the deprecated `ping` endpoint.

Learn more about the endpoints in [Health check endpoints](https://docs.pingidentity.com/pinggateway/2025.6/maintenance-guide/monitoring.html#health-check).

Find the full path to the endpoint in the reference for the `admin.json` property, [adminConnector](https://docs.pingidentity.com/pinggateway/2025.6/reference/AdminHttpApplication.html#AdminHttpApplication-adminConnector).

#### Specify the journey to authenticate to AM

PingGateway now lets you specify the authentication journey (tree) the `AmService` uses when authenticating to AM.

Learn more in the reference for the `AmService` [agent > journey](https://docs.pingidentity.com/pinggateway/2025.6/reference/AmService.html#AmService-agent-journey).

#### Audit session cache clearing events

The PingGateway `AmService` now lets you reference an `AuditService` to capture notifications from AM, such as cache clearing events, in an audit log.

Learn more in the reference for the `AmService` [notifications > audit](https://docs.pingidentity.com/pinggateway/2025.6/reference/AmService.html#AmService-notifications-enabled) settings.

#### Limit HTTP request body size

PingGateway now lets you set the maximum acceptable body size for incoming HTTP requests.

In [`admin.json`](https://docs.pingidentity.com/pinggateway/2025.6/reference/AdminHttpApplication.html), you can set:

* [`adminMaxBodyLength`](https://docs.pingidentity.com/pinggateway/2025.6/reference/AdminHttpApplication.html#AdminHttpApplication-adminMaxBodyLength): Maximum body size in bytes for HTTP requests to the administration port.

* [`maxBodyLength`](https://docs.pingidentity.com/pinggateway/2025.6/reference/AdminHttpApplication.html#AdminHttpApplication-maxBodyLength): Maximum body size in bytes for HTTP requests from client applications.

This takes effect only when [`"streamingEnabled": false`](https://docs.pingidentity.com/pinggateway/2025.6/reference/AdminHttpApplication.html#AdminHttpApplication-streamingEnabled) in the `admin.json` file.

## PingGateway 2025.3

### Use Bouncy Castle FIPS

PingGateway now describes how to use Bouncy Castle FIPS to help with FIPS 140–3 compliance without requiring an HSM using a PKCS#11 interface.

Learn more in [FIPS 140–3 compliance](https://docs.pingidentity.com/pinggateway/2025.3/installation-guide/fips.html).

### Offload TLS handshakes

[ClientTlsOptions](https://docs.pingidentity.com/pinggateway/2025.3/reference/ClientTlsOptions.html) and [ServerTlsOptions](https://docs.pingidentity.com/pinggateway/2025.3/reference/ServerTlsOptions.html) now support an optional `offloadHandshake` setting (default: `false`).

When processing a TLS handshake with revocation checks enabled, the handshake process can take an extended amount of time, blocking the event thread from processing other requests. When this option is `true`, PingGateway processes the TLS handshake in a separate worker thread. The event thread continues to process other requests.

### Close connections gracefully

PingGateway now supports options to help close connections more gracefully.

Use the new `"connectionTimeToLive"` and `"connectionShutdownGracePeriod"` settings for connections [to servers](https://docs.pingidentity.com/pinggateway/2025.3/reference/ClientHandler.html#ClientHandler-graceful-close) and [from client applications](https://docs.pingidentity.com/pinggateway/2025.3/reference/ReverseProxyHandler.html#ReverseProxyHandler-graceful-close).

### Custom unauthorized responses for Kerberos

The [KerberosIdentityAssertionPlugin](https://docs.pingidentity.com/pinggateway/2025.3/reference/KerberosIdentityAssertionPlugin.html) now supports customzing the HTTP 401 Unauthorized responses with an optional `unauthorizedResponseHandler`.

When a browser can't supply a Kerberos token and isn't configured to deal appropriately with HTTP 401 Unauthorized, the default response can leave the user stuck on an unauthorized page. Use the `unauthorizedResponseHandler` provide an appropriate response to resolve this issue.

### OpenTelemetry now supported

OpenTelemetry support is no longer a technology preview. It is now a supported feature.

The feature has [Evolving](stability.html#interface-stability) interface stability. It is subject to change without notice, even in a minor or maintenance release.

## PingGateway 2024.11.x

### PingGateway 2024.11.2

PingGateway 2024.11.2 is a maintenance release with no externally visible features or fixes.

### PingGateway 2024.11.1

PingGateway 2024.11.1 is a maintenance release to fix third-party dependency issues and the issue listed in [Fixed in PingGateway 2024.11.1](fixes.html#fix-in-2024.11.1).

It includes no new features.

### PingGateway 2024.11.0

### Device profile support for risk evaluation

PingGateway now supports gathering device profile data from the user-agent and including the profile data in PingOne Protect risk evaluation requests.

Learn more in [PingOne Protect integration](https://docs.pingidentity.com/pinggateway/2024.11/pingone/risk.html).

### PKCE support for OAuth 2.0 clients

The [AuthorizationCodeOAuth2ClientFilter](https://docs.pingidentity.com/pinggateway/2024.11/reference/AuthorizationCodeOAuth2ClientFilter.html) and [ClientRegistration](https://docs.pingidentity.com/pinggateway/2024.11/reference/ClientRegistration.html) configurations now support [RFC 7636: Proof Key for Code Exchange by OAuth Public Clients](https://www.rfc-editor.org/rfc/rfc7636.html) (PKCE).

PKCE is enabled by default and recommended. To disable it, set `"pkce_method": "none"` or `"pkceMethod": "none"` as described in the reference documentation.

### Graceful shutdown

The `stop.sh` and `stop.bat` scripts now accept additional arguments to change how long the script waits before forcing the PingGateway process to terminate.

Learn more in [Graceful shutdown](https://docs.pingidentity.com/pinggateway/2024.11/installation-guide/start-stop.html#graceful-shutdown).

### Lifetime for CDSSO sessions

The [CrossDomainSingleSignOnFilter](https://docs.pingidentity.com/pinggateway/2024.11/reference/CrossDomainSingleSignOnFilter.html) now has a `"lifetime"` setting to configure the duration after which PingGateway removes the initial CDSSO authentication session state.

### Propagate disconnections

PingGateway now supports a [ClientHandler](https://docs.pingidentity.com/pinggateway/2024.11/reference/ClientHandler.html) and [ReverseProxyHandler](https://docs.pingidentity.com/pinggateway/2024.11/reference/ReverseProxyHandler.html) `"propagateDisconnection"` setting to reset the connection to the protected application when the user-agent disconnects and PingGateway is in streaming mode.

### Support for DER certificates

PingGateway now supports a [`derCertificate(string)` function](https://docs.pingidentity.com/pinggateway/2024.11/reference/Functions.html#functions-derCertificate) to convert a base64-encoded DER-format string into a certificate.

### More flexible `AmSessionIdleTimeoutFilter` settings

A new `"idleTimeoutUpdate": "INCREASE_ONLY_THEN_ALWAYS"` setting for [AmSessionIdleTimeoutFilters](https://docs.pingidentity.com/pinggateway/2024.11/reference/AmSessionIdleTimeoutFilter.html) lets you enforce the longest timeout of either the idle timeout from the current filter or the tracking token, and then set the tracking token timeout to the idle timeout of the filter.

PingGateway uses the updated tracking token on the next interaction with an AmSessionIdleTimeoutFilter. The next AmSessionIdleTimeoutFilter filter can use a different `"idleTimeoutUpdate"` setting, for example, to enforce a shorter idle timeout.

## PingGateway 2024.9

### OpenTelemetry capabilities

This release adds the ability to push traces to an [OpenTelemetry](https://opentelemetry.io/) service.

|   |                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | These capabilities are available in [Technology preview](stability.html#interface-stability). They aren't yet supported, may be functionally incomplete, and are subject to change without notice. |

Learn more in the following documentation:

* [Push to an OpenTelemetry service](https://docs.pingidentity.com/pinggateway/2024.11/maintenance-guide/monitoring.html#monitoring-tracing)

* [AdminHttpApplication (`admin.json`)](https://docs.pingidentity.com/pinggateway/2024.11/reference/AdminHttpApplication.html)

* [Start the sample application](https://docs.pingidentity.com/pinggateway/2024.11/getting-started/start-sampleapp.html#start-sampleapp-start)

### Multiple versions of a secret with FileSystemSecretStore

With the new FileSystemSecretStore `versionSuffix` setting you can have multiple versions of a secret with the same ID.

Learn more in [FileSystemSecretStore](https://docs.pingidentity.com/pinggateway/2024.11/reference/FileSystemSecretStore.html).

### Replace setting for HeaderFilter

Use the new HeaderFilter `replace` setting to replace headers instead of removing then adding them.

Learn more in [HeaderFilter](https://docs.pingidentity.com/pinggateway/2024.11/reference/HeaderFilter.html).

### Runtime exception condition for retries

The new `runtimeExceptionCondition` setting lets you restrict which runtime exceptions lead to retries.

Learn more in [ClientHandler](https://docs.pingidentity.com/pinggateway/2024.11/reference/ClientHandler.html) and [ReverseProxyHandler](https://docs.pingidentity.com/pinggateway/2024.11/reference/ReverseProxyHandler.html).

### Security provider setting for keystores

The new `securityProvider` setting lets you choose the Java security provider to use when loading a keystore.

Learn more in [KeyStoreSecretStore](https://docs.pingidentity.com/pinggateway/2024.11/reference/KeyStoreSecretStore.html).

### Delayed route metrics creation

The new `delayRouteMetrics` setting lets you defer creation of route metrics until a request passes through the route. This can improve startup times for deployments with many routes.

Learn more in [Router](https://docs.pingidentity.com/pinggateway/2024.11/reference/Router.html).

### Separate endpoint for administration

PingGateway now lets you configure a separate endpoint for administrative connections. PingGateway is expected to require a separate administrative endpoint in a future release.

Learn more in [AdminHttpApplication (`admin.json`)](https://docs.pingidentity.com/pinggateway/2024.11/reference/AdminHttpApplication.html).

### New PingOne Authorize example

The documentation now includes an example showing how to protect a web application with help from PingOne Authorize.

Learn more in [PingOne Authorize integration](https://docs.pingidentity.com/pinggateway/2024.11/pingone/aam.html).

### Asynchronous reads in `FileAttributesFilter` and `SqlAttributesFilter`

When you omit the deprecated `target` setting from a [FileAttributesFilter](https://docs.pingidentity.com/pinggateway/2024.11/reference/FileAttributesFilter.html) or an [SqlAttributesFilter](https://docs.pingidentity.com/pinggateway/2024.11/reference/SqlAttributesFilter.html), PingGateway reads the file or performs the SQL query asynchronously when calling the filter. Place the filter immediately before the entity reading the data from the context.

## PingGateway 2024.6

### IG becomes PingGateway

Product names changed when ForgeRock became part of Ping Identity. PingGateway was formerly known as ForgeRock Identity Gateway. Learn more about the name changes in [New names for ForgeRock products](https://support.pingidentity.com/s/article/New-names-for-ForgeRock-products).

### PingOne Protect integration

You can now use PingOne Protect risk evaluations to help protect web applications. Configure PingGateway routes to react dynamically to risk scores from PingOne Protect.

|   |                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | PingOne Protect integration is available in [Technology preview](stability.html#interface-stability). It isn't yet supported, may be functionally incomplete, and is subject to change without notice. |

Learn more in [PingOne Protect integration](https://docs.pingidentity.com/pinggateway/2024.11/identity-cloud-guide/risk.html).

### Changes to the Prometheus Scrape Endpoint

To facilitate consumption of Prometheus metrics, the format of some metrics has been updated and the new format is available on the new endpoint `…​/openig/metrics/prometheus/0.0.4`.

The old format and endpoint are deprecated, but for backward compatibility, they are enabled and available by default.

The new property `serveDeprecatedPrometheusEndpoint` in [AdminHttpApplication](https://docs.pingidentity.com/pinggateway/2024.11/reference/RequiredConfiguration.html) is available to deliver Prometheus metrics in the deprecated format. It is enabled by default.

Learn more in [Metrics at the Prometheus Scrape Endpoint](https://docs.pingidentity.com/pinggateway/2024.11/reference/Monitoring.html#monitoring-metrics).

### New metrics at the Prometheus Scrape Endpoint

Startup and Websocket metrics are now available at the Prometheus Scrape Endpoint. Learn more in [Startup metrics at the Prometheus Scrape Endpoint](https://docs.pingidentity.com/pinggateway/2024.11/reference/Monitoring.html#prom-startup-metrics) and [WebSocket metrics at the Prometheus Scrape Endpoint](https://docs.pingidentity.com/pinggateway/2024.11/reference/Monitoring.html#websocket-metrics-prom).

### PingOneApiAccessManagementFilter now supported

The [PingOneApiAccessManagementFilter](https://docs.pingidentity.com/pinggateway/2024.11/reference/PingOneApiAccessManagementFilter.html) is now supported for general use.

### Hardened security for OpenID Connect ID tokens

PingGateway now supports OpenID Connect ID token validation according to the OpenID Connect specifications.

For this release, signature validation is optional. The next major release is expected to make ID token signature validation required.

The following new properties enable validation of the ID token signatures and the `iss`, `aud`, `exp`, `iat`, and `nonce` claims:

* [ClientRegistration](https://docs.pingidentity.com/pinggateway/2024.11/reference/MiscellaneousConfigurationObjects.html#ClientRegistration):

  * `skipSignatureVerification`

  * `clientSecretUsage`

  In addition, use the `clientSecretId` and `secretsProvider` properties for HMAC-based signature validation.

- [Issuer](https://docs.pingidentity.com/pinggateway/2024.11/reference/MiscellaneousConfigurationObjects.html#Issuer):

  * `issuer`

  * `secretsProvider`

  * `idTokenVerificationSecretId`

  * `idTokenSkewAllowance`

Learn more about *ClientRegistration configurations* and *Issuer configurations* in [Incompatible changes](changes.html).

## IG 2024.3

### Local authentication on behalf of PingOne Advanced Identity Cloud and Kerberos validation

The following new objects are available for local processing on behalf of PingOne Advanced Identity Cloud as part of an PingOne Advanced Identity Cloud journey:

* [IdentityAssertionHandler](https://docs.pingidentity.com/pinggateway/2024.11/reference/IdentityAssertionHandler.html)

* [IdentityRequestJwtContext](https://docs.pingidentity.com/pinggateway/2024.11/reference/IdentityRequestJwtContext.html)

* [ScriptableIdentityAssertionPlugin](https://docs.pingidentity.com/pinggateway/2024.11/reference/ScriptableIdentityAssertionPlugin.html)

* [KerberosIdentityAssertionPlugin](https://docs.pingidentity.com/pinggateway/2024.11/reference/KerberosIdentityAssertionPlugin.html) and the service objects UsernamePasswordServiceLogin and KeytabServiceLogin.

These objects exist alongside the Technical Preview objects, IdentityAssertionHandlerTechPreview, ScriptableIdentityAssertionPluginTechPreview, and IdentityAssertionPluginTechPreview, introduced in the last release.

### Monitoring of caches

Monitoring metrics are now available at the Prometheus Scrape Endpoint and Common REST Monitoring Endpoint for the caches described in [Caches](https://docs.pingidentity.com/pinggateway/2024.11/reference/Caches.html).

Learn more in [Cache metrics at the Prometheus Scrape Endpoint](https://docs.pingidentity.com/pinggateway/2024.11/reference/Caches.html#prom-cache-metrics).

### Use of secrets in Studio

IG now uses secrets instead of deprecated passwords. Learn how IG manages migration in [Upgrade from an earlier version of Studio](https://docs.pingidentity.com/pinggateway/2024.11/studio-guide/upgrade.html).

### Use of Splunk or ElasticSearch audit event handlers in Studio

IG Studio no longer uses the deprecated Splunk or ElasticSearch audit event handlers. Learn how IG manages migration in [Upgrade from an earlier version of Studio](https://docs.pingidentity.com/pinggateway/2024.11/studio-guide/upgrade.html).

### Hardened security for secrets

With PingOne Advanced Identity Cloud and from AM 7.5, passwords hardcoded in the identity provider configuration can optionally be managed by the identity provider's secret service. These passwords include the IG agent passwords and OAuth 2.0 client passwords.

### IssuerRepository

An IssuerRepository is provided as a default object. Learn more in [Default objects](https://docs.pingidentity.com/pinggateway/2024.11/reference/RequiredConfiguration.html##admin-default-objects).

### Dedicated filter for PingOne's API Access Management ([Technology preview](stability.html#interface-stability))

[PingOneApiAccessManagementFilter](https://docs.pingidentity.com/pinggateway/2024.11/reference/PingOneApiAccessManagementFilter.html) is a new filter dedicated to PingOne's API Access Management. Use this filter with API Access Management to evaluate HTTP requests and responses.

|   |                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The PingOneApiAccessManagementFilter is available in [Technology preview](stability.html#interface-stability). It isn't yet supported, may be functionally incomplete, and is subject to change without notice. |

## IG 2023.11.x

### IG 2023.11.2

IG 2023.11.2 is a maintenance version to fix third-party dependency issues and the issue listed in [Fixed in 2023.11.2](fixes.html#fix-in-2023.11.2).

It contains no new features.

### IG 2023.11.1

IG 2023.11.1 is a maintenance version to fix issues listed in [Fixed in 2023.11.1](fixes.html#fix-in-2023.11.1).

It contains no new features.

### IG 2023.11.0

#### General features

##### Harden OAuth 2.0 access token requests

[GrantSwapJwtAssertionOAuth2ClientFilter](https://docs.pingidentity.com/pinggateway/2023.11/reference/GrantSwapJwtAssertionOAuth2ClientFilter.html) is a new filter to transform requests for OAuth 2.0 access tokens into secure [JWT bearer grant type](https://docs.pingidentity.com/pingam/8.1/oauth2-guide/oauth2-jwt-bearer-grant.html) requests.

Use this filter with PingOne Advanced Identity Cloud or AM to increase the security of less-secure grant-type requests like [Client credentials grant](https://docs.pingidentity.com/pingam/8.1/oauth2-guide/oauth2-client-cred-grant.html) or [Resource owner password credentials grant](https://docs.pingidentity.com/pingam/8.1/oauth2-guide/oauth2-ropc-grant.html).

Learn more in [Secure the OAuth 2.0 access token endpoint](https://docs.pingidentity.com/pinggateway/2023.11/identity-cloud-guide/grant-swap.html#oauth2-GrantSwapJwtAssertionOAuth2ClientFilter).

##### Include key ID in JWT header

The new `includeKeyId` property is available in [JwtBuilderFilter](https://docs.pingidentity.com/pinggateway/2023.11/reference/JwtBuilderFilter.html) to include the ID of the signature key in the header of a built JWT.

##### Local processing on behalf of PingOne Advanced Identity Cloud ([Technology preview](stability.html#interface-stability))

The following new objects are available for local processing on behalf of PingOne Advanced Identity Cloud as part of an PingOne Advanced Identity Cloud journey:

* [IdentityAssertionHandlerTechPreview](https://docs.pingidentity.com/pinggateway/2023.11/reference/IdentityAssertionHandlerTechPreview.html)

* [ScriptableIdentityAssertionPluginTechPreview](https://docs.pingidentity.com/pinggateway/2023.11/reference/ScriptableIdentityAssertionPluginTechPreview.html)

|   |                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The IdentityAssertionHandlerTechPreview, ScriptableIdentityAssertionPluginTechPreview, and IdentityAssertionPluginTechPreview are available in [Technology preview](stability.html#interface-stability). They aren't yet supported, may be functionally incomplete, and are subject to change without notice. |

##### Secret format JwkPropertyFormat

[JwkPropertyFormat](https://docs.pingidentity.com/pinggateway/2023.11/reference/JwkPropertyFormat.html) is a new secret format. Use it with [FileSystemSecretStore](https://docs.pingidentity.com/pinggateway/2023.11/reference/FileSystemSecretStore.html) to decode JSON Web Key (JWK) formatted keys into secrets.

##### More flexible use of CA-certificates in mutual TLS

The new property `certificateVerificationSecretId` is available in [SecretsTrustManager](https://docs.pingidentity.com/pinggateway/2023.11/reference/SecretsTrustManager.html) to use of CA certificates in mutual TLS. In previous releases, the use of CA-signed certificates was more restricted.

##### Safeguard against accidental exposure of private keys with JwkSetHandler

The `exposePrivateSecrets` new property is available in [JwkSetHandler](https://docs.pingidentity.com/pinggateway/2023.11/reference/JwkSetHandler.html) to safeguard against the accidental exposure of private keys in a JWK set.

The property is `false` by default to prevent exposure of private keys. To expose private keys, explicitly set the property to `true`.

#### SAML

##### Prevention of redirect loops when session cookies aren't present in the SAML flow

In [SamlFederationFilter](https://docs.pingidentity.com/pinggateway/2023.11/reference/SamlFederationFilter.html), the new `redirectionMarker` property is enabled by default to prevent redirect loops when a session cookie isn't present in the SAML flow.

When the marker is present in the request query parameters, the request isn't redirected for authentication.

## IG 2023.9

### Revocation of access tokens initiated by OAuth 2.0 Resource Servers

The following new properties have been added in AuthorizationCodeOAuth2ClientFilter and Issuer:

* `AuthorizationCodeOAuth2ClientFilter:revokeOauth2TokenOnLogout`

* `Issuer:revocationEndpoint`

In OpenID Connect, use these properties to revoke access and refresh tokens issued by Authorization Servers during login.

### Logout initiated by OpenID Connect relying parties

The following new properties have been added in AuthorizationCodeOAuth2ClientFilter and Issuer:

* `AuthorizationCodeOAuth2ClientFilter:openIdEndSessionOnLogout`

* `Issuer:endSessionEndpoint`

In OpenID Connect, use these properties to initiate logout from authorization servers.

### Option to require the Authorization Server to prompt the end-user to reauthenticate and consent

A new property `prompt` is available in AuthorizationCodeOAuth2ClientFilter.

Use the property in [OIDC flows](https://openid.net/specs/openid-connect-core-1_0.html) to require the authorization server to prompt the end user to reauthenticate and consent.

### Improved error handling for AuthorizationCodeOAuth2ClientFilter

When an OAuth 2.0 authorization operation fails, the AuthorizationCodeOAuth2ClientFilter injects the error and error description into the OAuth2FailureContext. In previous releases, OAuth2FailureContext was used only for the OAuth2TokenExchangeFilter.

### New context for use with AuthorizationCodeOAuth2ClientFilter

In AuthorizationCodeOAuth2ClientFilter, retrieve the original target URI for a request from the new IdpSelectionLoginContext.

### Improved security for CrossDomainSingleSignOnFilter

When `verificationSecretId` in CrossDomainSingleSignOnFilter isn't configured, IG discovers and uses the AM JWK set to verify the signature of AM session tokens. If the JWK set isn't available, IG doesn't verify the tokens.

In earlier releases, IG didn't verify the tokens when `verificationSecretId` in CrossDomainSingleSignOnFilter wasn't configured.

To minimize the risk of CDSSO token tampering, always configure `verificationSecretId` in CrossDomainSingleSignOnFilter.

## IG 2023.6

### Large JWT session cookies are automatically split

When a JWT-based session cookie exceeds 4 KBytes, IG automatically splits it into multiple cookies.

If your JWT session size is too close to the value of `connectors:maxTotalHeadersSize` in AdminHttpApplication, IG can block your next request containing split JWT session cookies. Consider increasing the value of `connectors:maxTotalHeadersSize`.

### JWT session cookies not compressed by default

To improve security, JWT session cookies are no longer compressed by default.

### Startup allowed if there is an existing PID file

IG can now start up when there is an existing PID file. When activated, IG removes the existing PID file and creates a new one during startup. In previous releases, if there was an existing PID file during startup, the startup failed.

Activate the feature in the following ways:

* By the new property `pidFileMode` in AdminHttpApplication.

* With the new configuration token `ig.pid.file.mode`.

### Prevention of redirect loops when session cookies aren't present in the CDSSO flow

In CrossDomainSingleSignOnFilter, the new `redirectionMarker` property is enabled by default to prevent redirect loops when the session cookie isn't present in the CDSSO flow.

When the marker is present in the request query parameters, the request isn't redirected for authentication.

### Regex-based alias selection in KeyStoreSecretStore and HsmSecretStore

The new `mappings:aliasesMatching` property in KeyStoreSecretStore and HsmSecretStore is available to map all aliases that match a regular expression to a secret ID.

Some KeyStores, such as a global Java TrustStore, can contain hundreds of valid certificates. Use this property to map multiple aliases to a secret ID without listing them all in the mapping.

### Entity of StaticResponseHandler can be an array of strings

To improve readability, you can now define the `entity` property of a StaticResponseHandler as an array of strings or as a string.

### Maximum size for the sum of all request headers

The new `connectors:maxTotalHeadersSize` property in AdminHttpApplication defines the maximum size in bytes for the sum of all headers in a request. This property replaces the deprecated Vert.x properties `maxHeaderSize` and `initialSettings:maxHeaderListSize`.

### Support for unencoded policy advices

To support SDK in legacy installations, a new `useLegacyAdviceEncoding` property in the PolicyEnforcementFilter is available to provide unencoded advices. By default, advices are encoded with the encoder used by the AM version.

The use of this property is deprecated and should be used only to support SDK in legacy installations.

### Configure forward proxies for WebSocket connections

`websocket:proxyOptions` is a new property in ReverseProxyHandler to provide a dedicated WebSocket reverse proxy.

### Improved control of WebSocket connections to AM

The following properties are now available in AmService to improve control of WebSocket connections to AM:

* `notifications:connectionTimeout`

* `notifications:idleTimeout`

* `notifications:vertx`

## IG 2023.4

### Authentication of IG agent to PingOne Advanced Identity Cloud and AM

IG agents automatically authenticate to PingOne Advanced Identity Cloud and AM with a non-configurable authentication module. Authentication chains and modules are deprecated and replaced by nodes, trees, and journeys.

You can now authenticate IG agents to PingOne Advanced Identity Cloud and AM 7.3 with a journey. The procedure is currently optional, but will be required when authentication chains and modules are removed.

### Policy advices from PingOne Advanced Identity Cloud and AM available in a header

By default, when PingOne Advanced Identity Cloud or AM denies a request with advices, IG returns a redirect response with advices as parameters.

When the request includes the `x-authenticate-response` header with the value `header`, IG now returns the response with the advices in a `WWW-authentication` header.

Use this method for SDKs and single page applications. Placing advices in a header gives these applications more options for handling the advices.

Use the new `authenticateResponseRequestHeader` property in PolicyEnforcementFilter to configure the `x-authenticate-response` header name.

### SAML

The SamlFederationHandler is deprecated and replaced by the SamlFederationFilter.

The SamlFederationFilter can be used in a route protect a downstream application in the same way as other authentication-triggering filters like a SingleSignOnFilter or CrossDomainSingleSignOnFilter.

When triggered, the SamlFederationFilter can initiate the login or logout of a SAML service provider with a SAML identity provider.

### WebSocket connection renewal

IG can now automatically renew WebSocket connections to AM after a defined delay.

### Limit side effects when backend applications are slow

ClientHandler and ReverseProxyHandler have a new `waitQueueSize` property to set the maximum number of outbound requests allowed to queue when no downstream connections are available. Use this property to limit memory use when there is a backlog of outbound requests, for example, when the protected application or third-party service is slow.

In previous releases, the queue size was unlimited. It is now limited to the square of the value of the `connections` property by default.

### Route ID included access audit events

The name and ID of a route is now included by default in access audit events.

## IG 2023.2

### Session eviction

AM 7.3 can be configured to invalidate sessions based on user ID and send a notification with the topic `/agent/session.v2` to IG. IG can now use the notification to evict all sessions bound to the user.

|   |                               |
| - | ----------------------------- |
|   | This feature requires AM 7.3. |

### Preserve POST data during authentication

The DataPreservationFilter triggers POST data preservation when an unauthenticated client posts HTML form data to a protected resource.

### Prevent unnecessary session expiry

When the AmService property `sessionIdleRefresh` is enabled, IG now requests session refresh:

* The first time IG gets an SSO token from AM, irrespective of the age of the token.

* When `sessionIdleRefresh.interval` has elapsed.

In previous releases, IG requested session refresh only after `sessionIdleRefresh.interval` elapsed. If IG got an SSO token close to its maximum idle time, the token could expire before `sessionIdleRefresh.interval` elapsed and IG triggered a refresh.

### CapturedUserPasswordFilter supports secret rotation

When relying on a SecretsProvider to retrieve the shared key required by the CapturedUserPasswordFilter, you can now rotate a secret without reloading the filter if the underlying secret store supports secret rotation.

### KeyStoreSecretStore allows unprotected KeyStores

KeyStoreSecretStore can now use KeyStores that aren't password-protected. In previous releases, KeyStores had to be password-protected.

### Delay destroying HttpClientHandlerHeaplets during shutdown

When IG is cleanly shut down, the destruction of HttpClientHandlerHeaplets is now delayed until all other IG heaplets are destroyed. This change allows the other IG heaplets to use HttpClientHandlerHeaplets during shutdown. For example, AmService can now call logout on any agent tokens it has allocated, which can help to reduce the build up of tokens in AM.

ClientHandlers and ReverseProxyHandlers are examples of HttpClientHandlerHeaplets.

### Automatic reload of FileSystemSecretStore and KeystoreSecretStore

A new `autoRefresh` property is available in FileSystemSecretStore and KeyStoreSecretStore settings to configure automatic reloaded of the secret store when a file or a keystore is edited or deleted.

### Groovy 4

IG now uses Groovy 4 for scripting. Learn more in the [Release notes for Groovy 4.0](https://groovy-lang.org/releasenotes/groovy-4.0.html)

### Expression binding `now`

The expression binding `now` gives the time since epoch at the instant the expression is evaluated.

## IG 7.2

### Token exchange

[OAuth2TokenExchangeFilter](https://docs.pingidentity.com/pinggateway/7.2/reference/OAuth2TokenExchangeFilter.html) is a new filter to exchange a client's access token or ID token for a new token with increased or reduced scopes, while preserving the original token subject.

### Connectivity with OAuth 2.0-protected third-party services

#### OAuth2ClientFilter renamed as AuthorizationCodeOAuth2ClientFilter

IG provides several client authentication filters to protect resources using different types of information and credentials. To make it easier to differentiate between these filters, the OAuth2ClientFilter is now named AuthorizationCodeOAuth2ClientFilter. For backward compatibility, you can still use the name OAuth2ClientFilter in routes.

The following client authentication filters are available to authenticate clients:

* [AuthorizationCodeOAuth2ClientFilter](https://docs.pingidentity.com/pinggateway/7.2/reference/AuthorizationCodeOAuth2ClientFilter.html), using OAuth 2.0 delegated authorization.

* [ClientCredentialsOAuth2ClientFilter](https://docs.pingidentity.com/pinggateway/7.2/reference/ClientCredentialsOAuth2ClientFilter.html), using the client's OAuth 2.0 credentials.

* [ResourceOwnerOAuth2ClientFilter](https://docs.pingidentity.com/pinggateway/7.2/reference/ResourceOwnerOAuth2ClientFilter.html), using the resource owner's password credentials.

#### ClientCredentialsOAuth2ClientFilter uses `client_secret_basic` or `client_secret_post`

The [ClientCredentialsOAuth2ClientFilter](https://docs.pingidentity.com/pinggateway/7.2/reference/ClientCredentialsOAuth2ClientFilter.html) can now get a client's access token using the token endpoint authentication method `client_secret_post`. In previous releases, it could use only `client_secret_basic`.

Client authentication is now provided by the `endpointHandler` property of ClientCredentialsOAuth2ClientFilter, which uses ClientSecretBasicAuthenticationFilter or ClientSecretPostAuthenticationFilter. In previous releases, it was provided by the now deprecated properties `clientId` and `clientSecretId`.

#### ResourceOwnerOAuth2ClientFilter for services to access resources protected by OAuth 2.0

A new filter [ResourceOwnerOAuth2ClientFilter](https://docs.pingidentity.com/pinggateway/7.2/reference/ResourceOwnerOAuth2ClientFilter.html) is available for services to access resources protected by OAuth 2.0 using the *Resource Owner Password Credentials* grant type.

#### Filters to support OAuth 2.0 client authentication

When processing requests or responses, IG can require access to systems such as the PingOne Advanced Identity Cloud to query user information. The following filters enable OAuth 2.0 client authentication to these systems, where IG is the client:

* [ClientSecretBasicAuthenticationFilter](https://docs.pingidentity.com/pinggateway/7.2/reference/ClientSecretBasicAuthenticationFilter.html)

* [ClientSecretPostAuthenticationFilter](https://docs.pingidentity.com/pinggateway/7.2/reference/ClientSecretPostAuthenticationFilter.html)

* [EncryptedPrivateKeyJwtClientAuthenticationFilter](https://docs.pingidentity.com/pinggateway/7.2/reference/EncryptedPrivateKeyJwtClientAuthenticationFilter.html)

* [PrivateKeyJwtClientAuthenticationFilter](https://docs.pingidentity.com/pinggateway/7.2/reference/PrivateKeyJwtClientAuthenticationFilter.html)

Use these filters with the following objects:

* [ClientRegistration](https://docs.pingidentity.com/pinggateway/7.2/reference/ClientRegistration.html)

* [AuthorizationCodeOAuth2ClientFilter](https://docs.pingidentity.com/pinggateway/7.2/reference/AuthorizationCodeOAuth2ClientFilter.html)

* [OAuth2TokenExchangeFilter](https://docs.pingidentity.com/pinggateway/7.2/reference/OAuth2TokenExchangeFilter.html)

* [ClientCredentialsOAuth2ClientFilter](https://docs.pingidentity.com/pinggateway/7.2/reference/ClientCredentialsOAuth2ClientFilter.html)

* [ResourceOwnerOAuth2ClientFilter](https://docs.pingidentity.com/pinggateway/7.2/reference/ResourceOwnerOAuth2ClientFilter.html)

#### OAuth 2.0 session sharing across routes

The `oAuth2SessionKey` property has been added to [AuthorizationCodeOAuth2ClientFilter](https://docs.pingidentity.com/pinggateway/7.2/reference/AuthorizationCodeOAuth2ClientFilter.html) to allow multiple applications to share the same OAuth 2.0 session.

After a resource owner gives one application protected by IG consent to use its data, they don't need to give consent for another application protected by IG.

In previous releases, the OAuth 2.0 session was bound to the full URI of the client callback containing the IG hostname. It wasn't possible to use the same OAuth 2.0 session to access different applications.

### Circuit breaking

#### CircuitBreakerFilter

[CircuitBreakerFilter](https://docs.pingidentity.com/pinggateway/7.2/reference/CircuitBreakerFilter.html) is a new filter to monitor for failures. When the failures reach a specified threshold, the CircuitBreakerFilter prevents further calls to downstream filters and returns a runtime exception.

#### Circuit breaker in ClientHandler and ReverseProxyHandler

A new property `circuitBreaker` has been added to [ClientHandler](https://docs.pingidentity.com/pinggateway/7.2/reference/ClientHandler.html) and [ReverseProxyHandler](https://docs.pingidentity.com/pinggateway/7.2/reference/ReverseProxyHandler.html) to provide a circuit breaker service when the number of failures reaches a configured threshold.

### Stability

#### JwtBuilderFilter produces encrypted JWT

The JwtBuilderFilter now produces encrypted JWTs, as well as unsigned JWTs, signed JWTs, and signed then encrypted JWTs.

#### JwtSession cookie compression

The property `useCompression` has been added to [JwtSession](https://docs.pingidentity.com/pinggateway/7.2/reference/JwtSession.html). When a session stores large items like tokens, use the default value `true` to reduce size of the cookie that stores the JWT.

### Other

#### Windows start script for IG in standalone mode

A script is now provided to start IG in standalone mode on Windows.

#### Stop scripts for IG in standalone mode

Scripts are now provided to stop IG in standalone mode on Unix/OS X and Windows.

#### `IG_OPTS` environment variables for startup

`IG_OPTS` is a new environment variable to separate Java runtime options for IG startup and stop scripts with IG in standalone mode. Use `IG_OPTS` instead of `JAVA_OPTS` for all options that aren't shared with the stop script.

#### SNI to serve different certificates for TLS Connections to different server names

In [ServerTlsOptions](https://docs.pingidentity.com/pinggateway/7.2/reference/ServerTlsOptions.html), `sni` is a new property to serve different secret key and certificate pairs for TLS connections to different server names in the deployment. In previous releases, only the `keyManager` property was available to serve the same secret key and certificate pair for TLS connections to all server names.

Use this property when IG is acting server-side, or to front multiple services or websites on the same port of a machine.

#### IG proxies all WebSocket subprotocols by default

In previous releases, for IG in standalone mode it was necessary to list the WebSocket subprotocols IG proxied using the `vertx` property of [admin.json](https://docs.pingidentity.com/pinggateway/7.2/reference/RequiredConfiguration.html#AdminHttpApplication).

IG now proxies all WebSocket subprotocols by default; it isn't necessary to specify protocols. If you do specify protocols, IG supports only those protocols and no others.

#### Configurable conditions for retries in ClientHandler and ReverseProxyHandler

`condition` is a new property in the `retries` configuration of ClientHandler and ReverseProxyHandler. Use this property to configure a condition on which to trigger a retry. In previous releases, a retry could be triggered only for runtime exceptions.

#### User ID in audit logs

Audit logs can now include a user ID. Example scripts and setup information is provided in [Recording user ID in audit events](https://docs.pingidentity.com/pinggateway/7.2/maintenance-guide/auditing.html#audit-userid).

#### Tracking ID logged in access audit events

In routes containing an [OAuth2ResourceServerFilter](https://docs.pingidentity.com/pinggateway/7.2/reference/OAuth2ResourceServerFilter.html), OAuth 2.0 token tracking IDs are now logged in access audit events.

#### Transformation from string to placeholder string

The `$string` transformation has been added to facilitate the transformation from a string to a placeholder string that isn't encoded. Use this transformation for placeholder strings that mustn't be encrypted when they reference a secret value.

Learn more in [string](https://docs.pingidentity.com/pinggateway/7.2/reference/PropertyValueSubstitution.html#token-functions-string) in *Token Transformation*.

#### Use expressions to configure paths in UriPathRewriteFilter

The `mapping` object in UriPathRewriteFilter now uses configuration expressions to define the `fromPath` and `toPath`. In previous releases, the `mapping` object was a static JSON map.

Learn more in [UriPathRewriteFilter](https://docs.pingidentity.com/pinggateway/7.2/reference/UriPathRewriteFilter.html).

#### PolicyDecisionContext includes actions from the policy decision response

Actions from the AM policy decision response are now available for use in the PolicyDecisionContext.

The resource value used when making the policy request is now available in the [PolicyDecisionContext](https://docs.pingidentity.com/pinggateway/7.2/reference/PolicyDecisionContext.html).

#### AmService detects AM version

[AmService](https://docs.pingidentity.com/pinggateway/7.2/reference/AmService.html) now reads the AM version from the AM endpoint and uses the discovered version instead of the value configured in the AmService property `version`.

The property `version` is used only if the AmService can't discover the AM version.

#### Certificate issued by a trusted CA for any hostname or domain is accepted for a connection to any domain

When IG is acting as a WebSocket proxy and the downstream application is on HTTPS, the WebSocket configuration host can now allow a certificate issued by a trusted CA for any hostname or domain to be accepted for a connection to any domain. Learn more in the documentation for the `hostnameVerifier` property of [ClientTlsOptions](https://docs.pingidentity.com/pinggateway/7.2/reference/ClientTlsOptions.html).

#### Product information in startup logs

Key product information, such as the product version and build number, is now included in the startup logs.

#### Improved error handling in ScriptableFilter and ScriptableHandler

The ScriptableFilter and ScriptableHandler now propagate script exceptions as runtime exceptions in the promise flow. In previous releases, they replaced the exception with a response with HTTP status 500. Users didn't know if the response was from the requested endpoint or caused by an exception in the chain.

#### AmService Websocket connections protected from timeout

A heartbeat can be configured for the [AmService](https://docs.pingidentity.com/pinggateway/7.2/reference/AmService.html) WebSocket notification service to prevent Websocket connections from being closed for timeout.

#### Timeout of idle AM sessions

A new filter, [AmSessionIdleTimeoutFilter](https://docs.pingidentity.com/pinggateway/7.2/reference/AmSessionIdleTimeoutFilter.html), is available to force the revocation of AM sessions that have been idle for a specified timeout.

Use this filter in front of a SingleSignOnFilter or CrossDomainSingleSignOnFilter to manage idle timeout for client sessions in AM.

#### Proxy configuration can be created in the heap and used for AM notifications

A new [ProxyOptions](https://docs.pingidentity.com/pinggateway/7.2/reference/MiscellaneousConfigurationObjects.html#ProxyOptions) heaplet is available to define a proxy to which a [ClientHandler](https://docs.pingidentity.com/pinggateway/7.2/reference/Handlers.html#ClientHandler) or [ReverseProxyHandler](https://docs.pingidentity.com/pinggateway/7.2/reference/Handlers.html#ReverseProxyHandler) can submit requests. An [AmService](https://docs.pingidentity.com/pinggateway/7.2/reference/MiscellaneousConfigurationObjects.html#AmService) can use it to submit Websocket notifications.

A new global ProxyOption heap object is provided.