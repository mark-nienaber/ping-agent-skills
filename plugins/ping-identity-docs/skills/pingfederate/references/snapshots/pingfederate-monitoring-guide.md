---
title: Connecting to a local process
description: Unless you are running PingFederate as a Windows service, the easiest method by which to launch JConsole on the same machine as the server is to select Local Process.
component: pingfederate
version: 13.1
page_id: pingfederate:pingfederate_monitoring_guide:pf_connect_local_process
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/pingfederate_monitoring_guide/pf_connect_local_process.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Connecting to a local process

Unless you are running PingFederate as a Windows service, the easiest method by which to launch JConsole on the same machine as the server is to select **Local Process**.

## About this task

For information about connecting to a remote process, see [Connecting to a remote process](pf_connect_remote_process.html).

To connect to a local instance and start the monitoring process:

## Steps

* From the **Local Process** list, select **org.pingidentity.RunPF** and then click **Connect**.

  ![Screenshot of the Console: New Connection window with the correct file selected from the Local Process list.](_images/tni1580249740893.png)

  |   |                                                                                                           |
  | - | --------------------------------------------------------------------------------------------------------- |
  |   | If you are running the process locally, the system might prompt you to accept the connection as insecure. |

---

---
title: Connecting to a remote process
description: If PingFederate is running as a Windows Service, or if the org.pingidentity.RunPF class is unavailable in the Local Process list, use this procedure to establish a connection.
component: pingfederate
version: 13.1
page_id: pingfederate:pingfederate_monitoring_guide:pf_connect_remote_process
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/pingfederate_monitoring_guide/pf_connect_remote_process.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 13, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Connecting to a remote process

If PingFederate is running as a Windows Service, or if the `org.pingidentity.RunPF` class is unavailable in the Local Process list, use this procedure to establish a connection.

## About this task

To enable remote JMX monitoring in PingFederate:

## Steps

1. In the Administrative Console, go to the **Security > System Integration > Service Authentication** window.

2. Define the credentials that are required to connect to the PingFederate JMX service.

3. Restart PingFederate to enable the JMX Service.

4. If PingFederate is deployed in a clustered environment:

   1. Replicate the configuration changes on each node in the cluster.

   2. Restart each engine node.

5. After you enable the JMX service, connect to the remote JMX service by specifying the hostname and port `1099`, or a service URL like the following:

   ```
   service:jmx:rmi:///jndi/rmi://[hostname]:1099/jmxrmi
   ```

   Because JMX uses SSL by default when communicating with a remote host, the client host must trust the PingFederate SSL certificate that is presented when a connection is established.

   To disable the use of SSL for JMX, open the `/server/default/conf/jmx-remote-config.xml` file and set the `<item name="jmx.rmi.ssl">` property to `false`.

   |   |                                                                                                  |
   | - | ------------------------------------------------------------------------------------------------ |
   |   | If the JMX client does not trust the JMX certificate, a `connection failed` SSL message appears. |

6. If SSL is enabled in `jmx-remote-config.xml`, import the PingFederate SSL certificate to the client's trusted certificates.

7. If SSL is disabled, click **Insecure** to connect.

---

---
title: Connecting with JMX
description: You can connect to JMX using local and remote processes.
component: pingfederate
version: 13.1
page_id: pingfederate:pingfederate_monitoring_guide:pf_connect_with_jmx
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/pingfederate_monitoring_guide/pf_connect_with_jmx.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
---

# Connecting with JMX

You can connect to JMX using local and remote processes.

JConsole permits connections to local and remote Java processes. If your instance of PingFederate is running as a Windows Service, you must connect through the remote option. For more information on connecting to a local process, see [Connecting to a local process](pf_connect_local_process.html). For information on connecting to a remote process, see [Connecting to a remote process](pf_connect_remote_process.html).

---

---
title: Creating an error-only server log
description: This section describes an approach for modifying your log4j2.xml file, which can be sent to a security information and event management (SIEM) tool, such as Splunk. You can configure alerts to send notifications when such events occur, or to improve the monitoring of these events.
component: pingfederate
version: 13.1
page_id: pingfederate:pingfederate_monitoring_guide:pf_create_error_only_server_log
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/pingfederate_monitoring_guide/pf_create_error_only_server_log.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Creating an error-only server log

This section describes an approach for modifying your `log4j2.xml` file, which can be sent to a security information and event management (SIEM) tool, such as Splunk. You can configure alerts to send notifications when such events occur, or to improve the monitoring of these events.

## About this task

We recommend using the `server.log` file for error-level messages. Even when levels are down to a minimum, the server log generates large amounts of information in an active production environment. As an alternative, you can set up a specific log to log only `ERROR` and higher.

To change your `log4j2.xml` file to enable a separate log file:

## Steps

1. Create an appender.

   The easiest way to create an appender is to copy an existing one as a base. In the following example, the `RollingFile` is the same one that the `server.log` file uses. Bold text identifies items that have been changed.

   ```
   <!-- Error Only Main Log : A size based file rolling appender -->
   <RollingFile name="FILEERR"  fileName="${sys:pf.log.dir}/server.error.log"
            	filePattern="${sys:pf.log.dir}/server.error.log.%i" ignoreExceptions="false">
   	<PatternLayout>
       	<!-- Uncomment this if you want to use UTF-8 encoding instead
           	of system's default encoding.
       	<charset>UTF-8</charset> -->
       	<pattern>%d %X{trackingid} %-5p [%c] %m%n</pattern>
   	</PatternLayout>
   	<Policies>
       	<SizeBasedTriggeringPolicy
               	size="10000 KB" />
   	</Policies>
   	<DefaultRolloverStrategy max="5" />
   </RollingFile>
   ```

2. At the end of your `log4j2.xml` file, set the appender that you created in the previous step for `AsyncRoot`.

   ```
   <AsyncRoot level="INFO" includeLocation="false">
   	<!-- <AppenderRef ref="CONSOLE" /> -->
   	<AppenderRef ref="FILE" />
   	 <AppenderRef ref="FILEERR" level="ERROR" />
   </AsyncRoot>
   ```

   In this example, the `level` attribute indicates the level of messages that are sent to the log file.

3. Remove the attribute `additivity="false"` from all other loggers that contain a reference to the `File` appender.

   ```
   Logger name="org.sourceid.saml20.util.SystemUtil" level="INFO" additivity="false">
   	<!--<AppenderRef ref="CONSOLE" /> -->
   	<AppenderRef ref="FILE" />
   ```

   Becomes:

   ```
   <Logger name="org.sourceid.saml20.util.SystemUtil" level="INFO" >
   	<!--<AppenderRef ref="CONSOLE" /> -->
   	<AppenderRef ref="FILE" />
   ```

