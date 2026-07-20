---
title: API metrics
description: Reference for PingIDM API metrics at the /api endpoint, including metric types and names for recon, sync, JVM, Jetty, scheduler, and workflow
component: pingidm
version: 8.1
page_id: pingidm:monitoring-guide:api-metrics
canonical_url: https://docs.pingidentity.com/pingidm/8.1/monitoring-guide/api-metrics.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Monitoring"]
section_ids:
  crest-metric-types: Metric types
  crest-summary: Summary
  crest-timer: Timer
  crest-gauge: Gauge
  crest-counter: Counter
  api-metric-names: API metrics available in IDM
  api-jetty-metric-names: API Jetty metrics available in IDM
  api-jvm-metric-names: API JVM metrics available in IDM
  api-scheduler-metric-names: API scheduler metrics available in IDM
  api-workflow-metric-names: API workflow metrics available in IDM
---

# API metrics

|   |                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | IDM generates metrics only after a corresponding event occurs. For example, IDM doesn't create login-related metrics until a user logs in. If you're using a monitoring tool like Grafana, this may appear as missing data or empty panels on your dashboard. |

Metrics accessed at the `api` endpoint (such as those consumed by the Dropwizard dashboard widget) use dot notation for their metric names, for example, `recon.target-phase`.

## Metric types

The following metric types are available.

### Summary

The summary metric samples observations, providing a count of observations, sum total of observed amounts, average rate of events, and moving average rates across sliding time windows.

| Field       | Description                                                                                                                            |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `_id`       | The metric ID.                                                                                                                         |
| `_type`     | The metric type.                                                                                                                       |
| `count`     | The number of events recorded for this metric.                                                                                         |
| `total`     | The sum of the values of events recorded for this metric.	Because the increment is always 1, the total and the count are always equal. |
| `m1_rate`   | The one-minute average rate.                                                                                                           |
| `m5_rate`   | The five-minute average rate.                                                                                                          |
| `m15_rate`  | The fifteen-minute average rate.                                                                                                       |
| `mean_rate` | The average rate.                                                                                                                      |
| `units`     | A description of the units the metric is presented in.                                                                                 |

***Example***

```json
{
   "_id": "user.login.static-user",
   "m15_rate": 0.31152031322856183,
   "m1_rate": 0.009407098342403664,
   "m5_rate": 0.1889466210964059,
   "mean_rate": 0.00857374326779179,
   "units": "events/second",
   "total": 2.0,
   "count": 2,
   "_type": "summary"
}
```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | API summary metrics don't include a `quantile` grouping (designated with a footnote in [API metrics available in IDM](#api-metric-names)). There's a known issue where the `_total` metric isn't a total of the entire series. Instead, the `_total` metric is a total of each label group, which leads to identical metrics for the `_total` and `count`. You can find an example in the [Summary metric type](#crest-summary). |

### Timer

The timer metric combines rate and duration information.

| Field            | Description                                                   |
| ---------------- | ------------------------------------------------------------- |
| `_id`            | The metric ID.                                                |
| `_type`          | The metric type.                                              |
| `count`          | The number of events recorded for this metric.                |
| `total`          | The sum of the durations recorded for this metric.            |
| `min`            | The minimum duration recorded for this metric.                |
| `max`            | The maximum duration recorded for this metric.                |
| `mean`           | The mean average duration recorded for this metric.           |
| `stddev`         | The standard deviation of durations recorded for this metric. |
| `duration_units` | The units used for measuring the durations in the metric.     |
| `p50`            | 50% of the durations recorded are at or below this value.     |
| `p75`            | 75% of the durations recorded are at or below this value.     |
| `p95`            | 95% of the durations recorded are at or below this value.     |
| `p98`            | 98% of the durations recorded are at or below this value.     |
| `p99`            | 99% of the durations recorded are at or below this value.     |
| `p999`           | 99.9% of the durations recorded are at or below this value.   |
| `m1_rate`        | The one-minute average rate.                                  |
| `m5_rate`        | The five-minute average rate.                                 |
| `m15_rate`       | The fifteen-minute average rate.                              |
| `mean_rate`      | The average rate.                                             |
| `rate_units`     | The units used for measuring the rate of the metric.          |

|   |                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Duration-based values, such as `min`, `max`, and `p50`, are weighted toward newer data. By representing approximately the last five minutes of data, the timers make it easier to see recent changes in behavior, rather than a uniform average of recordings since the server was started. |

***Example***

```json
{
   "_id": "managed.user.queryCollection",
   "count": 9,
   "max": 14.78925,
   "mean": 8.440082684033516,
   "min": 3.8259589999999997,
   "p50": 8.211958,
   "p75": 11.111125,
   "p95": 14.78925,
   "p98": 14.78925,
   "p99": 14.78925,
   "p999": 14.78925,
   "stddev": 3.523788561175547,
   "m15_rate": 0.5581887695446408,
   "m1_rate": 0.20264650023649813,
   "m5_rate": 0.48307499952766003,
   "mean_rate": 0.10851915133390902,
   "duration_units": "milliseconds",
   "rate_units": "calls/second",
   "total": 75.987333,
   "_type": "timer"
}
```

### Gauge

The gauge metric is a numerical value that can increase or decrease. The value for a gauge is calculated when requested and represents the state of the metric at that specific time.

| Field   | Description                      |
| ------- | -------------------------------- |
| `_id`   | The metric ID.                   |
| `_type` | The metric type.                 |
| `value` | The current value of the metric. |

***Example***

```json
{
   "_id": "jvm.max-memory",
   "value": 2.147483648E9,
   "_type": "gauge"
}
```

### Counter

Metric providing a count of the *unique* events measured.

For example, this could be used to count the number of unique users who have authenticated or unique client IP addresses.

|   |                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------- |
|   | The `counter` metric is calculated per instance of IDM and can't be aggregated across multiple instances to get a site-wide view. |

| Field   | Description                                                                                                                            |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `_id`   | The metric ID.                                                                                                                         |
| `_type` | The metric type.  &#xA;&#xA;The counter type is reported as a gauge type. The output formats for counter and gauge type are identical. |
| `value` | The calculation of the number of unique values recorded in the metric.                                                                 |

***Example***

```json
{
   "_id": "jetty.request.max",
   "count": 6,
   "_type": "counter"
}
```

|   |                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Deprecated metrics are still available until they're removed in a future release. Learn more in [Deprecated metric collection](monitoring.html#deprecated-metric-collection). |

## API metrics available in IDM

