---
title: About the collection of system monitoring data
description: All PingDirectory servers have the capability to monitor the health of the server and host system they run on for diagnostic review and troubleshooting.
component: pingdirectory
version: 11.1
page_id: pingdirectory:monitoring_the_pingdirectory_suite_of_products:pd_ds_collection_system_monitoring_data
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/monitoring_the_pingdirectory_suite_of_products/pd_ds_collection_system_monitoring_data.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# About the collection of system monitoring data

All PingDirectory servers have the capability to monitor the health of the server and host system they run on for diagnostic review and troubleshooting.

|   |                                                      |
| - | ---------------------------------------------------- |
|   | This topic applies only to the PingDirectory server. |

Initially, the servers do not collect any performance data until they are prepared for monitoring by a Metrics server using the `monitored-servers add-servers` tool or an administrator enables system health data collection for real-time inspection and querying. At a high level, all of the important server and machine metrics that can be monitored are available in the `cn=monitor` backend.

The Stats Collector plugin relies exclusively on entries in the `cn=monitor` backend to sample data using LDAP queries. The Stats Collector plugin is the primary driver of performance data collection for LDAP, server response, replication, local Java Runtime Environment (JRE) databases, and host system machine metrics. Stats Collector configuration determines the sample and collection intervals, granularity of data (basic, extended, verbose), types of host system collection (CPU, disk, network) and the type of data aggregation that occurs for LDAP application statistics. The Stats Collector plugin is configured with the `dsconfig` tool and collects data using LDAP queries.

For example, the `--server-info:extended` option includes collection for the following:

* CPU

* Java virtual machine (JVM) memory

* Memory

* Disk information

* Network information

Utilization metrics are gathered through externally invoked OS commands, such as `iostat` and `netstat`, using platform-specific arguments and version-specific output parsing.

Enabling the Host System monitor provider automatically gathers CPU and memory utilization but only optionally gathers disk and network information. Disk and network interfaces are enumerated in the configuration by device names, such as `eth0` or `lo`, and by disk device names, such as `sd1, sdab, sda2, scsi0`.

---

---
title: Accessing the Processing Time Histogram
description: The PingDirectory server provides a processing time histogram that classifies operation response time into user-defined buckets.
component: pingdirectory
version: 11.1
page_id: pingdirectory:monitoring_the_pingdirectory_suite_of_products:pd_ds_access_processing_time_histogram
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/monitoring_the_pingdirectory_suite_of_products/pd_ds_access_processing_time_histogram.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 12, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Accessing the Processing Time Histogram

The PingDirectory server provides a processing time histogram that classifies operation response time into user-defined buckets.

## About this task

The histogram tracks the processing on a per-operation basis and as a percentage of the overall processing time for all operations. It also provides statistics for each operation type:

* `add`

* `bind`

* `compare`

* `delete`

* `modify`

* `modifyDN`

* `search`

## Steps

1. From the admin console, go to **Configuration > Status > Monitors**.

2. Select **Processing Time Histogram**.

   |   |                                                       |
   | - | ----------------------------------------------------- |
   |   | You can access other monitor entries in similar ways. |

---

---
title: Configuring SNMP
description: Because all server instances provide information for a common set of management information bases (MIBs), each server instance provides its information under a unique SNMPv3 context name equal to the server instance name.
component: pingdirectory
version: 11.1
page_id: pingdirectory:monitoring_the_pingdirectory_suite_of_products:pd_ds_config_snmp
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/monitoring_the_pingdirectory_suite_of_products/pd_ds_config_snmp.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 14, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  example: Example:
  result: Result:
  example-2: Example:
  example-3: Example:
  example-4: Example:
  example-5: Example:
  result-2: Result:
  example-6: Example:
  example-7: Example:
  example-8: Example:
---

# Configuring SNMP

Because all server instances provide information for a common set of management information bases (MIBs), each server instance provides its information under a unique SNMPv3 context name equal to the server instance name.

## About this task

The server instance name is defined in the Global Configuration and is constructed from the host name and the server LDAP port by default. Information must be requested using SNMPv3, specifying the context name that pertains to the desired server instance.

|   |                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The server supports SNMPv3, and only SNMPv3 can access the MIBs. For systems that implement SNMP v1 and v2c, Net-SNMP provides a proxy function to route requests in one version of SNMP to an agent using a different SNMP version. |

## Steps

1. To enable the server's SNMP plugin, use the `dsconfig` tool.

   |   |                                                                                                                                                                                                                                                                                                                          |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | The SNMPv3 context name is limited to 30 bytes maximum. Any context name longer than 30 characters returns an error message when you attempt to enable the plugin.The default context server name is the server instance name and the LDAP port number, so take note of the length of the fully-qualified DNS host name. |

   1. Specify the address and port of the SNMP primary agent.

   2. On each server instance, enable the SNMP subagent.

   3. Enable the SNMP Subagent Alert Handler so that the sub-agent sends traps for administrative alerts generated by the server.

      ### Example:

      ```shell
      $ bin/dsconfig set-alert-handler-prop \
        --handler-name "SNMP Subagent Alert Handler" --set enabled:true
      ```

2. View the error log.

   ### Result:

   A message displays that the primary agent is not connected because it is not yet online.

   ```
   The SNMP sub-agent was unable to connect to the master
   agent at localhost/705: Timeout
   ```

3. Edit the SNMP agent `snmpd.conf` configuration file and add the directive to run the agent as an AgentX primary agent.

   The file is often located in `/etc/snmp/snmpd.conf`.

   ### Example:

   ```
   master agentx agentXSocket tcp:localhost:705
   ```

   |   |                                                                                                                                                                                            |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Using `localhost` means that only sub-agents running on the same host can connect to the primary agent. This is necessary because there are no security mechanisms in the AgentX protocol. |

4. Add the trap directive to send SNMPv2 traps to `localhost` with the community name, public (or whatever SNMP community has been configured for your environment) and the port.

   ### Example:

   ```
   trap2sink localhost public 162
   ```

5. To create a SNMPv3 user, add the following lines to the `/etc/snmp/snmpd.conf` file.

   ### Example:

   ```
   rwuser initial
   createUser initial MD5 setup_passphrase DES
   ```

6. To create the SNMPv3 user, run `snmpusm`.

   ### Example:

   ```
   snmpusm -v3 -u initial -n "" -l authNoPriv -a MD5 -A setup_passphrase \
   localhost create snmpuser initial
   ```

7. Start the `snmpd` daemon.

   ### Result:

   A message displays in the server's error log.

   ```
   The SNMP subagent connected successfully to the master agent
   at localhost:705. The SNMP context name is host.example.com:389
   ```

8. To see the alerts that are generated by the server, set up a trap client.

   1. Create a config file in `/tmp/snmptrapd.conf`.

   2. Add the `authcommunity log, execute public` directive to the file.

      |   |                                                                                                                                              |
      | - | -------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | The directive specifies that the trap client can process traps using the public community string and can log and trigger executable actions. |

9. Install the MIB definitions for the Net-SNMP client tools in the `/usr/share/snmp/mibs` directory.

   ### Example:

   ```shell
   $ cp resource/mib/* /usr/share/snmp/mibs
   ```

10. To run the trap client, run the `snmptrapd` command.

    ### Example:

    This example specifies that the command should not create a new process using `fork()` from the calling shell (`-f`), should not read any configuration files (`-C`) except the one specified with the `-c` option, should print to standard output (`-Lo`), and then specifies that debugging output should be turned on for the User-based Security Module (`-Dusm`). The path after the `-M` option is a directory that contains the MIBs shipped with our product ( `server-root/resource/mib`).

    ```shell
    $ snmptrapd -f -C -c /tmp/snmptrapd.conf -Lf /root/trap.log -Dusm \
      -m all -M +/usr/share/snmp/mibs
    ```

