---
title: Alerts
description: Configure PingDS alert notifications over JMX or email, and review the full list of server alert types.
component: pingds
version: 8.1
page_id: pingds:monitoring-guide:alert-notifications
canonical_url: https://docs.pingidentity.com/pingds/8.1/monitoring-guide/alert-notifications.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Monitoring", "Troubleshooting"]
section_ids:
  jmx_alerts: JMX alerts
  mail_alerts: Mail alerts
  alert-types: Alert types
---

# Alerts

DS servers can send alerts for significant server events.

## JMX alerts

The following example enables JMX alert notifications:

```console
$ dsconfig \
 set-alert-handler-prop \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --handler-name "JMX Alert Handler" \
 --set enabled:true \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
```

## Mail alerts

The following example sets up an SMTP server, and configures email alerts:

```console
$ dsconfig \
 create-mail-server \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --server-name "SMTP server" \
 --set enabled:true \
 --set auth-username:mail.user \
 --set auth-password:password \
 --set smtp-server:smtp.example.com:587 \
 --set trust-manager-provider:"JVM Trust Manager" \
 --set use-start-tls:true \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
$ dsconfig \
 create-alert-handler \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --handler-name "SMTP Alert Handler" \
 --type smtp \
 --set enabled:true \
 --set message-subject:"DS Alert, Type: %%alert-type%%, ID: %%alert-id%%" \
 --set message-body:"%%alert-message%%" \
 --set recipient-address:kvaughan@example.com \
 --set sender-address:ds@example.com \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
```

## Alert types

DS servers use the following alert types. For alert types that indicate server problems, check `logs/errors` for details:

* `org.opends.server.AccessControlDisabled`

  The access control handler has been disabled.

* `org.opends.server.AccessControlEnabled`

  The access control handler has been enabled.

* `org.opends.server.authentiation.dseecompat.ACIParseFailed`

  The dseecompat access control subsystem failed to correctly parse one or more access control instruction (ACI) *(tooltip: \<div class="paragraph">
  \<p>An instruction or rule that can be used to grant or deny access to users to perform operations on a server.\</p>
  \</div>)* rules when the server first started.

* `org.opends.server.BackupFailure`

  A backup has failed.

* `org.opends.server.BackupSuccess`

  A backup has completed successfully.

* `org.opends.server.CannotCopySchemaFiles`

  A problem has occurred while attempting to create copies of the existing schema configuration files before making a schema update, and the schema configuration has been left in a potentially inconsistent state.

* `org.opends.server.CannotRenameCurrentTaskFile`

  The server is unable to rename the current tasks backing file in the process of trying to write an updated version.

* `org.opends.server.CannotRenameNewTaskFile`

  The server is unable to rename the new tasks backing file into place.

* `org.opends.server.CannotScheduleRecurringIteration`

  The server is unable to schedule an iteration of a recurring task.

* `org.opends.server.CannotWriteConfig`

  The server is unable to write its updated configuration for some reason and therefore the server may not exhibit the new configuration if it is restarted.

* `org.opends.server.CannotWriteNewSchemaFiles`

  A problem has occurred while attempting to write new versions of the server schema configuration files, and the schema configuration has been left in a potentially inconsistent state.

* `org.opends.server.CannotWriteTaskFile`

  The server is unable to write an updated tasks backing file for some reason.

* `org.opends.server.DirectoryServerShutdown`

  The server has begun the process of shutting down.

* `org.opends.server.DirectoryServerStarted`

  The server has completed its startup process.

* `org.opends.server.DiskFull`

  Free disk space has reached the full threshold.

  Default is 6% of the size of the file system.

* `org.opends.server.DiskSpaceLow`

  Free disk space has reached the low threshold.

  Default is 10% of the size of the file system.

* `org.opends.server.EnteringLockdownMode`

  The server is entering lockdown mode, wherein only root users are allowed to perform operations and only over the loopback address.

* `org.opends.server.LDAPHandlerDisabledByConsecutiveFailures`

  Consecutive failures have occurred in the LDAP connection handler and have caused it to become disabled.

* `org.opends.server.LDAPHandlerUncaughtError`

  Uncaught errors in the LDAP connection handler have caused it to become disabled.

* `org.opends.server.LDIFBackendCannotWriteUpdate`

  An LDIF backend was unable to store an updated copy of the LDIF file after processing a write operation.

* `org.opends.server.LDIFConnectionHandlerIOError`

  The LDIF connection handler encountered an I/O error that prevented it from completing its processing.

* `org.opends.server.LDIFConnectionHandlerParseError`

  The LDIF connection handler encountered an unrecoverable error while attempting to parse an LDIF file.

* `org.opends.server.LeavingLockdownMode`

  The server is leaving lockdown mode.

* `org.opends.server.ManualConfigEditHandled`

  The server detects that its configuration has been manually edited with the server online, and those changes were overwritten by another change made through the server. The manually edited configuration will be copied to another location.

* `org.opends.server.ManualConfigEditLost`

  The server detects that its configuration has been manually edited with the server online, and those changes were overwritten by another change made through the server. The manually edited configuration could not be preserved due to an unexpected error.

* `org.opends.server.replication.UnresolvedConflict`

  Multimaster replication cannot resolve a conflict automatically.

* `org.opends.server.UncaughtException`

  A server thread has encountered an uncaught exception that caused that thread to terminate abnormally. The impact that this problem has on the server depends on which thread was impacted and the nature of the exception.

* `org.opends.server.UniqueAttributeSynchronizationConflict`

  A unique attribute conflict has been detected during synchronization processing.

* `org.opends.server.UniqueAttributeSynchronizationError`

  An error occurred while attempting to perform unique attribute conflict detection during synchronization processing.

---

---
title: Distributed tracing with OpenTelemetry
description: Learn how to use distributed tracing to troubleshoot and optimize PingDS.
component: pingds
version: 8.1
page_id: pingds:monitoring-guide:opentelemetry
canonical_url: https://docs.pingidentity.com/pingds/8.1/monitoring-guide/opentelemetry.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-02-03T12:06:24Z
keywords: ["Monitoring"]
section_ids:
  why_use_distributed_tracing: Why use distributed tracing?
  what_is_distributed_tracing: What is distributed tracing?
  which_requests_are_traced: Which requests are traced?
  enable_and_configure_tracing: Enable and configure tracing
  how_to_view_traces: How to view traces
---

# Distributed tracing with OpenTelemetry

In a distributed system, requests pass through multiple services hosted on multiple servers. Without telemetry data, it can be difficult to identify the root cause of performance issues or errors.