| API Metric Name                                                                                                                                                        | Type      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `audit.audit-topic`\[[1](#_footnotedef_1 "View footnote.")]                                                                                                            | Summary   | Count of all audit events generated of a given topic type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `custom-endpoint.endpoint-name.request-type`                                                                                                                           | Timer     | Rate of calls to a custom endpoint script and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `field.augmentation.edge`                                                                                                                                              | Timer     | Rate of reading response objects to fulfill the `_fields` requested (when the fields weren't populated by the initial repo query).                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `field.augmentation.vertex`                                                                                                                                            | Timer     | Rate of reading response objects to fulfill the `_fields` requested (when the fields weren't populated by the initial repo query).                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []()`router-filter.name.action.script-name.quantile.system`\[[2](#_footnotedef_2 "View footnote.")]\[[3](#_footnotedef_3 "View footnote.")]                            | Timer     | Rate that filter scripts are executed per action. Monitors scripted filters and delegated administration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `icf_connector_server_availability.rcsName.rcsType`                                                                                                                    | Gauge     | Status of the connector server. A value of `1` indicates the server is running. A value of `0` indicates the server isn't running.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []()`icf_pending.connectorType.systemIdentifier.bundleVersion.location.objectClass.operation`\[[4](#_footnotedef_4 "View footnote.")]                                  | Gauge     | The number of pending requests over the configured limit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `icf.connectorType.systemIdentifier.bundleVersion.location.objectClass.query._queryExpression`                                                                         | Timer     | Rate of ICF query executions with queryExpression and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `icf.connectorType.systemIdentifier.bundleVersion.location.objectClass.query._queryFilter`                                                                             | Timer     | Rate of ICF query executions with queryFilter and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `icf.connectorType.systemIdentifier.bundleVersion.location.objectClass.query._queryId.queryId`                                                                         | Timer     | Rate of ICF query executions with queryId and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `icf.connectorType.systemIdentifier.bundleVersion.location.objectClass.query._UNKNOWN`                                                                                 | Timer     | Rate of ICF query executions when the query type is UNKNOWN and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `icf.connectorType.systemIdentifier.bundleVersion.location.objectClass.action.authenticate`                                                                            | Timer     | []()Rate of ICF authentication actions and action performance time for the given connector.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `icf.connectorType.systemIdentifier.bundleVersion.location.objectClass.create`                                                                                         | Timer     | Rate of ICF create operations and operation performance time for the given connector.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `icf.connectorType.systemIdentifier.bundleVersion.location.objectClass.delete`                                                                                         | Timer     | Rate of ICF delete operations and operation performance time for the given connector.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `icf.connectorType.systemIdentifier.bundleVersion.location.objectClass.patch`                                                                                          | Timer     | Rate of ICF patch operations and operation performance time for the given connector.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `icf.connectorType.systemIdentifier.bundleVersion.location.objectClass.read`                                                                                           | Timer     | Rate of ICF read operations and operation performance time for the given connector.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `icf.connectorType.systemIdentifier.bundleVersion.location.objectClass.update`                                                                                         | Timer     | Rate of ICF update operations and operation performance time for the given connector.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `icf.connectorType.systemIdentifier.bundleVersion.location.objectClass.liveSync`                                                                                       | []()Timer | Duration of live sync on a system object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `internal.managed-object.operation`                                                                                                                                    | Timer     | Rate of operations on internal objects.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `internal.managed-object.relationship.fetch-relationship-fields`                                                                                                       | Timer     | Rate of fetch operations of relationship fields for internal objects.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `internal.managed-object.relationship.get-relationship-value-for-resource`                                                                                             | Timer     | Query rate on relationship values for internal objects.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `internal.managed-object.script.script-name`                                                                                                                           | Timer     | Rate of script executions on internal object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `internal.managed-object.relationship.validate-relationship-fields`                                                                                                    | Timer     | Rate of validate operations of relationship fields for internal objects.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `managed.field.augmentation`                                                                                                                                           | Timer     | Rate of responses requiring field augmentation. When the repository can't retrieve all data in a single call, IDM performs additional read operations to complete (augment) the missing data.                                                                                                                                                                                                                                                                                                                                                                                     |
| `managed.managed-object.operation`                                                                                                                                     | Timer     | Rate of operations on a managed object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `managed.managed-object.relationship.fetch-relationship-fields`                                                                                                        | Timer     | Rate of fetches of relationship fields of a managed object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `managed.managed-object.relationship.get-relationship-value-for-resource`                                                                                              | Timer     | Rate of queries to get relationship values for a resource on a managed object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `managed.managed-object.relationship.validate-relationship-fields`                                                                                                     | Timer     | Rate of validations of relationship fields of a managed object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []()`managed-script-hook.object.script-hook`\[[5](#_footnotedef_5 "View footnote.")]\[[3](#_footnotedef_3 "View footnote.")]                                           | Timer     | Rate of executions of a script on a managed object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `managed.object.handle-temporal-constraints-on-create`                                                                                                                 | Timer     | Latency of enforcing temporal constraints on role objects during object creation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `managed.object.handle-temporal-constraints-on-delete`                                                                                                                 | Timer     | Latency of enforcing temporal constraints on role objects during object deletion.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `managed.object.handle-temporal-constraints-on-update`                                                                                                                 | Timer     | Latency of enforcing temporal constraints on role objects during object update.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `managed.relationship.handle-temporal-constraints-on-create`                                                                                                           | Timer     | Latency of enforcing temporal constraints on relationship grants during edge creation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `managed.relationship.handle-temporal-constraints-on-delete`                                                                                                           | Timer     | Latency of enforcing temporal constraints on relationship grants during edge deletion.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `managed.relationship.handle-temporal-constraints-on-update`                                                                                                           | Timer     | Latency of enforcing temporal constraints on relationship grants during edge update.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `managed.relationship.validate.read-relationship-endpoint-edges`                                                                                                       | Timer     | Rate of reads on relationship endpoint edges for validation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `null_array_filter.augmentationrequestType`                                                                                                                            | Timer     | Time spent in filter that maps non-nullable and null-valued array fields to an empty array. This filter is traversed for all repo access relating to internal and managed objects.                                                                                                                                                                                                                                                                                                                                                                                                |
| `recon`                                                                                                                                                                | Timer     | Rate of executions of a full reconciliation, and time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `recon-assoc-entry.merged-query.merge-results`                                                                                                                         | Timer     | Rate of merge operations after source and/or target objects have been retrieved during a merged query of recon association entries.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `recon-assoc-entry.merged-query.page-assoc-entries`                                                                                                                    | Timer     | Rate of individual paged recon association entry queries during a merged query. More than one page of entries might be requested to build a single page of merged results.                                                                                                                                                                                                                                                                                                                                                                                                        |
| `recon-assoc-entry.merged-query.query-source`                                                                                                                          | Timer     | Rate of source object retrieval using a query when merging source objects to recon association entries.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `recon-assoc-entry.merged-query.query-target`                                                                                                                          | Timer     | Rate of target object retrieval using a query when merging target objects to recon association entries.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `recon.association-persistence.recon-id-operation`                                                                                                                     | Timer     | The time taken to persist association data. The operation can be `source`, `target`, or `amendsource`, depending on whether data is being produced for a source-phase or target-phase recon association, or to amend the association for a specific source.                                                                                                                                                                                                                                                                                                                       |
| `recon.id-queries-phase`                                                                                                                                               | Timer     | Rate of executions of the id query phase of a reconciliation, and time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `recon.source-phase`                                                                                                                                                   | Timer     | Rate of executions of the source phase of a reconciliation, and time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `recon.source-phase.page`                                                                                                                                              | Timer     | Rate of pagination executions of the source phase of a reconciliation, and time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `recon.target-phase`                                                                                                                                                   | Timer     | Rate of executions of the target phase of a reconciliation, and time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `repo.jdbc.relationship.edge.execute.joinedToVertex`                                                                                                                   | Timer     | Time (ms) spent running the Edge→Vertex relationship join query on the database and collecting the result set.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `repo.jdbc.relationship.execute`                                                                                                                                       | Timer     | Rate of relationship graph query execution times.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `repo.jdbc.relationship.process`                                                                                                                                       | Timer     | Rate of relationship graph query result processing times.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `repo.raw._queryId.queryId`                                                                                                                                            | Timer     | Rate of executions of a query with queryId at a repository level and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `repo.repo-type.cache.objecttypes.event.resource-mapping`                                                                                                              | Count     | Counts the usage statistics of the `objecttypeid` cache, which maps an object type to its `objecttypeid`. The expected count is a small number of misses (sometimes, only one) and the remainder of hits.                                                                                                                                                                                                                                                                                                                                                                         |
| `repo.repo-typeget-connection`                                                                                                                                         | Timer     | Rate of retrievals of a repository connection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `repo.repo-type.operation.action_name.command.resource-mapping`                                                                                                        | Timer     | Rate of actions to a repository datasource for a generic/explicit mapped table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `repo.repo-type.operation._adhoc-expression.relationship`                                                                                                              | Timer     | Rate of filtered queries (using [native query expressions](../objects-guide/queries.html#native-queries)) on the relationship table. This metric measures the time spent making the query (in ms), and the number of times the query is invoked.                                                                                                                                                                                                                                                                                                                                  |
| `repo.repo-type.operation._adhoc-filter.relationship`                                                                                                                  | Timer     | Rate of filtered queries (using the `_queryFilter` parameter) on the relationship table. This metric measures the time spent making the query (in ms), and the number of times the query is invoked.                                                                                                                                                                                                                                                                                                                                                                              |
| `repo.repo-type.create_properties.execute.resource-mapping`                                                                                                            | Timer     | Rate of execution time on the JDBC database for the `create_properties` operations. This operation is performed for every generic object `create` when it persists the searchable properties. The rate measured here doesn't include the time taken to receive a connection to the database from the connection pool. The physical connections to the database have already been established inside the connection pool.                                                                                                                                                          |
| `repo.repo-type.operation.execute.resource-mapping`                                                                                                                    | Timer     | Rate of execution time on the JDBC database for CRUD operations. This rate doesn't include the time taken to receive a connection to the database from the connection pool. The physical connections to the database have already been established inside the connection pool.                                                                                                                                                                                                                                                                                                    |
| `repo.repo-type.query.execute.resource-mappingqueryType.]`                                                                                                             | Timer     | Rate of execution time on the JDBC database for queries (either `queryFilter` or `queryId`). This rate doesn't include the time taken to receive a connection to the database from the connection pool. The physical connections to the database have already been established inside the connection pool.                                                                                                                                                                                                                                                                        |
| `repo.repo-type.operation.relationship`                                                                                                                                | Timer     | Rate of CRUDPAQ operations to a repository datasource for a generic/explicit/relationship mapped table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `repo.repo-type.operation.relationship.stage.origin_type`                                                                                                              | Timer     | Time (ms) spent in the various phases to retrieve relationship expanded data referenced by queried objects.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `repo.repo-type.operation.resource-mapping`                                                                                                                            | Timer     | Rate of initiations of a CRUDPAQ operation to a repository datasource.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `router.path-name.action.action-type`                                                                                                                                  | Timer     | Rate of actions over the router and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `router.path-name.create`                                                                                                                                              | Timer     | Rate of creates over the router and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `router.path-name.delete`                                                                                                                                              | Timer     | Rate of deletes over the router and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `router.path-name.patch`                                                                                                                                               | Timer     | Rate of patches over the router and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `router.path-name.query.queryExpression`                                                                                                                               | Timer     | Rate of queries with queryExpression completed over the router and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `router.path-name.query.queryFilter`                                                                                                                                   | Timer     | Rate of queries with queryFilter completed over the router and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `router.path-name.read`                                                                                                                                                | Timer     | Rate of reads over the router and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `router.path-name.update`                                                                                                                                              | Timer     | Rate of updates over the router and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `sync.create-object`                                                                                                                                                   | Timer     | Rate of requests to create a target object, and time taken to perform the operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `sync.delete-target`                                                                                                                                                   | Timer     | Rate of requests to delete a target object, and time taken to perform the operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `sync.objectmapping.mapping-name`                                                                                                                                      | Timer     | Rate of configurations applied to a mapping.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `sync.queue.mapping-name.action.acquire`                                                                                                                               | Timer     | Rate of acquisition of queued synchronization events from the queue.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `sync.queue.mapping-name.action.discard`                                                                                                                               | Timer     | Rate of deletion of synchronization events from the queue.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `sync.queue.mapping-name.action.execution`                                                                                                                             | Timer     | Rate at which queued synchronization operations are executed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `sync.queue.mapping-name.action.failed`\[[1](#_footnotedef_1 "View footnote.")]                                                                                        | Summary   | Number of queued synchronization operations that failed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `sync.queue.mapping-name.action.precondition-failed`\[[1](#_footnotedef_1 "View footnote.")]                                                                           | Summary   | Number of queued synchronization events acquired by another node in the cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `sync.queue.mapping-name.action.rejected-executions`\[[1](#_footnotedef_1 "View footnote.")]                                                                           | Summary   | Number of queued synchronization events rejected because the backing thread-pool queue was at full capacity and the thread-pool had already allocated its maximum configured number of threads.                                                                                                                                                                                                                                                                                                                                                                                   |
| `sync.queue.mapping-name.action.release`                                                                                                                               | Timer     | Rate at which queued synchronization events are released.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `sync.queue.mapping-name.action.release-for-retry`                                                                                                                     | Timer     | Times the release of queued synchronization events after a failure and before exceeding the retry count.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `sync.queue.mapping-name.action.submit`                                                                                                                                | Timer     | Rate of insertion of synchronization events into the queue.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `sync.queue.mapping-name.poll-pending-events`                                                                                                                          | Timer     | The latency involved in polling for synchronization events.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `sync.raw-read-object`                                                                                                                                                 | Timer     | Rate of reads of an object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `sync.source.assess-situation`                                                                                                                                         | Timer     | Rate of assessments of a synchronization situation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `sync.source.correlate-target`                                                                                                                                         | Timer     | Rate of correlations between a target and a given source, and time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `sync.source.determine-action`                                                                                                                                         | Timer     | Rate of determinations done on a synchronization action based on its current situation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `sync.source.perform-action`                                                                                                                                           | Timer     | Rate of completions of an action performed on a synchronization operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `sync.target.assess-situation`                                                                                                                                         | Timer     | Rate of assessments of a target situation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `sync.target.determine-action`                                                                                                                                         | Timer     | Rate of determinations done on a target action based on its current situation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `sync.target.perform-action`                                                                                                                                           | Timer     | Rate of completions of an action performed on a target sync operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `sync.update-target`                                                                                                                                                   | Timer     | Rate of requests to update an object on the target, and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `user.login.user-type`\[[1](#_footnotedef_1 "View footnote.")]                                                                                                         | Summary   | Count of all successful logins by user type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `user.login.user-type.provider`\[[1](#_footnotedef_1 "View footnote.")]                                                                                                | Summary   | Count of all successful logins by user type and provider.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `virtual-properties-from-relationships.not-found.virtual_properties.resource_collection_relationship_field`\[[1](#_footnotedef_1 "View footnote.")]                    | Summary   | Number of 404 responses encountered when querying the `resource_collection`/`relationship_field` specified in the traversal\_depthX tag for the most recent X.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `virtual-properties-from-relationships.unsatisified-temp-constraint.virtual_properties.resource_collection_relationship_field`\[[1](#_footnotedef_1 "View footnote.")] | Summary   | Number of edges skipped due to an unsatisfied temporal constraint on either the edge or the referred-to vertex. Encountered when querying the resource collection and relationship field at the traversal\_depthX tag for the most recent X.                                                                                                                                                                                                                                                                                                                                      |
| `virtual-properties-from-relationships.virtual_properties.resource_collection_relationship_field`                                                                      | Timer     | Time spent traversing relationship fields to calculate the specified virtual properties. The managed objects linked to by the traversal relationship fields define a tree whose root is the virtual property host. This object tree is traversed depth-first with the traversal\_depthX corresponding to the latency involved with each relationship traversal. Traversal\_depth0 corresponds to the first relationship field traversed. Because the tree is traversed depth-first, traversal\_depthX subsumes all the traversal latencies for all traversal\_depth Y, where Y>X. |

## API Jetty metrics available in IDM

These metrics include Jetty thread pool and request metrics.

| API Metric Name                                                     | Type    | Unit        | Description                                                                                                                                    |
| ------------------------------------------------------------------- | ------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| []()`jetty.qos.queue.count`\[[6](#_footnotedef_6 "View footnote.")] | Gauge   | Count       | Current number of requests queued in the [Jetty QoSHandler](../install-guide/idm-config-properties-jetty.html#config-jetty-qos-handler) queue. |
| []()`jetty.qos.queue.count.max`                                     | Gauge   | Count       | Maximum number of requests that can be queued.                                                                                                 |
| []()`jetty.qos.queue.concurrent.max`                                | Gauge   | Count       | Maximum number of requests that can be handled concurrently.                                                                                   |
| []()`jetty.qos.queue.milliseconds.max`                              | Gauge   | Count       | Maximum amount of time a request can be queued.                                                                                                |
| `jetty.thread.queue`\[[6](#_footnotedef_6 "View footnote.")]        | Gauge   | Count       | Size of the job queue.                                                                                                                         |
| `jetty.thread.ready`                                                | Gauge   | Count       | Number of threads ready to run transient jobs, such as handling requests.                                                                      |
| `jetty.thread.leased`                                               | Gauge   | Count       | Number of threads used by internal Jetty components.                                                                                           |
| `jetty.thread.reserved`                                             | Gauge   | Count       | Number of available threads reserved for queue management.                                                                                     |
| `jetty.thread.idle`                                                 | Gauge   | Count       | Number of idle threads that aren't reserved.                                                                                                   |
| `jetty.thread.utilized`                                             | Gauge   | Count       | Number of threads currently running transient jobs, such as handling requests.                                                                 |
| `jetty.thread.total`                                                | Gauge   | Count       | Total number of threads in the pool.                                                                                                           |
| `jetty.thread.isLowOnThreads`                                       | Gauge   | Count       | Whether the pool is low on threads. `1` if true, `0` otherwise.                                                                                |
| `jetty.request.active`                                              | Gauge   | Count       | Current number of active requests.                                                                                                             |
| `jetty.request.max`                                                 | Counter | Count       | Maximum number of concurrently active requests.                                                                                                |
| `jetty.request.failed.4xx`                                          | Counter | Count       | Number of requests with a `4xx` response status.                                                                                               |
| `jetty.request.failed.5xx`                                          | Counter | Count       | Number of requests with a `5xx` response status.                                                                                               |
| `jetty.request.nanoseconds.max`                                     | Gauge   | Nanoseconds | Maximum request run time.                                                                                                                      |
| `jetty.request.nanoseconds.stddev`                                  | Gauge   | Nanoseconds | Standard deviation for request run time.                                                                                                       |
| `jetty.request.servlet.active`                                      | Gauge   | Count       | Current number of requests the servlets handle.                                                                                                |
| `jetty.request.servlet.max`                                         | Counter | Count       | Maximum number of requests the servlets handle concurrently.                                                                                   |
| `jetty.request.servlet.nanoseconds.max`                             | Gauge   | Nanoseconds | Maximum servlet run time.                                                                                                                      |
| `jetty.request.servlet.nanoseconds.stddev`                          | Gauge   | Nanoseconds | Standard deviation for servlet run time.                                                                                                       |

## API JVM metrics available in IDM

|   |                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | These metrics depend on the JVM version and configuration. In particular, garbage-collector-related metrics depend on the garbage collector that the server uses. The garbage-collector metric names are unstable and can change even in a minor JVM release. |

| API Metric Name                                                     | Type    | Unit         | Description                                                                                                                                                                                                                |
| ------------------------------------------------------------------- | ------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `jvm.available-cpus`                                                | Gauge   | Count        | Number of processors available to the JVM. Learn more about [Runtime](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runtime.html).                                                                |
| `jvm.class-loading.loaded.total`                                    | Counter | Count        | Number of classes loaded since the Java virtual machine started. Learn more about [ClassLoadingMXBean](https://docs.oracle.com/en/java/javase/21/docs/api/java.management/java/lang/management/ClassLoadingMXBean.html).   |
| `jvm.class-loading.unloaded.total`                                  | Counter | Count        | Number of classes unloaded since the Java virtual machine started. Learn more about [ClassLoadingMXBean](https://docs.oracle.com/en/java/javase/21/docs/api/java.management/java/lang/management/ClassLoadingMXBean.html). |
| `jvm.free-memory`                                                   | Gauge   | Bytes        | Learn more about [Runtime](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runtime.html).                                                                                                           |
| `jvm.garbage-collector.count.total_G1-Old-Generation`               | Count   | Count        | For each garbage collector in the JVM. Learn more about [GarbageCollectorMXBean](https://docs.oracle.com/en/java/javase/21/docs/api/java.management/java/lang/management/GarbageCollectorMXBean.html).                     |
| `jvm.garbage-collector.time.total_G1-Old-Generation`                | Counter | Milliseconds |                                                                                                                                                                                                                            |
| `jvm.garbage-collector.count.total_G1-Young-Generation`             | Counter | Count        |                                                                                                                                                                                                                            |
| `jvm.garbage-collector.time.total_G1-Young-Generation`              | Counter | Milliseconds |                                                                                                                                                                                                                            |
| `jvm.max-memory`                                                    | Gauge   | Bytes        | Learn more about [Runtime](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runtime.html).                                                                                                           |
| `jvm.memory-usage.committed_heap`                                   | Gauge   | Bytes        | Amount of heap memory committed for the JVM to use. Learn more about [MemoryMXBean](https://docs.oracle.com/en/java/javase/21/docs/api/java.management/java/lang/management/MemoryMXBean.html).                            |
| `jvm.memory-usage.init_heap`                                        | Gauge   | Bytes        |                                                                                                                                                                                                                            |
| `jvm.memory-usage.max_heap`                                         | Gauge   | Bytes        | Maximum amount of heap memory available to the JVM.                                                                                                                                                                        |
| `jvm.memory-usage.used_heap`                                        | Gauge   | Bytes        | Amount of heap memory used by the JVM.                                                                                                                                                                                     |
| `jvm.memory-usage.committed_non-heap`                               | Gauge   | Bytes        | Amount of non-heap memory committed for the JVM to use.                                                                                                                                                                    |
| `jvm.memory-usage.init_non-heap`                                    | Gauge   | Bytes        | Amount of non-heap memory the JVM initially requested from the operating system.                                                                                                                                           |
| `jvm.memory-usage.max_non-heap`                                     | Gauge   | Bytes        | Maximum amount of non-heap memory available to the JVM.                                                                                                                                                                    |
| `jvm.memory-usage.used_non-heap`                                    | Gauge   | Bytes        | Amount of non-heap memory used by the JVM.                                                                                                                                                                                 |
| `jvm.memory-usage.pools.committed_CodeHeap-'non-nmethods'`          | Gauge   | Bytes        | For each pool. Learn more about [MemoryPoolMXBean](https://docs.oracle.com/en/java/javase/21/docs/api/java.management/java/lang/management/MemoryPoolMXBean.html).                                                         |
| `jvm.memory-usage.pools.init_CodeHeap-'non-nmethods'`               | Gauge   | Bytes        |                                                                                                                                                                                                                            |
| `jvm.memory-usage.pools.max_CodeHeap-'non-nmethods'`                | Gauge   | Bytes        |                                                                                                                                                                                                                            |
| `jvm.memory-usage.pools.used_CodeHeap-'non-nmethods'`               | Gauge   | Bytes        |                                                                                                                                                                                                                            |
| `jvm.memory-usage.pools.committed_CodeHeap-'non-profiled-nmethods'` | Gauge   | Bytes        |                                                                                                                                                                                                                            |
| `jvm.memory-usage.pools.init_CodeHeap-'profiled-nmethods'`          | Gauge   | Bytes        |                                                                                                                                                                                                                            |
| `jvm.memory-usage.pools.max_CodeHeap-'non-profiled-nmethods'`       | Gauge   | Bytes        |                                                                                                                                                                                                                            |
| `jvm.memory-usage.pools.used_CodeHeap-'non-profiled-nmethods'`      | Gauge   | Bytes        |                                                                                                                                                                                                                            |
| `jvm.memory-usage.pools.committed_CodeHeap-'profiled-nmethods'`     | Gauge   | Bytes        |                                                                                                                                                                                                                            |
| `jvm.memory-usage.pools.init_CodeHeap-'non-profiled-nmethods'`      | Gauge   | Bytes        |                                                                                                                                                                                                                            |
| `jvm.memory-usage.pools.max_CodeHeap-'profiled-nmethods'`           | Gauge   | Bytes        |                                                                                                                                                                                                                            |
| `jvm.memory-usage.pools.used_CodeHeap-'profiled-nmethods'`          | Gauge   | Bytes        |                                                                                                                                                                                                                            |
| `jvm.memory-usage.pools.committed_Compressed-Class-Space`           | Gauge   | Bytes        |                                                                                                                                                                                                                            |
| `jvm.memory-usage.pools.init_Compressed-Class-Space`                | Gauge   | Bytes        |                                                                                                                                                                                                                            |
| `jvm.memory-usage.pools.max_Compressed-Class-Space`                 | Gauge   | Bytes        |                                                                                                                                                                                                                            |
| `jvm.memory-usage.pools.used_Compressed-Class-Space`                | Gauge   | Bytes        |                                                                                                                                                                                                                            |
| `jvm.memory-usage.pools.committed_G1-Eden-Space`                    | Gauge   | Bytes        |                                                                                                                                                                                                                            |
| `jvm.memory-usage.pools.init_G1-Eden-Space`                         | Gauge   | Bytes        |                                                                                                                                                                                                                            |
| `jvm.memory-usage.pools.max_G1-Eden-Space`                          | Gauge   | Bytes        |                                                                                                                                                                                                                            |
| `jvm.memory-usage.pools.used_G1-Eden-Space`                         | Gauge   | Bytes        |                                                                                                                                                                                                                            |
| `jvm.memory-usage.pools.used-after-gc_G1-Eden-Space`                | Gauge   | Bytes        |                                                                                                                                                                                                                            |
| `jvm.memory-usage.pools.committed_G1-Old-Gen`                       | Gauge   | Bytes        |                                                                                                                                                                                                                            |
| `jvm.memory-usage.pools.init_G1-Old-Gen`                            | Gauge   | Bytes        |                                                                                                                                                                                                                            |
| `jvm.memory-usage.pools.max_G1-Old-Gen`                             | Gauge   | Bytes        |                                                                                                                                                                                                                            |
| `jvm.memory-usage.pools.used_G1-Old-Gen`                            | Gauge   | Bytes        |                                                                                                                                                                                                                            |
| `jvm.memory-usage.pools.used-after-gc_G1-Old-Gen`                   | Gauge   | Bytes        |                                                                                                                                                                                                                            |
| `jvm.memory-usage.pools.committed_G1-Survivor-Space`                | Gauge   | Bytes        |                                                                                                                                                                                                                            |
| `jvm.memory-usage.pools.init_G1-Survivor-Space`                     | Gauge   | Bytes        |                                                                                                                                                                                                                            |
| `jvm.memory-usage.pools.max_G1-Survivor-Space`                      | Gauge   | Bytes        |                                                                                                                                                                                                                            |
| `jvm.memory-usage.pools.used_G1-Survivor-Space`                     | Gauge   | Bytes        |                                                                                                                                                                                                                            |
| `jvm.memory-usage.pools.used-after-gc_G1-Survivor-Space`            | Gauge   | Bytes        |                                                                                                                                                                                                                            |
| `jvm.memory-usage.pools.committed_Metaspace`                        | Gauge   | Bytes        |                                                                                                                                                                                                                            |
| `jvm.memory-usage.pools.init_Metaspace`                             | Gauge   | Bytes        |                                                                                                                                                                                                                            |
| `jvm.memory-usage.pools.max_Metaspace`                              | Gauge   | Bytes        |                                                                                                                                                                                                                            |
| `jvm.memory-usage.pools.used_Metaspace`                             | Gauge   | Bytes        |                                                                                                                                                                                                                            |
| `jvm.thread-state_blocked`                                          | Gauge   | Count        | Learn more about [ThreadMXBean](https://docs.oracle.com/en/java/javase/21/docs/api/java.management/java/lang/management/ThreadMXBean.html).                                                                                |
| `jvm.thread-state.daemon`                                           | Gauge   | Count        | Number of live daemon threads.                                                                                                                                                                                             |
| `jvm.thread-state_new`                                              | Gauge   | Count        | Number of threads in the `NEW` state.                                                                                                                                                                                      |
| `jvm.thread-state_runnable`                                         | Gauge   | Count        | Number of threads in the `RUNNABLE` state.                                                                                                                                                                                 |
| `jvm.thread-state_terminated`                                       | Gauge   | Count        | Number of threads in the `TERMINATED` state.                                                                                                                                                                               |
| `jvm.thread-state_timed_waiting`                                    | Gauge   | Count        | Number of threads in the `TIMED_WAITING` state.                                                                                                                                                                            |
| `jvm.thread-state_waiting`                                          | Gauge   | Count        | Number of threads in the `WAITING` state.                                                                                                                                                                                  |
| `jvm.used-memory`                                                   | Gauge   | Bytes        | Learn more about [totalMemory()](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runtime.html#totalMemory\(\)).                                                                                     |

|   |                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------ |
|   | [Deprecated](../release-notes/deprecated-functionality.html#deprecation-jvm-mem-usage-metrics) metrics aren't shown in the previous table. |

## API scheduler metrics available in IDM

Learn more about example requests in [Scheduler metrics](../schedules-guide/schedule-metrics.html).

| API Metric Name                                                                      | Type    | Description                                                                                           |
| ------------------------------------------------------------------------------------ | ------- | ----------------------------------------------------------------------------------------------------- |
| `scheduler.job.job-group.job-name.completed`\[[1](#_footnotedef_1 "View footnote.")] | Summary | A summary of completed jobs for the specified job-group and job-name.                                 |
| `scheduler.job.job-group.job-name.executed`                                          | Timer   | Time spent on executed jobs for the specified job-group and job-name.                                 |
| `scheduler.job-store.repo.operation.scheduler-object`                                | Timer   | Time spent storing scheduled jobs in the repository for the specified operation and scheduler-object. |
| `scheduler.trigger.acquired.success`\[[1](#_footnotedef_1 "View footnote.")]         | Summary | A summary of successfully acquired jobs.                                                              |
| `scheduler.trigger.acquired.timeout`\[[1](#_footnotedef_1 "View footnote.")]         | Summary | A summary of acquired jobs that time out.                                                             |
| `scheduler.trigger.fired`\[[1](#_footnotedef_1 "View footnote.")]                    | Summary | A summary of fired schedule triggers.                                                                 |
| `scheduler.trigger.misfired`\[[1](#_footnotedef_1 "View footnote.")]                 | Summary | A summary of misfired schedule triggers.                                                              |
| `scheduler.trigger.recovered`                                                        | Timer   | Time spent on recovered triggers.                                                                     |
| `scheduler.type.operation`                                                           | Timer   | Execution rate of scheduler requests for the specified type and operation.                            |

## API workflow metrics available in IDM

| API Metric Name                                     | Type  | Description                                                                 |
| --------------------------------------------------- | ----- | --------------------------------------------------------------------------- |
| `workflow.execution.action.message`                 | Timer | Time spent invoking a message event.                                        |
| `workflow.execution.action.signal`                  | Timer | Time spent invoking a signal event.                                         |
| `workflow.execution.action.trigger`                 | Timer | Time spent triggering an execution.                                         |
| `workflow.execution.query`                          | Timer | Time spent querying executions.                                             |
| `workflow.job.action.execute`                       | Timer | Time spent forcing synchronous execution of a job.                          |
| `workflow.job.action.stacktrace`                    | Timer | Time spent displaying the stacktrace for a job that triggered an exception. |
| `workflow.job.delete`                               | Timer | Time spent deleting a job.                                                  |
| `workflow.job.query`                                | Timer | Time spent querying jobs.                                                   |
| `workflow.job.read`                                 | Timer | Time spent reading a single job.                                            |
| `workflow.jobdeadletter.action.execute`             | Timer | Time spent to execute dead-letter job.                                      |
| `workflow.jobdeadletter.action.stacktrace`          | Timer | Time spent to retrieve the stacktrace for a dead-letter job.                |
| `workflow.jobdeadletter.delete`                     | Timer | Time spent to delete a dead letter job.                                     |
| `workflow.jobdeadletter.query`                      | Timer | Time spent to query dead letter jobs.                                       |
| `workflow.jobdeadletter.read`                       | Timer | Time spent to read a dead letter job.                                       |
| `workflow.model.action.deploy`                      | Timer | Time spent to deploy a model.                                               |
| `workflow.model.action.list_deployments`            | Timer | Time spent to list model deployments.                                       |
| `workflow.model.action.validate_bpmn`               | Timer | Time spent to validate BPMN content.                                        |
| `workflow.model.create`                             | Timer | Time spent to create a model.                                               |
| `workflow.model.delete`                             | Timer | Time spent to delete a model.                                               |
| `workflow.model.query`                              | Timer | Time spent to query models.                                                 |
| `workflow.model.read`                               | Timer | Time spent to read a model.                                                 |
| `workflow.model.update`                             | Timer | Time spent to update a model.                                               |
| `workflow.processdefinition.delete`                 | Timer | Time spent to delete a process definition.                                  |
| `workflow.processdefinition.query`                  | Timer | Time spent to query process definitions.                                    |
| `workflow.processdefinition.read`                   | Timer | Time spent to read a process definition.                                    |
| `workflow.processinstance.action.migrate`           | Timer | Time spent to migrate a process instance.                                   |
| `workflow.processinstance.action.validateMigration` | Timer | Time spent to validate a migration of a process instance.                   |
| `workflow.processinstance.create`                   | Timer | Time spent to create a process instance.                                    |
| `workflow.processinstance.delete`                   | Timer | Time spent to delete a process instance.                                    |
| `workflow.processinstance.query`                    | Timer | Time spent to query process instances.                                      |
| `workflow.processinstance.read`                     | Timer | Time spent to read a process instance.                                      |
| `workflow.taskdefinition.query`                     | Timer | Time spent to query task definitions.                                       |
| `workflow.taskdefinition.read`                      | Timer | Time spent to read a task definition.                                       |
| `workflow.taskinstance.action.complete`             | Timer | Time spent to complete a task instance.                                     |
| `workflow.taskinstance.query`                       | Timer | Time spent to query task instances.                                         |
| `workflow.taskinstance.read`                        | Timer | Time spent to read a task instance.                                         |
| `workflow.taskinstance.update`                      | Timer | Time spent to update a task instance.                                       |

***

[1](#_footnoteref_1). This summary metric doesn't include a quantile grouping and only has the metric\_name\_count and metric\_name\_total entries.[2](#_footnoteref_2). The "router-filter" metric name replaces the "filter" metric name. This metric can specify a "name" and "system" label. If no "name" label is specified, it defaults to "unknown". The "system" label is always system="false".[3](#_footnoteref_3). The deprecated metric names are still available and are generated along with the new metric names unless "deprecatedMetricsEnabled" is set to "false" in "conf/metrics.json".[4](#_footnoteref_4). A pending request gauge won't register until the associated RequestType has been invoked at least one time.[5](#_footnoteref_5). This metric naming convention replaces managed.managed-object.script.script-name and includes optional "object" and "script-hook" components.[6](#_footnoteref_6). The QoSHandler metric, jetty.qos.queue.count, accurately contains the number of queued requests in the handler queue and replaces the jetty.thread.queue metric.

---

---
title: Distributed tracing
description: Configure distributed tracing in PingIDM using OpenTelemetry to monitor request flows, troubleshoot errors, and visualize trace data
component: pingidm
version: 8.1
page_id: pingidm:monitoring-guide:distributed-tracing
canonical_url: https://docs.pingidentity.com/pingidm/8.1/monitoring-guide/distributed-tracing.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Monitoring", "Distributed tracing"]
section_ids:
  tracing-benefits: Tracing benefits
  idm_and_opentelemetry: IDM and OpenTelemetry
  request_types_supported_in_idm: Request types supported in IDM
  understand-trace-object: Understand a trace object
  enable-tracing: Enable distributed tracing
  disable-tracing: Disable distributed tracing
  configure-distributed-tracing: Configure distributed tracing
  viz-otel-traces: Visualize traces with a trace collector
  ex-viz-trace-collector: Example visualization with a trace collector
---

# Distributed tracing

|   |                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Distributed tracing is an [Evolving](../release-notes/appendix-interface-stability.html) feature in PingIDM. It's subject to change without notice, even in a minor or maintenance release. |

Distributed tracing helps you monitor and observe system requests as they flow through IDM. A request is tracked and analyzed with a unique identifier (ID) used to troubleshoot requests that show errors or performance issues. This unique ID remains with a transaction as it interacts with microservices, containers, and infrastructure.

When a user interacts with the Ping Identity Platform, the request can travel through multiple services before it completes. Distributed tracing lets you monitor the request flow through the Ping Identity Platform.

## Tracing benefits

Distributed tracing makes it easier to:

* Provide a single view of a request's journey

* Locate bottlenecks and errors

* Identify slow services

* Optimize application performance and reduce debugging time

* Improve the end-user experience

## IDM and OpenTelemetry

IDM supports the [OpenTelemetry framework](https://opentelemetry.io/docs/what-is-opentelemetry/) (OTEL) for collecting [distributed tracing](#distributed-tracing) and [logging](opentelemetry-logging.html) data.

OpenTelemetry handles:

* Generation

* Collection

* Management

* Export of telemetry

|   |                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | OpenTelemetry doesn't handle telemetry storage and visualization. You can use a trace collector, such as [Jaeger](https://www.jaegertracing.io/), to collect and visualize trace data. |

## Request types supported in IDM

IDM supports distributed tracing for the following request types:

* Incoming HTTP requests

* Outgoing HTTP requests to PingAM (Ping Identity Platform deployments only)

* Outgoing LDAP requests

  These requests are searchable and identifiable for the following LDAP operations:

  * ADD

  * MODIFY

  * SEARCH

  * DELETE

  * BIND

* Outgoing scripting HTTP requests

  |   |                                                                                                                                     |
  | - | ----------------------------------------------------------------------------------------------------------------------------------- |
  |   | Outgoing scripting HTTP requests must use the `openidm.action` function to make an external call using IDM's external REST service. |

## Understand a trace object

A *trace* represents the path of a request through an application. A trace is made up of one or more *spans*.

Each span includes the following elements:

* `traceId`: Representing the trace that the span is a part of

* `spanId`: A unique ID for that span

* `parentSpanId`: The ID of the originating request

The *root span* indicates the start and end of an entire operation. The `parentSpanId` of the root span is `null` because the root span isn't part of an existing trace.

Subsequent spans in the trace have their own unique `spanId`. The `traceId` is the same as that of the root span. The `parentId` matches the `spanId` of the root span.

Learn more in [Traces](https://opentelemetry.io/docs/concepts/signals/traces/) in the OpenTelemetry documentation.

## Enable distributed tracing

|   |                                             |
| - | ------------------------------------------- |
|   | Distributed tracing is disabled by default. |

To enable distributed tracing:

1. In the `/path/to/openidm` directory, create a `/trace` directory, for example, where you can place the tracing configuration file.

   |   |                                                                                                                                |
   | - | ------------------------------------------------------------------------------------------------------------------------------ |
   |   | The configuration file isn't required to be in the `/conf` directory. You can place this file in any location readable by IDM. |

2. In the `/trace` directory, for example, create an OTEL configuration JSON file with the following information and set `"enabled": true`:

   ```json
   {
     "tracing": {
       "enabled": true,
       "exporter": {
         "type": "otlp",
         "config": {
           "endpoint": "http://localhost:4318/v1/traces"
         }
       }
     }
   }
   ```

   You can find information on additional configuration properties in [Configure distributed tracing](#configure-distributed-tracing).

   |   |                                                                                                                                    |
   | - | ---------------------------------------------------------------------------------------------------------------------------------- |
   |   | If the content of the configuration file is invalid JSON, distributed tracing remains disabled, even if you set `"enabled": true`. |

3. IDM uses the environment variable `OPENIDM_TRACING_CONFIG_PATH`. Set this environment variable to point to the configuration file in `/path/to/openidm` or to any location readable by IDM, for example:

   ```
   OPENIDM_TRACING_CONFIG_PATH=/path/to/openidm/trace/tracing.json
   ```

4. After you create the OTEL configuration file in the directory that you choose and point the environment variable to the OTEL configuration file, [start IDM](../install-guide/chap-install.html#run-openidm).

   Starting IDM launches a service that reads the OTEL configuration file and monitors it for changes to perform runtime updates to the distributed tracing service.

### Disable distributed tracing

To disable distributed tracing:

In the OTEL configuration file, set `"enabled": false`.

After you've changed the configuration file, the service that detects configuration changes relaunches the distributed tracing service in a disabled state.

## Configure distributed tracing

The Ping Identity Platform supports a common set of configuration properties for OpenTelemetry support.

|   |                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * The stability of this configuration interface is classified as [Evolving](../release-notes/appendix-interface-stability.html).

* Any changes to the configuration require a server restart. |

To change the default OpenTelemetry configuration, add the configuration properties to your configuration file, for example:

```json
{
  "tracing": {
    "enabled": true,
    "resourceAttributes": {
      "service.instance.id": "idm-server-1"
    },
    "exporter": {
      "config": {
        "headers": {
          "X-CUSTOM-HEADER": "custom-value"
        }
      }
    },
    "spanLimits": {
      "maxNumberOfAttributesPerEvent": 128
    }
  }
}
```

> **Collapse: Distributed tracing configuration properties**
>
> * enabled: boolean, optional
>
>   Set to `true` to enable OpenTelemetry tracing.
>
>   Default: `false`
>
> * resourceAttributes: object, optional
>
>   A map of additional resource attributes for processing traces. Find more information in the OpenTelemetry documentation on [Semantic Attributes with SDK-provided Default Value](https://opentelemetry.io/docs/specs/semconv/resource/#semantic-attributes-with-sdk-provided-default-value).
>
>   For example, if there are multiple Ping Identity Platform instances in a deployment, you could set the `"service.instance.id"` resource attribute differently for each one to distinguish between them:
>
>   ```json
>   {
>     "resourceAttributes": {
>       "service.instance.id": "idm-server-1"
>     }
>   }
>   ```
>
> * exporter: object, optional
>
>   Configuration for the exporter, which pushes traces to the OpenTelemetry service:
>
>   * type: string, optional
>
>     Set to `otlp` for OpenTelemetry Protocol (OTLP) support. This is currently the only supported protocol.
>
>     Default: `otlp`
>
>   * config: object, optional
>
>     Endpoint and timeout configuration:
>
>     * `compressionMethod`: *enumeration, optional*
>
>       Method used to compress trace data; either `gzip` or `none`.
>
>       Default: `gzip`
>
>     * `connectionTimeout`: *duration, optional*
>
>       Time out a connection to the endpoint after this duration.
>
>       Default: 10 seconds.
>
>     * `endpoint`: *string, optional*
>
>       The endpoint to publish traces to.
>
>       For HTTPS, IDM trusts the default JVM CAs. To override this, set the `-Djavax.net.ssl.trustStore` and associated JVM settings when starting IDM. Learn more about the optional settings in the [Java Secure Socket Extension (JSSE) Reference Guide](https://docs.oracle.com/en/java/javase/21/security/java-secure-socket-extension-jsse-reference-guide.html).
>
>       |   |                                                                              |
>       | - | ---------------------------------------------------------------------------- |
>       |   | IDM doesn't support TLS configuration for the tracing endpoint at this time. |
>
>       Default: `http://localhost:4318/v1/traces`
>
>     * `headers`: *object, optional*
>
>       Map of additional headers to include in the export span request.
>
>       The following example sets the authorization header, `Authorization: Bearer ${bearer.token}`:
>
>       ```none
>       "headers": { "Authorization": "Bearer ${bearer.token}" }
>       ```
>
>     * `retries`: *object, optional*
>
>       Defines a retry policy for the export span requests.
>
>       Default: Enabled
>
>       * `backoffMultiplier`: *number, optional* Multiplier for the backoff wait time before retries.
>
>         Default: 1.5
>
>       * `enabled`: *boolean, optional*
>
>         Retry failed requests.
>
>         Default: `true`
>
>       * `initialBackoff`: *duration, optional*
>
>         How long to wait before the first retry.
>
>         Default: 1 second
>
>       * `maxAttempts`: *number, optional*
>
>         Maximum number of retries.
>
>         Default: 5
>
>       * `maxBackoff`: *duration, optional*
>
>         Maximum wait time between retries.
>
>         Default: 5 seconds
>
>     * `timeout`: *duration, optional*
>
>       Time out a request to publish data to the endpoint after this duration.
>
>       Default: 10 seconds.
>
>   * `batch`: *object, optional*
>
>     Enable and configure batch processing for trace data.
>
>     * `compressionMethod`: *enumeration, optional*
>
>       Method used to compress trace data; either `gzip` or `none`.
>
>       Default: `gzip`
>
>     * `enabled`: *boolean, optional*
>
>       Leave batch processing enabled in deployment.
>
>       Default: `true`
>
>     * `exporterTimeout`: *duration, optional*
>
>       Time out a data exporter after this duration.
>
>       Default: 30 seconds
>
>     * `exportUnsampledSpans`: *boolean, optional*
>
>       Whether to report on unsampled spans.
>
>       Default: `false`
>
>     * `maxExportBatchSize`: *number, optional*
>
>       Maximum number of spans in a batch.
>
>       Default: 512
>
>     * `maxQueueSize`: *number, optional*
>
>       Maximum number of spans to queue before dropping them.
>
>       Default: 2048
>
>     * `scheduleDelay`: *duration, optional*
>
>       Maximum interval between sending batches of trace data.
>
>       Default: 50 seconds
>
> * `sampler`: *object, optional*
>
>   Configuration for sampling spans.
>
>   * `ratio`: *number, optional*
>
>     For ratio-based types, a percentage of spans to process.
>
>     Default: 50 (percent)
>
>   * `type`: *string, optional*
>
>     The sampler strategy to use is one of the following:
>
>     * `alwaysOn`: Send every span for processing.
>
>     * `alwaysOff`: Never send any span for processing.
>
>     * `traceIdRatio`: Sample the specified ratio of spans deterministically based on the trace IDs of the spans.
>
>     * `parentBasedAlwaysOn`: Always send the span for processing if the parent span was sampled. (Default)
>
>     * `parentBasedAlwaysOff`: Never send the span for processing if the parent span was sampled.
>
>     * `parentBasedTraceIdRatio`: Send the specified ratio of spans for processing if the parent span was sampled.
>
> * `spanLimits`: *object, optional*
>
>   Configuration for limits enforced when recording spans.
>
>   * `maxNumberOfAttributes`: *number, optional*
>
>     The maximum number of attributes per span.
>
>     Default: 128
>
>   * `maxNumberOfAttributesPerEvent`: *number, optional*
>
>     The maximum number of metadata items (attributes) attached to a span per event. An event is an annotation to span at a particular, meaningful point in time during the span's duration.
>
>     Default: 128
>
>   * `maxNumberOfAttributesPerLink`: *number, optional*
>
>     The maximum number of attributes per link.
>
>     Default: 128
>
>   * `maxNumberOfEvents`: *number, optional*
>
>     The maximum number of events per span.
>
>     Default: 128
>
>   * `maxNumberOfLinks`: *number, optional*
>
>     The maximum number of links per span. Links associate the current span with one or more other spans.
>
>     Default: 128

## Visualize traces with a trace collector

Trace collectors work alongside IDM, allowing the service to offload data quickly. A collector manages retries, batching, encryption, and data filtering.

You can use a trace collector to collect trace data from the OpenTelemetry Collector and visualize that data.

### Example visualization with a trace collector

This example assumes a local IDM deployment.

1. Start the trace collector.

2. Send a request against IDM:

   ```bash
   curl --location 'http://localhost:8080/openidm/schema/managed/user' \
   --header 'x-openidm-username: openidm-admin' \
   --header 'x-openidm-password: openidm-admin'
   ```

3. Query the trace collector's localhost URL for the request:

   ```bash
    curl --location 'http://localhost:portnumber/api/traces?service=idm'
   ```

4. You should receive a query response similar to the following:

   ```json
   {
     "data": [
       {
         "traceID": "09cb4130f4c8803011b3996f8bda6b8c",
         "spans": [
           {
             "traceID": "09cb4130f4c8803011b3996f8bda6b8c",
             "spanID": "e49cd1d70d65502d",
             "operationName": "GET /openidm",
             "references": [],
             "startTime": 1741892475358333,
             "duration": 165774,
             "tags": [
               {
                 "key": "forgerock.transaction_id",
                 "type": "string",
                 "value": "c246e9ea-e596-4a99-a0eb-5072806cefe3-890"
               },
               {
                 "key": "http.request.method",
                 "type": "string",
                 "value": "GET"
               },
               {
                 "key": "network.protocol.name",
                 "type": "string",
                 "value": "http"
               },
               {
                 "key": "otel.scope.name",
                 "type": "string",
                 "value": "idm"
               },
               {
                 "key": "span.kind",
                 "type": "string",
                 "value": "server"
               },
               {
                 "key": "url.full",
                 "type": "string",
                 "value": "http://localhost:8080/openidm/schema/managed/user"
               },
               {
                 "key": "url.path",
                 "type": "string",
                 "value": "/openidm/schema/managed/user"
               }
             ],
             "logs": [],
             "processID": "p1",
             "warnings": null
           }
         ],
         ...
       }
     ]
   }
   ```

---

---
title: Load testing
description: Best practices for load testing PingIDM, including test planning with SLAs, resource usage, and execution principles
component: pingidm
version: 8.1
page_id: pingidm:monitoring-guide:load-testing
canonical_url: https://docs.pingidentity.com/pingidm/8.1/monitoring-guide/load-testing.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Monitoring", "Load Testing"]
section_ids:
  plan_tests: Plan tests
  understand_resource_usage: Understand resource usage
  execute_tests: Execute tests
  change-jvm-heap: Change the JVM heap size
---

# Load testing

Load testing can help you get the most out of IDM and other Ping products. The benefits load testing provides include:

* Reducing the chance that unexpected spikes in system activity will cause the system to become unstable

* Allowing developers and system administrators to reason more accurately and be more confident in release cycle timelines

* Providing baseline statistics which can be used to identify and investigate unexpected behavior

Load testing is a complex subject that requires knowledge of your system and a disciplined approach. There is no "one-size-fits-all" solution that applies in all circumstances. However, there are some basic principles to keep in mind while planning, executing, and evaluating load tests.

## Plan tests

The first step is to determine what metrics need to be examined, what components are going to be tested, what levels of load are going to be used, and what response ranges are acceptable. Answering these questions requires:

* Service-level Agreements (SLAs)

* Understanding of your use case

* Baseline knowledge of your system

SLAs provide a stationary, business-based target to aim for in testing. An example SLA appears as follows:

| Service/Endpoint                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Sustained load       | Peak load                                        | Required response time |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------ | ---------------------- |
| Customer auth against LDAP repo                                                                                                                                                                                                                                                                                                                                                                                                                                            | 50,000 over 16 hours | 4,000 per second three times in a 16-hour period | 200ms                  |
| Employee auth against AD repo                                                                                                                                                                                                                                                                                                                                                                                                                                              | 4,000 over 10 hours  | 100/second                                       | 400ms                  |
| Customer registration                                                                                                                                                                                                                                                                                                                                                                                                                                                      | 1,000 over 24 hours  | 10/second                                        | 500ms                  |
| Employee password reset                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 10 over 24 hours     | 1/second                                         | 500ms                  |
| **Sample SLA warnings and details:**- Response times are between load generator and Ping platform and do not account for latency between client devices and architecture.

- IDM must support four writes and 45 read transactions per second for 12 hours using DS as the repository.

- IDM must support 2,000 changes from HR service.

- Measuring response times occurs after establishing 10,000 active, concurrent stateful sessions with 10,000 unique identities. |                      |                                                  |                        |

Details will vary depending on your use case and application flow, present usage patterns, full load profile, and environment. To get the most benefit, collect this information.

The system's full load profile depends on how it is designed and used. For example, some systems have thousands of clients each using a small slice of bandwidth, while others have only a few high-bandwidth connections. Understanding these nuances helps determine an appropriate number of connections and threads of execution to use to generate a test load.

|   |                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you have trouble determining which systems and components are being used at various points during your application flow, consider modeling your application using a sequence diagram. |

## Understand resource usage

Understanding what resources are heavily consumed by Ping products will help you with your test planning. The following chart details some products and their consumed resources:

| Product                                                                                                                 | Consumed resources                                                   |
| ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| AM with external stores                                                                                                 | CPU, memory                                                          |
| DS as a user repository                                                                                                 | I/O, memory                                                          |
| DS as a token store                                                                                                     | I/O, memory (if high token count)                                    |
| IDM                                                                                                                     | I/O, CPU, and memory play an important role in provisioning and sync |
| PingGateway                                                                                                             | CPU                                                                  |
| **All of the above depends on network performance, including name resolution and proper load balancing when required.** |                                                                      |

## Execute tests

When it comes to executing tests, these are the basic principles to keep in mind:

1. Every system is different; "it depends" is the cardinal rule.

2. Testing scenarios that don't happen in reality gives you test results that don't happen in reality.

3. System performance is constrained by the scarcest resource.

One way to ensure that your tests reflect real use patterns is to begin with a load generator that creates periods of consistent use and periods of random spikes in activity. During the consistent periods, gradually add load until you exceed your SLAs and baselines. By using that data and the data from the periods of spiking activity, you can determine how your system handles spikes in activity in many different scenarios.

|   |                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Your load generator should be located on separate hardware/instances from your production systems. It should have adequate resources to generate the expected load. |

When testing systems with many components, begin by testing the most basic things — I/O, CPU, and memory use. IDM provides insight into these by exposing [JVM Metrics](api-metrics.html#api-jvm-metric-names).

Once you have an understanding of the basic elements of your system, introduce new components into the tests. Keep a record of each test's environment and the components which were under test. These components may include:

* Hardware/Hypervisor/Container platform

* Hosting OS/VM/Container environment

* Hosted OS

* Java Virtual Machine (JVM)

* Web/J2EE Container (if used to host PingAM/PingGateway or PingAM Agent)

* Databases, repositories, and directory servers used with Ping

* Networking, load balancers, and firewalls between instances

* SSL, termination points, and other communications

* Points of integration, if any

* Other applications and services that utilize Ping components

* Load generation configuration

* Sample data, logs from test runs, and other generated files

|   |                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | While there are many tools that can help you monitor your system, a thorough understanding of your system logs is the best path to understanding its behavior. |

|   |                                                                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | To keep your results clear and focused, only add or adjust one variable at a time.Do not run tests designed to stress the system to its theoretical limit. The results you get from these stress tests rarely provide actionable insights. |

## Change the JVM heap size

Changing the JVM heap size can improve performance and reduce the time it takes to run reconciliations.

You can set the JVM heap size via the `OPENIDM_OPTS` environment variable. If `OPENIDM_OPTS` is undefined, the JVM maximum heap size defaults to 2GB. For example, to set the minimum and maximum heap sizes to 4GB, enter the following before starting IDM:

* Unix/Linux

* Windows

```
cd /path/to/openidm/
export OPENIDM_OPTS="-Xms4096m -Xmx4096m"
./startup.sh
Using OPENIDM_HOME:   /path/to/openidm
Using PROJECT_HOME:   /path/to/openidm
Using OPENIDM_OPTS:   -Xms4096m -Xmx4096m
...
OpenIDM ready
```

```
cd \path\to\openidm
set OPENIDM_OPTS=-Xms4096m -Xmx4096m
startup.bat
"Using OPENIDM_HOME:   \path\to\openidm"
"Using PROJECT_HOME:   \path\to\openidm"
"Using OPENIDM_OPTS:   -Xms4096m -Xmx4096m -Dfile.encoding=UTF-8"
...
OpenIDM ready
```

You can also edit the `OPENIDM_OPTS` values in `startup.sh` or `startup.bat`.

---

---
title: Metrics reference
description: "Reference for PingIDM metric types: timer, summary, gauge, and counter with examples from the /api and /prometheus endpoints"
component: pingidm
version: 8.1
page_id: pingidm:monitoring-guide:metrics
canonical_url: https://docs.pingidentity.com/pingidm/8.1/monitoring-guide/metrics.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Monitoring"]
section_ids:
  metric_types: Metric types
  timer: Timer
  summary: Summary
  gauge: Gauge
  counter: Counter
---

# Metrics reference

IDM exposes a number of metrics. All metrics are available at both the `openidm/metrics/api` and `openidm/metrics/prometheus` endpoints. The actual metric names can vary, depending on the endpoint used. Also refer to [Monitoring](monitoring.html).

|   |                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | IDM generates metrics only after a corresponding event occurs. For example, IDM doesn't create login-related metrics until a user logs in. If you're using a monitoring tool like Grafana, this may appear as missing data or empty panels on your dashboard. |

## Metric types

Metrics are organized into the following *types*:

### Timer

Timers provide a histogram of the duration of an event, along with a measure of the rate of occurrences. Timers can be monitored using the Dropwizard dashboard widget and the IDM Prometheus endpoint. Durations in timers are measured in milliseconds. Rates are reported in number of calls per second. The following example shows a timer metric:

```json
{
   "_id": "sync.source.perform-action",
   "count": 2,
   "max": 371.53391,
   "mean": 370.1752705,
   "min": 368.816631,
   "p50": 371.53391,
   "p75": 371.53391,
   "p95": 371.53391,
   "p98": 371.53391,
   "p99": 371.53391,
   "p999": 371.53391,
   "stddev": 1.3586395,
   "m15_rate": 0.393388581528647,
   "m1_rate": 0.311520313228562,
   "m5_rate": 0.3804917698002856,
   "mean_rate": 0.08572717156016606,
   "duration_units": "milliseconds",
   "rate_units": "calls/second",
   "total": 740.350541,
   "_type": "timer"
 }
```

### Summary

Summaries are similar to timers in that they measure a distribution of events. However, summaries record values that aren't units of time, such as user login counts. Summaries cannot be graphed in the Dropwizard dashboard widget, but are available through the Prometheus endpoint, and by querying the `openidm/metrics/api` endpoint directly. The following example shows a summary metric:

```json
{
  "_id": "audit.recon",
  "m15_rate": 0.786777163057294,
  "m1_rate": 0.623040626457124,
  "m5_rate": 0.7609835396005712,
  "mean_rate": 0.16977218861919927,
  "units": "events/second",
  "total": 4,
  "count": 4,
  "_type": "summary"
}
```

### Gauge

Gauge metrics return a numerical value that can increase or decrease. The value for a gauge is calculated on request, and represents the state of the metric at that specific time. The following example shows a gauge metric:

```json
{
  "_id": "jvm.used-memory",
  "value": 2147483648,
  "_type": "gauge"
}
```

### Counter

Counter metrics are cumulative numerical values that can only increase or reset to zero on restart. The value for a counter metric is calculated on request. The following example shows a counter metric:

```json
{
  "_id": "jvm.class-loading.loaded.total",
  "count": 22757,
  "_type": "counter"
}
```

---

---
title: Monitoring
description: Enable and configure PingIDM metrics collection using the Prometheus endpoint, Dropwizard widget, and Grafana dashboard
component: pingidm
version: 8.1
page_id: pingidm:monitoring-guide:monitoring
canonical_url: https://docs.pingidentity.com/pingidm/8.1/monitoring-guide/monitoring.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Monitoring", "JSON"]
section_ids:
  enable-metrics: Enable metrics
  deprecated-metric-collection: Deprecated metric collection
  dropwizard: Dropwizard widget
  prometheus: Prometheus endpoint
  disable_prometheus: Disable Prometheus
  configure-prometheus: Configure Prometheus
  configure-grafana: Configure Grafana
  create_a_grafana_dashboard: Create a Grafana dashboard
---

# Monitoring

IDM includes the following tools for monitoring metrics:

* A Dropwizard dashboard widget, for viewing metrics within IDM.

  |   |                                                                                                                                                                                          |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Widgets are deprecated and will be removed in a future release of IDM. For more information, refer to [Deprecation](../release-notes/deprecated-functionality.html#deprecation-widgets). |

* A Prometheus endpoint, for viewing metrics through external resources such as Prometheus and Grafana.

## Enable metrics

IDM does not collect metrics by default. To enable metrics collection, open `conf/metrics.json` and set the `enabled` property to `true`:

```json
{
    "enabled" : true
}
```

After you have enabled metrics, the following command returns all collected metrics:

Request

```
curl \
--header "X-OpenIDM-Username: openidm-admin" \
--header "X-OpenIDM-Password: openidm-admin" \
--header "Accept-API-Version: resource=1.0" \
--request GET \
'http://localhost:8080/openidm/metrics/api?_queryFilter=true'
```

> **Collapse: Show example response**
>
> Response
>
> ```json
> {
>   "result": [
>     {
>       "_id": "repo.ds.get-connection",
>       "count": 5,
>       "max": 0.033023,
>       "mean": 0.01632066766586218,
>       "min": 0.006605,
>       "p50": 0.007868,
>       "p75": 0.026865999999999998,
>       "p95": 0.033023,
>       "p98": 0.033023,
>       "p99": 0.033023,
>       "p999": 0.033023,
>       "stddev": 0.011254712526201813,
>       "m15_rate": 0.0,
>       "m1_rate": 0.0,
>       "m5_rate": 0.0,
>       "mean_rate": 1.5494157682573269,
>       "duration_units": "milliseconds",
>       "rate_units": "calls/second",
>       "total": 0.081915,
>       "_type": "timer"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.G1-Old-Gen.committed",
>       "value": 794820608,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.max-memory",
>       "value": 2147483648,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.CodeHeap-'non-profiled-nmethods'.init",
>       "value": 2555904.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.G1-Old-Gen.init",
>       "value": 2.03423744E+9,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.init_G1-Survivor-Space",
>       "value": 0.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.total.max",
>       "value": 2147483647,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.total.committed",
>       "value": 2359099392,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.heap.init",
>       "value": 2147483648,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.init_heap",
>       "value": 2147483648,
>       "_type": "gauge"
>     },
>     {
>       "_id": "repo.ds.update.cluster",
>       "count": 1,
>       "max": 5.685331,
>       "mean": 5.685331,
>       "min": 5.685331,
>       "p50": 5.685331,
>       "p75": 5.685331,
>       "p95": 5.685331,
>       "p98": 5.685331,
>       "p99": 5.685331,
>       "p999": 5.685331,
>       "stddev": 0.0,
>       "m15_rate": 0.0,
>       "m1_rate": 0.0,
>       "m5_rate": 0.0,
>       "mean_rate": 0.548450244910786,
>       "duration_units": "milliseconds",
>       "rate_units": "calls/second",
>       "total": 5.685331,
>       "_type": "timer"
>     },
>     {
>       "_id": "jvm.thread-state_blocked",
>       "value": 0.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "repo.ds.read.cluster",
>       "count": 1,
>       "max": 2.404851,
>       "mean": 2.404851,
>       "min": 2.404851,
>       "p50": 2.404851,
>       "p75": 2.404851,
>       "p95": 2.404851,
>       "p98": 2.404851,
>       "p99": 2.404851,
>       "p999": 2.404851,
>       "stddev": 0.0,
>       "m15_rate": 0.0,
>       "m1_rate": 0.0,
>       "m5_rate": 0.0,
>       "mean_rate": 0.5469820381458513,
>       "duration_units": "milliseconds",
>       "rate_units": "calls/second",
>       "total": 2.404851,
>       "_type": "timer"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.max_G1-Eden-Space",
>       "value": -1.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.free-memory",
>       "value": 1147588736,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.CodeHeap-'non-nmethods'.usage",
>       "value": 0.3304220516962843,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.init_non-heap",
>       "value": 7667712.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.used_G1-Old-Gen",
>       "value": 118043136,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.used_CodeHeap-'non-nmethods'",
>       "value": 2513280.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.Metaspace.init",
>       "value": 0.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.class-loading.unloaded.total",
>       "count": 1,
>       "_type": "counter"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.committed_Metaspace",
>       "value": 145227776,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.G1-Survivor-Space.committed",
>       "value": 75497472,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.heap.usage",
>       "value": 0.46512436866760254,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.init_G1-Eden-Space",
>       "value": 113246208,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.garbage-collector.G1-Old-Generation.count",
>       "value": 0.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.thread-state.waiting.count",
>       "value": 54.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.used_CodeHeap-'profiled-nmethods'",
>       "value": 30778496,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.class-loading.loaded",
>       "value": 22757.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.available-cpus",
>       "value": 16.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.max_G1-Old-Gen",
>       "value": 2147483648,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.max_Metaspace",
>       "value": -1.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.CodeHeap-'non-profiled-nmethods'.committed",
>       "value": 11730944,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.used-memory",
>       "value": 2147483648,
>       "_type": "gauge"
>     },
>     {
>       "_id": "scheduler.job-store.repo.query-list.triggers",
>       "count": 1,
>       "max": 3.064977,
>       "mean": 3.064977,
>       "min": 3.064977,
>       "p50": 3.064977,
>       "p75": 3.064977,
>       "p95": 3.064977,
>       "p98": 3.064977,
>       "p99": 3.064977,
>       "p999": 3.064977,
>       "stddev": 0.0,
>       "m15_rate": 0.0,
>       "m1_rate": 0.0,
>       "m5_rate": 0.0,
>       "mean_rate": 0.30915432245454577,
>       "duration_units": "milliseconds",
>       "rate_units": "calls/second",
>       "total": 3.064977,
>       "_type": "timer"
>     },
>     {
>       "_id": "jvm.memory-usage.total.init",
>       "value": 2.15515136E+9,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.CodeHeap-'non-nmethods'.used",
>       "value": 2513280.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.G1-Eden-Space.init",
>       "value": 113246208,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.Metaspace.usage",
>       "value": 0.9798155967078914,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.G1-Eden-Space.max",
>       "value": -1.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.init_Compressed-Class-Space",
>       "value": 0.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.G1-Old-Gen.max",
>       "value": 2147483648,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.init_CodeHeap-'profiled-nmethods'",
>       "value": 2555904.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.total.used",
>       "value": 1202003416,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.used_Compressed-Class-Space",
>       "value": 1.63824E+7,
>       "_type": "gauge"
>     },
>     {
>       "_id": "authorization-check.full-check",
>       "count": 1,
>       "max": 1.8842489999999998,
>       "mean": 1.8842489999999998,
>       "min": 1.8842489999999998,
>       "p50": 1.8842489999999998,
>       "p75": 1.8842489999999998,
>       "p95": 1.8842489999999998,
>       "p98": 1.8842489999999998,
>       "p99": 1.8842489999999998,
>       "p999": 1.8842489999999998,
>       "stddev": 0.0,
>       "m15_rate": 0.0,
>       "m1_rate": 0.0,
>       "m5_rate": 0.0,
>       "mean_rate": 82.67584677222334,
>       "duration_units": "milliseconds",
>       "rate_units": "calls/second",
>       "total": 1.884249,
>       "_type": "timer"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.committed_G1-Eden-Space",
>       "value": 1277165568,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.used_Metaspace",
>       "value": 142296984,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.CodeHeap-'profiled-nmethods'.used",
>       "value": 30785408,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.G1-Survivor-Space.init",
>       "value": 0.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.non-heap.max",
>       "value": -1.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.G1-Survivor-Space.max",
>       "value": -1.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.CodeHeap-'profiled-nmethods'.max",
>       "value": 122023936,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.thread-state.daemon.count",
>       "value": 66.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.G1-Eden-Space.used-after-gc",
>       "value": 0.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.thread-state.new.count",
>       "value": 0.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.max_G1-Survivor-Space",
>       "value": -1.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "repo.ds.query._adhoc-filter.cluster",
>       "count": 2,
>       "max": 2.625038,
>       "mean": 2.2533855,
>       "min": 1.8817329999999999,
>       "p50": 2.625038,
>       "p75": 2.625038,
>       "p95": 2.625038,
>       "p98": 2.625038,
>       "p99": 2.625038,
>       "p999": 2.625038,
>       "stddev": 0.3716525,
>       "m15_rate": 0.0,
>       "m1_rate": 0.0,
>       "m5_rate": 0.0,
>       "mean_rate": 1.096972198056336,
>       "duration_units": "milliseconds",
>       "rate_units": "calls/second",
>       "total": 4.506771,
>       "_type": "timer"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.G1-Eden-Space.used",
>       "value": 805306368,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.garbage-collector.G1-Young-Generation.time",
>       "value": 238.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.CodeHeap-'non-profiled-nmethods'.max",
>       "value": 122028032,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.heap.used",
>       "value": 998846976,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.max_Compressed-Class-Space",
>       "value": 1073741824,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.class-loading.unloaded",
>       "value": 1.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.init_CodeHeap-'non-profiled-nmethods'",
>       "value": 2555904.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.G1-Eden-Space.committed",
>       "value": 1277165568,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.used-after-gc_G1-Eden-Space",
>       "value": 0.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.max_CodeHeap-'non-nmethods'",
>       "value": 7606272.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.class-loading.loaded.total",
>       "count": 22757,
>       "_type": "counter"
>     },
>     {
>       "_id": "jvm.memory-usage.heap.max",
>       "value": 2147483648,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.init_G1-Old-Gen",
>       "value": 2.03423744E+9,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.Metaspace.used",
>       "value": 142301024,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.non-heap.used",
>       "value": 203165728,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.thread-state_new",
>       "value": 0.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "user.session.static-user",
>       "m15_rate": 0.0,
>       "m1_rate": 0.0,
>       "m5_rate": 0.0,
>       "mean_rate": 66.81303621219794,
>       "units": "events/second",
>       "total": 1.0,
>       "count": 1,
>       "_type": "summary"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.Compressed-Class-Space.usage",
>       "value": 0.015257298946380615,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.used_non-heap",
>       "value": 203165952,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.committed_G1-Old-Gen",
>       "value": 794820608,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.non-heap.usage",
>       "value": 0.9597728811919505,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.thread-state_waiting",
>       "value": 54.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.init_CodeHeap-'non-nmethods'",
>       "value": 2555904.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.CodeHeap-'profiled-nmethods'.init",
>       "value": 2555904.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.committed_CodeHeap-'non-nmethods'",
>       "value": 4390912.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.max_CodeHeap-'profiled-nmethods'",
>       "value": 122023936,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.Compressed-Class-Space.init",
>       "value": 0.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.thread-state_runnable",
>       "value": 67.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.G1-Old-Gen.used",
>       "value": 118043136,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.thread-state.timed_waiting.count",
>       "value": 39.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.G1-Old-Gen.usage",
>       "value": 0.05496811866760254,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.garbage-collector.time.total_G1-Young-Generation",
>       "count": 238,
>       "_type": "counter"
>     },
>     {
>       "_id": "jvm.thread-state_terminated",
>       "value": 0.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.CodeHeap-'non-profiled-nmethods'.usage",
>       "value": 0.09162589789205156,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.max_non-heap",
>       "value": -1.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.garbage-collector.G1-Young-Generation.count",
>       "value": 16.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.thread-state.terminated.count",
>       "value": 0.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.garbage-collector.G1-Old-Generation.time",
>       "value": 0.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.heap.committed",
>       "value": 2147483648,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.garbage-collector.time.total_G1-Old-Generation",
>       "count": 0,
>       "_type": "counter"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.Metaspace.committed",
>       "value": 145293312,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.init_Metaspace",
>       "value": 0.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.CodeHeap-'non-nmethods'.committed",
>       "value": 4390912.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.non-heap.committed",
>       "value": 2.1168128E+8,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.max_heap",
>       "value": 2147483648,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.G1-Survivor-Space.usage",
>       "value": 1.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.thread-state_timed_waiting",
>       "value": 39.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.committed_heap",
>       "value": 2147483648,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.committed_non-heap",
>       "value": 2.1168128E+8,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.max_CodeHeap-'non-profiled-nmethods'",
>       "value": 122028032,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.committed_G1-Survivor-Space",
>       "value": 75497472,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.thread-state.blocked.count",
>       "value": 0.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.used_heap",
>       "value": 998846976,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.garbage-collector.count.total_G1-Old-Generation",
>       "count": 0,
>       "_type": "counter"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.used_G1-Survivor-Space",
>       "value": 75497472,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.G1-Survivor-Space.used-after-gc",
>       "value": 6630416.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "authorization-check.router-authz",
>       "count": 1,
>       "max": 1.7509839999999999,
>       "mean": 1.7509839999999999,
>       "min": 1.7509839999999999,
>       "p50": 1.7509839999999999,
>       "p75": 1.7509839999999999,
>       "p95": 1.7509839999999999,
>       "p98": 1.7509839999999999,
>       "p99": 1.7509839999999999,
>       "p999": 1.7509839999999999,
>       "stddev": 0.0,
>       "m15_rate": 0.0,
>       "m1_rate": 0.0,
>       "m5_rate": 0.0,
>       "mean_rate": 61.599943968690965,
>       "duration_units": "milliseconds",
>       "rate_units": "calls/second",
>       "total": 1.750984,
>       "_type": "timer"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.committed_Compressed-Class-Space",
>       "value": 17629184,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.G1-Eden-Space.usage",
>       "value": 0.6305418719211823,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.CodeHeap-'non-profiled-nmethods'.used",
>       "value": 11180928,
>       "_type": "gauge"
>     },
>     {
>       "_id": "repo.ds.query._adhoc-filter.scheduler",
>       "count": 1,
>       "max": 2.687975,
>       "mean": 2.687975,
>       "min": 2.687975,
>       "p50": 2.687975,
>       "p75": 2.687975,
>       "p95": 2.687975,
>       "p98": 2.687975,
>       "p99": 2.687975,
>       "p999": 2.687975,
>       "stddev": 0.0,
>       "m15_rate": 0.0,
>       "m1_rate": 0.0,
>       "m5_rate": 0.0,
>       "mean_rate": 0.3087729850177765,
>       "duration_units": "milliseconds",
>       "rate_units": "calls/second",
>       "total": 2.687975,
>       "_type": "timer"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.committed_CodeHeap-'profiled-nmethods'",
>       "value": 32636928,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.used_CodeHeap-'non-profiled-nmethods'",
>       "value": 11180928,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.garbage-collector.count.total_G1-Young-Generation",
>       "count": 16,
>       "_type": "counter"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.G1-Survivor-Space.used",
>       "value": 75497472,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.committed_CodeHeap-'non-profiled-nmethods'",
>       "value": 11730944,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.used_G1-Eden-Space",
>       "value": 805306368,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.thread-state.daemon",
>       "value": 66.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.Compressed-Class-Space.committed",
>       "value": 17629184,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.thread-state.count",
>       "value": 160.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.CodeHeap-'non-nmethods'.init",
>       "value": 2555904.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "audit.authentication",
>       "m15_rate": 0.0,
>       "m1_rate": 0.0,
>       "m5_rate": 0.0,
>       "mean_rate": 57.05540262171857,
>       "units": "events/second",
>       "total": 1.0,
>       "count": 1,
>       "_type": "summary"
>     },
>     {
>       "_id": "jvm.memory-usage.non-heap.init",
>       "value": 7667712.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.thread-state.runnable.count",
>       "value": 67.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.CodeHeap-'profiled-nmethods'.committed",
>       "value": 32636928,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.Metaspace.max",
>       "value": -1.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.used-after-gc_G1-Old-Gen",
>       "value": 0.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.used-after-gc_G1-Survivor-Space",
>       "value": 6630416.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.G1-Old-Gen.used-after-gc",
>       "value": 0.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.Compressed-Class-Space.max",
>       "value": 1073741824,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.CodeHeap-'non-nmethods'.max",
>       "value": 7606272.0,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.CodeHeap-'profiled-nmethods'.usage",
>       "value": 0.252550057064214,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.memory-usage.pools.Compressed-Class-Space.used",
>       "value": 1.63824E+7,
>       "_type": "gauge"
>     },
>     {
>       "_id": "jvm.free-used-memory",
>       "value": 1146838232,
>       "_type": "gauge"
>     }
>   ],
>   "resultCount": 142,
>   "pagedResultsCookie": null,
>   "totalPagedResultsPolicy": "EXACT",
>   "totalPagedResults": 142,
>   "remainingPagedResults": -1
> }
> ```
>
> |   |                                                                                                                                         |
> | - | --------------------------------------------------------------------------------------------------------------------------------------- |
> |   | Some metrics in the sample response are [deprecated](../release-notes/deprecated-functionality.html#deprecation-jvm-mem-usage-metrics). |

|   |                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | IDM generates metrics only after a corresponding event occurs. For example, IDM doesn't create login-related metrics until a user logs in. If you're using a monitoring tool like Grafana, this may appear as missing data or empty panels on your dashboard. |

Learn more:

* [Metrics reference](metrics.html)

* [Load testing](load-testing.html)

## Deprecated metric collection

Deprecated metric names are still available until they're removed in a future release and generated only when the `deprecatedMetricsEnabled` property is set to `true` (default) in `conf/metrics.json`. The default preserves backward compatibility for existing dashboards and alerts.

To generate only the replacement metric names, set the property to `false`:

```json
{
    "enabled" : true,
    "deprecatedMetricsEnabled" : false
}
```

For example, if the property is set to `true`, both metric names are generated:

* `managed.managed-object.script.script-name` ([API deprecated metric](../release-notes/changed-functionality.html#managed-object-script-name-dep))

* `managed-script-hook.object.script-hook` ([API replacement metric](api-metrics.html#changed-managed-object-script-hook-metric))

* `idm_managed_seconds{managed_object="managed_object",operation="operation_name",script="script_name"}` ([Prometheus deprecated metric](../release-notes/changed-functionality.html#managed-seconds-managed-object-dep))

* `idm_managed_script_hook_seconds{object="object",script_hook="script_hook"}` ([Prometheus replacement metric](prometheus-metrics.html#changed-managed-object-script-hook-metric-prom))

## Dropwizard widget

|   |                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Widgets are deprecated and will be removed in a future release of IDM. For more information, refer to [Deprecation](../release-notes/deprecated-functionality.html#deprecation-widgets). |

The Dropwizard widget creates a graph of metrics based on server activity and is useful for lightweight, live monitoring of IDM. The widget has the following limitations:

* The graph created by the widget does not persist. If you reload or navigate away from the page, the graph restarts.

* The widget only works with time-based metrics.

To add the Dropwizard widget:

1. From the navigation bar, click Dashboards > Dashboard Name.

2. On the Dashboard Name page, click Add Widget.

3. In the Add Widget window, from the Select a Widget drop-down list, select Dropwizard Table with Graph.

   ![Add widget window with dropwizard selected](_images/add-widget-window-dropwizard.png)

4. To preview any metric on the graph, click Add to Graph adjacent to any metric.

5. Click Add.

   The Dropwizard widget now displays on the dashboard.

## Prometheus endpoint

This topic describes how to configure Prometheus and Grafana to collect IDM metrics. These third-party tools are *not* supported by Ping. Refer to the [Prometheus documentation](https://prometheus.io/docs/introduction/overview/).

Prometheus is a third-party tool used for gathering and processing monitoring data. Prometheus uses the `openidm/metrics/prometheus` endpoint to gather information. This endpoint is protected by a basic authentication filter, using the following credentials, set in the `resolver/boot.properties` file:

```properties
openidm.prometheus.username=username
openidm.prometheus.password=password
```

|   |                                                                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Storing secrets and passwords directly in configuration and property files is [deprecated](../release-notes/deprecated-functionality.html#deprecation-secrets-in-config). The Prometheus endpoint supports [Secret stores](../security-guide/secret-stores.html) for secret resolution. |

### Disable Prometheus

To disable IDM's Prometheus handler:

1. Comment out or remove `openidm.prometheus.username` and `openidm.prometheus.password` from the `resolver/boot.properties` file.

2. Remove or don't define the `idm.prometheus.credentials` purpose.

   If these properties and purpose aren't set, IDM doesn't enable the Prometheus handler.

### Configure Prometheus

1. Download [Prometheus](https://prometheus.io/).

2. Create a `prometheus.yml` configuration file. For more information, refer to the [Prometheus configuration documentation](https://prometheus.io/docs/prometheus/latest/configuration/configuration/). An example `prometheus.yml` file:

   ```yaml
   global:
     scrape_interval: 15s
     external_labels:
       monitor: 'my_prometheus'

   # https://prometheus.io/docs/operating/configuration/#scrape_config
   scrape_configs:
     - job_name: 'openidm'
       scrape_interval: 15s
       scrape_timeout: 5s
       metrics_path: 'openidm/metrics/prometheus'
       scheme: http
       basic_auth:
         username: 'prometheus'
         password: 'prometheus'
       static_configs:
         - targets: ['localhost:8080']
   ```

   This example configures Prometheus to poll the `openidm/metrics/prometheus` endpoint every 5 seconds (`scrape_interval: 5s`), receiving metrics in a plain text format (`_fields: ['text']` and `_mimeType: ['text/plain;version=0.0.4']`). For more information about reporting formats, refer to the Prometheus documentation on [Exposition Formats](https://prometheus.io/docs/instrumenting/exposition_formats/).

3. Verify the configuration returns metric results:

   Request

   ```console
   curl \
   --user prometheus:prometheus \
   --header "Accept-API-Version: resource=1.0" \
   --request GET \
   'http://localhost:8080/openidm/metrics/prometheus'
   ```

   > **Collapse: Show example response**
   >
   > Response
   >
   > ```console
   > # HELP idm_jvm_available_cpus Automatically generated
   > # TYPE idm_jvm_available_cpus gauge
   > idm_jvm_available_cpus 10.0
   > # HELP idm_jvm_class_loading_loaded Automatically generated
   > # TYPE idm_jvm_class_loading_loaded gauge
   > idm_jvm_class_loading_loaded 24876.0
   > # HELP idm_jvm_class_loading_unloaded Automatically generated
   > # TYPE idm_jvm_class_loading_unloaded gauge
   > idm_jvm_class_loading_unloaded 1.0
   > # HELP idm_jvm_free_used_memory_bytes Automatically generated
   > # TYPE idm_jvm_free_used_memory_bytes gauge
   > idm_jvm_free_used_memory_bytes 9.77543264E8
   > # HELP idm_jvm_garbage_collector_g1_old_generation_count Automatically generated
   > # TYPE idm_jvm_garbage_collector_g1_old_generation_count gauge
   > idm_jvm_garbage_collector_g1_old_generation_count 0.0
   > # HELP idm_jvm_garbage_collector_g1_old_generation_time Automatically generated
   > # TYPE idm_jvm_garbage_collector_g1_old_generation_time gauge
   > idm_jvm_garbage_collector_g1_old_generation_time 0.0
   > # HELP idm_jvm_garbage_collector_g1_young_generation_count Automatically generated
   > # TYPE idm_jvm_garbage_collector_g1_young_generation_count gauge
   > idm_jvm_garbage_collector_g1_young_generation_count 82.0
   > # HELP idm_jvm_garbage_collector_g1_young_generation_time Automatically generated
   > # TYPE idm_jvm_garbage_collector_g1_young_generation_time gauge
   > idm_jvm_garbage_collector_g1_young_generation_time 2127.0
   > # HELP idm_jvm_max_memory_bytes Automatically generated
   > # TYPE idm_jvm_max_memory_bytes gauge
   > idm_jvm_max_memory_bytes 2.147483648E9
   > ...
   > ```

4. Start Prometheus with the `prometheus.yml` configuration file:

   ```console
   prometheus --config.file=/path/to/prometheus.yml
   ```

5. To confirm that Prometheus is gathering data from IDM, go to the Prometheus monitoring page (default `http://localhost:9090`).

   ![prometheus main page](_images/prometheus-main-page.png)

You can store your Prometheus credentials in the `idm.prometheus.credentials` well-defined purpose. This can allow for zero-downtime credentials rotation. For more information, refer to [Store Prometheus credentials as a secret](../security-guide/secret-stores.html#secret-rotation-prometheus).

### Configure Grafana

|   |                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | IDM generates metrics only after a corresponding event occurs. For example, IDM doesn't create login-related metrics until a user logs in. If you're using a monitoring tool like Grafana, this may appear as missing data or empty panels on your dashboard. |

Prometheus lets you monitor and process information provided by IDM. If you need deeper analytics, you can use tools such as Grafana to create customized charts and graphs based on Prometheus data. For information on installing and running Grafana, refer to the [Grafana website](https://grafana.com).

You can also monitor aspects of IDM's performance using Prometheus to plug JVM metrics into a Grafana dashboard. For more information on using metrics to observe the system under load, refer to [Load testing](load-testing.html).

|   |                                                                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Before you get started, download the *Monitoring Dashboard Samples* from the [Backstage download site](https://backstage.forgerock.com/downloads). Open `monitoring.dashboard.json` from the downloaded .zip file, as you'll need it during the following procedure. |

To set up a Grafana dashboard with IDM metrics using Prometheus:

1. In a browser, go to the main Grafana page (default `http://localhost:3000`) and log in.

   |   |                                                           |
   | - | --------------------------------------------------------- |
   |   | The default username and password for Grafana is `admin`. |

2. To add your Prometheus installation to Grafana as a data source, click the toggle menu button ![grafana toggle menu](_images/grafana-toggle-menu.svg), and click Connections > Data sources.

3. On the Data sources page, click Add data source.

4. On the Add data source page, select Prometheus.

   ![grafana add prometheus source](_images/grafana-add-prometheus-source.png)

5. Enter information and select options, as needed. The information you enter here should match the settings in the `monitoring.dashboard.json` file:

   1. Give your data source a name; for example, `PingIDM`.

   2. Set the URL (default `http://localhost:9090`).

   3. Enable Basic auth.

      1. Enter the User (default `prometheus`).

      2. Enter the Password (default `prometheus`).

6. Click Save & test.

   If the test succeeds, Grafana displays Data source is working.

### Create a Grafana dashboard

After Prometheus has been configured as a data source in Grafana, you can create a dashboard with IDM metrics:

1. In Grafana, click the toggle menu button ![grafana toggle menu](_images/grafana-toggle-menu.svg), and click Dashboards.

2. Click New, and do one of the following:

   * Select Import.

     1. On the Import dashboard page, drag the `monitoring.dashboard.json` file from its location on your system to the Upload dashboard JSON file area.

     2. Enter information in the Options area, and select the Prometheus data source you previously created.

     3. Click Import.

   * Select New dashboard.

     1. Click Add visualization.

     2. Select the Prometheus data source you previously created.

     3. Configure the panel.

        |   |                                                                                                                                                                                                                                              |
        | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        |   | For more information, refer to:- [Prometheus query language](https://prometheus.io/docs/prometheus/latest/querying/basics/)

        - [Panel editor overview](https://grafana.com/docs/grafana/latest/panels-visualizations/panel-editor-overview/) |

---

---
title: Monitoring and metrics
description: Guide to configuring PingIDM server logs and monitoring metrics
component: pingidm
version: 8.1
page_id: pingidm:monitoring-guide:preface
canonical_url: https://docs.pingidentity.com/pingidm/8.1/monitoring-guide/preface.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Monitoring", "Logs", "REST API"]
page_aliases: ["index.adoc"]
---

# Monitoring and metrics

> Configure PingIDM server logs and monitoring metrics.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Starting with IDM 8.1, the [legacy admin UI is deprecated](../release-notes/deprecated-functionality.html#legacy-admin-ui-deprecated) and is no longer bundled with IDM. New deployments should use the [Platform admin UI](../setup-guide/platform-admin-ui.html), which is the replacement for the legacy admin UI.Both UIs are available as separate downloads from the [Backstage download site](https://backstage.forgerock.com/downloads):- To install the Platform admin UI, follow the steps in [Install the Platform admin UI for standalone IDM](../setup-guide/platform-admin-ui.html).

- To continue using the legacy admin UI, follow the steps in [Install the legacy admin UI](../setup-guide/legacy-admin-ui.html). |

[icon: feather-alt, set=fad, size=3x]

#### [Server Logs](server-logs.html)

Manage and read server logs.

[icon: eye, set=fad, size=3x]

#### [Monitoring](monitoring.html)

Set up systems to monitor IDM.

[icon: file-medical-alt, set=fad, size=3x]

#### [Metrics](metrics.html)

Monitoring metrics reference information.

---

---
title: OpenTelemetry logging
description: Configure OpenTelemetry logging in PingIDM to export logs using OTLP and correlate them with trace and span IDs in an OTEL collector
component: pingidm
version: 8.1
page_id: pingidm:monitoring-guide:opentelemetry-logging
canonical_url: https://docs.pingidentity.com/pingidm/8.1/monitoring-guide/opentelemetry-logging.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Monitoring", "Distributed tracing", "OpenTelemetry logging"]
section_ids:
  benefits-of-otel-logging: Benefits of OTEL logging
  configure-opentelemetry-logging: Configuring OTEL logging
  otel-log-record-example: OTEL log records
  otel-log-record-fields: Log record fields
  otel-logging-http-inbound-requests: OTEL logging for HTTP inbound requests
---

# OpenTelemetry logging

|   |                                                                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | [OpenTelemetry (OTEL)](https://opentelemetry.io/docs/what-is-opentelemetry/) logging is an [Evolving](../release-notes/appendix-interface-stability.html) feature in PingIDM. It's subject to change without notice, even in a minor or maintenance release. |

OTEL logging collects and exports logs using the [OpenTelemetry Protocol (OTLP)](https://github.com/open-telemetry/opentelemetry-proto/tree/main/docs/). It's a part of the broader OpenTelemetry observability framework that provides a unified way to collect logs, traces, and metrics from applications. Learn more in [Distributed tracing](distributed-tracing.html).

In PingIDM, logs are sent directly from IDM to an [OTEL collector](https://opentelemetry.io/docs/collector/) using JSON format and OTLP, rather than through traditional logging pipelines. Learn more in [Server logs](server-logs.html).

## Benefits of OTEL logging

OTEL logging makes it easier to:

* Correlate logs across Ping Identity products using trace IDs and span IDs. When a request flows through multiple systems, such as PingAM, IDM, and PingDS, you can track the entire journey using a single trace ID. Learn more in [Understand a trace object](distributed-tracing.html#understand-trace-object).

* Troubleshoot and pinpoint where issues occur in complex workflows. Trace IDs provide a high-level overview of a request, while span IDs show specific tasks within that trace.

* Standardize observability. You can use your preferred observability tools, such as Splunk, Datadog, or Grafana that support OTLP.

* Simplify setup because logs go directly to the OTEL collector and bypass previous processing steps.

* Enhance visibility to efficiently identify patterns, bottlenecks, or errors across distributed systems.

## Configuring OTEL logging

To configure and implement OpenTelemetry logging:

1. [Enable distributed tracing](distributed-tracing.html#enable-tracing) in IDM, which includes [trace](https://opentelemetry.io/docs/concepts/signals/traces/) and [span](https://opentelemetry.io/docs/concepts/signals/traces/#spans) IDs in the logs.

2. Start the OTEL collector. Learn more in the [OTEL Collector Quick Start](https://opentelemetry.io/docs/collector/quick-start/) and in [Visualize traces with a trace collector](distributed-tracing.html#viz-otel-traces).

3. [Configure the `OpenTelemetryAppender`](server-logs.html#logging-opentelemetry-appender). Learn more in [Log appenders](server-logs.html#log-appenders).

4. Initialize the OTEL `LoggerProvider`, which contains information about the OTEL collector endpoint where logs are sent and default settings for batched log processing.

   * Add the `LoggerProvider` configuration to the `trace.json` file created when you enabled distributed tracing in step 1:

     ```json
     {
        "logging": {
           "enabled": true,
           "exporter": {
              "type": "otlp",
              "config": {
                 "endpoint": "http://localhost:4318/v1/logs"
              }
           }
        }
     }
     ```

     The following example shows all available `LoggerProvider` configuration options:

     ```json
     {
        "logging": {
           "enabled": true,
           "exporter": {
              "type": "otlp",
              "config": {
                 "endpoint": "http://localhost:4318/v1/logs",
                 "headers": "<headers>",
                 "connectionTimeout": "10 seconds",
                 "timeout": "10 seconds",
                 "compressionMethod": "gzip",
                 "retries": {
                    "backoffMultiplier": 1.5,
                    "initialBackoff": "1 second",
                    "maxAttempts": 5,
                    "maxBackoff": "5 seconds"
                 }
              },
              "batch": {
                 "maxExportBatchSize": 512,
                 "maxQueueSize": 2048,
                 "scheduleDelay": "5 seconds",
                 "exporterTimeout": "30 seconds"
              }
           }
        }
     }
     ```

     > **Collapse: OpenTelemetry logging configuration properties**
     >
     > * enabled: boolean, optional
     >
     >   Set to `true` to enable OpenTelemetry logging.
     >
     >   Default: `false`
     >
     > * resourceAttributes: object, optional
     >
     >   A map of additional resource attributes for processing logs. Find more information in the OpenTelemetry documentation on [Semantic Attributes with SDK-provided Default Value](https://opentelemetry.io/docs/specs/semconv/resource/#semantic-attributes-with-sdk-provided-default-value).
     >
     >   For example, if there are multiple Ping Identity Platform instances in a deployment, you could set the `"service.instance.id"` resource attribute differently for each one to distinguish between them:
     >
     >   ```json
     >   {
     >     "resourceAttributes": {
     >       "service.instance.id": "idm-server-1"
     >     }
     >   }
     >   ```
     >
     > * exporter: object, optional
     >
     >   Configuration for the exporter, which pushes logs to the OpenTelemetry service:
     >
     >   * type: string, optional
     >
     >     Set to `otlp` for OpenTelemetry Protocol (OTLP) support. This is currently the only supported protocol.
     >
     >     Default: `otlp`
     >
     >   * config: object, optional
     >
     >     Endpoint and timeout configuration:
     >
     >     * `compressionMethod`: *enumeration, optional*
     >
     >       Method used to compress log data; either `gzip` or `none`.
     >
     >       Default: `gzip`
     >
     >     * `connectionTimeout`: *duration, optional*
     >
     >       Time out a connection to the endpoint after this duration.
     >
     >       Default: 10 seconds.
     >
     >     * `endpoint`: *string, optional*
     >
     >       The endpoint to publish traces to.
     >
     >       For HTTPS, IDM trusts the default JVM CAs. To override this, set the `-Djavax.net.ssl.trustStore` and associated JVM settings when starting IDM. Learn more about the optional settings in the [Java Secure Socket Extension (JSSE) Reference Guide](https://docs.oracle.com/en/java/javase/21/security/java-secure-socket-extension-jsse-reference-guide.html).
     >
     >       |   |                                                                              |
     >       | - | ---------------------------------------------------------------------------- |
     >       |   | IDM doesn't support TLS configuration for the tracing endpoint at this time. |
     >
     >       Default: `http://localhost:4318/v1/traces`
     >
     >     * `headers`: *object, optional*
     >
     >       Map of additional headers to include in the export span request.
     >
     >       The following example sets the authorization header, `Authorization: Bearer ${bearer.token}`:
     >
     >       ```none
     >       "headers": { "Authorization": "Bearer ${bearer.token}" }
     >       ```
     >
     >     * `retries`: *object, optional*
     >
     >       Defines a retry policy for the export span requests.
     >
     >       Default: Enabled
     >
     >       * `backoffMultiplier`: *number, optional* Multiplier for the backoff wait time before retries.
     >
     >         Default: 1.5
     >
     >       * `enabled`: *boolean, optional*
     >
     >         Retry failed requests.
     >
     >         Default: `true`
     >
     >       * `initialBackoff`: *duration, optional*
     >
     >         How long to wait before the first retry.
     >
     >         Default: 1 second
     >
     >       * `maxAttempts`: *number, optional*
     >
     >         Maximum number of retries.
     >
     >         Default: 5
     >
     >       * `maxBackoff`: *duration, optional*
     >
     >         Maximum wait time between retries.
     >
     >         Default: 5 seconds
     >
     >     * `timeout`: *duration, optional*
     >
     >       Time out a request to publish data to the endpoint after this duration.
     >
     >       Default: 10 seconds.
     >
     >   * `batch`: *object, optional*
     >
     >     Enable and configure batch processing for log data.
     >
     >     * `enabled`: *boolean, optional*
     >
     >       Leave batch processing enabled in deployment.
     >
     >       Default: `true`
     >
     >     * `exporterTimeout`: *duration, optional*
     >
     >       Time out a data exporter after this duration.
     >
     >       Default: 30 seconds
     >
     >     * `exportUnsampledSpans`: *boolean, optional*
     >
     >       Whether to report on unsampled spans.
     >
     >       Default: `false`
     >
     >     * `maxExportBatchSize`: *number, optional*
     >
     >       Maximum number of spans in a batch.
     >
     >       Default: 512
     >
     >     * `maxQueueSize`: *number, optional*
     >
     >       Maximum number of spans to queue before dropping them.
     >
     >       Default: 2048
     >
     >     * `scheduleDelay`: *duration, optional*
     >
     >       Maximum interval between sending batches of log data.
     >
     >       Default: 5 seconds

5. At the end of the `resolver/boot.properties` file, add the location of the `trace.json` file:

   ```
   openidm.tracing.config.path=trace/trace.json
   ```

6. [Start IDM](../install-guide/chap-install.html#run-openidm).

7. Go to your OTEL collector and view the logs sent from IDM.

### OTEL log records

In the OTEL collector, you can view log records in the OTLP format to find the trace and span IDs to follow a request across multiple systems.

This is an example of an IDM log record in the OTEL collector:

```text
Trace ID:
Span ID:
Flags: 0
LogRecord #238
ObservedTimestamp: 2025-11-14 18:23:29.219669 +0000 UTC
Timestamp: 2025-11-14 18:23:29.219661 +0000 UTC
SeverityText: DEBUG
SeverityNumber: Debug(5)
Body: Str(Bundle xstream not matched by org.forgerock.*)
Attributes:
 -> thread.name: Str(HealthCheck Bundles Started)
```

#### Log record fields

| Field Name          | Description                                                                                                                                                                                                           |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `LogRecord`         | Represents the recording of an event. In OpenTelemetry, a log record contains two kinds of fields:- Named top-level fields of specific type and meaning

- Resource and attributes fields of arbitrary value and type |
| `ObservedTimestamp` | Time when the event was observed.                                                                                                                                                                                     |
| `Timestamp`         | Time when the event occurred.                                                                                                                                                                                         |
| `SeverityText`      | The severity text (also known as log level).                                                                                                                                                                          |
| `SeverityNumber`    | Numerical value of the severity.                                                                                                                                                                                      |
| `Body`              | The body of the log record.                                                                                                                                                                                           |
| `Attributes`        | Additional information about the event.                                                                                                                                                                               |
| `Trace ID`          | Request trace ID.                                                                                                                                                                                                     |
| `Span ID`           | Request span ID.                                                                                                                                                                                                      |
| `Flags`             | A binary encoding that contains trace information.                                                                                                                                                                    |

Learn more about [Log Record fields and descriptions](https://opentelemetry.io/docs/concepts/signals/logs/#log-record).

### OTEL logging for HTTP inbound requests

When tracing is enabled, incoming HTTP requests automatically generate trace and span IDs. These IDs are included in log records sent to the OTEL collector. The trace and span ID fields are blank if the request doesn't come from an HTTP inbound request.

For an HTTP inbound request, here's an example scenario to find the trace and span IDs in the OTEL collector logs:

1. Sign on to the [IDM admin user interface (UI)](../setup-guide/chap-ui.html).

2. Go to the OTEL collector and view the span for the sign-on request that contains the trace ID:

   ```text
   Span #7 (1)
   Trace ID: 4cafb0e638a8c2ba58a8288e0e12470fd (2)
   Parent ID:
   ID: 6bdc24e07a2c9754
   Name: GET /openidm
   Kind: Server
   Start time: 2025-11-14 18:26:24.104794 +0000 UTC
   End time: 2025-11-14 18:26:24.110788 +0000 UTC
   Status code: Unset
   Status message:
   Attributes:
    -> http.request.method: Str(GET)
    -> url.path: Str(/openidm/info/version)
    -> url.full: Str(https://localhost:8443/openidm/info/version)
    -> network.protocol.name: Str(http)
    -> forgerock.transaction.id: Str(3caddd39-2942-4ccd-b527-9dfbd1f6353-1380)
    -> {"resource": "{service.instance.id": "5f481198b-5fc4-416b-a8d5-1d2cd5581f64", "service.name": "otelcol-contrib", "service.version": "0.128.0"}, "otelcol.component.id": "debug", "otelcol.component.kind": "exporter", "otelcol.signal": "traces"}
   2025-11-14T18:26:27.590Z info Metrics {"resource": "{service.instance.id": "5f481198b-5fc4-416b-a8d5-1d2cd5581f64", "service.name": "otelcol-contrib", "service.version": "0.128.0"}, "otelcol.component.id": "debug", "otelcol.component.kind": "exporter", "otelcol.signal": "metrics", "resource metrics": 1, "metrics": 27, "data points": 28}
   2025-11-14T18:26:27.591Z info Resource@Metrics #0
   Resource SchemaURL:
   Resource attributes:
    -> service.name: Str(otelcol-contrib)
    -> service.instance.id: Str(5f481198b-5fc4-416b-a8d5-1d2cd5581f64)
    -> server.port: Str(8888)
   ```

   |       |                                  |
   | ----- | -------------------------------- |
   | **1** | Span for the sign-on request     |
   | **2** | Associated trace ID for the span |

3. Find the matching trace ID in the log records to see the associated span ID:

   ```text
   LogRecord #23
   ObservedTimestamp: 2025-11-14 18:26:24.107832 +0000 UTC
   Timestamp: 2025-11-14 18:26:24.107823 +0000 UTC
   SeverityText: DEBUG
   SeverityNumber: Debug(5)
   Body: Str(Invoking read access)
   Attributes:
    -> thread.name: Str(qtp1868624459-218)
   Trace ID: 4cafb0e638a8c2ba58a8288e0e12470fd (1)
   Span ID: 6bdc24e07a2c9754 (2)
   Flags: 1
   ```

   |       |                                     |
   | ----- | ----------------------------------- |
   | **1** | Matching trace ID in the log record |
   | **2** | Matching associated span ID         |

4. View the log record body and attributes for more details about the sign-on request.

   In this example, the `Body` field for `LogRecord #23` shows the string `(Invoking read access)` because the user requested read access to the admin dashboard. This inbound HTTP request generated the trace and span IDs in the previous steps:

   ```text
   LogRecord #23
   ObservedTimestamp: 2025-11-14 18:26:24.107832 +0000 UTC
   Timestamp: 2025-11-14 18:26:24.107823 +0000 UTC
   SeverityText: DEBUG
   SeverityNumber: Debug(5)
   Body: Str(Invoking read access) (1)
   Attributes:
    -> thread.name: Str(qtp1868624459-218)
   Trace ID: 4cafb0e638a8c2ba58a8288e0e12470fd
   Span ID: 6bdc24e07a2c9754
   Flags: 1
   ```

   |       |                                                                          |
   | ----- | ------------------------------------------------------------------------ |
   | **1** | This string shows the user requested read access to the admin dashboard. |

---

---
title: Prometheus metrics
description: Reference for PingIDM Prometheus metrics at the /prometheus endpoint, including metric names for recon, sync, JVM, Jetty, scheduler, and workflow
component: pingidm
version: 8.1
page_id: pingidm:monitoring-guide:prometheus-metrics
canonical_url: https://docs.pingidentity.com/pingidm/8.1/monitoring-guide/prometheus-metrics.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Monitoring"]
section_ids:
  prometheus-metric-names: Prometheus general metrics available in IDM
  prometheus-jetty-metric-names: Prometheus Jetty metrics available in IDM
  prometheus-jvm-metric-names: Prometheus JVM metrics available in IDM
  prometheus-scheduler-metric-names: Prometheus scheduler metrics available in IDM
  prometheus-workflow-metric-names: Prometheus workflow metrics available in IDM
---

# Prometheus metrics

|   |                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | IDM generates metrics only after a corresponding event occurs. For example, IDM doesn't create login-related metrics until a user logs in. If you're using a monitoring tool like Grafana, this may appear as missing data or empty panels on your dashboard. |

Metrics accessed through the Prometheus endpoint are prepended with `idm_` and use underscores between words. For example, `idm_recon_target_phase_seconds`.

In IDM, the available Prometheus metric types include:

* [Summary](https://prometheus.io/docs/concepts/metric_types/#summary)

* [Counter](https://prometheus.io/docs/concepts/metric_types/#counter)

* [Gauge](https://prometheus.io/docs/concepts/metric_types/#gauge)

Summary metrics include:

* `metric_name_time-unit`: Contains `quantile` labels that provide the time-based distribution of measurements.

* `metric_name_count`: Represents the number of times the metric has been timed.

* `metric_name_time-unit_total`: Provides the total number of seconds measured by the metric per label group.

For example:

```text
idm_managed_seconds{managed_object="assignment",operation="queryCollection",quantile="0.5",} 9.728750000000001E-4
idm_managed_seconds{managed_object="assignment",operation="queryCollection",quantile="0.75",} 0.001247417
idm_managed_seconds{managed_object="assignment",operation="queryCollection",quantile="0.95",} 0.0016447500000000002
idm_managed_seconds{managed_object="assignment",operation="queryCollection",quantile="0.98",} 0.003216834
idm_managed_seconds{managed_object="assignment",operation="queryCollection",quantile="0.99",} 0.005315167
idm_managed_seconds{managed_object="assignment",operation="queryCollection",quantile="0.999",} 0.005315167
idm_managed_count{managed_object="assignment",operation="queryCollection",} 88.0
idm_managed_seconds_total{managed_object="assignment",operation="queryCollection",} 0.098369748

idm_managed_seconds{managed_object="organization",operation="create",quantile="0.5",} 0.007266166
idm_managed_seconds{managed_object="organization",operation="create",quantile="0.75",} 0.008662667
idm_managed_seconds{managed_object="organization",operation="create",quantile="0.95",} 0.028109959
idm_managed_seconds{managed_object="organization",operation="create",quantile="0.98",} 0.08822537500000001
idm_managed_seconds{managed_object="organization",operation="create",quantile="0.99",} 0.08822537500000001
idm_managed_seconds{managed_object="organization",operation="create",quantile="0.999",} 0.08822537500000001
idm_managed_count{managed_object="organization",operation="create",} 31.0
idm_managed_seconds_total{managed_object="organization",operation="create",} 0.373556921
```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For Summary metrics that don't include the `quantile` grouping (designated with a footnote in the following table), there's a known issue where the `_total` metric isn't a total of the entire series. Instead, the `_total` metric is a total of each label group, which leads to identical metrics for the `_total` and `count`.For example, the audit summary metric produces the following output:```text
idm_audit_total{audit_topic="access",} 571.0
idm_audit_count{audit_topic="access",} 571.0
idm_audit_total{audit_topic="activity",} 470.0
idm_audit_count{audit_topic="activity",} 470.0
idm_audit_total{audit_topic="authentication",} 548.0
idm_audit_count{audit_topic="authentication",} 548.0
``` |

|   |                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Deprecated metrics are still available until they're removed in a future release. Learn more in [Deprecated metric collection](monitoring.html#deprecated-metric-collection). |

## Prometheus general metrics available in IDM

| Metric Name                                                                                                           | Label / Type                                                                                                                                                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `idm_audit`\[[1](#_footnotedef_1 "View footnote.")]                                                                   | `{audit_topic=audit-topic}` Summary                                                                                                                                                                                                       | Count of all audit events generated of a given topic type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `idm_custom_endpoint_seconds`                                                                                         | `{name=endpoint-name,request_type=request-type}` Summary                                                                                                                                                                                  | Rate of calls to a custom endpoint script and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `idm_field_augmentation`                                                                                              | `{origin-type=edge\|vertex}` Summary                                                                                                                                                                                                      | Rate of reading response objects to fulfill the `_fields` requested (when the fields weren't populated by the initial repo query).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []()`idm_router_filter_seconds`\[[2](#_footnotedef_2 "View footnote.")]\[[3](#_footnotedef_3 "View footnote.")]       | `{action=action,name=name,script_name=script_name,quantile=quantile,system=system}` Summary                                                                                                                                               | Rate that filter scripts are executed, per action. Monitors scripted filters and delegated administration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `idm_icf_connector_server_availability`                                                                               | `{name=system-identifier,type=connector-server-type}` Gauge                                                                                                                                                                               | Status of the connector server. A value of `1` indicates the server is running. A value of `0` indicates the server isn't running.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []()`idm_icf_pending`\[[4](#_footnotedef_4 "View footnote.")]                                                         | `{action="authentication",bundle_version=bundle_version,connector=connector,connector_type=connector_type,location=location,operation="action",system_identifier=system_identifier,quantile=quantile}` Gauge                              | The number of pending `authentication` actions over the configured limit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                       | `{bundle_version=bundle_version,connector=connector,connector_type=connector_type,location=location,operation="create",system_identifier=system_identifier,quantile=quantile}` Gauge                                                      | The number of pending `create` operations over the configured limit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                       | `{bundle_version=bundle_version,connector=connector,connector_type=connector_type,location=location,operation="delete",system_identifier=system_identifier,quantile=quantile}` Gauge                                                      | The number of pending `delete` operations over the configured limit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                       | `{action="liveSync",bundle_version=bundle_version,connector=connector,connector_type=connector_type,location=location,object_class=objectClass,operation="action",system_identifier=system_identifier,quantile=quantile}` Gauge           | The number of pending `liveSync` actions on a system object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                       | `{bundle_version=bundle_version,connector=connector,connector_type=connector_type,location=location,operation="patch",system_identifier=system_identifier,quantile=quantile}` Gauge                                                       | The number of pending `patch` operations over the configured limit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                       | `{bundle_version=bundle_version,connector=connector,connector_type=connector_type,location=location,operation="read",system_identifier=system_identifier,quantile=quantile}` Gauge                                                        | The number of pending `read` operations over the configured limit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                       | `{bundle_version=bundle_version,connector=connector,connector_type=connector_type,location=location,operation="update",system_identifier=system_identifier,quantile=quantile}` Gauge                                                      | The number of pending `update` operations over the configured limit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                       | `{bundle_version=bundle_version,connector=connector,connector_type=connector_type,location=location,operation="query",query_type="_queryExpression",system_identifier=system_identifier,quantile=quantile}` Gauge                         | The number of pending `queryExpression` operations over the configured limit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                       | `{bundle_version=bundle_version,connector=connector,connector_type=connector_type,location=location,operation="query",query_type="_queryFilter",system_identifier=system_identifier,quantile=quantile}` Gauge                             | The number of pending `queryFilter` operations over the configured limit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                       | `{bundle_version=bundle_version,connector=connector,connector_type=connector_type,location=location,operation="query",query_type="_queryId",system_identifier=system_identifier,quantile=quantile}` Gauge                                 | The number of pending `queryId` operations over the configured limit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                       | `{bundle_version=bundle_version,connector=connector,connector_type=connector_type,location=location,operation="query",query_type="_UNKNOWN",system_identifier=system_identifier,quantile=quantile}` Gauge                                 | The number of pending `UNKNOWN` operations over the configured limit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `idm_icf_seconds`                                                                                                     | `{action="authenticate",bundle_version=bundle_version,connector=connector,connector_type=connector_type,location=location,object_class=objectClass,operation="action",system_identifier=system_identifier,quantile=quantile}` Summary     | Rate of ICF `authentication` actions and the action performance time for the given connector.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                       | `{bundle_version=bundle_version,connector=connector,connector_type=connector_type,location=location,object_class=objectClass,operation="create",system_identifier=system_identifier,quantile=quantile}` Summary                           | Rate of ICF `create` operations and the operation performance time for the given connector.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                       | `{bundle_version=bundle_version,connector=connector,connector_type=connector_type,location=location,object_class=objectClass,operation="delete",system_identifier=system_identifier,quantile=quantile}` Summary                           | Rate of ICF `delete` operations and the operation performance time for the given connector.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                       | []()`{action="liveSync",bundle_version=bundle_version,connector=connector,connector_type=connector_type,location=location,object_class=objectClass,operation="action",system_identifier=system_identifier,quantile=quantile}` Summary     | Duration of live sync on a system object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                       | `{bundle_version=bundle_version,connector=connector,connector_type=connector_type,location=location,object_class=objectClass,operation="patch",system_identifier=system_identifier,quantile=quantile}` Summary                            | Rate of ICF `patch` operations and the operation performance time for the given connector.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                       | `{bundle_version=bundle_version,connector=connector,connector_type=connector_type,location=location,object_class=objectClass,operation="read",system_identifier=system_identifier,quantile=quantile}` Summary                             | Rate of ICF `read` operations and the operation performance time for the given connector.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                       | `{bundle_version=bundle_version,connector=connector,connector_type=connector_type,location=location,object_class=objectClass,operation="update",system_identifier=system_identifier,quantile=quantile}` Summary                           | Rate of ICF `update` operations and the operation performance time for the given connector.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                       | `{bundle_version=bundle_version,connector=connector,connector_type=connector_type,location=location,object_class=objectClass,operation="query",query_type=queryExpression,system_identifier=system_identifier,quantile=quantile}` Summary | Rate of ICF query executions with `queryExpression` and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                       | `{bundle_version=bundle_version,connector=connector,connector_type=connector_type,location=location,object_class=objectClass,operation="query",query_type=queryFilter,system_identifier=system_identifier,quantile=quantile}` Summary     | Rate of ICF query executions with `queryFilter` and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                       | `{bundle_version=bundle_version,connector=connector,connector_type=connector_type,location=location,object_class=objectClass,operation="query",query_type=queryId,system_identifier=system_identifier,quantile=quantile}` Summary         | Rate of ICF query executions with `queryId` and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                       | `{bundle_version=bundle_version,connector=connector,connector_type=connector_type,location=location,object_class=objectClass,operation="query",query_type="UNKNOWN",system_identifier=system_identifier,quantile=quantile}` Summary       | Rate of ICF query executions when the query type is `UNKNOWN` and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `idm_internal_relationship_fetch_relationship_fields_seconds`                                                         | `{internal_object=internal-object}` Summary                                                                                                                                                                                               | Rate of fetch operations of relationship fields for internal objects.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `idm_internal_role_relationship_get_relationship_value_for_resource_seconds`                                          | Summary                                                                                                                                                                                                                                   | Query rate on relationship values for internal objects.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `idm_internal_relationship_validate_relationship_fields_seconds`                                                      | `{internal-object=internal-object}` Summary                                                                                                                                                                                               | Rate of validate operations of relationship fields for internal objects.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `idm_internal_seconds`                                                                                                | `{internal_object=internal-object,operation=operation}` Summary                                                                                                                                                                           | Rate of operations on internal objects.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `idm_live_sync_seconds`                                                                                               | `{object-type=object-type,system-name=system-name}` Summary                                                                                                                                                                               | Duration of live sync on a system object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `idm_managed_relationship_fetch_relationship_fields_seconds`                                                          | Summary                                                                                                                                                                                                                                   | Rate of fetches of relationship fields of a managed object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `idm_managed_managed-object_relationship_get_relationship_value_for_resource_seconds`                                 | Summary                                                                                                                                                                                                                                   | Rate of queries to get relationship values for a resource on a managed object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `idm_managed_relationship_validate_relationship_fields_seconds`                                                       | Summary                                                                                                                                                                                                                                   | Rate of validations of relationship fields of a managed object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `idm_managed_seconds`                                                                                                 | `{managed_object=managed-object,operation=operation}` Summary                                                                                                                                                                             | Rate of operations on a managed object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| []()`idm_managed_script_hook_seconds`\[[5](#_footnotedef_5 "View footnote.")]\[[3](#_footnotedef_3 "View footnote.")] | `{object=object, script_hook=script_hook}` Summary                                                                                                                                                                                        | Rate of executions of a script on a managed object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `idm_managed_object_handle_temporal_constraints_on_create`                                                            | Summary                                                                                                                                                                                                                                   | Latency of enforcing temporal constraints on role objects during object creation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `idm_managed_object_handle_temporal_constraints_on_delete`                                                            | Summary                                                                                                                                                                                                                                   | Latency of enforcing temporal constraints on role objects during object deletion.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `idm_managed_object_handle_temporal_constraints_on_update`                                                            | Summary                                                                                                                                                                                                                                   | Latency of enforcing temporal constraints on role objects during object update.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `idm_managed_relationship_handle_temporal_constraints_on_create`                                                      | Summary                                                                                                                                                                                                                                   | Latency of enforcing temporal constraints on relationship grants during edge creation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `idm_managed_relationship_handle_temporal_constraints_on_delete`                                                      | Summary                                                                                                                                                                                                                                   | Latency of enforcing temporal constraints on relationship grants during edge deletion.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `idm_managed_relationship_handle_temporal_constraints_on_update`                                                      | Summary                                                                                                                                                                                                                                   | Latency of enforcing temporal constraints on relationship grants during edge update.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `idm_managed_relationship_validate_read_relationship_endpoint_edges_seconds`                                          | Summary                                                                                                                                                                                                                                   | Rate of reads on relationship endpoint edges for validation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `idm_null_array_filter_augmentation_seconds`                                                                          | `{request_type=requestType}` Summary                                                                                                                                                                                                      | Time spent in filter that maps non-nullable, null-valued array fields to an empty array. This filter is traversed for all repository access relating to internal and managed objects.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `idm_recon_assoc_entry_merged_query_merge_results_seconds`                                                            | Summary                                                                                                                                                                                                                                   | Rate of merge operations after source or target objects are retrieved during a merged query of reconciled association entries.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `idm_recon_assoc_entry_merged_query_page_assoc_entries_seconds`                                                       | Summary                                                                                                                                                                                                                                   | Rate of individual paged reconciled association entry queries during a merged query. More than one page of entries might be requested to build a single page of merged results.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `idm_recon_assoc_entry_merged_query_query_source_seconds`                                                             | Summary                                                                                                                                                                                                                                   | Rate of source object retrieval using a query when merging source objects to reconciled association entries.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `idm_recon_assoc_entry_merged_query_query_target_seconds`                                                             | Summary                                                                                                                                                                                                                                   | Rate of target object retrieval using a query when merging target objects to reconciled association entries.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `idm_recon_association-persistence`                                                                                   | `{recon-id=reconId,operation=operation}` Summary                                                                                                                                                                                          | The time taken to persist association data. The operation can be `source`, `target`, or `amendsource`, depending on whether data is produced for a source-phase or target-phase reconciliation association, or to amend the association for a specific source.                                                                                                                                                                                                                                                                                                                                                                               |
| `idm_recon_id_queries_phase_seconds`                                                                                  | Summary                                                                                                                                                                                                                                   | Rate of executions of the ID query phase of a reconciliation and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `idm_recon_seconds`                                                                                                   | Summary                                                                                                                                                                                                                                   | Rate of executions of a full reconciliation and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `idm_recon_source_phase_page_seconds`                                                                                 | Summary                                                                                                                                                                                                                                   | Rate of pagination executions of the source phase of a reconciliation and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `idm_recon_source_phase_seconds`                                                                                      | Summary                                                                                                                                                                                                                                   | Rate of executions of the source phase of a reconciliation and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `idm_recon_target_phase_seconds`                                                                                      | Summary                                                                                                                                                                                                                                   | Rate of executions of the target phase of a reconciliation and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `idm_repo_seconds`                                                                                                    | `{action_name=action-name,command=command,operation=operation,repo_type=repo-type,resource_mapping=resource-mapping}` Summary                                                                                                             | Rate of actions to a repository datasource for a generic or explicit mapped table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                       | `{operation=operation,repo_type=repo-type,resource_mapping=resource_mapping,query_type=query_type,action_name=action_name,command=command}` Summary                                                                                       | Rate of filtered queries (using [native query expressions](../objects-guide/queries.html#native-queries)) on the relationship table. This metric measures the time spent running the query and the number of times it's invoked.                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                       | `{operation=operation,repo_type=repo-type,resource_mapping=resource_mapping,query_type=queryFilter,action_name=action_name,command=command}` Summary                                                                                      | Rate of filtered queries using the `_queryFilter` parameter on the relationship table. This metric measures the time spent running the query and the number of times it's invoked.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `idm_repo_execute_seconds`                                                                                            | `{operation=create_properties,repo_type=repo-type,resource_mapping=resource-mapping}` Summary                                                                                                                                             | Rate of execution time on the JDBC database for the `create_properties` operations. This operation is performed for every generic object `create` when it persists the searchable properties. The rate measured here doesn't include the time taken to connect to the database from the connection pool. The physical connections to the database have already been established inside the connection pool.                                                                                                                                                                                                                                  |
|                                                                                                                       | `{operation=operation,repo_type=repo-type,resource_mapping=resource-mapping}` Summary                                                                                                                                                     | Rate of execution time on the JDBC database for CRUD operations. This rate doesn't include the time taken to connect to the database from the connection pool. The physical connections to the database have already been established inside the connection pool.                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                       | `{operation="query",queryType=queryFilter\|queryId,repo_type=repo-type,resource_mapping=resource-mapping}` Summary                                                                                                                        | Rate of execution time on the JDBC database for queries (either `queryFilter` or `queryId`). This rate doesn't include the time taken to connect to the database from the connection pool. The physical connections to the database have already been established inside the connection pool.                                                                                                                                                                                                                                                                                                                                                |
| `idm_repo_get_connection_seconds`                                                                                     | `{repo_type=repo-type}` Summary                                                                                                                                                                                                           | Rate of retrievals of a repository connection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `idm_repo_jdbc_cache_objecttypes_count`                                                                               | `{event="hit\|miss",type=resource-mapping}` Counter                                                                                                                                                                                       | Counts the usage statistics of the `objecttypeid` cache that maps an object type to its `objecttypeid`. The expected count is a small number of misses (sometimes, only one) and the remainder of hits.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `idm_repo_jdbc_relationship_edge_execute_seconds`                                                                     | `{joinedToVertex=joinedToVertex>}` Summary                                                                                                                                                                                                | Time spent running the Edge→Vertex relationship join query on the database and collecting the result set.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `idm_repo_jdbc_relationship_edge_process_seconds`\[[1](#_footnotedef_1 "View footnote.")]                             | `{joinedToVertex=joinedToVertex}` Summary                                                                                                                                                                                                 | The amount of time taken to process the results returned from the query measured by `idm_repo_jdbc_relationship_edge_execute_seconds`, but not the query itself.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `idm_repo_jdbc_relationship_find_referenced_collections_seconds` \[[1](#_footnotedef_1 "View footnote.")]             | Summary                                                                                                                                                                                                                                   | Measures the SQL execution time to find referenced collections on the Edge→Vertex relationship.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `idm_repo_jdbc_relationship_vertex_execute_seconds`                                                                   | Summary                                                                                                                                                                                                                                   | Rate of relationship graph query execution times.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `idm_repo_jdbc_relationship_vertex_process_seconds`                                                                   | Summary                                                                                                                                                                                                                                   | Rate of relationship graph query result processing times.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `idm_repo_raw__queryid_credential_queryId_seconds`                                                                    | Summary                                                                                                                                                                                                                                   | Execution rate of a query with `queryId` at a repository level and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `idm_repo_relationship_count`                                                                                         | `{operation=operation,origin_type=origin_type,repo_type=repo_type,stage=stage}` Counter                                                                                                                                                   | The count of all repository relationship calls referenced by queried objects.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `idm_repo_relationship_seconds`                                                                                       | `{operation=operation,repo_type=repo-type}` Summary                                                                                                                                                                                       | Time of CRUDPAQ operations to a repository datasource for a generic, explicit, or relationship mapped table.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                       | `{operation=operation,repo_type=repo-type,resource_mapping=resource-mapping}` Summary                                                                                                                                                     | Rate of initiations of a CRUDPAQ operation to a repository datasource.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `idm_router_path-name_action_action-type_seconds`                                                                     | Summary                                                                                                                                                                                                                                   | Rate of actions over the router and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `idm_router_path-name_create_seconds`                                                                                 | Summary                                                                                                                                                                                                                                   | Rate of creates over the router and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `idm_router_path-name_delete_seconds`                                                                                 | Summary                                                                                                                                                                                                                                   | Rate of deletes over the router and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `idm_router_path-name_patch_seconds`                                                                                  | Summary                                                                                                                                                                                                                                   | Rate of patches over the router and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `idm_router_path-name_query_queryExpression_seconds`                                                                  | Summary                                                                                                                                                                                                                                   | Rate of queries with `queryExpression` completed over the router and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `idm_router_path-name_query_queryFilter_seconds`                                                                      | Summary                                                                                                                                                                                                                                   | Rate of queries with `queryFilter` completed over the router and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `idm_router_path-name_read_seconds`                                                                                   | Summary                                                                                                                                                                                                                                   | Rate of reads over the router and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `idm_router_path-name_update_seconds`                                                                                 | Summary                                                                                                                                                                                                                                   | Rate of updates over the router and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `idm_sync_create_object_seconds`                                                                                      | Summary                                                                                                                                                                                                                                   | Rate of requests to create an object on the target and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `idm_sync_delete_target_seconds`                                                                                      | Summary                                                                                                                                                                                                                                   | Rate of requests to delete an object on the target and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `idm_sync_objectmapping_seconds`                                                                                      | `{mapping_name=mapping-name}` Summary                                                                                                                                                                                                     | Rate of configurations applied to a mapping.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `idm_sync_queue_acquire`                                                                                              | `{mapping_name=mapping-name, action=action}` Summary                                                                                                                                                                                      | Rate of acquisition of queued synchronization events from the queue.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `idm_sync_queue_discard`                                                                                              | `{mapping_name=mapping-name, action=action}` Summary                                                                                                                                                                                      | Rate of deletion of synchronization events from the queue.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `idm_sync_queue_execution`                                                                                            | `{mapping_name=mapping-name, action=action}` Summary                                                                                                                                                                                      | Rate at which queued synchronization operations are run.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `idm_sync_queue_failed` \[[1](#_footnotedef_1 "View footnote.")]                                                      | `{mapping_name=mapping-name, action=action}` Summary                                                                                                                                                                                      | Number of queued synchronization operations that failed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `idm_sync_queue_poll_pending_events`                                                                                  | `{mapping_name=mapping-name}` Summary                                                                                                                                                                                                     | The polling latency for synchronization events.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `idm_sync_queue_precondition_failed` \[[1](#_footnotedef_1 "View footnote.")]                                         | `{mapping_name=mapping-name, action=action}` Summary                                                                                                                                                                                      | Number of queued synchronization events acquired by another node in the cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `idm_sync_queue_query_previously_acquired_events_seconds` \[[1](#_footnotedef_1 "View footnote.")]                    | `{mapping_name=mapping-name}` Summary                                                                                                                                                                                                     | Measures the amount of time spent querying for synchronization events previously acquired by another node that have now been acquired by this node due to a mapping rebalancing.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `idm_sync_queue_rejected_executions` \[[1](#_footnotedef_1 "View footnote.")]                                         | `{mapping_name=mapping-name, action=action}` Summary                                                                                                                                                                                      | Number of queued synchronization events rejected because the backing thread-pool queue reached full capacity and the thread pool had allocated its maximum-configured number of threads.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `idm_sync_queue_release`                                                                                              | `{mapping_name=mapping-name, action=action}` Summary                                                                                                                                                                                      | Rate at which queued synchronization events are released.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `idm_sync_queue_submit`                                                                                               | `{mapping_name=mapping-name, action=action}` Summary                                                                                                                                                                                      | Insertion rate of synchronization events into the queue.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `idm_sync_raw_read_object_seconds`                                                                                    | Summary                                                                                                                                                                                                                                   | Rate of reads of an object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `idm_sync_source_assess_situation_seconds`                                                                            | Summary                                                                                                                                                                                                                                   | Assessment rate of a synchronization situation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `idm_sync_source_correlate_target_seconds`                                                                            | Summary                                                                                                                                                                                                                                   | Correlation rate between a target and a given source, and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `idm_sync_source_determine_action_seconds`                                                                            | Summary                                                                                                                                                                                                                                   | Determination rate on a synchronization action based on its current situation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `idm_sync_source_perform_action_seconds`                                                                              | Summary                                                                                                                                                                                                                                   | Completion rate of an action performed on a synchronization operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `idm_sync_target_assess_situation_seconds`                                                                            | Summary                                                                                                                                                                                                                                   | Assessment rate of a target situation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `idm_sync_target_determine_action_seconds`                                                                            | Summary                                                                                                                                                                                                                                   | Determination rate on a target action based on its current situation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `idm_sync_target_perform_action_seconds`                                                                              | Summary                                                                                                                                                                                                                                   | Completion rate of an action performed on a target synchronization operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `idm_sync_update_target_seconds`                                                                                      | Summary                                                                                                                                                                                                                                   | Request rate to update an object on the target and the time taken to perform this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `idm_user_login` \[[1](#_footnotedef_1 "View footnote.")]                                                             | `{user_type=user-type}` Summary                                                                                                                                                                                                           | Count of all successful logins by user type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `idm_user_login_total` \[[1](#_footnotedef_1 "View footnote.")]                                                       | `{provider=provider,user_type=user-type}` Summary                                                                                                                                                                                         | Count of all successful logins by user type and provider.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `idm_virtualpropertiesfromrelationships_notfound` \[[1](#_footnotedef_1 "View footnote.")]                            | `{virtual_properties=virtual_properties[6],relationship_traversal=relationship_resource_path}[7]` Summary                                                                                                                                 | Number of 404 responses encountered when querying the `resource_collection`/`relationship_field` specified in the `traversal_depthX` tag for the most recent X. X corresponds to the relationship field sequence.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `idm_virtualpropertiesfromrelationships_unsatisfiedtempconstraint`\[[1](#_footnotedef_1 "View footnote.")]            | `{virtual_properties=virtual_properties[6],relationship_traversal=relationship_resource_path}[7]` Summary                                                                                                                                 | Number of edges skipped due to an unsatisfied temporal constraint on either the edge or the referred-to vertex. Encountered when querying the resource collection and relationship field at the `traversal_depthX` tag for the most recent X. X corresponds to the relationship field sequence.                                                                                                                                                                                                                                                                                                                                              |
| `idm_virtualpropertiesfromrelationships_seconds`\[[1](#_footnotedef_1 "View footnote.")]                              | `{virtual_properties=virtual_properties[6],relationship_resource_path=relationship_resource_path}[7]` Summary                                                                                                                             | Time spent traversing relationship fields to calculate the specified virtual properties. The managed objects linked to by the traversal relationship fields define a tree, whose root is the virtual property host. This object tree is traversed depth-first, with the `traversal_depthX` corresponding to the latency involved with each relationship traversal. `Traversal_depth0` corresponds to the first relationship field traversed. Because the tree is traversed depth-first, `traversal_depthX` will subsume all the traversal latencies for all `traversal_depthY`, where Y>X. X corresponds to the relationship field sequence. |
| `idm_edge_to_vertex_relationship_created_seconds` \[[1](#_footnotedef_1 "View footnote.")]                            | Summary                                                                                                                                                                                                                                   | Time it takes to create the Edge→Vertex relationship.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `idm_edge_to_vertex_relationship_notification_seconds` \[[1](#_footnotedef_1 "View footnote.")]                       | Summary                                                                                                                                                                                                                                   | Time it takes to provide notifications on the Edge→Vertex relationship.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

## Prometheus Jetty metrics available in IDM

These metrics include Jetty thread pool and request metrics.

| Prometheus Metric Name                                                  | Type    | Unit        | Description                                                                                                                                    |
| ----------------------------------------------------------------------- | ------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| []()`idm_jetty_qos_queue_count`\[[8](#_footnotedef_8 "View footnote.")] | Gauge   | Count       | Current number of requests queued in the [Jetty QoSHandler](../install-guide/idm-config-properties-jetty.html#config-jetty-qos-handler) queue. |
| []()`idm_jetty_qos_queue_count_max`                                     | Gauge   | Count       | Maximum number of requests that can be queued.                                                                                                 |
| []()`idm_jetty_qos_concurrent_max`                                      | Gauge   | Count       | Maximum number of requests that can be handled concurrently.                                                                                   |
| []()`idm_jetty_qos_queue_milliseconds_max`                              | Gauge   | Count       | Maximum amount of time a request can be queued.                                                                                                |
| `idm_jetty_thread_queue`\[[8](#_footnotedef_8 "View footnote.")]        | Gauge   | Count       | Size of the job queue.                                                                                                                         |
| `idm_jetty_thread{thread_type="ready"}`                                 | Gauge   | Count       | Number of threads ready to run transient jobs, such as handling requests.                                                                      |
| `idm_jetty_thread{thread_type="leased"}`                                | Gauge   | Count       | Number of threads used by internal Jetty components.                                                                                           |
| `idm_jetty_thread{thread_type="reserved"}`                              | Gauge   | Count       | Number of available threads reserved for queue management.                                                                                     |
| `idm_jetty_thread{thread_type="idle"}`                                  | Gauge   | Count       | Number of idle threads that aren't reserved.                                                                                                   |
| `idm_jetty_thread{thread_type="utilized"}`                              | Gauge   | Count       | Number of threads currently running transient jobs, such as handling requests.                                                                 |
| `idm_jetty_thread_total`                                                | Gauge   | Count       | Total number of threads in the pool.                                                                                                           |
| `idm_jetty_thread_islowonthreads`                                       | Gauge   | Count       | Whether the pool is low on threads. `1` if true, `0` otherwise.                                                                                |
| `idm_jetty_request_active`                                              | Gauge   | Count       | Current number of active requests.                                                                                                             |
| `idm_jetty_request_max`                                                 | Counter | Count       | Maximum number of concurrently active requests.                                                                                                |
| `idm_jetty_request_failed{error_code="4xx"}`                            | Counter | Count       | Number of requests with a `4xx` response status.                                                                                               |
| `idm_jetty_request_failed{error_code="5xx"}`                            | Counter | Count       | Number of requests with a `5xx` response status.                                                                                               |
| `idm_jetty_request_nanoseconds_max`                                     | Gauge   | Nanoseconds | Maximum request run time.                                                                                                                      |
| `idm_jetty_request_nanoseconds_stddev`                                  | Gauge   | Nanoseconds | Standard deviation for request run time.                                                                                                       |
| `idm_jetty_request_servlet_active`                                      | Gauge   | Count       | Current number of requests the servlets handle.                                                                                                |
| `idm_jetty_request_servlet_max`                                         | Counter | Count       | Maximum number of requests the servlets handle concurrently.                                                                                   |
| `idm_jetty_request_servlet_nanoseconds_max`                             | Gauge   | Nanoseconds | Maximum servlet run time.                                                                                                                      |
| `idm_jetty_request_servlet_nanoseconds_stddev`                          | Gauge   | Nanoseconds | Standard deviation for servlet run time.                                                                                                       |

## Prometheus JVM metrics available in IDM

|   |                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | These metrics depend on the JVM version and configuration. In particular, garbage-collector-related metrics depend on the garbage collector that the server uses. The garbage-collector metric names are unstable and can change even in a minor JVM release. |

| Prometheus Metric Name                                                          | Type    | Unit         | Description                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------- | ------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `idm_jvm_available_cpus`                                                        | Gauge   | Count        | Number of processors available to the JVM. Learn more in [Runtime](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runtime.html).                                                                |
| `idm_jvm_class_loading_loaded_total`                                            | Counter | Count        | Number of classes loaded since the Java virtual machine started. Learn more in [ClassLoadingMXBean](https://docs.oracle.com/en/java/javase/21/docs/api/java.management/java/lang/management/ClassLoadingMXBean.html).   |
| `idm_jvm_class_loading_unloaded_total`                                          | Counter | Count        | Number of classes unloaded since the Java virtual machine started. Learn more in [ClassLoadingMXBean](https://docs.oracle.com/en/java/javase/21/docs/api/java.management/java/lang/management/ClassLoadingMXBean.html). |
| `idm_jvm_free_memory_bytes`                                                     | Gauge   | Bytes        | Learn more in [Runtime](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runtime.html).                                                                                                           |
| `idm_jvm_garbage_collector_count_total{name="G1-Old-Generation"}`               | Counter | Count        | For each garbage collector in the JVM. Learn more in [GarbageCollectorMXBean](https://docs.oracle.com/en/java/javase/21/docs/api/java.management/java/lang/management/GarbageCollectorMXBean.html).                     |
| `idm_jvm_garbage_collector_time_total{name="G1-Old-Generation"}`                | Counter | Milliseconds |                                                                                                                                                                                                                         |
| `idm_jvm_garbage_collector_count_total{name="G1-Young-Generation"}`             | Counter | Count        |                                                                                                                                                                                                                         |
| `idm_jvm_garbage_collector_time_total{name="G1-Young-Generation"}`              | Counter | Milliseconds |                                                                                                                                                                                                                         |
| `idm_jvm_max_memory_bytes`                                                      | Gauge   | Bytes        | Learn more in [Runtime](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runtime.html).                                                                                                           |
| `idm_jvm_memory_usage_committed{location="heap"}`                               | Gauge   | Bytes        | Amount of heap memory committed for the JVM to use. Learn more in [MemoryMXBean](https://docs.oracle.com/en/java/javase/21/docs/api/java.management/java/lang/management/MemoryMXBean.html).                            |
| `idm_jvm_memory_usage_init{location="heap"}`                                    | Gauge   | Bytes        |                                                                                                                                                                                                                         |
| `idm_jvm_memory_usage_max{location="heap"}`                                     | Gauge   | Bytes        | Maximum amount of heap memory available to the JVM.                                                                                                                                                                     |
| `idm_jvm_memory_usage_used{location="heap"}`                                    | Gauge   | Bytes        | Amount of heap memory used by the JVM.                                                                                                                                                                                  |
| `idm_jvm_memory_usage_committed{location="non-heap"}`                           | Gauge   | Bytes        | Amount of non-heap memory committed for the JVM to use.                                                                                                                                                                 |
| `idm_jvm_memory_usage_init{location="non-heap"}`                                | Gauge   | Bytes        | Amount of non-heap memory the JVM initially requested from the operating system.                                                                                                                                        |
| `idm_jvm_memory_usage_max{location="non-heap"}`                                 | Gauge   | Bytes        | Maximum amount of non-heap memory available to the JVM.                                                                                                                                                                 |
| `idm_jvm_memory_usage_used{location="non-heap"}`                                | Gauge   | Bytes        | Amount of non-heap memory used by the JVM.                                                                                                                                                                              |
| `idm_jvm_memory_usage_pools_committed{name="CodeHeap-'non-nmethods'"}`          | Gauge   | Bytes        | For each pool. Learn more in [MemoryPoolMXBean](https://docs.oracle.com/en/java/javase/21/docs/api/java.management/java/lang/management/MemoryPoolMXBean.html).                                                         |
| `idm_jvm_memory_usage_pools_init{name="CodeHeap-'non-nmethods'"}`               | Gauge   | Bytes        |                                                                                                                                                                                                                         |
| `idm_jvm_memory_usage_pools_max{name="CodeHeap-'non-nmethods'"}`                | Gauge   | Bytes        |                                                                                                                                                                                                                         |
| `idm_jvm_memory_usage_pools_used{name="CodeHeap-'non-nmethods'"}`               | Gauge   | Bytes        |                                                                                                                                                                                                                         |
| `idm_jvm_memory_usage_pools_committed{name="CodeHeap-'non-profiled-nmethods'"}` | Gauge   | Bytes        |                                                                                                                                                                                                                         |
| `idm_jvm_memory_usage_pools_init{name="CodeHeap-'non-profiled-nmethods'"}`      | Gauge   | Bytes        |                                                                                                                                                                                                                         |
| `idm_jvm_memory_usage_pools_max{name="CodeHeap-'non-profiled-nmethods'"}`       | Gauge   | Bytes        |                                                                                                                                                                                                                         |
| `idm_jvm_memory_usage_pools_used{name="CodeHeap-'non-profiled-nmethods'"}`      | Gauge   | Bytes        |                                                                                                                                                                                                                         |
| `idm_jvm_memory_usage_pools_committed{name="CodeHeap-'profiled-nmethods'"}`     | Gauge   | Bytes        |                                                                                                                                                                                                                         |
| `idm_jvm_memory_usage_pools_init{name="CodeHeap-'profiled-nmethods'"}`          | Gauge   | Bytes        |                                                                                                                                                                                                                         |
| `idm_jvm_memory_usage_pools_max{name="CodeHeap-'profiled-nmethods'"}`           | Gauge   | Bytes        |                                                                                                                                                                                                                         |
| `idm_jvm_memory_usage_pools_used{name="CodeHeap-'profiled-nmethods'"}`          | Gauge   | Bytes        |                                                                                                                                                                                                                         |
| `idm_jvm_memory_usage_pools_committed{name="Compressed-Class-Space"}`           | Gauge   | Bytes        |                                                                                                                                                                                                                         |
| `idm_jvm_memory_usage_pools_init{name="Compressed-Class-Space"}`                | Gauge   | Bytes        |                                                                                                                                                                                                                         |
| `idm_jvm_memory_usage_pools_max{name="Compressed-Class-Space"}`                 | Gauge   | Bytes        |                                                                                                                                                                                                                         |
| `idm_jvm_memory_usage_pools_used{name="Compressed-Class-Space"}`                | Gauge   | Bytes        |                                                                                                                                                                                                                         |
| `idm_jvm_memory_usage_pools_committed{name="G1-Eden-Space"}`                    | Gauge   | Bytes        |                                                                                                                                                                                                                         |
| `idm_jvm_memory_usage_pools_init{name="G1-Eden-Space"}`                         | Gauge   | Bytes        |                                                                                                                                                                                                                         |
| `idm_jvm_memory_usage_pools_max{name="G1-Eden-Space"}`                          | Gauge   | Bytes        |                                                                                                                                                                                                                         |
| `idm_jvm_memory_usage_pools_used{name="G1-Eden-Space"}`                         | Gauge   | Bytes        |                                                                                                                                                                                                                         |
| `idm_jvm_memory_usage_pools_used_after_gc{name="G1-Eden-Space"}`                | Gauge   | Bytes        |                                                                                                                                                                                                                         |
| `idm_jvm_memory_usage_pools_committed{name="G1-Old-Gen"}`                       | Gauge   | Bytes        |                                                                                                                                                                                                                         |
| `idm_jvm_memory_usage_pools_init{name="G1-Old-Gen"}`                            | Gauge   | Bytes        |                                                                                                                                                                                                                         |
| `idm_jvm_memory_usage_pools_max{name="G1-Old-Gen"}`                             | Gauge   | Bytes        |                                                                                                                                                                                                                         |
| `idm_jvm_memory_usage_pools_used{name="G1-Old-Gen"}`                            | Gauge   | Bytes        |                                                                                                                                                                                                                         |
| `idm_jvm_memory_usage_pools_used_after_gc{name="G1-Old-Gen"}`                   | Gauge   | Bytes        |                                                                                                                                                                                                                         |
| `idm_jvm_memory_usage_pools_committed{name="G1-Survivor-Space"}`                | Gauge   | Bytes        |                                                                                                                                                                                                                         |
| `idm_jvm_memory_usage_pools_init{name="G1-Survivor-Space"}`                     | Gauge   | Bytes        |                                                                                                                                                                                                                         |
| `idm_jvm_memory_usage_pools_max{name="G1-Survivor-Space"}`                      | Gauge   | Bytes        |                                                                                                                                                                                                                         |
| `idm_jvm_memory_usage_pools_used{name="G1-Survivor-Space"}`                     | Gauge   | Bytes        |                                                                                                                                                                                                                         |
| `idm_jvm_memory_usage_pools_used_after_gc{name="G1-Survivor-Space"}`            | Gauge   | Bytes        |                                                                                                                                                                                                                         |
| `idm_jvm_memory_usage_pools_committed{name="Metaspace"}`                        | Gauge   | Bytes        |                                                                                                                                                                                                                         |
| `idm_jvm_memory_usage_pools_init{name="Metaspace"}`                             | Gauge   | Bytes        |                                                                                                                                                                                                                         |
| `idm_jvm_memory_usage_pools_max{name="Metaspace"}`                              | Gauge   | Bytes        |                                                                                                                                                                                                                         |
| `idm_jvm_memory_usage_pools_used{name="Metaspace"}`                             | Gauge   | Bytes        |                                                                                                                                                                                                                         |
| `idm_jvm_thread_state{state="blocked"}`                                         | Gauge   | Count        | Learn more in [ThreadMXBean](https://docs.oracle.com/en/java/javase/21/docs/api/java.management/java/lang/management/ThreadMXBean.html).                                                                                |
| `idm_jvm_thread_state_daemon`                                                   | Gauge   | Count        | Number of live daemon threads.                                                                                                                                                                                          |
| `idm_jvm_thread_state{state="new"}`                                             | Gauge   | Count        | Number of threads in the `NEW` state.                                                                                                                                                                                   |
| `idm_jvm_thread_state{state="runnable"}`                                        | Gauge   | Count        | Number of threads in the `RUNNABLE` state.                                                                                                                                                                              |
| `idm_jvm_thread_state{state="terminated"}`                                      | Gauge   | Count        | Number of threads in the `TERMINATED` state.                                                                                                                                                                            |
| `idm_jvm_thread_state{state="timed_waiting"}`                                   | Gauge   | Count        | Number of threads in the `TIMED_WAITING` state.                                                                                                                                                                         |
| `idm_jvm_thread_state{state="waiting"}`                                         | Gauge   | Count        | Number of threads in the `WAITING` state.                                                                                                                                                                               |
| `idm_jvm_used_memory_bytes`                                                     | Gauge   | Bytes        | Learn more in [totalMemory()](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Runtime.html#totalMemory\(\)).                                                                                     |

|   |                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------- |
|   | [Deprecated](../release-notes/deprecated-functionality.html#deprecation-jvm-mem-usage-metrics) metrics are not shown in the previous table. |

## Prometheus scheduler metrics available in IDM

| Prometheus Metric Name                                                                        | Type    | Description                                                                                           |
| --------------------------------------------------------------------------------------------- | ------- | ----------------------------------------------------------------------------------------------------- |
| `idm_scheduler_job{job-group=job-group,job-name=job-name,activity=completed}`                 | Summary | A summary of completed jobs for the specified job-group and job-name.                                 |
| `idm_scheduler_job{job-group=job-group,job-name=job-name,activity=executed}`                  | Summary | Time spent on executed jobs for the specified job-group and job-name.                                 |
| `idm_scheduler_job_store_repo_seconds{operation=operation,scheduler_object=scheduler-object}` | Summary | Time spent storing scheduled jobs in the repository for the specified operation and scheduler-object. |
| `idm_scheduler_trigger{activity=acquired,result=success}`                                     | Summary | A summary of successfully acquired jobs.                                                              |
| `idm_scheduler_trigger{activity=acquired,result=timeout}`                                     | Summary | A summary of acquired jobs that time out.                                                             |
| `idm_scheduler_trigger{activity=fired}`                                                       | Summary | A summary of fired schedule triggers.                                                                 |
| `idm_scheduler_trigger{activity=misfired}`                                                    | Summary | A summary of misfired schedule triggers.                                                              |
| `idm_scheduler_trigger{activity=recovered}`                                                   | Summary | Time spent on recovered triggers.                                                                     |
| `idm_scheduler_seconds{operation=operation,type=type}`                                        | Summary | Execution rate of scheduler requests for the specified type and operation.                            |

## Prometheus workflow metrics available in IDM

| Prometheus Metric Name                                                    | Type    | Description                                                                 |
| ------------------------------------------------------------------------- | ------- | --------------------------------------------------------------------------- |
| `idm_workflow_execution_action_seconds{action="message"}`                 | Summary | Time spent invoking a message event.                                        |
| `idm_workflow_execution_action_seconds{action="signal"}`                  | Summary | Time spent invoking a signal event.                                         |
| `idm_workflow_execution_action_seconds{action="trigger"}`                 | Summary | Time spent triggering an execution.                                         |
| `idm_workflow_execution_query_seconds`                                    | Summary | Time spent querying executions.                                             |
| `idm_workflow_job_action_seconds{action="execute"}`                       | Summary | Time spent forcing synchronous execution of a job.                          |
| `idm_workflow_job_action_seconds{action="stacktrace"}`                    | Summary | Time spent displaying the stacktrace for a job that triggered an exception. |
| `idm_workflow_job_delete_seconds`                                         | Summary | Time spent deleting a job.                                                  |
| `idm_workflow_job_query_seconds`                                          | Summary | Time spent querying jobs.                                                   |
| `idm_workflow_job_read_seconds`                                           | Summary | Time spent reading a single job.                                            |
| `idm_workflow_jobdeadletter_action_seconds{action="execute"}`             | Summary | Time spent to execute dead-letter job.                                      |
| `idm_workflow_jobdeadletter_action_seconds{action="stacktrace"}`          | Summary | Time spent to retrieve the stacktrace for a dead-letter job.                |
| `idm_workflow_jobdeadletter_delete_seconds`                               | Summary | Time spent to delete a dead letter job.                                     |
| `idm_workflow_jobdeadletter_query_seconds`                                | Summary | Time spent to query dead letter jobs.                                       |
| `idm_workflow_jobdeadletter_read_seconds`                                 | Summary | Time spent to read a dead letter job.                                       |
| `idm_workflow_model_action_seconds{action="deploy"}`                      | Summary | Time spent to deploy a model.                                               |
| `idm_workflow_model_action_seconds{action="list_deployments"}`            | Summary | Time spent to list model deployments.                                       |
| `idm_workflow_model_action_seconds{action="validate_bpmn"}`               | Summary | Time spent to validate BPMN content.                                        |
| `idm_workflow_model_create_seconds`                                       | Summary | Time spent to create a model.                                               |
| `idm_workflow_model_delete_seconds`                                       | Summary | Time spent to delete a model.                                               |
| `idm_workflow_model_query_seconds`                                        | Summary | Time spent to query models.                                                 |
| `idm_workflow_model_read_seconds`                                         | Summary | Time spent to read a model.                                                 |
| `idm_workflow_model_update_seconds`                                       | Summary | Time spent to update a model.                                               |
| `idm_workflow_processdefinition_delete_seconds`                           | Summary | Time spent to delete a process definition.                                  |
| `idm_workflow_processdefinition_query_seconds`                            | Summary | Time spent to query process definitions.                                    |
| `idm_workflow_processdefinition_read_seconds`                             | Summary | Time spent to read a process definition.                                    |
| `idm_workflow_processinstance_action_seconds{action="migrate"}`           | Summary | Time spent to migrate a process instance.                                   |
| `idm_workflow_processinstance_action_seconds{action="validateMigration"}` | Summary | Time spent to validate a migration of a process instance.                   |
| `idm_workflow_processinstance_create_seconds`                             | Summary | Time spent to create a process instance.                                    |
| `idm_workflow_processinstance_delete_seconds`                             | Summary | Time spent to delete a process instance.                                    |
| `idm_workflow_processinstance_query_seconds`                              | Summary | Time spent to query process instances.                                      |
| `idm_workflow_processinstance_read_seconds`                               | Summary | Time spent to read a process instance.                                      |
| `idm_workflow_taskdefinition_query_seconds`                               | Summary | Time spent to query task definitions.                                       |
| `idm_workflow_taskdefinition_read_seconds`                                | Summary | Time spent to read a task definition.                                       |
| `idm_workflow_taskinstance_action_seconds{action="complete"}`             | Summary | Time spent to complete a task instance.                                     |
| `idm_workflow_taskinstance_query_seconds`                                 | Summary | Time spent to query task instances.                                         |
| `idm_workflow_taskinstance_read_seconds`                                  | Summary | Time spent to read a task instance.                                         |
| `idm_workflow_taskinstance_update_seconds`                                | Summary | Time spent to update a task instance.                                       |

***

[1](#_footnoteref_1). This summary metric doesn't include the quantile grouping and only has the metric\_name\_count and metric\_name\_total entries.[2](#_footnoteref_2). The idm\_router\_filter\_seconds metric name replaces the "filter" name. This metric can specify a "name" and "system" label. If no "name" label is specified, it defaults to "unknown". The "system" label is always system="false".[3](#_footnoteref_3). The deprecated metric names are still available and are generated along with the new metric names unless "deprecatedMetricsEnabled" is set to "false" in "conf/metrics.json".[4](#_footnoteref_4). A pending request gauge won't register until the associated RequestType has been invoked at least one time.[5](#_footnoteref_5). This metric naming convention replaces idm\_managed\_seconds{managed\_object="managed\_object",operation="operation\_name",script="script\_name"} and includes optional "object" and "script\_hook" labels.[6](#_footnoteref_6). Each virtual property is listed in both the label name and value. For example: effectiveAssignments\_effectiveRoles="effectiveAssignments,effectiveRoles"[7](#_footnoteref_7). The relationship resource path is used as both the label name and value. For example: managed\_user\_roles="managed\_user.roles"[8](#_footnoteref_8). The QoSHandler metric, idm\_jetty\_qos\_queue\_count, accurately contains the number of queued requests in the handler queue and replaces the idm\_jetty\_thread\_queue metric.

---

---
title: Server logs
description: Configure PingIDM server logs using logback, including file, console, and OpenTelemetry appenders, log encoders, and log levels
component: pingidm
version: 8.1
page_id: pingidm:monitoring-guide:server-logs
canonical_url: https://docs.pingidentity.com/pingidm/8.1/monitoring-guide/server-logs.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Monitoring", "JSON", "Configuration", "Logs"]
section_ids:
  log-appenders: Log appenders
  log-appender-settings: Log appender settings
  logging-file-appender: Configuring RollingFileAppender
  logging-console-appender: Configuring ConsoleAppender
  logging-opentelemetry-appender: Configuring OpenTelemetryAppender
  log-message-format: Log encoders
  log-levels: Log levels
---

# Server logs

IDM uses [logback](https://logback.qos.ch/manual/introduction.html) to generate server logs.

|   |                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Before 8.0, IDM used `java.util.logging` (JUL) to generate its logs. Learn more about producing logs in the older format in [PatternLayoutEncoder](#pattern-layout-encoder) and [Configuring `ConsoleAppender`](#logging-console-appender). |

Server logging isn't the same as [the audit service](../audit-guide/audit.html). The audit service logs activity on the IDM system, such as access and synchronization. Server logging records information about the internal workings of IDM, such as system messages, error reporting, service loading, and startup and shutdown messaging.

The default location for the server logging configuration file is your project's `conf/logback.xml` file. You can configure this location by setting the `LOGGING_CONFIG` environment variable in your project's `startup.sh` file.

Changes to logging settings take effect without restarting the server. You can configure the interval at which the system scans for updates using the following tag:

```xml
<configuration scan="true" scanPeriod="30 seconds">
```

You can specify a global [logging level](#log-levels):

```xml
<root level="INFO">
    <appender-ref ref="console" />
    <appender-ref ref="file" />
</root>
```

## Log appenders

IDM logs messages using `<appender>` tags in the `logback.xml` file. The three default appenders are:

* [`RollingFileAppender`](#logging-file-appender) writes formatted log records to a single file or to a set of rotating log files. By default, log files are written to `logs/openidm*.log` files. Rotated files will have a date within the file name, such as `openidm-2025-03-11.log`.

* [`ConsoleAppender`](#logging-console-appender) writes formatted logs to `System.out`.

* [`OpenTelemetryAppender`](#logging-opentelemetry-appender) writes formatted JSON logs to an [OpenTelemetry collector](https://opentelemetry.io/docs/collector/) using the [OpenTelemetry Protocol (OTLP)](https://github.com/open-telemetry/opentelemetry-proto/tree/main/docs).

Additional log message handlers are listed in the `logback.xml` file.

### Log appender settings

You can configure logback appender settings in the `conf/logback.xml` file. For example:

```xml
<appender name="OpenTelemetry" class="io.opentelemetry.instrumentation.logback.appender.v1_0.OpenTelemetryAppender">
  <captureExperimentalAttributes>true</captureExperimentalAttributes>
  <captureMdcAttributes>*</captureMdcAttributes>
</appender>
```

The available settings are:

| Appender setting                     | Type    | Default | Description                                                                                                                                                                                                                                            |
| ------------------------------------ | ------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `captureExperimentalAttributes`      | Boolean | false   | Enables the capture of experimental log attributes `thread.name` and `thread.id`.                                                                                                                                                                      |
| `captureCodeAttributes`              | Boolean | false   | Enables the capture of source code attributes.  &#xA;&#xA;Capturing source code attributes at logging sites might add a performance overhead.                                                                                                          |
| `captureMarkerAttribute`             | Boolean | false   | Enables the capture of Logback markers as attributes.                                                                                                                                                                                                  |
| `captureKeyValuePairAttributes`      | Boolean | false   | Enables the capture of Logback key-value pairs as attributes.                                                                                                                                                                                          |
| `captureLoggerContext`               | Boolean | false   | Enables the capture of Logback logger context properties as attributes.                                                                                                                                                                                |
| `captureArguments`                   | Boolean | false   | Enables the capture of Logback logger arguments.                                                                                                                                                                                                       |
| `captureLogstashMarkerAttributes`    | Boolean | false   | Enables the capture of Logstash markers, supported are those added to logs using `Markers.append()`, `Markers.appendEntries()`, `Markers.appendArray()`, and `Markers.appendRaw()` methods.                                                            |
| `captureLogstashStructuredArguments` | Boolean | false   | Enables the capture of Logstash `StructuredArguments` as attributes, such as `StructuredArguments.v()` and `StructuredArguments.keyValue()`.                                                                                                           |
| `captureMdcAttributes`               | String  |         | Comma-separated list of Mapped Diagnostic Context (MDC) attributes to capture. Use the wildcard character `*` to capture all attributes.                                                                                                               |
| `captureEventName`                   | Boolean | false   | Enables moving the `event.name` attribute, which is captured by one of the other mechanisms that captures attributes, to the log event name.                                                                                                           |
| `numLogsCapturedBeforeOtelInstall`   | Integer | 1000    | Log telemetry is emitted after the initialization of the OpenTelemetry Logback appender with an OpenTelemetry object. This setting allows you to modify the size of the cache used to replay the first logs. The `thread.id` attribute isn't captured. |

### Configuring `RollingFileAppender`

The rolling file appender writes formatted log records to a single file or to a set of rotating log files. To configure it, you might need to:

1. Update the `<file>` tag to contain the path to your default log file.

2. Set the `ThresholdFilter` to the minimum log level for your appender.

3. Enable or disable the `logger.LogbackLogFilter`.

4. Configure the `<RollingPolicy>`.

5. Specify the `<encoder>`.

The file appender supports the following configuration tags:

* \<file>

  Contains the path for the default log file, for example:

  ```xml
  <file>path/to/openidm/logs/logback.log</file>
  ```

* \<filter>

  Filters log events. Use `class="ThresholdFilter"` and the `<level>` tag to configure the [log level](#log-levels). This should be the minimum log level for your appender, for example:

  ```xml
  <filter class="ThresholdFilter">
      <level>TRACE</level>
  </filter>
  ```

  Use `class="org.forgerock.openidm.logger.LogbackLogFilter"` to filter some common "noise" from the logs, for example:

  ```xml
  <filter class="org.forgerock.openidm.logger.LogbackLogFilter" />
  ```

- \<rollingPolicy>

  Controls the system's behavior during log rotation. By default, this is `TimeBasedRollingPolicy` with a daily rolling option. `SizeAndTimeBasedRollingPolicy` is also supported, though you should only use it in cases where performance isn't a concern.

  Learn more about rolling policies in the [logback documentation](https://logback.qos.ch/manual/appenders.html#RollingFileAppender).

- \<encoder>

  Controls the system's [log message format](#log-message-format). By default, this is `JsonEncoder`, though `PatternLayoutEncoder` is also supported.

  Learn more about encoders in the [logback documentation](https://logback.qos.ch/manual/encoders.html).

### Configuring `ConsoleAppender`

`ConsoleAppender` writes formatted logs to `System.out`. To configure it, you might need to:

1. Set the `ThresholdFilter` to the minimum required logging level.

2. Enable or disable the `logger.LogbackLogFilter`.

3. Specify the `<encoder>`.

The console appender has the following tags:

* \<filter>

  Filters log events. Use `class="ThresholdFilter"` and the `<level>` tag to configure the logging level, for example:

  ```xml
  <filter class="ThresholdFilter">
      <level>TRACE</level>
  </filter>
  ```

  Use `class="org.forgerock.openidm.logger.LogbackLogFilter"` to filter some common "noisy" entries from the logs, for example:

  ```xml
  <filter class="org.forgerock.openidm.logger.LogbackLogFilter" />
  ```

* \<encoder>

  Controls the system's [log message format](#log-message-format). By default, this is `JsonEncoder`.

  Learn more about encoders in the [logback documentation](https://logback.qos.ch/manual/encoders.html).

### Configuring `OpenTelemetryAppender`

|   |                                                                                                                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | [OpenTelemetry (OTEL)](https://opentelemetry.io/docs/what-is-opentelemetry/) logging is an [Evolving](../release-notes/appendix-interface-stability.html) feature in PingIDM. It's subject to change without notice, even in a minor or maintenance release. |

The `OpenTelemetryAppender` writes formatted JSON logs to an OTEL collector using the OTLP protocol. This appender uses the class `logback.appender.v1_0.OpenTelemetryAppender`.

To configure the `OpenTelemetryAppender`:

1. In the `conf/logback.xml` file, uncomment the following appender class and settings:

   ```xml
   <!--
   <appender name="OpenTelemetry" class="io.opentelemetry.instrumentation.logback.appender.v1_0.OpenTelemetryAppender">
       <captureExperimentalAttributes>true</captureExperimentalAttributes>
       <captureKeyValuePairAttributes>true</captureKeyValuePairAttributes>
       <captureLoggerContext>true</captureLoggerContext>
       <captureMdcAttributes>*</captureMdcAttributes>
       <numLogsCapturedBeforeOtelInstall>1000</numLogsCapturedBeforeOtelInstall>
    </appender>
   -->
   ```

2. In the appender `root` tag, uncomment the `"OpenTelemetry"` call:

   ```xml
   <!--
   Default root logging level.
   This specifies which kinds of events are logged across all loggers.
   For any given facility this root level can be overridden by a facility specific level.
   Note that the ConsoleHandler also has a separate level setting to limit messages printed to the console.
   Loggers and Handlers may override this level.
   -->

   <root level="INFO">
       <appender-ref ref="console" />
       <appender-ref ref="file" />
       <appender-ref ref="OpenTelemetry" /> (1)
   </root>
   ```

   |       |                                                                                    |
   | ----- | ---------------------------------------------------------------------------------- |
   | **1** | Uncomment the "OpenTelemetry" call . The appender is now available on IDM startup. |

3. Optionally, to view more OTEL log output, change the [log level](#log-levels) to `"DEBUG"`:

   ```xml
   <root level="DEBUG">
   ```

Learn more about [OpenTelemetry logging](opentelemetry-logging.html) and [Distributed tracing](distributed-tracing.html).

## Log encoders

IDM supports two log encoders:

* `JsonEncoder` outputs logs as a JSON object. This is the default and recommended encoder for most purposes.

  Example JSON output

  ```json
  {
    "timestamp": 1738355903784,
    "level": "DEBUG",
    "threadName": "persisted_1738355821854_QuartzSchedulerThread",
    "loggerName": "org.forgerock.openidm.quartz.RepoJobStore",
    "context": {
      "name": "default",
      "birthdate": 1738355793181,
      "properties": {}
    },
    "mdc": {},
    "formattedMessage": "Processing 0 deferred Trigger Job Completions",
    "throwable": null
  }
  ```

  Learn more about `JsonEncoder` in the [logback documentation](https://logback.qos.ch/manual/encoders.html#JsonEncoder).

- `PatternLayoutEncoder` outputs a text log file which emulates the `java.util.logging` format. Enabling this option will generate logs in the same format as past versions of IDM. To enable, replace the `JsonEncoder` with the `PatternLayoutEncoder` provided in the code comments of `conf/logback.xml`.

  Example Pattern Layout output

  ```
  [19] May 23, 2018 10:30:26.959 AM org.forgerock.openidm.repo.opendj.impl.Activator start
  INFO: Registered bootstrap repository service
  [19] May 23, 2018 10:30:26.960 AM org.forgerock.openidm.repo.opendj.impl.Activator start
  INFO: DS bundle started
  ```

  Learn more about `PatternLayoutEncoder` in the [logback documentation](https://logback.qos.ch/manual/encoders.html#PatternLayoutEncoder).

## Log levels

Logging levels are controlled by `<filter class="ThresholdFilter">` tags contained within an `<appender>` tag in `conf/logback.xml`. For example, this tag filters events with a level below DEBUG:

```xml
<filter class="ThresholdFilter">
    <level>DEBUG</level>
</filter>
```

The following table lists the supported threshold filter values in descending order from most to least general and includes the equivalent level in the previously supported `java.util.logging`:

**Threshold filter concordance**

| Logback threshold | java.util.logging threshold |
| ----------------- | --------------------------- |
| ERROR             | SEVERE                      |
| WARN              | WARNING                     |
| INFO              | INFO                        |
| DEBUG             | FINE                        |
| DEBUG             | FINER                       |
| TRACE             | FINEST                      |

Set the threshold value to `OFF` to disable logging.

Learn more about threshold values in the [logback documentation](https://logback.qos.ch/manual/architecture.html#basic_selection).

You can specify different logging levels for individual server features which override the global logging level. For example:

```xml
<!-- Commons api.models and OpenApiTransformer (API Descriptor) is noisy at INFO level -->
<logger name="org.forgerock.api.models" level="WARN" />
<logger name="org.forgerock.api.transform.OpenApiTransformer" level="WARN" />
<!-- Logs the output from OSGi logging -->
<logger name="org.forgerock.openidm.Framework" level="WARN" />
<!-- On restart the BarURLHandler can create warning noise -->
<logger name="org.activiti.osgi.BarURLHandler" level="ERROR" />
```

If you use logger functions in your JavaScript scripts, set the log level for the scripts as follows:

```xml
<logger name="org.forgerock.openidm.script.javascript.JavaScript" level="level" />
```

You can override the log level settings, per script, with the following setting:

```xml
<logger name="org.forgerock.openidm.script.javascript.JavaScript.script-name" level="level" />
```