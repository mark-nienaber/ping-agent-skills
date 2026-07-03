---
title: Connecting to a local process
description: Use the local process option to establish a connection when the PingAccess server is running on a local system.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_monitoring_guide:pa_connecting_to_a_local_process
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_monitoring_guide/pa_connecting_to_a_local_process.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 12, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Connecting to a local process

Use the local process option to establish a connection when the PingAccess server is running on a local system.

## About this task

Unless you are running the PingAccess server as a Windows service, the easiest method to launch JConsole on the same machine as the server is to select **Local Process**. For information about connecting to a remote process instead, see [Connecting to a remote process](pa_connecting_to_a_remote_process.html).

To connect to a local instance and start the monitoring process:

## Steps

* In the **Local Process** list, select `com.pingidentity.pa.cli.Starter`, then click **Connect.**

  |   |                                                                                                           |
  | - | --------------------------------------------------------------------------------------------------------- |
  |   | If you are running the process locally, the system might prompt you to accept the connection as insecure. |

  ![Screen capture of the JConsole: New Connection window with the local process option and the com.pingidentity.pa.cli.Starter connection highlighted.](_images/mzs1580499549454.png)

---

---
title: Connecting to a remote process
description: Use the remote process option to establish a connection when the PingAccess server is running as a Windows service, or if the com.pingidentity.pa.cli.Starter class is unavailable in the Local Process list.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_monitoring_guide:pa_connecting_to_a_remote_process
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_monitoring_guide/pa_connecting_to_a_remote_process.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 12, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
  troubleshooting: Troubleshooting:
---

# Connecting to a remote process

Use the remote process option to establish a connection when the PingAccess server is running as a Windows service, or if the `com.pingidentity.pa.cli.Starter` class is unavailable in the **Local Process** list.

## About this task

