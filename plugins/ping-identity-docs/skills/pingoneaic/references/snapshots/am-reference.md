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
  ref-gsm-pubsub-metrics: GSM Pub/Sub metrics
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

## GSM Pub/Sub metrics

Advanced Identity Cloud exposes the following metric for monitoring Google Cloud Platform (GCP) Pub/Sub subscription health for Google Secret Manager (GSM) stores:

> **Collapse: Prometheus GSM Pub/Sub metrics**
>
> | Name                                                                    | Type  | Description                                                                                                                                                  |
> | ----------------------------------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
> | `am_gsm_pubsub_subscription_active{store=store name,realm=realm path,}` | Gauge | Set to `1` when the store's Pub/Sub subscription is connected, and to `0` if initial subscription creation fails or if all reconnect attempts are exhausted. |
>
> **GSM Pub/Sub metrics labels**
>
> | Label        | Values                                              |
> | ------------ | --------------------------------------------------- |
> | `store name` | The secret store name, for example, `my-gsm-store`. |
> | `realm path` | The realm path, for example, `/alpha`.              |

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
  realm-deviceidservice: Device ID Service
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
  realm-osconfigurationsservice: OneSpan Configuration
  realm-pingone-worker-service: PingOne Worker service
  configuration: Configuration
  realm-pingone-worker-service-secondary-config: Secondary Configurations
  test-connection: Test the connection
  realm-policyconfiguration: Policy Configuration
  realm-pushnotification: Push Notification Service
  realm-remoteconsentservice: Remote Consent Service
  realm-selfservicetrees: Self Service Trees
  realm-session: Session
  realm-session-dynamic-attributes: Dynamic Attributes
  realm-amsessionpropertywhitelist: Session Property Whitelist Service
  realm-socialauthentication: Social Authentication Implementations
  realm-socialidentityproviders: Social Identity Provider Service
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

You now configure these settings in the Advanced Identity Cloud admin console. To do this, go to Authentication > Authentication Methods > Android Key Attestation.

Learn more in [Android Key Attestation settings](../authentication/authentication-methods-android-key-attestation.html).

### Base URL Source

The following settings are available in this service:

* Base URL Source

  Specifies how the base URL is generated.

  The following values are supported:

  * **Extension class** (`EXTENSION_CLASS`). This value doesn't apply to Advanced Identity Cloud.

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

### Device ID Service

This service doesn't apply to Advanced Identity Cloud.

### Device Binding service

You now configure these settings in the Advanced Identity Cloud admin console. To do this, go to Authentication > Authentication Methods > Device Binding.

Learn more in [Device binding settings](../authentication/authentication-methods-device-binding.html).

### Device Profiles Service

The following settings are available in this service:

* Profile Storage Attribute

  The user's attribute in which to store Device profiles.

* Device Profile Encryption Scheme

  Encryption scheme to use to secure device profiles stored on the server.

  If enabled, each device profile is encrypted using a unique random secret key using the given strength of AES encryption in CBC mode with PKCS#5 padding. An HMAC-SHA of the given strength (truncated to half-size) is used to ensure integrity protection and authenticated encryption. The unique random key is encrypted with the given RSA key pair and stored with the data.

  The possible values for this property are:

  * `AES-256/HMAC-SHA-512 with RSA Key Wrapping`

  * `AES-128/HMAC-SHA-256 with RSA Key Wrapping`

  * `No encryption of device settings.`

  Default value: `No encryption of device settings.`

* Encryption Key Store

  Path to the key store from which to load encryption keys.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Updating this setting isn't currently supported in Advanced Identity Cloud. Changing its value may lead to a loss of functionality in this feature.For greater security, store encryption key information in [ESVs](../tenants/esvs-signing-encryption.html), instead of in the configuration. Use the [secret label](secret-id-mappings.html#encrypted-device-storage-secret-labels) `am.services.deviceprofiles.encryption` to map an alias for Device Profiles service secrets.If you update encryption key information in the configuration or in the secret stores, users with existing device profiles will no longer be able to log in using this service. Delete the end user's device profile so that they can create a new one when they next log in. |

  |   |                                                                                                                                                                  |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If Advanced Identity Cloud finds a matching secret for the `am.services.deviceprofiles.encryption` label in the realm's ESV secret store, this value is ignored. |

