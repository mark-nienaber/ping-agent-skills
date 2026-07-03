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
