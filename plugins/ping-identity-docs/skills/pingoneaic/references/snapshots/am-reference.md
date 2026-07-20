---
title: AM Prometheus metrics
description: Prometheus monitoring metrics for access management authentication, authorization, sessions, and operations
component: pingoneaic
page_id: pingoneaic:am-reference:prometheus-metrics
canonical_url: https://docs.pingidentity.com/pingoneaic/am-reference/prometheus-metrics.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  metric-types: Metric types
  summary: Summary
  timer: Timer
  gauge: Gauge
  distinct-counter: Distinct counter
  ref-authentication-metrics: Authentication metrics
  ref-authorization-metrics: Authorization metrics
  ref-blacklisting-metrics: Denylisting metrics
  ref-CTS-metrics: CTS metrics
  ref-oauth2-metrics: OAuth 2.0 metrics
  ref-session-metrics: Session metrics
  ref-script-cache-metrics: Script cache metrics
---

# AM Prometheus metrics

Advanced Identity Cloud provides monitoring endpoints you can use with [Prometheus](https://prometheus.io/docs/introduction/overview/).

This section describes the Prometheus monitoring metrics accessible at the `/monitoring/prometheus/am` endpoint.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * Metric names listed here all start with `am_` and include a `kubernetes_pod_name` label to distinguish between the Kubernetes pods within a tenant environment. For example:

  ```none
   # TYPE am_authentication summary
   am_authentication_sum{kubernetes_pod_name="am-75b55d85c8-gqw9l",outcome="failure",} 0.0
   am_authentication_count{kubernetes_pod_name="am-75b55d85c8-gqw9l",outcome="failure",} 0.0
   am_authentication_sum{kubernetes_pod_name="am-75b55d85c8-gqw9l",outcome="success",} 7016.0
   am_authentication_count{kubernetes_pod_name="am-75b55d85c8-gqw9l",outcome="success",} 7016.0
  ```

* The Prometheus endpoints don't provide rate-based statistics because rates can be calculated from the time-series data. |

## Metric types

The following metric types are available.

### Summary

The summary metric samples observations, providing a count of observations, sum total of observed amounts, average rate of events, and moving average rates across sliding time windows.

> **Collapse: Prometheus summary fields**
>
> | Field    | Description                                    |
> | -------- | ---------------------------------------------- |
> | `# TYPE` | The metric ID and type formatted as a comment. |
> | `_count` | The number of events recorded.                 |
> | `_sum`   | The sum of the number of events recorded.      |
>
> ***Example***
>
> ```none
> # TYPE am_authentication summary
> am_authentication_count{outcome="success"} 2.0
> am_authentication_sum{outcome="success"} 2.0
> ```

### Timer

The timer metric combines rate and duration information.

> **Collapse: Prometheus timer fields**
>
> | Field                | Description                                                                                           |
> | -------------------- | ----------------------------------------------------------------------------------------------------- |
> | `# TYPE`             | The metric ID, and type. Formatted as a comment.	The Timer metric type is reported as a Summary type. |
> | `_count`             | The number of events recorded.                                                                        |
> | `_sum`               | The sum of the number of events recorded.                                                             |
> | `{quantile="0.5"}`   | 50% of the durations are at or below this value.                                                      |
> | `{quantile="0.75"}`  | 75% of the durations are at or below this value.                                                      |
> | `{quantile="0.95"}`  | 95% of the durations are at or below this value.                                                      |
> | `{quantile="0.98"}`  | 98% of the durations are at or below this value.                                                      |
> | `{quantile="0.99"}`  | 99% of the durations are at or below this value.                                                      |
> | `{quantile="0.999"}` | 99.9% of the durations are at or below this value.                                                    |
>
> |   |                                                                                                                                                                                                                                                                     |
> | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | Duration-based quantile values are weighted towards newer data. By representing approximately the last five minutes of data, the timers make it easier to see recent changes in behavior, rather than a uniform average of recordings since the server was started. |

### Gauge

The gauge metric is a numerical value that can increase or decrease. The value for a gauge is calculated when requested, and represents the state of the metric at that specific time.

> **Collapse: Prometheus gauge fields**
>
> | Field         | Description                                                                  |
> | ------------- | ---------------------------------------------------------------------------- |
> | `# TYPE`      | The metric ID, and type. Formatted as a comment.                             |
> | `{Metric ID}` | The current value. Large values may be represented in scientific E-notation. |

### Distinct counter

Metric providing an estimate of the number of *unique* values recorded.

For example, this could be used to estimate the number of unique users who have authenticated, or unique client IP addresses.

> **Collapse: Prometheus distinct counter fields**
>
> | Field         | Description                                                                                                                                            |
> | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
> | `# TYPE`      | The metric ID, and type. Note that the `distinctCounter` type is reported as a `gauge` type. The output formats are identical. Formatted as a comment. |
> | `{Metric ID}` | The calculated estimate of the number of unique values recorded in the metric.                                                                         |
>
> ***Example***
>
> ```none
> # TYPE am_authentication_unique_uuid gauge
> am_authentication_unique_uuid{outcome="success"} 3.0
> ```

## Authentication metrics

Advanced Identity Cloud exposes the following monitoring metrics related to authentication:

> **Collapse: Prometheus authentication metrics**
>
> | Name                                              | Type    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
> | ------------------------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | `am_authentication_count{outcome=outcome,}`       | Summary | Rate of successful/unsuccessful/timed-out authentication flows (count).The count of successful authentications is incremented when an authentication journey completes successfully. Likewise, the authentication count for failure outcomes is incremented for failed authentication journeys.For example, the authorization code flow requires a user session to exist and could redirect the user to a journey for authentication. The completion of this authentication step would then update the count.The client credentials grant, however, doesn't use a journey for authentication and, therefore, doesn't increment the count. |
> | `am_authentication_sum{outcome=outcome,}`         | Summary | Rate of successful/unsuccessful/timed-out authentication flows (total).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
> | `am_authentication_unique_uuid{outcome=outcome,}` | Gauge   | Count of unique identities that have successfully logged in.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
>
> **Authentication metrics labels**
>
> | Label     | Values                                |
> | --------- | ------------------------------------- |
> | `outcome` | * `success`
>
> * `failure`
>
> * `timeout` |

## Authorization metrics

Advanced Identity Cloud exposes the following authorization-related monitoring metrics after a policy evaluation takes place:

> **Collapse: Prometheus authorization metrics**
>
> | Name                                                                                                     | Type    | Description                                                                                                                            |
> | -------------------------------------------------------------------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------- |
> | `am_authorization_policy_set_policy_count{operation=policy-operation,policy_set=policy-set,}`            | Summary | Number of policies created/updated/deleted under a given policy set since the Advanced Identity Cloud service was restarted. (Summary) |
> | `am_authorization_policy_set_policy_sum{operation=policy-operation,policy_set=policy-set,}`              | Summary | Number of policies created/updated/deleted under a given policy set since the Advanced Identity Cloud service was restarted. (Summary) |
> | `am_authorization_policy_set_evaluate_subject_cache_size`                                                | Summary | Number of cached subject membership relationships.                                                                                     |
> | `am_authorization_policy_set_evaluate_seconds{outcome=outcome,policy_set=policy-set,quantile=quantile,}` | Summary | Rate of successful/unsuccessful policy evaluation calls under a given policy set and time taken to perform this operation. (Timer)     |
> | `am_authorization_policy_set_evaluate_count{outcome=outcome,policy_set=policy-set,}`                     | Summary | Rate of successful/unsuccessful policy evaluation calls under a given policy set and time taken to perform this operation. (count)     |
> | `am_authorization_policy_set_evaluate_seconds_sum{outcome=outcome,policy_set=policy-set,}`               | Summary | Rate of successful/unsuccessful policy evaluation calls under a given policy set and time taken to perform this operation. (total)     |
> | `am_authorization_policy_set_evaluate_action_sum{action_type=action,outcome,policy_set=policy-set,}`     | Summary | Rate of policy evaluation allowed/denied actions being returned under a given policy set (total).                                      |
> | `am_authorization_policy_set_evaluate_action_count{action_type=action,outcome,policy_set=policy-set,}`   | Summary | Rate of policy evaluation allowed/denied actions being returned under a given policy set (count).                                      |
> | `am_authorization_policy_set_evaluate_advice{policy_set=policy-set,advice-type=advice-type,}`            | Summary | Rate of policy evaluation advice types being returned under a given policy set.                                                        |
> | `am_authorization_policy_set_evaluate_advice_count{policy_set=policy-set,advice-type,}`                  | Summary | Rate of policy evaluation advice types being returned under a given policy set (count).                                                |
> | `am_authorization_policy_set_evaluate_advice_sum{policy_set=policy-set,advice-type=advice-type}`         | Summary | Rate of policy evaluation advice types being returned under a given policy set (total).                                                |
>
> **Authorization metrics labels**
>
> | Label              | Values                                                                                                                                                 |
> | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
> | `action`           | Name of the action as specified in the policy, for example:- `GET`
>
> - `GRANT`
>
> - `MODIFY`
>
> - `DELEGATE`
>
> - `READ`                                      |
> | `advice-type`      | Name of the policy condition advice, for example:- `AuthenticateToRealmAdvice`
>
> - `AuthenticateToServiceConditionAdvice`
>
> - `AuthLevelConditionAdvice` |
> | `outcome`          | * `success`
>
> * `allow`                                                                                                                                 |
> | `policy-operation` | Type of operation performed on the policy, for example:* `create`
>
> * `delete`
>
> * `update`                                                              |
> | `policy-set`       | Name of the policy set, for example:* `iPlanetAMWebAgentService`
>
> * `oauth2Scopes`                                                                     |
> | `quantile`         | Refer to [Timer](#timer) for `quantile` values.                                                                                                        |

## Denylisting metrics

Advanced Identity Cloud exposes the following denylisting monitoring metrics:

> **Collapse: Prometheus denylisting metrics**
>
> | Name                                                                                               | Type    | Description                                             |
> | -------------------------------------------------------------------------------------------------- | ------- | ------------------------------------------------------- |
> | `am_blacklist_cts_search_count{blacklist_type=denylist type,outcome=outcome,}`                     | Summary | Tracks time to search CTS for denylist entries (count). |
> | `am_blacklist_cts_search_result_count{blacklist_type=denylist type,}`                              | Summary | Rate of denylist entries returned by searches (count).  |
> | `am_blacklist_cts_search_result_sum{blacklist_type=denylist type,}`                                | Summary | Rate of denylist entries returned by searches (total).  |
> | `am_blacklist_cts_search_seconds_sum{blacklist_type=denylist type,outcome=outcome,}`               | Summary | Tracks time to search CTS for denylist entries (count). |
> | `am_blacklist_cts_search_seconds{blacklist_type=denylist type,outcome=outcome,quantile=quantile,}` | Summary | Tracks time to search CTS for denylist entries.         |
> | `am_blacklist_bloomfilter_check{blacklist_type=denylist type,outcome=outcome}`                     | Summary | Rate of bloom filter denylist checks.                   |
> | `am_blacklist_cache{blacklist_type=denylist type,outcome=cache outcome}`                           | Summary | Rate of cache hits/misses of the denylist cache layer.  |
> | `am_blacklist_check{blacklist_type=denylist type,outcome=check outcome}`                           | Summary | Rate of denylist checks.                                |
>
> **Denylisting metrics labels**
>
> | Label           | Values                                                                  |
> | --------------- | ----------------------------------------------------------------------- |
> | `denylist type` | * `session_client_based`
>
> * `oauth2`                                    |
> | `outcome`       | - `success`
>
> - `failure`                                                |
> | `cache outcome` | * `hit`
>
> * `miss`                                                       |
> | `check outcome` | - `true` The token is denylisted
>
> - `false` The token is not denylisted |
> | `quantile`      | Refer to [Timer](#timer) for `quantile` values.                         |

## CTS metrics

Advanced Identity Cloud exposes the following CTS-related monitoring metrics:

> **Collapse: Prometheus CTS metrics**
>
> | Name                                                                                                | Type    | Description                                                                                                |
> | --------------------------------------------------------------------------------------------------- | ------- | ---------------------------------------------------------------------------------------------------------- |
> | `am_cts_task_count{operation=operation,outcome=outcome,token_type=token-type,}`                     | Summary | Rate of successful/unsuccessful CTS operation types, by token type and time taken to perform them.         |
> | `am_cts_task_pending{operation=operation,}`                                                         | Counter | Tracks number of active create operations.                                                                 |
> | `am_cts_task_seconds_sum{operation=operation,outcome=outcome,token_type=token-type,}`               | Summary | Rate of successful/unsuccessful CTS operation types, by token type and time taken to perform them (total). |
> | `am_cts_task_seconds{operation=operation,outcome=outcome,token_type=token-type,quantile=quantile,}` | Summary | Rate of successful/unsuccessful CTS operation types, by token type and time taken to perform them.         |
>
> **CTS metrics labels**
>
> | Label        | Values                                                                                                                                                                                                                                                                                                                                                                                                                                            |
> | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | `operation`  | * `create`
>
> * `delete`
>
> * `partial-query`
>
> * `patch`
>
> * `query`
>
> * `read`
>
> * `update`
>
> * `upsert`                                                                                                                                                                                                                                                                                                                                                 |
> | `outcome`    | - `success`
>
> - `failure`                                                                                                                                                                                                                                                                                                                                                                                                                          |
> | `quantile`   | Refer to [Timer](#timer) for `quantile` values.                                                                                                                                                                                                                                                                                                                                                                                                   |
> | `status`     | * `out`
>
> * `pending`                                                                                                                                                                                                                                                                                                                                                                                                                              |
> | `token_type` | - `authentication-whitelist`
>
> - `back-channel-authentication-state`
>
> - `cluster-notification`
>
> - `logout-user`
>
> - `oauth2-blacklist`
>
> - `oauth2-csrf-protection`
>
> - `oauth2-grant-set`
>
> - `oauth2-stateless-grant`
>
> - `oauth2-stateless`
>
> - `oauth2`
>
> - `push-notification`
>
> - `request-uri-object`
>
> - `resource-set`
>
> - `rest`
>
> - `saml2`
>
> - `session-blacklist`
>
> - `session`
>
> - `sts`
>
> - `suspended-auth-session`
>
> - `transaction`
>
> - `unknown` |

## OAuth 2.0 metrics

Advanced Identity Cloud exposes the following OAuth 2.0 monitoring metrics:

> **Collapse: Prometheus OAuth 2.0 metrics**
>
> | Name                                                                      | Type    | Description                                                                          |
> | ------------------------------------------------------------------------- | ------- | ------------------------------------------------------------------------------------ |
> | `am_oauth2_grant_count{grant_type=grant-type,}`                           | Summary | Rate of OAuth 2.0 grant completion by grant type (count).                            |
> | `am_oauth2_grant_revoke_count{grant_type="unknown",}`                     | Summary | Rate of OAuth 2.0 grant revocation for unknown grant types (count).                  |
> | `am_oauth2_grant_revoke_sum{grant_type="unknown",}`                       | Summary | Rate of OAuth 2.0 grant revocation for unknown grant types (total).                  |
> | `am_oauth2_grant_sum{grant_type=grant-type,}`                             | Summary | Rate of OAuth 2.0 grant completion by grant type (total).                            |
> | `am_oauth2_token_issue_count{token_type=token-type,}`                     | Summary | Rate of OAuth 2.0 token issuance by token type (count).                              |
> | `am_oauth2_token_issue_sum{token_type=token-type,}`                       | Summary | Rate of OAuth 2.0 token issuance by token type (total).                              |
> | `am_oauth2_token_read_as_jwt_count{outcome=outcome,}`                     | Summary | Rate of successfully/unsuccessfully reading OAuth 2.0 JSON Web Tokens (JWT) (count). |
> | `am_oauth2_token_read_as_jwt_seconds_sum{outcome=outcome,}`               | Summary | Rate of successfully/unsuccessfully reading OAuth 2.0 JSON Web Tokens (JWT) (total). |
> | `am_oauth2_token_read_as_jwt_seconds{outcome=outcome,quantile=quantile,}` | Summary | Rate of successfully/unsuccessfully reading OAuth 2.0 JSON Web Tokens (JWT).         |
> | `am_oauth2_token_revoke_count{token_type="access-token",}`                | Summary | Rate of OAuth 2.0 access token revocation (count)                                    |
> | `am_oauth2_token_revoke_sum{token_type="access-token",}`                  | Summary | Rate of OAuth 2.0 access token revocation (total)                                    |
>
> **OAuth 2.0 metrics labels**
>
> | Label        | Values                                                                                                                                                                                   |
> | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | `grant-type` | * `authorization-code`
>
> * `back-channel`
>
> * `client-credentials`
>
> * `device-code`
>
> * `implicit`
>
> * `jwt-bearer`
>
> * `refresh`
>
> * `resource-owner-password`
>
> * `saml2`
>
> * `token-exchange` |
> | `outcome`    | - `success`
>
> - `failure`                                                                                                                                                                 |
> | `token-type` | * `access-token`
>
> * `authorization-code`
>
> * `device-code`
>
> * `id-token`
>
> * `ops`
>
> * `permission-ticket`
>
> * `refresh-token`                                                               |

## Session metrics

Advanced Identity Cloud exposes the following session-related monitoring metrics:

> **Collapse: Prometheus session metrics**
>
> | Name                                                                                                           | Type    | Description                                                                                                     |
> | -------------------------------------------------------------------------------------------------------------- | ------- | --------------------------------------------------------------------------------------------------------------- |
> | `am_session_count{operation=session-operation,outcome=session-outcome,session_type=session-type,}`             | Summary | Rate of successful/unsuccessful sessions for idle/max timeout and time taken to perform this operation (count). |
> | `am_session_cts_based_cache_count{outcome=session-outcome,}`                                                   | Summary | Number of cache hits/misses in the session cache (count).                                                       |
> | `am_session_cts_based_cache_eviction_count`                                                                    | Summary | Rate of evictions from the session cache.                                                                       |
> | `am_session_cts_based_cache_eviction_sum`                                                                      | Summary | Rate of evictions from the session cache (total).                                                               |
> | `am_session_cts_based_cache_size`                                                                              | Gauge   | Number of sessions in the session cache.                                                                        |
> | `am_session_cts_based_cache_sum{outcome=session-outcome,}`                                                     | Summary | Number of cache hits/misses in the session cache (total).                                                       |
> | `am_session_lifetime_count{session_type=session-type,}`                                                        | Summary | Rate of session lifetimes (count).                                                                              |
> | `am_session_lifetime_seconds_sum{session_type=session-type,}`                                                  | Summary | Lifetime of session, by session type (total).                                                                   |
> | `am_session_lifetime_seconds{session_type=session-type,quantile=quantile,}`                                    | Summary | Lifetime of session, by session type.                                                                           |
> | `am_session_seconds_sum{operation=session-operation,outcome=outcome,session_type=session-type,}`               | Summary | Rate of OAuth 2.0 grant completion by grant type (count).                                                       |
> | `am_session_seconds{operation=session-operation,outcome=outcome,session_type=session-type,quantile=quantile,}` | Summary | Tracks service time for successful/unsuccessful sessions by operation and session type.                         |
> | `am_session_store_size{session_type="authentication-in-memory",}`                                              | Gauge   | Number of journey sessions stored in the in-memory authentication session store.                                |
> | `am_session_sum{operation=session-operation,session_type=session-type,}`                                       | Summary | Rate of successful/unsuccessful sessions for idle/max timeout and time taken to perform this operation (total). |
>
> **Session metrics labels**
>
> | Label                    | Values                                                                                                                                                                                                                                                                                                                               |
> | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
> | `operation`              | * `check-exists`
>
> * `create`
>
> * `dereference-restricted-token-id`
>
> * `destroy`
>
> * `get-matching-sessions`
>
> * `get-restricted-token-id`
>
> * `get-valid-sessions`
>
> * `is-applicable`
>
> * `logout`
>
> * `refresh`
>
> * `register-listener`
>
> * `register-pll-listener`
>
> * `resolve`
>
> * `set-external-property`
>
> * `set-property`
>
> * `validate` |
> | `outcome`                | - `success`
>
> - `failure`                                                                                                                                                                                                                                                                                                             |
> | `` `session-operation `` | * `idle-timeout`
>
> * `max-timeout`                                                                                                                                                                                                                                                                                                    |
> | `session-outcome`        | - `hit`
>
> - `miss`                                                                                                                                                                                                                                                                                                                    |
> | `session-type`           | * `authentication-client-based`
>
> * `authentication-cts-based`
>
> * `authentication-in-memory`
>
> * `client-based`
>
> * `cts-based`                                                                                                                                                                                                         |

## Script cache metrics

Advanced Identity Cloud exposes the following metrics for monitoring [script caches](../am-scripting/cache-manager.html):

> **Collapse: Prometheus script cache metrics**
>
> | Name                                | Type  | Description                                                                                                     |
> | ----------------------------------- | ----- | --------------------------------------------------------------------------------------------------------------- |
> | `am_script_cache_eviction`          | Gauge | Returns the number of times an entry has been evicted. This count doesn't include manual invalidations.         |
> | `am_script_cache_hit`               | Gauge | The number of times cache lookup methods have returned a cached value.                                          |
> | `am_script_cache_invalidate`        | Gauge | The number of times the `invalidate` method has been called on the cache to manually invalidate a key.          |
> | `am_script_cache_invalidate_all`    | Gauge | The number of times the `invalidateAll` method has been called on the cache to manually invalidate all entries. |
> | `am_script_cache_load_failure`      | Gauge | The number of times Cache lookup methods threw an exception while loading a new value.                          |
> | `am_script_cache_load_time_seconds` | Gauge | The total number of seconds the cache has spent loading new values.                                             |
> | `am_script_cache_load_count`        | Gauge | The total number of times that Cache lookup methods attempted to load new values.                               |
> | `am_script_cache_memory_bytes`      | Gauge | The estimated memory size of the cache in bytes.                                                                |
> | `am_script_cache_miss`              | Gauge | The number of times cache lookup methods have returned an uncached (newly loaded) value, or null.               |
> | `am_script_cache_size`              | Gauge | The approximate number of entries in the cache.                                                                 |

---

---
title: Configure services
description: Global and per-realm service configuration settings
component: pingoneaic
page_id: pingoneaic:am-reference:services-configuration
canonical_url: https://docs.pingidentity.com/pingoneaic/am-reference/services-configuration.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Realm", "Configuration"]
page_aliases: ["reference:realm-services-configuration.adoc", "realm-services-configuration.adoc", "release-notes:rapid-channel/http-client-service.adoc"]
section_ids:
  global_services: Global services
  global-corsservice: CORS Service
  global-corsservice-configuration: Configuration
  global-corsservice-secondary-config: Secondary Configurations
  global-corsservice-secondary-config-configuration: configuration
  global-dashboard: Dashboard
  global-dashboard-realm-defaults: Realm Defaults
  global-dashboard-secondary-config: Secondary Configurations
  global-dashboard-secondary-config-instances: instances
  realm_services: Realm services
  realm-androidkeyattestation: Android Key Attestation Service
  realm-baseurl: Base URL Source
  cachemanager-service: Cache Manager service
  cachemanager-service-configuration: Configuration
  cachemanager-service-secondary: Secondary configurations
  realm-devicebindingservice: Device Binding service
  realm-deviceprofilesservice: Device Profiles Service
  realm-email: Email Service
  realm-email-secondary-config: Secondary configurations
  realm-email-secondary-config-ms: Microsoft Graph API
  realm-email-secondary-config-smtp: SMTP
  realm-authenticatoroathservice: ForgeRock Authenticator (OATH) Service
  realm-authenticatorpushservice: ForgeRock Authenticator (Push) Service
  realm-globalization: Globalization Settings
  realm-httpclient: Http Client service
  httpclient-realm-defaults: Realm defaults
  httpclient-secondary-config: Secondary configurations
  httpclient-secondary-config-configuration: Configuration
  global-httpclient-secondary-config-tlsconfiguration: TLS Configuration
  httpclient-secondary-config-timeouts: Timeouts
  httpclient-secondary-config-proxy: Proxy Configuration
  realm-identity-assertion: Identity Assertion service
  realm-identity-assertion-configuration: Configuration
  global-identity-assertion-secondary-config: Secondary configurations
  realm-iot: IoT Service
  realm-oauth-oidc: OAuth 2.0 provider
  realm-oauth-oidc-core: Core
  realm-oauth-oidc-advanced: Advanced
  realm-oauth-oidc-client-dynamic-registration: Client Dynamic Registration
  realm-oauth-oidc-openid-connect: OpenID Connect
  realm-oauth-oidc-advanced-openid-connect: Advanced OpenID Connect
  realm-oauth-oidc-device-flow: Device Flow
  realm-oauth-oidc-consent: Consent
  realm-oauth-oidc-ciba: CIBA
  realm-oauth-oidc-plugins: Plugins
  realm-osconfigurationsservice: OneSpan Configuration
  realm-pingone-worker-service: PingOne Worker service
  configuration: Configuration
  realm-pingone-worker-service-secondary-config: Secondary Configurations
  test-connection: Test the connection
  realm-policyconfiguration: Policy Configuration
  realm-pushnotification: Push Notification Service
  realm-remoteconsentservice: Remote Consent Service
  realm-selfservicetrees: Self Service Trees
  realm-selfservicetrees-realm-attributes: Realm Attributes
  realm-selfservicetrees-tree-mapping: Tree Mapping
  realm-session: Session
  realm-session-dynamic-attributes: Dynamic Attributes
  realm-amsessionpropertywhitelist: Session Property Whitelist Service
  realm-socialauthentication: Social Authentication Implementations
  realm-socialidentityproviders: Social Identity Provider Service
  realm-socialidentityproviders-configuration: Configuration
  realm-socialidentityproviders-secondary-config: Secondary Configurations
  realm-transaction: Transaction Authentication Service
  realm-user: User
  realm-user-dynamic-attributes: Dynamic Attributes
  realm-validation: Validation Service
  realm-authenticatorwebauthnservice: WebAuthn Profile Encryption Service
  webauthn-metadata-service: WebAuthn Metadata service
---

# Configure services

You can configure services globally or per realm. Global services affect all realms in Advanced Identity Cloud. Realm services affect only the realm in which they're configured.

## Global services

Under Native Consoles > Access Management > Configure > Global Services, locate the CORS Service and the Dashboard service.

These services affect all realms in Advanced Identity Cloud.

### CORS Service

#### Configuration

The following settings appear on the **Configuration** tab:

* Enable the CORS filter

  If disable, no CORS headers will be added to responses.

  Default value: `true`

#### Secondary Configurations

This service has the following Secondary Configurations.

##### configuration

* Enable the CORS filter

  If disable, no CORS headers will be added to responses.

  Default value: `false`

* Accepted Origins

  The set of accepted origins.

* Accepted Methods

  The set of (non-simple) accepted methods, included in the pre-flight response in the header Access-Control-Allow-Methods.

* Accepted Headers

  The set of (non-simple) accepted headers, included in the pre-flight response in the header Access-Control-Allow-Headers.

* Exposed Headers

  The set of headers to transmit in the header Access-Control-Expose-Headers.

* Max Age

  The max age (in seconds) for caching, included in the pre-flight response in the header Access-Control-Max-Age.

  Default value: `0`

* Allow Credentials

  Whether to transmit the Access-Control-Allow-Credentials: true header in the response.

  Default value: `false`

### Dashboard

#### Realm Defaults

The following settings appear on the **Realm Defaults** tab:

* Available Dashboard Apps

  List of application dashboard names available by default for realms with the Dashboard service configured.

#### Secondary Configurations

This service has the following Secondary Configurations.

##### instances

* Dashboard Class Name

  Identifies how to access the application, for example `SAML2ApplicationClass` for a SAML 2.0 application.

* Dashboard Name

  The application name as it will appear to the administrator for configuring the dashboard.

* Dashboard Display Name

  The application name that displays on the dashboard client.

* Dashboard Icon

  The icon name that will be displayed on the dashboard client identifying the application.

* Dashboard Login

  The URL that takes the user to the application.

* ICF Identifier

  Identifier used by the ForgeRock Identity Connector Framework (ICF).

## Realm services

Under Native Consoles > Access Management > Realms > *Realm Name* > Services, you can enable, remove, or configure services for individual realms.

### Android Key Attestation Service

The following settings are available in this service:

* Cache duration (hours)

  The number of hours to cache the certificate revocation status list and Google hardware attestation root certificate.

  Defaults to one day (`24`).

  Specify `0` to prevent caching.

* Certificate revocation status list URL

  The URL to retrieve the certificate revocation status list (CRL).

  Keys are checked against the revocation status list to ensure they have not been revoked or suspended.

  Keys can be revoked for a number of reasons, including mishandling or suspected extraction by an attacker.

  Defaults to `https://android.googleapis.com/attestation/status` - a list maintained by Google.

* Google hardware attestation root certificate URL

  The URL for retrieving the Google hardware attestation root certificates.

  Refer to [Verifying hardware-backed key pairs with Key Attestation](https://developer.android.com/training/articles/security-key-attestation#root_certificate) in the Android developer documentation.

  If you do not provide a URL, you must map the certificate using the secret label `am.services.attestation.google.public.key`.

  For more information, refer to [Use ESVs for signing and encryption keys](../tenants/esvs-signing-encryption.html).

### Base URL Source

The following settings are available in this service:

* Base URL Source

  Specifies how the base URL is generated.

  The following values are supported:

  * **Extension class** (`EXTENSION_CLASS`). The extension class returns a base URL from a provided HttpServletRequest. In the Extension class name field, enter `org.forgerock.openam.services.baseurl.BaseURLProvider`.

  * **Fixed value** (`FIXED_VALUE`). The base URL is retrieved from the value specified in the Fixed value base URL field.

  * **Forwarded header** (`FORWARDED_HEADER`). The base URL is retrieved from a forwarded header field in the HTTP request. The Forwarded HTTP header field is standardized and specified in [RFC7239](https://www.rfc-editor.org/info/rfc7239).

  * **Host/protocol from incoming request** (`REQUEST_VALUES`). The hostname, server name, and port are retrieved from the incoming HTTP request.

  * **X-Forwarded-\* headers** (`X_FORWARDED_HEADERS`). The base URL is retrieved from non-standard header fields, such as `X-Forwarded-For`, `X-Forwarded-By`, `X-Forwarded-Proto`, `X-Forwarded-Host` and `X-Forwarded-Port`.

    If the `X-Forwarded-Proto` header is not provided, the server uses a fallback scheme, based on the URI of the request.

    If multiple `X-Forwarded-Host` headers are specified, the outermost proxy host is used.

  Default value: `REQUEST_VALUES`

### Cache Manager service

#### Configuration

* Enabled

  Enable the Cache Manager Service. If not enabled, entries are computed but never stored, so that each entry is reloaded each time it's requested.

  Learn about using the Cache Manager service in [Cache script values](../am-scripting/cache-manager.html).

  Default value: Not enabled

#### Secondary configurations

Configure instances of the Cache Manager service. You can create multiple caches within each realm. The total size for all caches in a realm is limited to 20MB, and each cache entry can't exceed 5KB.

* Loading Script

  The script that's used to load cache entries. The script type must be `Cache Loader`, and it should have a `load()` function, and optionally, a `reload()` function.

  Default value: `--- Select a script ---`

- Eviction Policy

  The eviction policy used to determine when to remove or reload entries from the cache.

  The possible values are as follows:

  * `Expire after access`: Entries expire and are removed from the cache after a period of inactivity determined by the Eviction Period. After this time, the cache `load()` function runs.

    Entries remain in the cache indefinitely if they're continuously accessed within this time.

  * `Expire after write`: After the eviction period, entries expire and are removed from the cache. If the cache entry is accessed again, the `load()` function runs.

  * `Refresh after write`: After the eviction period, the `reload()` function runs.

  * `Never`: The cache entry isn't set to expire.

  Default value: `Expire after write`

- Duration Unit

  The unit of time for the eviction period. Possible values are `Seconds`, `Minutes`, or `Hours`.

  This setting is ignored if the eviction policy is set to `Never`.

  Default value: `Hours`

- Eviction Period

  The period of time after which entries are evicted or reloaded from the cache.

  This setting is ignored if the eviction policy is set to `Never`.

  Default value: `1`

### Device Binding service

The following settings are available in this service:

* Device Binding Attribute

  The user's attribute in which to store bound device data.

  Advanced Identity Cloud must be able to write to the attribute.

  Default value: `boundDevices`

* Device Binding Encryption Scheme

  Encryption scheme to use to secure device binding data stored on the server.

  Advanced Identity Cloud encrypts the data for each bound device using a unique random secret key with the selected AES encryption standard in CBC mode with PKCS#5 padding. An HMAC-SHA of the selected strength (truncated to half-size) protects the integrity and authenticity of the encryption. Advanced Identity Cloud encrypts the unique random key with the given RSA key pair and stores it with the bound device data.

  The possible values for this property are:

  * Label: **AES-256/HMAC-SHA-512 with RSA Key Wrapping** (value: `RSAES_AES256CBC_HS512`)

  * Label: **AES-128/HMAC-SHA-256 with RSA Key Wrapping** (value: `RSAES_AES128CBC_HS256`)

  * Label: **No encryption of device settings** (value: `NONE`)

  Default value: `NONE`

* Encryption Key Store

  Path to the key store from which to load encryption keys.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Updating this setting isn't currently supported in Advanced Identity Cloud. Changing its value may lead to a loss of functionality in this feature.For greater security, store encryption key information in [ESVs](../tenants/esvs-signing-encryption.html), instead of in the configuration. Use the [secret label](secret-id-mappings.html#encrypted-device-storage-secret-labels) `am.services.devicebinding.encryption` to map an alias for Device Binding service secrets.If you update encryption key information in the configuration or in the secret stores, users with existing device profiles will no longer be able to log in using this service. If you update encryption key information in the configuration or in the secret stores, users with existing device profiles will no longer be able to log in using this service. Delete the end user's device profile so that they can create a new one when they next log in. |

  |   |                                                                                                                                                                 |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If Advanced Identity Cloud finds a matching secret for the `am.services.devicebinding.encryption` label in the realm's ESV secret store, this value is ignored. |

  Default value: `/path/to/openam/security/keystores/keystore.jks`

* Key Store Type

  Type of key store to load.

  |   |                                                                                                  |
  | - | ------------------------------------------------------------------------------------------------ |
  |   | This property is preconfigured in your Advanced Identity Cloud tenant and should not be altered. |

  Default value: `JKS`

* Key Store Password

  Password to unlock the key store. This password is encrypted when it is saved in the Advanced Identity Cloud configuration. You should modify the default value.

  |   |                                                                                                                                                                 |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If Advanced Identity Cloud finds a matching secret for the `am.services.devicebinding.encryption` label in the realm's ESV secret store, this value is ignored. |

* Key-Pair Alias

  Alias of the certificate and private key in the key store. The private key is used to encrypt and decrypt bound device data.

  |   |                                                                                                                                                                 |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If Advanced Identity Cloud finds a matching secret for the `am.services.devicebinding.encryption` label in the realm's ESV secret store, this value is ignored. |

* Private Key Password

  Password to unlock the private key.

  |   |                                                                                                                                                                 |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If Advanced Identity Cloud finds a matching secret for the `am.services.devicebinding.encryption` label in the realm's ESV secret store, this value is ignored. |

### Device Profiles Service

The following settings are available in this service:

* Profile Storage Attribute

  The user's attribute in which to store Device profiles.

* Device Profile Encryption Scheme

  Encryption scheme to use to secure device profiles stored on the server.

  If enabled, each device profile is encrypted using a unique random secret key using the given strength of AES encryption in CBC mode with PKCS#5 padding. An HMAC-SHA of the given strength (truncated to half-size) is used to ensure integrity protection and authenticated encryption. The unique random key is encrypted with the given RSA key pair and stored with the device profile.

  |   |                                                                              |
  | - | ---------------------------------------------------------------------------- |
  |   | AES-256 may require installation of the JCE Unlimited Strength policy files. |

  The possible values for this property are:

  * Label: **AES-256/HMAC-SHA-512 with RSA Key Wrapping** (Value: `RSAES_AES256CBC_HS512`)

  * Label: **AES-128/HMAC-SHA-256 with RSA Key Wrapping** (Value: `RSAES_AES128CBC_HS256`)

  * Label: **No encryption of device settings.** (Value: `NONE`)

* Encryption Key Store

  Path to the key store from which to load encryption keys.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Updating this setting isn't currently supported in Advanced Identity Cloud. Changing its value may lead to a loss of functionality in this feature.For greater security, store encryption key information in [ESVs](../tenants/esvs-signing-encryption.html), instead of in the configuration. Use the [secret label](secret-id-mappings.html#encrypted-device-storage-secret-labels) `am.services.deviceprofile.encryption` to map an alias for Device Profiles service secrets.If you update encryption key information in the configuration or in the secret stores, users with existing device profiles will no longer be able to log in using this service. Delete the end user's device profile so that they can create a new one when they next log in. |

  |   |                                                                                                                                                                 |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If Advanced Identity Cloud finds a matching secret for the `am.services.deviceprofile.encryption` label in the realm's ESV secret store, this value is ignored. |

* Key Store Type

  Type of key store to load.

  Refer to the [JDK 8 PKCS#11 Reference Guide](https://docs.oracle.com/javase/8/docs/technotes/guides/security/p11guide.html) for more details.

  The possible values for this property are:

  * Label: **Java Key Store (JKS).** (Value: `JKS`)

  * Label: **Java Cryptography Extension Key Store (JCEKS).** (Value: `JCEKS`)

  * Label: **PKCS#11 Hardware Crypto Storage.** (Value: `PKCS11`)

  * Label: **PKCS#12 Key Store.** (Value: `PKCS12`)

* Key Store Password

  Password to unlock the key store. This password is encrypted when it is saved in the Advanced Identity Cloud configuration.

  |   |                                                                                                                                                                 |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If Advanced Identity Cloud finds a matching secret for the `am.services.deviceprofile.encryption` label in the realm's ESV secret store, this value is ignored. |

* Key-Pair Alias

  Alias of the certificate and private key in the key store. The private key is used to encrypt and decrypt device profiles.

  |   |                                                                                                                                                                 |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If Advanced Identity Cloud finds a matching secret for the `am.services.deviceprofile.encryption` label in the realm's ESV secret store, this value is ignored. |

* Private Key Password

  Password to unlock the private key.

  |   |                                                                                                                                                                 |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If Advanced Identity Cloud finds a matching secret for the `am.services.deviceprofile.encryption` label in the realm's ESV secret store, this value is ignored. |

### Email Service

|   |                                                                     |
| - | ------------------------------------------------------------------- |
|   | The Email Service is not currently used in Advanced Identity Cloud. |

The following settings are available in this service:

* Email From Address

  Specifies the address from which to send email notifications.

  For example, you might set this property to: no-reply\@example.com

  For Microsoft Graph API transport configurations, this must exist as a valid address in the Microsoft Exchange administration center.

* Email Attribute Name

  Specifies the profile attribute from which to retrieve the end user's email address.

  Default value: `mail`

* Email Subject

  Specifies a subject for notification messages. If you do not set this, Advanced Identity Cloud does not set the subject for notification messages.

* Email Content

  Specifies content for notification messages. If you do not set this, Advanced Identity Cloud includes only the confirmation URL in the mail body.

* Email Rate Limit

  Specifies the minimum number of seconds that must elapse between sending emails to an individual user.

  Default value: `1`

* Transport Type

  The mail server transport type to use. This value must be set to one of the secondary configurations.

#### Secondary configurations

This service has the following secondary configurations.

##### Microsoft Graph API

* Email Message Implementation Class

  Specifies the class that sends email notifications, such as those sent for user registration and forgotten passwords.

  Default value: `org.forgerock.openam.services.email.rest.MicrosoftRestMailServer`

* Email Rest Endpoint URL

  Specifies the REST endpoint for sending emails, in the format `https://graph.microsoft.com/v1.0/users/USER ID/sendMail`.

  Refer to the [sendMail API reference](https://learn.microsoft.com/en-us/graph/api/user-sendmail?view=graph-rest-1.0\&tabs=http) for details.

* OAuth2 Token Endpoint URL

  Specifies the endpoint for OAuth 2.0 authentication, in the format `https://login.microsoftonline.com/TENANT ID/oauth2/v2.0/token`.

* OAuth2 Client Id

  Specifies the client ID for use in OAuth 2.0 authentication.

  This is the client ID or application ID provided by the Microsoft Application Registration portal.

* OAuth2 Scopes

  Specifies the scopes to request as part of the OAuth 2.0 authentication.

  The value supported by Microsoft Graph API is `https://graph.microsoft.com/.default`.

##### SMTP

* Email Message Implementation Class

  Specifies the class that sends email notifications, such as those sent for user registration and forgotten passwords.

* Mail Server Host Name

  Specifies the fully qualified domain name of the SMTP mail server through which to send email notifications.

  For example, you might set this property to: smtp.example.com

* Mail Server Host Port

  Specifies the port number for the SMTP mail server.

* Mail Server Authentication Username

  Specifies the username for the SMTP mail server.

  For example, you might set this property to: username

* Mail Server Authentication Password

  Specifies the password for the SMTP username.

* Mail Server Secure Connection

  Specifies whether to connect to the SMTP mail server using SSL.

  The possible values for this property are:

  * `SSL`

  * `Non SSL`

  * `Start TLS`

### ForgeRock Authenticator (OATH) Service

The following settings are available in this service:

* Profile Storage Attribute

  Attribute for storing ForgeRock Authenticator OATH profiles.

* Device Profile Encryption Scheme

  Encryption scheme for securing device profiles stored on the server.

  If enabled, each device profile is encrypted using a unique random secret key using the given strength of AES encryption in CBC mode with PKCS#5 padding. An HMAC-SHA of the given strength (truncated to half-size) is used to ensure integrity protection and authenticated encryption. The unique random key is encrypted with the given RSA key pair and stored with the device profile.

  |   |                                                                              |
  | - | ---------------------------------------------------------------------------- |
  |   | AES-256 may require installation of the JCE Unlimited Strength policy files. |

  The possible values for this property are:

  * Label: **AES-256/HMAC-SHA-512 with RSA Key Wrapping** (Value: `RSAES_AES256CBC_HS512`)

  * Label: **AES-128/HMAC-SHA-256 with RSA Key Wrapping** (Value: `RSAES_AES128CBC_HS256`)

  * Label: **No encryption of device settings.** (Value: `NONE`)

* Encryption Key Store

  Path to the key store from which to load encryption keys.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Updating this setting isn't currently supported in Advanced Identity Cloud. Changing its value may lead to a loss of functionality in this feature.For greater security, store encryption key information in [ESVs](../tenants/esvs-signing-encryption.html), instead of in the configuration. Use the [secret label](secret-id-mappings.html#encrypted-device-storage-secret-labels) `am.services.authenticatoroath.encryption` to map an alias for ForgeRock Authenticator (OATH) service secrets.If you update encryption key information, users with existing device profiles won't be able to log in using this service. Delete the end user's device profile so that they can create a new one when they next log in. |

  |   |                                                                                                                                                                     |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If Advanced Identity Cloud finds a matching secret for the `am.services.authenticatoroath.encryption` label in the realm's ESV secret store, this value is ignored. |

* Key Store Type

  Type of encryption key store.

  Refer to the [JDK 8 PKCS#11 Reference Guide](https://docs.oracle.com/javase/8/docs/technotes/guides/security/p11guide.html) for more details.

  The possible values for this property are:

  * Label: **Java Key Store (JKS).** (Value: `JKS`)

  * Label: **Java Cryptography Extension Key Store (JCEKS).** (Value: `JCEKS`)

  * Label: **PKCS#11 Hardware Crypto Storage.** (Value: `PKCS11`)

  * Label: **PKCS#12 Key Store.** (Value: `PKCS12`)

  |   |                                                                                                                                                                     |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If Advanced Identity Cloud finds a matching secret for the `am.services.authenticatoroath.encryption` label in the realm's ESV secret store, this value is ignored. |

* Key Store Password

  Password to unlock the key store. This password will be encrypted.

  |   |                                                                                                                                                                     |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If Advanced Identity Cloud finds a matching secret for the `am.services.authenticatoroath.encryption` label in the realm's ESV secret store, this value is ignored. |

* Key-Pair Alias

  Alias of the certificate and private key in the key store. The private key is used to encrypt and decrypt device profiles.

  |   |                                                                                                                                                                     |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If Advanced Identity Cloud finds a matching secret for the `am.services.authenticatoroath.encryption` label in the realm's ESV secret store, this value is ignored. |

* Private Key Password

  Password to unlock the private key.

  |   |                                                                                                                                                                     |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If Advanced Identity Cloud finds a matching secret for the `am.services.authenticatoroath.encryption` label in the realm's ESV secret store, this value is ignored. |

* ForgeRock Authenticator (OATH) Device Skippable Attribute Name

  The data store attribute that holds the user's decision to enable or disable obtaining and providing a password obtained from an authenticator app. This attribute must be writeable.

### ForgeRock Authenticator (Push) Service

The following settings are available in this service:

* Profile Storage Attribute

  The user's attribute in which to store Push Notification profiles.

* Device Profile Encryption Scheme

  Encryption scheme to use to secure device profiles stored on the server.

  If enabled, each device profile is encrypted using a unique random secret key using the given strength of AES encryption in CBC mode with PKCS#5 padding. An HMAC-SHA of the given strength (truncated to half-size) is used to ensure integrity protection and authenticated encryption. The unique random key is encrypted with the given RSA key pair and stored with the device profile.

  |   |                                                                              |
  | - | ---------------------------------------------------------------------------- |
  |   | AES-256 may require installation of the JCE Unlimited Strength policy files. |

  The possible values for this property are:

  * Label: **AES-256/HMAC-SHA-512 with RSA Key Wrapping** (Value: `RSAES_AES256CBC_HS512`)

  * Label: **AES-128/HMAC-SHA-256 with RSA Key Wrapping** (Value: `RSAES_AES128CBC_HS256`)

  * Label: **No encryption of device settings.** (Value: `NONE`)

* Encryption Key Store

  Path to the key store from which to load encryption keys.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Updating this setting isn't currently supported in Advanced Identity Cloud. Changing its value may lead to a loss of functionality in this feature.For greater security, store encryption key information in [ESVs](../tenants/esvs-signing-encryption.html), instead of in the configuration. Use the [secret label](secret-id-mappings.html#encrypted-device-storage-secret-labels) `am.services.authenticatorpush.encryption` to map an alias for ForgeRock Authenticator (Push) service secrets.If you update encryption key information in the configuration or in the secret stores, users with existing device profiles will no longer be able to log in using this service. Delete the end user's device profile so that they can create a new one when they next log in. |

  |   |                                                                                                                                                                     |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If Advanced Identity Cloud finds a matching secret for the `am.services.authenticatorpush.encryption` label in the realm's ESV secret store, this value is ignored. |

* Key Store Type

  Type of key store to load.

  Refer to the [JDK 8 PKCS#11 Reference Guide](https://docs.oracle.com/javase/8/docs/technotes/guides/security/p11guide.html) for more details.

  The possible values for this property are:

  * Label: **Java Key Store (JKS).** (Value: `JKS`)

  * Label: **Java Cryptography Extension Key Store (JCEKS).** (Value: `JCEKS`)

  * Label: **PKCS#11 Hardware Crypto Storage.** (Value: `PKCS11`)

  * Label: **PKCS#12 Key Store.** (Value: `PKCS12`)

  |   |                                                                                                                                                                     |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If Advanced Identity Cloud finds a matching secret for the `am.services.authenticatorpush.encryption` label in the realm's ESV secret store, this value is ignored. |

* Key Store Password

  Password to unlock the key store. This password is encrypted when it is saved in the Advanced Identity Cloud configuration.

  |   |                                                                                                                                                                     |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If Advanced Identity Cloud finds a matching secret for the `am.services.authenticatorpush.encryption` label in the realm's ESV secret store, this value is ignored. |

* Key-Pair Alias

  Alias of the certificate and private key in the key store. The private key is used to encrypt and decrypt device profiles.

  |   |                                                                                                                                                                     |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If Advanced Identity Cloud finds a matching secret for the `am.services.authenticatorpush.encryption` label in the realm's ESV secret store, this value is ignored. |

* Private Key Password

  Password to unlock the private key.

  |   |                                                                                                                                                                     |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If Advanced Identity Cloud finds a matching secret for the `am.services.authenticatorpush.encryption` label in the realm's ESV secret store, this value is ignored. |

* ForgeRock Authenticator (Push) Device Skippable Attribute Name

  The name of the attribute in a user's profile used to store their decision on skipping push authentication.

### Globalization Settings

The following settings are available in this service:

* Auto Generated Common Name Format

  Use this list to configure how Advanced Identity Cloud formats names shown in the console banner.

  This setting lets you customize the name of the authenticated user shown in the UI, based on the user's locale.

### Http Client service

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can use the Http Client service to send an HTTP request over mTLS from within a script, set timeouts, or route a connection through a proxy server.Find out how to configure a service instance as the `clientName` for the `httpClient` script binding in [Send a request using mTLS](../am-scripting/script-bindings.html#httpclient-mtls) and [Route a request through a proxy](../am-scripting/script-bindings.html#httpclient-proxy). |

#### Realm defaults

The following settings appear on the Realm Defaults tab:

* Enabled

  Enable this Http Client service to use the secondary configurations when making HTTP requests.

#### Secondary configurations

This service has the following secondary configurations.

##### Configuration

* Enabled

  Enable this Http Client instance.

##### TLS Configuration

Configure instances of the Http Client service to control how and which certificates Advanced Identity Cloud uses in TLS connections.

* Client Certificate Secret Label Identifier

  Advanced Identity Cloud uses this identifier to create a specific secret label, using the template `am.services.httpclient.mtls.clientcert.identifier.secret` where identifier is the value of Client Certificate Secret Label Identifier.

  The identifier can only contain alphanumeric characters `a-z`, `A-Z`, `0-9`, and periods (`.`). It can't start or end with a period.

  If this field is empty, the Http Client service doesn't attach a client certificate to HTTP requests that use mTLS to connect with a target server.

* Server Trust Certificates Secret Label Identifier

  Advanced Identity Cloud uses this identifier to create a specific secret label, using the template `am.services.httpclient.mtls.servertrustcerts.identifier.secret` where identifier is the value of Server Trust Certificates Secret Label Identifier.

  The identifier can only contain alphanumeric characters `a-z`, `A-Z`, `0-9`, and periods (`.`). It can't start or end with a period.

  If this field is empty, the system truststore is used when attempting to verify the target server's certificate during a TLS connection.

* Disable Certificate Revocation Check

  If enabled, Advanced Identity Cloud doesn't check certificate revocation lists when performing a TLS connection with the target server.

* Trust All Certificates

  If enabled, all certificates are trusted when performing a TLS connection with the target server.

  |   |                                                                                                  |
  | - | ------------------------------------------------------------------------------------------------ |
  |   | Don't enable this setting in a production environment. It is intended for testing purposes only. |

##### Timeouts

* Use Instance Timeouts

  If enabled, Advanced Identity Cloud uses the connection and response timeouts defined in this Http Client service instance.

* Connection Timeout (secs)

  The maximum time (in seconds) to wait for a connection to be established before failing.

  Default value: `10`

* Response Timeout (secs)

  The maximum time (in seconds) to wait for a response from the target server before failing.

  Default value: `10`

##### Proxy Configuration

* Use Instance Proxy

  If enabled, Advanced Identity Cloud uses the proxy settings defined in this instance. Otherwise, Advanced Identity Cloud routes HTTP Client requests using the proxy settings defined in your deployment.

* Proxy URI

  The URI of the proxy server to use for HTTP requests. The format of the URI must be `http://hostname:port` or `https://hostname:port`.

* Proxy Username

  The proxy authentication username, if required.

* Proxy Secret Label Identifier

  The identifier for the proxy authentication secret.

  Advanced Identity Cloud uses this identifier to create a secret label for mapping to a secret in the secret store. The secret label takes the form `am.services.httpclient.proxy.identifier.secret`, where identifier is the value of Proxy Secret Label Identifier. The label can only contain characters `a-z`, `A-Z`, `0-9`, and periods (`.`). It can't start or end with a period.

  If this field is empty, Advanced Identity Cloud doesn't perform proxy authentication.

### Identity Assertion service

#### Configuration

The following settings appear on the Configuration tab:

* Enable

  Enables the Identity Assertion service that lets Advanced Identity Cloud use PingGateway to manage authentication through a third party such as WDSSO or Kerberos.

  When enabled, the servers defined in the secondary configuration become available as options in the [Identity Assertion node](https://docs.pingidentity.com/auth-node-ref/latest/identity-assertion-node.html) configuration.

* Server cache duration (minutes)

  Supports caching of identity assertion server configurations. A value greater than `0` indicates the duration in minutes that the server configurations are cached. A value of `0` disables caching.

#### Secondary configurations

This service has the following secondary configurations.

* Identity Assertion server URL

  The identity assertion server URL, for example, `https://ig.example.com:8448`. Don't include the route in this URL because you define the route when you configure the [Identity Assertion node](https://docs.pingidentity.com/auth-node-ref/latest/identity-assertion-node.html).

* Shared Encryption Secret

  Advanced Identity Cloud uses this identifier to create a specific secret label, using the template `am.services.identityassertion.service.identifier.shared.secret` where identifier is the value of Shared Encryption Secret.

  The identifier can only contain alphanumeric characters `a-z`, `A-Z`, `0-9`, and periods (`.`). It can't start or end with a period.

  The secret is shared by Advanced Identity Cloud and PingGateway to encrypt the assertion request JWT sent to PingGateway and then decrypt the result JWT.

  Learn about mapping secrets in [Map ESV secrets to secret labels](../tenants/esvs-signing-encryption.html#map-esv-secrets-to-secret-labels).

* JWT TTL (seconds)

  The identity assertion request JWT time-to-live duration in seconds. This is the period until the JWT sent to the gateway expires.

* Skew Allowance (seconds)

  The time difference skew allowance to use when validating the assertion result JWT's `issued-at` and `expiry` claims. This is to address time differences between the PingGateway host and the AM hosts.

### IoT Service

The following settings are available in this service:

* Create OAuth 2.0 Client

  Create an OAuth 2.0 Client with the given name and default configuration required to serve as the client for the IoT Service. The client will be created without any scope(s).

* OAuth 2.0 Client Name

  The name of the default OAuth 2.0 Client used by the IoT Service to request access tokens for things.

* Create OAuth 2.0 JWT Issuer

  Create a Trusted JWT Issuer with the given name and default configuration required for the IoT Service to act as the Issuer when handling request for thing access tokens.

* OAuth 2.0 JWT Issuer Name

  The name of the Trusted JWT Issuer used by the IoT Service to request access tokens for things.

* OAuth 2.0 Subject Attribute

  The name of the identity store attribute from which to read the OAuth 2.0 subject value. The subject is used in access tokens issued for things. This allows the thing's access token subject to have a value other than the thing's ID, which is the value used by default.

* Readable Attributes

  Specifies the list of attributes that a thing is allowed to request from its identity.

### OAuth 2.0 provider

#### Core

The following settings appear on the Core tab:

* Use Client-Side Access & Refresh Tokens

  When enabled, Advanced Identity Cloud issues access and refresh tokens that can be inspected by resource servers.

  You can override this setting for individual clients. To access client application settings, go to Native Consoles > Access Management > Realms > *Realm Name* > Applications > OAuth 2.0 > Clients > *Client ID*.

* Use Macaroon Access and Refresh Tokens

  When enabled, AM will issue access and refresh tokens as Macaroons with caveats.

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

  * If a policy returns an action of GRANT=true, the scope is consented automatically, and the user is not consulted in a user-interaction flow.

  * If a policy returns an action of GRANT=false, the scope is not added to any resulting token, and the user will not refer to it in a user-interaction flow.

  * If no policy returns a value for the GRANT action:

    * For user-facing grant types, such as the authorization or device code flows, the user is asked for consent or saved consent is used.

    * For grant types that are not user-facing, such as those using password or client credentials, the scope is not added to any resulting token.

  You can override this setting for individual clients. To access client application settings, go to Native Consoles > Access Management > Realms > *Realm Name* > Applications > OAuth 2.0 > Clients > *Client ID*.

* Scopes Policy Set

  The policy set that defines the context in which policy evaluations occur when `Use Policy Engine for Scope decisions` is enabled on the OAuth 2.0 provider. Leave this field blank, or set it to `oauth2Scopes` to use the default policy set.

  You can override this setting for individual clients. To access client application settings, go to Native Consoles > Access Management > Realms > *Realm Name* > Applications > OAuth 2.0 > Clients > *Client ID*.

  Default value: `[Empty]`

* OAuth2 Access Token May Act Script

  The script that is executed when issuing an access token explicitly to modify the `may_act` claim placed on the token.

  You can override this setting for individual clients. To access client application settings, go to Native Consoles > Access Management > Realms > *Realm Name* > Applications > OAuth 2.0 > Clients > *Client ID*.

  The possible values for this property are:

  * `c735de08-f8f2-4e69-aa4a-2d8d3d438323`. OAuth2 May Act Script

  * `[Empty]`. --- Select a script ---

* OIDC ID Token May Act Script

  The script that is executed when issuing an OIDC ID Token explicitly to modify the `may_act` claim placed on the token.

  You can override this setting for individual clients. To access client application settings, go to Native Consoles > Access Management > Realms > *Realm Name* > Applications > OAuth 2.0 > Clients > *Client ID*.

  The possible values for this property are:

  * `c735de08-f8f2-4e69-aa4a-2d8d3d438323`. OAuth2 May Act Script

  * `[Empty]`. --- Select a script ---

#### Advanced

The following settings appear on the Advanced tab:

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

  |   |                                                                                                |
  | - | ---------------------------------------------------------------------------------------------- |
  |   | The default Advanced Identity Cloud login page is constructed using "Base URL Source" service. |

  You can override this setting for individual clients. To access client application settings, go to Native Consoles > Access Management > Realms > *Realm Name* > Applications > OAuth 2.0 > Clients > *Client ID*.

* Scope Implementation Class

  The class that contains the required scope implementation, must implement the `org.forgerock.oauth2.core.ScopeValidator` interface.

  You can override this setting for individual clients. To access client application settings, go to Native Consoles > Access Management > Realms > *Realm Name* > Applications > OAuth 2.0 > Clients > *Client ID*.

- Additional Audience Values

  The additional audience values that will be permitted when verifying Client Authentication JWTs.

  These audience values will be in addition to the AS base, issuer and endpoint URIs.

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

* OAuth2 Token Signing Algorithm

  Algorithm used to sign client-side OAuth 2.0 tokens in order to detect tampering.

  Advanced Identity Cloud supports the signing algorithms listed in JSON Web Algorithms (JWA): ["alg" (Algorithm) Header Parameter Values for JWS](https://www.rfc-editor.org/rfc/rfc7518.html#section-3.1):

  * `HS256` - HMAC with SHA-256.

  * `HS384` - HMAC with SHA-384.

  * `HS512` - HMAC with SHA-512.

  * `ES256` - ECDSA with SHA-256 and NIST standard P-256 elliptic curve.

  * `ES384` - ECDSA with SHA-384 and NIST standard P-384 elliptic curve.

  * `ES512` - ECDSA with SHA-512 and NIST standard P-521 elliptic curve.

  * `RS256` - RSASSA-PKCS-v1\_5 using SHA-256.

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

* Client-Side Token Compression

  Whether client-side access and refresh tokens should be compressed.

* Encrypt Client-Side Tokens

  Whether client-side access and refresh tokens should be encrypted.

  Enabling token encryption will disable token signing as encryption is performed using direct symmetric encryption.

  You can override this setting for individual clients. To access client application settings, go to Native Consoles > Access Management > Realms > *Realm Name* > Applications > OAuth 2.0 > Clients > *Client ID*.

* Subject Identifier Hash Salt

  If *pairwise* subject types are supported, it is *STRONGLY RECOMMENDED* to change this value. It is used in the salting of hashes for returning specific `sub` claims to individuals using the same `request_uri` or `sector_identifier_uri`.

  |   |                                                                                                                                                                                                                                                                              |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If you map `am.services.oauth2.provider.hash.salt.secret` to a secret in a secret store, Advanced Identity Cloud ignores this value.Learn more about secret labels in [OAuth 2.0 and OpenID Connect provider secrets](secret-id-mappings.html#oauth2-default-secret-labels). |

* Code Verifier Parameter Required

  If enabled, requests using the authorization code grant or device flow require a `code_challenge` attribute to comply with the PKCE standard.

  For more information, read the [PKCE specification](https://www.rfc-editor.org/info/rfc7636).

  Note that if a client specifies a `code_challenge` parameter in the authorization request, PKCE is enabled regardless of the value of this attribute.

  The possible values for this property are:

  * `true`. All requests

  * `public`. Requests from all public clients

  * `passwordless`. Requests from all passwordless public clients

  * `false`. No requests

* Modified Timestamp Attribute Name

  The identity Data Store attribute used to return modified timestamp values.

  This attribute is paired together with the *Created Timestamp Attribute Name* attribute (`createdTimestampAttribute`). You can leave both attributes unset (default) or set them both. If you set only one attribute and leave the other blank, the access token fails with a 500 error.

  For example, when you configure Advanced Identity Cloud as an OIDC Provider in a Mobile Connect application, the client accesses the `userinfo` endpoint to obtain the `updated_at` claim value in the ID token. The `updated_at` claim gets its value from the `modifiedTimestampAttribute` attribute in the user profile. If the profile has never been modified, the `updated_at` claim uses the `createdTimestampAttribute` attribute.

* Created Timestamp Attribute Name

  The identity Data Store attribute used to return created timestamp values.

* Password Grant Authentication Service

  The journey used to authenticate the username and password for the [Resource owner password credentials grant](../am-oauth2/oauth2-ropc-grant.html).

  The list of possible values for this property reflects the list of configured authentication journeys.

  Don't change the default value (`PasswordGrant`) unless you have configured a suitable replacement journey.

* Enable Auth Module Messages for Password Credentials Grant

  This property doesn't apply to Advanced Identity Cloud.

* Grant Types

  The set of Grant Types (OAuth 2.0 flows) this client can use.

  If you don't set any Grant Types here, the client can't use any OAuth 2.0 flows.

* Trusted TLS Client Certificate Header

  HTTP Header to receive TLS client certificates when TLS is terminated at a proxy.

  Leave blank if not terminating TLS at a proxy. Configure the proxy to strip this header from incoming requests. Best practice is to use a random string.

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

  PEM-encoded certificate to use to verify OCSP responses.

  If specified this certificate will be used to verify the signature on all OCSP responses. Otherwise the appropriate certificate will be determined from the trusted CA certificates.

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

  If set to a value greater than 0, and either `nbf` or `exp` is not defined, the JWT is validated successfully, providing the claims are not required.

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

  For information about the PAR flow, refer to [Authorization code grant with PAR](../am-oauth2/oauth2-authz-grant-par.html).

  Default value: `90`

- Require Pushed Authorization Requests

  If enabled, clients must use the PAR endpoint to initiate authorization requests, otherwise Advanced Identity Cloud returns an error indicating a missing or invalid request object.

  This applies to *all* clients, including clients that aren't configured to require PAR.

  You can also set this independently for individual clients under Native Consoles > Access Management. Go to Realms > *Realm Name* > Applications > OAuth 2.0 > Clients > *Client ID*.

  Default value: `false`

* Refresh Token Grace Period (seconds)

  The time, in seconds, that a refresh token can be reused. This grace period lets OAuth 2.0 clients recover seamlessly if the response from an original refresh token request is not received because of a network problem or other transient issue. During the grace period, the refresh token can be reused multiple times, if the network problem persists. When the grace period ends, the refresh token is revoked.

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

  If this setting is `true`, Advanced Identity Cloud validates audience parameter values in token exchange requests against the values defined in Allowed Resource Server Audience Values.

  If validation fails, the token exchange request is rejected.

  Find more information in [The `aud` claim](../am-oauth2/token-exchange.html#aud-claim).

* Allowed Resource Server Audience Values

  List of audience (`aud`) claim values that are allowed for resource servers.

  The value(s) must match those expected by the resource server for which the access tokens are requested.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | This property is different to the [Additional Audience Values](#oauth-provider-additional-audience-values) property of the OAuth 2.0 provider service, which lists values for the authorization server (Advanced Identity Cloud) when a JWT is sent to Advanced Identity Cloud as the OAuth 2.0 request parameter. The Allowed Resource Server Audience Values property reflects allowed values for the *resource server* where Advanced Identity Cloud generates a JWT and returns it to the client. |

- Use token\_introspection claim for JWT

  Specifies whether Advanced Identity Cloud wraps the introspected token's claims inside a `token_introspection` claim in the JWT introspection response, as required by RFC 9701.

  When enabled, Advanced Identity Cloud separates the JWT's own top-level claims (`iss`, `aud`, `iat`) from the introspected token's claims, which appear inside `token_introspection`. The `aud` claim of the introspected token is always included.

  When disabled, Advanced Identity Cloud returns a flat JWT structure and omits the `aud` claim from the response.

  Learn more in [RFC 9701 token\_introspection claim](../am-oauth2/oauth2-introspect-endpoint.html#rfc-9701-token-introspection-claim).

  Default: Not enabled

#### Client Dynamic Registration

The following settings appear on the Client Dynamic Registration tab:

* Require Software Statement for Dynamic Client Registration

  When enabled, a software statement JWT containing at least the `iss` (issuer) claim must be provided when registering an OAuth 2.0 client dynamically.

* Required Software Statement Attested Attributes

  The client attributes that must be present in the software statement JWT when registering an OAuth 2.0 client dynamically. Applies only if you enable Require Software Statements for Dynamic Client Registration.

  Leave blank to allow any attributes to be present.

* Allow Open Dynamic Client Registration

  Allow clients to register without an access token. If enabled, consider adding some form of rate limiting. For details, refer to [Client Registration](https://openid.net/specs/openid-connect-registration-1_0.html#ClientRegistration) in the OIDC specification.

* Generate Registration Access Tokens

  Whether to generate Registration Access Tokens for clients that register by using open dynamic client registration. Such tokens let the client access the [Client Configuration Endpoint](https://openid.net/specs/openid-connect-registration-1_0.html#ClientConfigurationEndpoint) as per the OpenID Connect specification. This setting has no effect if Allow Open Dynamic Client Registration is disabled.

* Scope to give access to dynamic client registration

  Mandatory scope required when registering a new OAuth2 client.

* Dynamic Client Registration Script

  Provide a script to customize dynamic client registration after a successful create, update, or delete operation.

#### OpenID Connect

The following settings appear on the OpenID Connect tab:

* Overrideable Id\_Token Claims

  List of claims in the ID token that can be overridden in the OIDC claims script. These should be the subset of the core OIDC claims, such as `aud` or `azp`.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | * For information about the core OIDC claims, refer to the [ID Token data structure](https://openid.net/specs/openid-connect-core-1_0.html#IDToken).

  * For details of the OIDC script and how to implement a custom scripted plugin, refer to [OIDC claims](../am-oauth2/plugins-user-info-claims.html).

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

  * `RS256` - RSASSA-PKCS-v1\_5 using SHA-256.

  * `RS384` - RSASSA-PKCS-v1\_5 using SHA-384.

  * `RS512` - RSASSA-PKCS-v1\_5 using SHA-512.

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

  Claims may be entered as simple strings or pipe separated strings representing the internal claim name, locale, and localized description.

  For example: `name|en|Your full name.`.

  Locale strings are in the format: `language + "" + country + "" + variant`, for example `en`, `en_GB`, or `en_US_WIN`. If the locale and pipe is omitted, the description is displayed to all users that have undefined locales.

  If the description is also omitted, nothing is displayed on the consent page for the claim. For example specifying `family_name|` would allow the claim `family_name` to be used by the client, but would not display it to the user on the consent page when requested.

- OpenID Connect JWT Token Lifetime (seconds)

  The amount of time the JWT will be valid for, in seconds.

- OIDC Provider Discovery

  Turns on and off OIDC Discovery endpoint.

#### Advanced OpenID Connect

The following settings appear on the Advanced OpenID Connect tab:

* Remote JSON Web Key URL

  The Remote URL where the provider's JSON Web Key can be retrieved.

  If this setting is not configured, Advanced Identity Cloud provides a local URL to access the public key of the private key used to sign ID tokens.

* JWT Signing kid Header Mappings

  Map custom `kid` header values for JWTs signed with the signing key to the specified secret alias.

  * Key is the secret alias of the key used to sign the given JWT.

  * Value is the custom `kid` value.

  Advanced Identity Cloud only applies custom `kid` mappings if you set a value for Remote JSON Web Key URL. Use these mappings to guarantee that the `kid` header of a signed JWT references the correct key in a remote JWKS.

  If you don't configure a custom `kid` for a JWT signing key, Advanced Identity Cloud generates a default `kid` value.

  Find more information in [Map custom key IDs to secrets](../am-oidc1/managing-jwk_uri.html#map-custom-kids).

* Idtokeninfo Endpoint Requires Client Authentication

  When enabled, the `/oauth2/idtokeninfo` endpoint requires client authentication if the signing algorithm is set to `HS256`, `HS384`, or `HS512`.

* Enable "claims\_parameter\_supported"

  If enabled, clients will be able to request individual claims using the `claims` request parameter, as per [section 5.5 of the OpenID Connect specification](http://openid.net/specs/openid-connect-core-1_0.html#ClaimsParameter).

* OpenID Connect acr\_values to Auth Mapping

  Maps OIDC ACR values to authentication journeys. For details, refer to the [acr\_values parameter](http://openid.net/specs/openid-connect-core-1_0.html#AuthRequest) in the OIDC authentication request specification.

  |   |                                                                                                                                                                        |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Do not configure more than one ACR mapping to the same authentication journey. Doing so can result in misrepresentation of the ACR information in the issued ID token. |

* Default ACR values

  Default requested Authentication Context Class Reference values.

  List of strings that specifies the default acr values that the OP is being requested to use for processing requests from this Client, with the values appearing in order of preference. The Authentication Context Class satisfied by the authentication performed is returned as the acr Claim Value in the issued ID Token. The acr Claim is requested as a Voluntary Claim by this parameter. The acr\_values\_supported discovery element contains a list of the acr values supported by this server. Values specified in the acr\_values request parameter or an individual acr Claim request override these default values.

* OpenID Connect id\_token amr Values to Auth Module Mappings

  This property doesn't apply to Advanced Identity Cloud.

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

  * `RS256` - RSASSA-PKCS-v1\_5 using SHA-256.

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

  Supported JWS Signing Algorithms for 'private\_key\_jwt' JWT based authentication method.

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

  * `RS256` - RSASSA-PKCS-v1\_5 using SHA-256.

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

  * `RS256` - RSASSA-PKCS-v1\_5 using SHA-256.

  * `RS384` - RSASSA-PKCS-v1\_5 using SHA-384.

  * `RS512` - RSASSA-PKCS-v1\_5 using SHA-512.

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

  * `RS256` - RSASSA-PKCS-v1\_5 using SHA-256

  * `RS384` - RSASSA-PKCS1-v1\_5 using SHA-384

  * `RS512` - RSASSA-PKCS1-v1\_5 using SHA-512

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

- Include all kty and alg combinations in jwks\_uri

  By default only distinct kid entries are returned in the jwks\_uri and the alg property is not included. Enabling this flag will result in duplicate kid entries, each one specifying a different kty and alg combination. [RFC7517 distinct key KIDs](https://www.rfc-editor.org/rfc/rfc7517.html#section-4.5)

* Use Force Authentication for prompt=login

  If you specify the `prompt=login` parameter in the URL, Advanced Identity Cloud forces the end user to authenticate even if they already have a valid session. Set the Use Force Authentication for prompt=login property to control how the end user's existing session is handled after reauthentication.

  If you set this property to `false` (the default), Advanced Identity Cloud destroys the existing session and creates a new session on reauthentication.

  If you set this property to `true`, Advanced Identity Cloud performs a [session upgrade](../am-sessions/session-upgrade.html) on reauthentication.

* Use Force Authentication for max\_age

  This property applies only to reauthentication triggered by the Default Max Age property of an OAuth 2.0 client.

  If the age of an end user's session reaches the value set in the Default Max Age property of the client, Advanced Identity Cloud forces the end user to reauthenticate. Set the Use Force Authentication for max\_age property to control how the end user's existing session is handled after reauthentication.

  If this property is `false` (the default) and the user requests authorization after the `max_age` has passed, Advanced Identity Cloud destroys the existing session and creates a new session after reauthentication.

  If this property is `true` and the user requests authorization after the `max_age` has passed, Advanced Identity Cloud performs a [session upgrade](../am-sessions/session-upgrade.html) on reauthentication.

* Minimum max\_age for Authorize Requests

  The minimum `max_age` value that's permitted in an authorization request, in seconds.

  If this property is set too low, it can cause repeated authentication requests if the OIDC flow takes longer to complete than the specified `max_age`.

  Default value: `60`

#### Device Flow

The following settings appear on the Device Flow tab:

* Verification URL

  The URL that the user will be instructed to visit to complete their OAuth 2.0 login and consent when using the device code flow.

* Device Completion URL

  The URL that the user will be sent to on completion of their OAuth 2.0 login and consent when using the device code flow.

* Device Code Lifetime (seconds)

  The lifetime of the device code, in seconds.

* Device Polling Interval

  The polling frequency for devices waiting for tokens when using the device code flow.

* User Code Character Length

  The number of characters in the generated user code.

  Default value: `8`

* User Code Character Set

  The set of characters to be used to generate a user code.

  Consider limitations of low resolution mobile devices when defining a character set. For example, the OAuth 2.0 Device Grant specification recommends removing characters that can be easily confused, such as "0" and "O" or "1", "l" and "I". Refer to [RFC 8628](https://www.rfc-editor.org/rfc/rfc8628.html#section-6.1) for further examples.

  Default value: `234567ACDEFGHJKLMNPQRSTWXYZabcdefhijkmnopqrstwxyz`

* Allow unauthenticated user code entry

  If enabled, during an OAuth 2.0 device code authentication flow, users can access and input a user code without first logging in.

  Default value: `false`

#### Consent

The following settings appear on the Consent tab:

* Saved Consent Attribute Name

  Name of a multi-valued attribute on resource owner profiles where Advanced Identity Cloud can save authorization consent decisions.

  When the resource owner chooses to save the decision to authorize access for a client application, Advanced Identity Cloud updates the resource owner's profile to avoid having to prompt the resource owner to grant authorization when the client issues subsequent authorization requests.

* Allow Clients to Skip Consent

  If enabled, clients may be configured so that the resource owner will not be asked for consent during authorization flows.

  You can override this setting for individual clients. To access client application settings, go to Native Consoles > Access Management > Realms > *Realm Name* > Applications > OAuth 2.0 > Clients > *Client ID*.

* Enable Remote Consent

  Enables consent to be gathered by a separate service.

  You can override this setting for individual clients. To access client application settings, go to Native Consoles > Access Management > Realms > *Realm Name* > Applications > OAuth 2.0 > Clients > *Client ID*.

- Enable Rich Authorization Requests with RCS

  Lets Advanced Identity Cloud process `authorization_details` from [RFC 9396: OAuth 2.0 Rich Authorization Requests](https://www.rfc-editor.org/rfc/rfc9396.html) when an RCS is configured.

  Requires Enable Remote Consent to be enabled and a configured RCS.

  Learn more in [Remote consent service](../am-oauth2/oauth2-remote-consent.html).

  Default value: `false`

- Remote Consent Service ID

  The ID of an existing remote consent service agent.

  You can override this setting for individual clients. To access client application settings, go to Native Consoles > Access Management > Realms > *Realm Name* > Applications > OAuth 2.0 > Clients > *Client ID*.

  The possible values for this property are:

  * `[Empty]`

- Remote Consent Service Request Signing Algorithms Supported

  Algorithms supported to sign consent\_request JWTs for Remote Consent Services.

  Advanced Identity Cloud supports the signing algorithms listed in JSON Web Algorithms (JWA): ["alg" (Algorithm) Header Parameter Values for JWS](https://www.rfc-editor.org/rfc/rfc7518.html#section-3.1):

  * `HS256` - HMAC with SHA-256.

  * `HS384` - HMAC with SHA-384.

  * `HS512` - HMAC with SHA-512.

  * `ES256` - ECDSA with SHA-256 and NIST standard P-256 elliptic curve.

  * `ES384` - ECDSA with SHA-384 and NIST standard P-384 elliptic curve.

  * `ES512` - ECDSA with SHA-512 and NIST standard P-521 elliptic curve.

  * `RS256` - RSASSA-PKCS-v1\_5 using SHA-256.

- Remote Consent Service Request Encryption Algorithms Supported

  Encryption algorithms supported to encrypt Remote Consent Service requests.

  Advanced Identity Cloud supports the following encryption algorithms:

  * `RSA1_5` - RSA with PKCS#1 v1.5 padding.

  * `RSA-OAEP` - RSA with Optimal Asymmetric Encryption Padding (OAEP) with SHA-1 and MGF-1.

  * `RSA-OAEP-256` - RSA with OAEP with SHA-256 and MGF-1.

  * `A128KW` - AES Key Wrapping with 128-bit key derived from the client secret.

  * `A192KW` - AES Key Wrapping with 192-bit key derived from the client secret.

  * `A256KW` - AES Key Wrapping with 256-bit key derived from the client secret.

  * `dir` - Direct encryption with AES using the hashed client secret.

- Remote Consent Service Request Encryption Methods Supported

  Encryption methods supported to encrypt Remote Consent Service requests.

  Advanced Identity Cloud supports the following encryption methods:

  * `A128GCM`, `A192GCM`, and `A256GCM` - AES in Galois Counter Mode (GCM) authenticated encryption mode.

  * `A128CBC-HS256`, `A192CBC-HS384`, and `A256CBC-HS512` - AES encryption in CBC mode, with HMAC-SHA-2 for integrity.

- Remote Consent Service Response Signing Algorithms Supported

  Algorithms supported to verify signed consent\_response JWT from Remote Consent Services.

  Advanced Identity Cloud supports the signing algorithms listed in JSON Web Algorithms (JWA): ["alg" (Algorithm) Header Parameter Values for JWS](https://www.rfc-editor.org/rfc/rfc7518.html#section-3.1):

  * `HS256` - HMAC with SHA-256.

  * `HS384` - HMAC with SHA-384.

  * `HS512` - HMAC with SHA-512.

  * `ES256` - ECDSA with SHA-256 and NIST standard P-256 elliptic curve.

  * `ES384` - ECDSA with SHA-384 and NIST standard P-384 elliptic curve.

  * `ES512` - ECDSA with SHA-512 and NIST standard P-521 elliptic curve.

  * `RS256` - RSASSA-PKCS-v1\_5 using SHA-256.

- Remote Consent Service Response Encryption Algorithms Supported

  Encryption algorithms supported to decrypt Remote Consent Service responses.

  Advanced Identity Cloud supports the following encryption algorithms:

  * `RSA1_5` - RSA with PKCS#1 v1.5 padding.

  * `RSA-OAEP` - RSA with Optimal Asymmetric Encryption Padding (OAEP) with SHA-1 and MGF-1.

  * `RSA-OAEP-256` - RSA with OAEP with SHA-256 and MGF-1.

  * `A128KW` - AES Key Wrapping with 128-bit key derived from the client secret.

  * `A192KW` - AES Key Wrapping with 192-bit key derived from the client secret.

  * `A256KW` - AES Key Wrapping with 256-bit key derived from the client secret.

  * `dir` - Direct encryption with AES using the hashed client secret.

- Remote Consent Service Response Encryption Methods Supported

  Encryption methods supported to decrypt Remote Consent Service responses.

  Advanced Identity Cloud supports the following encryption methods:

  * `A128GCM`, `A192GCM`, and `A256GCM` - AES in Galois Counter Mode (GCM) authenticated encryption mode.

  * `A128CBC-HS256`, `A192CBC-HS384`, and `A256CBC-HS512` - AES encryption in CBC mode, with HMAC-SHA-2 for integrity.

#### CIBA

The following settings appear on the CIBA tab:

* Back Channel Authentication ID Lifetime (seconds)

  The time back channel authentication request id is valid for, in seconds.

* Polling Wait Interval (seconds)

  The minimum amount of time in seconds that the Client should wait between polling requests to the token endpoint

* Signing Algorithms Supported

  Algorithms supported to sign the CIBA request parameter.

  Advanced Identity Cloud supports the signing algorithms listed in JSON Web Algorithms (JWA): ["alg" (Algorithm) Header Parameter Values for JWS](https://www.rfc-editor.org/rfc/rfc7518.html#section-3.1):

  * `ES256` - ECDSA with SHA-256 and NIST standard P-256 elliptic curve.

  * `PS256` - RSASSA-PSS using SHA-256.

#### Plugins

The Plugins settings are used to configure the following supported OAuth2 plugin extension points:

* [Access token modification](../am-oauth2/modifying-access-tokens-scripts.html)

* [OIDC claims](../am-oauth2/plugins-user-info-claims.html)

* [Scope evaluation](../am-oauth2/plugins-scope-evaluator.html)

* [Scope validation](../am-oauth2/plugins-scope-validator.html)

* [Authorize endpoint data provider](../am-oauth2/plugins-auth-endpoint-data-provider.html)

Each plugin is configured using three different attributes:

* `Plugin Type`:

  This value can be either `SCRIPTED` to run a custom script, or `JAVA` for a custom implementation class.

* `Script`:

  The script that is run for `SCRIPTED` plugin types.

* `Implementation Class`:

  The class that is invoked for `JAVA` plugin types. The class must implement the appropriate Java interface in the `org.forgerock.oauth2.core.plugins` package for the plugin.

  |   |                                                                                                                                                                                                                    |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | You can override this setting for individual clients. To access client application settings, go to Native Consoles > Access Management > Realms > *Realm Name* > Applications > OAuth 2.0 > Clients > *Client ID*. |

The following settings appear on the Plugins tab:

* Access Token Modification Plugin Type

  Default value: `SCRIPTED`

* Access Token Modification Script

  This script is run when issuing an access token. The script lets you modify the token, for example, by altering the data fields, before it is persisted or returned to the client.

  The script is run if `Access Token Modification Plugin Type` is set to `SCRIPTED`.

  Refer to [Access tokens](../am-oauth2/modifying-access-tokens-scripts.html).

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

### OneSpan Configuration

The following settings are available in this service:

* OneSpan IAA user name

  OneSpan IAA user name

* OneSpan IAA Environment

  OneSpan IAA Environment

  The possible values for this property are:

  * `sdb`

  * `prod`

* Application Reference

  A descriptive value for the integrated application

### PingOne Worker service

#### Configuration

The following settings appear on the Configuration tab:

* Enabled

  Enables the service.

#### Secondary Configurations

This service has the following Secondary Configurations.

The fields you need to configure depend on whether you connect to PingOne using a credential JWT or OIDC client credentials.

* Client ID

  Client ID of the worker application in PingOne.

  Find more information in [Adding a worker application for the PingOne Authorize service](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_adding_worker_app.html).

* Client Secret Label Identifier

  Identifier that Advanced Identity Cloud uses to create a specific secret label for the client secret of the worker application.

  The secret label uses the template `am.services.pingone.worker.identifier.clientsecret` where identifier is the Client Secret Label Identifier value.

  This field can only contain characters `a-z`, `A-Z`, `0-9`, and `.` and can't start or end with a period.

  Learn how to map the client secret to the secret label in [Map ESV secrets to secret labels](../tenants/esvs-signing-encryption.html#map-esv-secrets-to-secret-labels).

* Environment ID

  The environment that contains the worker application in PingOne.

* PingOne API Server URL

  The regional base URL of the PingOne ***API*** server.

  Enter one of the following:

  * `https://api.pingone.com/v1` - for the North America region (excluding Canada)

  * `https://api.pingone.ca/v1` - for the Canada region

  * `https://api.pingone.eu/v1` - for the European Union region

  * `https://api.pingone.asia/v1` - for the Asia-Pacific region

  Default: `https://api.pingone.com/v1`

* PingOne Authorization Server URL

  The regional base URL for the PingOne ***authorization*** server.

  Enter one of the following:

  * `https://auth.pingone.com` - for the North America region (excluding Canada)

  * `https://auth.pingone.ca` - for the Canada region

  * `https://auth.pingone.eu` - for the European Union region

  * `https://auth.pingone.asia` - for the Asia-Pacific region

  Default: `https://auth.pingone.com`

* Enable Connection via Credential

  When enabled, Advanced Identity Cloud uses the details extracted from the PingOne credential JWT to connect to PingOne.

* Credential Secret Label Identifier

  Identifier that Advanced Identity Cloud uses to create a specific secret label for the credential JWT.

  The secret label uses the template `am.services.pingone.worker.identifier.credential` where identifier is the Credential Secret Label Identifier value.

  This field can only contain characters `a-z`, `A-Z`, `0-9`, and `.` and can't start or end with a period.

  Learn how to map the credential JWT to the secret label in [Map ESV secrets to secret labels](../tenants/esvs-signing-encryption.html#map-esv-secrets-to-secret-labels).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can query the configured worker services using the `_queryFilter` parameter on the `realm-config/services/pingOneWorkerService/workers` endpoint.For example, use the following request to return all worker services that are configured to use a credential JWT for connection:```none
$ curl \
--request GET \
--header 'Accept-API-Version: resource=1.0' \
--header 'Authorization: Bearer <access-token>' \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/realm-config/services/pingOneWorkerService/workers?_queryFilter=useCredential%20eq%20true'
``` |

##### Test the connection

After you configure the worker service, test the connection from Advanced Identity Cloud to PingOne to verify the details. When you test the connection, Advanced Identity Cloud attempts to get an access token from PingOne using the worker service configuration.

If the connection fails, check the worker service configuration:

* Ensure that the ESVs contain the correct values from the worker in the mapped PingOne environment.

* Ensure that the ESVs are correctly mapped in the Advanced Identity Cloud service.

There are two ways to test the connection:

* In the AM native admin console

  Click the Save and Test Connection button to test the connection from Advanced Identity Cloud to PingOne.

  A Test Results window indicates whether the connection was successful. It also displays the values used in the connection test, which are extracted from the credential JWT or derived from the worker service configuration, and the reason for failure if the connection was unsuccessful.

* Over REST

  Use the `testConnection` action on the `realm-config/services/pingOneWorkerService/workers/pingone-worker-service-name` endpoint to test the connection from Advanced Identity Cloud to PingOne.

  1. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token) that has the `fr:am:*` scope.

  2. Test the connection from Advanced Identity Cloud to PingOne:

     ```none
     $ curl \
     --request POST 'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/realm-config/services/pingOneWorkerService/workers/<pingone-worker-service-name>?_action=testConnection' \(1) (2)
     --header 'Content-Type: application/json' \
     --header 'Accept-API-Version: resource=1.0' \
     --header 'Authorization: Bearer <access-token>'(3)
     ```

     |       |                                                                                                                                                                      |
     | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                                                                                                 |
     | **2** | Replace \<pingone-worker-service-name> with the name of the PingOne worker service, ensuring that any spaces are URL encoded. For example, `PingOne%20Worker%20AIC`. |
     | **3** | Replace \<access-token> with the access token created in step 1.                                                                                                     |

     If you get a `200 OK` response, the connection is successful. The response includes the values used in the connection test, which are extracted from the credential JWT or derived from the worker service configuration.

     > **Collapse: Example successful response**
     >
     > The following example response indicates a successful connection test using a credential JWT, with the response including the `credentialId` (`jti` claim) and the `createdAt` timestamp (`iat` claim) along with the other values extracted from the credential JWT:
     >
     > ```json
     > {
     >         "environmentId": "219...43e",
     >         "apiServerUrl": "https://api.pingone.eu/v1",
     >         "authServerUrl": "https://auth.pingone.eu",
     >         "environmentName": "Test Environment",
     >         "region": "Europe",
     >         "organizationId": "99f...d1c",
     >         "organizationName": "My Organization",
     >         "credentialId": "c0fd...b8e",
     >         "createdAt": "2026-04-21T17:42:00Z"
     >     }
     > ```

     If you get a `400 Bad Request` response, the connection has failed. The response includes the reason for failure (including an upstream error, if relevant) and the values used in the connection test, if available. These values might be missing if a misconfiguration, such as an invalid credential JWT or an incorrectly mapped ESV, prevents them from being retrieved.

     > **Collapse: Example unsuccessful response**
     >
     > The following example response indicates an unsuccessful connection test due to invalid client credentials, with the response including the error details from PingOne as well as the values extracted from the credential JWT:
     >
     > ```json
     > {
     >     "code": 400,
     >     "reason": "Bad Request",
     >     "message": "Failed to retrieve PingOne Worker access token.[Status: 401 Unauthorized]-{\n  \"error\" : \"invalid_client\",\n  \"error_description\" : \"Request denied: Invalid client credentials (Correlation ID: ea883d65-6de5-4906-8109-78516a5214da)\"\n}",
     >     "detail": {
     >         "environmentId": "219...43e",
     >         "apiServerUrl": "https://api.pingone.eu/v1",
     >         "authServerUrl": "https://auth.pingone.eu",
     >         "environmentName": "Test Environment",
     >         "region": "Europe",
     >         "organizationId": "99f...d1c",
     >         "organizationName": "My Organization",
     >         "credentialId": "c0fd...b8e",
     >         "createdAt": "2026-04-21T17:42:00Z"
     >     }
     > }
     > ```

### Policy Configuration

The following settings are available in this service:

* Primary LDAP Server

  Configuration directory server host:port that Advanced Identity Cloud searches for policy information.

  Format: `local Advanced Identity Cloud server name | hostname:port`

  Multiple entries must be prefixed by local server name. Make sure to place the multiple entries on a single line and separate the hostname:port URLs with a space.

  For example, am.example.com|ds.example.com:1389 ds.example.com:2389

  Default value:

  ```none
  userstore-1.userstore:1389
  userstore-0.userstore:1389
  userstore-2.userstore:1389
  ```

* LDAP Users Base DN

  Base DN for LDAP Users subject searches.

  Default value: `ou=identities`

* LDAP Bind DN

  Bind DN to connect to the directory server for policy information.

  If you enable mTLS, Advanced Identity Cloud ignores this property.

  Default value: `&{am.stores.user.username}`

* LDAP Bind Password

  Bind password to connect to the directory server for policy information.

  If you enable mTLS, Advanced Identity Cloud ignores this property.

  Default value:

  ```none
  {
      "$string": "&{am.stores.user.password}"
  }
  ```

* LDAP Organization Search Filter

  Search filter to match organization entries.

  Default value: `(objectclass=sunismanagedorganization)`

* LDAP Users Search Filter

  Search filter to match user entries.

  Default value: `(objectclass=inetorgperson)`

* LDAP Users Search Scope

  Search scope to find user entries.

  The possible values for this property are:

  * `SCOPE_BASE`

  * `SCOPE_ONE`

  * `SCOPE_SUB`

  Default value: `SCOPE_SUB`

* LDAP Users Search Attribute

  Naming attribute for user entries.

  Default value: `uid`

* Maximum Results Returned from Search

  Search limit for LDAP searches.

  Default value: `100`

* Search Timeout

  Time after which Advanced Identity Cloud returns an error for an incomplete search, in seconds.

  Default value: `5`

* LDAP SSL/TLS

  If enabled, Advanced Identity Cloud connects securely to the directory server. This requires that you install the directory server certificate.

  Default value:

  ```none
  {
      "$bool": "&{am.stores.ssl.enabled}"
  }
  ```

* LDAP Connection Pool Minimum Size

  Minimum number of connections in the pool.

  Default value: `1`

* LDAP Connection Pool Maximum Size

  Maximum number of connections in the pool.

  Default value: `10`

* Heartbeat Interval

  Specifies how often should Advanced Identity Cloud send a heartbeat request to the directory.

  Use this option in case a firewall/loadbalancer can close idle connections, since the heartbeat requests will ensure that the connections won't become idle.

  Default value: `10`

* Heartbeat Unit

  Defines the time unit corresponding to the Heartbeat Interval setting.

  Use this option in case a firewall/loadbalancer can close idle connections, since the heartbeat requests will ensure that the connections won't become idle.

  The possible values for this property are:

  * Label: **second** (Value: `SECONDS`)

  * Label: **minute** (Value: `MINUTES`)

  * Label: **hour** (Value: `HOURS`)

  Default value: `SECONDS`

* Subjects Result Time to Live

  Maximum time that Advanced Identity Cloud caches a subject result for evaluating policy requests, in minutes. A value of `0` prevents Advanced Identity Cloud from caching subject evaluations for policy decisions.

  Default value: `10`

* User Alias

  If enabled, Advanced Identity Cloud can evaluate policy for remote users aliased to local users.

  Default value: `false`

* Check resources exist when Resource Server is updated

  Check all registered resources exist when updating the Resource Server.

  When enabled, the Policy Set checks registered Resource Types one by one against the configuration store. Consider disabling this option if you have many Resource Types registered to a Policy Set.

  Default value: `true`

* mTLS Enabled

  Enables mutual TLS (mTLS) authentication between Advanced Identity Cloud and this data store.

  When you enable mTLS, you must also:

  * Enable LDAP SSL/TLS.

  * Map the secret label `am.policy.configuration.serice.mtls.cert` to the alias you want to use for mTLS authentication to this store.

Advanced Identity Cloud ignores the LDAP Bind DN and LDAP Bind Password when you enable mTLS.

### Push Notification Service

The following settings are available in this service:

* SNS Access Key ID

  Amazon Simple Notification Service Access Key ID. For more information, refer to [Create an AWS (Push Auth) Credential](https://backstage.forgerock.com/knowledge/backstagehelp/article/a92326771#aws) in the ForgeRock Knowledge Base.

  For example, you might set this property to: AKIAIOSFODNN7EXAMPLE

* SNS Access Key Secret

  Amazon Simple Notification Service Access Key Secret. For more information, refer to [Create an AWS (Push Auth) Credential](https://backstage.forgerock.com/knowledge/backstagehelp/article/a92326771#aws) in the ForgeRock Knowledge Base.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | For greater security, you can store this secret in the realm secret store.Map the secret to the secret label `am.services.pushnotification.sns.accesskey.secret`.If a secret is mapped to this secret label, Advanced Identity Cloud uses that secret and ignores the value of the SNS Access Key Secret property.If a secret is mapped to this secret label and Advanced Identity Cloud can't locate the secret, it falls back to the value of the SNS Access Key Secret property. |

* SNS Endpoint for APNS

  The Simple Notification Service endpoint in Amazon Resource Name format, used to send push messages to the Apple Push Notification Service (APNS).

  For example, you might set this property to: arn:aws:sns:us-east-1:1234567890:app/APNS/production

* SNS Endpoint for GCM

  The Simple Notification Service endpoint in Amazon Resource Name format, used to send push messages over Google Cloud Messaging (GCM).

  For example, you might set this property to: arn:aws:sns:us-east-1:1234567890:app/GCM/production

* SNS Client Region

  Region of your registered Amazon Simple Notification Service client. For more information, refer to <https://docs.aws.amazon.com/general/latest/gr/rande.html>.

  The possible values for this property are:

  * `us-gov-west-1`

  * `us-east-1`

  * `us-west-1`

  * `us-west-2`

  * `eu-west-1`

  * `eu-west-2`

  * `eu-central-1`

  * `ap-southeast-1`

  * `ap-southeast-2`

  * `ap-southeast-3`

  * `ap-northeast-1`

  * `ap-northeast-2`

  * `sa-east-1`

  * `ca-central-1`

  * `cn-north-1`

* Message Transport Delegate Factory

  The fully qualified class name of the factory responsible for creating the PushNotificationDelegate. The class must implement `org.forgerock.openam.services.push.PushNotificationDelegate`.

* Response Cache Duration

  The minimum lifetime to keep unanswered message records in the message dispatcher cache, in seconds. To keep unanswered message records indefinitely, set this property to `0`.

* Response Cache Concurrency

  Level of concurrency to use when accessing the message dispatcher cache. Must be greater than `0`. Choose a value to accommodate as many threads as will ever concurrently access the message dispatcher cache.

* Response Cache Size

  Maximum size of the message dispatcher cache, in number of records. If set to `0` the cache can grow indefinitely. If the number of records that need to be stored exceeds this maximum, then older items in the cache will be removed to make space.

### Remote Consent Service

The following settings are available in this service:

* Client Name

  The name used to identify this OAuth 2.0 remote consent service when referencedin other services.

* Authorization Server jwk\_uri

  The jwk\_uri for retrieving the authorization server signing and encryption keys.

* JWK Store Cache Timeout (in minutes)

  The cache timeout for the JWK store of the authorization server, in minutes.

* JWK Store Cache Miss Cache Time (in minutes)

  The length of time a cache miss is cached, in minutes.

* Consent Response Time Limit (in minutes)

  The time limit set on the consent response JWT before it expires, in minutes.

### Self Service Trees

#### Realm Attributes

The following settings appear on the Realm Attributes tab:

* Enabled

  Enable the service.

#### Tree Mapping

The following settings appear in the Tree Mapping pane:

* resetPassword

  Map the default journey to use for resetting passwords.

* updatePassword

  Map the default journey to use for updating passwords.

* forgottenUsername

  Map the default journey to use to retrieve forgotten usernames.

* registration

  Map the default journey to use when registering a new account.

### Session

#### Dynamic Attributes

The following settings appear on the Dynamic Attributes tab:

* Maximum Session Time

  Maximum time a session can remain valid before Advanced Identity Cloud requires the user to authenticate again, in minutes.

  Default value: `120`

* Maximum Idle Time

  Maximum time a server-side session can remain idle before Advanced Identity Cloud requires the user to authenticate again, in minutes.

  Default value: `30`

* Maximum Caching Time

  Maximum duration that external clients should cache the session, in minutes.

  Default value: `3`

* Active User Sessions

  Maximum number of concurrent server-side authenticated sessions Advanced Identity Cloud allows a user to have.

  Default value: `5`

### Session Property Whitelist Service

The following settings are available in this service:

* Allowlisted Session Property Names

  A list of properties that users may read, edit the value of, or delete from their session.

  Adding properties to sessions can affect Advanced Identity Cloud's performance because there is no size constraint limiting the set of properties you can add to sessions and no limit on the number of session properties you can add.

  |   |                                                                                                       |
  | - | ----------------------------------------------------------------------------------------------------- |
  |   | Protected attributes *can't* be set, edited, or deleted, even if they are included in this allowlist. |

* Session Properties to return for session queries

  A list of session properties that can be returned to admins in a REST session query response.

  This setting can impact REST query performance. When session properties are added, the CTS token must be retrieved, and can be decrypted and decompressed, if configured.

  Protected attributes *can't* be set, edited or deleted, even if they are included in this list.

### Social Authentication Implementations

This service doesn't apply to Advanced Identity Cloud.

### Social Identity Provider Service

#### Configuration

The following settings appear on the Configuration tab:

* Enabled

  Enable the service.

#### Secondary Configurations

The `SocialIdentityProviders` service provides a number of [default social identity provider configurations](../self-service/social-registration.html#default-social-providers). It also lets you configure [custom configurations](../self-service/social-registration.html#custom-social-providers) for social identity providers that implement the OAuth 2.0 or OpenID Connect (OIDC) specifications.

Learn about the specific identity provider settings in [Client configuration reference](../am-authentication/social-idp-client-reference.html).

|   |                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | View the names of your configured social identity providers in Native Consoles > Access Management > Realms > *Realm name* > Services > Social Identity Provider Service > Secondary Configurations. |

### Transaction Authentication Service

The following settings are available in this service:

* Time to Live

  The number of seconds within which the transaction must be completed.

### User

#### Dynamic Attributes

The following settings appear on the Dynamic Attributes tab:

* User Preferred Timezone

  Time zone for accessing the UI.

* Administrator DN Starting View

  Specifies the DN for the initial screen when an administrator successfully logs in to the UI.

* Default User Status

  Inactive users cannot authenticate, though Advanced Identity Cloud stores their profiles.

  The possible values for this property are:

  * `Active`

  * `Inactive`

### Validation Service

The following settings are available in this service:

* Valid goto URL Resources

  List of valid goto URL resources.

  Specifies a list of valid URLs for the `goto` and `gotoOnFail` query string parameters.

  After login or logout, Advanced Identity Cloud can redirect a user to a URL in this list. If the URL is not in this list, Advanced Identity Cloud redirects to the user profile page or the URL set in the [Success URL node](https://docs.pingidentity.com/auth-node-ref/latest/success-url.html). If you don't set this property, Advanced Identity Cloud only allows URLs that match its domain. Use the `*` wildcard to match all characters except `?`.

  Examples:

  * `http://app.example.com:80/*`

  * `http://app.example.com:80/*?*`

### WebAuthn Profile Encryption Service

The following settings are available in this service:

* Profile Storage Attribute

  The user's attribute in which to store WebAuthn profiles.

* Device Profile Encryption Scheme

  Encryption scheme to use to secure device profiles stored on the server.

  If enabled, each device profile is encrypted using a unique random secret key using the given strength of AES encryption in CBC mode with PKCS#5 padding. An HMAC-SHA of the given strength (truncated to half-size) is used to ensure integrity protection and authenticated encryption. The unique random key is encrypted with the given RSA key pair and stored with the device profile.

  |   |                                                                              |
  | - | ---------------------------------------------------------------------------- |
  |   | AES-256 may require installation of the JCE Unlimited Strength policy files. |

  The possible values for this property are:

  * Label: **AES-256/HMAC-SHA-512 with RSA Key Wrapping** (Value: `RSAES_AES256CBC_HS512`)

  * Label: **AES-128/HMAC-SHA-256 with RSA Key Wrapping** (Value: `RSAES_AES128CBC_HS256`)

  * Label: **No encryption of device settings.** (Value: `NONE`)

* Encryption Key Store

  Path to the key store from which to load encryption keys.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Updating this setting isn't currently supported in Advanced Identity Cloud. Changing its value may lead to a loss of functionality in this feature.For greater security, store encryption key information in [ESVs](../tenants/esvs-signing-encryption.html), instead of in the configuration. Use the [secret label](secret-id-mappings.html#encrypted-device-storage-secret-labels) `am.services.authenticatorwebauthn.encryption` to map an alias for WebAuthn Profile Encryption service secrets.If you update encryption key information in the configuration or in the secret stores, users with existing device profiles will no longer be able to log in using this service. Delete the end user's device profile so that they can create a new one when they next log in. |

  |   |                                                                                                                                                                         |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If Advanced Identity Cloud finds a matching secret for the `am.services.authenticatorwebauthn.encryption` label in the realm's ESV secret store, this value is ignored. |

* Key Store Type

  Type of key store to load.

  Refer to the [JDK 8 PKCS#11 Reference Guide](https://docs.oracle.com/javase/8/docs/technotes/guides/security/p11guide.html) for more details.

  The possible values for this property are:

  * Label: **Java Key Store (JKS).** (Value: `JKS`)

  * Label: **Java Cryptography Extension Key Store (JCEKS).** (Value: `JCEKS`)

  * Label: **PKCS#11 Hardware Crypto Storage.** (Value: `PKCS11`)

  * Label: **PKCS#12 Key Store.** (Value: `PKCS12`)

  |   |                                                                                                                                                                         |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If Advanced Identity Cloud finds a matching secret for the `am.services.authenticatorwebauthn.encryption` label in the realm's ESV secret store, this value is ignored. |

* Key Store Password

  Password to unlock the key store. This password is encrypted when it is saved in the Advanced Identity Cloud configuration.

  |   |                                                                                                                                                                         |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If Advanced Identity Cloud finds a matching secret for the `am.services.authenticatorwebauthn.encryption` label in the realm's ESV secret store, this value is ignored. |

* Key-Pair Alias

  Alias of the certificate and private key in the key store. The private key is used to encrypt and decrypt device profiles.

  |   |                                                                                                                                                                         |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If Advanced Identity Cloud finds a matching secret for the `am.services.authenticatorwebauthn.encryption` label in the realm's ESV secret store, this value is ignored. |

* Private Key Password

  Password to unlock the private key.

### WebAuthn Metadata service

The WebAuthn Metadata service lets you configure how Advanced Identity Cloud obtains metadata from the [FIDO Metadata Service](https://fidoalliance.org/metadata/).

The service has the following configurable attributes:

* Metadata service URIs

  The list of locations from which to download the [metadata blob](https://fidoalliance.org/specs/mds/fido-metadata-service-v3.0-ps-20210518.html#metadata-blob).

  Advanced Identity Cloud verifies the blob signature against secrets mapped to the `am.authentication.nodes.webauthn.fidometadataservice.rootcertificate` secret label.

* Enforce revocation check

  This setting specifies whether Advanced Identity Cloud must check revocation entries from certificates.

  The setting is disabled by default, so Advanced Identity Cloud doesn't check presented certificates for revocation.

  If you enable this setting, Advanced Identity Cloud must be able to verify any attestation certificate's trust chain with a CRL or OCSP entry during processing.

  |   |                                                                                            |
  | - | ------------------------------------------------------------------------------------------ |
  |   | Certificates downloaded from the FIDO Metadata Service might not have a CRL or OCSP entry. |

---

---
title: Glossary
description: Glossary of key terms and concepts used across Advanced Identity Cloud documentation
component: pingoneaic
page_id: pingoneaic:am-reference:glossary
canonical_url: https://docs.pingidentity.com/pingoneaic/am-reference/glossary.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Glossary

* Access control

  Control to grant or to deny access to a resource.

* Account lockout

  The act of making an account temporarily or permanently inactive after successive authentication failures.

* Actions

  Defined as part of policies, these verbs indicate what authorized identities can do to resources.

* Advice

  In the context of a policy decision denying access, a hint to the policy enforcement point about remedial action to take that could result in a decision allowing access.

* Agent administrator

  User having privileges only to read and write agent profile configuration information, typically created to delegate agent profile creation to the user installing a web or Java agent.

* Agent authenticator

  Entity with read-only access to multiple agent profiles defined in the same realm; allows an agent to read web service profiles.

* Application

  In general terms, a service exposing protected resources.

  In the context of Advanced Identity Cloud policies, the application is a template that constrains the policies that govern access to protected resources. An application can have zero or more policies.

* Application type

  Application types act as templates for creating policy applications.

  Application types define a preset list of actions and functional logic, such as policy lookup and resource comparator logic.

  Application types also define the internal normalization, indexing logic, and comparator logic for applications.

* Attribute-based access control (ABAC)

  Access control that is based on attributes of a user, such as how old a user is or whether the user is a paying customer.

- Authenticated session

  The interval that starts after the user has authenticated and ends when the user logs out, or when their session is terminated. For browser-based clients, Advanced Identity Cloud manages authenticated sessions across one or more applications by setting a session cookie.

  Learn more in [server-side sessions](#def-server-side-session) and [client-side sessions](#def-client-side-session).

  A [journey session](#def-journey-session) exists before an authenticated session.

- Authentication

  The act of confirming the identity of a principal.

- Authentication level

  Positive integer associated with an authentication node, usually used to require success with more stringent authentication measures when requesting resources requiring special protection.

- Authorization

  The act of determining whether to grant or to deny a user access to a resource.

- Authorization server

  In OAuth 2.0, issues access tokens to the client after authenticating a resource owner and confirming that the owner authorizes the client to access the protected resource. Advanced Identity Cloud can play this role in the OAuth 2.0 authorization framework.

- Auto-federation

  Arrangement to federate a principal's identity automatically based on a common attribute value shared across the principal's profiles at different providers.

- Circle of trust

  Group of providers, including at least one identity provider, who have agreed to trust each other to participate in a SAML 2.0 provider federation.

- Client

  In OAuth 2.0, requests protected web resources on behalf of the resource owner given the owner's authorization. Advanced Identity Cloud can play this role in the OAuth 2.0 authorization framework.

* Client-side OAuth 2.0 tokens

  After a successful OAuth 2.0 grant flow, Advanced Identity Cloud returns a token to the client.

  This differs from [server-side OAuth 2.0 tokens](#def-server-side-token), where Advanced Identity Cloud returns a *reference* to the token to the client.

- Client-side sessions

  Sessions for which Advanced Identity Cloud returns session state to the client after each request, and requires the state to be passed in with the subsequent request.

  For browser-based clients, Advanced Identity Cloud sets a cookie in the browser that contains the session state. When the browser returns the cookie, Advanced Identity Cloud decodes the session state from the cookie.

  A [journey session](#def-journey-session) and an [authenticated session](#def-auth-session) can be a client-side session.

- Conditions

  Defined as part of policies, these determine the circumstances under which a policy applies.

  Environmental conditions reflect circumstances like the client IP address, time of day, how the subject authenticated, or the authentication level achieved.

  Subject conditions reflect characteristics of the subject like whether the subject authenticated, the identity of the subject, or claims in the subject's JWT.

- Configuration datastore

  LDAP directory service holding Advanced Identity Cloud configuration data.

- Cross-domain single sign-on (CDSSO)

  Advanced Identity Cloud capability allowing single sign-on across different DNS domains.

- Delegation

  Granting users administrative privileges with Advanced Identity Cloud.

- Entitlement

  Decision that defines which resource names can and cannot be accessed for a given identity in the context of a particular application, which actions are allowed and which are denied, and any related advice and attributes.

- Extended metadata

  Federation configuration information specific to Advanced Identity Cloud.

- Extensible Access Control Markup Language (XACML)

  Standard, XML-based access control policy language, including a processing model for making authorization decisions based on policies.

- Federation

  Standardized means for aggregating identities, sharing authentication and authorization data information between trusted providers, and allowing principals to access services across different providers without authenticating repeatedly.

- Identity

  Set of data that uniquely describes a person or a thing such as a device or an application.

- Identity federation

  Linking of a principal's identity across multiple providers.

- Identity provider (IDP)

  Entity that produces assertions about a principal (such as how and when a principal authenticated, or that the principal's profile has a specified attribute value).

- Identity repository

  Data store holding user profiles and group information.

- Java agent

  Java web application installed in a web container that acts as a policy enforcement point, filtering requests to other applications in the container with policies based on application resource URLs.

* Journey session

  The interval that starts when the user begins progressing through an authentication journey and ends when the journey completes or the session has timed out.

  An [authenticated session](#def-auth-session) is created if they authenticate successfully.

  A journey session can be a [server-side session](#def-server-side-session) or a [client-side session](#def-client-side-session).

* Metadata

  Federation configuration information for a provider.

* No session journey

  Journey that doesn't result in an authenticated session when it successfully completes.

* Policy

  Set of rules that define who is granted access to a protected resource when, how, and under what conditions.

* Policy agent

  Java, web, or custom agent that intercepts requests for resources, directs principals to Advanced Identity Cloud for authentication, and enforces policy decisions from Advanced Identity Cloud.

* Policy Administration Point (PAP)

  Entity that manages and stores policy definitions.

* Policy Decision Point (PDP)

  Entity that evaluates access rights and then issues authorization decisions.

* Policy Enforcement Point (PEP)

  Entity that intercepts a request for a resource and then enforces policy decisions from a PDP.

* Policy Information Point (PIP)

  Entity that provides extra information, such as user profile attributes that a PDP needs to make a decision.

- Principal

  Represents an entity that has been authenticated (such as a user, a device, or an application), and thus is distinguished from other entities.

  When a [Subject](#def-subject) successfully authenticates, Advanced Identity Cloud associates the Subject with the Principal.

- Privilege

  In the context of delegated administration, a set of administrative tasks that can be performed by specified identities in a given realm.

- Provider federation

  Agreement among providers to participate in a circle of trust.

- Realm

  Advanced Identity Cloud unit for organizing configuration and identity information.

  Administrators can delegate realm administration. The administrator assigns administrative privileges to users, allowing them to perform administrative tasks within the realm.

- Resource

  Something a user can access over the network such as a web page.

  Defined as part of policies, these can include wildcards to match multiple actual resources.

- Resource owner

  In OAuth 2.0, entity who can authorize access to protected web resources, such as an end user.

- Resource server

  In OAuth 2.0, server hosting protected web resources, capable of handling access tokens to respond to requests for such resources.

- Response attributes

  Defined as part of policies, these Advanced Identity Cloud return additional information in the form of "attributes" with the response to a policy decision.

- Role based access control (RBAC)

  Access control that is based on whether a user has been granted a set of permissions (a role).

- Security Assertion Markup Language (SAML)

  Standard, XML-based language for exchanging authentication and authorization data between identity providers and service providers.

* Server-side OAuth 2.0 tokens

  After a successful OAuth 2.0 grant flow, Advanced Identity Cloud returns a *reference* to the token to the client, rather than the token itself.

  This differs from [client-side OAuth 2.0 tokens](#def-client-side-token), where Advanced Identity Cloud returns the entire token to the client.

- Server-side sessions

  Sessions that reside in the Core Token Service (CTS) token store. Server-side sessions could also be cached in memory.

  Advanced Identity Cloud tracks these sessions to handle events like logout and timeout, to permit session constraints, and to notify applications involved in SSO when a session ends.

  A [journey session](#def-journey-session) and an [authenticated session](#def-auth-session) can be a server-side session.

- Service provider (SP)

  Entity that consumes assertions about a principal (and provides a service that the principal is trying to access).

- Session token

  Unique identifier issued by Advanced Identity Cloud after successful authentication.

  For a [server-side sessions](#def-server-side-session), the session token is used to track a principal's session.

- Single log out (SLO)

  Capability allowing a principal to end a session once, thereby ending her session across multiple applications.

- Single sign-on (SSO)

  Capability allowing a principal to authenticate once and gain access to multiple applications without authenticating again.

- Standard metadata

  Standard federation configuration information that you can share with other access management software.

* Stateless service

  Stateless services do not store any data locally to the service.

  When the service requires data to perform any action, it requests it from a data store.

  For example, a stateless authentication service stores session state for logged-in users in a database. This way, any server in the deployment can recover the session from the database and service requests for any user.

  All Advanced Identity Cloud services are stateless unless otherwise specified. Learn more in [client-side sessions](#def-client-side-session) and [server-side sessions](#def-server-side-session).

- Subject

  Entity that requests access to a resource.

  When an identity successfully authenticates, Advanced Identity Cloud associates the identity with the [Principal](#def-principal) that distinguishes it from other identities.

  An identity can be associated with multiple principals.

- Web agent

  Native library installed in a web server that acts as a policy enforcement point with policies based on web page URLs.

---

---
title: Reference
description: Access management reference guide for designers, developers, and administrators covering configuration and secret label mappings
component: pingoneaic
page_id: pingoneaic:am-reference:preface
canonical_url: https://docs.pingidentity.com/pingoneaic/am-reference/preface.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Administration", "Configuration"]
page_aliases: ["index.adoc", "reference:preface.adoc"]
---

# Reference

This reference is for access management designers, developers, and administrators.

[icon: th-list, set=fas, size=3x]

#### [Configuration](realm-services-configuration.html)

Review Advanced Identity Cloud configuration properties.

[icon: lock, set=fas, size=3x]

#### [Secret mappings](secret-id-mappings.html)

Learn how Advanced Identity Cloud secret labels map to aliases.

---

---
title: Secret labels
description: Secret labels for signing and encryption across OAuth 2.0, OpenID Connect, SAML 2.0, and other services
component: pingoneaic
page_id: pingoneaic:am-reference:secret-id-mappings
canonical_url: https://docs.pingidentity.com/pingoneaic/am-reference/secret-id-mappings.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["ESV", "Encryption", "Secret Stores", "Federation", "OAuth 2.0", "OpenID Connect (OIDC)", "SAML 2.0"]
page_aliases: ["reference:secret-id-mappings.adoc"]
section_ids:
  oauth2-default-secret-labels: OAuth 2.0 and OpenID Connect provider secrets
  oidc-social-registration-secret-labels: Social identity client secrets
  agents-default-secret-labels: Web and Java agent secrets
  authentication-default-secret-labels: Authentication secrets
  saml2-default-secret-labels: SAML 2.0 secrets
  attestation-secret-labels: Attestation secrets
  encrypted-device-storage-secret-labels: Encrypted device storage services
  httpclient-secret-labels: Http Client service secrets
  pingone-worker-service-default-secret-IDs: PingOne Worker service
  policy-config-service-default-secret-labels: Policy Configuration service secrets
  push-notification-service-default-secret-labels: Push Notification service secrets
  webauthn-secret-labels: WebAuthn Metadata service secrets
---

# Secret labels

Advanced Identity Cloud uses these labels to match secrets for access management signing and encryption with the aliases of the secrets in the secret store. Expand the categories for additional information.

For instructions on using these secret labels, refer to [Use ESVs for signing and encryption keys](../tenants/esvs-signing-encryption.html).

|   |                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The term *secret IDs* is being phased out in favor of *secret labels* but you might come across instances of *secret ID* in the documentation and in the UI until the terminology change is complete. |

## OAuth 2.0 and OpenID Connect provider secrets

> **Collapse: Encrypt client-side OAuth 2.0 tokens**
>
> This table shows the label for the secret to encrypt [client-side](../am-oauth2/client-side-tokens.html) access tokens:
>
> | Secret label                                    | Algorithms    |
> | ----------------------------------------------- | ------------- |
> | `am.services.oauth2.stateless.token.encryption` | A128CBC-HS256 |

> **Collapse: Sign client-side OAuth 2.0 tokens**
>
> This table shows the labels for the secrets to sign [client-side](../am-oauth2/client-side-tokens.html) access tokens:
>
> | Secret label                                 | Algorithms                          |
> | -------------------------------------------- | ----------------------------------- |
> | `am.services.oauth2.stateless.signing.ES256` | ES256                               |
> | `am.services.oauth2.stateless.signing.ES384` | ES384                               |
> | `am.services.oauth2.stateless.signing.ES512` | ES512                               |
> | `am.services.oauth2.stateless.signing.HMAC`  | HS256 HS384 HS512                   |
> | `am.services.oauth2.stateless.signing.RSA`   | PS256 PS384 PS512 RS256 RS384 RS512 |

> **Collapse: Authenticate OAuth 2.0 clients**
>
> The secret label mappings used to authenticate [OAuth 2.0 clients](../am-oauth2/oauth2-register-client.html):
>
> | Secret label                                                          | Algorithms |
> | --------------------------------------------------------------------- | ---------- |
> | `am.applications.oauth2.client.identifier.secret`(1)                  |            |
> | `am.applications.oauth2.client.identifier.jwt.public.key`(2)          |            |
> | `am.applications.oauth2.client.identifier.mtls.trusted.cert`(3)       |            |
> | `am.applications.oauth2.client.identifier.id.token.enc.public.key`(4) |            |
>
> (1) Map the `am.applications.oauth2.client.identifier.secret` dynamic secret label to override the OAuth 2.0 client's Client secret property, where identifier is the value of the Secret Label Identifier set in the client configuration.\
> (2) Map the `am.applications.oauth2.client.identifier.jwt.public.key` dynamic secret label to override the OAuth 2.0 client's Client JWT Bearer Public Key, where identifier is the value of the Secret Label Identifier set in the client configuration.\
> (3) Map the `am.applications.oauth2.client.identifier.mtls.trusted.cert` dynamic secret label to override the OAuth 2.0 client's mTLS Self-Signed Certificate, where identifier is the value of the Secret Label Identifier set in the client configuration.\
> (4) Map the `am.applications.oauth2.client.identifier.id.token.enc.public.key` dynamic secret label to override the OAuth 2.0 client's Client ID Token Public Encryption Key, where identifier is the value of the Secret Label Identifier set in the client configuration.

> **Collapse: Sign remote consent requests**
>
> This table shows the labels for the secrets to sign remote consent requests:
>
> | Secret label                                                  | Algorithms                          |
> | ------------------------------------------------------------- | ----------------------------------- |
> | `am.applications.agents.remote.consent.request.signing.ES256` | ES256                               |
> | `am.applications.agents.remote.consent.request.signing.ES384` | ES384                               |
> | `am.applications.agents.remote.consent.request.signing.ES512` | ES512                               |
> | `am.applications.agents.remote.consent.request.signing.RSA`   | RS256 RS384 RS512 PS256 PS384 PS512 |
>
> If you select an HMAC algorithm for signing consent requests (`HS256`, `HS384`, or `HS512`), Advanced Identity Cloud uses the Remote Consent Service secret, not an entry from the secret store.

> **Collapse: Decrypt remote consent responses**
>
> This table shows the label for the secret to decrypt remote consent responses:
>
> | Secret label                                            | Algorithms   |
> | ------------------------------------------------------- | ------------ |
> | `am.services.oauth2.remote.consent.response.decryption` | RSA-OAEP-256 |
>
> If you select an algorithm other than RSA-OAEP-256 for decrypting consent responses, Advanced Identity Cloud uses the Remote Consent Service secret, not an entry from the secret store.

> **Collapse: OAuth 2.0 example remote consent service**
>
> This table shows the labels for the secrets for the example remote consent service:
>
> | Secret label                                             | Algorithms                            |
> | -------------------------------------------------------- | ------------------------------------- |
> | `am.services.oauth2.remote.consent.response.signing.RSA` | RS256 RSA (at least 2048 bits)        |
> | `am.services.oauth2.remote.consent.request.encryption`   | RSA-OAEP-256 RSA (at least 2048 bits) |

> **Collapse: Secret label mappings for salting hashes**
>
> The secret label for salting hashes in OAuth 2.0 and OIDC flows.
>
> | Secret label                                   | Algorithms |
> | ---------------------------------------------- | ---------- |
> | `am.services.oauth2.provider.hash.salt.secret` |            |
>
> Use this secret label to override Subject Identifier Hash Salt in the provider configuration.
>
> This secret can't be rotated.

> **Collapse: Decrypt OIDC request parameters**
>
> This table shows the labels for secrets to decrypt OIDC request parameters:
>
> | Secret label                                      | Algorithms                           |
> | ------------------------------------------------- | ------------------------------------ |
> | `am.services.oauth2.oidc.decryption.RSA1.5`       | RSA with PKCS#1 v1.5 padding         |
> | `am.services.oauth2.oidc.decryption.RSA.OAEP`     | RSA with OAEP with SHA-1 and MGF-1   |
> | `am.services.oauth2.oidc.decryption.RSA.OAEP.256` | RSA with OAEP with SHA-256 and MGF-1 |
>
> For *confidential clients*, if you select an AES algorithm (`A128KW`, `A192KW`, or `A256KW`) or the direct encryption algorithm (`dir`), Advanced Identity Cloud uses the Client Secret from the profile, not an entry from the secret store.
>
> The following use the Client Secret:
>
> * Signing ID tokens with an HMAC algorithm
>
> * Encrypting ID tokens with AES or direct encryption
>
> * Encrypting parameters with AES or direct encryption
>
> Store only one secret in the Client Secret field.
>
> For details about encryption options, refer to the [OIDC specification](https://openid.net/specs/openid-connect-core-1_0.html).

> **Collapse: Sign OIDC tokens**
>
> This table shows the labels for secrets to sign OIDC tokens and backchannel logout tokens:
>
> | Secret label                            | Algorithms(1)                       |
> | --------------------------------------- | ----------------------------------- |
> | `am.services.oauth2.oidc.signing.ES256` | ES256                               |
> | `am.services.oauth2.oidc.signing.ES384` | ES384                               |
> | `am.services.oauth2.oidc.signing.ES512` | ES512                               |
> | `am.services.oauth2.oidc.signing.RSA`   | PS256 PS384 PS512 RS256 RS384 RS512 |
> | `am.services.oauth2.oidc.signing.EDDSA` | EdDSA with SHA-512                  |
>
> For *confidential clients*, if you select an HMAC algorithm for signing ID tokens (`HS256`, `HS384`, or `HS512`), Advanced Identity Cloud uses the Client Secret from the profile instead of an entry from the secret store.

> **Collapse: CA certificates for mTLS client authentication**
>
> This table shows the label of the trusted CA certificate for mTLS client authentication:
>
> | Secret label                                        | Algorithms |
> | --------------------------------------------------- | ---------- |
> | `am.services.oauth2.tls.client.cert.authentication` |            |

## Social identity client secrets

> **Collapse: Decrypt ID tokens**
>
> This table shows the label for the secret to decrypt ID tokens and `userinfo` endpoint JWTs when Advanced Identity Cloud acts as a relying party (RP) of the social identity provider service:
>
> | Secret label                                    | Algorithms                                                   |
> | ----------------------------------------------- | ------------------------------------------------------------ |
> | `am.services.oauth2.oidc.rp.idtoken.encryption` | Consult the `.well-known` endpoint of the identity provider. |
>
> The public key is exposed at the [/oauth2/connect/rp/jwk\_uri](../am-oidc1/managing-rp-jwk_uri.html) endpoint.
>
> For details, refer to [Social authentication](../self-service/social-registration.html).

> **Collapse: Sign JWTs and objects**
>
> This table shows the label for the secret to sign JWTs and objects when Advanced Identity Cloud acts as a relying party (RP) of the social identity provider service:
>
> | Secret label                                          | Algorithms                                                   |
> | ----------------------------------------------------- | ------------------------------------------------------------ |
> | `am.services.oauth2.oidc.rp.jwt.authenticity.signing` | Consult the `.well-known` endpoint of the identity provider. |
>
> The public key is exposed at the [/oauth2/connect/rp/jwk\_uri](../am-oidc1/managing-rp-jwk_uri.html) endpoint.
>
> For details, refer to [Social authentication](../self-service/social-registration.html).

> **Collapse: Certificates for mTLS client authentication**
>
> This table shows the label of the trusted CA or self-signed certificate for mTLS client authentication when Advanced Identity Cloud acts as a relying party (RP) of the social identity provider service:
>
> | Secret label                                        | Algorithms                                                   |
> | --------------------------------------------------- | ------------------------------------------------------------ |
> | `am.services.oauth2.tls.client.cert.authentication` | Consult the `.well-known` endpoint of the identity provider. |
>
> The public key is exposed at the [/oauth2/connect/rp/jwk\_uri](../am-oidc1/managing-rp-jwk_uri.html) endpoint.
>
> For details, refer to [Social authentication](../self-service/social-registration.html).

## Web and Java agent secrets

> **Collapse: Sign agent JWTs**
>
> This table shows the label for the secret to sign the JWTs issued to Web and Java agents:
>
> | Secret label                                           | Algorithms        |
> | ------------------------------------------------------ | ----------------- |
> | `am.global.services.oauth2.oidc.agent.idtoken.signing` | RS256 RS384 RS512 |

## Authentication secrets

> **Collapse: Secure journey state data**
>
> This table shows the label for the secret to encrypt sensitive data in the secure state of an authentication journey:
>
> | Secret label                               | Algorithms  |
> | ------------------------------------------ | ----------- |
> | `am.authn.trees.transientstate.encryption` | AES 256-bit |

> **Collapse: Secret label mappings for persistent cookie nodes**
>
> The following table shows the secret label mappings used to encrypt and sign persistent cookies for the [Set Persistent Cookie node](https://docs.pingidentity.com/auth-node-ref/latest/set-persistent-cookie.html) and [Persistent Cookie Decision node](https://docs.pingidentity.com/auth-node-ref/latest/persistent-cookie-decision.html):
>
> | Secret label                                                      | Algorithms               |
> | ----------------------------------------------------------------- | ------------------------ |
> | `am.authentication.nodes.persistentcookie.encryption` (1)         | RSA (at least 2048 bits) |
> | `am.authentication.nodes.persistentcookie.identifier.signing` (2) |                          |
>
> (1) The `am.authentication.nodes.persistentcookie.encryption` label overrides the value for Persistent Cookie Encryption Certificate Alias in the [Core authentication attributes](../am-authentication/realm-auth-config.html).
>
> (2) Map the `am.authentication.nodes.persistentcookie.identifier.signing` dynamic secret label to override the HMAC Signing Key node property, where identifier is the value of the HMAC Signing Key Secret Label Identifier.
>
> |   |                                                                                                                                                                                                                                                                                                                                            |
> | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
> |   | To read the persistent cookies generated by the [Set Persistent Cookie node](https://docs.pingidentity.com/auth-node-ref/latest/set-persistent-cookie.html), configure the [Persistent Cookie Decision node](https://docs.pingidentity.com/auth-node-ref/latest/persistent-cookie-decision.html) to use the same signing key secret label. |

> **Collapse: Secret label mappings for RADIUS nodes**
>
> The [RADIUS Decision node](https://docs.pingidentity.com/auth-node-ref/latest/radius-decision.html) secures all conversations between Advanced Identity Cloud and the RADIUS server with the secret mapped to this secret label:
>
> | Secret label                                       | Algorithms |
> | -------------------------------------------------- | ---------- |
> | `am.authentication.nodes.radius.identifier.secret` |            |

## SAML 2.0 secrets

> **Collapse: Sign SAML 2.0 metadata**
>
> This table shows the label for the secret to sign SAML 2.0 metadata:
>
> | Secret label                             | Algorithms  |
> | ---------------------------------------- | ----------- |
> | `am.services.saml2.metadata.signing.RSA` | RSA SHA-256 |

> **Collapse: SAML 2.0 signing and encryption**
>
> The following table shows the secret label mappings used to sign and encrypt SAML 2.0 elements, and to enable mTLS authentication between entity providers:
>
> | Secret label                                                                | Algorithms                                                                                             |
> | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
> | `am.default.applications.federation.entity.providers.saml2.idp.encryption`  | RSA with PKCS#1 v1.5 padding RSA with OAEP                                                             |
> | `am.default.applications.federation.entity.providers.saml2.idp.signing`     | RSA SHA-1(1) ECDSA SHA-256 ECDSA SHA-384 ECDSA SHA-512 RSA SHA-256 RSA SHA-384 RSA SHA-512 DSA SHA-256 |
> | `am.default.applications.federation.entity.providers.saml2.sp.encryption`   | RSA with PKCS#1 v1.5 padding RSA with OAEP                                                             |
> | `am.default.applications.federation.entity.providers.saml2.sp.signing`      | RSA SHA-1(1) ECDSA SHA-256 ECDSA SHA-384 ECDSA SHA-512 RSA SHA-256 RSA SHA-384 RSA SHA-512 DSA SHA-256 |
> | `am.default.applications.federation.entity.providers.saml2.sp.mtls`(2)      |                                                                                                        |
> | `am.applications.federation.entity.providers.saml2.identifier.basicauth`(3) |                                                                                                        |
>
> (1) This algorithm is for compatibility purposes only. Avoid its use.
>
> (2) For artifact resolution requests only, the SP uses the certificates mapped to this secret label for mTLS authentication to the remote IDP. These certificates are exported with `<KeyDescriptor use="signing">` in the SP metadata.
>
> (3) The SP uses the certificate mapped to this secret label for basic authentication. If you set a Secret Label Identifier, and Advanced Identity Cloud finds a mapping to `am.applications.federation.entity.providers.saml2.identifier .basicauth`, Advanced Identity Cloud uses this secret and ignores the value of the Password field. For basic authentication, there is no *default* secret label for the realm, or globally.
>
> You can specify a custom Secret Label Identifier for each SAML 2.0 entity provider in a realm. Advanced Identity Cloud generates new secret labels that can be unique to the provider, or shared by multiple providers.
>
> For example, you could add a custom secret label identifier named *mySamlSecrets* to a hosted identity provider. Advanced Identity Cloud then dynamically creates the following secret labels, which the hosted identity provider uses for signing and encryption:
>
> * `am.applications.federation.entity.providers.saml2.mySamlSecrets.signing`
>
> * `am.applications.federation.entity.providers.saml2.mySamlSecrets.encryption`
>
> Advanced Identity Cloud attempts to look up the secrets with the custom secret label identifier. If unsuccessful, Advanced Identity Cloud looks up the secrets using the default secret labels.

## Attestation secrets

> **Collapse: Google hardware attestation root certificate**
>
> This table shows the label for the Google hardware attestation root certificate, which is used to increase confidence that the keys used by bound Android devices are valid, have not been revoked, and use hardware-backed security storage.
>
> Refer to [Verifying hardware-backed key pairs with Key Attestation](https://developer.android.com/training/articles/security-key-attestation#root_certificate) in the Android developer documentation.
>
> | Secret label                                | Algorithms  |
> | ------------------------------------------- | ----------- |
> | `am.services.attestation.google.public.key` | RSA / X.509 |

## Encrypted device storage services

> **Collapse: Secret label mappings for encrypted device storage services**
>
> The secret label mappings for services that use encrypted device storage.
>
> These mappings override the encryption keys set in the service configuration.
>
> | Service                                                                                               | Secret label                                   |
> | ----------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
> | [Device ID Service](services-configuration.html#realm-deviceidservice)                                | `am.services.deviceid.encryption`              |
> | [Device Binding Service](services-configuration.html#realm-devicebindingservice)                      | `am.services.devicebinding.encryption`         |
> | [Device Profile Service](services-configuration.html#realm-deviceprofilesservice)                     | `am.services.deviceprofile.encryption`         |
> | [WebAuthn Profile Encryption Service](services-configuration.html#realm-authenticatorwebauthnservice) | `am.services.authenticatorwebauthn.encryption` |
> | [ForgeRock Authentication (OATH) Service](services-configuration.html#realm-authenticatoroathservice) | `am.services.authenticatoroath.encryption`     |
> | [ForgeRock Authentication (PUSH) Service](services-configuration.html#realm-authenticatorpushservice) | `am.services.authenticatorpush.encryption`     |

## Http Client service secrets

> **Collapse: HTTP client mTLS certificates**
>
> The following table shows the secret label mappings for CA certificates used by the [httpclient](../am-scripting/script-bindings.html#common-httpclient) script binding to secure HTTP requests.
>
> | Secret label                                                        | Algorithms |
> | ------------------------------------------------------------------- | ---------- |
> | `am.services.httpclient.mtls.clientcert.identifier.secret`(1)       |            |
> | `am.services.httpclient.mtls.servertrustcerts.identifier.secret`(2) |            |
>
> (1) Map the `am.services.httpclient.mtls.clientcert.identifier.secret` dynamic secret label to the certificate to be used by the `httpclient` script binding when making HTTP requests. The identifier is the value of the Client Certificate Secret Label Identifier set in the HTTP Client service configuration.
>
> (2) Map the `am.services.httpclient.mtls.servertrustcerts.identifier.secret` dynamic secret label to the truststore of certificates that verify the server certificate. The identifier is the value of Server Trust Certificate Secret Label Identifier set in the HTTP Client service configuration.

> **Collapse: HTTP client proxy connection**
>
> The following table shows the secret label mappings used by the [httpclient](../am-scripting/script-bindings.html#common-httpclient) script binding to route HTTP requests through a proxy connection.
>
> | Secret label                                        | Algorithms |
> | --------------------------------------------------- | ---------- |
> | `am.services.httpclient.proxy.identifier.secret`(1) |            |
>
> (1) Map the `am.services.httpclient.proxy.identifier.secret` dynamic secret label to the secret to be used by the `httpclient` script binding when making HTTP requests. The identifier is the value of the Proxy Secret Label Identifier set in the HTTP Client service configuration.

## PingOne Worker service

> **Collapse: PingOne Worker service**
>
> The following table shows the secret label mappings used when configuring the [PingOne Worker service](services-configuration.html#realm-pingone-worker-service):
>
> | Secret label                                             | Default alias | Algorithms |
> | -------------------------------------------------------- | ------------- | ---------- |
> | `am.services.pingone.worker.identifier.clientsecret` (1) |               |            |
> | `am.services.pingone.worker.identifier.credential` (2)   |               |            |
>
> (1) The identifier is the value of the Client Secret Label Identifier set in the PingOne Worker service configuration.
>
> (2) The identifier is the value of the Credential Secret Label Identifier set in the PingOne Worker service configuration.

## Policy Configuration service secrets

> **Collapse: Certificates for the Policy Configuration service**
>
> This table shows the labels for secrets to encrypt the certificate used to authenticate Policy Configuration service connections:
>
> | Secret label                            | Algorithms(1)                       |
> | --------------------------------------- | ----------------------------------- |
> | `am.services.oauth2.oidc.signing.ES256` |                                     |
> | `am.services.oauth2.oidc.signing.ES384` | ES384                               |
> | `am.services.oauth2.oidc.signing.ES512` | ES512                               |
> | `am.services.oauth2.oidc.signing.RSA`   | PS256 PS384 PS512 RS256 RS384 RS512 |
> | `am.services.oauth2.oidc.signing.EDDSA` | EdDSA with SHA-512                  |
>
> For *confidential clients*, if you select an HMAC algorithm for signing ID tokens (`HS256`, `HS384`, or `HS512`), Advanced Identity Cloud uses the Client Secret from the profile instead of an entry from the secret store.

## Push Notification service secrets

> **Collapse: Sign the Push Notification service access key**
>
> This table shows the label for secrets to sign the Amazon Simple Notification Service access key used by the Push Notification service.
>
> The secret label mapping overrides the SNS Access Key Secret set in the service configuration.
>
> | Secret label                                        | Algorithms |
> | --------------------------------------------------- | ---------- |
> | `am.services.pushnotification.sns.accesskey.secret` |            |

## WebAuthn Metadata service secrets

> **Collapse: WebAuthn Metadata**
>
> The [WebAuthn Metadata service](services-configuration.html#webauthn-metadata-service) verifies the FIDO metadata blob signature against secrets mapped to this secret label.
>
> | Secret label                                                           | Algorithms |
> | ---------------------------------------------------------------------- | ---------- |
> | `am.authentication.nodes.webauthn.fidometadataservice.rootcertificate` |            |