4. Make this change on all nodes within the cluster.

   |   |                                                                                                                        |
   | - | ---------------------------------------------------------------------------------------------------------------------- |
   |   | To expedite this step, we recommend creating a base file with the appropriate changes and copying it to all the nodes. |

5. Restart PingFederate.

---

---
title: Liveliness and responsiveness
description: One of the simpler methods for monitoring the performance of a PingFederate deployment involves determining whether the PingFederate Server is available and responsive. To help you identify the status of a server, PingFederate provides a heartbeat request endpoint.
component: pingfederate
version: 13.1
page_id: pingfederate:pingfederate_monitoring_guide:pf_liveliness_responsiveness
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/pingfederate_monitoring_guide/pf_liveliness_responsiveness.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 18, 2024
section_ids:
  heartbeat-endpoint: Heartbeat endpoint
  response-time-logging: Response-time logging
---

# Liveliness and responsiveness

One of the simpler methods for monitoring the performance of a PingFederate deployment involves determining whether the PingFederate Server is available and responsive. To help you identify the status of a server, PingFederate provides a heartbeat request endpoint.

## Heartbeat endpoint

If the PingFederate server is running, the process of sending a request to the endpoint `/pf/heartbeat.ping` returns an `HTTP 200` status. If the request times out or requires an extended amount of time to return, the server might be overloaded or experiencing other difficulties.

If a request requires more than two or three seconds to return, multiple factors in your PingFederate deployment might be responsible. We recommend that you develop a baseline for the desired response time by testing the heartbeat endpoint of your deployment at various times. This endpoint can be useful when load balancing a cluster of PingFederate instances. Some load balancers can alter the number of requests that are sent to a particular server based on the response code received, or the responsiveness of requests that are made to the heartbeat endpoint.

The output of the heartbeat endpoint can be modified to provide performance-related information, such as CPU and memory usage, and response times. The response metrics can help you make better auto-scaling decisions. The map size metrics can help you recognize performance issues.

The following example shows a report containing a sample of the PingFederate server metrics available from the heartbeat endpoint. This response does not include examples of every field. For a complete list of fields, see the server metrics table below.

```json
{"items":[{
"cpu.load": "14.86",
"total.jvm.memory": "536.871 MB",
"free.jvm.memory": "305.31 MB",
"used.jvm.memory": "231.561 MB",
"total.physical.system.memory": "68.719 GB",
"total.free.physical.system.memory": "30789.845 MB",
"total.used.physical.system.memory": "37.93 GB",
"number.of.cpus": "12",
"response.statistics.count": "540",
"response.statistics.window.seconds": "15",
"response.time.statistics.90.percentile": "159.350784",
"response.time.statistics.max": "6343.0",
"response.time.statistics.mean": "23.522222222222222",
"response.time.statistics.min": "0.0",
"response.concurrency.statistics.90.percentile": "2.0625",
"response.concurrency.statistics.max": "2.0",
"response.concurrency.statistics.mean": "0.7222222222222222",
"response.concurrency.statistics.min": "0.0",
"response.http.status.1xx": "0",
"response.http.status.2xx": "360",
"response.http.status.3xx": "180",
"response.http.status.4xx": "0",
"response.http.status.5xx": "0",
"transaction.count": "240",
"transaction.errors": "0",
"total.transactions": "660",
"total.failed.transactions": "0",
"ds.JDBC.PFIndexDS.request.count": "360",
"ds.JDBC.PFIndexDS.response.time.90.percentile": "0.0",
"ds.JDBC.PFIndexDS.response.time.max": "3.0",
"ds.JDBC.PFIndexDS.response.time.mean": "0.030555555555555555",
"ds.JDBC.PFIndexDS.response.time.min": "0.0",
"ds.LDAP.LDAP-8C4A5F60684C90B9ECE388D2B7194F7909C804CF.max.connections": "12"
"ds.LDAP.LDAP-8C4A5F60684C90B9ECE388D2B7194F7909C804CF.idle.connections": "6"
"ds.LDAP.LDAP-8C4A5F60684C90B9ECE388D2B7194F7909C804CF.min.connections": "5"
"ds.LDAP.LDAP-8C4A5F60684C90B9ECE388D2B7194F7909C804CF.request.count": "485",
"ds.LDAP.LDAP-8C4A5F60684C90B9ECE388D2B7194F7909C804CF.response.time.90.percentile": "50.29888",
"ds.LDAP.LDAP-8C4A5F60684C90B9ECE388D2B7194F7909C804CF.response.time.max": "5964.0",
"ds.LDAP.LDAP-8C4A5F60684C90B9ECE388D2B7194F7909C804CF.response.time.mean": "21.25773195876289",
"ds.LDAP.LDAP-8C4A5F60684C90B9ECE388D2B7194F7909C804CF.response.time.min": "0.0",
"adapter.CIAMHtml.lookupAuthN.90.percentile": "100.630528",
"adapter.CIAMHtml.lookupAuthN.count": "121",
"adapter.CIAMHtml.lookupAuthN.max": "6123.0",
"adapter.CIAMHtml.lookupAuthN.mean": "43.768595041322314",
"adapter.CIAMHtml.lookupAuthN.min": "0.98304",
"connection.https://pfdev.ping-eng.com:9031.jwks.90.percentile": "0.0",
"connection.https://pfdev.ping-eng.com:9031.jwks.count": "0",
"connection.https://pfdev.ping-eng.com:9031.jwks.max": "46.0",
"connection.https://pfdev.ping-eng.com:9031.jwks.mean": "0.0",
"connection.https://pfdev.ping-eng.com:9031.jwks.min": "0.0",
"connection.https://pfdev.ping-eng.com:9031.token.90.percentile": "3.93216",
"connection.https://pfdev.ping-eng.com:9031.token.count": "60",
"connection.https://pfdev.ping-eng.com:9031.token.max": "1044.0",
"connection.https://pfdev.ping-eng.com:9031.token.mean": "3.9",
"connection.https://pfdev.ping-eng.com:9031.token.min": "2.883584",
"connection.https://pfdev.ping-eng.com:9031.userinfo.90.percentile": "2.981888",
"connection.https://pfdev.ping-eng.com:9031.userinfo.count": "60",
"connection.https://pfdev.ping-eng.com:9031.userinfo.max": "18.0",
"connection.https://pfdev.ping-eng.com:9031.userinfo.mean": "2.4166666666666665",
"connection.https://pfdev.ping-eng.com:9031.userinfo.min": "0.98304",
"engine.jetty.queued.thread.pool.max.available.threads": "199",
"engine.jetty.queued.thread.pool.queue.size": "0",
"engine.jetty.queued.thread.pool.utilization.rate": "0.01507537688442211",
"engine.jetty.queued.thread.pool.utilized.threads": "3",
"idp.session.registry.session.map.size": "165",
"sp.session.registry.session.map.size": "165",
"session.state.attribute.map.size": "166",
"transaction.state.map.size": "1",
"atm.default.token.map.size": "0",
"cluster.members": "[172.31.28.63:7600, 172.31.29.114:7600]",
"cluster.rpc.addKeys.90.percentile": "0.0",
"cluster.rpc.addKeys.count": "0",
"cluster.rpc.addKeys.max": "0.0",
"cluster.rpc.addKeys.mean": "0.0",
"cluster.rpc.addKeys.min": "0.0",
"cluster.rpc.getAttr.90.percentile": "0.98304",
"cluster.rpc.getAttr.count": "423",
"cluster.rpc.getAttr.max": "1.0",
"cluster.rpc.getAttr.mean": "0.1276595744680851",
"cluster.rpc.getAttr.min": "0.0",
"cluster.rpc.getAuthnSessionInfo.90.percentile": "0.98304",
"cluster.rpc.getAuthnSessionInfo.count": "121",
"cluster.rpc.getAuthnSessionInfo.max": "4.0",
"cluster.rpc.getAuthnSessionInfo.mean": "0.371900826446281",
"cluster.rpc.getAuthnSessionInfo.min": "0.0",
"cluster.rpc.registerBeans.90.percentile": "0.98304",
"cluster.rpc.registerBeans.count": "121",
"cluster.rpc.registerBeans.max": "9.0",
"cluster.rpc.registerBeans.mean": "0.45454545454545453",
"cluster.rpc.registerBeans.min": "0.0",
"cluster.rpc.registerSriToUniqueUserKey.90.percentile": "0.98304",
"cluster.rpc.registerSriToUniqueUserKey.count": "122",
"cluster.rpc.registerSriToUniqueUserKey.max": "1.0",
"cluster.rpc.registerSriToUniqueUserKey.mean": "0.1885245901639344",
"cluster.rpc.registerSriToUniqueUserKey.min": "0.0",
"cluster.rpc.removeAttr.90.percentile": "0.98304",
"cluster.rpc.removeAttr.count": "361",
"cluster.rpc.removeAttr.max": "1.0",
"cluster.rpc.removeAttr.mean": "0.16620498614958448",
"cluster.rpc.removeAttr.min": "0.0",
"cluster.rpc.retrieveAndRemoveState.90.percentile": "0.98304",
"cluster.rpc.retrieveAndRemoveState.count": "180",
"cluster.rpc.retrieveAndRemoveState.max": "3.0",
"cluster.rpc.retrieveAndRemoveState.mean": "0.47222222222222227",
"cluster.rpc.retrieveAndRemoveState.min": "0.0",
"cluster.rpc.saveState.90.percentile": "0.98304",
"cluster.rpc.saveState.count": "180",
"cluster.rpc.saveState.max": "10.0",
"cluster.rpc.saveState.mean": "0.55",
"cluster.rpc.saveState.min": "0.0",
"cluster.rpc.setAttr.90.percentile": "0.98304",
"cluster.rpc.setAttr.count": "301",
"cluster.rpc.setAttr.max": "20.0",
"cluster.rpc.setAttr.mean": "0.318936877076412",
"cluster.rpc.setAttr.min": "0.0",
"cluster.rpc.synchronizeKeys.90.percentile": "2.883584",
"cluster.rpc.synchronizeKeys.count": "0",
"cluster.rpc.synchronizeKeys.max": "3.0",
"cluster.rpc.synchronizeKeys.mean": "0.0",
"cluster.rpc.synchronizeKeys.min": "2.883584"
}]}
```

