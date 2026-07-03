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