* Key Store Type

  Type of key store to load.

  This property is preconfigured in your Advanced Identity Cloud tenant and shouldn't be altered.

  Default value: `Java Key Store (JKS).`

* Key Store Password

  Password to unlock the key store. This password is encrypted when it is saved in the Advanced Identity Cloud configuration.

  |   |                                                                                                                                                                  |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If Advanced Identity Cloud finds a matching secret for the `am.services.deviceprofiles.encryption` label in the realm's ESV secret store, this value is ignored. |

* Key-Pair Alias

  Alias of the certificate and private key in the key store. The private key is used to encrypt and decrypt device profiles.

  |   |                                                                                                                                                                  |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If Advanced Identity Cloud finds a matching secret for the `am.services.deviceprofiles.encryption` label in the realm's ESV secret store, this value is ignored. |

* Private Key Password

  Password to unlock the private key.

  |   |                                                                                                                                                                  |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If Advanced Identity Cloud finds a matching secret for the `am.services.deviceprofiles.encryption` label in the realm's ESV secret store, this value is ignored. |

### Email Service

|   |                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------- |
|   | The `openidm` binding provides more complete email functionality than the email service. Use `openidm` to send emails from scripts. |

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

You now configure these settings in the Advanced Identity Cloud admin console. To do this, go to Authentication > Authentication Methods > One-time Passcode (TOTP).

Learn more in [One-time passcode (TOTP) settings](../authentication/authentication-methods-totp.html).

### ForgeRock Authenticator (Push) Service

You now configure these settings in the Advanced Identity Cloud admin console. To do this, go to Authentication > Authentication Methods > Push Authentication.

Learn more in [Push authentication settings](../authentication/authentication-methods-push-authentication.html).

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

You now configure these settings in the Advanced Identity Cloud admin console. To do this, go to Authorization > OAuth2 Provider.

Learn more in [Configure Advanced Identity Cloud as an authorization server](../authorization/oauth2-provider.html).

### OneSpan Configuration

You now configure these settings in the Advanced Identity Cloud admin console. To do this, go to Integrations > Identity Verification > OneSpan.

Learn more in [OneSpan settings](../authentication/identity-verification-onespan.html).

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

You now configure these settings in the Advanced Identity Cloud admin console. To do this, go to Authentication > Authentication Methods > Push Notification Delivery.

Learn more in [Push notification delivery settings](../authentication/authentication-methods-push-notification.html).

### Remote Consent Service

You now configure these settings in the Advanced Identity Cloud admin console. To do this, go to Authorization > Remote Consent Service.

Learn more in [Remote consent service](../authorization/remote-consent-service.html).

### Self Service Trees

This service is now configured in the Advanced Identity Cloud admin console. To configure this service, go to Authenication > Self-service journeys.

Learn more in [Self-service journeys](../self-service/self-service-journeys.html).

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

This service is now configured in the Advanced Identity Cloud admin console. To configure this service, go to Integrations > Identity Providers.

Learn more in [Social authentication](../authentication/social-authentication.html).

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

You now configure these settings in the Advanced Identity Cloud admin console. To do this, go to Authentication > Authentication Methods > WebAuthn storage & encryption service.

Learn more in [WebAuthn storage & encryption settings](../authentication/authentication-methods-webauthn-encryption.html).

### WebAuthn Metadata service

You now configure these settings in the Advanced Identity Cloud admin console. To do this, go to Authentication > Authentication Methods > WebAuthn Verification.

Learn more in [WebAuthn verification settings](../authentication/authentication-methods-webauthn-verification.html).

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
> The public key is exposed at the [/oauth2/connect/rp/jwk_uri](../am-oidc1/managing-rp-jwk_uri.html) endpoint.
>
> For details, refer to [Social authentication](../authentication/social-authentication.html).