The following table describes all the PingFederate server metrics available from the heartbeat endpoint.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In the following table, for server metrics that end in `.90.percentile`, the current `90` value is determined by the `ServerPercentilesList` item in the `com.pingidentity.monitoring.MonitoringService.xml` file. `90` is the default value. For more information on how to edit this value, see step 4 in [Liveliness and responsiveness](../administrators_reference_guide/pf_customize_heartbeat_message.html). |

| Server metrics                                                   | Description                                                                                                                                                                                                                                           |
| ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cpu.load`                                                       | Load on the PingFederate server's cores as a percentage of total capacity                                                                                                                                                                             |
| `total.jvm.memory`                                               | Total memory of the JVM                                                                                                                                                                                                                               |
| `free.jvm.memory`                                                | Free memory of the JVM                                                                                                                                                                                                                                |
| `used.jvm.memory`                                                | Used memory of the JVM                                                                                                                                                                                                                                |
| `total.physical.system.memory`                                   | Total system memory                                                                                                                                                                                                                                   |
| `total.free.physical.system.memory`                              | Free system memory                                                                                                                                                                                                                                    |
| `total.used.physical.system.memory`                              | Used system memory                                                                                                                                                                                                                                    |
| `number.of.cpus`                                                 | Number of cores on the PingFederate server                                                                                                                                                                                                            |
| `response.statistics.count`                                      | Number of items considered in the heartbeat report for the time and concurrency statistics                                                                                                                                                            |
| `response.statistics.window.seconds`                             | Time interval (in seconds) for the statistics report (this is an echo of the `StatisticsWindowSecs` parameter's value and provides context for the concurrency and time statistics)                                                                   |
| `response.time.statistics.90.percentile`                         | The 90th percentile response time in milliseconds during the statistics window (for example, if this value is 168, then 90% of the report samples had response times below 168 milliseconds)                                                          |
| `response.time.statistics.max`                                   | Longest time in milliseconds that the PingFederate server took to respond during the statistics window                                                                                                                                                |
| `response.time.statistics.mean`                                  | Mean time in milliseconds that the PingFederate server took to respond during the statistics window                                                                                                                                                   |
| `response.time.statistics.min`                                   | Shortest time in milliseconds that the PingFederate server took to respond during the statistics window                                                                                                                                               |
| `response.concurrency.statistics.90.percentile`                  | The 90th percentile response concurrency during the statistics window (for example, if this value is 124, then 90% of the report samples had response concurrency values below 124)                                                                   |
| `response.concurrency.statistics.max`                            | Maximum number of HTTP requests that the PingFederate server processed concurrently during the statistics window                                                                                                                                      |
| `response.concurrency.statistics.mean`                           | Mean number of HTTP requests that the PingFederate server processed concurrently during the statistics window                                                                                                                                         |
| `response.concurrency.statistics.min`                            | Minimum number of HTTP requests that the PingFederate server processed concurrently during the statistics window                                                                                                                                      |
| `response.http.status.1xx`                                       | Number of 1xx HTTP response codes during the statistics window                                                                                                                                                                                        |
| `response.http.status.2xx`                                       | Number of 2xx HTTP response codes during the statistics window                                                                                                                                                                                        |
| `response.http.status.3xx`                                       | Number of 3xx HTTP response codes during the statistics window                                                                                                                                                                                        |
| `response.http.status.4xx`                                       | Number of 4xx HTTP response codes during the statistics window                                                                                                                                                                                        |
| `response.http.status.5xx`                                       | Number of 5xx HTTP response codes during the statistics window                                                                                                                                                                                        |
| `transaction.count`                                              | Number of SSO, SLO, and STS transactions during the statistics window                                                                                                                                                                                 |
| `transaction.errors`                                             | Number of failed SSO, SLO, and STS transactions during the statistics window                                                                                                                                                                          |
| `total.transactions`                                             | Total number of SSO, SLO, and STS transactions since the server started                                                                                                                                                                               |
| `total.failed.transactions`                                      | Total number of failed SSO, SLO, and STS transactions since the server started                                                                                                                                                                        |
| `ds.<type>.<id>.max.connections`                                 | The maximum number of active connections that can be established at the same time                                                                                                                                                                     |
| `ds.<type>.<id>.active.connections`                              | The current number of active connections that are currently in use&#xA;&#xA;There is no active connections metric for LDAP connectors, because LDAPConnectionPool does not track the number of connections that are established and currently in use. |
| `ds.<type>.<id>.idle.connections`                                | The current number of established connections that are not in use                                                                                                                                                                                     |
| `ds.<type>.<id>.min.connections`                                 | The minimum number of connections configured for the connection pool                                                                                                                                                                                  |
| `ds.<type>.<id>.request.count`                                   | Number of requests for the data store during the statistics window                                                                                                                                                                                    |
| `ds.<type>.<id>.response.time.90.percentile`                     | The data store's 90th percentile response time in milliseconds during the statistics window                                                                                                                                                           |
| `ds.<type>.<id>.response.time.mean`                              | The data store's mean response time in milliseconds during the statistics window                                                                                                                                                                      |
| `ds.<type>.<id>.response.time.min`                               | The data store's minimum response time in milliseconds during the statistics window                                                                                                                                                                   |
| `ds.<type>.<id>.response.time.max`                               | The data store's maximum response time in milliseconds during the statistics window                                                                                                                                                                   |
| `ds.<type>.<id>.errors`                                          | Number of data store errors during the statistics window                                                                                                                                                                                              |
| `adapter.<adapter id>.lookupAuthN.count`                         | Number of authentication requests for the adapter during the statistics window                                                                                                                                                                        |
| `adapter.<adapter id>.lookupAuthN.90.percentile`                 | The adapter's 90th percentile response time in milliseconds during the statistics window                                                                                                                                                              |
| `adapter.<adapter id>.lookupAuthN.mean`                          | The adapter's mean response time in milliseconds during the statistics window                                                                                                                                                                         |
| `adapter.<adapter id>.lookupAuthN.min`                           | The adapter's minimum response time in milliseconds during the statistics window                                                                                                                                                                      |
| `adapter.<adapter id>.lookupAuthN.max`                           | The adapter's maximum response time in milliseconds during the statistics window                                                                                                                                                                      |
| `adapter.<adapter id>.lookupAuthN.errors`                        | Number of failed adapter authentication requests during the statistics window                                                                                                                                                                         |
| `connection.<issuer id>.jwks.count`                              | Number of requests for the OIDC identity provider (IdP) connection JWKS endpoint during the statistics window                                                                                                                                         |
| `connection.<issuer id>.jwks.90.percentile`                      | The OIDC IdP connection JWKS endpoint's 90th percentile response time in milliseconds during the statistics window                                                                                                                                    |
| `connection.<issuer id>.jwks.mean`                               | The OIDC IdP connection JWKS endpoint's mean response time in milliseconds during the statistics window                                                                                                                                               |
| `connection.<issuer id>.jwks.min`                                | The OIDC IdP connection JWKS endpoint's minimum response time in milliseconds during the statistics window                                                                                                                                            |
| `connection.<issuer id>.jwks.max`                                | The OIDC IdP connection JWKS endpoint's maximum response time in milliseconds during the statistics window                                                                                                                                            |
| `connection.<issuer id>.jwks.errors`                             | Number of failed OIDC IdP connection JWKS endpoint requests during the statistics window                                                                                                                                                              |
| `connection.<issuer id>.token.count`                             | Number of requests for the OIDC IdP connection token endpoint during the statistics window                                                                                                                                                            |
| `connection.<issuer id>.token.90.percentile`                     | The OIDC IdP connection token endpoint's 90th percentile response time in milliseconds during the statistics window                                                                                                                                   |
| `connection.<issuer id>.token.mean`                              | The OIDC IdP connection token endpoint's mean response time in milliseconds during the statistics window                                                                                                                                              |
| `connection.<issuer id>.token.min`                               | The OIDC IdP connection token endpoint's minimum response time in milliseconds during the statistics window                                                                                                                                           |
| `connection.<issuer id>.token.max`                               | The OIDC IdP connection token endpoint's maximum response time in milliseconds during the statistics window                                                                                                                                           |
| `connection.<issuer id>.token.errors`                            | Number of failed OIDC IdP connection token endpoint requests during the statistics window                                                                                                                                                             |
| `connection.<issuer id>.userinfo.count`                          | Number of requests for the OIDC IdP connection user info endpoint during the statistics window                                                                                                                                                        |
| `connection.<issuer id>.userinfo.90.percentile`                  | The OIDC IdP connection user info endpoint's 90th percentile response time in milliseconds during the statistics window                                                                                                                               |
| `connection.<issuer id>.userinfo.mean`                           | The OIDC IdP connection user info endpoint's mean response time in milliseconds during the statistics window                                                                                                                                          |
| `connection.<issuer id>.userinfo.min`                            | The OIDC IdP connection user info endpoint's minimum response time in milliseconds during the statistics window                                                                                                                                       |
| `connection.<issuer id>.userinfo.max`                            | The OIDC IdP connection user info endpoint's maximum response time in milliseconds during the statistics window                                                                                                                                       |
| `connection.<issuer id>.userinfo.errors`                         | Number of failed OIDC IdP connection user info endpoint requests during the statistics window                                                                                                                                                         |
| `connection.<entity id>.ars.count`                               | Number of requests for the SAML IdP connection artifact endpoint during the statistics window                                                                                                                                                         |
| `connection.<entity id>.ars.90.percentile`                       | The SAML IdP connection artifact endpoint's 90th percentile response time in milliseconds during the statistics window                                                                                                                                |
| `connection.<entity id>.ars.mean`                                | The SAML IdP connection artifact endpoint's mean response time in milliseconds during the statistics window                                                                                                                                           |
| `connection.<entity id>.ars.min`                                 | The SAML IdP connection artifact endpoint's minimum response time in milliseconds during the statistics window                                                                                                                                        |
| `connection.<entity id>.ars.max`                                 | The SAML IdP connection artifact endpoint's maximum response time in milliseconds during the statistics window                                                                                                                                        |
| `connection.<entity id>.ars.errors`                              | Number of failed SAML IdP connection artifact endpoint requests during the statistics window                                                                                                                                                          |
| `<admin\|engine>.jetty.queued.thread.pool.utilized.threads`      | Number of threads in the Jetty thread pool that are currently in use                                                                                                                                                                                  |
| `<admin\|engine>.jetty.queued.thread.pool.max.available.threads` | Maximum number of threads in the Jetty thread pool                                                                                                                                                                                                    |
| `<admin\|engine>.jetty.queued.thread.pool.utilization.rate`      | The threads in the pool that are currently in use, as a fraction of the maximum available threads                                                                                                                                                     |
| `<admin\|engine>.jetty.queued.thread.pool.queue.size`            | Number of requests currently queued waiting to be handled by a thread in the pool                                                                                                                                                                     |
| `idp.session.registry.session.map.size`                          | Number of IdP sessions                                                                                                                                                                                                                                |
| `idp.session.registry.session.map.purge.unexpired`               | Number of unexpired entries purged from the IdP session registry during the statistics window                                                                                                                                                         |
| `sp.session.registry.session.map.size`                           | Number of service provider (SP) sessions                                                                                                                                                                                                              |
| `sp.session.registry.session.map.purge.unexpired`                | Number of unexpired entries purged from the SP session registry during the statistics window                                                                                                                                                          |
| `session.state.attribute.map.size`                               | Number of items in the session state attribute map                                                                                                                                                                                                    |
| `session.state.attribute.map.purge.unexpired`                    | Number of unexpired entries purged from the session state attribute map during the statistics window                                                                                                                                                  |
| `transaction.state.map.size`                                     | Number of items in the SSO transaction state map                                                                                                                                                                                                      |
| `transaction.state.map.purge.unexpired`                          | Number of unexpired entries purged from the SSO transaction state map during the statistics window                                                                                                                                                    |
| `atm.<atm>.token.map.size`                                       | Number of tokens in the access token manager with the ID specified by *\<atm>*                                                                                                                                                                        |
| `cluster.members`                                                | Holds the cluster membership list                                                                                                                                                                                                                     |
| `cluster.rpc.<rpc name>.90.percentile`                           | The synchronous cluster Remote Procedure Call (RPC)'s 90th percentile response time in milliseconds during the statistics window                                                                                                                      |
| `cluster.rpc.<rpc name>.mean`                                    | The synchronous cluster RPC's mean response time in milliseconds during the statistics window                                                                                                                                                         |
| `cluster.rpc.<rpc name>.min`                                     | The synchronous cluster RPC's minimum response time in milliseconds during the statistics window                                                                                                                                                      |
| `cluster.rpc.<rpc name>.max`                                     | The synchronous cluster RPC's maximum response time in milliseconds during the statistics window                                                                                                                                                      |
| `cluster.rpc.<rpc name>.errors`                                  | Number of cases where the RPC received no valid responses                                                                                                                                                                                             |

As indicated in the table, the values of some metrics are calculated over a configurable time window. The default statistics window is five minutes.

To customize the statistics window period, change the value of the `StatisticsWindowSecs` parameter in the `<pf_install>/pingfederate/server/default/data/config-store/com.pingidentity.monitoring.MonitoringService.xml file`. This file also lets you specify additional JMX MBean attributes that will be made available to the heartbeat page templates.

For more information, see [Customizing the heartbeat message](../administrators_reference_guide/pf_customize_heartbeat_message.html)

## Response-time logging

By default, the audit logs record the processing time for each transaction. With audit logging enabled, you can identify the speed with which PingFederate processes the following transaction types:

* Single sign-on (SSO)

* OAuth

* Security token services (STS)

Depending on your logging configuration, audit logging might not log any transactions. For more information, see [Security audit logging](../administrators_reference_guide/pf_security_audit_logging.html).

The following provides examples of the default audit log.

```
2019-11-10 13:24:57,493| tid:cYunBsgybiw_fiRnJjkAhbIXvzc| AUTHN_SESSION_USED| | 127.0.0.1 | | ac_client| | localhost| IdP| success| PdFormAdpt| |  17
```

```
2019-11-10 13:24:58,720| tid:cYunBsgybiw_fiRnJjkAhbIXvzc| OAuth| 5c60f022-1e9d-3fbe-9749-4b9ca5591356| 127.0.0.1 | | ac_client| OAuth20| localhost| AS| success| PdFormAdpt| |  7
```

Processing times are shown at the end of the entry in milliseconds.

---

---
title: Logging, reporting, and troubleshooting
description: This section provides an overview of the available logging, reporting, and troubleshooting features for PingFederate.
component: pingfederate
version: 13.1
page_id: pingfederate:pingfederate_monitoring_guide:pf_logging_reporting_troubleshooting
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/pingfederate_monitoring_guide/pf_logging_reporting_troubleshooting.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 11, 2023
section_ids:
  pingfederate-logs: PingFederate Logs
---

# Logging, reporting, and troubleshooting

This section provides an overview of the available logging, reporting, and troubleshooting features for PingFederate.

## PingFederate Logs

The `server.log` file represents the primary troubleshooting log. Along with an HTTP trace from the browser, which can be generated from a debugging application like Fiddler, this file is helpful for identifying issues that must be resolved. The following table identifies the available PingFederate logs and summarizes their purposes.

| Name                              | Purpose                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `admin.log`                       | Records the actions that users of the Administrative Console and the Administrative API perform.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `admin-event-detail.log`          | If detailed event logging is enabled, this log records detailed information about each applicable administrative event that users perform using the Administrative Console and the Administrative API.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `admin-api.log`                   | Records the actions that users of the administrative API perform.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `runtime-api.log`                 | Records the actions that API users perform by using the OAuth Client Management Service, the OAuth Access Grant Management Service, and the Session Revocation API.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `transaction.log`                 | Records individual identity-federation runtime transactions at specified levels of detail.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `audit.log`                       | Records a selected, configurable subset of transaction log information plus additional details. Intended for security-audit and regulatory-compliance purposes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `provisioner-audit.log`           | Records outbound provisioning events intended for security-audit purposes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `provisioner.log`                 | Records provisioning activity only. Useful when troubleshooting issues that relate to provisioning.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `server.log`                      | Records PingFederate runtime and administrative server activities. For more information about the primary troubleshooting log, see [Creating an error-only server log](pf_create_error_only_server_log.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `init.log`                        | Records only Jetty messages that are generated prior to starting PingFederate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `thread-pool-exhaustion-dump.log` | Contains log messages and stack traces of all threads in PingFederate's Java Virtual Machine (JVM) *(tooltip: \<div class="paragraph">&#xA;\<p>A virtual machine that allows a computer to run Java programs and programs that are compiled to Java bytecode.\</p>&#xA;\</div>)*, including Java threads and VM internal threads. This information can help with troubleshooting the root cause of potential thread exhaustion events. The format of the thread dumps can be consumed by utilities such as jstack that is included with a Java Development Kit (JDK) *(tooltip: \<div class="paragraph">&#xA;\<p>A development environment for building applications and components using Java.\</p>&#xA;\</div>)*.This log is written only if you enable the runtime notification for thread pool exhaustion events. For more information, see [Configuring runtime notifications](../administrators_reference_guide/pf_configuring_runtime_notifications.html). |

---

---
title: Monitoring
description: This topic outlines the key JVM performance metrics for evaluating the performance of a PingFederate deployment.
component: pingfederate
version: 13.1
page_id: pingfederate:pingfederate_monitoring_guide:pf_monitoring
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/pingfederate_monitoring_guide/pf_monitoring.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 13, 2022
section_ids:
  monitoring-clustered-pingfederate-engines: Monitoring clustered PingFederate engines
  monitoring-cpu-utilization: Monitoring CPU utilization
  monitoring-memory-utilization: Monitoring memory utilization
  old-generation-space: Old Generation space
  entire-heap-space: Entire heap space
  eden-space: Eden space
  increasing-heap-size: Increasing heap size
---

# Monitoring

This topic outlines the key JVM performance metrics for evaluating the performance of a PingFederate deployment.

After a connection is established, you can access the JConsole monitoring interface.

## Monitoring clustered PingFederate engines

JConsole can be connected to multiple processes. To monitor several instances of PingFederate after a connection is established, click **Connection > New Connection** and add the additional connection.

## Monitoring CPU utilization

The **Overview** tab provides a dashboard of the following performance and resource-utilization charts:

* Heap Memory Usage (cumulative memory that is used by all memory pools).

* Live Threads

* CPU Usage

* Classes (number of classes that are loaded)

This tab provides a high-level view of the JVM's performance metrics.

![Screenshot of the Overview tab showing a high level view of performance metrics.](_images/ntj1580329602157.png)

Use the **Overview** tab to visualize and collect CPU usage data. When your PingFederate deployment is subjected to its normal or expected load, the CPU utilization typically falls between 60 and 80%. If the system registers consistently at 80% or higher, additional CPU resources might be necessary to handle load spikes that occur during peak usage times.

## Monitoring memory utilization

The **Overview** tab shows only overall heap usage. To view additional details about memory utilization, click the **Memory** tab, which lets you analyze usage patterns in specific memory pools within the heap. This tab also provides information about the overall heap utilization profile.

## Old Generation space

Objects that survive a sufficient number of garbage-collection cycles are promoted to the Old Generation. To view the memory usage in the pool of such objects, click **Memory Pool > PS Old Gen** or **Memory Pool > G1 Old**, depending on the relevant garbage collection. PingFederate services mostly short-lived transactions, like SSO, STS, and OAuth requests and most of the created memory objects are required only for a short period of time.

Although PingFederate makes use of some memory objects that are medium to long lived, such as session data for authentication session, adapter sessions, or single logout functionality, most of the objects that are promoted to the Old Generation are likely to become garbage that requires cleaning up. If the younger generation, or *Eden space*, is not sized appropriately, objects are moved to and retained in the Old Generation before they are collected as garbage. If size limitations prevent the Old Generation from accumulating future garbage as well as longer-lived objects, then garbage-collection cycles occur more frequently.

The Old Generation space is the most important space to monitor. It is easy to identify if the heap is sized and proportioned appropriately for a specific load, based on its usage pattern. The following examples involve two Old Generation usage charts. In both examples, the following examples involve two Old Generation usage charts. In both examples, the same user load executes the same workflow. The size of the heap represents the only difference.

Garbage collection frees around 60 to 75% of the space, and room is available to accommodate the future garbage of newly created objects that are moved from the Eden space, as well as the longer-term objects that remain in use. Although the space is 1 GB in size, the average full (PS MarkSweep or G1 Old Generation) collection time is approximately only 240 milliseconds (0.728 seconds for three collections).

![Windowshot of the Memory tab showing an Old Generation usage chart and how memory rises at a reasonably slow rate because the heap is sized adequately.](_images/uey1580330439264.png)

When a heap is sized inadequately, the Old Generation runs out of space. In the following example, the amount of memory that becomes free with each garbage collection shrinks, due to the rate at which objects are promoted from the Eden space.

![Windowshot of the Memory tab showing an Old Generation usage chart where the amount of memory that becomes free with each garbage collection shrinks due to the rate objects are promoted from the Eden space.](_images/bzb1580330596562.png)

184 PS MarkSweep (full) collections require garbage collections more frequently, totaling 60 seconds, or an average of 326 milliseconds per collection.

## Entire heap space

If the heap is sized appropriately for the load that the system must handle, it fills up and is followed by an appreciable drop in usage as a full garbage collection occurs (such as a PS MarkSweep collection triggered by the Old Generation filling up). In this example, the heap rises steadily, with drops from minor collections until a PS MarkSweep collection occurs and collects approximately 70% of the heap.

![Windowshot of the Memory tab showing the heap rising steadily with drops from minor collections until a PS MarkSweep collection occurs.](_images/qiw1580330777966.png)

When the heap is undersized, full collections that are performed more frequently return less memory. In the following example, the frequency of JMX data that the JConsole retrieves does not keep pace with the frequency of full collections. As a result, only a fraction of them occur.

![Windowshot of the Memory tab showing the frequency of JMX data that the JConsole retrieves does not keep pace with the frequency of full collections.](_images/usq1580330843656.png)

## Eden space

Regardless of whether the heap is adequately sized or undersized, the usage pattern is nearly identical with the Eden space. This similarity can be due to the sampling frequency of the data-collection tool because the number of samples might be insufficient to show that, with an undersized heap, memory is consumed and subsequently freed with greater frequency. The behavior of garbage collection in the Eden space is such that when it fills, the space is completely emptied by moving live objects to the Survivor and Old Generation spaces. Under load, the pattern resembles a jagged sawtooth, as shown in the following examples of an adequately sized heap and an undersized heap.

![Windowshot of the Memory tab showing how the pattern resembles a jagged sawtooth in an undersized heap.](_images/qat1580331057278.png)

## Increasing heap size

Because garbage collectors manage memory in the Java Runtime Environment, simply increasing the size of the heap is not always the appropriate solution. The following table outlines the total heap size recommendations for the available garbage collectors, based on available CPU resources.

| Garbage Collector     | Minimum Recommended Number of CPUs | Recommended Heap Size |
| --------------------- | ---------------------------------- | --------------------- |
| Parallel              | 4                                  | 6 GB maximum          |
| Concurrent Mark Sweep | 12                                 | 4 - 6 GB minimum      |
| Garbage First (G1)    | 12                                 | 6 GB minimum          |

If additional memory is unavailable, or if increasing the size of the heap is inadvisable because of these recommendations, the load that is handled by this instance is probably too high. In such instances, consider adding additional resources to your deployment. To verify whether the load for the instance is too high, check the CPU utilization

To allow for the most efficient management of memory, set the minimum and maximum heap sizes to the maximum allowed values to avoid potentially expensive heap allocation resizing and divide it evenly between the young and old generations. If you are using the Garbage First collector, generational spaces are not specified through command line options because they are managed logically in real time. Even in such instances, we recommend setting the minimum and maximum heap sizes to the maximum allowed values.

Learn more about fine-tuning the JVM options in the `jvm-memory.options` file in [Fine-tuning JVM options](../performance_tuning_guide/pf_fine_tuning_jvm_option.html).

---

---
title: PingFederate Monitoring Guide
description: PingFederate provides a range of monitoring options, from simple heartbeat options for checking responsiveness to transaction response-time logging and resource-utilization metrics.
component: pingfederate
version: 13.1
page_id: pingfederate:pingfederate_monitoring_guide:pf_monitoring_guide
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/pingfederate_monitoring_guide/pf_monitoring_guide.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
---

# PingFederate Monitoring Guide

PingFederate provides a range of monitoring options, from simple heartbeat options for checking responsiveness to transaction response-time logging and resource-utilization metrics.

To help you gain insight into the health and performance of your PingFederate deployment, this guide provides the following information:

* [Liveliness and responsiveness](pf_liveliness_responsiveness.html) describes the heartbeat request endpoint and audit logs

* [Resource metrics](pf_resource_metrics.html) describes mechanisms for obtaining resource metrics including JMX

* [Monitoring](pf_monitoring.html) describes the key JVM performance metrics for evaluating the performance of PingFederate deployments

* [Thread pool](pf_thread_pool.html) describes the MBeans tab and the recommended number of threads in the pool

* [Logging, reporting, and troubleshooting](pf_logging_reporting_troubleshooting.html) describes the available logging, reporting, and troubleshooting features

---

---
title: Resource metrics
description: PingFederate provides mechanisms for obtaining resource metrics including JMX and heartbeat endpoint.
component: pingfederate
version: 13.1
page_id: pingfederate:pingfederate_monitoring_guide:pf_resource_metrics
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/pingfederate_monitoring_guide/pf_resource_metrics.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 21, 2023
---

# Resource metrics

PingFederate provides mechanisms for obtaining resource metrics including JMX and heartbeat endpoint.

PingFederate provides the following mechanisms for obtaining resource metrics:

* JMX - Ping recommends using JMX MBeans because this method provides a more comprehensive set of resource metric counters for analyzing performance. Several tools are available for collecting and analyzing data from JMX MBeans, including many security information and event management (SIEM) tools, like Splunk.

* Heartbeat endpoint - For information about enabling and customizing heartbeat message reporting, see [Liveliness and responsiveness](pf_liveliness_responsiveness.html).

[Monitoring](pf_monitoring.html) discusses the JConsole monitoring tool that is included with the Java SE platform. For more information about the Comprehensive JConsole, see [Troubleshoot with the JConsole Tool](https://docs.oracle.com/javase/9/troubleshoot/diagnostic-tools.htm#JSTGD174) in the Oracle JDK documentation and [The Java Monitoring and Management Console (jconsole)](https://openjdk.org/tools/svc/jconsole/) in the OpenJDK documentation.

---

---
title: Runtime monitoring using JMX
description: PingFederate supports runtime monitoring and reporting through Java Management Extensions (JMX). JMX technology represents a Java-centric approach to application management and monitoring.
component: pingfederate
version: 13.1
page_id: pingfederate:pingfederate_monitoring_guide:pf_runtime_monitor_using_jmx
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/pingfederate_monitoring_guide/pf_runtime_monitor_using_jmx.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: November 29, 2022
section_ids:
  pingfederate-mbeans: PingFederate MBeans
  sample-jetty-metrics: Sample Jetty metrics
  advanced-jmx-configuration: Advanced JMX configuration
---

# Runtime monitoring using JMX

PingFederate supports runtime monitoring and reporting through Java Management Extensions (JMX). JMX technology represents a Java-centric approach to application management and monitoring.

JMX exposes instrumented code in the form of MBeans. Application management systems that support JMX technology, such as JConsole, can request runtime information from the PingFederate JMX server.

|   |                                                                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Authentication is required for JMX-client access to PingFederate runtime data. For more information, see [Configuring service authentication](../administrators_reference_guide/help_manageserviceauthenticationtasklet_serviceauthenticationstate.html). |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can use HTTP requests at any time to verify the status of the PingFederate server. For more information, see [Customizing the heartbeat message](../administrators_reference_guide/pf_customize_heartbeat_message.html).You can also supplement monitoring information by applying third-party analysis and reporting tools to the security audit log, in which PingFederate records fine-grain details, including response times and event types, for all server transactions. For more information, see [Security audit logging](../administrators_reference_guide/pf_security_audit_logging.html). |

PingFederate JMX server reports monitoring data for single sign-on (SSO) and single logout (SLO) transactions. In addition, numerous Jetty-standard MBeans are available to the PingFederate server's JMX clients.

## PingFederate MBeans

PingFederate provides MBeans for tracking server performance. The attributes exposed by these MBeans align with those available at the [heartbeat endpoint](pf_liveliness_responsiveness.html). Most statistics and counts are calculated over a period. You can configure the period's length in the file `com.pingidentity.monitoring.MonitoringService.xml`.

* `TOTAL_TRANSACTIONS`: The total number of SSO, SLO, and STS transactions processed since the server started. PingFederate resets this counter to zero after restart.

* `TOTAL_FAILED_TRANSACTIONS`: The total number of failed transactions since the server started. PingFederate resets this counter to zero after restart.

* `dataStores`: The request rate and response time statistics for data stores

* `adapters`: The request rate and response time statistics for adapters

* `connections`: The request rate and response time statistics for connections

* `cluster`: Cluster membership and the request rate and response time statistics for cluster Remote Procedure Calls (RPCs)

* `httpRequests.admin`: The request rate and response time statistics for HTTP requests to the administrative console

* `httpRequests.engine`: The request rate and response time statistics for HTTP requests to PingFederate's runtime endpoints

* `stateMaps`: The current number of entries in various runtime state maps

* `transactions`: The counts of all transactions and failed transactions, including values for the previous period and accumulated totals since the server started

## Sample Jetty metrics

The following table describes examples of Jetty MBean metrics, available through JMX, that you might find useful to supplement the information that the PingFederate-specific MBeans provide.

| MBean                                                                                                                                                                          | Attributes                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `org.eclipse.jetty.io: connectionstatistics`For Jetty connectors including the primary and secondary PingFederate runtime server ports.                                        | `connectionsTotal` – Total number of TCP connections accepted by the server`connectionDuration*` – How long connections are kept open. Maximum, mean, and standard deviation are available`connections` – Current number of open connections. Maximum is also available (`connectionsMax`)                                                                                            |
| `org.eclipse.jetty.server.handler: statisticshandler`                                                                                                                          | `requests` – Total number of requests received`requestsActive` – Number of requests currently being processed. Max is also available`requestTime` – Request duration. Maximum, mean, standard deviation, and total accumulated time are available`responses1xx, responses2xx, responses3xx`, … – Total number of requests that returned HTTP status codes of 1xx, 2xx, 3xx, and so on |
| `org.eclipse.jetty.util.thread: queuedthreadpool`Two pools: one for the runtime server, with 200 maximum threads; one for the administrative console, with 20 maximum threads. | `idleThreads` – Number of idle threads currently available`threads` – Number of threads currently running, including both idle and active`minThreads` – Minimum number of threads in the pool`maxThreads` – Maximum number of threads in the pool`lowOnThreads` – A boolean flag indicating whether the pool is running low on threads                                                |
| `java.lang: Memory``java.lang: MemoryPool``java.lang: GarbageCollection``java.lang: OperatingSystem`                                                                           | Attributes measuring CPU usage and memory                                                                                                                                                                                                                                                                                                                                             |

## Advanced JMX configuration

PingFederate uses port 1099 for its JMX server. You can change the port and other Java Message Service (JMS) settings by modifying the `jmx-remote-config.xml` file in the `<pf_install>/pingfederate/server/default/conf` directory.

|   |                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When connecting to the JMX service using SSL, the default, ensure that the client trusts the PingFederate SSL server certificate presented. For more information, see [Manage SSL server certificates](../administrators_reference_guide/help_certmanagementtasklet_sslservercerts_certmanagementstate.html). |

---

---
title: Splunk dashboards and audit logs
description: Ping provides a free Splunk for PingFederate application that customers can use to create dashboards.
component: pingfederate
version: 13.1
page_id: pingfederate:pingfederate_monitoring_guide:pf_splunk_dashboard_audit_log
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/pingfederate_monitoring_guide/pf_splunk_dashboard_audit_log.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  examples-of-splunk-dashboards: Examples of Splunk dashboards
---

# Splunk dashboards and audit logs

Ping provides a free [Splunk for PingFederate](https://splunkbase.splunk.com/app/976) application that customers can use to create dashboards.

This application takes advantage of the [Writing audit logs for Splunk](../administrators_reference_guide/pf_writin_audit_log_splunk.html) and [Outbound provisioning audit logging](../administrators_reference_guide/pf_outbound_provis_audit_loggin.html), which can be enabled in `log4j2.xml` file.

## Examples of Splunk dashboards

To help you review different events, the following dashboards are available from the top-level menu of the PingFederate app for Splunk:

* Account Manager

* Identity Provider

* Service Provider

* OAuth Server

![Screenshot of the Splunk Dashboard header showing the Account Management, Identity Provider, Service Provider and OAuth Server sub-menus.](_images/cqt1580336135938.png)

Click a menu item to view its sub-menus, as the following example shows for **OAuth Server**.

![Screenshot showing the OAuth Server sub-menu expanded displaying options for Client Request, Token Validation and Dynamic Client Registration.](_images/vlx1580490692708.png)

The following image shows the **Identity Provider Access** sub-menu dashboard with examples from the security audit log entries.

![Screenshot showing the Identity Provider Access sub-menu dashboard with example security audit log entries.](_images/xys1580490727302.png)

After you select a sub-menu, an image like the following **OAuth Server Client Request** example is displayed while the dashboard waits for the search results.

![Screenshot of the OAuth Server Client Request dashboard with the different sections waiting for search results.](_images/obx1580490763640.png)

After you click **Submit**, the dashboard displays the following search results for the client request.

![Screenshot of the Client Request dashboard with the search results displayed.](_images/wip1580490803929.png)

To view additional results, scroll downward or select another page. The following **Client Request** page provides an example.

![Screenshot of the Client Request page displaying additional results.](_images/bzv1580490837979.png)

The following images provide additional examples of the **Service Provider Access** sub-menu dashboard.

![Screenshot of the Server Provider Access sub-menu dashboard.](_images/dlz1580490867401.png)

![Screenshot of the Server Provider Access dashboard showing additional results.](_images/nyk1580490898863.png)

---

---
title: Thread pool
description: The following topic describes the MBeans tab and the recommended number of threads in the pool.
component: pingfederate
version: 13.1
page_id: pingfederate:pingfederate_monitoring_guide:pf_thread_pool
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/pingfederate_monitoring_guide/pf_thread_pool.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
---

# Thread pool

The following topic describes the MBeans tab and the recommended number of threads in the pool.

The **MBeans** tab provides access to the JMX Managed Beans and their available attributes and operations. Of particular interest are the `queuedthreadpool` instances that are available within the `org.eclipse.jetty.util.thread` bean. For example, instance 0 represents the thread pool that handles runtime requests. When you click the **Attributes** item for instance 0, the current state of the thread pool is displayed.

![Screenshot of the MBeans tab showing the current state of the thread pool.](_images/vcd1580332503811.png)

The number of threads in the pool (the `threads` attribute) can be compared to the number of threads that are not currently in use (the `idleThreads` attribute). Ideally, a sufficient number of threads is available to handle load spikes that occur during peak usage times, while also limiting the number of idle threads that are running. If the thread pool is too small, requests might be blocked. If the thread pool is too large, memory might be used unnecessarily, and CPU contention might increase, limiting the processing effectiveness.

We recommend allowing for 10 to 25% more threads than are typically active while the system executes a normal or expected load. Because most of your users will not be active at the same time, set the minimum threads to 10% above the average number of active threads that are observed during monitoring.

We also recommend setting the maximum number of threads to 25% above the average number of active threads that are observed while monitoring under expected load conditions. Make certain to weigh this recommendation against the observed CPU utilization metrics and the suggestions in the [About Performance Tuning](../performance_tuning_guide/pf_about_performance_tuning.html).