Distributed tracing provides visibility into the full path a request takes through a distributed system. DS supports the [OpenTelemetry framework](https://opentelemetry.io/docs/what-is-opentelemetry/) for collecting distributed tracing data. You can send traces collected by DS to a backend service, such as [Jaeger](https://www.jaegertracing.io/), for aggregation, storage, and visualization.

|   |                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The interface stability for OpenTelemetry support is *Evolving*.The plugin configuration, the content of spans, the span name, and the span attributes are all subject to change without prior notice. |

## Why use distributed tracing?

Diagnosing escalated production issues can take hours to days, involving multiple subject-matter experts trying to correlate fragmented logs and understand what happened, often yielding a lot of noise and little clarity. The more services and instances involved, the more challenging troubleshooting becomes.

Distributed tracing addresses these challenges by supporting end-to-end request visibility and data correlation across multiple services and servers. As a result, you can troubleshoot performance issues and errors more quickly and effectively. You can also use distributed tracing to optimize system performance by identifying bottlenecks and inefficiencies in service interactions.

## What is distributed tracing?

Distributed tracing shows you how an incoming request was processed across all servers and services in a distributed system, including:

* Which servers and services the request went through.

* How much time each service took to process its part of the request.

* How the services are connected.

* What the failure point was in case of a request failure.

A distributed trace provides a visual representation of a request's path through the system. Spans show when an operation started, when it ended, and its duration. When one service calls another, these calls are linked within the trace, showing the flow and time spent in each service. The DS server uses the OpenTelemetry framework to create and manage these spans and traces.

* Traces

  A trace represents the path of a request through an application. A trace is made up of one or more spans. Learn more about traces in the [OpenTelemetry documentation](https://opentelemetry.io/docs/concepts/signals/traces/).

* Spans

  A span is a segment of a request's path through the system. It represents a unit of work or an operation within a service. Each span includes the following elements:

  * `traceId` represents the trace that the span is a part of.

  * `spanId` is a unique ID for the span.

  * `parentSpanId` is the ID of the originating request.

  Servers add span attributes following the [semantic conventions](https://opentelemetry.io/docs/specs/semconv/general/attributes/), with LDAP-specific attributes based on [HTTP conventions](https://opentelemetry.io/docs/specs/semconv/http/http-spans/).

* Root span

  The root span indicates the start and end of an entire operation. The `parentSpanId` of the root span is null because the root span isn't part of an existing trace. Subsequent spans in the trace have their own unique `spanId`. Their `traceId` is the same as that of the root span, and their `parentSpanId` matches the `spanId` of the root span.

* OpenTelemetry

  OpenTelemetry is an open-source observability framework for instrumenting, generating, collecting, and exporting telemetry data. It provides a standardized way to capture distributed traces across different services and platforms. It doesn't provide a backend for storing or analyzing telemetry data. Learn more in the [OpenTelemetry documentation](https://opentelemetry.io/docs/what-is-opentelemetry/).

## Which requests are traced?

All incoming LDAP requests are supported. Requests must include the [W3C trace context LDAP request control](https://www.w3.org/TR/trace-context/) to propagate trace information.

The W3C trace context allows for consistent correlation IDs and metadata across systems that support the W3C standard. If a request doesn't include the W3C trace context control, a new trace starts for that request.

## Enable and configure tracing

Distributed tracing is disabled by default. To enable the feature, enable the OpenTelemetry plugin, making sure it targets the endpoint for the service. You can limit what the plugin pushes using additional settings.

The following example enables the plugin. It pushes all traces to the default endpoint, `http://localhost:4318/v1/traces`. It samples all the spans, which is the default behavior. Adapt the configuration as necessary for your production deployment:

```console
$ dsconfig \
 set-plugin-prop \
 --plugin-name OpenTelemetry \
 --set enabled:true \
 --set tracer-sampler:always-on \
 --set tracer-exporter-otlp-endpoint:http://localhost:4318/v1/traces \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
```

Learn about all the optional plugin settings in the [OpenTelemetry Plugin](../configref/objects-open-telemetry-plugin.html) reference.

## How to view traces

DS can push traces to an [OpenTelemetry Protocol (OTLP)](https://opentelemetry.io/docs/specs/otel/protocol/) endpoint over HTTP. Any backend that supports OTLP/HTTP can be used to collect and visualize the traces.

|   |                                                                                                                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Try the [Jaeger tracing All-in-one Docker image](https://www.jaegertracing.io/docs/latest/getting-started/) to capture exported spans. By default, Jaeger stores the spans in memory, but you can configure Jaeger to send the spans to various persistent datastores external to the Docker image. |

---

---
title: HTTP-based monitoring
description: Monitor PingDS servers over HTTP using the alive, healthy, and Prometheus metrics endpoints.
component: pingds
version: 8.1
page_id: pingds:monitoring-guide:http-monitoring
canonical_url: https://docs.pingidentity.com/pingds/8.1/monitoring-guide/http-monitoring.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-02-09T09:34:08Z
keywords: ["Monitoring", "REST API", "Troubleshooting"]
section_ids:
  basic_availability: Basic availability
  monitoring-liveness-http: Server is alive (HTTP)
  monitoring-health-http: Server health (HTTP)
  monitoring-health-status-prometheus: Server health (Prometheus)
  monitoring-disk-space: Disk space (Prometheus)
  monitoring-certificate-expiration: Certificate expiration (Prometheus)
  activity: Activity
  monitoring-activity-http: Active users (Prometheus)
  monitoring-operation-stats-http: Request statistics (Prometheus)
  monitoring-work-queue-http: Work queue (Prometheus)
  counts: Counts
  monitoring-acis-http: ACIs (Prometheus)
  monitoring-entry-counts-http: Database size (Prometheus)
  monitoring-entry-cache-http: Entry caches (Prometheus)
  monitoring-groups-http: Groups (Prometheus)
  monitoring-subentries-http: Subentries (Prometheus)
  indexing: Indexing
  monitoring-index-cost-http: Index cost (Prometheus)
  monitoring-index-reads-http: Index use (Prometheus)
  monitoring-replication-http: Replication
  monitoring-replication-delay-http: Replication delay (Prometheus)
  monitoring-replication-status-http: Replication status (Prometheus)
  monitoring-filters-http: Filtering results (Prometheus)
---

# HTTP-based monitoring

|   |                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This page covers the HTTP interfaces for monitoring DS servers. For the same capabilities over LDAP, refer to [LDAP-based monitoring](ldap-monitoring.html). |

DS servers publish monitoring information at these HTTP endpoints:

* `/alive`

  Whether the server is currently *alive*, meaning its internal checks have not found any errors that would require administrative action.

* `/healthy`

  Whether the server is currently *healthy*, meaning it's alive, the replication server is accepting connections on the configured port, and any replication delays are below the configured threshold.

* `/metrics/prometheus/0.0.4`

  Monitoring information in [Prometheus monitoring software](https://prometheus.io/) format. For details, refer to [Prometheus metrics reference](monitoring-metrics-prometheus.html).

  The following example command accesses the Prometheus endpoint:

  ```console
  $ curl \
  --cacert ca-cert.pem \
  --user monitor:password \
  https://localhost:8443/metrics/prometheus/0.0.4
  ```

To give a regular user privileges to read monitoring data, refer to [Monitor privilege](ldap-monitoring.html#monitoring-read-privilege).

## Basic availability

### Server is alive (HTTP)

The following example reads the `/alive` endpoint anonymously. If the DS server's internal tests do not find errors that require administrative action, then it returns HTTP 200 OK:

```console
$ curl --cacert ca-cert.pem --head https://localhost:8443/alive
```

> **Collapse: Show output**
>
> ```
> HTTP/1.1 200 OK
> ...
> ```

If the server finds that it is subject to errors requiring administrative action, it returns HTTP 503 Service Unavailable.

If there are errors, anonymous users receive only the 503 error status. Error strings for diagnosis are returned as an array of `"alive-errors"` in the response body, but the response body is only returned to a user with the `monitor-read` privilege.

When a server returns `"alive-errors"`, diagnose and fix the problem, and then either restart or replace the server.

### Server health (HTTP)

The following example reads the `/healthy` endpoint anonymously. If the DS server is alive, as described in [Server is alive (HTTP)](#monitoring-liveness-http), any replication listener threads are functioning normally, and any replication delay is below the threshold configured as `max-replication-delay-health-check` (default: 5 seconds), then it returns HTTP 200 OK:

```console
$ curl --cacert ca-cert.pem --head https://localhost:8443/healthy
```

> **Collapse: Show output**
>
> ```
> HTTP/1.1 200 OK
> ...
> ```

If the server is subject to a replication delay above the threshold, then it returns HTTP 503 Service Unavailable. This result only indicates a problem if the replication delay is steadily high and increasing for the long term.

If there are errors, anonymous users receive only the 503 error status. Error strings for diagnosis are returned as an array of `"ready-errors"` in the response body, but the response body is only returned to a user with the `monitor-read` privilege.

When a server returns `"ready-errors"`, route traffic to another server until the current server is ready again.

### Server health (Prometheus)

In addition to the examples above, you can monitor whether a server is alive and able to handle requests as Prometheus metrics:

```console
$ curl \
--cacert ca-cert.pem \
--user monitor:password \
https://localhost:8443/metrics/prometheus/0.0.4 2>/dev/null | grep health_status
```

> **Collapse: Show output**
>
> ```
> # HELP ds_health_status_alive Indicates whether the server is alive
> # TYPE ds_health_status_alive gauge
> ds_health_status_alive 1.0
> # HELP ds_health_status_healthy Indicates whether the server is able to handle requests
> # TYPE ds_health_status_healthy gauge
> ds_health_status_healthy 1.0
> ```

### Disk space (Prometheus)

The following example shows monitoring metrics you can use to check whether the server is running out of disk space:

```console
$ curl \
--cacert ca-cert.pem \
--user monitor:password \
https://localhost:8443/metrics/prometheus/0.0.4 2>/dev/null | grep disk
```

> **Collapse: Show output**
>
> ```
> # HELP ds_disk_free_space_bytes The amount of free disk space (in bytes)
> # TYPE ds_disk_free_space_bytes gauge
> ds_disk_free_space_bytes{disk="<partition>",} <bytes>
> # HELP ds_disk_free_space_full_threshold_bytes The effective full disk space threshold (in bytes)
> # TYPE ds_disk_free_space_full_threshold_bytes gauge
> ds_disk_free_space_full_threshold_bytes{disk="<partition>",} <bytes>
> # HELP ds_disk_free_space_low_threshold_bytes The effective low disk space threshold (in bytes)
> # TYPE ds_disk_free_space_low_threshold_bytes gauge
> ds_disk_free_space_low_threshold_bytes{disk="<partition>",} <bytes>
> ```

In your monitoring software, compare free space with the disk low and disk full thresholds. For database backends, these thresholds are set using the configuration properties: [disk-low-threshold](../configref/objects-je-backend.html#disk-low-threshold) and [disk-full-threshold](../configref/objects-je-backend.html#disk-full-threshold).

When you read from `cn=monitor` instead ,as described in [LDAP-based monitoring](ldap-monitoring.html), the relevant data are exposed on child entries of `cn=disk space monitor,cn=monitor`.

### Certificate expiration (Prometheus)

The following example shows how you can use monitoring metrics to check whether the server certificate is due to expire soon:

```console
$ curl \
--cacert ca-cert.pem \
--user monitor:password \
https://localhost:8443/metrics/prometheus/0.0.4 2>/dev/null | grep cert
```

> **Collapse: Show output**
>
> ```
> # HELP ds_certificates_certificate_expires_at_seconds Certificate expiration date and time
> # TYPE ds_certificates_certificate_expires_at_seconds gauge
> ds_certificates_certificate_expires_at_seconds{alias="ssl-key-pair",key_manager="PKCS12",} <sec_since_epoch>
> ```

In your monitoring software, compare the expiration date with the current date.

When you read from `cn=monitor` instead, as described in [LDAP-based monitoring](ldap-monitoring.html), the relevant data are exposed on child entries of `cn=certificates,cn=monitor`.

## Activity

### Active users (Prometheus)

DS server connection handlers respond to client requests. The following example uses the default monitor user account to read active connections on each connection handler:

```console
$ curl \
--cacert ca-cert.pem \
--user monitor:password \
https://localhost:8443/metrics/prometheus/0.0.4 2>/dev/null | grep "active_[cp]"
```

### Request statistics (Prometheus)

DS server connection handlers respond to client requests. The following example uses the default monitor user account to read statistics about client operations on each of the available connection handlers:

```console
$ curl \
--cacert ca-cert.pem \
--user monitor:password \
https://localhost:8443/metrics/prometheus/0.0.4 2>/dev/null | grep connection_handlers
```

### Work queue (Prometheus)

DS servers have a work queue to track request processing by worker threads, and whether the server has rejected any requests due to a full queue. If enough worker threads are available, then no requests are rejected. The following example uses the default monitor user account to read statistics about the work queue:

```console
$ curl \
--cacert ca-cert.pem \
--user monitor:password \
https://localhost:8443/metrics/prometheus/0.0.4 2>/dev/null | grep work_queue
```

To adjust the number of worker threads, refer to the settings for [Traditional Work Queue](../configref/objects-traditional-work-queue.html).

## Counts

### ACIs (Prometheus)

DS maintains counts of ACIs *(tooltip: \<div class="paragraph">
\<p>An instruction or rule that can be used to grant or deny access to users to perform operations on a server.\</p>
\</div>)*:

```console
$ curl \
--cacert ca-cert.pem \
--user monitor:password \
https://localhost:8443/metrics/prometheus/0.0.4 2>/dev/null | grep _aci
```

### Database size (Prometheus)

DS servers maintain counts of the number of entries in each backend. The following example uses the default monitor user account to read the counts:

```console
$ curl \
--cacert ca-cert.pem \
--user monitor:password \
https://localhost:8443/metrics/prometheus/0.0.4 2>/dev/null | grep backend_entry_count
```

### Entry caches (Prometheus)

DS servers maintain entry cache statistics:

```console
$ curl \
--cacert ca-cert.pem \
--user monitor:password \
https://localhost:8443/metrics/prometheus/0.0.4 2>/dev/null | grep entry_cache
```

### Groups (Prometheus)

The following example reads counts of static, dynamic, and virtual static groups, and statistics on the distribution of static group size:

```console
$ curl \
--cacert ca-cert.pem \
--user monitor:password \
https://localhost:8443/metrics/prometheus/0.0.4 2>/dev/null | grep -i group
```

At startup time, DS servers log a message showing the number of different types of groups and the memory allocated to cache static groups.

### Subentries (Prometheus)

DS maintains counts of LDAP subentries:

```console
$ curl \
--cacert ca-cert.pem \
--user monitor:password \
https://localhost:8443/metrics/prometheus/0.0.4 2>/dev/null | grep subentries
```

## Indexing

### Index cost (Prometheus)

DS maintains metrics about index cost. The metrics count the number of updates and how long they took since the DS server started.

The following example demonstrates how to read the metrics for all monitored indexes:

```console
$ curl \
--cacert ca-cert.pem \
--user monitor:password \
https://localhost:8443/metrics/prometheus/0.0.4 2>/dev/null | grep index_cost
```

### Index use (Prometheus)

DS maintains metrics about index use. The metrics indicate how often an index was accessed since the DS server started.

The following example demonstrates how to read the metrics for all monitored indexes:

```console
$ curl \
--cacert ca-cert.pem \
--user monitor:password \
https://localhost:8443/metrics/prometheus/0.0.4 2>/dev/null | grep index_uses
```

## Replication

Monitor the following to ensure replication runs smoothly. Take action as described in these sections and in the troubleshooting documentation for [replication problems](../maintenance-guide/troubleshooting.html#troubleshoot-repl).

### Replication delay (Prometheus)

The following example reads a metric to check the delay in replication:

```console
$ curl \
--cacert ca-cert.pem \
--user monitor:password \
https://localhost:8443/metrics/prometheus/0.0.4 2>/dev/null | grep receive_delay
```

> **Collapse: Show output**
>
> ```
> # HELP ds_replication_replica_remote_replicas_receive_delay_seconds Current local delay in receiving replicated operations
> # TYPE ds_replication_replica_remote_replicas_receive_delay_seconds gauge
> ds_replication_replica_remote_replicas_receive_delay_seconds{<labels>} <delay>
> ```

DS replicas measure replication delay as the local delay when receiving and replaying changes. There are two parts to replication delay: *receive delay* and *replay delay*. To understand what's causing replication delay, you must determine which part is responsible for the delay.

A replica calculates these local delays based on changes received from other replicas. Therefore, a replica can only calculate delays based on changes it has received. Network outages cause inaccuracy in delay metrics.

A replica calculates delay metrics based on times reflecting the following events:

* **t0**: the remote replica records the change in its data

* **t1**: the remote replica sends the change to a replica server

  (This time isn't necessary to calculate the delays in the metrics.)

* **t2**: the local replica receives the change from a replica server

* **t3**: the local replica applies the change to its data

This figure illustrates when these events occur:

![Replication change processing events](../_images/repl-delay.svg)

Replication keeps track of changes using CSNs *(tooltip: \<div class="paragraph">
\<p>An opaque string uniquely identifying a single change to directory data and when it occurred.\</p>
\</div>)*, opaque and unique identifiers for each change that indicate when and where each change first occurred. The **tn** values are CSNs.

When the CSNs for the last change received and the last change replayed are identical, the replica has applied all the changes it has received. In this case, there is no known delay. The receive and replay delay metrics are set to 0 (zero).

When the last received and last replayed CSNs differ:

* *Receive delay* is set to the time **t2** - **t0** for the last change received.

  Another name for receive delay is current delay.

* *Replay delay* is the absolute value of **t3** for the last change replayed - **t2** for the last change received. In other words, it is an approximation of how long it takes for DS to replay a change. Bursty traffic can generate spikes in replay delay that aren't a symptom of a replication problem.

As long as replication delay tends toward zero regularly and over the long term, temporary spikes and increases in delay measurements are normal. When all replicas remain connected and yet replication delay remains high and increases over the long term, the high replication delay indicates a problem. Steadily high and increasing replication delay shows that replication is not converging, and the service is failing to achieve eventual consistency.

For a current snapshot of replication delays, you can also use the `dsrepl status` command. Learn more in [Replication status](../config-guide/repl-status.html).

### Replication status (Prometheus)

The following example checks the replication status metrics:

```console
$ curl \
--cacert ca-cert.pem \
--user monitor:password \
https://localhost:8443/metrics/prometheus/0.0.4 2>/dev/null | grep replica_status
```

The effective replica status is the gauge whose value is `1.0`. For example, this output shows normal status:

```none
ds_replication_replica_status{domain_name="dc=example,dc=com",server_id="evaluation-only",status="BAD_DATA",} 0.0
ds_replication_replica_status{domain_name="dc=example,dc=com",server_id="evaluation-only",status="DEGRADED",} 0.0
ds_replication_replica_status{domain_name="dc=example,dc=com",server_id="evaluation-only",status="FULL_UPDATE",} 0.0
ds_replication_replica_status{domain_name="dc=example,dc=com",server_id="evaluation-only",status="INVALID",} 0.0
ds_replication_replica_status{domain_name="dc=example,dc=com",server_id="evaluation-only",status="NORMAL",} 1.0
ds_replication_replica_status{domain_name="dc=example,dc=com",server_id="evaluation-only",status="NOT_CONNECTED",} 0.0
ds_replication_replica_status{domain_name="dc=example,dc=com",server_id="evaluation-only",status="TOO_LATE",} 0.0
```

|   |                                                                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * The `DEGRADED` status is for backwards compatibility only.

* The values in the `Status` column of the command output don't necessarily match the monitoring attribute values.

  Learn more in the [dsrepl status](../tools-reference/dsrepl.html#dsrepl_status) command reference. |

If the status is not `Normal`, how you react depends on the value of the `ds-mon-status` attribute for LDAP, or `ds_replication_replica_status{status}` for Prometheus.

| Status          | Explanation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Actions to take                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Bad data`      | Replication is broken.Internally, DS replicas store a shorthand form of the initial state called a *generation ID*. The generation ID is a hash of the first 1000 entries in a backend, combined with the total number of entries. When the replicas' generation IDs match, the servers can replicate data without user intervention. When the replicas' generation IDs don't match for a given backend, the servers can't replicate the data.This status arises for one of the following reasons:- The replica and the replication server have different generation IDs for the data because the replica began with different data than its peer replicas.

- The fractional replication configuration for this replica doesn't match the backend data. For example, you reconfigured fractional replication to include or exclude different attributes, or you configured fractional replication incompatibly on different peer replicas.You must intervene to make sure the replicas with bad data start from the same initial state as their peers. Follow the suggested actions to take. Don't replace or reinitialize the backend data alone. DS stores the generation ID in the backend and in the changelog. The generation IDs in the backend and in the changelog must match on all peer replicas.DS 7.3 introduced this status. Earlier releases included this state as part of the `Bad generation id` status. | Whenever this status displays:1) If fractional replication is configured, make sure the configuration is compatible on all peer replicas.

   Learn more in [Fractional replication (advanced)](../config-guide/repl-fractional.html).

2) Initialize the replica with `Bad data` online from a replica with good data.

   Use the `dsrepl initialize` command to initialize the single bad replica. This fixes the bad generation IDs, correcting the problem in the backend and changelog data.

   Find an example in [Initialize over the network](../config-guide/repl-init.html#init-repl-online).

   If you can't initialize the replica with `Bad data` online, [remove it](../install-guide/uninstall.html) and [replace it with a new replica](../config-guide/repl-add-replica.html). |
| `Full update`   | Replication is operating normally.You have chosen to initialize replication over the network.The time to complete the operation depends on the network bandwidth and volume of data to synchronize.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Monitor the server output and wait for initialization to complete.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `Invalid`       | This status arises for one of the following reasons:- The replica has encountered a replication protocol error. This status can arise due to faulty network communication between the replica and the replication server.

- The replica has just started, and is initializing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | If this status happens during normal operation:1) Review the replica and replication server error logs, described in [About logs](../logging-guide/about-logs.html), for network-related replication error messages.

2) Independently verify network communication between the replica and the replication server systems.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `Normal`        | Replication is operating normally.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Nothing to do.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `Not connected` | This status arises for one of the following reasons:- The replica has just started and is not yet connected to the replication server.

- The replica cannot connect to a replication server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | If this status happens during normal operation:1) Review the replica and replication server error logs for network-related replication error messages.

2) Independently verify network communication between the replica and the replication server systems.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `Too late`      | The replica has fallen further behind the replication server than allowed by the [replication-purge-delay](../configref/objects-replication-synchronization-provider.html#replication-purge-delay). In other words, the replica is missing too many changes, and lacks the historical information required to synchronize with peer replicas.The replica no longer receives updates from replication servers. Other replicas that recognize this status stop returning referrals to this replica.DS 7.3 introduced this status. Earlier releases included this state as part of the `Bad generation id` status.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Whenever this status displays:1) Reinitialize replication for the replica that is too late.

   Learn more in [Manual initialization](../config-guide/repl-init.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## Filtering results (Prometheus)

By default, DS servers return all Prometheus metrics. To limit what the server returns, set one of these HTTP endpoint properties for the `/metrics/prometheus/0.0.4`:

* [`excluded-metric-pattern`](../configref/objects-prometheus-endpoint.html#excluded-metric-pattern)

* [`included-metric-pattern`](../configref/objects-prometheus-endpoint.html#included-metric-pattern)

Set these properties to valid [Java regular expression patterns](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/regex/Pattern.html).

The following configuration change causes the server to return only `ds_connection_handlers_ldap_requests_*` metrics. As mentioned in the reference documentation, "*The metric name prefix must not be included in the filter.*" Notice that the example uses `connection_handlers_ldap_requests`, not including the leading `ds_`:

```console
$ dsconfig \
 set-http-endpoint-prop \
 --endpoint-name /metrics/prometheus/0.0.4 \
 --set included-metric-pattern:'connection_handlers_ldap_requests' \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
```

The following configuration change causes the server to exclude metrics whose names start with `ds_jvm_`. Notice that the example uses the regular expression `jvm_.*`:

```console
$ dsconfig \
 set-http-endpoint-prop \
 --endpoint-name /metrics/prometheus/0.0.4 \
 --set excluded-metric-pattern:'jvm_.*' \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
```

---

---
title: LDAP metrics reference
description: Reference listing of PingDS LDAP monitoring metrics exposed as attributes on entries under cn=monitor.
component: pingds
version: 8.1
page_id: pingds:monitoring-guide:monitoring-metrics-ldap
canonical_url: https://docs.pingidentity.com/pingds/8.1/monitoring-guide/monitoring-metrics-ldap.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["LDAP", "Monitoring"]
---

# LDAP metrics reference

LDAP metrics are exposed as LDAP attributes on entries under `cn=monitor`. Metrics entry object class names start with `ds-monitor`. Metrics attribute names start with `ds-mon`. For details, refer to the [About This Reference](../schemaref/preface.html).

For examples of common monitoring requests, refer to [LDAP-based monitoring](ldap-monitoring.html).

|   |                                                                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Some `ds-mon-jvm-*` metrics depend on the JVM version and configuration. In particular, GC-related metrics depend on the garbage collector that the server uses. The GC metric names are *unstable*, and can change even in a minor JVM release. |

| Name                                                | Syntax                       | Description                                                                                                                                                                                                                                                                           |
| --------------------------------------------------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ds-mon-abandoned-requests`                         | Counter metric               | Total number of abandoned operations since startup                                                                                                                                                                                                                                    |
| `ds-mon-active-connections-count`                   | Integer                      | Number of active client connections                                                                                                                                                                                                                                                   |
| `ds-mon-active-persistent-searches`                 | Integer                      | Number of active persistent searches                                                                                                                                                                                                                                                  |
| `ds-mon-admin-connector-connections`                | Integer                      | Number of connections currently established on the Administration Connector                                                                                                                                                                                                           |
| `ds-mon-admin-hostport`                             | Host port                    | The administrative host and port                                                                                                                                                                                                                                                      |
| `ds-mon-alias`                                      | Directory String             | Certificate alias                                                                                                                                                                                                                                                                     |
| `ds-mon-alive`                                      | Boolean                      | Indicates whether the server is alive                                                                                                                                                                                                                                                 |
| `ds-mon-alive-errors`                               | Directory String             | Lists server errors preventing the server from operating correctly that require administrative action                                                                                                                                                                                 |
| `ds-mon-backend-degraded-index`                     | Directory String             | Backend untrusted index                                                                                                                                                                                                                                                               |
| `ds-mon-backend-degraded-index-count`               | Integer                      | Number of untrusted indexes in the backend                                                                                                                                                                                                                                            |
| `ds-mon-backend-entry-count`                        | Integer                      | Number of entries contained in the backend                                                                                                                                                                                                                                            |
| `ds-mon-backend-entry-size-read`                    | Summary metric               | Histogram of entry sizes being read from the underlying storage                                                                                                                                                                                                                       |
| `ds-mon-backend-entry-size-written`                 | Summary metric               | Histogram of entry sizes being written to the underlying storage                                                                                                                                                                                                                      |
| `ds-mon-backend-filter-indexed`                     | Integer                      | Number of indexed searches performed against the backend                                                                                                                                                                                                                              |
| `ds-mon-backend-filter-unindexed`                   | Integer                      | Number of unindexed searches performed against the backend                                                                                                                                                                                                                            |
| `ds-mon-backend-filter-use`                         | Json                         | Information about the simple search filter processed against the backend                                                                                                                                                                                                              |
| `ds-mon-backend-filter-use-start-time`              | Generalized Time             | Time the server started recording statistical information about the simple search filters processed against the backend                                                                                                                                                               |
| `ds-mon-backend-is-private`                         | Boolean                      | Whether the base DNs of this backend should be considered public or private                                                                                                                                                                                                           |
| `ds-mon-backend-proxy-base-dn`                      | DN                           | Base DNs routed to remote LDAP servers by the proxy backend                                                                                                                                                                                                                           |
| `ds-mon-backend-proxy-shard`                        | Summary metric               | Remote LDAP servers that the proxy backend forwards requests to                                                                                                                                                                                                                       |
| `ds-mon-backend-ttl-entries-deleted`                | Summary metric               | Summary for entries purged by time-to-live                                                                                                                                                                                                                                            |
| `ds-mon-backend-ttl-is-running`                     | Boolean                      | Indicates whether time-to-live is in the process of purging expired entries                                                                                                                                                                                                           |
| `ds-mon-backend-ttl-last-run-time`                  | Generalized Time             | Last time time-to-live finished purging expired entries                                                                                                                                                                                                                               |
| `ds-mon-backend-ttl-queue-size`                     | Integer                      | Number of entries queued for purging by the time-to-live service                                                                                                                                                                                                                      |
| `ds-mon-backend-ttl-thread-count`                   | Integer                      | Number of active time-to-live threads                                                                                                                                                                                                                                                 |
| `ds-mon-backend-untrusted-index`                    | Directory String             | Backend untrusted index                                                                                                                                                                                                                                                               |
| `ds-mon-backend-untrusted-index-count`              | Integer                      | Number of untrusted indexes in the backend                                                                                                                                                                                                                                            |
| `ds-mon-backend-writability-mode`                   | Directory String             | Current backend behavior when processing write operations, can either be "disabled", "enabled" or "internal-only"                                                                                                                                                                     |
| `ds-mon-base-dn`                                    | DN                           | Base DN handled by a backend                                                                                                                                                                                                                                                          |
| `ds-mon-base-dn-entry-count`                        | Integer                      | Number of subordinate entries of the base DN, including the base DN                                                                                                                                                                                                                   |
| `ds-mon-build-number`                               | Integer                      | Build number of the Directory Server                                                                                                                                                                                                                                                  |
| `ds-mon-build-time`                                 | Directory String             | Build date and time of the Directory Server                                                                                                                                                                                                                                           |
| `ds-mon-bytes-read`                                 | Summary metric               | Network bytes read summary                                                                                                                                                                                                                                                            |
| `ds-mon-bytes-written`                              | Summary metric               | Network bytes written summary                                                                                                                                                                                                                                                         |
| `ds-mon-cache-entry-count`                          | Integer                      | Current number of entries held in this cache                                                                                                                                                                                                                                          |
| `ds-mon-cache-max-entry-count`                      | Integer                      | Maximum number of entries allowed in this cache                                                                                                                                                                                                                                       |
| `ds-mon-cache-max-size-bytes`                       | Size in bytes                | Memory limit for this cache                                                                                                                                                                                                                                                           |
| `ds-mon-cache-misses`                               | Summary metric               | Number of attempts to retrieve an entry that was not held in this cache                                                                                                                                                                                                               |
| `ds-mon-cache-size-bytes`                           | Integer                      | Total memory in bytes used by this cache                                                                                                                                                                                                                                              |
| `ds-mon-cache-total-tries`                          | Summary metric               | Number of attempts to retrieve an entry from this cache                                                                                                                                                                                                                               |
| `ds-mon-certificate-expires-at`                     | Generalized Time             | Time the certificate expires                                                                                                                                                                                                                                                          |
| `ds-mon-certificate-issuer-dn`                      | DN                           | Certificate issuer DN                                                                                                                                                                                                                                                                 |
| `ds-mon-certificate-serial-number`                  | Integer                      | Certificate serial number                                                                                                                                                                                                                                                             |
| `ds-mon-certificate-subject-dn`                     | DN                           | Certificate subject DN                                                                                                                                                                                                                                                                |
| `ds-mon-changelog-file-count`                       | Integer                      | The number of changelog files containing updates generated by this replica. A value of zero indicates the replica did not generate any updates during the last purge delay interval                                                                                                   |
| `ds-mon-changelog-hostport`                         | Host port                    | The host and port of the changelog server                                                                                                                                                                                                                                             |
| `ds-mon-changelog-id`                               | Directory String             | Changelog identifier                                                                                                                                                                                                                                                                  |
| `ds-mon-changelog-purge-delay`                      | Duration in milli-seconds    | The purge delay of the changelog                                                                                                                                                                                                                                                      |
| `ds-mon-collective-attribute-subentries-count`      | Integer                      | Total number of collective attribute subentries                                                                                                                                                                                                                                       |
| `ds-mon-compact-version`                            | Directory String             | Compact version of the Directory Server                                                                                                                                                                                                                                               |
| `ds-mon-config-dn`                                  | DN                           | DN of the configuration entry                                                                                                                                                                                                                                                         |
| `ds-mon-connected-to-server-hostport`               | Host port                    | Host and replication port of the server that this server is connected to                                                                                                                                                                                                              |
| `ds-mon-connected-to-server-id`                     | Directory String             | Identifier of the server that this server is connected to                                                                                                                                                                                                                             |
| `ds-mon-connection`                                 | Json                         | Client connection summary information                                                                                                                                                                                                                                                 |
| `ds-mon-connections`                                | Summary metric               | Connection summary                                                                                                                                                                                                                                                                    |
| `ds-mon-current-connections`                        | Integer                      | Number of client connections currently established except on the Administration Connector                                                                                                                                                                                             |
| `ds-mon-current-receive-window`                     | Integer                      | Current replication window size for receiving messages, indicating the number of replication messages a remote server can send before waiting on acknowledgement from this server. This does not depend on the TCP window size                                                        |
| `ds-mon-current-time`                               | Generalized Time             | Current time                                                                                                                                                                                                                                                                          |
| `ds-mon-db-cache-evict-internal-nodes-count`        | Integer                      | Number of internal nodes evicted from the database cache                                                                                                                                                                                                                              |
| `ds-mon-db-cache-evict-leaf-nodes-count`            | Integer                      | Number of leaf nodes (data records) evicted from the database cache                                                                                                                                                                                                                   |
| `ds-mon-db-cache-leaf-nodes`                        | Boolean                      | Whether leaf nodes are cached                                                                                                                                                                                                                                                         |
| `ds-mon-db-cache-misses-internal-nodes`             | Integer                      | Number of internal nodes requested by btree operations that were not in the database cache                                                                                                                                                                                            |
| `ds-mon-db-cache-misses-leaf-nodes`                 | Integer                      | Number of leaf nodes (data records) requested by btree operations that were not in the database cache                                                                                                                                                                                 |
| `ds-mon-db-cache-size-active`                       | Size in bytes                | Size of the database cache                                                                                                                                                                                                                                                            |
| `ds-mon-db-cache-size-total`                        | Size in bytes                | Maximum size of the database cache                                                                                                                                                                                                                                                    |
| `ds-mon-db-cache-total-tries-internal-nodes`        | Integer                      | Number of internal nodes requested by btree operations                                                                                                                                                                                                                                |
| `ds-mon-db-cache-total-tries-leaf-nodes`            | Integer                      | Number of leaf nodes (data records) requested by btree operations                                                                                                                                                                                                                     |
| `ds-mon-db-checkpoint-count`                        | Integer                      | Number of checkpoints run so far                                                                                                                                                                                                                                                      |
| `ds-mon-db-log-cleaner-file-deletion-count`         | Integer                      | Number of cleaner file deletions                                                                                                                                                                                                                                                      |
| `ds-mon-db-log-files-open`                          | Integer                      | Number of files currently open in the database file cache                                                                                                                                                                                                                             |
| `ds-mon-db-log-files-opened`                        | Integer                      | Number of times a log file has been opened                                                                                                                                                                                                                                            |
| `ds-mon-db-log-size-active`                         | Size in bytes                | Estimate of the amount in bytes of live data in all data files (i.e., the size of the DB, ignoring garbage)                                                                                                                                                                           |
| `ds-mon-db-log-size-total`                          | Size in bytes                | Size used by all data files on disk                                                                                                                                                                                                                                                   |
| `ds-mon-db-log-utilization-max`                     | Integer                      | Current maximum (upper bound) log utilization as a percentage                                                                                                                                                                                                                         |
| `ds-mon-db-log-utilization-min`                     | Integer                      | Current minimum (lower bound) log utilization as a percentage                                                                                                                                                                                                                         |
| `ds-mon-db-version`                                 | Directory String             | Database version used by the backend                                                                                                                                                                                                                                                  |
| `ds-mon-disk-dir`                                   | Filesystem path              | A monitored directory containing data that may change over time                                                                                                                                                                                                                       |
| `ds-mon-disk-free`                                  | Size in bytes                | Amount of free disk space                                                                                                                                                                                                                                                             |
| `ds-mon-disk-full-threshold`                        | Size in bytes                | Effective full disk space threshold                                                                                                                                                                                                                                                   |
| `ds-mon-disk-low-threshold`                         | Size in bytes                | Effective low disk space threshold                                                                                                                                                                                                                                                    |
| `ds-mon-disk-root`                                  | Filesystem path              | Monitored disk root                                                                                                                                                                                                                                                                   |
| `ds-mon-disk-state`                                 | Directory String             | Current disk state, can be either "normal", "low" or "full"                                                                                                                                                                                                                           |
| `ds-mon-domain-generation-id`                       | Integer                      | Replication domain generation identifier                                                                                                                                                                                                                                              |
| `ds-mon-domain-name`                                | DN                           | Replication domain name                                                                                                                                                                                                                                                               |
| `ds-mon-dynamic-groups-count`                       | Integer                      | Total number of dynamic groups                                                                                                                                                                                                                                                        |
| `ds-mon-entries-acis-count`                         | Integer                      | Total number of entries ACIs                                                                                                                                                                                                                                                          |
| `ds-mon-entries-awaiting-updates-count`             | Integer                      | Number of entries for which an update operation has been received but not replayed yet by this replica                                                                                                                                                                                |
| `ds-mon-entries-with-aci-attributes-count`          | Integer                      | Total number of entries with ACI attributes                                                                                                                                                                                                                                           |
| `ds-mon-fix-ids`                                    | Directory String             | IDs of issues that have been fixed in this Directory Server build                                                                                                                                                                                                                     |
| `ds-mon-full-version`                               | Directory String             | Full version of the Directory Server                                                                                                                                                                                                                                                  |
| `ds-mon-global-acis-count`                          | Integer                      | Total number of global ACIs                                                                                                                                                                                                                                                           |
| `ds-mon-group-id`                                   | Directory String             | Unique identifier of the group in which the directory server belongs                                                                                                                                                                                                                  |
| `ds-mon-healthy`                                    | Boolean                      | Indicates whether the server is able to handle requests                                                                                                                                                                                                                               |
| `ds-mon-healthy-errors`                             | Directory String             | Lists transient server errors preventing the server from temporarily handling requests                                                                                                                                                                                                |
| `ds-mon-index`                                      | Directory String             | The name of the index                                                                                                                                                                                                                                                                 |
| `ds-mon-index-cost`                                 | Timer metric                 | Number of index updates and their time cost                                                                                                                                                                                                                                           |
| `ds-mon-index-uses`                                 | Summary metric               | Number of accesses of this index. For attribute indexes it represents the number of search operations that have used this index, for system indexes it represents the number of key lookups.                                                                                          |
| `ds-mon-install-path`                               | Filesystem path              | Directory Server root installation path                                                                                                                                                                                                                                               |
| `ds-mon-instance-path`                              | Filesystem path              | Directory Server instance path                                                                                                                                                                                                                                                        |
| `ds-mon-jvm-architecture`                           | Directory String             | Java virtual machine architecture (e.g. 32-bit, 64-bit)                                                                                                                                                                                                                               |
| `ds-mon-jvm-arguments`                              | Directory String             | Input arguments passed to the Java virtual machine                                                                                                                                                                                                                                    |
| `ds-mon-jvm-available-cpus`                         | Integer                      | Number of processors available to the Java virtual machine                                                                                                                                                                                                                            |
| `ds-mon-jvm-classes-loaded`                         | Integer                      | Number of classes loaded since the Java virtual machine started                                                                                                                                                                                                                       |
| `ds-mon-jvm-classes-unloaded`                       | Integer                      | Number of classes unloaded since the Java virtual machine started                                                                                                                                                                                                                     |
| `ds-mon-jvm-class-path`                             | Filesystem path              | Path used to find directories and JAR archives containing Java class files                                                                                                                                                                                                            |
| `ds-mon-jvm-java-home`                              | Filesystem path              | Installation directory for Java runtime environment (JRE)                                                                                                                                                                                                                             |
| `ds-mon-jvm-java-vendor`                            | Directory String             | Java runtime environment (JRE) vendor                                                                                                                                                                                                                                                 |
| `ds-mon-jvm-java-version`                           | Directory String             | Java runtime environment (JRE) version                                                                                                                                                                                                                                                |
| `ds-mon-jvm-memory-heap-init`                       | Size in bytes                | Amount of heap memory that the Java virtual machine initially requested from the operating system                                                                                                                                                                                     |
| `ds-mon-jvm-memory-heap-max`                        | Size in bytes                | Maximum amount of heap memory that the Java virtual machine will attempt to use                                                                                                                                                                                                       |
| `ds-mon-jvm-memory-heap-reserved`                   | Size in bytes                | Amount of heap memory that is committed for the Java virtual machine to use                                                                                                                                                                                                           |
| `ds-mon-jvm-memory-heap-used`                       | Size in bytes                | Amount of heap memory used by the Java virtual machine                                                                                                                                                                                                                                |
| `ds-mon-jvm-memory-init`                            | Size in bytes                | Amount of memory that the Java virtual machine initially requested from the operating system                                                                                                                                                                                          |
| `ds-mon-jvm-memory-max`                             | Size in bytes                | Maximum amount of memory that the Java virtual machine will attempt to use                                                                                                                                                                                                            |
| `ds-mon-jvm-memory-non-heap-init`                   | Size in bytes                | Amount of non-heap memory that the Java virtual machine initially requested from the operating system                                                                                                                                                                                 |
| `ds-mon-jvm-memory-non-heap-max`                    | Size in bytes                | Maximum amount of non-heap memory that the Java virtual machine will attempt to use                                                                                                                                                                                                   |
| `ds-mon-jvm-memory-non-heap-reserved`               | Size in bytes                | Amount of non-heap memory that is committed for the Java virtual machine to use                                                                                                                                                                                                       |
| `ds-mon-jvm-memory-non-heap-used`                   | Size in bytes                | Amount of non-heap memory used by the Java virtual machine                                                                                                                                                                                                                            |
| `ds-mon-jvm-memory-reserved`                        | Size in bytes                | Amount of memory that is committed for the Java virtual machine to use                                                                                                                                                                                                                |
| `ds-mon-jvm-memory-used`                            | Size in bytes                | Amount of memory used by the Java virtual machine                                                                                                                                                                                                                                     |
| `ds-mon-jvm-supported-tls-ciphers`                  | Directory String             | Transport Layer Security (TLS) cipher suites supported by this Directory Server                                                                                                                                                                                                       |
| `ds-mon-jvm-supported-tls-protocols`                | Directory String             | Transport Layer Security (TLS) protocols supported by this Directory Server                                                                                                                                                                                                           |
| `ds-mon-jvm-threads-blocked-count`                  | Integer                      | Number of threads in the BLOCKED state                                                                                                                                                                                                                                                |
| `ds-mon-jvm-threads-count`                          | Integer                      | Number of live threads including both daemon and non-daemon threads                                                                                                                                                                                                                   |
| `ds-mon-jvm-threads-daemon-count`                   | Integer                      | Number of live daemon threads                                                                                                                                                                                                                                                         |
| `ds-mon-jvm-threads-deadlock-count`                 | Integer                      | Number of deadlocked threads                                                                                                                                                                                                                                                          |
| `ds-mon-jvm-threads-deadlocks`                      | Directory String             | Diagnostic stack traces for deadlocked threads                                                                                                                                                                                                                                        |
| `ds-mon-jvm-threads-new-count`                      | Integer                      | Number of threads in the NEW state                                                                                                                                                                                                                                                    |
| `ds-mon-jvm-threads-runnable-count`                 | Integer                      | Number of threads in the RUNNABLE state                                                                                                                                                                                                                                               |
| `ds-mon-jvm-threads-terminated-count`               | Integer                      | Number of threads in the TERMINATED state                                                                                                                                                                                                                                             |
| `ds-mon-jvm-threads-timed-waiting-count`            | Integer                      | Number of threads in the TIMED\_WAITING state                                                                                                                                                                                                                                         |
| `ds-mon-jvm-threads-waiting-count`                  | Integer                      | Number of threads in the WAITING state                                                                                                                                                                                                                                                |
| `ds-mon-jvm-vendor`                                 | Directory String             | Java virtual machine vendor                                                                                                                                                                                                                                                           |
| `ds-mon-jvm-version`                                | Directory String             | Java virtual machine version                                                                                                                                                                                                                                                          |
| `ds-mon-last-received-update`                       | Directory String             | The CSN of the last received update originating from the remote replica                                                                                                                                                                                                               |
| `ds-mon-last-replayed-update`                       | Directory String             | The CSN of the last replayed update originating from the remote replica                                                                                                                                                                                                               |
| `ds-mon-last-seen`                                  | Generalized Time             | Time this server was last seen                                                                                                                                                                                                                                                        |
| `ds-mon-ldap-hostport`                              | Host port                    | The host and port to connect using LDAP (no support for start TLS)                                                                                                                                                                                                                    |
| `ds-mon-ldaps-hostport`                             | Host port                    | The host and port to connect using LDAPS                                                                                                                                                                                                                                              |
| `ds-mon-ldap-starttls-hostport`                     | Host port                    | The host and port to connect using LDAP (with support for start TLS)                                                                                                                                                                                                                  |
| `ds-mon-listen-address`                             | Directory String             | Host and port                                                                                                                                                                                                                                                                         |
| `ds-mon-lost-connections`                           | Integer                      | Number of times the replica lost its connection to the replication server                                                                                                                                                                                                             |
| `ds-mon-major-version`                              | Integer                      | Major version number of the Directory Server                                                                                                                                                                                                                                          |
| `ds-mon-max-connections`                            | Integer                      | Maximum number of simultaneous client connections that have been established with the Directory Server                                                                                                                                                                                |
| `ds-mon-minor-version`                              | Integer                      | Minor version number of the Directory Server                                                                                                                                                                                                                                          |
| `ds-mon-newest-change-number`                       | Integer                      | Newest change number present in the change number index database                                                                                                                                                                                                                      |
| `ds-mon-newest-csn`                                 | CSN (Change Sequence Number) | Newest CSN present in the replica database                                                                                                                                                                                                                                            |
| `ds-mon-newest-csn-timestamp`                       | Generalized Time             | Time of the newest CSN present in the replica database                                                                                                                                                                                                                                |
| `ds-mon-oldest-change-number`                       | Integer                      | Oldest change number present in the change number index database                                                                                                                                                                                                                      |
| `ds-mon-oldest-csn`                                 | CSN (Change Sequence Number) | Oldest CSN present in the replica database                                                                                                                                                                                                                                            |
| `ds-mon-oldest-csn-timestamp`                       | Generalized Time             | Time of the oldest CSN present in the replica database                                                                                                                                                                                                                                |
| `ds-mon-os-architecture`                            | Directory String             | Operating system architecture                                                                                                                                                                                                                                                         |
| `ds-mon-os-name`                                    | Directory String             | Operating system name                                                                                                                                                                                                                                                                 |
| `ds-mon-os-version`                                 | Directory String             | Operating system version                                                                                                                                                                                                                                                              |
| `ds-mon-password-policy-subentries-count`           | Integer                      | Total number of password policy subentries                                                                                                                                                                                                                                            |
| `ds-mon-point-version`                              | Integer                      | Point version number of the Directory Server                                                                                                                                                                                                                                          |
| `ds-mon-process-id`                                 | UUID                         | Process ID of the running directory server                                                                                                                                                                                                                                            |
| `ds-mon-product-name`                               | Directory String             | Full name of the Directory Server                                                                                                                                                                                                                                                     |
| `ds-mon-protocol`                                   | Directory String             | Network protocol                                                                                                                                                                                                                                                                      |
| `ds-mon-receive-delay`                              | Duration in milli-seconds    | Current local delay in receiving replicated operations                                                                                                                                                                                                                                |
| `ds-mon-replay-delay`                               | Duration in milli-seconds    | Current local delay in replaying replicated operations                                                                                                                                                                                                                                |
| `ds-mon-replayed-internal-updates`                  | Counter metric               | Number of updates replayed on this replica which modify the internal state but not user data                                                                                                                                                                                          |
| `ds-mon-replayed-updates`                           | Timer metric                 | Replay etime for updates that have been replayed on this replica                                                                                                                                                                                                                      |
| `ds-mon-replayed-updates-conflicts-resolved`        | Counter metric               | Number of updates replayed on this replica for which replication naming conflicts have been resolved                                                                                                                                                                                  |
| `ds-mon-replayed-updates-conflicts-unresolved`      | Counter metric               | Number of updates replayed on this replica for which replication naming conflicts have not been resolved                                                                                                                                                                              |
| `ds-mon-replication-domain`                         | DN                           | The replication domain                                                                                                                                                                                                                                                                |
| `ds-mon-replication-protocol-version`               | Integer                      | The protocol version used for replication                                                                                                                                                                                                                                             |
| `ds-mon-requests-abandon`                           | Timer metric                 | Abandon request timer                                                                                                                                                                                                                                                                 |
| `ds-mon-requests-add`                               | Timer metric                 | Add request timer                                                                                                                                                                                                                                                                     |
| `ds-mon-requests-bind`                              | Timer metric                 | Bind request timer                                                                                                                                                                                                                                                                    |
| `ds-mon-requests-compare`                           | Timer metric                 | Compare request timer                                                                                                                                                                                                                                                                 |
| `ds-mon-requests-delete`                            | Timer metric                 | Delete request timer                                                                                                                                                                                                                                                                  |
| `ds-mon-requests-extended`                          | Timer metric                 | Extended request timer                                                                                                                                                                                                                                                                |
| `ds-mon-requests-failure-client-invalid-request`    | Timer metric                 | Timer for requests that failed because there was a problem while attempting to perform the associated operation (associated LDAP result codes: 1, 2, 12, 15, 16, 17, 18, 19, 20, 21, 23, 34, 35, 36, 37, 38, 39; associated HTTP status codes: client error (4xx) except 401 and 403) |
| `ds-mon-requests-failure-client-redirect`           | Timer metric                 | Timer for requests that could not complete because further action is required (associated HTTP status codes: redirection (3xx))                                                                                                                                                       |
| `ds-mon-requests-failure-client-referral`           | Timer metric                 | Timer for requests that failed because the server did not hold the request targeted entry (but was able to provide alternative servers that may) (associated LDAP result code: 10)                                                                                                    |
| `ds-mon-requests-failure-client-resource-limit`     | Timer metric                 | Timer for requests that failed because they were trying to exceed the resource limits allocated to the associated clients (associated LDAP result codes: time, size and admin limit exceeded (respectively 4, 5 and 11)                                                               |
| `ds-mon-requests-failure-client-security`           | Timer metric                 | Timer for requests that failed for security reasons (associated LDAP result codes: 8, 9, 13, 25, 26, 27; associated HTTP status codes: unauthorized (401) and forbidden (403))                                                                                                        |
| `ds-mon-requests-failure-server`                    | Timer metric                 | Timer for apparently valid requests that failed because the server was not able to process them (associated LDAP result codes: busy (51), unavailable (52), unwilling to perform (53) and other (80); associated HTTP status codes: server error (5xx))                               |
| `ds-mon-requests-failure-uncategorized`             | Timer metric                 | Timer for requests that failed due to uncategorized reasons                                                                                                                                                                                                                           |
| `ds-mon-requests-get`                               | Timer metric                 | GET request timer                                                                                                                                                                                                                                                                     |
| `ds-mon-requests-in-queue`                          | Integer                      | Number of requests in the work queue that have not yet been picked up for processing                                                                                                                                                                                                  |
| `ds-mon-requests-modify`                            | Timer metric                 | Modify request timer                                                                                                                                                                                                                                                                  |
| `ds-mon-requests-modify-dn`                         | Timer metric                 | Modify DN request timer                                                                                                                                                                                                                                                               |
| `ds-mon-requests-patch`                             | Timer metric                 | PATCH request timer                                                                                                                                                                                                                                                                   |
| `ds-mon-requests-post`                              | Timer metric                 | POST request timer                                                                                                                                                                                                                                                                    |
| `ds-mon-requests-psearch`                           | Timer metric                 | Persistent search request timer                                                                                                                                                                                                                                                       |
| `ds-mon-requests-put`                               | Timer metric                 | PUT request timer                                                                                                                                                                                                                                                                     |
| `ds-mon-requests-search-base`                       | Timer metric                 | Base object search request timer                                                                                                                                                                                                                                                      |
| `ds-mon-requests-search-one`                        | Timer metric                 | One level search request timer                                                                                                                                                                                                                                                        |
| `ds-mon-requests-search-sub`                        | Timer metric                 | Subtree search request timer                                                                                                                                                                                                                                                          |
| `ds-mon-requests-submitted`                         | Summary metric               | Summary for operations that have been successfully submitted to the work queue                                                                                                                                                                                                        |
| `ds-mon-requests-unbind`                            | Timer metric                 | Unbind request timer                                                                                                                                                                                                                                                                  |
| `ds-mon-requests-uncategorized`                     | Timer metric                 | Uncategorized request timer                                                                                                                                                                                                                                                           |
| `ds-mon-revision`                                   | Directory String             | Revision ID in the source repository from which the Directory Server is build                                                                                                                                                                                                         |
| `ds-mon-sent-updates`                               | Counter metric               | Number of replication updates sent by this replica                                                                                                                                                                                                                                    |
| `ds-mon-server-id`                                  | Directory String             | Server identifier                                                                                                                                                                                                                                                                     |
| `ds-mon-server-is-local`                            | Boolean                      | Indicates whether this is the topology server that has handled the monitoring request                                                                                                                                                                                                 |
| `ds-mon-server-state`                               | CSN (Change Sequence Number) | Replication server state                                                                                                                                                                                                                                                              |
| `ds-mon-short-name`                                 | Directory String             | Short name of the Directory Server                                                                                                                                                                                                                                                    |
| `ds-mon-ssl-encryption`                             | Boolean                      | Whether SSL encryption is used when exchanging messages with this server                                                                                                                                                                                                              |
| `ds-mon-start-time`                                 | Generalized Time             | Time the Directory Server started                                                                                                                                                                                                                                                     |
| `ds-mon-static-groups-count`                        | Integer                      | Total number of static groups                                                                                                                                                                                                                                                         |
| `ds-mon-static-group-size-less-or-equal-to-100`     | Integer                      | Number of static groups with at most 100 members                                                                                                                                                                                                                                      |
| `ds-mon-static-group-size-less-or-equal-to-1000`    | Integer                      | Number of static groups with at most 1000 members                                                                                                                                                                                                                                     |
| `ds-mon-static-group-size-less-or-equal-to-10000`   | Integer                      | Number of static groups with at most 10000 members                                                                                                                                                                                                                                    |
| `ds-mon-static-group-size-less-or-equal-to-100000`  | Integer                      | Number of static groups with at most 100000 members                                                                                                                                                                                                                                   |
| `ds-mon-static-group-size-less-or-equal-to-1000000` | Integer                      | Number of static groups with at most 1000000 members                                                                                                                                                                                                                                  |
| `ds-mon-static-group-size-less-or-equal-to-inf`     | Integer                      | Total number of static groups                                                                                                                                                                                                                                                         |
| `ds-mon-status`                                     | Directory String             | Replication status of the local replica, can either be "Invalid", "Not connected", "Normal", "Too late", "Full update", "Bad data"                                                                                                                                                    |
| `ds-mon-status-last-changed`                        | Generalized Time             | Last time the replication status of the local replica changed                                                                                                                                                                                                                         |
| `ds-mon-supported-log-category`                     | Directory String             | Supported server log categories                                                                                                                                                                                                                                                       |
| `ds-mon-system-name`                                | Directory String             | Fully qualified domain name of the system where the Directory Server is running                                                                                                                                                                                                       |
| `ds-mon-total-connections`                          | Integer                      | Total number of client connections that have been established with the Directory Server since it started                                                                                                                                                                              |
| `ds-mon-total-update`                               | Directory String             | The type of total update when it is in progress. Possible values: import or export                                                                                                                                                                                                    |
| `ds-mon-total-update-entry-count`                   | Integer                      | The total number of entries to be processed when a total update is in progress                                                                                                                                                                                                        |
| `ds-mon-total-update-entry-left`                    | Integer                      | The number of entries still to be processed when a total update is in progress                                                                                                                                                                                                        |
| `ds-mon-updates-already-in-progress`                | Counter metric               | Number of duplicate updates: updates received by this replica which cannot be applied because they are already in progress. Can happen when a directory server fails over to another replication server                                                                               |
| `ds-mon-updates-inbound-queue`                      | Integer                      | Number of remote updates received from the replication server but not replayed yet on this replica                                                                                                                                                                                    |
| `ds-mon-updates-in-progress`                        | Integer                      | Number of remote updates received in the queue waiting to be replayed                                                                                                                                                                                                                 |
| `ds-mon-updates-in-queue`                           | Integer                      | Number of remote updates received in the queue                                                                                                                                                                                                                                        |
| `ds-mon-updates-outbound-queue`                     | Integer                      | Number of local updates that are waiting to be sent to the replication server once they complete                                                                                                                                                                                      |
| `ds-mon-updates-totals-per-replay-thread`           | Json                         | JSON array of the number of updates replayed per replay thread                                                                                                                                                                                                                        |
| `ds-mon-vendor-name`                                | Directory String             | Vendor name of the Directory Server                                                                                                                                                                                                                                                   |
| `ds-mon-version-qualifier`                          | Directory String             | Version qualifier of the Directory Server                                                                                                                                                                                                                                             |
| `ds-mon-virtual-static-groups-count`                | Integer                      | Total number of virtual static groups                                                                                                                                                                                                                                                 |
| `ds-mon-working-directory`                          | Filesystem path              | Current working directory of the user running the Directory Server                                                                                                                                                                                                                    |

---

---
title: LDAP-based monitoring
description: Monitor PingDS servers over LDAP by reading availability, activity, index, and replication data from cn=monitor.
component: pingds
version: 8.1
page_id: pingds:monitoring-guide:ldap-monitoring
canonical_url: https://docs.pingidentity.com/pingds/8.1/monitoring-guide/ldap-monitoring.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-02-09T09:34:08Z
keywords: ["LDAP", "Monitoring", "Troubleshooting"]
section_ids:
  basic_availability: Basic availability
  monitoring-health-status-anonymously: Server health (LDAP)
  monitoring-health-status-ldap: Server health details (LDAP)
  activity: Activity
  monitoring-activity-ldap: Active users (LDAP)
  monitoring-operation-stats-ldap: Request statistics (LDAP)
  monitoring-work-queue-ldap: Work queue (LDAP)
  counts: Counts
  monitoring-acis-ldap: ACIs (LDAP)
  monitoring-entry-counts-ldap: Database size (LDAP)
  monitoring-entry-cache-ldap: Entry caches (LDAP)
  monitoring-groups-ldap: Groups (LDAP)
  monitoring-subentries-ldap: Subentries (LDAP)
  indexing: Indexing
  monitoring-index-reads-ldap: Index use (LDAP)
  monitoring-index-cost-ldap: Index cost (LDAP)
  monitoring-logs: Logging
  monitoring-replication-ldap: Replication
  monitoring-replication-delay-ldap: Replication delay (LDAP)
  monitoring-replication-status-ldap: Replication status (LDAP)
  monitoring-read-privilege: Monitor privilege
---

# LDAP-based monitoring

|   |                                                                                                                                                                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This page covers the Lightweight Directory Access Protocol (LDAP) *(tooltip: \<div class="paragraph">&#xA;\<p>An open, cross-platform protocol used for interacting with directory services.\</p>&#xA;\</div>)* interfaces for monitoring DS servers. For the same capabilities over HTTP, refer to [HTTP-based monitoring](http-monitoring.html). |

DS servers publish whether the server is alive and able to handle requests in the root DSE. They publish monitoring information over LDAP under the entry `cn=monitor`.

The following example reads all available monitoring entries:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=monitor \
 --bindPassword password \
 --baseDN cn=monitor \
 "(&)"
```

The monitoring entries under `cn=monitor` reflect activity since the server started.

Many types of metrics are exposed. For details, refer to [LDAP metrics reference](monitoring-metrics-ldap.html).

## Basic availability

### Server health (LDAP)

Anonymous clients can monitor the health status of the DS server by reading the `alive` attribute of the root DSE:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --baseDN "" \
 --searchScope base \
 "(&)" \
 alive
```

> **Collapse: Show output**
>
> ```
> dn:
> alive: true
> ```

When `alive` is `true`, the server's internal tests have not found any errors requiring administrative action. When it is `false`, fix the errors and either restart or replace the server.

If the server returns `false` for this attribute, get error information, as described in [Server health details (LDAP)](#monitoring-health-status-ldap).

### Server health details (LDAP)

The default monitor user can check whether the server is alive and able to handle requests on `cn=health status,cn=monitor`:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=monitor \
 --bindPassword password \
 --baseDN "cn=health status,cn=monitor" \
 --searchScope base \
 "(&)"
```

> **Collapse: Show output**
>
> ```
> dn: cn=health status,cn=monitor
> ds-mon-alive: true
> ds-mon-healthy: true
> objectClass: top
> objectClass: ds-monitor
> objectClass: ds-monitor-health-status
> cn: health status
> ```

When the server is either not alive or not able to handle requests, this entry includes error diagnostics as strings on the `ds-mon-alive-errors` and `ds-mon-healthy-errors` attributes.

## Activity

### Active users (LDAP)

DS server connection handlers respond to client requests. The following example uses the default monitor user account to read the metrics about active connections on each connection handler:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=monitor \
 --bindPassword password \
 --baseDN cn=monitor \
 "(objectClass=ds-monitor-connection*)" \
 ds-mon-active-connections-count ds-mon-active-persistent-searches ds-mon-connection ds-mon-listen-address
```

For details about the content of metrics returned, refer to [Metric types reference](monitoring-types.html).

### Request statistics (LDAP)

DS server connection handlers respond to client requests. The following example uses the default monitor user account to read statistics about client operations on each of the available connection handlers:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=monitor \
 --bindPassword password \
 --baseDN "cn=connection handlers,cn=monitor" \
 "(&)"
```

For details about the content of metrics returned, refer to [Metric types reference](monitoring-types.html).

### Work queue (LDAP)

DS servers have a work queue to track request processing by worker threads, and whether the server has rejected any requests due to a full queue. If enough worker threads are available, then no requests are rejected. The following example uses the default monitor user account to read statistics about the work queue:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=monitor \
 --bindPassword password \
 --baseDN "cn=work queue,cn=monitor" \
 "(&)"
```

For details about the content of metrics returned, refer to [Metric types reference](monitoring-types.html). To adjust the number of worker threads, refer to the settings for [Traditional Work Queue](../configref/objects-traditional-work-queue.html).

## Counts

### ACIs (LDAP)

DS maintains counts of ACIs *(tooltip: \<div class="paragraph">
\<p>An instruction or rule that can be used to grant or deny access to users to perform operations on a server.\</p>
\</div>)*:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=monitor \
 --bindPassword password \
 --baseDN cn=monitor \
 "(objectClass=ds-monitor-aci)" \
 ds-mon-entries-acis-count ds-mon-entries-with-aci-attributes-count ds-mon-global-acis-count
```

### Database size (LDAP)

DS servers maintain counts of the number of entries in each backend and under each base DN. The following example uses the default monitor user account to read the counts:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=monitor \
 --bindPassword password \
 --baseDN cn=monitor \
 "(|(ds-mon-backend-entry-count=*)(ds-mon-base-dn-entry-count=*))" \
 ds-mon-backend-entry-count ds-mon-base-dn-entry-count
```

### Entry caches (LDAP)

DS servers maintain entry cache statistics:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=monitor \
 --bindPassword password \
 --baseDN cn=monitor \
 "(objectClass=ds-monitor-entry-cache)" \
```

Entry caches for groups have their own monitoring entries.

### Groups (LDAP)

The following example reads counts of static, dynamic, and virtual static groups, and statistics on the distribution of static group size:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=monitor \
 --bindPassword password \
 --baseDN cn=monitor \
 "(objectClass=ds-monitor-groups)" \
 ds-mon-dynamic-groups-count ds-mon-static-groups-count ds-mon-virtual-static-groups-count \
 ds-mon-static-group-size-less-or-equal-to-100 \
 ds-mon-static-group-size-less-or-equal-to-1000 \
 ds-mon-static-group-size-less-or-equal-to-10000 \
 ds-mon-static-group-size-less-or-equal-to-100000 \
 ds-mon-static-group-size-less-or-equal-to-1000000 \
 ds-mon-static-group-size-less-or-equal-to-inf
```

At startup time, DS servers log a message showing the number of different types of groups and the memory allocated to cache static groups.

### Subentries (LDAP)

DS maintains counts of LDAP subentries:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=monitor \
 --bindPassword password \
 --baseDN cn=monitor \
 "(objectClass=ds-monitor-subentries)" \
 ds-mon-collective-attribute-subentries-count \
 ds-mon-password-policy-subentries-count
```

## Indexing

### Index use (LDAP)

DS maintains metrics about index use. The metrics indicate how often an index was accessed since the DS server started.

The following example demonstrates how to read the metrics for all monitored indexes:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=monitor \
 --bindPassword password \
 --baseDN cn=monitor \
 "(objectClass=ds-monitor-backend-index)" ds-mon-index ds-mon-index-uses
```

### Index cost (LDAP)

DS maintains metrics about index cost. The metrics count the number of updates and how long they took since the DS server started.

The following example demonstrates how to read the metrics for all monitored indexes:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=monitor \
 --bindPassword password \
 --baseDN cn=monitor \
 "(objectClass=ds-monitor-backend-index)" ds-mon-index ds-mon-index-cost
```

## Logging

DS maintains a list of supported logging categories. The following example reads the list:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=monitor \
 --bindPassword password \
 --baseDN cn=monitor \
 "(objectClass=ds-monitor-logging)"
```

## Replication

Monitor the following to ensure replication runs smoothly. Take action as described in these sections and in the troubleshooting documentation for [replication problems](../maintenance-guide/troubleshooting.html#troubleshoot-repl).

### Replication delay (LDAP)

The following example uses the default monitor user account to check the delay in replication:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=monitor \
 --bindPassword password \
 --baseDN cn=monitor \
 "(ds-mon-receive-delay=*)" \
 ds-mon-receive-delay
```

> **Collapse: Show output**
>
> ```
> dn: ds-mon-domain-name=cn=schema,cn=replicas,cn=replication,cn=monitor
> ds-mon-receive-delay: <delay>
>
> dn: ds-mon-domain-name=dc=example\,dc=com,cn=replicas,cn=replication,cn=monitor
> ds-mon-receive-delay: <delay>
>
> dn: ds-mon-domain-name=uid=monitor,cn=replicas,cn=replication,cn=monitor
> ds-mon-receive-delay: <delay>
> ```

DS replicas measure replication delay as the local delay when receiving and replaying changes. There are two parts to replication delay: *receive delay* and *replay delay*. To understand what's causing replication delay, you must determine which part is responsible for the delay.

A replica calculates these local delays based on changes received from other replicas. Therefore, a replica can only calculate delays based on changes it has received. Network outages cause inaccuracy in delay metrics.

A replica calculates delay metrics based on times reflecting the following events:

* **t0**: the remote replica records the change in its data

* **t1**: the remote replica sends the change to a replica server

  (This time isn't necessary to calculate the delays in the metrics.)

* **t2**: the local replica receives the change from a replica server

* **t3**: the local replica applies the change to its data

This figure illustrates when these events occur:

![Replication change processing events](../_images/repl-delay.svg)

Replication keeps track of changes using CSNs *(tooltip: \<div class="paragraph">
\<p>An opaque string uniquely identifying a single change to directory data and when it occurred.\</p>
\</div>)*, opaque and unique identifiers for each change that indicate when and where each change first occurred. The **tn** values are CSNs.

When the CSNs for the last change received and the last change replayed are identical, the replica has applied all the changes it has received. In this case, there is no known delay. The receive and replay delay metrics are set to 0 (zero).

When the last received and last replayed CSNs differ:

* *Receive delay* is set to the time **t2** - **t0** for the last change received.

  Another name for receive delay is current delay.

* *Replay delay* is the absolute value of **t3** for the last change replayed - **t2** for the last change received. In other words, it is an approximation of how long it takes for DS to replay a change. Bursty traffic can generate spikes in replay delay that aren't a symptom of a replication problem.

As long as replication delay tends toward zero regularly and over the long term, temporary spikes and increases in delay measurements are normal. When all replicas remain connected and yet replication delay remains high and increases over the long term, the high replication delay indicates a problem. Steadily high and increasing replication delay shows that replication is not converging, and the service is failing to achieve eventual consistency.

For a current snapshot of replication delays, you can also use the `dsrepl status` command. Learn more in [Replication status](../config-guide/repl-status.html).

### Replication status (LDAP)

The following example uses the default monitor user account to check the replication status of the local replica:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=monitor \
 --bindPassword password \
 --baseDN cn=monitor \
 "(ds-mon-status=*)" \
 ds-mon-status
```

> **Collapse: Show output**
>
> ```
> dn: ds-mon-domain-name=dc=example\,dc=com,cn=replicas,cn=replication,cn=monitor
> ds-mon-status: Normal
> ```

|   |                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The values in the `Status` column of the command output don't necessarily match the monitoring attribute values.Learn more in the [dsrepl status](../tools-reference/dsrepl.html#dsrepl_status) command reference. |

If the status is not `Normal`, how you react depends on the value of the `ds-mon-status` attribute for LDAP, or `ds_replication_replica_status{status}` for Prometheus.

| Status          | Explanation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Actions to take                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Bad data`      | Replication is broken.Internally, DS replicas store a shorthand form of the initial state called a *generation ID*. The generation ID is a hash of the first 1000 entries in a backend, combined with the total number of entries. When the replicas' generation IDs match, the servers can replicate data without user intervention. When the replicas' generation IDs don't match for a given backend, the servers can't replicate the data.This status arises for one of the following reasons:- The replica and the replication server have different generation IDs for the data because the replica began with different data than its peer replicas.

- The fractional replication configuration for this replica doesn't match the backend data. For example, you reconfigured fractional replication to include or exclude different attributes, or you configured fractional replication incompatibly on different peer replicas.You must intervene to make sure the replicas with bad data start from the same initial state as their peers. Follow the suggested actions to take. Don't replace or reinitialize the backend data alone. DS stores the generation ID in the backend and in the changelog. The generation IDs in the backend and in the changelog must match on all peer replicas.DS 7.3 introduced this status. Earlier releases included this state as part of the `Bad generation id` status. | Whenever this status displays:1) If fractional replication is configured, make sure the configuration is compatible on all peer replicas.

   Learn more in [Fractional replication (advanced)](../config-guide/repl-fractional.html).

2) Initialize the replica with `Bad data` online from a replica with good data.

   Use the `dsrepl initialize` command to initialize the single bad replica. This fixes the bad generation IDs, correcting the problem in the backend and changelog data.

   Find an example in [Initialize over the network](../config-guide/repl-init.html#init-repl-online).

   If you can't initialize the replica with `Bad data` online, [remove it](../install-guide/uninstall.html) and [replace it with a new replica](../config-guide/repl-add-replica.html). |
| `Full update`   | Replication is operating normally.You have chosen to initialize replication over the network.The time to complete the operation depends on the network bandwidth and volume of data to synchronize.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Monitor the server output and wait for initialization to complete.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `Invalid`       | This status arises for one of the following reasons:- The replica has encountered a replication protocol error. This status can arise due to faulty network communication between the replica and the replication server.

- The replica has just started, and is initializing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | If this status happens during normal operation:1) Review the replica and replication server error logs, described in [About logs](../logging-guide/about-logs.html), for network-related replication error messages.

2) Independently verify network communication between the replica and the replication server systems.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `Normal`        | Replication is operating normally.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Nothing to do.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `Not connected` | This status arises for one of the following reasons:- The replica has just started and is not yet connected to the replication server.

- The replica cannot connect to a replication server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | If this status happens during normal operation:1) Review the replica and replication server error logs for network-related replication error messages.

2) Independently verify network communication between the replica and the replication server systems.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `Too late`      | The replica has fallen further behind the replication server than allowed by the [replication-purge-delay](../configref/objects-replication-synchronization-provider.html#replication-purge-delay). In other words, the replica is missing too many changes, and lacks the historical information required to synchronize with peer replicas.The replica no longer receives updates from replication servers. Other replicas that recognize this status stop returning referrals to this replica.DS 7.3 introduced this status. Earlier releases included this state as part of the `Bad generation id` status.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Whenever this status displays:1) Reinitialize replication for the replica that is too late.

   Learn more in [Manual initialization](../config-guide/repl-init.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

## Monitor privilege

The following example assigns the required privilege to Kirsten Vaughan's entry to read monitoring data, and shows monitoring information for the backend holding Example.com data:

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=admin \
 --bindPassword password << EOF
dn: uid=kvaughan,ou=People,dc=example,dc=com
changetype: modify
add: ds-privilege-name
ds-privilege-name: monitor-read
EOF
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 --baseDN cn=monitor \
 "(ds-cfg-backend-id=dsEvaluation)"
```

> **Collapse: Show output**
>
> ```
> dn: ds-cfg-backend-id=dsEvaluation,cn=backends,cn=monitor
> objectClass: top
> objectClass: ds-monitor
> objectClass: ds-monitor-backend
> objectClass: ds-monitor-backend-pluggable
> objectClass: ds-monitor-backend-db
> ds-cfg-backend-id: dsEvaluation
> ds-mon-backend-degraded-index-count: <number>
> ds-mon-backend-entry-count: <number>
> ds-mon-backend-entry-size-read: <json>
> ds-mon-backend-entry-size-written: <json>
> ds-mon-backend-filter-indexed: <number>
> ds-mon-backend-filter-unindexed: <number>
> ds-mon-backend-filter-use-start-time: <timestamp>
> ds-mon-backend-is-private: <boolean>
> ds-mon-backend-ttl-entries-deleted: <json>
> ds-mon-backend-ttl-is-running: <boolean>
> ds-mon-backend-ttl-last-run-time: <timestamp>
> ds-mon-backend-ttl-queue-size: <number>
> ds-mon-backend-ttl-thread-count: <number>
> ds-mon-backend-untrusted-index-count: <number>
> ds-mon-backend-writability-mode: enabled
> ds-mon-db-cache-evict-internal-nodes-count: <number>
> ds-mon-db-cache-evict-leaf-nodes-count: <number>
> ds-mon-db-cache-leaf-nodes: <boolean>
> ds-mon-db-cache-misses-internal-nodes: <number>
> ds-mon-db-cache-misses-leaf-nodes: <number>
> ds-mon-db-cache-size-active: <number>
> ds-mon-db-cache-size-total: <number>
> ds-mon-db-cache-total-tries-internal-nodes: <number>
> ds-mon-db-cache-total-tries-leaf-nodes: <number>
> ds-mon-db-checkpoint-count: <number>
> ds-mon-db-log-cleaner-file-deletion-count: <number>
> ds-mon-db-log-files-open: <number>
> ds-mon-db-log-files-opened: <number>
> ds-mon-db-log-size-active: <number>
> ds-mon-db-log-size-total: <number>
> ds-mon-db-log-utilization-max: <number>
> ds-mon-db-log-utilization-min: <number>
> ds-mon-db-version: <version>
> ```

---

---
title: Metric types reference
description: "Reference for PingDS monitoring metric types: counter, gauge, histogram, summary, and timer formats over LDAP and Prometheus."
component: pingds
version: 8.1
page_id: pingds:monitoring-guide:monitoring-types
canonical_url: https://docs.pingidentity.com/pingds/8.1/monitoring-guide/monitoring-types.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["LDAP", "Monitoring", "REST API"]
---

# Metric types reference

The following monitoring metrics are available in each interface:

| Type      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Counter   | Cumulative metric for a numerical value that only increases while the server is running.Counts that reflect volatile data, such as the number of requests, are reset to 0 when the server starts up.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Gauge     | Metric for a numerical value that can increase or decrease.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Histogram | Metric that samples observations, and counts them in buckets, as well as providing a sum of all observed values.LDAP metrics show histograms as JSON objects. JSON histograms for entry sizes (in bytes) have the following fields:(1)```none
{
  "count": number,      // Number of events since the server started
  "sum": number,        // Sum of quantities measured for each event
                        // since the server started
  // The buckets in a histogram depend on what the server observes.
  // Each bucket for an entry size measurement has a ceiling size.
  // The first field shows the number of 500-byte or smaller entries,
  // and the second shows the number of 1000-byte or smaller entries.
  // The final field shows the number of entries larger than
  // 1,000,000 bytes:
  "less-than-or-equal-to-500": number,
  "less-than-or-equal-to-1000": number,
  "less-than-or-equal-to-5000": number,
  "less-than-or-equal-to-10000": number,
  "less-than-or-equal-to-50000": number,
  "less-than-or-equal-to-100000": number,
  "less-than-or-equal-to-500000": number,
  "less-than-or-equal-to-1000000": number,
  "less-than-or-equal-to-inf": number
}
```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Summary   | Metric that samples observations, providing a count of observations, sum total of observed amounts, average rate of events, and moving average rates across sliding time windows.LDAP metrics show summaries as JSON objects. JSON summaries have the following fields:(1)```none
{
  "count": number,      // Number of events since the server started
  "total": number,      // Sum of quantities measured for each event
                        // since the server started
  // The following are related to the "count":
  "mean_rate": number,  // Average event rate per second
                        // since the server started
  "m1_rate": number,    // One-minute average event rate per second
                        // (exponentially decaying)
  "m5_rate": number,    // Five-minute average event rate per second
                        // (exponentially decaying)
  "m15_rate": number,   // Fifteen-minute average event rate per second
                        // (exponentially decaying)
}
```The `"total"` depends on the type of events measured. For example, if the `"count"` is the number of requests, then the `"total"` is the total elapsed time (etime) *(tooltip: \<div class="paragraph">&#xA;\<p>Time to process a request, starting from the moment a worker thread can process the decoded operation.\</p>&#xA;\</div>)* in milliseconds to process all the requests. If the `"count"` is the number of times the server read bytes of data, then the `"total"` is the total number of bytes read.The Prometheus view does not provide time-based statistics, as rates can be calculated from the time-series data. Instead, the Prometheus view includes summary metrics whose names have the following suffixes or labels:- `_count`: number of events since the server started

- `_total`: sum of quantities measured for each event since the server started

- `{quantile="0.5"}`: 50% at or below this value since the server started

- `{quantile="0.75"}`: 75% at or below this value since the server started

- `{quantile="0.95"}`: 95% at or below this value since the server started

- `{quantile="0.98"}`: 98% at or below this value since the server started

- `{quantile="0.99"}`: 99% at or below this value since the server started

- `{quantile="0.999"}`: 99.9% at or below this value since the server started                                                                                                                                                                                                                                                                      |
| Timer     | Metric combining a summary with other statistics.LDAP metrics show summaries as JSON objects. JSON summaries have the following fields(1)```none
{
  "count": number,     // Number of events since the server started
  "total": number,     // Total duration for all events
                       // since the server started, in ms
                       // (for requests, sum of the etimes
                       // since the server started, in ms)
  // The following are related to the "count":
  "mean_rate": number, // Average event rate per second
                       // since the server started
  "m1_rate": number,   // One-minute average event rate per second
                       // (exponentially decaying)
  "m5_rate": number,   // Five-minute average event rate per second
                       // (exponentially decaying)
  "m15_rate": number,  // Fifteen-minute average event rate per second
                       // (exponentially decaying)
  // The following are related to the "total":
  "mean": number,      // Average duration over all events
                       // since the server started, in ms
  "min": number,       // Minimum duration recorded
                       // since the server started, in ms
  "max": number,       // Maximum duration recorded
                       // since the server started, in ms
  "stddev": number,    // Standard deviation of durations
                       // since the server started, in ms
  "p50": number,       // 50% durations at or below this value
                       // (median) since the server started, in ms
  "p75": number,       // 75% durations at or below this value
                       // since the server started, in ms
  "p95": number,       // 95% durations at or below this value
                       // since the server started, in ms
  "p98": number,       // 98% durations at or below this value
                       // since the server started, in ms
  "p99": number,       // 99% durations at or below this value
                       // since the server started, in ms
  "p999": number,      // 99.9% durations at or below this value
                       // since the server started, in ms
  "p9999": number,     // 99.99% durations at or below this value
                       // since the server started, in ms
  "p99999": number     // 99.999% durations at or below this value
                       // since the server started, in ms
}
```The Prometheus view does not provide time-based statistics. Rates can be calculated from the time-series data. |

(1) Monitoring metrics reflect sample observations made while the server is running. The values are not saved when the server shuts down. As a result, metrics of this type reflect data recorded since the server started.

Metrics that show etime measurements in milliseconds (ms) continue to show values in ms even if the server is configured to log etimes in nanoseconds.

The calculation of moving averages is intended to be the same as that of the `uptime` and `top` commands, where the moving average plotted over time is smoothed by weighting that decreases exponentially. For an explanation of the mechanism, refer to the Wikipedia section, [Exponential moving average](http://en.wikipedia.org/wiki/Moving_average#Exponential_moving_average).

---

---
title: Monitoring
description: Overview of monitoring PingDS servers, covering HTTP and LDAP interfaces, alerts, status, and metrics references.
component: pingds
version: 8.1
page_id: pingds:monitoring-guide:preface
canonical_url: https://docs.pingidentity.com/pingds/8.1/monitoring-guide/preface.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Monitoring"]
page_aliases: ["index.adoc"]
---

# Monitoring

These pages cover monitoring and alerts.

[icon: wrench, set=fas, size=3x]

#### [What to Monitor](security.html)

Things to key an eye on.

[icon: cloud, set=fas, size=3x]

#### [HTTP](http-monitoring.html)

Monitor DS over HTTP.

[icon: sitemap, set=fas, size=3x]

#### [LDAP](ldap-monitoring.html)

Monitor DS over LDAP.

[icon: info, set=fas, size=3x]

#### [Status/Tasks](monitoring-status-and-tasks.html)

About status and tasks.

[icon: exclamation-triangle, set=fas, size=3x]

#### [Alerts](alert-notifications.html)

Manage alerts.

[icon: list, set=fas, size=3x]

#### [Metrics](monitoring-types.html)

Reference for DS metrics.

---

---
title: Prometheus metrics reference
description: Reference listing of PingDS Prometheus metrics available at the /metrics/prometheus/0.0.4 endpoint.
component: pingds
version: 8.1
page_id: pingds:monitoring-guide:monitoring-metrics-prometheus
canonical_url: https://docs.pingidentity.com/pingds/8.1/monitoring-guide/monitoring-metrics-prometheus.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Monitoring", "REST API"]
---

# Prometheus metrics reference

This page lists Prometheus metrics:

* This page shows labels in braces; for example, the labels in `ds_backend_db_cache_misses_internal_nodes{backend,type}` are `backend` and `type`.

* Time gauges whose names end in `_seconds` indicate seconds since 1 Jan 1970 UTC; for example `ds_current_time_seconds 1679472039` means Wed, 22 Mar 2023 08:00:39.

Find examples of common monitoring requests in [HTTP-based monitoring](http-monitoring.html).

|   |                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Some `ds_jvm_*` metrics depend on the JVM version and configuration. In particular, GC-related metrics depend on the garbage collector that the server uses. The GC metric names are *unstable*, and can change even in a minor JVM release. |

| Name                                                                                                               | Type      | Description                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ds_acis_count{type}`                                                                                              | Gauge     | Total number of ACIs of the specified type                                                                                                                                                                                                                                            |
| `ds_admin_connector_connections`                                                                                   | Gauge     | Number of connections currently established on the Administration Connector                                                                                                                                                                                                           |
| `ds_all_entry_caches_cache_entry_count`                                                                            | Gauge     | Current number of entries held in this cache                                                                                                                                                                                                                                          |
| `ds_all_entry_caches_cache_misses_count`                                                                           | Summary   | Number of attempts to retrieve an entry that was not held in this cache                                                                                                                                                                                                               |
| `ds_all_entry_caches_cache_misses_sum`                                                                             | Summary   | Number of attempts to retrieve an entry that was not held in this cache                                                                                                                                                                                                               |
| `ds_all_entry_caches_cache_size_bytes`                                                                             | Gauge     | Total memory in bytes used by this cache                                                                                                                                                                                                                                              |
| `ds_all_entry_caches_cache_total_tries_count`                                                                      | Summary   | Number of attempts to retrieve an entry from this cache                                                                                                                                                                                                                               |
| `ds_all_entry_caches_cache_total_tries_sum`                                                                        | Summary   | Number of attempts to retrieve an entry from this cache                                                                                                                                                                                                                               |
| `ds_backend_db_cache_evict_internal_nodes_count{backend,type}`                                                     | Gauge     | Number of internal nodes evicted from the database cache                                                                                                                                                                                                                              |
| `ds_backend_db_cache_evict_leaf_nodes_count{backend,type}`                                                         | Gauge     | Number of leaf nodes (data records) evicted from the database cache                                                                                                                                                                                                                   |
| `ds_backend_db_cache_leaf_nodes{backend,type}`                                                                     | Gauge     | Whether leaf nodes are cached                                                                                                                                                                                                                                                         |
| `ds_backend_db_cache_misses_internal_nodes{backend,type}`                                                          | Gauge     | Number of internal nodes requested by btree operations that were not in the database cache                                                                                                                                                                                            |
| `ds_backend_db_cache_misses_leaf_nodes{backend,type}`                                                              | Gauge     | Number of leaf nodes (data records) requested by btree operations that were not in the database cache                                                                                                                                                                                 |
| `ds_backend_db_cache_size_active_bytes{backend,type}`                                                              | Gauge     | Size of the database cache                                                                                                                                                                                                                                                            |
| `ds_backend_db_cache_size_total_bytes{backend,type}`                                                               | Gauge     | Maximum size of the database cache                                                                                                                                                                                                                                                    |
| `ds_backend_db_cache_total_tries_internal_nodes{backend,type}`                                                     | Gauge     | Number of internal nodes requested by btree operations                                                                                                                                                                                                                                |
| `ds_backend_db_cache_total_tries_leaf_nodes{backend,type}`                                                         | Gauge     | Number of leaf nodes (data records) requested by btree operations                                                                                                                                                                                                                     |
| `ds_backend_db_checkpoint_count{backend,type}`                                                                     | Gauge     | Number of checkpoints run so far                                                                                                                                                                                                                                                      |
| `ds_backend_db_log_cleaner_file_deletion_count{backend,type}`                                                      | Gauge     | Number of cleaner file deletions                                                                                                                                                                                                                                                      |
| `ds_backend_db_log_files_opened{backend,type}`                                                                     | Gauge     | Number of times a log file has been opened                                                                                                                                                                                                                                            |
| `ds_backend_db_log_files_open{backend,type}`                                                                       | Gauge     | Number of files currently open in the database file cache                                                                                                                                                                                                                             |
| `ds_backend_db_log_size_active_bytes{backend,type}`                                                                | Gauge     | Estimate of the amount in bytes of live data in all data files (i.e., the size of the DB, ignoring garbage)                                                                                                                                                                           |
| `ds_backend_db_log_size_total_bytes{backend,type}`                                                                 | Gauge     | Size used by all data files on disk                                                                                                                                                                                                                                                   |
| `ds_backend_db_log_utilization_max{backend,type}`                                                                  | Gauge     | Current maximum (upper bound) log utilization as a percentage                                                                                                                                                                                                                         |
| `ds_backend_db_log_utilization_min{backend,type}`                                                                  | Gauge     | Current minimum (lower bound) log utilization as a percentage                                                                                                                                                                                                                         |
| `ds_backend_degraded_index_count{backend,type}` (deprecated)                                                       | Gauge     | Number of untrusted indexes in the backend                                                                                                                                                                                                                                            |
| `ds_backend_entry_count{backend,base_dn,type}`                                                                     | Gauge     | Number of subordinate entries of the base DN, including the base DN                                                                                                                                                                                                                   |
| `ds_backend_entry_size_read_bucket{backend,type,le}`                                                               | Histogram | Histogram of entry sizes being read from the underlying storage                                                                                                                                                                                                                       |
| `ds_backend_entry_size_read_count{backend,type}`                                                                   | Histogram | Histogram of entry sizes being read from the underlying storage                                                                                                                                                                                                                       |
| `ds_backend_entry_size_read_sum{backend,type}`                                                                     | Histogram | Histogram of entry sizes being read from the underlying storage                                                                                                                                                                                                                       |
| `ds_backend_entry_size_written_bucket{backend,type,le}`                                                            | Histogram | Histogram of entry sizes being written to the underlying storage                                                                                                                                                                                                                      |
| `ds_backend_entry_size_written_count{backend,type}`                                                                | Histogram | Histogram of entry sizes being written to the underlying storage                                                                                                                                                                                                                      |
| `ds_backend_entry_size_written_sum{backend,type}`                                                                  | Histogram | Histogram of entry sizes being written to the underlying storage                                                                                                                                                                                                                      |
| `ds_backend_filter_indexed{backend,type}`                                                                          | Gauge     | Number of indexed searches performed against the backend                                                                                                                                                                                                                              |
| `ds_backend_filter_unindexed{backend,type}`                                                                        | Gauge     | Number of unindexed searches performed against the backend                                                                                                                                                                                                                            |
| `ds_backend_filter_use_start_time_seconds{backend,type}`                                                           | Gauge     | Time the server started recording statistical information about the simple search filters processed against the backend                                                                                                                                                               |
| `ds_backend_index_cost_seconds_count{backend,base_dn,index,type}`                                                  | Summary   | Number of index updates and their time cost                                                                                                                                                                                                                                           |
| `ds_backend_index_cost_seconds_sum{backend,base_dn,index,type}`                                                    | Summary   | Number of index updates and their time cost                                                                                                                                                                                                                                           |
| `ds_backend_index_cost_seconds{backend,base_dn,index,type,quantile}`                                               | Summary   | Number of index updates and their time cost                                                                                                                                                                                                                                           |
| `ds_backend_index_uses_count{backend,base_dn,index,type}`                                                          | Summary   | Number of accesses of this index. For attribute indexes it represents the number of search operations that have used this index, for system indexes it represents the number of key lookups.                                                                                          |
| `ds_backend_index_uses_sum{backend,base_dn,index,type}`                                                            | Summary   | Number of accesses of this index. For attribute indexes it represents the number of search operations that have used this index, for system indexes it represents the number of key lookups.                                                                                          |
| `ds_backend_is_private{backend,type}`                                                                              | Gauge     | Whether the base DNs of this backend should be considered public or private                                                                                                                                                                                                           |
| `ds_backend_ttl_entries_deleted_count{backend,type}`                                                               | Summary   | Summary for entries purged by time-to-live                                                                                                                                                                                                                                            |
| `ds_backend_ttl_entries_deleted_sum{backend,type}`                                                                 | Summary   | Summary for entries purged by time-to-live                                                                                                                                                                                                                                            |
| `ds_backend_ttl_is_running{backend,type}`                                                                          | Gauge     | Indicates whether time-to-live is in the process of purging expired entries                                                                                                                                                                                                           |
| `ds_backend_ttl_last_run_time_seconds{backend,type}`                                                               | Gauge     | Last time time-to-live finished purging expired entries                                                                                                                                                                                                                               |
| `ds_backend_ttl_queue_size{backend,type}`                                                                          | Gauge     | Number of entries queued for purging by the time-to-live service                                                                                                                                                                                                                      |
| `ds_backend_ttl_thread_count{backend,type}`                                                                        | Gauge     | Number of active time-to-live threads                                                                                                                                                                                                                                                 |
| `ds_backend_untrusted_index_count{backend,type}`                                                                   | Gauge     | Number of untrusted indexes in the backend                                                                                                                                                                                                                                            |
| `ds_certificates_certificate_expires_at_seconds{alias,key_manager}`                                                | Gauge     | Time the certificate expires                                                                                                                                                                                                                                                          |
| `ds_connection_handlers_http_active_connections_count{http_handler}`                                               | Gauge     | Number of active client connections                                                                                                                                                                                                                                                   |
| `ds_connection_handlers_http_bytes_read_count{http_handler}`                                                       | Summary   | Network bytes read summary                                                                                                                                                                                                                                                            |
| `ds_connection_handlers_http_bytes_read_sum{http_handler}`                                                         | Summary   | Network bytes read summary                                                                                                                                                                                                                                                            |
| `ds_connection_handlers_http_bytes_written_count{http_handler}`                                                    | Summary   | Network bytes written summary                                                                                                                                                                                                                                                         |
| `ds_connection_handlers_http_bytes_written_sum{http_handler}`                                                      | Summary   | Network bytes written summary                                                                                                                                                                                                                                                         |
| `ds_connection_handlers_http_requests_failure_seconds_count{http_handler,type}`                                    | Summary   | Timer for requests that failed because there was a problem while attempting to perform the associated operation (associated LDAP result codes: 1, 2, 12, 15, 16, 17, 18, 19, 20, 21, 23, 34, 35, 36, 37, 38, 39; associated HTTP status codes: client error (4xx) except 401 and 403) |
| `ds_connection_handlers_http_requests_failure_seconds_sum{http_handler,type}`                                      | Summary   | Timer for requests that failed because there was a problem while attempting to perform the associated operation (associated LDAP result codes: 1, 2, 12, 15, 16, 17, 18, 19, 20, 21, 23, 34, 35, 36, 37, 38, 39; associated HTTP status codes: client error (4xx) except 401 and 403) |
| `ds_connection_handlers_http_requests_failure_seconds{http_handler,type,quantile}`                                 | Summary   | Timer for requests that failed because there was a problem while attempting to perform the associated operation (associated LDAP result codes: 1, 2, 12, 15, 16, 17, 18, 19, 20, 21, 23, 34, 35, 36, 37, 38, 39; associated HTTP status codes: client error (4xx) except 401 and 403) |
| `ds_connection_handlers_http_requests_seconds_count{http_handler,type}`                                            | Summary   | Timer for the specified request type                                                                                                                                                                                                                                                  |
| `ds_connection_handlers_http_requests_seconds_sum{http_handler,type}`                                              | Summary   | Timer for the specified request type                                                                                                                                                                                                                                                  |
| `ds_connection_handlers_http_requests_seconds{http_handler,type,quantile}`                                         | Summary   | Timer for the specified request type                                                                                                                                                                                                                                                  |
| `ds_connection_handlers_ldap_abandoned_requests_total{ldap_handler}`                                               | Counter   | Total number of abandoned operations since startup                                                                                                                                                                                                                                    |
| `ds_connection_handlers_ldap_abandoned_requests{ldap_handler}` (deprecated)                                        | Counter   | Total number of abandoned operations since startup                                                                                                                                                                                                                                    |
| `ds_connection_handlers_ldap_active_connections_count{ldap_handler}`                                               | Gauge     | Number of active client connections                                                                                                                                                                                                                                                   |
| `ds_connection_handlers_ldap_active_persistent_searches{ldap_handler}`                                             | Gauge     | Number of active persistent searches                                                                                                                                                                                                                                                  |
| `ds_connection_handlers_ldap_bytes_read_count{ldap_handler}`                                                       | Summary   | Network bytes read summary                                                                                                                                                                                                                                                            |
| `ds_connection_handlers_ldap_bytes_read_sum{ldap_handler}`                                                         | Summary   | Network bytes read summary                                                                                                                                                                                                                                                            |
| `ds_connection_handlers_ldap_bytes_written_count{ldap_handler}`                                                    | Summary   | Network bytes written summary                                                                                                                                                                                                                                                         |
| `ds_connection_handlers_ldap_bytes_written_sum{ldap_handler}`                                                      | Summary   | Network bytes written summary                                                                                                                                                                                                                                                         |
| `ds_connection_handlers_ldap_connections_count{ldap_handler}`                                                      | Summary   | Connection summary                                                                                                                                                                                                                                                                    |
| `ds_connection_handlers_ldap_connections_sum{ldap_handler}`                                                        | Summary   | Connection summary                                                                                                                                                                                                                                                                    |
| `ds_connection_handlers_ldap_requests_failure_seconds_count{ldap_handler,type}`                                    | Summary   | Timer for requests that failed because there was a problem while attempting to perform the associated operation (associated LDAP result codes: 1, 2, 12, 15, 16, 17, 18, 19, 20, 21, 23, 34, 35, 36, 37, 38, 39; associated HTTP status codes: client error (4xx) except 401 and 403) |
| `ds_connection_handlers_ldap_requests_failure_seconds_sum{ldap_handler,type}`                                      | Summary   | Timer for requests that failed because there was a problem while attempting to perform the associated operation (associated LDAP result codes: 1, 2, 12, 15, 16, 17, 18, 19, 20, 21, 23, 34, 35, 36, 37, 38, 39; associated HTTP status codes: client error (4xx) except 401 and 403) |
| `ds_connection_handlers_ldap_requests_failure_seconds{ldap_handler,type,quantile}`                                 | Summary   | Timer for requests that failed because there was a problem while attempting to perform the associated operation (associated LDAP result codes: 1, 2, 12, 15, 16, 17, 18, 19, 20, 21, 23, 34, 35, 36, 37, 38, 39; associated HTTP status codes: client error (4xx) except 401 and 403) |
| `ds_connection_handlers_ldap_requests_seconds_count{ldap_handler,scope,type}`                                      | Summary   | Timer for the specified request type                                                                                                                                                                                                                                                  |
| `ds_connection_handlers_ldap_requests_seconds_count{ldap_handler,type}`                                            | Summary   | Timer for the specified request type                                                                                                                                                                                                                                                  |
| `ds_connection_handlers_ldap_requests_seconds_sum{ldap_handler,scope,type}`                                        | Summary   | Timer for the specified request type                                                                                                                                                                                                                                                  |
| `ds_connection_handlers_ldap_requests_seconds_sum{ldap_handler,type}`                                              | Summary   | Timer for the specified request type                                                                                                                                                                                                                                                  |
| `ds_connection_handlers_ldap_requests_seconds{ldap_handler,scope,type,quantile}`                                   | Summary   | Timer for the specified request type                                                                                                                                                                                                                                                  |
| `ds_connection_handlers_ldap_requests_seconds{ldap_handler,type,quantile}`                                         | Summary   | Timer for the specified request type                                                                                                                                                                                                                                                  |
| `ds_connection_handlers_unified_abandoned_requests_total{unified_handler}`                                         | Counter   | Total number of abandoned operations since startup                                                                                                                                                                                                                                    |
| `ds_connection_handlers_unified_abandoned_requests{unified_handler}`                                               | Counter   | Total number of abandoned operations since startup                                                                                                                                                                                                                                    |
| `ds_connection_handlers_unified_active_connections_count{unified_handler}`                                         | Gauge     | Number of active client connections                                                                                                                                                                                                                                                   |
| `ds_connection_handlers_unified_active_persistent_searches{unified_handler}`                                       | Gauge     | Number of active persistent searches                                                                                                                                                                                                                                                  |
| `ds_connection_handlers_unified_bytes_read_count{unified_handler}`                                                 | Summary   | Network bytes read summary                                                                                                                                                                                                                                                            |
| `ds_connection_handlers_unified_bytes_read_sum{unified_handler}`                                                   | Summary   | Network bytes read summary                                                                                                                                                                                                                                                            |
| `ds_connection_handlers_unified_bytes_written_count{unified_handler}`                                              | Summary   | Network bytes written summary                                                                                                                                                                                                                                                         |
| `ds_connection_handlers_unified_bytes_written_sum{unified_handler}`                                                | Summary   | Network bytes written summary                                                                                                                                                                                                                                                         |
| `ds_connection_handlers_unified_connections_count{unified_handler}`                                                | Summary   | Connection summary                                                                                                                                                                                                                                                                    |
| `ds_connection_handlers_unified_connections_sum{unified_handler}`                                                  | Summary   | Connection summary                                                                                                                                                                                                                                                                    |
| `ds_connection_handlers_unified_requests_failure_seconds_count{type,unified_handler}`                              | Summary   | Timer for requests that failed because there was a problem while attempting to perform the associated operation (associated LDAP result codes: 1, 2, 12, 15, 16, 17, 18, 19, 20, 21, 23, 34, 35, 36, 37, 38, 39; associated HTTP status codes: client error (4xx) except 401 and 403) |
| `ds_connection_handlers_unified_requests_failure_seconds_sum{type,unified_handler}`                                | Summary   | Timer for requests that failed because there was a problem while attempting to perform the associated operation (associated LDAP result codes: 1, 2, 12, 15, 16, 17, 18, 19, 20, 21, 23, 34, 35, 36, 37, 38, 39; associated HTTP status codes: client error (4xx) except 401 and 403) |
| `ds_connection_handlers_unified_requests_failure_seconds{type,unified_handler,quantile}`                           | Summary   | Timer for requests that failed because there was a problem while attempting to perform the associated operation (associated LDAP result codes: 1, 2, 12, 15, 16, 17, 18, 19, 20, 21, 23, 34, 35, 36, 37, 38, 39; associated HTTP status codes: client error (4xx) except 401 and 403) |
| `ds_connection_handlers_unified_requests_seconds_count{scope,type,unified_handler}`                                | Summary   | Timer for the specified request type                                                                                                                                                                                                                                                  |
| `ds_connection_handlers_unified_requests_seconds_count{type,unified_handler}`                                      | Summary   | Timer for the specified request type                                                                                                                                                                                                                                                  |
| `ds_connection_handlers_unified_requests_seconds_sum{scope,type,unified_handler}`                                  | Summary   | Timer for the specified request type                                                                                                                                                                                                                                                  |
| `ds_connection_handlers_unified_requests_seconds_sum{type,unified_handler}`                                        | Summary   | Timer for the specified request type                                                                                                                                                                                                                                                  |
| `ds_connection_handlers_unified_requests_seconds{scope,type,unified_handler,quantile}`                             | Summary   | Timer for the specified request type                                                                                                                                                                                                                                                  |
| `ds_connection_handlers_unified_requests_seconds{type,unified_handler,quantile}`                                   | Summary   | Timer for the specified request type                                                                                                                                                                                                                                                  |
| `ds_current_connections`                                                                                           | Gauge     | Number of client connections currently established except on the Administration Connector                                                                                                                                                                                             |
| `ds_current_time_seconds`                                                                                          | Gauge     | Current time                                                                                                                                                                                                                                                                          |
| `ds_disk_free_space_bytes{disk}`                                                                                   | Gauge     | Amount of free disk space                                                                                                                                                                                                                                                             |
| `ds_disk_free_space_full_threshold_bytes{disk}`                                                                    | Gauge     | Effective full disk space threshold                                                                                                                                                                                                                                                   |
| `ds_disk_free_space_low_threshold_bytes{disk}`                                                                     | Gauge     | Effective low disk space threshold                                                                                                                                                                                                                                                    |
| `ds_entries_with_aci_attributes_count`                                                                             | Gauge     | Total number of entries with ACI attributes                                                                                                                                                                                                                                           |
| `ds_entry_cache_entry_count{cache}`                                                                                | Gauge     | Current number of entries held in this cache                                                                                                                                                                                                                                          |
| `ds_entry_cache_max_entry_count{cache}`                                                                            | Gauge     | Maximum number of entries allowed in this cache                                                                                                                                                                                                                                       |
| `ds_entry_cache_max_size_bytes{cache}`                                                                             | Gauge     | Memory limit for this cache                                                                                                                                                                                                                                                           |
| `ds_entry_cache_misses_count{cache}`                                                                               | Summary   | Number of attempts to retrieve an entry that was not held in this cache                                                                                                                                                                                                               |
| `ds_entry_cache_misses_sum{cache}`                                                                                 | Summary   | Number of attempts to retrieve an entry that was not held in this cache                                                                                                                                                                                                               |
| `ds_entry_cache_size_bytes{cache}`                                                                                 | Gauge     | Total memory in bytes used by this cache                                                                                                                                                                                                                                              |
| `ds_entry_cache_total_tries_count{cache}`                                                                          | Summary   | Number of attempts to retrieve an entry from this cache                                                                                                                                                                                                                               |
| `ds_entry_cache_total_tries_sum{cache}`                                                                            | Summary   | Number of attempts to retrieve an entry from this cache                                                                                                                                                                                                                               |
| `ds_groups_count{type}`                                                                                            | Gauge     | Total number of groups of the specified type                                                                                                                                                                                                                                          |
| `ds_health_status_alive`                                                                                           | Gauge     | Indicates whether the server is alive                                                                                                                                                                                                                                                 |
| `ds_health_status_healthy`                                                                                         | Gauge     | Indicates whether the server is able to handle requests                                                                                                                                                                                                                               |
| `ds_jvm_available_cpus`                                                                                            | Gauge     | Number of processors available to the Java virtual machine                                                                                                                                                                                                                            |
| `ds_jvm_classes_loaded`                                                                                            | Gauge     | Number of classes loaded since the Java virtual machine started                                                                                                                                                                                                                       |
| `ds_jvm_classes_unloaded`                                                                                          | Gauge     | Number of classes unloaded since the Java virtual machine started                                                                                                                                                                                                                     |
| `ds_jvm_memory_heap_init_bytes`                                                                                    | Gauge     | Amount of heap memory that the Java virtual machine initially requested from the operating system                                                                                                                                                                                     |
| `ds_jvm_memory_heap_max_bytes`                                                                                     | Gauge     | Maximum amount of heap memory that the Java virtual machine will attempt to use                                                                                                                                                                                                       |
| `ds_jvm_memory_heap_reserved_bytes`                                                                                | Gauge     | Amount of heap memory that is committed for the Java virtual machine to use                                                                                                                                                                                                           |
| `ds_jvm_memory_heap_used_bytes`                                                                                    | Gauge     | Amount of heap memory used by the Java virtual machine                                                                                                                                                                                                                                |
| `ds_jvm_memory_init_bytes`                                                                                         | Gauge     | Amount of memory that the Java virtual machine initially requested from the operating system                                                                                                                                                                                          |
| `ds_jvm_memory_max_bytes`                                                                                          | Gauge     | Maximum amount of memory that the Java virtual machine will attempt to use                                                                                                                                                                                                            |
| `ds_jvm_memory_non_heap_init_bytes`                                                                                | Gauge     | Amount of non-heap memory that the Java virtual machine initially requested from the operating system                                                                                                                                                                                 |
| `ds_jvm_memory_non_heap_max_bytes`                                                                                 | Gauge     | Maximum amount of non-heap memory that the Java virtual machine will attempt to use                                                                                                                                                                                                   |
| `ds_jvm_memory_non_heap_reserved_bytes`                                                                            | Gauge     | Amount of non-heap memory that is committed for the Java virtual machine to use                                                                                                                                                                                                       |
| `ds_jvm_memory_non_heap_used_bytes`                                                                                | Gauge     | Amount of non-heap memory used by the Java virtual machine                                                                                                                                                                                                                            |
| `ds_jvm_memory_reserved_bytes`                                                                                     | Gauge     | Amount of memory that is committed for the Java virtual machine to use                                                                                                                                                                                                                |
| `ds_jvm_memory_used_bytes`                                                                                         | Gauge     | Amount of memory used by the Java virtual machine                                                                                                                                                                                                                                     |
| `ds_jvm_threads_blocked_count`                                                                                     | Gauge     | Number of threads in the BLOCKED state                                                                                                                                                                                                                                                |
| `ds_jvm_threads_count`                                                                                             | Gauge     | Number of live threads including both daemon and non-daemon threads                                                                                                                                                                                                                   |
| `ds_jvm_threads_daemon_count`                                                                                      | Gauge     | Number of live daemon threads                                                                                                                                                                                                                                                         |
| `ds_jvm_threads_deadlock_count`                                                                                    | Gauge     | Number of deadlocked threads                                                                                                                                                                                                                                                          |
| `ds_jvm_threads_new_count`                                                                                         | Gauge     | Number of threads in the NEW state                                                                                                                                                                                                                                                    |
| `ds_jvm_threads_runnable_count`                                                                                    | Gauge     | Number of threads in the RUNNABLE state                                                                                                                                                                                                                                               |
| `ds_jvm_threads_terminated_count`                                                                                  | Gauge     | Number of threads in the TERMINATED state                                                                                                                                                                                                                                             |
| `ds_jvm_threads_timed_waiting_count`                                                                               | Gauge     | Number of threads in the TIMED\_WAITING state                                                                                                                                                                                                                                         |
| `ds_jvm_threads_waiting_count`                                                                                     | Gauge     | Number of threads in the WAITING state                                                                                                                                                                                                                                                |
| `ds_max_connections`                                                                                               | Gauge     | Maximum number of simultaneous client connections that have been established with the Directory Server                                                                                                                                                                                |
| `ds_replication_changelog_connected_changelogs_current_receive_window{changelog_id,domain_name}`                   | Gauge     | Current replication window size for receiving messages, indicating the number of replication messages a remote server can send before waiting on acknowledgement from this server. This does not depend on the TCP window size                                                        |
| `ds_replication_changelog_connected_changelogs_domain_generation_id{changelog_id,domain_name}`                     | Gauge     | Replication domain generation identifier                                                                                                                                                                                                                                              |
| `ds_replication_changelog_connected_changelogs_ssl_encryption{changelog_id,domain_name}`                           | Gauge     | Whether SSL encryption is used when exchanging messages with this server                                                                                                                                                                                                              |
| `ds_replication_changelog_connected_replicas_current_receive_window{domain_name,server_id}`                        | Gauge     | Current replication window size for receiving messages, indicating the number of replication messages a remote server can send before waiting on acknowledgement from this server. This does not depend on the TCP window size                                                        |
| `ds_replication_changelog_connected_replicas_domain_generation_id{domain_name,server_id}`                          | Gauge     | Replication domain generation identifier                                                                                                                                                                                                                                              |
| `ds_replication_changelog_connected_replicas_ssl_encryption{domain_name,server_id}`                                | Gauge     | Whether SSL encryption is used when exchanging messages with this server                                                                                                                                                                                                              |
| `ds_replication_changelog_domain_generation_id{domain_name}`                                                       | Gauge     | Replication domain generation identifier                                                                                                                                                                                                                                              |
| `ds_replication_changelog_newest_change_number`                                                                    | Gauge     | Newest change number present in the change number index database                                                                                                                                                                                                                      |
| `ds_replication_changelog_oldest_change_number`                                                                    | Gauge     | Oldest change number present in the change number index database                                                                                                                                                                                                                      |
| `ds_replication_changelog_replica_dbs_changelog_file_count{domain_name,server_id}`                                 | Gauge     | The number of changelog files containing updates generated by this replica. A value of zero indicates the replica did not generate any updates during the last purge delay interval                                                                                                   |
| `ds_replication_changelog_replica_dbs_newest_csn_timestamp_seconds{domain_name,server_id}`                         | Gauge     | Time of the newest CSN present in the replica database                                                                                                                                                                                                                                |
| `ds_replication_changelog_replica_dbs_oldest_csn_timestamp_seconds{domain_name,server_id}`                         | Gauge     | Time of the oldest CSN present in the replica database                                                                                                                                                                                                                                |
| `ds_replication_replica_current_receive_window{domain_name,server_id}`                                             | Gauge     | Current replication window size for receiving messages, indicating the number of replication messages a remote server can send before waiting on acknowledgement from this server. This does not depend on the TCP window size                                                        |
| `ds_replication_replica_domain_generation_id{domain_name,server_id}`                                               | Gauge     | Replication domain generation identifier                                                                                                                                                                                                                                              |
| `ds_replication_replica_entries_awaiting_updates_count{domain_name,server_id}`                                     | Gauge     | Number of entries for which an update operation has been received but not replayed yet by this replica                                                                                                                                                                                |
| `ds_replication_replica_lost_connections{domain_name,server_id}`                                                   | Gauge     | Number of times the replica lost its connection to the replication server                                                                                                                                                                                                             |
| `ds_replication_replica_remote_replicas_receive_delay_seconds{domain_name,remote_server_id,server_id}`             | Gauge     | Current local delay in receiving replicated operations                                                                                                                                                                                                                                |
| `ds_replication_replica_remote_replicas_replay_delay_seconds{domain_name,remote_server_id,server_id}`              | Gauge     | Current local delay in replaying replicated operations                                                                                                                                                                                                                                |
| `ds_replication_replica_remote_replicas_replayed_updates_seconds_count{domain_name,remote_server_id,server_id}`    | Summary   | Replay etime for updates that have been replayed on this replica                                                                                                                                                                                                                      |
| `ds_replication_replica_remote_replicas_replayed_updates_seconds_sum{domain_name,remote_server_id,server_id}`      | Summary   | Replay etime for updates that have been replayed on this replica                                                                                                                                                                                                                      |
| `ds_replication_replica_remote_replicas_replayed_updates_seconds{domain_name,remote_server_id,server_id,quantile}` | Summary   | Replay etime for updates that have been replayed on this replica                                                                                                                                                                                                                      |
| `ds_replication_replica_remote_replicas_updates_in_progress{domain_name,remote_server_id,server_id}`               | Gauge     | Number of remote updates received in the queue waiting to be replayed                                                                                                                                                                                                                 |
| `ds_replication_replica_remote_replicas_updates_in_queue{domain_name,remote_server_id,server_id}`                  | Gauge     | Number of remote updates received in the queue                                                                                                                                                                                                                                        |
| `ds_replication_replica_replayed_internal_updates_total{domain_name,server_id}`                                    | Counter   | Number of updates replayed on this replica which modify the internal state but not user data                                                                                                                                                                                          |
| `ds_replication_replica_replayed_internal_updates{domain_name,server_id}` (deprecated)                             | Counter   | Number of updates replayed on this replica which modify the internal state but not user data                                                                                                                                                                                          |
| `ds_replication_replica_replayed_updates_conflicts_resolved_total{domain_name,server_id}`                          | Counter   | Number of updates replayed on this replica for which replication naming conflicts have been resolved                                                                                                                                                                                  |
| `ds_replication_replica_replayed_updates_conflicts_resolved{domain_name,server_id}` (deprecated)                   | Counter   | Number of updates replayed on this replica for which replication naming conflicts have been resolved                                                                                                                                                                                  |
| `ds_replication_replica_replayed_updates_conflicts_unresolved_total{domain_name,server_id}`                        | Counter   | Number of updates replayed on this replica for which replication naming conflicts have not been resolved                                                                                                                                                                              |
| `ds_replication_replica_replayed_updates_conflicts_unresolved{domain_name,server_id}` (deprecated)                 | Counter   | Number of updates replayed on this replica for which replication naming conflicts have not been resolved                                                                                                                                                                              |
| `ds_replication_replica_replayed_updates_seconds_count{domain_name,server_id}`                                     | Summary   | Replay etime for updates that have been replayed on this replica                                                                                                                                                                                                                      |
| `ds_replication_replica_replayed_updates_seconds_sum{domain_name,server_id}`                                       | Summary   | Replay etime for updates that have been replayed on this replica                                                                                                                                                                                                                      |
| `ds_replication_replica_replayed_updates_seconds{domain_name,server_id,quantile}`                                  | Summary   | Replay etime for updates that have been replayed on this replica                                                                                                                                                                                                                      |
| `ds_replication_replica_sent_updates_total{domain_name,server_id}`                                                 | Counter   | Number of replication updates sent by this replica                                                                                                                                                                                                                                    |
| `ds_replication_replica_ssl_encryption{domain_name,server_id}`                                                     | Gauge     | Whether SSL encryption is used when exchanging messages with this server                                                                                                                                                                                                              |
| `ds_replication_replica_status_last_changed_seconds{domain_name,server_id}`                                        | Gauge     | Last time the replication status of the local replica changed                                                                                                                                                                                                                         |
| `ds_replication_replica_status{domain_name,server_id,status}`                                                      | Gauge     | Status of the specified replica                                                                                                                                                                                                                                                       |
| `ds_replication_replica_total_update_entry_count{domain_name,server_id}`                                           | Gauge     | The total number of entries to be processed when a total update is in progress                                                                                                                                                                                                        |
| `ds_replication_replica_total_update_entry_left{domain_name,server_id}`                                            | Gauge     | The number of entries still to be processed when a total update is in progress                                                                                                                                                                                                        |
| `ds_replication_replica_updates_already_in_progress_total{domain_name,server_id}`                                  | Counter   | Number of duplicate updates: updates received by this replica which cannot be applied because they are already in progress. Can happen when a directory server fails over to another replication server                                                                               |
| `ds_replication_replica_updates_already_in_progress{domain_name,server_id}` (deprecated)                           | Counter   | Number of duplicate updates: updates received by this replica which cannot be applied because they are already in progress. Can happen when a directory server fails over to another replication server                                                                               |
| `ds_replication_replica_updates_inbound_queue{domain_name,server_id}`                                              | Gauge     | Number of remote updates received from the replication server but not replayed yet on this replica                                                                                                                                                                                    |
| `ds_replication_replica_updates_outbound_queue{domain_name,server_id}`                                             | Gauge     | Number of local updates that are waiting to be sent to the replication server once they complete                                                                                                                                                                                      |
| `ds_start_time_seconds`                                                                                            | Gauge     | Time the Directory Server started                                                                                                                                                                                                                                                     |
| `ds_static_group_size_bucket{le}`                                                                                  | Gauge     | Number of static groups with at most the specified number of members                                                                                                                                                                                                                  |
| `ds_subentries_count{type}`                                                                                        | Gauge     | Total number of LDAP subentries of the specified type                                                                                                                                                                                                                                 |
| `ds_topology_servers_server_is_local{server_id}`                                                                   | Gauge     | Indicates whether this is the topology server that has handled the monitoring request                                                                                                                                                                                                 |
| `ds_total_connections`                                                                                             | Gauge     | Total number of client connections that have been established with the Directory Server since it started                                                                                                                                                                              |
| `ds_work_queue_requests_in_queue`                                                                                  | Gauge     | Number of requests in the work queue that have not yet been picked up for processing                                                                                                                                                                                                  |
| `ds_work_queue_requests_submitted_count`                                                                           | Summary   | Summary for operations that have been successfully submitted to the work queue                                                                                                                                                                                                        |
| `ds_work_queue_requests_submitted_sum`                                                                             | Summary   | Summary for operations that have been successfully submitted to the work queue                                                                                                                                                                                                        |

---

---
title: Push to Graphite
description: Deprecated. Configure PingDS to push monitoring metrics to Graphite using the Graphite Monitor Reporter plugin.
component: pingds
version: 8.1
page_id: pingds:monitoring-guide:graphite
canonical_url: https://docs.pingidentity.com/pingds/8.1/monitoring-guide/graphite.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Monitoring"]
---

# Push to Graphite

The [Graphite](https://graphiteapp.org/) application stores numeric time-series data of the sort produced by monitoring metrics, and allows you to render graphs of that data.

|   |                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | DS has deprecated support for Graphite and will remove it in a future release.Use [Prometheus](https://prometheus.io/) and the PromQL query language instead. |

Your applications, in this case DS servers, push data into Graphite. You do this by configuring the [Graphite Monitor Reporter Plugin (DEPRECATED)](../configref/objects-graphite-monitor-reporter-plugin.html) with the host and port number of the Graphite service, and with a prefix for your server, such as its FQDN. By default, the plugin pushes all metrics it produces to the Graphite service. You can opt to limit this by setting the `excluded-metric-pattern` or `included-metric-pattern` properties.

The following example configures the plugin to push metrics to Graphite at `graphite.example.com:2004` every 10 seconds (default):

```console
$ dsconfig \
 create-plugin \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --plugin-name Graphite \
 --type graphite-monitor-reporter \
 --set enabled:true \
 --set graphite-server:graphite.example.com:2004 \
 --set metric-name-prefix:ds.example.com \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
```

To view metrics stored in Graphite, you can use the Graphite render API or [Grafana](https://grafana.com/), for example. Learn more in the Graphite and Grafana documentation.

---

---
title: Status and tasks
description: Use the status and manage-tasks commands to check PingDS server configuration and manage scheduled tasks.
component: pingds
version: 8.1
page_id: pingds:monitoring-guide:monitoring-status-and-tasks
canonical_url: https://docs.pingidentity.com/pingds/8.1/monitoring-guide/monitoring-status-and-tasks.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Monitoring", "Troubleshooting"]
---

# Status and tasks

The `status` command functions in offline mode, but provides more information with the server is running. The command describes the server's capabilities, including the ports and disks it uses, and the backends it serves. With the `--script-friendly` option, the command returns JSON output. The command requires administrative credentials to read a running server's configuration:

```console
$ status \
 --bindDn uid=admin \
 --bindPassword password \
 --hostname localhost \
 --port 4444 \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --script-friendly
```

The `manage-tasks` command lets you manage scheduled [server tasks](../maintenance-guide/server-process.html#server-tasks), such as regular backup. The command connects to the administration port of a local or remote server:

```console
$ manage-tasks \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
```

---

---
title: What to monitor
description: Understand what to monitor in PingDS to detect availability problems, security threats, and performance issues.
component: pingds
version: 8.1
page_id: pingds:monitoring-guide:security
canonical_url: https://docs.pingidentity.com/pingds/8.1/monitoring-guide/security.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["LDAP", "Monitoring", "Security"]
---

# What to monitor

Monitor the directory service for the following reasons:

* Noticing availability problems as they occur.

  If a server becomes unresponsive, goes offline, or crashes, you discover the problem quickly, and take corrective action.

* Identifying how client applications use the directory service.

  You can parse directory access logs to determine what client applications do. This information helps you understand what is most important, and make decisions about indexing, for example.

  Access log messages can also provide evidence of security threats, and traces of insecure client application behavior.

* Spotting performance problems, where the directory service does not meet habitual, expected, or formally defined functional, throughput, or response time characteristics.

  For example, if it suddenly becomes impossible to perform updates, the directory service has a performance problem. Alternatively, if a search that regularly completes in 500 milliseconds now takes 15 seconds, the directory service has a performance problem.

  A performance problem could also be evidence of a security threat.

Monitoring directory security is thus part of an overall monitoring strategy. Aim to answer at least the following questions when monitoring specifically for security problems:

* What insecure client behaviors do you observe?

  Examples:

  * Attempts to send simple bind credentials over insecure connections

  * Attempts to change passwords over insecure connections

  * Attempts to change configuration over insecure connections

* What unusual or unexpected usage patterns do you observe?

  Examples:

  * Search requests that perform unindexed searches

  * Requests that hit resource limits

  * Unusually large numbers of bind requests that fail

  * Unusual large numbers of password change requests that fail

  * Unusual large numbers of account lockout *(tooltip: \<div class="paragraph">
    \<p>The act of making an account temporarily or permanently inactive after successive authentication failures.\</p>
    \</div>)* events

* Are you observing any sudden or hard-to-explain performance problems?

  Examples:

  * Unusual increases in throughput

  * Unusual increases in response times for typical requests

  * Servers suddenly starved for system resources

Keep in mind when you notice evidence of what looks like a security problem that it might be explained by a mistake made by an administrator or an application developer. Whether the problem is due to malice or user error, you can nevertheless use monitoring information to guide corrective actions.