11. To test the feature, run the Net-SNMP client tools.

    You must use the following options:

    * `-v` *\<SNMP version>*

    * `-u` *\<username>*

    * `-l` *\<security level>*

    * `-n` *\<context name (instance name)>*

    * `-A` *\<user password>*

      ### Example:

      In this example, the `-m all`option loads all MIBs in the default MIB directory in `/usr/share/snmp/mibs` so that MIB names can be used in place of numeric OIDs.

      ```shell
      $ snmpget -v 3 -u snmpuser -A password -l authNoPriv -n host.example.com:389 \
      -m all localhost localDBBackendCount.0

      $ snmpwalk -v 3 -u snmpuser -A password -l authNoPriv -n host.example.com:389 \
      -m all localhost systemStatus
      ```

---

---
title: Distributed tracing
description: Learn how to use distributed tracing to troubleshoot and optimize PingDirectory.
component: pingdirectory
version: 11.1
page_id: pingdirectory:monitoring_the_pingdirectory_suite_of_products:pd_ds_distributed_tracing_main
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/monitoring_the_pingdirectory_suite_of_products/pd_ds_distributed_tracing_main.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  why-use-distributed-tracing: Why use distributed tracing?
  what-is-distributed-tracing: What is distributed tracing?
  which-requests-are-traced: Which requests are traced?
  enable-and-configure-tracing: Enable and configure tracing
  how-to-view-traces: How to view traces
---

# Distributed tracing

In a distributed system, requests pass through multiple services hosted on multiple servers. Without telemetry data, it can be difficult to identify the root cause of performance issues or errors.