> **Collapse: Sign JWTs and objects**
>
> This table shows the label for the secret to sign JWTs and objects when Advanced Identity Cloud acts as a relying party (RP) of the social identity provider service:
>
> | Secret label                                          | Algorithms                                                   |
> | ----------------------------------------------------- | ------------------------------------------------------------ |
> | `am.services.oauth2.oidc.rp.jwt.authenticity.signing` | Consult the `.well-known` endpoint of the identity provider. |
>
> The public key is exposed at the [/oauth2/connect/rp/jwk_uri](../am-oidc1/managing-rp-jwk_uri.html) endpoint.
>
> For details, refer to [Social authentication](../authentication/social-authentication.html).

> **Collapse: Certificates for mTLS client authentication**
>
> This table shows the label of the trusted CA or self-signed certificate for mTLS client authentication when Advanced Identity Cloud acts as a relying party (RP) of the social identity provider service:
>
> | Secret label                                        | Algorithms                                                   |
> | --------------------------------------------------- | ------------------------------------------------------------ |
> | `am.services.oauth2.tls.client.cert.authentication` | Consult the `.well-known` endpoint of the identity provider. |
>
> The public key is exposed at the [/oauth2/connect/rp/jwk_uri](../am-oidc1/managing-rp-jwk_uri.html) endpoint.
>
> For details, refer to [Social authentication](../authentication/social-authentication.html).

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

> **Collapse: Persistent cookie nodes**
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

> **Collapse: Authentication nodes**
>
> The dynamic secret labels for authentication nodes, where identifier is defined in the node configuration:
>
> | Node                                                                                                                                                                                                                              | Secret label                                                          |
> | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
> | [AD Decision node](https://docs.pingidentity.com/auth-node-ref/latest/ad-decision.html)                                                                                                                                           | `am.authentication.nodes.ad.decision.mtls.identifier.cert`            |
> | [CAPTCHA node](https://docs.pingidentity.com/auth-node-ref/latest/captcha.html)                                                                                                                                                   | `am.authentication.nodes.captcha.identifier.secret`                   |
> | [Certificate Validation node](https://docs.pingidentity.com/auth-node-ref/latest/certificate-validation.html)                                                                                                                     | `am.authentication.nodes.certificate.validation.mtls.identifier.cert` |
> | [JWT Password Replay node](https://docs.pingidentity.com/auth-node-ref/latest/jwt-password-replay.html)                                                                                                                           | `am.authentication.nodes.jwt.replay.identifier.encryption`            |
> | [LDAP Decision node](https://docs.pingidentity.com/auth-node-ref/latest/ldap-decision.html)                                                                                                                                       | `am.authentication.nodes.ldap.decision.mtls.identifier.cert`          |
> | [OTP Email Sender node](https://docs.pingidentity.com/auth-node-ref/latest/otp-email-sender.html)                                                                                                                                 | `am.authentication.nodes.otp.mail.identifier.password`                |
> | [OTP SMS Sender node](https://docs.pingidentity.com/auth-node-ref/latest/otp-sms-sender.html)                                                                                                                                     | `am.authentication.nodes.otp.sms.identifier.password`                 |
> | [Persistent Cookie Decision node](https://docs.pingidentity.com/auth-node-ref/latest/persistent-cookie-decision.html) [Set Persistent Cookie node](https://docs.pingidentity.com/auth-node-ref/latest/set-persistent-cookie.html) | `am.authentication.nodes.persistentcookie.identifier.signing`         |
> | [RADIUS Decision node](https://docs.pingidentity.com/auth-node-ref/latest/radius-decision.html)                                                                                                                                   | `am.authentication.nodes.radius.identifier.secret`                    |
> | [reCAPTCHA Enterprise node](https://docs.pingidentity.com/auth-node-ref/latest/recaptcha-enterprise.html)                                                                                                                         | `am.authentication.nodes.captchaEnterprise.identifier.secret`         |
> | [RSA SecurID node](https://docs.pingidentity.com/auth-node-ref/latest/rsa-securid.html)                                                                                                                                           | `am.authentication.nodes.securid.identifier.client.key`               |
> | [WebAuthn Registration node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-registration.html)                                                                                                                       | `am.authentication.nodes.webauthn.truststore.identifier`              |

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
> | [Device Binding Service](services-configuration.html#realm-devicebindingservice)                      | `am.services.devicebinding.encryption`         |
> | [Device Profile Service](services-configuration.html#realm-deviceprofilesservice)                     | `am.services.deviceprofiles.encryption`        |
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