Use these instructions to configure the remote process option to establish a connection. For demonstration purposes, the following task uses an Lightweight Directory Access Protocol (LDAP) *(tooltip: \<div class="paragraph">
\<p>An open, cross platform protocol used for interacting with directory services.\</p>
\</div>)* configuration.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | No direct configuration support is provided for enabling remote access Java Management Extensions (JMX) *(tooltip: \<div class="paragraph">&#xA;\<p>Java technology that provides tools for managing and monitoring applications, devices, system objects, and service-oriented networks.\</p>&#xA;\</div>)* for the PingAccess server. To enable this level of access, use the built-in options that are available through the Java Virtual Machine (JVM) *(tooltip: \<div class="paragraph">&#xA;\<p>A virtual machine that allows a computer to run Java programs and programs that are compiled to Java bytecode.\</p>&#xA;\</div>)*. For more information, see [Monitoring and Management Using JMX Technology](https://docs.oracle.com/javase/8/docs/technotes/guides/management/agent.html) in the Oracle Java Development Kit (JDK) *(tooltip: \<div class="paragraph">&#xA;\<p>A development environment for building applications and components using Java.\</p>&#xA;\</div>)* documentation. |

## Steps

1. In the `jvm-memory.options` file for the PingAccess server, add the following text at the end of the last memory settings:

   ```
   #Settings to enable remote access to JMX
   -Dcom.sun.management.jmxremote.port=5000"
   -Dcom.sun.management.jmxremote.login.config=ExampleCompanyConfig"
   #Configuration is assumed to be in the conf folder, relative path used
   -Djava.security.auth.login.config=conf/ldap.config"
   -Dcom.sun.management.jmxremote.ssl=false"
   ```

   |   |                                                                                                                                                          |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Each entry must reside on its own line. In this example, a relative path is used for the `ldap.config` file. Some deployments might require a full path. |

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | In a production environment, use Secure Sockets Layer (SSL) *(tooltip: \<div class="paragraph">&#xA;\<p>A protocol for authenticated and encrypted links between networked machines, typically over HTTPS. SSL was deprecated in 1999 in favor of Transport Layer Security (TLS).\</p>&#xA;\</div>)*, as shown in this example for initial testing and debugging. For information about setting up SSL, see [Monitoring and Management Using JMX Technology](https://docs.oracle.com/javase/8/docs/technotes/guides/management/agent.html) in the Oracle JDK documentation. |

2. Create the `ldap.config` file.

   ```
   ExampleCompanyConfig {
       com.sun.security.auth.module.LdapLoginModule REQUIRED
       userProvider="ldaps://ldap.server:port/OU=where,OU=users,OU=located"
       userFilter="(&(uid={USERNAME})(objectClass=inetOrgPerson))"
       authIdentity="uid={USERNAME},OU=where,OU=users,OU=located"
       authzIdentity=monitorRole
       useSSL=true;
       };
   ```

   |   |                                                                                                                                                                                                                                                                                                                                                    |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Each entry must reside on its own line. In this example, `ldap.config` is placed in the PingAccess `conf` folder. If your JVM setup trusts the certificates, you can use SSL. Because of the `authIdentity` option, the configuration binds as the user that you enter. Otherwise, an anonymous bind validates the user name but not the password. |

3. Place the `ldap.config` file that you created in step 2 in a location from which the PingAccess process can read it at start up.

4. If you have a clustered PingAccess environment:

   1. Perform steps 1 - 3 to each node in the cluster.

   2. Restart each node.

5. After you enable the JMX service, connect to the remote JMX service by specifying one of the following:

   ### Choose from:

   * The name of the PingAccess server instance

   * The Internet Protocol (IP) *(tooltip: \<div class="paragraph">
     \<p>The method by which data is sent across the internet from the source host to the destination host.\</p>
     \</div>)* address, port, and authentication credentials.

     ![A screen capture of the JConsole: New Connection window for connecting through a remote process.](_images/wcy1580499695401.png)

     |   |                                                                                                                                                                                                                                                                                    |
     | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | Because JMX uses SSL by default when communicating with a remote host, the client host must trust the SSL certificate that is presented during setup for JMX. If the JMX client does not trust the JMX certificate, it displays the following message:```
     ConnectionFailedSSL1
     ``` |

   ![A screen capture of the failed connection error message.](_images/odg1580499734034.png)

### Troubleshooting:

1. If SSL is enabled, import the JMX SSL certificate to the client's trusted certificates.

2. If SSL is disabled, click **Insecure** to connect.

---

---
title: Connecting with JMX
description: The Java Management Extensions (JMX) MBeans agent included on the Java SE platform enables connections to local and remote Java clients to monitor performance.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_monitoring_guide:pa_connecting_with_jmx
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_monitoring_guide/pa_connecting_with_jmx.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 27, 2024
---

# Connecting with JMX

The Java Management Extensions (JMX) *(tooltip: \<div class="paragraph">
\<p>Java technology that provides tools for managing and monitoring applications, devices, system objects, and service-oriented networks.\</p>
\</div>)* MBeans agent included on the Java SE platform enables connections to local and remote Java clients to monitor performance.

JConsole permits connections to local and remote Java processes.

|   |                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------- |
|   | If your instance of PingFederate is running as a Windows service, you must connect through the remote option. |

* For information on connecting to a local process, see [Connecting to a local process](pa_connecting_to_a_local_process.html).

* For information on connecting to a remote process, see [Connecting to a remote process](pa_connecting_to_a_remote_process.html).

---

---
title: Creating an error-only server log
description: Modify your log4j2.xml file to set up a specific log to log only ERROR-level and higher notifications.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_monitoring_guide:pa_creating_an_error_only_server_log
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_monitoring_guide/pa_creating_an_error_only_server_log.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 12, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  example: Example:
---

# Creating an error-only server log

Modify your `log4j2.xml` file to set up a specific log to log only `ERROR`-level and higher notifications.

## About this task

Monitor the `pingaccess.log` file for `ERROR`-level messages. You can configure alerts to send notifications when events occur and to improve the monitoring of these events. Even when levels are down to a minimum, the server log generates large amounts of information in an active production environment. You can set up a specific log to log only `ERROR`-level and higher alerts, which can be sent to a security information and event management (SIEM) tool, such as Splunk, when they occur.

To change your `log4j2.xml` file to enable a separate log file:

## Steps

1. Create an appender.

   |   |                                                                                     |
   | - | ----------------------------------------------------------------------------------- |
   |   | The simplest way to create an appender is to copy an existing one to use as a base. |

   In the following example, the `RollingFile` is the same one that the `pingaccess.log` file uses. The bold text identifies items that have been changed.

   ```
   <!-- Error Only Main Log : A size based file rolling appender -->
   <RollingFile name="FILEERR"
            	fileName="${sys:pa.home}/log/pingaccess.error.log"
            	filePattern="${sys:pa.home}/log/pingaccess.error.log.%i"
            	ignoreExceptions="false">
   	<PatternLayout>
       	<!-- Uncomment this if you want to use UTF-8 encoding instead of system's default encoding. -->
       	<!--
       	<charset>UTF-8</charset>
       	-->
       	<!--
           	To Activate location information uncomment the following pattern,
           	comment out the current pattern and set "includeLocation" to true
           	in "com.pingidentity" async logger.
       	-->
       	<!--
       	<pattern>%d{ISO8601} %5p [%X{exchangeId}] %c:%L - %m%n</pattern>
       	-->
       	<pattern>%d{ISO8601} %5p [%X{exchangeId}] %c - %m%n</pattern>
   	</PatternLayout>
   	<Policies>
       	<SizeBasedTriggeringPolicy size="100000 KB"/>
   	</Policies>
   	<DefaultRolloverStrategy max="10"/>
   </RollingFile>
   ```

2. Set the appender that you created in step 1 for `AsyncRoot` at the end of your `log4j2.xml` file.

   The following example shows the necessary changes. In this example, the `level` attribute indicates the level of messages that are sent to the log file.

   ```
   <!-- Root Logger-->
   <AsyncRoot level="INFO" includeLocation="false" >
   	<AppenderRef ref="File"/>
   	<AppenderRef ref="FILEERR" level="ERROR"/>
   </AsyncRoot>
   ```

3. Remove the attribute `additivity="false"` from all other loggers that contain a reference to the `File` appender.

   ### Example:

   ```
   <AsyncLogger name="com.pingidentity" level="DEBUG" additivity="false"
             includeLocation="false">
   ```

   **Becomes:**

   ```
   <AsyncLogger name="com.pingidentity" level="DEBUG"
           includeLocation="false">
   ```

4. Restart the PingAccess server.

5. If you have a clustered environment, perform steps 1-4 on all nodes within the cluster.

   |   |                                                                                                      |
   | - | ---------------------------------------------------------------------------------------------------- |
   |   | To expedite this step, create a base file with the appropriate changes and copy it to all the nodes. |

---

---
title: Customizing the heartbeat message
description: "Customize the amount of detail included in the heartbeat endpoint's response."
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_monitoring_guide:customizing_the_heartbeat_message
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_monitoring_guide/customizing_the_heartbeat_message.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 28, 2026
section_ids:
  steps: Steps
  choose-from: Choose from:
  example: Example:
---

# Customizing the heartbeat message

The [heartbeat endpoint](../reference_guides/pa_heartbeat_endpoint.html), `/pa/heartbeat.ping`, returns a 200 HTTP status code and a customizable `OK` browser message if the PingAccess server is running.

You can customize the amount of detail included in the browser message by modifying the `enable.detailed.heartbeat.response` PingAccess property.

|   |                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If a GET request receives a connection error or an HTTP status code other than 200, the server associated with the endpoint is either down or malfunctioning. |

## Steps

1. To configure the heartbeat response level, make the following changes to the `<PA_HOME>/conf/run.properties` file.

   Learn more about the following properties in the [Configuration file reference](../reference_guides/pa_config_file_ref.html#pa-monitoring).

   1. To configure the level of detail included in the heartbeat response, set the `enable.detailed.heartbeat.response` property to `true` or `false`.

      While the PingAccess server is running, calls to the heartbeat endpoint result in the following behavior, depending on the value of this property:

      * `false` (default)

        The `/pa/heartbeat.ping` endpoint returns only the HTTP status code and `OK` message.

      * `true`

        The `/pa/heartbeat.ping` endpoint returns all available statistics. The response output format is an Apache Velocity template defined in `<PA_HOME>/conf/template/heartbeat.page.json`.

      |   |                                                                                                                                                                                          |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Before exposing these additional statistics on the heartbeat endpoint, ensure the endpoint cannot be reached beyond the load balancer so this information isn't made publicly available. |

   2. If `enable.detailed.heartbeat.response` is set to `true`, enter a value for the `pa.statistics.window.seconds` property to establish how long PingAccess should spend collecting statistics before providing the heartbeat response.

   3. You must restart PingAccess for changes to the `run.properties` file to take effect.

2. To customize the heartbeat template, edit the `heartbeat.page.json` file, located in the `<PA_HOME>/conf/template` directory.

   The following template values are available for modification.

   > **Collapse: Template values**
   >
   > | Value                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
   > | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | `$monitor.getTotalJvmMemory('bytes'\|'KB'\|'MB'\|'GB')`                | Returns the total memory in the Java Virtual Machine (JVM) *(tooltip: \<div class="paragraph">&#xA;\<p>A virtual machine that allows a computer to run Java programs and programs that are compiled to Java bytecode.\</p>&#xA;\</div>)*.Enter `'bytes'`, `'KB'`, `'MB'`, or `'GB'` to specify the units. The default value is `'bytes'`.                                                                                                                                                                                                                                                                 |
   > | `$monitor.getUsedJvmMemory('bytes'\|'KB'\|'MB'\|'GB')`                 | Returns the used memory in the JVM.Enter `'bytes'`, `'KB'`, `'MB'`, or `'GB'` to specify the units. The default value is `'bytes'`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   > | `$monitor.getFreeJvmMemory('bytes'\|'KB'\|'MB'\|'GB')`                 | Returns the free memory in the JVM. Enter `'bytes'`, `'KB'`, `'MB'`, or `'GB'` to specify the units. The default value is `'bytes'`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   > | `$monitor.getTotalPhysicalSystemMemory('bytes'\|'KB'\|'MB'\|'GB')`     | Returns the total system memory.Enter `'bytes'`, `'KB'`, `'MB'`, or `'GB'` to specify the units. If you don't specify the units, `'bytes'` is the default value.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
   > | `$monitor.getTotalFreePhysicalSystemMemory('bytes'\|'KB'\|'MB'\|'GB')` | Returns the free system memory. Enter `'bytes'`, `'KB'`, `'MB'`, or `'GB'` to specify the units. If you don't specify the units, `'bytes'` is the default value.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
   > | `$monitor.getTotalUsedPhysicalSystemMemory('bytes'\|'KB'\|'MB'\|'GB')` | Returns the used system memory. Enter `'bytes'`, `'KB'`, `'MB'`, or `'GB'` to specify the units. If you don't specify the units, `'bytes'` is the default value.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
   > | `$monitor.getHostname()`                                               | Returns the host name for the system running PingAccess.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   > | `$monitor.getNumberOfCpus()`                                           | Returns the number of CPU cores in the system.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
   > | `$monitor.getCpuLoad('###.##')`                                        | Returns the CPU utilization. The parameter contains an optional format value:- If the format is specified, the value returned is a percentage value from 0%-100%, formatted using the [Java DecimalFormat](http://docs.oracle.com/javase/7/docs/api/java/text/DecimalFormat.html) specification.
   >
   > - If no format value is specified, then the value returned is a real number from 0 to 1 which represents the CPU utilization percentage.For example, a format value of `'###.##'` will return a value similar to `'56.12'`, but no specified format would cause the value to be returned as `'0.5612'`. |
   > | `$monitor.getOpenClientConnections()`                                  | Returns the number of clients connected to PingAccess.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   > | `$monitor.getNumberOfVirtualHosts()`                                   | Returns the number of configured virtual hosts in PingAccess.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
   > | `$monitor.getNumberOfApplications()`                                   | Returns the number of configured applications in PingAccess.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
   > | `$monitor.getNumberOfSites()`                                          | Returns the number of configured sites in the PingAccess configuration database. In a clustered environment, on the engine nodes, this number will reflect the number of sites associated with applications rather than the number of configured sites that show on the admin node.You can find more information in the [Clustering in PingAccess](../reference_guides/pa_clustering_ref_guide.html) documentation.&#xA;&#xA;This value isn't included in the default template but can be added by the system administrator if desired.                                                                   |
   > | `$monitor.getLastRefreshTime('yyyy/MM/dd HH:mm:ss')`                   | Returns the time that the PingAccess configuration was last refreshed.The parameter informs which date format to use:- If the parameter isn't specified, the ISO 8601 date format is used.
   >
   > - If the parameter is specified, the format used comes from the [Joda DateTimeFormat](https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormatter.html) specification.                                                                                                                                                                                                                      |

   |   |                                                                                                                                                                           |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The default content type for the output is `application/json`. However, you can specify a content type header using the `$monitor.setContentType()` line in the template. |

   1. To specify percentiles in addition to, or in place of, the default 90th percentile in the statistics reported on the heartbeat, go to the following line:

      ```html
      ##    "response.time.statistics.90.percentile": "$monitor.getProcessingStatistics().getResponseTimePercentileMs(90.0, '###.##')":
      ```

      |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
      | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | The `ProcessingStatistics.getResponseTimePercentileMs(p, '###.##')` function allows you to customize the percentiles displayed in the heartbeat endpoint response for the metrics ending in `.<p>.percentile`. Percentiles can be a helpful way to understand a metric's distribution and identify patterns or trends over time. They can also be used to set performance targets or to identify bottlenecks in a system.In the context of server response metrics, you can use percentiles to compare a server's response time to other servers or previous periods. |

      You can use decimal values as described in the previous `$monitor.getCpuLoad('###.##')` table entry.

      To update the percentile, do one of the following.

      ### Choose from:

      * To change the percentile value, replace `.90` with the desired percentile value:

        ```html
        ##    "response.time.statistics.75.percentile": "$monitor.getProcessingStatistics().getResponseTimePercentileMs(75.0, '###.##')",
        ```

      * To specify a percentile in addition to the default 90th percentile, add a new line using the same format:

        ```html
        "response.time.statistics.90.percentile": "$monitor.getProcessingStatistics().getResponseTimePercentileMs(90.0, '###.##')",
        "response.time.statistics.50.percentile": "$monitor.getProcessingStatistics().getResponseTimePercentileMs(50.0, '###.##')",
        ```

        ### Example:

        > **Collapse: Details**
        >
        > Setting the value to `50` will display the 50th percentile of a server's response time in the heartbeat endpoint response. A value of `200` milliseconds for the 50th percentile means that 50% of the server's responses were faster than 200 milliseconds, while 50% were slower.
        >
        > Similarly, a value of `500` milliseconds for the 95th percentile means that 95% of the server's responses were faster than 500 milliseconds, while 5% were slower.

   2. Save your changes.

3. For a clustered PingAccess environment, repeat these steps on each node.

---

---
title: Liveliness and responsiveness
description: One of the simpler methods for monitoring the performance of a PingAccess deployment is determining whether the PingAccess server is available and responsive. To help you identify the status of a server, PingAccess provides a heartbeat request endpoint.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_monitoring_guide:pa_liveliness_and_responsiveness
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_monitoring_guide/pa_liveliness_and_responsiveness.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 1, 2026
section_ids:
  using-the-heartbeat-endpoint: Using the heartbeat endpoint
  modifying-the-heartbeat-message: Modifying the heartbeat message
  example: Example
  server-metrics: Server metrics table
  logging-response-times: Logging response times
  example-2: Example
---

# Liveliness and responsiveness

One of the simpler methods for monitoring the performance of a PingAccess deployment is determining whether the PingAccess server is available and responsive. To help you identify the status of a server, PingAccess provides a *heartbeat request endpoint*.

## Using the heartbeat endpoint

When the PingAccess server is running, sending a request to the `/pa/heartbeat.ping` endpoint (or `/<Application Context Root>/pa/heartbeat.ping` if you have the **Use context root as reserved resource base path** checkbox enabled on your PingAccess application) should return an `200 OK` message. If the request times out or takes a long time to complete, the server might be overloaded or experiencing other difficulties.

We recommend that you develop a baseline for the desired response time by testing the [heartbeat endpoint](../reference_guides/pa_heartbeat_endpoint.html) of your deployment at various times. This endpoint can be useful when [load balancing](../pingaccess_user_interface_reference_guide/pa_load_balancing_strategies.html) a [cluster](../reference_guides/pa_clustering_ref_guide.html) of PingAccess server instances. Some load balancers can alter the number of requests that are sent to a particular server based on the response code received, or the responsiveness of requests that are made to the heartbeat endpoint.

## Modifying the heartbeat message

You can modify the output of the heartbeat to provide performance-related information, such as CPU and memory usage, along with response times. The response metrics can help you make better auto-scaling decisions. The map size metrics can help you recognize performance issues. Learn more in [Customizing the heartbeat message](customizing_the_heartbeat_message.html).

### Example

The following example demonstrates the JSON response data returned after changing the `heartbeat.page.json` template file to show the memory, CPU, and response time.

|   |                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This example contains PingAccess server metrics available from the heartbeat endpoint. You can find more information about these metrics in the [Server metrics table](#server-metrics). |

> **Collapse: Example JSON response data**
>
> ```json
> {
>   "items": [
>     {
>       "response.statistics.window.seconds": "5",
>       "response.statistics.count": "1",
>       "response.time.statistics.90.percentile": "129",
>       "response.time.statistics.mean": "129",
>       "response.time.statistics.max":"129",
>       "response.time.statistics.min": "129",
>       "response.concurrency.statistics.90.percentile": "1",
>       "response.concurrency.statistics.mean": "1",
>       "response.concurrency.statistics.max": "1",
>       "response.concurrency.statistics.min": "1",
>       "cpu.load": "15.53",
>       "total.jvm.memory": "500.695 MB",
>       "free.jvm.memory": "215.339 MB",
>       "used.jvm.memory": "285.356 MB",
>       "total.physical.system.memory": "17.18 GB",
>       "total.free.physical.system.memory": "278.45 MB",
>       "total.used.physical.system.memory": "16.901 GB",
>       "number.of.cpus": "8",
>       "hostname": "jdasilva-r",
>       "open.client.connections": "1",
>       "number.of.applications": "11",
>       "number.of.virtual.hosts": "6",
>       "last.refresh.time": "1969-12-31T18:00:00.000Z"
>     }
>   ]
> }
> ```

### Server metrics table

The following table describes all the PingAccess server metrics available from the heartbeat endpoint.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In the following table, for server metrics that end in `.90.percentile`, the current `90` value is determined by the function calling the `ProcessingStatistics.getResponseTimePercentileMs(p, '###.##')` line in the `heartbeat.page.json` file. `90` is the default value.You can find more information on how to edit this value in step 4 of [Customizing the heartbeat message](customizing_the_heartbeat_message.html). |

> **Collapse: Server metrics**
>
> | Server metrics                                    | Description                                                                                                                                                                                                                       |
> | ------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | **response.statistics.window\.seconds**           | The time interval, in seconds, for the statistics report.This is an echo of the `pa.statistics.window.seconds` property's value. It provides context for the concurrency and time statistics.                                     |
> | **response.statistics.count**                     | The number of items considered in the heartbeat report for the time and concurrency statistics.                                                                                                                                   |
> | **response.time.statistics.90.percentile**        | The 90th percentile response time, in milliseconds, during the statistics window\.For example, if this value is 168, then 90% of the report samples had response times below 168 milliseconds.                                    |
> | **response.time.statistics.mean**                 | The mean time, in milliseconds, that the PingAccess server took to respond during the statistics window.                                                                                                                          |
> | **response.time.statistics.max**                  | The longest time, in milliseconds, that the PingAccess server took to respond during the statistics window.                                                                                                                       |
> | **response.time.statistics.min**                  | The shortest time, in milliseconds, that the PingAccess server took to respond during the statistics window.                                                                                                                      |
> | **response.concurrency.statistics.90.percentile** | The 90th percentile response concurrency during the statistics window\.For example, if this value is 124, then 90% of the report samples had response concurrency values below 124.                                               |
> | **response.concurrency.statistics.mean**          | The mean number of HTTP requests that the PingAccess server processed concurrently during the statistics window.                                                                                                                  |
> | **response.concurrency.statistics.max**           | The maximum number of HTTP requests that the PingAccess server processed concurrently during the statistics window.                                                                                                               |
> | **response.concurrency.statistics.min**           | The minimum number of HTTP requests that the PingAccess server processed concurrently during the statistics window.                                                                                                               |
> | **cpu.load**                                      | The load on the PingAccess server's cores as a percentage of total capacity.                                                                                                                                                      |
> | **total.jvm.memory**                              | The total memory of the Java Virtual Machine (JVM) *(tooltip: \<div class="paragraph">&#xA;\<p>A virtual machine that allows a computer to run Java programs and programs that are compiled to Java bytecode.\</p>&#xA;\</div>)*. |
> | **free.jvm.memory**                               | The free memory of the JVM.                                                                                                                                                                                                       |
> | **used.jvm.memory**                               | The used memory of the JVM.                                                                                                                                                                                                       |
> | **total.physical.system.memory**                  | The total system memory.                                                                                                                                                                                                          |
> | **total.free.physical.system.memory**             | The free system memory.                                                                                                                                                                                                           |
> | **total.used.physical.system.memory**             | The used system memory.                                                                                                                                                                                                           |
> | **number.of.cpus**                                | The number of cores on the PingAccess server.                                                                                                                                                                                     |
> | **hostname**                                      | The host name of the system running PingAccess.                                                                                                                                                                                   |
> | **open.client.connections**                       | The number of clients connected to PingAccess.                                                                                                                                                                                    |
> | **number.of.applications**                        | The number of configured applications in PingAccess.                                                                                                                                                                              |
> | **number.of.virtual.hosts**                       | The number of configured virtual hosts in PingAccess.                                                                                                                                                                             |
> | **last.refresh.time**                             | Returns the time that the PingAccess configuration was last refreshed, in ISO 8601 date format.                                                                                                                                   |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | As indicated in the table, the values of some metrics are calculated over a configurable time window. The default statistics window is zero seconds.To customize the statistics window period, change the value of the `pa.statistics.window.seconds` property in the `<PA_HOME>/conf/run.properties` file. Learn more in the [Configuration file reference](../reference_guides/pa_config_file_ref.html#pa-monitoring). |

## Logging response times

By default, the audit logs record the processing time for each transaction. You can enable audit logging to identify the speed at which PingAccess processes web and API application transactions.

|   |                                                                                        |
| - | -------------------------------------------------------------------------------------- |
|   | Depending on your logging configuration, audit logging might not log any transactions. |

### Example

The following example shows an entry from the default audit log, specifically the included processing times:

```none
2019-12-15T17:23:12,192|GRmozOujPDDFct8RbtnfJw|tid:wUu9F0vDd9pZPKe4Oc5Ym_-RFCc..9r72.v8c0Y2CUA5qSpvcxKHgd7QoCp|
81 ms | 50 ms | 0 ms| servapp.ext.wal-ping.com [] /SimpleWebApi /*:3000| joe| Cookie| 127.0.0.1| GET| /SimpleWebApi/web/web.jsp| 200| | | Web-API| Root Resource| /*
```

Processing times are as follows:

* Total round trip: 81 ms.

  Learn more in the `AUDIT.roundTripMS` audit log element.

* Proxy round trip: 50 ms.

  Learn more in the `AUDIT.proxyRoundTripMS` audit log element.

* UserInfo round trip: 0 ms.

  The total number of milliseconds PingAccess spent making a backchannel call to the OIDC [UserInfo endpoint](https://docs.pingidentity.com/pingfederate/13.0/developers_reference_guide/pf_userinfo_endpoint.html) and waiting for a response. A value of 0 ms indicates that a call wasn't made. Calls might be omitted on subsequent log entries.

You can find more information about logging in [Log configuration](../configuring_and_customizing_pingaccess/pa_logging_configuration.html) and the elements of a log entry in [Security audit logging](../configuring_and_customizing_pingaccess/pa_security_audit_logging.html).

---

---
title: Logging, reporting, and troubleshooting
description: This section provides a brief summary and purpose of the available logging, reporting, and troubleshooting for PingAccess.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_monitoring_guide:pa_logging_reporting_and_troubleshooting
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_monitoring_guide/pa_logging_reporting_and_troubleshooting.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 12, 2024
---

# Logging, reporting, and troubleshooting

This section provides a brief summary and purpose of the available logging, reporting, and troubleshooting for PingAccess.

The following table identifies the available PingAccess logs and their purposes.

> **Collapse: PingAccess Logs and Purposes**
>
> | Name                                   | Purpose                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
> | -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | `pingaccess.log`                       | Primary troubleshooting log. Records PingAccess runtime and administrative server activities.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
> | `pingaccess_engine_audit.log`          | Records transactions of configured resources. Additionally, the log records transaction details when PingAccess sends requests to PingFederate, such as Security Token Service (STS) *(tooltip: \<div class="paragraph">&#xA;\<p>An entity responsible for responding to WS-Trust requests for validation and issuance of security tokens used for SSO authentication to web services.\</p>&#xA;\</div>)*, OAuth2, and JSON Web Signature (JWS) *(tooltip: \<div class="paragraph">&#xA;\<p>A signed instance of a JSON Web Token (JWT) based on IETF standard syntax and used for the exchange of signed content.\</p>&#xA;\</div>)* requests. |
> | `pingaccess_api_audit.log`             | Records PingAccess administrative application programming interface (API) *(tooltip: \<div class="paragraph">&#xA;\<p>A specification of interactions available for building software to access an application or service.\</p>&#xA;\</div>)* transactions. These transactions capture activity in the PingAccess administrative console. If you're using scripts to configure PingAccess, this log also records transaction activity.                                                                                                                                                                                                          |
> | `pingaccess_agent_audit.log`           | Records transactions between PingAccess agents and the PingAccess engine.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
> | `pingaccess_sideband_client_audit.log` | Records transactions sent to and from the sideband client integration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
> | `pingaccess_sideband_audit.log`        | Records the end-user transactions that the sideband client request captures.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

> **Collapse: Troubleshooting**
>
> * The `pingaccess.log` file is the primary troubleshooting log.
>
> * Alongside an HTTP trace from the browser, which you can generate from a debugging application like Fiddler, the `pingaccess_engine_audit.log` and `pingaccess_agent_audit.log` files are helpful for identifying issues that must be resolved.
>
> For more information about managing PingAccess logs, see [Log configuration](../configuring_and_customizing_pingaccess/pa_logging_configuration.html).

---

---
title: Monitoring
description: The JConsole monitoring interface is accessible after establishing a connection. This section outlines the key Java Virtual Machine (JVM) performance metrics for evaluating the activity of your PingAccess deployment.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_monitoring_guide:pa_monitoring
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_monitoring_guide/pa_monitoring.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 12, 2024
---

# Monitoring

The JConsole monitoring interface is accessible after establishing a connection. This section outlines the key Java Virtual Machine (JVM) *(tooltip: \<div class="paragraph">
\<p>A virtual machine that allows a computer to run Java programs and programs that are compiled to Java bytecode.\</p>
\</div>)* performance metrics for evaluating the activity of your PingAccess deployment.

> **Collapse: Monitoring clustered PingAccess engines**
>
> The JConsole can be connected to multiple processes. To monitor several instances of the PingAccess server after a connection is established, go to **Connection → New Connection** and add the additional connection.

> **Collapse: Monitoring CPU utilization**
>
> The **Overview** tab provides a dashboard of the following performance and resource-utilization charts:
>
> * Heap memory usage (cumulative memory that is used by all memory pools)
>
> * Live threads
>
> * CPU usage
>
> * Classes (number of classes that are loaded)
>
> This tab provides a high-level view of the JVM's performance metrics.
>
> ![A screen capture of the Java Monitoring Console showing CPU usage charts.](_images/rhr1580499858821.png)
>
> Use the **Overview** tab to visualize and collect CPU usage data. When your PingAccess deployment is subjected to its normal or expected load, the CPU utilization typically falls between 60% and 80%. If the system registers consistently at 80% or higher, additional CPU resources might be necessary to handle load spikes that occur during peak usage times.

> **Collapse: Monitoring memory utilization**
>
> The **Overview** tab shows only overall heap usage. To view additional details about memory utilization, click the **Memory** tab, which lets you analyze usage patterns usage in specific memory pools within the heap. This tab also provides information about the overall heap utilization profile.

> **Collapse: Old Generation space**
>
> Objects that survive a sufficient number of garbage-collection cycles are promoted to the Old Generation. To view the memory usage in the pool of such objects, go to **Memory Pool → PS Old Gen** or **Memory Pool → G1 Old**, depending on the relevant garbage collector. The PingAccess server services mostly short-lived transactions, such as single sign-on (SSO) *(tooltip: \<div class="paragraph">
> \<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
> \</div>)*, Security Token Service (STS) *(tooltip: \<div class="paragraph">
> \<p>An entity responsible for responding to WS-Trust requests for validation and issuance of security tokens used for SSO authentication to web services.\</p>
> \</div>)*, and OAuth *(tooltip: \<div class="paragraph">
> \<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
> \</div>)* requests. Most of the created memory objects are required only for a short period of time.
>
> Although the PingAccess server makes use of some memory objects that are medium- to long-lived, such as session data for authentication sessions, adapter sessions, or single logout (SLO) *(tooltip: \<div class="paragraph">
> \<p>The process of signing a user out of multiple sites where the user has started a SSO session.\</p>
> \</div>)* functionality, most of the objects that are promoted to the Old Generation are likely to become garbage that requires cleaning up. If the younger generation, or Eden space, is not sized appropriately, objects are moved to and retained in the Old Generation before they are collected as garbage. If size limitations prevent the Old Generation from accumulating future garbage as well as longer-lived objects, then garbage-collection cycles occur more frequently.
>
> The Old Generation space is the most important space to monitor. It is easy to identify if the heap is sized and proportioned appropriately for a specific load, based on its usage pattern. The following examples involve two Old Generation usage charts. In both examples, the same user load executes the same workflow. The size of the heap represents the only difference.
>
> Because the heap is sized adequately in the first example, memory in the Old Generation rises at a reasonably slow rate. Garbage collection frees around 60% to 75% of the space, and room is available to accommodate the future garbage of newly created objects that are moved from the Eden space, as well as the longer-term objects that remain in use. Although the space is 1 GB in size, the average full (PS MarkSweep or G1 Old Generation) collection time is approximately only 240 milliseconds, or 0.728 seconds for three collections.
>
> ![A screen capture of the Memory Pool PS Old Gen chart measured in gigabytes.](_images/mgx1580500063039.png)
>
> When a heap is sized inadequately, the Old Generation runs out of space.
>
> In the following example, the amount of memory that becomes free with each garbage collection shrinks, due to the rate at which objects are promoted from the Eden space.
>
> ![A screen capture of the Memory Pool PS Old Gen chart measured in megabytes.](_images/via1580500186577.png)
>
> 184 PS MarkSweep (full) collections require garbage collections more frequently, totaling 60 seconds, or an average of 326 milliseconds per collection.

> **Collapse: Entire heap space**
>
> If the heap is sized appropriately for the load that the system must handle, it fills up and is followed by an appreciable drop in usage as a full garbage collection occurs, such as a PS MarkSweep collection triggered by the Old Generation filling up. In this example, the heap rises steadily, with drops from minor collections until a PS MarkSweep collection occurs and collects approximately 70% of the heap.
>
> ![A screen capture of the heap memory usage chart measured in gigabytes.](_images/vtq1580500277959.png)
>
> When the heap is undersized, full collections that are performed more frequently return less memory. In the following example, the frequency of Java Management Extensions (JMX) data that the JConsole retrieves does not keep pace with the frequency of full collections. As a result, only a fraction of them occur.
>
> ![A screen capture of the Memory Pool PS Old Gen chart measured in megabytes.](_images/shh1580500392163.png)

> **Collapse: Eden space**
>
> Regardless of whether the heap is adequately sized or undersized, the usage pattern is nearly identical with the Eden space. This similarity can be due to the sampling frequency of the data-collection tool because the number of samples might be insufficient to show that, with an undersized heap, memory is consumed and subsequently freed with greater frequency. The behavior of garbage collection in the Eden space is such that when it fills, the space is completely emptied by moving live objects to the Survivor and Old Generation spaces. Under load, the pattern resembles a jagged sawtooth, as shown in the following examples of an adequately sized heap and an undersized heap.
>
> ![A screen capture of the memory pool PS Eden space monitoring chart measured in gigabytes.](_images/qii1580500480713.png)
>
> ![A screen capture of the memory pool PS Eden space monitoring chart measured in megabytes.](_images/mks1580500659585.png)

> **Collapse:&#x20;**
>
> Because garbage collectors manage memory in the Java Runtime Environment (JRE) *(tooltip: \<div class="paragraph">
> \<p>A software layer that provides the class libraries and resources needed for a Java program to run.\</p>
> \</div>)*, simply increasing the size of the heap is not always the appropriate solution. The following table outlines the total heap size recommendations for the available garbage collectors, based on available CPU resources.
>
> For more information about garbage collectors, see [Garbage collector configuration reference](../reference_guides/pa_garbage_collector_config_ref.html).

> **Collapse: Total Heap Size Recommendations for Garbage Collectors**
>
> | Garbage collector     | Minimum recommended number of CPUs | Recommended heap size |
> | --------------------- | ---------------------------------- | --------------------- |
> | Parallel              | 4                                  | 6 GB maximum          |
> | Concurrent Mark Sweep | 12                                 | 4 - 6 GB minimum      |
> | Garbage First (G1)    | 12                                 | 6 GB minimum          |
>
> If additional memory is unavailable, or if increasing the size of the heap is inadvisable because of these recommendations, the load that is handled by this instance is probably too high. In such instances, consider adding additional resources to your deployment. To verify whether the load for the instance is too high, check the CPU utilization.
>
> To allow for the most efficient management of memory, set the minimum and maximum heap sizes to the maximum allowed values to avoid potentially expensive heap allocation resizing and divide it evenly between the young and old generations. If you are using the Garbage First collector, generational spaces are not specified through command line options because they are managed logically in real time. Even in such instances, we recommend setting the minimum and maximum heap sizes to the maximum allowed values.
>
> For more information about fine-tuning the JVM options in the `jvm-memory.options` file, see [Modifying the Java heap size](../reference_guides/pa_modifying_the_java_heap_size.html) in the Performance Tuning Reference Guide.

---

---
title: PingAccess Monitoring Guide
description: PingAccess provides a range of monitoring options, from simple heartbeat options for checking responsiveness to transaction response-time logging and resource-utilization metrics. These metrics can help you gain insight into the health and performance of your PingAccess deployment.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_monitoring_guide:pa_monitoring_guide
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_monitoring_guide/pa_monitoring_guide.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 12, 2024
---

# PingAccess Monitoring Guide

PingAccess provides a range of monitoring options, from simple heartbeat options for checking responsiveness to transaction response-time logging and resource-utilization metrics. These metrics can help you gain insight into the health and performance of your PingAccess deployment.

To help you monitor the performance of a PingAccess deployment, this guide provides:

* Suggestions for key performance metrics to monitor and means by which to monitor them

* Recommendations about resource-utilization thresholds and patterns

* Monitoring options, including logs that can be used to create Splunk dashboards

The features documented here are affected by the settings in the configuration file. For more information, see the [Configuration file reference](../reference_guides/pa_config_file_ref.html).

---

---
title: Resource metrics
description: PingAccess provides monitoring capabilities for resource-utilization metrics, such as thresholds and patterns, to strengthen the health and performance of your deployment.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_monitoring_guide:pa_resource_metrics
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_monitoring_guide/pa_resource_metrics.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 14, 2023
---

# Resource metrics

PingAccess provides monitoring capabilities for resource-utilization metrics, such as thresholds and patterns, to strengthen the health and performance of your deployment.

PingAccess provides the following mechanisms for obtaining resource metrics:

* Java Management Extensions (JMX) *(tooltip: \<div class="paragraph">
  \<p>Java technology that provides tools for managing and monitoring applications, devices, system objects, and service-oriented networks.\</p>
  \</div>)* - Ping recommends using JMX MBeans because this method provides a more comprehensive set of resource metric counters for analyzing performance. Several tools are available for collecting and analyzing data from JMX MBeans, including many security information and event management (SIEM) tools, such as Splunk.

* Heartbeat endpoint - For more information about enabling heartbeat message reporting, see [Heartbeat endpoint](../reference_guides/pa_heartbeat_endpoint.html).

[Monitoring](pa_monitoring.html) discusses the JConsole monitoring tool which is included with the Java SE platform. For more information about the Comprehensive JConsole, see [Troubleshoot with the JConsole Tool](https://docs.oracle.com/javase/9/troubleshoot/diagnostic-tools.htm#JSTGD174) in the Oracle Java Development Kit (JDK) *(tooltip: \<div class="paragraph">
\<p>A development environment for building applications and components using Java.\</p>
\</div>)* documentation and [The Java Monitoring and Management Console (jconsole)](http://openjdk.java.net/tools/svc/jconsole/) in the OpenJDK documentation.

---

---
title: Splunk audit log
description: PingAccess can enable and write audit logs for Splunk to effectively collect and analyze data from Java Management Extensions (JMX) MBeans.
component: pingaccess
version: 9.1
page_id: pingaccess:pingaccess_monitoring_guide:pa_splunk_audit_log
canonical_url: https://docs.pingidentity.com/pingaccess/9.1/pingaccess_monitoring_guide/pa_splunk_audit_log.html
llms_txt: https://docs.pingidentity.com/pingaccess/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 12, 2024
---

# Splunk audit log

PingAccess can enable and write audit logs for Splunk to effectively collect and analyze data from Java Management Extensions (JMX) *(tooltip: \<div class="paragraph">
\<p>Java technology that provides tools for managing and monitoring applications, devices, system objects, and service-oriented networks.\</p>
\</div>)* MBeans.

You can [enable Splunk audit logs](../configuring_and_customizing_pingaccess/pa_writing_audit_logs_for_splunk.html) and use them to create dashboards in Splunk. These logs record the same information as the default audit logs, but they are formatted to facilitate parsing for specific information when you create dashboards. All of the necessary information resides within the commented-out sections.

|   |                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The link above provides instructions on how to set up the PingAccess for Splunk app, which can be found here: <https://splunkbase.splunk.com/app/5368> |