Distributed tracing provides visibility into the full path a request takes through a distributed system. PingDirectory supports the [OpenTelemetry framework](https://opentelemetry.io/docs/what-is-opentelemetry/) for collecting distributed tracing data. You can send traces collected by PingDirectory to a backend service, such as [Jaeger](https://www.jaegertracing.io/), for aggregation, storage, and visualization.

|   |                                                                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This feature is provided as a **Preview**, which means that it isn't supported and should not be used in production environments. Learn more in [Feature statuses](../feature_status.html).Additionally, distributed tracing is only available for the PingDirectory server. |

## Why use distributed tracing?

Diagnosing escalated production issues can take hours to days, involving multiple subject matter experts trying to correlate fragmented logs and understand what happened, often yielding a lot of noise and little clarity. The more services and instances involved, the more challenging troubleshooting becomes.

Distributed tracing addresses these challenges by supporting end-to-end request visibility and data correlation across multiple services and servers. As a result, you can troubleshoot performance issues and errors more quickly and effectively. You can also use distributed tracing to optimize system performance by identifying bottlenecks and inefficiencies in service interactions.

## What is distributed tracing?

Distributed tracing shows you how an incoming request was processed across all servers and services in a distributed system, including:

* Which servers and services the request went through.

* How much time each service took to process its part of the request.

* How the services are connected.

* What the failure point was in case of a request failure.

A distributed trace provides a visual representation of a request's journey. Spans show when an operation started, when it ended, and its duration. When one service calls another, these calls are linked within the trace, showing the flow and time spent in each service. The PingDirectory server uses the OpenTelemetry framework to create and manage these spans and traces.

* Traces

  A trace represents the path of a request through an application. A trace is made up of one or more spans. Learn more about traces in the [OpenTelemetry documentation](https://opentelemetry.io/docs/concepts/signals/traces/).

* Spans

  A span is a segment of a request journey. It represents a unit of work or an operation within a service. Each span includes the following elements:

  * `traceId` represents the trace that the span is a part of.

  * `spanId` is a unique ID for the span.

  * `parentSpanId` is the ID of the originating request.

  Servers add span attributes following the [semantic conventions](https://opentelemetry.io/docs/specs/semconv/general/attributes/), with LDAP-specific attributes based on [HTTP conventions](https://opentelemetry.io/docs/specs/semconv/http/http-spans/).

* Root span

  The root span indicates the start and end of an entire operation. The `parentSpanId` of the root span is null because the root span isn't part of an existing trace. Subsequent spans in the trace have their own unique `spanId`. Their `traceId` is the same as that of the root span, and their `parentSpanId` matches the `spanId` of the root span.

* OpenTelemetry

  OpenTelemetry is an open-source observability framework for instrumenting, generating, collecting, and exporting telemetry data. It provides a standardized way to capture distributed traces across different services and platforms. It doesn't provide a backend for storing or analyzing telemetry data. Learn more in the [OpenTelemetry documentation](https://opentelemetry.io/docs/what-is-opentelemetry/).

## Which requests are traced?

All incoming LDAP requests, including those from PingFederate, are supported. Requests must include the [W3C trace context LDAP request control](https://www.w3.org/TR/trace-context/) to propagate trace information.

The W3C trace context allows for consistent correlation IDs and metadata across systems that support the W3C standard. If a request doesn't include the W3C trace context control, a new trace starts for that request.

## Enable and configure tracing

Distributed tracing is disabled by default. To enable the feature, you need to enable the OpenTelemetry plugin, as follows:

```shell
bin/dsconfig set-plugin-prop \
    --plugin-name OpenTelemetry \
    --set enabled:true
```

Supply the following properties to configure how spans are sampled and where telemetry data gets exported:

| Property                        | Description                                                                                                                                                                                                                                                                                                             | Values                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `key-manager-provider`          | The key manager provider to use if the OTLP/HTTP collector requires a client certificate.                                                                                                                                                                                                                               | For example, `JKS`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `trust-manager-provider`        | The trust manager provider used to validate the certificate presented by the OTLP/HTTP collector.                                                                                                                                                                                                                       | For example, `JKS`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `ssl-cert-nickname`             | The nickname in the associated key store for the certificate to present to the OTLP/HTTP collector.You can leave this undefined if no key manager provider is configured or if the JVM should select a certificate automatically.                                                                                       | For example, `server-cert`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `tracer-exporter-otlp-endpoint` | Sets the OTLP/HTTP endpoint where the server exports sampled spans.                                                                                                                                                                                                                                                     | The endpoint must start with either http\:// or https\:// and include the full HTTP path.&#xA;&#xA;If you don't set this value, the spans won't be exported.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `tracer-sampler`                | Selects the sampling strategy used when new spans are created.                                                                                                                                                                                                                                                          | * `always-on`: Samples every span.

* `always-off`: Samples none of the spans and produces no telemetry data.

* `trace-id-ratio`: Samples spans according to the `tracer-sampler-ratio` value.

* `parent-based-default-always-on`: Samples according to the parent span configuration, defaulting to `always-on` when there is no parent span.

* `parent-based-default-always-off`: Samples according to the parent span configuration, defaulting to `always-off` when there is no parent span.

* `parent-based-default-trace-id-ratio`: Samples according to the parent span configuration, defaulting to `trace-id-ratio` when there is no parent span. |
| `tracer-sampler-ratio`          | Specifies the sampling percentage used by ratio-based samplers. Higher values result in more spans being sampled but could impact performance.When the sampling strategy is either `trace-id-ratio` or `parent-based-default-trace-id-ratio`, this value determines the percentage of new spans that should be sampled. | `0` - `100` (inclusive)The default value is `10`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

The following example configures the plugin to push all traces to http\://localhost:4318/v1/traces, sampling all the spans:

```shell
bin/dsconfig set-plugin-prop \
    --plugin-name OpenTelemetry \
    --set enabled:true \
    --set tracer-sampler:always-on \
    --set tracer-exporter-otlp-endpoint:http://localhost:4318/v1/traces \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --no-prompt
```

## How to view traces

PingDirectory can push traces to an [OpenTelemetry Protocol (OTLP)](https://opentelemetry.io/docs/specs/otel/protocol/) endpoint over HTTP. Any backend that supports OTLP/HTTP can be used to collect and visualize the traces.

|   |                                                                                                                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Try the [Jaeger tracing All-in-one Docker image](https://www.jaegertracing.io/docs/2.11/getting-started/) to capture exported spans. By default, Jaeger stores the spans in memory, but you can configure Jaeger to send the spans to various persistent datastores external to the Docker image. |

---

---
title: Enabling and configuring the StatsD monitoring endpoint
description: The Monitoring Endpoint configuration type provides the StatsD endpoint type that you can use to transfer metrics data in the StatsD format.
component: pingdirectory
version: 11.1
page_id: pingdirectory:monitoring_the_pingdirectory_suite_of_products:pd_ds_enable_config_statsd_monitor_endpoint
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/monitoring_the_pingdirectory_suite_of_products/pd_ds_enable_config_statsd_monitor_endpoint.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
page_aliases: ["pd_ds_enable_config_statsd_collector_plugin.adoc", "pd_proxy_send_metrics_splunk_statsd.adoc"]
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  enabling-and-configuring-the-stats-collector-plugin: Enabling and configuring the Stats Collector Plugin
  about-this-task-2: About this task
  steps-2: Steps
  choose-from-2: Choose from:
  next-steps: Next steps
  met_splunk_statsd: Sending metrics to Splunk with StatsD
  about-this-task-3: About this task
  steps-3: Steps
---

# Enabling and configuring the StatsD monitoring endpoint

The Monitoring Endpoint configuration type provides the StatsD endpoint type that you can use to transfer metrics data in the StatsD format.

## About this task

You can configure the Monitoring Endpoint using the `dsconfig` command or the admin console.

## Steps

* To create the StatsD monitoring Endpoint, use either of the following:

  ### Choose from:

  * To use the command-line, run `dsconfig` with the `create-monitoring-endpoint` option.

    This example configures a new StatsD Monitoring Endpoint to send UDP data to localhost port 8125 using `dsconfig`.

    ```
    dsconfig create-monitoring-endpoint \
        --type statsd \
        --endpoint-name StatsDEndpoint \
        --set enabled:true \
        --set hostname:localhost \
        --set server-port:8125 \
        --set connection-type:unencrypted-udp
    ```

  * To use the admin console:

    1. In the sidebar, click **Configuration**.

    2. Enable the **Show all configuration** toggle in the upper right.

    3. In the **Logging, Monitoring, and Notifications** section, click **Monitoring Endpoints**.

    4. Click **New Monitoring Endpoint**.

  When you configure Monitoring Endpoint include:

  * The endpoint's host name

  * The endpoint's port

  * A toggle to use TCP or UDP

  * A toggle to use SSL if you use TCP

  You can configure a StatsD Monitoring Endpoint with custom tags using the `additional-tags` property. This adds the defined tags to each metric message sent to the endpoint. Each tag should be created in a "key=value" format. Additional tags are appended to the end of the StatsD message. Here is a sample StatsD message with custom tags:

  ```
  example.metric:123|g|#tag1:value1,tag2:value2
  ```

  |   |                                                          |
  | - | -------------------------------------------------------- |
  |   | You can send data to any number of monitoring endpoints. |

## Enabling and configuring the Stats Collector Plugin

The Stats Collector Plugin controls the metrics used by the StatsD monitoring endpoint.

### About this task

|   |                                                      |
| - | ---------------------------------------------------- |
|   | This topic applies only to the PingDirectory server. |

To send metrics with the StatsD monitoring endpoint, enable the Stats Collector Plugin and configure the plugin to indicate which metrics to send.

Examples of metrics you can send are:

* Busy worker thread count

* Garbage collection statistics

* Host system metrics such as CPU and memory

|   |                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For a list of available metrics, use the interactive `dsconfig` menu for the Stats Collector Plugin, or in the admin console, edit the Stats Collector plugin, as explained in the second example. |

### Steps

* To enable and configure the Stats Collector Plugin, use either of the following:

  #### Choose from:

  * To use the command line, run `dsconfig` with the `set-plugin-prop` option.

    This example enables the Stats Collector Plugin to send host CPU metrics, memory metrics, and server status metrics using `dsconfig`.

    ```
    dsconfig set-plugin-prop \
        --plugin-name "Stats Collector" \
        --set enabled:true \
        --set host-info:cpu \
        --set host-info:disk \
        --set status-summary-info:basic
    ```

    |   |                                                                                                                                                                                                                                                                         |
    | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | If you are not using Data Metrics Server to monitor your server, you can disable the generation of some unnecessary metrics files for the StatsD Monitoring Endpoint. To do this, set the `generate-collector-files` property on the Stats Collector Plugin to `false`. |

  * To use the admin console:

    1. In the sidebar, click **Configuration**.

    2. Enable the **Show all configuration** toggle in the upper right.

    3. In the **LDAP (Administration and Monitoring)** section, click **Plugin Root**.

    4. Edit the **Stats Collector** plugin and select the configuration options to indicate which metrics to send.

### Next steps

After you enable the Stats Collector and create the StatsD monitoring endpoint, you can:

* Use the data with Splunk, as explained in [Sending metrics to Splunk with StatsD](#met_splunk_statsd).

* Configure other tools that support StatsD, such as CloudWatch or a Prometheus StatsD exporter, to use the data. You can find more information about this configuration in your tool's StatsD documentation.

## Sending metrics to Splunk with StatsD

### About this task

|   |                                                           |
| - | --------------------------------------------------------- |
|   | This topic applies only to the PingDirectoryProxy server. |

Using the StatsD Endpoint type, you can send metric data to a Splunk installation. In Splunk, you can use Secure Sockets Layer (SSL) *(tooltip: \<div class="paragraph">
\<p>A protocol for authenticated and encrypted links between networked machines, typically over HTTPS. SSL was deprecated in 1999 in favor of Transport Layer Security (TLS).\</p>
\</div>)* to secure ports opened for StatsD. You can configure open UDP or TCP ports in Splunk to accept only connections from a certain hostname or IP address.

|   |                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | StatsD metrics are typically sent over UDP. Using UDP, the client sending metrics does not have to block as it would if using TCP. However, using TCP guarantees order and ensures no metrics are lost. |

To securely send UDP or TCP data to Splunk:

### Steps

1. Send the data to a Splunk Universal Forwarder.

2. Request that the forwarder use SSL to communicate with the Splunk Indexer.

---

---
title: MIBS
description: The server provides SMIv2-compliant management information base (MIB) definitions (RFC 2578, 2579, 2580) for distinct monitoring statistics. These MIB definition text files are in the server's /resource/mib directory.
component: pingdirectory
version: 11.1
page_id: pingdirectory:monitoring_the_pingdirectory_suite_of_products:pd_ds_mibs
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/monitoring_the_pingdirectory_suite_of_products/pd_ds_mibs.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 14, 2024
---

# MIBS

The server provides SMIv2-compliant management information base (MIB) definitions (RFC 2578, 2579, 2580) for distinct monitoring statistics. These MIB definition text files are in the server's `/resource/mib` directory.

Each MIB provides managed object tables for each specific SNMP management information as follows:

* LDAP Remote Server MIB

  Provides information related to the health and status of the LDAP servers that the server connects to and statistics about the operations invoked by the server on those LDAP servers.

* LDAP Statistics MIB

  Provides a collection of connection-oriented performance data that is based on a connection handler in the server.

A server typically contain only one connection handler and therefore supplies only one table entry.

* Local DB Backend MIB

  Provides key metrics related to the state of the local database backends contained in the server.

* Processing Time MIB

  Provides a collection of key performance data related to the processing time of operations broken down by several criteria but reported as a single aggregated data set.

* Replication MIB

  Provides key metrics related to the current state of replication that can help diagnose how much outstanding work replication might have to do.

* System Status MIB

  Provides a set of critical metrics for determining the status and health of the system in relation to its work load.

For information on the available monitoring statistics for each MIB available on the PingDirectory server and the PingDirectoryProxy server, see the text files located in the server's `/resource/mib` directory.

The server generates an extensive set of SNMP traps for event monitoring. The traps display the severity, description, name, OID, and summary. For information about the available alert types for event monitoring, see the `resource/mib/UNBOUNDID-ALERT-MIB.txt` file.

---

---
title: Monitoring disk space usage
description: The disk space usage monitor provides information about the amount of usable disk space available for the server components.
component: pingdirectory
version: 11.1
page_id: pingdirectory:monitoring_the_pingdirectory_suite_of_products:pd_ds_monitor_disk_space_usage
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/monitoring_the_pingdirectory_suite_of_products/pd_ds_monitor_disk_space_usage.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
---

# Monitoring disk space usage

The disk space usage monitor provides information about the amount of usable disk space available for the server components.

The disk space usage monitor evaluates the free space at locations registered through the `DiskSpaceConsumer` interface by various components of the server. Disk space monitoring excludes disk locations that do not have server components registered. However, other disk locations might still impact server performance, such as the operating system disk, if it becomes full. When relevant to the server, these locations include the server root, the location of the `/config` directory, the location of every log file, all Java Runtime Environment (JRE) backend directories, the location of the changelog, the location of the replication environment database, and the location of any server extension that registers itself with the `DiskSpaceConsumer` interface.

The disk space usage monitor provides the ability to generate administrative alerts and take additional action if the amount of usable space drops below the defined thresholds.

You can configure three thresholds for this monitor:

* Low space warning threshold

  This threshold is defined as either a percentage or absolute amount of usable space. If the amount of usable space drops below this threshold, then the server generates an administrative alert but remains fully functional. It generates alerts at regular intervals that you configure (such as once a day) unless action is taken to increase the amount of usable space. The server generates additional alerts as the amount of usable space is further reduced, such as each time the amount of usable space drops below a value 10% closer to the low space error threshold. If an administrator frees up disk space or adds additional capacity, then the server should automatically recognize this and stop generating alerts.

* Low space error threshold

  This threshold is also defined as either a percentage or absolute size. If the amount of usable space drops below this threshold, the server generates an alert notification and begins rejecting all operations requested by non-root users with `UNAVAILABLE` results. The server should continue to generate alerts during this time. When the server enters this mode, an administrator has to take some kind of action, such as, running a command to invoke a task or removing a signal file, before the server resumes normal operation. This threshold must be less than or equal to the low space warning threshold. If they are equal, the server begins rejecting requests from non-root users immediately upon detecting low usable disk space.

* Out of space error threshold

  This threshold can also be defined as a percentage or absolute size. If the amount of usable space drops below this threshold, the server generates a final administrative alert and shuts itself down. This threshold must be less than or equal to the low space error threshold. If they are equal, the server shuts itself down rather than rejecting requests from non-root users.

The server monitors disk space consumption during processing for the `export-ldif`, `rebuild-index`, and `backup` tools. Space is monitored every 10 seconds if usable space for all monitored paths is greater than 15 percent of the capacity of those volumes. If usable space for any path drops below 15 percent, or below 10GB free, the space check frequency is increased to every second. Warning messages are generated if available space falls below 10 percent, or below 5GB free. If usable space for any path drops below two percent, or 1GB free, the tool processing is aborted and files can be removed to free up space.

The default configuration uses the same values for the low space error threshold and out of space error threshold. This is to prevent having the server online but rejecting requests, which causes problems with applications trying to interact with the server. The low space warning threshold generates an alert before the problem becomes serious, well in advance of available disk space dropping to a point that it is critical.

The default values might not be suitable for all disk sizes, and should be adjusted to fit the deployment. Determining the best values should factor in the size of the disk, how big the database might become, how much space log files might consume, and how many backups are stored.

The threshold values can be specified either as absolute sizes or as percentages of the total available disk space. You must specify all values as absolute values or as percentages. A mix of absolute values and percentages cannot be used. The low space warning threshold must be greater than or equal to the low space error threshold, the low space error threshold must be greater than or equal to the out of space error threshold, and the out of space error threshold must be greater than or equal to zero.

If the out of space error threshold is set to zero, then the server does not attempt to automatically shut itself down if it detects that usable disk space has become critically low. If the amount of usable space reaches zero, then the database preserves its integrity but might enter a state in which it rejects all operations with an error and requires the server, or at least the affected backends, to be restarted. If the low space error threshold is also set to zero, then the server generates periodic warnings about low available disk space but remains fully functional for as long as possible. If all three threshold values are set to zero, then the server does not attempt to warn about or otherwise react to a lack of usable disk space.

---

---
title: Monitoring key performance indicators by application
description: PingDirectory server can be configured to track many key performance metrics, such as throughput and response-time, by the client applications requesting them.
component: pingdirectory
version: 11.1
page_id: pingdirectory:monitoring_the_pingdirectory_suite_of_products:pd_ds_monitor_key_perf_indicators
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/monitoring_the_pingdirectory_suite_of_products/pd_ds_monitor_key_perf_indicators.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 12, 2024
---

# Monitoring key performance indicators by application

PingDirectory server can be configured to track many key performance metrics, such as throughput and response-time, by the client applications requesting them.

This feature is invaluable for measuring whether the identify infrastructure meets all of your service-level agreements (SLA) that have been defined for client applications.

When enabled, the per-application monitoring data:

* Can be accessed in the `cn=monitor` backend

* Can be accessed in the Periodic Stats Logger

* Can be made available for collection by the Metrics server

For more information on using the Stats Logger, see [Profiling server performance using the Stats Logger](pd_ds_profile_server_perf_stats_logger.html).

---

---
title: Monitoring over LDAP
description: The PingDirectory server exposes a majority of its information under the cn=monitor entry.
component: pingdirectory
version: 11.1
page_id: pingdirectory:monitoring_the_pingdirectory_suite_of_products:pd_ds_monitor_over_ldap
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/monitoring_the_pingdirectory_suite_of_products/pd_ds_monitor_over_ldap.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 14, 2024
section_ids:
  steps: Steps
  example: Example:
---

# Monitoring over LDAP

The PingDirectory server exposes a majority of its information under the `cn=monitor` entry.

## Steps

* To access these entries over LDAP, use the `ldapsearch` tool.

  ### Example:

  ```shell
  $ bin/ldapsearch --hostname server1.example.com --port 1389 \
    --bindDN "uid=admin,dc=example,dc=com" --bindPassword secret \
    --baseDN "cn=monitor" "(objectclass=*)"
  ```

---

---
title: Monitoring the PingDirectory Suite of Products
description: The PingDirectory and PingDirectoryProxy servers provide a flexible monitoring framework that enables you to track server performance.
component: pingdirectory
version: 11.1
page_id: pingdirectory:monitoring_the_pingdirectory_suite_of_products:pd_ds_manage_monitoring
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/monitoring_the_pingdirectory_suite_of_products/pd_ds_manage_monitoring.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 18, 2023
---

# Monitoring the PingDirectory Suite of Products

The PingDirectory and PingDirectoryProxy servers provide a flexible monitoring framework that enables you to track server performance.

This framework exposes its monitoring information under the `cn=monitor` entry and provides interfaces through the admin console, SNMP, Java Management Extensions (JMX), and over LDAP. The PingDirectory server also provides a tool, the Periodic Stats Logger, to profile server performance.

---

---
title: Monitoring the server using JConsole
description: Set up JConsole to monitor the server using a remote process.
component: pingdirectory
version: 11.1
page_id: pingdirectory:monitoring_the_pingdirectory_suite_of_products:pd_ds_monitor_dir_server_jconsole
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/monitoring_the_pingdirectory_suite_of_products/pd_ds_monitor_dir_server_jconsole.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 13, 2024
section_ids:
  steps: Steps
  example: Example:
  example-2: Example:
  example-3: Example:
---

# Monitoring the server using JConsole

Set up JConsole to monitor the server using a remote process.

## Steps

1. Start the server.

   ### Example:

   ```shell
   $ bin/start-server
   ```

2. Enable the Java Management Extensions (JMX) Connection handler using`dsconfig` with the `set-connection-handler-prop` option.

   |   |                                                                                                                               |
   | - | ----------------------------------------------------------------------------------------------------------------------------- |
   |   | The handler is disabled by default.Include the LDAP connection parameters, such as host name, port, bindDN, and bindPassword. |

   ### Example:

   ```shell
   $ bin/dsconfig set-connection-handler-prop \
     --handler-name "JMX Connection Handler" --set enabled:true
   ```

3. Assign privileges to a regular user account with the `ldapmodify` tool.

   |   |                                                                                        |
   | - | -------------------------------------------------------------------------------------- |
   |   | Do not use a root user account, as using a root user account would be a security risk. |

   ### Example:

   This example grants `jmx-read`, `jmx-write`, and `jmx-notify` privileges to the user.

   ```shell
   $ bin/ldapmodify --hostname server1.example.com --port 1389 \
     --bindDN "cn=Directory Manager" --bindPassword secret
   dn: uid=admin,dc=example,dc=com
   changetype: modify
   replace: ds-privilege-name
   ds-privilege-name: jmx-read
   ds-privilege-name: jmx-write
   ds-privilege-name: jmx-notify
   ```

4. In **Java Monitoring & Administrative Console**, click **Remote Process**, and enter the following JMX URL using the host and port of your server.

   ```
   service:jmx:rmi:///jndi/rmi://<host>:<port>/com.unboundid.directory.server.protocols.jmx.client-unknown
   ```

5. In the **Username** and **Password** fields, enter the bind distinguished name (DN) and password for a user that has at least the `jmx-read` privilege.

6. Click **Connect**.

7. Click **com.unboundid.directory.server**, and expand the `rootDSE` node and the `cn-monitor` sub-node.

8. Select a monitoring entry.

---

---
title: Monitoring using SNMP
description: The PingDirectory server supports real-time monitoring using SNMP. The server provides an embedded SNMPv3 subagent plugin that, when enabled, sets up the server as a managed device and exchanges monitoring information with a primary agent based on the AgentX protocol.
component: pingdirectory
version: 11.1
page_id: pingdirectory:monitoring_the_pingdirectory_suite_of_products:pd_ds_monitor_snmp
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/monitoring_the_pingdirectory_suite_of_products/pd_ds_monitor_snmp.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
---

# Monitoring using SNMP

The PingDirectory server supports real-time monitoring using SNMP. The server provides an embedded SNMPv3 subagent plugin that, when enabled, sets up the server as a managed device and exchanges monitoring information with a primary agent based on the AgentX protocol.

|   |                     |
| - | ------------------- |
|   | SNMP is deprecated. |

---

---
title: Monitoring using the LDAP SDK
description: You can use the monitoring API to retrieve monitor entries from the PingDirectoryProxy server and retrieve specific types of monitor entries.
component: pingdirectory
version: 11.1
page_id: pingdirectory:monitoring_the_pingdirectory_suite_of_products:pd_ds_monitor_ldap_sdk
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/monitoring_the_pingdirectory_suite_of_products/pd_ds_monitor_ldap_sdk.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 13, 2024
---

# Monitoring using the LDAP SDK

You can use the monitoring API to retrieve monitor entries from the PingDirectoryProxy server and retrieve specific types of monitor entries.

For example, you can retrieve all monitor entries published by the server, and print the information contained in each using the generic API for accessing monitor entry data as follows.

```
for (MonitorEntry e : MonitorManager.getMonitorEntries(connection))
  {
    System.out.println("Monitor Name: " + e.getMonitorName());
    System.out.println("Monitor Type: " + e.getMonitorDisplayName());
    System.out.println("Monitor Data:");
    for (MonitorAttribute a : e.getMonitorAttributes().values())
    {
      for (Object value : a.getValues())
      {
        System.out.println(" " + a.getDisplayName() + ": " + String.valueOf(value));
      }
     }
     System.out.println();
  }
```

For more information about the LDAP SDK and the methods in this example, see the [LDAP SDK repository on GitHub](https://github.com/pingidentity/ldapsdk).

---

---
title: Monitoring with JMX
description: The PingDirectory server supports monitoring the Java virtual machine (JVM) through a Java Management Extensions (JMX) management agent, which can be accessed using JConsole or any other kind of JMX client.
component: pingdirectory
version: 11.1
page_id: pingdirectory:monitoring_the_pingdirectory_suite_of_products:pd_ds_monitor_with_jmx
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/monitoring_the_pingdirectory_suite_of_products/pd_ds_monitor_with_jmx.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
---

# Monitoring with JMX

The PingDirectory server supports monitoring the Java virtual machine (JVM) through a Java Management Extensions (JMX) management agent, which can be accessed using JConsole or any other kind of JMX client.

The JMX interface provides JVM performance and resource utilization information for applications running Java. In addition to the monitor information that the server provides, you can monitor generic metrics exposed by the JVM, including:

* Memory pools

* Threads

* Loaded classes

* MBeans

You can also subscribe to receive JMX notifications for any administrative alerts that are generated within the server.

---

---
title: Monitoring with the admin console
description: The admin console can be used to monitor items, such as disk space usage, active operations in the server, and alarms raised.
component: pingdirectory
version: 11.1
page_id: pingdirectory:monitoring_the_pingdirectory_suite_of_products:pd_proxy_monitor_admin_console
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/monitoring_the_pingdirectory_suite_of_products/pd_proxy_monitor_admin_console.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 15, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result
---

# Monitoring with the admin console

The admin console can be used to monitor items, such as disk space usage, active operations in the server, and alarms raised.

## About this task

The console provides a status option that accesses the server's monitor content.

To view the monitor dashboard:

## Steps

1. In your browser, go to http\://*\<server-name>*:*\<port>*/console.

2. Enter the root user distinguished name and password. Click **Continue**.

3. In the sidebar, click **Status**.

4. Click the **Monitors** tab.

   ![Screen capture of the Status page in the admin console with the Monitors tab selected](../_images/admin-console-monitors-tab.png)

## Result

The **Monitors** page opens, and you can monitor your server by selecting a monitor attribute.

---

---
title: Profiling server performance using the Stats Logger
description: The PingDirectory server includes a built-in Stats Logger that is useful for profiling server performance for a given configuration.
component: pingdirectory
version: 11.1
page_id: pingdirectory:monitoring_the_pingdirectory_suite_of_products:pd_ds_profile_server_perf_stats_logger
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/monitoring_the_pingdirectory_suite_of_products/pd_ds_profile_server_perf_stats_logger.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 12, 2024
page_aliases: ["pd_ds_enable_stats_logger.adoc", "pd_ds_config_multiple_periodic_stats_loggers.adoc", "pd_ds_add_custom_logged_stats_periodic_stats_logger.adoc", "pd_ds_config_custom_logged_stat_dsconfig_int.adoc", "pd_ds_config_custom_stats_logger_dsconfig_non_int.adoc"]
section_ids:
  enable_stats_logger: Enabling the Stats Logger
  about-this-task: About this task
  steps: Steps
  example: Example:
  result: Result:
  example-2: Example:
  configuring-multiple-periodic-stats-loggers: Configuring multiple Periodic Stats Loggers
  about-this-task-2: About this task
  steps-2: Steps
  example-3: Example:
  example-4: Example:
  result-2: Result
  adding-custom-logged-statistics-to-a-periodic-stats-logger: Adding custom logged statistics to a Periodic Stats Logger
  configuring-a-custom-logged-statistic-using-dsconfig-interactive: Configuring a custom logged statistic using dsconfig interactive
  steps-3: Steps
  example-5: Example:
  example-6: Example:
  result-3: Result:
  configuring-a-custom-stats-logger-using-dsconfig-non-interactive: Configuring a custom stats logger using dsconfig non-interactive
  about-this-task-3: About this task
  steps-4: Steps
  example-7: Example:
---

# Profiling server performance using the Stats Logger

The PingDirectory server includes a built-in Stats Logger that is useful for profiling server performance for a given configuration.

At a specified interval, the Stats Logger can write server statistics to a JSON file or to a log file in a `.csv` file, which can be read by spreadsheet applications. The logger has a negligible impact on server performance unless the `log-interval` property is set to a value of less than 1 second. You can customize the statistics logged and their verbosity.

The Stats Logger can also be used to view historical information about server statistics, including:

* Replication

* LDAP operations

* Host information

* Gauges

To update the configuration of the existing Stats Logger Plugin, you can either:

* Set the advanced `gauge-info` property to `basic/extended` to include this information.

* Create a dedicated Periodic Stats Logger for information about statistics of interest.

Learn more in [Enabling the Stats Logger](#enable_stats_logger).

## Enabling the Stats Logger

### About this task

By default, the PingDirectory server's built-in Stats Logger is disabled. To enable the Stats Logger:

### Steps

1. Run `dsconfig` in interactive mode.

   When you are prompted, enter the LDAP or LDAPS connection parameters.

   #### Example:

   ```shell
   $ bin/dsconfig
   ```

2. To change to the `Advanced Objects` menu, enter `o`.

3. On the main menu, enter the selection for `Plugins`.

4. On the `Plugin` menu, enter the selection for `View and edit an existing plugin`.

5. In the `Plugin` selection list, enter the selection for `Stats Logger`.

6. On the `Stats Logger Plugin` menu, enter the selection to set the `enabled` property to `TRUE`. To save and apply the configuration, enter `f`.

   #### Result:

   The default logger logs information about the server every second to `<server-root>/logs/dsstats.csv`. If the server is idle, nothing is logged.

   |   |                                                                                      |
   | - | ------------------------------------------------------------------------------------ |
   |   | To change the idle logging behavior, set the `suppress-if-idle` property to `FALSE`. |

7. Run the PingDirectory server.

   #### Example:

   For example, if you are running in a test environment, you can run the `search-and-mod-rate` tool to apply some searches and modifications to the server.

   |   |                                                                |
   | - | -------------------------------------------------------------- |
   |   | To see an example command, run `search-and-mod-rate` `--help`. |

8. View the Stats Logger output at `<server-root>/logs/dsstats.csv`.

   You can open the file in a spreadsheet.

## Configuring multiple Periodic Stats Loggers

### About this task

You can create multiple Periodic Stats Loggers to:

* Log different statistics

* View historical information about gauges

* To create a log at different intervals, such as logging cumulative operations statistics every hour

To create a new log, use the existing Stats Logger as a template to get reasonable settings, including rotation and retention policy.

### Steps

1. Run `dsconfig` in interactive mode.

   When prompted, enter the LDAP or LDAPS connection parameters.

   #### Example:

   ```shell
   $ bin/dsconfig
   ```

2. To change to the `Advanced Objects` menu, enter `o`.

3. In the main menu, enter the selection for `Plugins`.

4. In the `Plugin management` menu, enter the selection for `Create a new plugin`.

5. To use an existing plugin as a template, in the `Create a New Periodic Stats Logger Plugin` menu, enter `t`.

6. Enter the number corresponding to the existing stats logger as a template.

7. Enter a descriptive name for the new stats logger.

   For this example, enter `Stats Logger-10s`.

8. Enter the log file path to the file.

   For this example, enter `logs/dsstats2.csv`.

9. In the menu, make any other changes to the logger. To save and apply the configuration, enter `f`.

   #### Example:

   For this example, change the `log-interval` to `10s`, and the `suppress-if-idle` to `FALSE`.

### Result

You should see two loggers, `dsstats.csv` and `dsstats2.csv`, in the `logs` directory.

## Adding custom logged statistics to a Periodic Stats Logger

Add custom statistics based on any attribute in any entry under `cn=monitor` with the Custom Logged Stats object.

This configuration object provides powerful controls for how monitor attributes are written to the log. For example, you can extract a value from a monitor attribute using a regular expression. New Custom Logged Stats are automatically included in the Periodic Stats Logger output.

In addition to allowing a straight pass-through of the values using the raw statistic-type, you can configure attributes to be treated as any of the following:

* A counter, where the interval includes the difference in the value since the last interval

* An average value held by the attribute during the specified interval

* A minimum value held by the attribute during the specified interval

* A maximum value held by the attribute during the specified interval

The value of an attribute can also be scaled by a fixed value or by the value of another monitor attribute.

|   |                                                                                                                                                                                                                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Custom third-party server extensions written using the Server SDK can also expose interval statistics using a Periodic Stats Logger. The extension must first implement the SDK's `MonitorProvider` interface and register with the server. The monitor attributes produced by this custom `MonitorProvider` are then available to be referenced by a Custom Logged Stats object. |

To show you how to configure a Custom Logged Statistics Logger, the following sections reproduce the built-in `Consumer Total GB` column that displays in the output when the `included-resource-stat` property is set to memory-utilization on the Periodic Stats Logger.

The column is derived from the `total-bytes-used-by-memory-consumers` attribute of the `cn=JVM Memory Usage,cn=monitor` entry as follows.

```
dn: cn=JVM Memory Usage,cn=monitor
objectClass: top
objectClass: ds-monitor-entry
objectClass: ds-memory-usage-monitor-entry
objectClass: extensibleObject
cn: JVM Memory Usage
...
total-bytes-used-by-memory-consumers: 3250017037
```

### Configuring a custom logged statistic using `dsconfig` interactive

#### Steps

1. Run `dsconfig` and, when prompted, enter the LDAP or LDAPS connection parameters.

   ##### Example:

   ```shell
   $ bin/dsconfig
   ```

2. In the server's `Advanced Objects menu`, enter the selection for `Custom Logged Stats`.

3. In the `Custom Logged Stats menu`, enter the selection for `Create a new Custom Logged Stats`.

4. Select the `Stats Logger Plugin` from the list if more than one is present on the system. If you only have one stats logger, press Enter to confirm that you want to use the existing plugin.

5. Enter a descriptive name for the `Custom Logged Stats`.

   For this example, enter `Memory Usage`.

6. In the `monitor-objectclass` property menu, enter the `objectclass` attribute to monitor.

   For this example, enter `ds-memory-usage-monitor-entry`.

   |   |                                                                                                                    |
   | - | ------------------------------------------------------------------------------------------------------------------ |
   |   | To view the entry, run `ldapsearch` using the base distinguished name (DN) `cn=JVM Memory Usage,cn=monitor` entry. |

7. Enter the attributes of the monitor entry that you want to log in the stats logger, and then press Enter again to continue.

   For this example, enter `total-bytes-used-by-memory-consumers`.

8. Specify the type of statistics for the monitored attribute to appear in the log file.

   For this example, enter the option for `raw statistics` as recorded by the logger.

9. In the `Custom Logged Stats menu,` review the configuration.

10. To set up a column name that lists the memory usage, enter the option to change the `column-name` property.

11. To add a specific label for the column name, enter the option to `add a value`, and then enter `Memory Consumer Total (GB)`. To continue, press Enter.

12. Confirm that you want to use the `column-name` value that you entered in the previous step. To use the value, press Enter.

13. To scale the `Memory Consumer Totals (GB)` by 1 gigabyte (GB), in the `Custom Logged Stats menu`, enter the option to change the `divide-value-by` property.

14. In the `divide-value-by` property menu, enter the option to change the value, and then enter `1073741824`.

    1073741824 bytes is equivalent to 1 gigabyte.

15. In the `Custom Logged Stats menu`, review your configuration. To save and apply the settings, enter `f`.

    ##### Example:

    ```
    >>>> Configure the properties of the Custom Logged Stats
     >>>> via creating 'Memory Usage' Custom Logged Stats

             Property                   Value(s)
             ---------------------------------------------------------------
        1)   description                -
        2)   enabled                    true
        3)   monitor-objectclass        ds-memory-usage-monitor-entry
        4)   include-filter             -
        5)   attribute-to-log           total-bytes-used-by-memory-consumers
        6)   column-name                Memory Consumer Total (GB)
        7)   statistic-type             raw
        8)   header-prefix              -
        9)   header-prefix-attribute    -
        10)  regex-pattern              -
        11)  regex-replacement          -
        12)  divide-value-by            1073741824
        13)  divide-value-by-attribute  -
        14)  decimal-format             #.##
        15)  non-zero-implies-not-idle  false

        ?)   help
        f)   finish - create the new Custom Logged Stats
        a)   hide advanced properties of the Custom Logged Stats
        d)   display the equivalent dsconfig arguments to create this object
        b)   back
        q)   quit

    Enter choice [b]:
    ```

    ##### Result:

    A message of `The Custom Logged Stats was created successfully` is returned.

    After the Custom Logged Stats configuration change is completed, the new stats value should immediately show up in the Stats Logger output file.

### Configuring a custom stats logger using dsconfig non-interactive

#### About this task

The following task replicates the previous procedure using `dsconfig` in non-interactive mode.

To create a custom stats logger:

#### Steps

* Run the `dsconfig` non-interactive command with the `create-custom-logged-stats` option.

  ##### Example:

  In this example, the command produces a column named `Memory Consumer Total (GB)` that contains the value of the of `total-bytes-used-by-memory-consumers` attribute pulled from the entry with the `ds-memory-usage-monitor-entry` objectclass. This value is scaled by 1073741824 to get to a value represented in GBs.

  ```shell
  $ bin/dsconfig create-custom-logged-stats --plugin-name "Stats Logger" \
    --stats-name "Memory Usage" --type custom \
    --set monitor-objectclass:ds-memory-usage-monitor-entry \
    --set attribute-to-log:total-bytes-used-by-memory-consumers \
    --set "column-name:Memory Consumer Total (GB)" --set statistic-type:raw \
    --set divide-value-by:1073741824
  ```

---

---
title: Proxy considerations for tracked applications
description: In a proxy environment, the criteria should be defined in the PingDirectoryProxy server, because the PingDirectoryProxy server passes the application name through to the PingDirectory server in the intermediate client control.
component: pingdirectory
version: 11.1
page_id: pingdirectory:monitoring_the_pingdirectory_suite_of_products:pd_ds_proxy_considerations_tracked_apps
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/monitoring_the_pingdirectory_suite_of_products/pd_ds_proxy_considerations_tracked_apps.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
---

# Proxy considerations for tracked applications

In a proxy environment, the criteria should be defined in the PingDirectoryProxy server, because the PingDirectoryProxy server passes the application name through to the PingDirectory server in the intermediate client control.

If a client of the PingDirectoryProxy server or the PingDirectory server happens to use the intermediate client control, then the client name specified in the control is used as the application name regardless of the criteria listed in the `tracked-application` property.

---

---
title: Running JConsole
description: Run jconsole to monitor the memory usage and thread activity of a Java virtual machine.
component: pingdirectory
version: 11.1
page_id: pingdirectory:monitoring_the_pingdirectory_suite_of_products:pd_ds_run_jconsole
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/monitoring_the_pingdirectory_suite_of_products/pd_ds_run_jconsole.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 13, 2024
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  choose-from: Choose from:
---

# Running JConsole

Run `jconsole` to monitor the memory usage and thread activity of a Java virtual machine.

## Before you begin

Before you can run `jconsole`, you must:

* Configure and enable the Java Management Extensions (JMX) *(tooltip: \<div class="paragraph">
  \<p>Java technology that provides tools for managing and monitoring applications, devices, system objects, and service-oriented networks.\</p>
  \</div>)* Connection Handler for the server using the `dsconfig` tool.

  |   |                                                                                                                                                                                    |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | For more information, see [Configuring the JMX connection handler and alert handler](../pingdirectory_server_administration_guide/pd_ds_config_jmx_connection_alert_handler.html). |

* Invoke the `jconsole` executable by entering `jconsole` in your command-line interface or terminal.

  |   |                                                                                                                       |
  | - | --------------------------------------------------------------------------------------------------------------------- |
  |   | If *\<JDK\_HOME>* is not set in your path, you can access `jconsole` in the `bin` directory of the `<JDK_HOME>` path. |

## Steps

1. To open the **Java Monitoring & Management Console**, run `jconsole`:

   ### Choose from:

   * To monitor a specific process ID for your application, run `jconsole <process ID>`.

   * To run `jconsole` remotely, run `jconsole <hostname:port>`.

     If SSL is configured on the JMX Connection Handler, you must specify the PingDirectory server `.jar` file in the class path when running `jconsole` over SSL, as in the following example:

     ```shell
     $ jconsole -J-Dcom.unboundid.directory.server.protocol.jmx.trustStorePath=$INSTANCE_ROOT/config/truststore -J-Dcom.unboundid.directory.server.protocol.jmx.trustStorePin=secret -J-Dcom.unboundid.directory.server.protocol.jmx.trustStoreType=JKS -J-classpath -J"$INSTANCE_ROOT/lib/*:/Library/Java/JavaVirtualMachines /jdk1.8.0_201.jdk/Contents/Home/lib/jconsole.jar"
     ```

   Set the following properties in the above command:

   * Set the `com.unboundid.directory.server.protocol.jmx.trustStorePath` property with the full trust store path.

   * Set the `com.unboundid.directory.server.protocol.jmx.trustStoreType` property if the default type, Java KeyStore (JKS) *(tooltip: \<div class="paragraph">
     \<p>A repository of security certificates and corresponding private keys.\</p>
     \</div>)*, is not used.

   * Set the `com.unboundid.directory.server.protocol.jmx.trustStorePin` property with the trust store file password, if there is one.

   * Set the `com.unboundid.directory.server.protocol.jmx.trustStorePinFile` property with the file path containing the trust store password in plain text.

     Do not use this property if the `com.unboundid.directory.server.protocol.jmx.trustStorePin` property is used.

     |   |                                                                                                                                                                                                                                                                                                                                    |
     | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | When establishing a connection to `jconsole`, a window opens asking if you want to retry connecting insecurely. Click **Insecure connection**.Although `jconsole` considers anything other than `SslRmiClientSocketFactory` to be insecure, choosing to retry insecurely will enable PingDirectory's secure client socket factory. |

2. In the **Java Monitoring & Administrative Console** window, click **Local Process**, and then click the **PID** corresponding to the server.

3. Review the resource monitoring information.

---

---
title: SNMP implementation
description: In a typical SNMP deployment, many production environments use a network management system (NMS) for a unified monitoring and administrative view of all SNMP-enabled devices.
component: pingdirectory
version: 11.1
page_id: pingdirectory:monitoring_the_pingdirectory_suite_of_products:pd_ds_snmp_implementation
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/monitoring_the_pingdirectory_suite_of_products/pd_ds_snmp_implementation.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 12, 2024
---

# SNMP implementation

In a typical SNMP deployment, many production environments use a network management system (NMS) for a unified monitoring and administrative view of all SNMP-enabled devices.

The NMS communicates with a primary agent, whose main responsibility is to translate the SNMP protocol messages and multiplex any request messages to the subagent on each managed device, such as a PingDirectory server instance, a PingDirectoryProxy server, a PingDataSync server, or an OS Subagent. The primary agent also processes responses or traps from the agents. Many vendors provide commercial NMS systems. Consult with your NMS system for specific information.

The server contains an SNMP subagent plugin that connects to a Net-SNMP primary agent over TCP. The main configuration properties of the plugin are the address and port of the primary agent, which default to localhost and port 705, respectively. When the plugin is initialized, it creates an AgentX subagent and a managed object server and then registers as a management information base (MIB) server with the server instance. After the plugin's startup method is called, it starts a session thread with the primary agent. Whenever the connection is lost, the subagent automatically attempts to reconnect with the primary agent. The server's SNMP subagent plugin transmits only read-only values for polling or trap purposes. Set and inform operations are not supported. SNMP management applications cannot perform actions on the server on their own or through an NMS system.

![A diagram of an example SNMP deployment showing four subagent messages for a Net-SNMP primary Agent.](_images/zky1564011868109.png)Example SNMP Deployment

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The PingDirectory server was designed to interface with a Net-SNMP (5.3.2.2 or later) primary agent implementation with AgentX over TCP. Many operating systems provide their own Net-SNMP module. However, Service Management Automation (SMA) disables some features present in the Net-SNMP package and only enables AgentX over UNIX Domain Sockets, which cannot be supported by Java. If your operating system has a native Net-SNMP primary agent that only enables UNIX Domain Sockets, you should download and install a separate Net-SNMP binary from its website. |

---

---
title: The monitor backend
description: The server exposes its monitoring information under the cn=monitor entry.
component: pingdirectory
version: 11.1
page_id: pingdirectory:monitoring_the_pingdirectory_suite_of_products:pd_ds_monitor_backend
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/monitoring_the_pingdirectory_suite_of_products/pd_ds_monitor_backend.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 14, 2024
---

# The monitor backend

The server exposes its monitoring information under the `cn=monitor` entry.

Administrators can use various means to monitor the servers, including SNMP, the admin console, JConsole, LDAP command-line tools, and the Periodic Stats Logger.

|   |                                                                            |
| - | -------------------------------------------------------------------------- |
|   | To display server component activity and state, use the `bin/status` tool. |

To see the list of all monitor entries, use `ldapsearch` as in the following example.

```shell
$ bin/ldapsearch --hostname server1.example.com --port 1389 \
 --bindDN "uid=admin,dc=example,dc=com" --bindPassword secret \
 --baseDN "cn=monitor" "(objectclass=*)" cn
```

The following table describes a subset of the monitor entries.

| Component                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Active Operations                        | Provides information about the operations currently being processed by the server. Shows the number of operations, information on each operation, and the number of active persistent searches.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Backends                                 | Provides general information about the state of a server backend, including the entry count. If the backend is a local database, there is a corresponding database environment monitor entry with information on cache usage and on-disk size.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Client Connections                       | Provides information about all client connections to the server. The client connection information contains a name followed by an equal sign and a quoted value, such as `connID="15", connectTime="20100308223038Z"` and so forth.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Connection Handlers                      | Provides information about the available connection handlers on the server, which includes the LDAP and LDIF connection handlers. These handlers are used to accept client connections and to read requests and send responses to those clients.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Disk Space Usage                         | Provides information about the disk space available to various components of the server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| General                                  | Provides general information about the state of the server, including product name, vendor name, server version, etc.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Index                                    | The monitor captures the number of keys preloaded, and counters for read/write/remove/open-cursor/read-for-search. These counters provide insight into how useful an index is for a given workload.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| HTTP/HTTPS Connection Handler Statistics | Provides statistics about the interaction that the associated HTTP connection handler has had with its clients, including the number of connections accepted, average requests per connection, average connection duration, total bytes returned, and average processing time by status code.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| JVM Stack Trace                          | Provides a stack trace of all threads processing within the Java virtual machine (JVM).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| LDAP Connection Handler Statistics       | Provides statistics about the interaction that the associated LDAP connection handler has had with its clients, including the number of connections established and closed, bytes read and written, LDAP messages read and written, operations initiated, completed, and abandoned, etc.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Processing Time Histogram                | Categorizes operation processing times into several user-defined buckets of information, including the total number of operations processed, overall average response time in milliseconds (ms), number of processing times between 0ms and 1ms, and so forth.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| System Information                       | Provides general information about the system and the JVM on which the server is running, including system host name, operation system, JVM architecture, Java home, Java version, and so forth.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Version                                  | Provides information about the server version, including build ID, version, revision number, etc.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Work Queue                               | Provides information about the state of the PingDirectory server work queue, which holds requests until they can be processed by a worker thread, including the requests rejected, current work queue size, number of worker threads, and number of busy worker threads. The work queue configuration has a `monitor-queue-time` property set to `true` by default. This logs messages for new operations with a `qtime` attribute included in the log messages. Its value is expressed in milliseconds and represents the length of time that operations are held in the work queue.A dedicated thread pool can be used for processing administrative operations. This thread pool enables diagnosis and corrective action if all other worker threads are processing operations. To request that operations use the administrative thread pool, using the `ldapsearch` command for example, use the `--useAdministrativeSession` option. The requester must have the `use-admin-session` privilege, which is included for root users. By default, eight threads are available for this purpose. This can be changed with the `num-administrative-session-worker-threads` property in the work queue configuration. |