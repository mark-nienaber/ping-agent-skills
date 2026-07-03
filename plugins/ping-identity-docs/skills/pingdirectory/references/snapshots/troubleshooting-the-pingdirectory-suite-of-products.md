---
title: Common problems and potential solutions
description: This section describes several different types of problems that can occur and common potential causes for them.
component: pingdirectory
version: 11.1
page_id: pingdirectory:troubleshooting_the_pingdirectory_suite_of_products:pd_ds_common_probs_potential_sols
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/troubleshooting_the_pingdirectory_suite_of_products/pd_ds_common_probs_potential_sols.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
---

# Common problems and potential solutions

This section describes several different types of problems that can occur and common potential causes for them.

---

---
title: Conditions for automatic server shutdown
description: All PingDirectory servers will shut down in an out of memory condition, a low disk space error state, or for running out of file descriptors. The server will enter lockdown mode on unrecoverable database environment errors, but can be configured to shutdown instead with this setting:
component: pingdirectory
version: 11.1
page_id: pingdirectory:troubleshooting_the_pingdirectory_suite_of_products:pd_ds_conditions_auto_server_shutdown
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/troubleshooting_the_pingdirectory_suite_of_products/pd_ds_conditions_auto_server_shutdown.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 13, 2024
---

# Conditions for automatic server shutdown

All PingDirectory servers will shut down in an out of memory condition, a low disk space error state, or for running out of file descriptors. The server will enter lockdown mode on unrecoverable database environment errors, but can be configured to shutdown instead with this setting:

```shell
$ dsconfig set-global-configuration-prop \
            --set unrecoverable-database-error-mode:initiate-server-shutdown
```

---

---
title: Conditions for automatic server shutdown
description: All PingDirectory servers will shutdown in an out of memory condition, a low disk space error state, or for running out of file descriptors. The PingDirectory server will enter lockdown mode on unrecoverable database environment errors, but can be configured to shutdown instead with this setting:
component: pingdirectory
version: 11.1
page_id: pingdirectory:troubleshooting_the_pingdirectory_suite_of_products:pd_sync_conditions_auto_server_shutdown
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/troubleshooting_the_pingdirectory_suite_of_products/pd_sync_conditions_auto_server_shutdown.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Conditions for automatic server shutdown

All PingDirectory servers will shutdown in an out of memory condition, a low disk space error state, or for running out of file descriptors. The PingDirectory server will enter lockdown mode on unrecoverable database environment errors, but can be configured to shutdown instead with this setting:

```shell
$ dsconfig set-global-configuration-prop \
  --set unrecoverable-database-error-mode:initiate-server-shutdown
```

---

---
title: Enabling JVM debugging
description: Enable the Java Virtual Machine (JVM) debugging options to track garbage collection data for the system. These options can impact JVM performance, but provide valuable data to tune the server. While the jstat utility with the -gc option can be used to obtain some information about garbage collection activity, there are additional arguments that can be added to provide additional detail, such as:
component: pingdirectory
version: 11.1
page_id: pingdirectory:troubleshooting_the_pingdirectory_suite_of_products:pd_sync_enable_jvm_debugging
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/troubleshooting_the_pingdirectory_suite_of_products/pd_sync_enable_jvm_debugging.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Enabling JVM debugging

## About this task

Enable the Java Virtual Machine (JVM) *(tooltip: \<div class="paragraph">
\<p>A virtual machine that allows a computer to run Java programs and programs that are compiled to Java bytecode.\</p>
\</div>)* debugging options to track garbage collection data for the system. These options can impact JVM performance, but provide valuable data to tune the server. While the `jstat` utility with the `-gc` option can be used to obtain some information about garbage collection activity, there are additional arguments that can be added to provide additional detail, such as:

```
-XX:+PrintGCDetails
-XX:+PrintTenuringDistribution
-XX:+PrintGCApplicationConcurrentTime
-XX:+PrintGCApplicationStoppedTime
-XX:+PrintGCDateStamps
```

## Steps

1. On the server, go to the `config/java.properties` file.

2. Edit the `config/java.properties` file. Add any additional arguments to the end of the line that begins with `start-<server>.java-args`.

3. Save the file.

4. Run the following command for the new arguments to take effect the next time the server is started:

   ```shell
   $ bin/dsjavaproperties
   ```

---

---
title: General troubleshooting methodology
description: When a problem is detected, the following general methodology to isolate the problem are recommended.
component: pingdirectory
version: 11.1
page_id: pingdirectory:troubleshooting_the_pingdirectory_suite_of_products:pd_ds_general_troubleshoot_method
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/troubleshooting_the_pingdirectory_suite_of_products/pd_ds_general_troubleshoot_method.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 13, 2024
---

# General troubleshooting methodology

When a problem is detected, the following general methodology to isolate the problem are recommended.

1. Run the `bin/status` tool or look at the server status in the admin console. The `status` tool provides a summary of the server's current state with key metrics and a list of recent alerts.

2. Look in the server logs. In particular, view the following logs:

   * logs/errors

   * logs/failed-ops

   * logs/expensive-ops

3. Use system commands, such as `vmstat` and `iostat` to determine if the server is bottle-necked on a system resource like CPU or disk throughput.

4. For performance problem (especially intermittent ones like spikes in response time), enabling the `periodic-stats-logger` can help to isolate problems, because it stores important server performance information on a per-second basis. The `periodic-stats-logger` can save the information in a csv-formatted file that can be loaded into a spreadsheet. The information this logger makes available is very configurable. You can create multiple loggers for different types of information or a different frequency of logging (for example, hourly data in addition to per-second data). For more information, see "Profiling Server Performance Using the Periodic Stats Logger".

5. For replication problem, run `dsreplication status` and look at the `logs/replication` file.

6. For more advanced users, run the `collect-support-data` tool on the system, unzip the archive somewhere, and look through the collected information. This is often useful when administrators most familiar with the Data Platform do not have direct access to the systems where the production servers are running. They can examine the `collect-support-data` archive on a different server. For more information, see Using the Collect Support Data Tool.

|   |                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Run the `collect-support-data` tool whenever there is a problem whose cause is not easily identified, so that this information can be passed back to your authorized support provider before corrective action can be taken. |

---

---
title: How to regenerate the server ads-certificate
description: This topic applies only to the PingDirectory server.
component: pingdirectory
version: 11.1
page_id: pingdirectory:troubleshooting_the_pingdirectory_suite_of_products:pd_ds_regen_server_ads_cert
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/troubleshooting_the_pingdirectory_suite_of_products/pd_ds_regen_server_ads_cert.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# How to regenerate the server ads-certificate

|   |                                                      |
| - | ---------------------------------------------------- |
|   | This topic applies only to the PingDirectory server. |

At setup time, the server generates a private key and certificate for use when secure communication between servers is required. This certificate, `ads-certificate`, is stored in `config/ads-truststore` and should typically remain unchanged for the life of the server deployment. If the need arises for a new ads-certificate to be created, say because the server-root has been copied to a new host, then the private key and certificate will be recreated by the startup process if the `config/ads-truststore` and `config/ads-truststore.pin` files are first manually removed while the server is offline. Note that if replication is enabled, the server must have replication disabled before regeneration of the ads-certificate.

For example, the server allows easy copying of its installation, which can then be used to install another server instance. If a server (ldap1.example.com:389) is enabled with its own copy (ldap2.example.com:389), `dsreplication` will exit with the following error message:

```
Replication cannot be enabled between servers ldap1.example.com:389 and ldap2.example.com:389
because they are using the same instance key.
```

The solution is to stop the server, remove `config/adstruststore` and `config/adstruststore.pin` and re-start the server. Upon startup, a new `adstruststore`, containing the server's instance key, will be generated. Then, you can re-run `dsreplication enable` to set up replication between the two servers.

---

---
title: Installation and maintenance issues
description: The following are common installation and maintenance issues and possible solutions.
component: pingdirectory
version: 11.1
page_id: pingdirectory:troubleshooting_the_pingdirectory_suite_of_products:pd_sync_install_maint_issues
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/troubleshooting_the_pingdirectory_suite_of_products/pd_sync_install_maint_issues.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
page_aliases: ["pd_sync_setup_will_not_run.adoc", "pd_sync_server_will_not_start.adoc", "pd_sync_server_has_shutdown.adoc", "pd_sync_server_will_not_accept_client_connections.adoc", "pd_sync_server_unresponsive.adoc", "pd_sync_problems_admin_console.adoc"]
section_ids:
  the-setup-program-will-not-run: The setup program will not run
  a-java-environment-is-not-available: A Java environment is not available
  unexpected-arguments-provided-to-the-jvm: Unexpected arguments provided to the JVM
  the-server-has-already-been-configured-or-started: The server has already been configured or started
  the-server-will-not-start: The server will not start
  the-server-or-other-administrative-tool-is-already-running: The server or other administrative tool is already running
  there-is-not-enough-memory-available: There is not enough memory available
  an-invalid-java-environment-or-jvm-option-was-used: An invalid Java environment or JVM option was used
  an-invalid-command-line-option-was-used: An invalid command-line option was used
  the-server-has-an-invalid-configuration: The server has an invalid configuration
  proper-permissions-are-missing: Proper permissions are missing
  the-server-has-shutdown: The server has shutdown
  the-server-wont-accept-client-connections: The server won't accept client connections
  the-server-is-unresponsive: The server is unresponsive
  problems-with-the-admin-console: Problems with the admin console
---

# Installation and maintenance issues

The following are common installation and maintenance issues and possible solutions.

## The setup program will not run

If the `setup` tool does not run properly, some of the most common reasons include the following.

### A Java environment is not available

The server requires that Java be installed on the system before running the `setup` tool.

If there are multiple instances of Java on the server, run the `setup` tool with an explicitly defined value for the `JAVA_HOME` environment variable that specifies the path to the Java installation. For example:

```shell
$ env JAVA_HOME=/ds/java ./setup
```

Another issue might be that the value specified in the provided `JAVA_HOME` environment variable can be overridden by another environment variable. If that occurs, use the following command to override any other environment variables:

```shell
$ env UNBOUNDID_JAVA_HOME="/ds/java" UNBOUNDID_JAVA_BIN="" ./setup
```

### Unexpected arguments provided to the JVM

If the `setup` tool attempts to launch the java command with an invalid set of arguments, it might prevent the Java Virtual Machine (JVM) *(tooltip: \<div class="paragraph">
\<p>A virtual machine that allows a computer to run Java programs and programs that are compiled to Java bytecode.\</p>
\</div>)* from starting. By default, no special options are provided to the JVM when running `setup`, but this might not be the case if either the `JAVA_ARGS` or `UNBOUNDID_JAVA_ARGS` environment variable is set. If the `setup` tool displays an error message that indicates that the Java environment could not be started with the provided set of arguments, run the following command:

```shell
$ unset JAVA_ARGS UNBOUNDID_JAVA_ARGS
```

### The server has already been configured or started

The `setup` tool is only intended to provide the initial configuration for the server. It will not run if it detects that it has already been run.

A previous installation should be removed before installing a new one. However, if there is nothing of value in the existing installation, the following steps can be used to run the `setup` program:

* Remove the `config/config.ldiffile` and replace it with the `config/update/config.ldif.{revision}` file containing the initial configuration.

* If there are any files or subdirectories in the `db` directory, then remove them.

* If a `config/java.properties` file exists, then remove it.

* If a `lib/setup-java-home` script (or `lib\set-java-home.bat` file on Microsoft Windows) exists, then remove it.

## The server will not start

If the server does not start, then there are several potential causes.

### The server or other administrative tool is already running

Only a single instance of the server can run at any time from the same installation root. Other administrative operations can prevent the server from being started. In such cases, the attempt to start the server should fail with a message like:

```
The <server> could not acquire an exclusive lock on file
/ds/PingData<server>/locks/server.lock:
The exclusive lock requested for file
/ds/PingData<server>/locks/ server.lock
was not granted, which indicates that another
process already holds a shared or exclusive lock on
that file. This generally means that another instance
of this server is already running.
```

If the server is not running (and is not in the process of starting up or shutting down), and there are no other tools running that could prevent the server from being started, it is possible that a previously held lock was not properly released. Try removing all of the files in the locks directory before attempting to start the server.

### There is not enough memory available

When the server is started, the JVM *(tooltip: \<div class="paragraph">
\<p>A virtual machine that allows a computer to run Java programs and programs that are compiled to Java bytecode.\</p>
\</div>)* attempts to allocate all memory that it has been configured to use. If there is not enough free memory available on the system, the server generates an error message indicating that it could not be started.

There are several potential causes for this:

* If the amount of memory in the underlying system has changed, the server might need to be re-configured to use a smaller amount of memory.

* Another process on the system is consuming memory and there is not enough memory to start the server. Either terminate the other process, or reconfigure the server to use a smaller amount of memory.

* The server just shut down and an attempt was made to immediately restart it. If the server is configured to use a significant amount of memory, it can take a few seconds for all of the memory to be released back to the operating system. Run the `vmstat` Installation and maintenance issues command and wait until the amount of free memory stops growing before restarting the server.

* If the system is configured with one or more memory-backed file systems (such as `/tmp`), determine if any large files are consuming a significant amount of memory. If so, remove them or relocate them to a disk-based file system.

### An invalid Java environment or JVM option was used

If an attempt to start the server fails with 'no valid Java environment could be found,' or 'the Java environment could not be started,' and memory is not the cause, other causes can include the following:

* The Java installation that was previously used to run the server no longer exists. Update the `config/java.properties` file to reference the new Java installation and run the `bin/dsjavaproperties` command to apply that change.

* The Java installation has been updated, and one or more of the options that had worked with the previous Java version no longer work. Re-configure the server to use the previous Java version, and investigate which options should be used with the new installation.

* If an `UNBOUNDID_JAVA_HOME` or `UNBOUNDID_JAVA_BIN` environment variable is set, its value might override the path to the Java installation used to run the server (defined in the `config/java.properties` file). Similarly, if an `UNBOUNDID_JAVA_ARGS` environment variable is set, then its value might override the arguments provided to the JVM. If this is the case, explicitly unset the `UNBOUNDID_JAVA_HOME`, `UNBOUNDID_JAVA_BIN`, and `UNBOUNDID_JAVA_ARGS`environment variables before starting the server.

Any time the `config/java.properties` file is updated, the `bin/dsjavaproperties` tool must be run to apply the new configuration. If a problem with the previous Java configuration prevents the `bin/dsjavaproperties` tool from running properly, remove the `lib/set-java-home` script (or`lib\set-java-home.bat` file on Microsoft Windows) and invoke the `bin/dsjavaproperties` tool with an explicitly-defined path to the Java environment, such as:

```shell
$ env UNBOUNDID_JAVA_HOME=/ds/java bin/dsjavaproperties
```

### An invalid command-line option was used

There are a small number of arguments that can be provided when running the `bin/start-server` command. If arguments were provided and are not valid, the server displays an error message. Correct or remove the invalid argument and try to start the server again.

### The server has an invalid configuration

If a change is made to the server configuration using `dsconfig` or the admin console, the server will validate the change before applying it. However, it is possible that a configuration change can appear to be valid, but does not work as expected when the server is restarted.

In most cases, the server displays (and writes to the error log) a message that explains the problem. If the message does not provide enough information to identify the problem, the `logs/config-audit.logfile` provides recent configuration changes, or the `config/archived-configs` directory contains configuration changes not made through a supported configuration interface. The server can be started with the last valid configuration using the `-- useLastKnownGoodConfig` option:

```shell
$ bin/start-server --useLastKnownGoodConfig
```

To determine the set of configuration changes made to the server since the installation, use the `config-difftool` with the arguments `--sourceLocal --targetLocal --sourceBaseline`. The `dsconfig --offline` command can be used to make configuration changes.

### Proper permissions are missing

The server should only be started by the user or role used to initially install the server. However, if the server was initially installed as a non-root user and then started by the root account, the server can no longer be started as a non-root user. Any new files that are created are owned by root.

If the user account used to run the server needs to change, change ownership of all files in the installation to that new user. For example, if the server should be run as the "ds" user in the "other" group, run the following command as root:

```shell
$ chown -R ds:other /ds/PingData<server>
```

## The server has shutdown

Check the current server state by using the `bin/server-state` command. If the server was previously running but is no longer active, potential reasons can include:

* Shut down by an administrator – Unless the server was forcefully terminated, then messages are written to the error and server logs stating the reason.

* Shut down when the underlying system crashed or was rebooted – Run the `uptime` command on the underlying system to determine what was recently started or stopped.

* Process terminated by the underlying operating system – If this happens, a message is written to the system error log.

* Shut down in response to a serious problem – This can occur if the server has detected that the amount of usable disk space is critically low, or if errors have been encountered during processing that left the server without worker threads. Messages are written to the error and server logs (if disk space is available).

* JVM *(tooltip: \<div class="paragraph">
  \<p>A virtual machine that allows a computer to run Java programs and programs that are compiled to Java bytecode.\</p>
  \</div>)* has crashed – If this happens, then the JVM should provide a fatal error log (a `hs_err_pid<processID>.log` file), and potentially a core file.

## The server won't accept client connections

Check the current server state by using the `bin/server-state` command. If the server doesn't appear to be accepting connections from clients, reasons can include the following:

* The server isn't running.

* The underlying system on which the server is installed isn't running.

* The server is running, but isn't reachable as a result of a network or firewall configuration problem. If that is the case, connection attempts should time out rather than be rejected.

* If the server is configured to allow secure communication through Secure Sockets Layer (SSL) *(tooltip: \<div class="paragraph">
  \<p>A protocol for authenticated and encrypted links between networked machines, typically over HTTPS. SSL was deprecated in 1999 in favor of Transport Layer Security (TLS).\</p>
  \</div>)* or StartTLS, a problem with the key manager or trust manager configuration can cause connection rejections. Messages are written to the server access log for each failed connection attempt.

* The server might have reached its maximum number of allowed connections. Messages should be written to the server access log for each rejected connection attempt.

* If the server is configured to restrict access based on the address of the client, messages should be written to the server access log for each rejected connection attempt.

* If a connection handler encounters a significant error, it can stop listening for new requests. A message should be written to the server error log with information about the problem. Restarting the server can also solve the issue. A third option is to restart the connection handler using the LDIF connection handler to make it available again. To do this, create an LDIF file that disables and then re-enables the connection handler, create the `config/auto-process-ldif` directory if it doesn't already exist, and then copy the LDIF file into it.

## The server is unresponsive

Check the current server state by using the `bin/server-state` command. If the server process is running and appears to be accepting connections but does not respond to requests received on those connections, potential reasons for this include:

* If all worker threads are busy processing other client requests, new requests are forced to wait until a worker thread becomes available. A stack trace can be obtained using the `jstack` command to show the state of the worker threads and the waiting requests.

  If all worker threads are processing the same requests for a long time, the server sends an alert that it might be deadlocked. All threads might be tied up processing unindexed searches.

* If a request handler is busy with a client connection, other requests sent through that request handler are forced to wait until it is able to read data. If there is only one request handler, all connections are impacted. Stack traces obtained using the `jstack` command will show that a request handler thread is continuously blocked.

* If the JVM *(tooltip: \<div class="paragraph">
  \<p>A virtual machine that allows a computer to run Java programs and programs that are compiled to Java bytecode.\</p>
  \</div>)* in which the server is running is not properly configured, it can spend too much time performing garbage collection. The effect on the server is similar to that of a network or firewall configuration problem. A stack trace obtained with the `pstack` utility will show that most threads are idle except the one performing garbage collection. It is also likely that a small number of CPUs is 100% busy while all other CPUs are idle. The server will also issue an alert after detecting a long JVM pause that will include details.

* If the JVM in which the server is running has hung, the `pstack` utility should show that one or more threads are blocked and unable to make progress. In such cases, the system CPUs should be mostly idle.

* If a there is a network or firewall configuration problem, communication attempts with the server will fail. A network sniffer will show that packets sent to the system are not receiving TCP acknowledgment.

* If the host system is hung or lost power with a graceful shutdown, the server will be unresponsive.

## Problems with the admin console

If a problem occurs when trying to use the admin console, reasons might include one of the following:

* The web application container that hosts the console is not running. If an error occurs while trying to start it, consult the logs for the web application container.

* If a problem occurs while trying to authenticate, make sure that the target server is online. If it is, the access log might provide information about the authentication failure.

* If a problem occurs while interacting with the server instance using the admin console, the access and error logs for that instance might provide additional information.

---

---
title: Insufficient memory errors
description: If the server shuts down because of insufficient memory errors, it is possible that the allocated heap size is not enough for the amount of data being returned. Consider increasing the heap size, or reducing the number of request handler threads using the following dsconfig command:
component: pingdirectory
version: 11.1
page_id: pingdirectory:troubleshooting_the_pingdirectory_suite_of_products:pd_sync_insufficient_memory_errors
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/troubleshooting_the_pingdirectory_suite_of_products/pd_sync_insufficient_memory_errors.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Insufficient memory errors

If the server shuts down because of insufficient memory errors, it is possible that the allocated heap size is not enough for the amount of data being returned. Consider increasing the heap size, or reducing the number of request handler threads using the following `dsconfig` command:

```shell
$ bin/dsconfig set-connection-handler-prop \
         --handler-name "HTTP Connection Handler" \
         --set num-request-handlers:<num-of-threads>
```

---

---
title: Java diagnostic information
description: In addition to the tools listed in the previous section, the JVM can provide additional diagnostic information in response to certain events.
component: pingdirectory
version: 11.1
page_id: pingdirectory:troubleshooting_the_pingdirectory_suite_of_products:pd_ds_java_diagnostic_info
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/troubleshooting_the_pingdirectory_suite_of_products/pd_ds_java_diagnostic_info.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
page_aliases: ["pd_ds_jvm_crash_diagnostics_info.adoc", "pd_proxy_garbage_collection_diag_info.adoc"]
section_ids:
  jvm-crash-diagnostic-information: JVM crash diagnostic information
  garbage-collection-diagnostic-information: Garbage collection diagnostic information
---

# Java diagnostic information

In addition to the tools listed in the previous section, the JVM can provide additional diagnostic information in response to certain events.

## JVM crash diagnostic information

If the JVM itself should happen to crash for some reason, then it generates a fatal error log with information about the state of the JVM at the time of the crash. By default, this file is named `hs_err_pid{processID}.log` and is written into the base directory of the PingDirectory server installation. This file includes information on the underlying cause of the JVM crash, information about the threads running and Java heap at the time of the crash, the options provided to the JVM, environment variables that were set, and information about the underlying system.

## Garbage collection diagnostic information

|   |                                                           |
| - | --------------------------------------------------------- |
|   | This topic applies only to the PingDirectoryProxy server. |

You can enable the JVM debugging options to track garbage collection data for your system. The options can impact JVM performance, but they provide valuable data to tune your server when troubleshooting garbage collection issues. While the `jstat` utility with the `-gc` option can be used to obtain some information about garbage collection activity, there are additional arguments that can be added to the JVM to use when running the server to provide additional detail.

```
-XX:+PrintGCDetails
-XX:+PrintTenuringDistribution
-XX:+PrintGCApplicationConcurrentTime
-XX:+PrintGCApplicationStoppedTime
-XX:+PrintGCDateStamps
```

To run the server with these options, edit the `config/java.properties` file and add them to the end of the line that begins with "`bin/start-server.java-args`". After the file has been saved, invoke the following command to make those new arguments take effect the next time the server is started:

```shell
$ bin/dsjavaproperties
```

---

---
title: Java troubleshooting tools
description: The Java Development Kit provides several very useful tools to obtain information about Java applications and diagnosing problems. These tools are not included with the Java Runtime Environment (JRE), so the full Java Development Environment (JDK) should always be installed and used to run the Server.
component: pingdirectory
version: 11.1
page_id: pingdirectory:troubleshooting_the_pingdirectory_suite_of_products:pd_ds_java_troubleshoot_tools
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/troubleshooting_the_pingdirectory_suite_of_products/pd_ds_java_troubleshoot_tools.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 2, 2024
page_aliases: ["pd_ds_jps.adoc", "pd_ds_jstack.adoc", "pd_ds_jmap.adoc", "pd_ds_jhat.adoc", "pd_ds_jstat.adoc"]
section_ids:
  jps: jps
  jstack: jstack
  jmap: jmap
  jhat: jhat
  jstat: jstat
---

# Java troubleshooting tools

The Java Development Kit provides several very useful tools to obtain information about Java applications and diagnosing problems. These tools are not included with the Java Runtime Environment (JRE), so the full Java Development Environment (JDK) should always be installed and used to run the Server.

## jps

The `jps` tool is a Java-specific version of the UNIX `ps` tool. It can be used to obtain a list of all Java processes currently running and their respective process identifiers. When invoked by a non-root user, it will list only Java processes running as that user. When invoked by a root user, then it lists all Java processes on the system.

This tool can be used to see if the PingDirectory server is running and if a process ID has been assigned to it. This process ID can be used in conjunction with other tools to perform further analysis.

This tool can be run without any arguments, but some of the more useful arguments that include:

* `-v`: Includes the arguments passed to the JVM for the processes that are listed.

* `-m`: Includes the arguments passed to the main method for the processes that are listed.

* `-l` (lowercase L): Include the fully qualified name for the main class rather than only the base class name.

## jstack

The `jstack` tool is used to obtain a stack trace of a running Java process, or optionally from a core file generated if the JVM happens to crash. A stack trace can be extremely valuable when trying to debug a problem, because it provides information about all threads running and exactly what each is doing at the point in time that the stack trace was obtained.

Stack traces are helpful when diagnosing problems in which the server appears to be hung or behaving slowly. Java stack traces are generally more helpful than native stack traces, because Java threads can have user-friendly names (as do the threads used by the Server), and the frame of the stack trace can include the line number of the source file to which it corresponds. This is useful when diagnosing problems and often allows them to be identified and resolved quickly.

To obtain a stack trace from a running JVM, use the command:

```
jstack {processID}
```

where {processID} is the process ID of the target JVM as returned by the `jps` command. To obtain a stack trace from a core file from a Java process, use the command:

```
jstack {pathToJava} {pathToCore}
```

where `{pathToJava}` is the path to the java command from which the core file was created, and `{pathToCore}` is the path to the core file to examine. In either case, the stack trace is written to standard output and includes the names and call stacks for each of the threads that were active in the JVM.

In many cases, no additional options are necessary. The "`-l`" option can be added to obtain a long listing, which includes additional information about locks owned by the threads. The "`-m`" option can be used to include native frames in the stack trace.

## jmap

The `jmap` tool is used to obtain information about the memory consumed by the JVM. It is very similar to the native `pmap` tool provided by many operating systems. As with the `jstack` tool, `jmap` can be invoked against a running Java process by providing the process ID, or against a core file , like:

```
jmap {processID}
jmap {pathToJava} {pathToCore}
```

Some of the additional arguments include:

* `-dump:live,format=b,file=filename`: Dump the live heap data to a file that can be examined by the `jhat` tool

* `-heap`: Provides a summary of the memory used in the Java heap, along with information about the garbage collection algorithm in use.

* `-histo:live`: Provides a count of the number of objects of each type contained in the heap. If the "`:live`" portion is included, then only live objects are included; otherwise, the count include objects that are no longer in use and are garbage collected.

## jhat

The `jhat` (Java Heap Analysis Tool) utility provides the ability to analyze the contents of the Java heap. It can be used to analyze a heap dump file, which is generated if the PingDirectory server encounters an out of memory error (as a result of the "`-XX:+HeapDumpOnOutOfMemoryError`" JVM option) or from the use of the `jmap` command with the "`-dump`" option.

The `jhat` tool acts as a web server that can be accessed by a browser in order to query the contents of the heap. Several predefined queries are available to help determine the types of objects consuming significant amounts of heap space, and it also provides a custom query language (OQL, the Object Query Language) for performing more advanced types of analysis.

The `jhat` tool can be launched with the path to the heap dump file, like:

```
jhat /path/to/heap.dump
```

This command causes the `jhat` web server to begin listening on port 7000. It can be accessed in a browser at `http://localhost:7000` (or `http://address:7000` from a remote system). An alternate port number can be specified using the "`-port`" option, like:

```
jhat -port 1234 /path/to/heap.dump
```

To issue custom OQL searches, access the web interface using the URL `http://localhost:7000/oql/` (the trailing slash must be provided). Additional information about the OQL syntax can be obtained in the web interface at `http://localhost:7000/oqlhelp/`.

## jstat

The `jstat` tool is used to obtain a variety of statistical information from the JVM, much like the `vmstat` utility that can be used to obtain CPU utilization information from the operating system. The general manner to invoke it is as follows:

```
jstat {type} {processID} {interval}
```

The `{interval}` option specifies the length of time in milliseconds between lines of output. The `{processID}` option specifies the process ID of the JVM used to run the PingDirectory server, which can be obtained by running `jps` as mentioned previously. The `{type}` option specifies the type of output that should be provided. Some of the most useful types include:

* `-class`: Provides information about class loading and unloading.

* `-compile`: Provides information about the activity of the JIT complex.

* `-printcompilation`: Provides information about JIT method compilation.

* `-gc`: Provides information about the activity of the garbage collector.

* `-gccapacity`: Provides information about memory region capacities.

---

---
title: Management tools
description: Each PingDirectory server provides command-line tools to manage, monitor, and diagnose server operations. Each tool provides a description of the subcommands, arguments, and usage examples needed to run the tool.
component: pingdirectory
version: 11.1
page_id: pingdirectory:troubleshooting_the_pingdirectory_suite_of_products:pd_sync_management_tools
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/troubleshooting_the_pingdirectory_suite_of_products/pd_sync_management_tools.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Management tools

Each PingDirectory server provides command-line tools to manage, monitor, and diagnose server operations. Each tool provides a description of the subcommands, arguments, and usage examples needed to run the tool.

|   |                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For detailed information and examples of the command-line tools, see the Configuration Reference Guide in the `<server-root>/docs` directory, or linked from the admin console. |

To view detailed argument options and examples, use `--help` with the each tool:

```shell
$ bin/dsconfig --help
```

For those utilities that support additional subcommands (such as `dsconfig`), list the subcommands with the following:

```shell
$ bin/dsconfig --help-subcommands
```

View more detailed subcommand information by using `--help` with the specific subcommand:

```shell
$ bin/dsconfig list-log-publishers --help
```

---

---
title: Monitor entries
description: This topic applies only to the PingDirectory server.
component: pingdirectory
version: 11.1
page_id: pingdirectory:troubleshooting_the_pingdirectory_suite_of_products:pd_ds_monitor_entries
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/troubleshooting_the_pingdirectory_suite_of_products/pd_ds_monitor_entries.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 4, 2024
---

# Monitor entries

|   |                                                      |
| - | ---------------------------------------------------- |
|   | This topic applies only to the PingDirectory server. |

While the server is running, it generates a significant amount of information available through monitor entries. Monitor entries are available over LDAP in the `cn=monitor` subtree. The types of monitor entries that are available include:

* **General Monitor Entry (cn=monitor)** – Provides a basic set of general information about the server.

* **Active Operations Monitor Entry (cn=Active Operations,cn=monitor)** – Provides information about all operations currently in progress in the server.

* **Backend Monitor Entries (cn={id} Backend,cn=monitor)** – Provides information about the backend, including the number of entries, the base DN(s), and whether it is private.

* **Client Connections Monitor Entry (cn=Client Connections,cn=monitor)** – Provides information about all connections currently established to the server.

* **Connection Handler Monitor Entry (cn={name},cn=monitor)** – Provides information about the configuration of each connection handler and the client connections established to it.

* **Database Environment Monitor Entries (cn={id} Database Environment,cn=monitor)** – Provides statistics and other data from the Oracle Berkeley DB Java Edition database environment used by the associated backend.

* **Disk Space Usage Monitor Entry (cn=Disk Space Usage,cn=monitor)** – Provides information about the amount of usable disk space available to server components.

* **JVM Memory Usage Monitor Entry (cn=JVM Memory Usage,cn=monitor)** – Provides information about garbage collection activity, the amount of memory available to the server, and the amount of memory consumed by various server components.

* **JVM Stack Trace Monitor Entry (cn=JVM Stack Trace,cn=monitor)** – Provides a stack trace of all threads in the JVM.

* **LDAP Statistics Monitor Entries (cn={name} Statistics,cn=monitor)** – Provides information about the number of each type of operation requested and bytes transferred over the connection handler.

* **Processing Time Histogram Monitor Entry (cn=Processing Time Histogram,cn=monitor)** – Provides information about the number of percent of operations that completed in various response time categories.

* **SSL Context Monitor Entry (cn=SSL Context,cn=monitor)** – Provides information about the available and supported SSL Cipher Suites and Protocols on the server.

* **System Information Monitor Entry (cn=System Information,cn=monitor)** – Provides information about the underlying JVM and system.

* **Version Monitor Entry (cn=Version,cn=monitor)** – Provides information about the server version.

* **Work Queue Monitor Entry (cn=Work Queue,cn=monitor)** – Provides information about the state of the server's work queue, including the number of operations waiting on worker threads and the number of operations that have been rejected because the queue became full.

---

---
title: PingDataSync gauges
description: The PingDataSync server provides several built-in gauges to monitor PingDataSync performance. These gauges are listed in the following table:
component: pingdirectory
version: 11.1
page_id: pingdirectory:troubleshooting_the_pingdirectory_suite_of_products:pd_sync_pds_gauges
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/troubleshooting_the_pingdirectory_suite_of_products/pd_sync_pds_gauges.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# PingDataSync gauges

The PingDataSync server provides several built-in gauges to monitor PingDataSync performance. These gauges are listed in the following table:

**Directory Server Gauges**

| Gauge Name                      | Enabled by default? | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Available File Descriptors      | true                | Monitors the number of file descriptors available to the server process. The server allows for an unlimited number of connections by default, but is restricted by the file descriptor limit on the operating system. The number of file descriptors that the server will use can be configured by either using a `NUM_FILE_DESCRIPTORS` environment variable, or by creating a `config/num-file-descriptors` file with a single line such as `NUM_FILE_DESCRIPTORS=12345`. If these are not set, the default of 65535 is used. Running out of available file descriptors can lead to unpredictable behavior and severe system instability.                                                                                                                                                                                                                                                                                                                                                                               |
| Certificate Expiration (Days)   | true                | Monitors the expiration dates of key server certificates. A server certificate expiring can cause server unavailability, degradation, or loss of key server functionality. Certificates nearing the end of their validity should be replaced as soon as possible. See the status tool, or **Status** in the admin console, for more information about server certificates and how they are managed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| CPU Usage (Percent)             | true                | Monitors server CPU use and provides an averaged percentage for the interval defined. The monitored resource is the host system's CPU, which does not include a resource identifier. If CPU use is high, check the server's current workload and other processes on this system and make any needed adjustments. Reducing the load on the system will lead to better response times.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Destination Unavailable Seconds | true                | Gauge that raises an alarm if the Sync Destination is not available.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Disk Busy (Percent)             | true                | Monitors the percentage of disk use time averaged over the specified update interval. This gauge requires that the Host System Monitor Provider be enabled and that any monitored disks be registered using the disk-devices property of that configuration object. The resource identifier for this gauge is the disk device name. Use the `iostat` command or a similar system utility to see a list of disk device names. A separate gauge monitor entry will be created for each monitored disk.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| HTTP Processing (Percent)       | true                | Monitors the percentage of time that request handler threads spend processing HTTP requests. This percentage represents the inverse of the server's ability to handle new requests without queuing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| JVM Memory Usage (Percent)      | true                | Monitors the percentage of Java Virtual Machine (JVM) *(tooltip: \<div class="paragraph">&#xA;\<p>A virtual machine that allows a computer to run Java programs and programs that are compiled to Java bytecode.\</p>&#xA;\</div>)* memory that is in use. This value naturally fluctuates because of garbage collection, so the minimum value within an interval is reported since it is a better indication of overall memory growth. When the memory usage exceeds 90%, this should be reported to customer support since the server is either misconfigured or has a memory leak. As memory usage approaches 100%, the server is more and more likely to experience garbage collection pauses, which leave the server unresponsive for a long time. Restarting the server is likely the only remedy for this situation. Before restarting the server, run `collect-support-data` and capture the output of 'jmap -histo ' to provide to customer support. The pid of the server can be found from `/logs/server.pid`. |
| License Expiration (Days)       | true                | Monitors the expiration date of the product license. An expired license will cause warnings to appear in the server's logs and in the status tool output. Request a license key through the Ping Identity licensing website <https://www.pingidentity.com/en/account/request-license-key.html> or contact <sales@pingidentity.com>. Use the dsconfig tool to update the License configuration's license key property.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Memory Usage (Percent)          | false               | Monitors the percentage of memory use averaged over the update interval defined. The monitored resource is the host system's memory use, which does not have a resource identifier. Some operating systems, including Linux, use the majority of memory for file system cache, which is freed as applications need it. If memory use is high, check the applications that are running on the server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Strong Encryption Not Available | true                | The JVM does not appear to support strong encryption algorithms, like 256-bit AES. The server will fall back to using weaker algorithms, like 128-bit AES. To enable support for strong encryption, update your JVM to a newer version that supports it by default, or install or enable the unlimited encryption strength jurisdiction policy files in your Java installation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

---

---
title: PingDataSync log files
description: The following log files are specific to PingDataSync, and contain details about the synchronization processes:
component: pingdirectory
version: 11.1
page_id: pingdirectory:troubleshooting_the_pingdirectory_suite_of_products:pd_sync_synchronize_troubleshooting
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/troubleshooting_the_pingdirectory_suite_of_products/pd_sync_synchronize_troubleshooting.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# PingDataSync log files

The following log files are specific to PingDataSync, and contain details about the synchronization processes:

* Sync Log

  Provides information about the synchronization operations that occur within the server. Specifically, the Sync Log records all changes applied, detected or failed; dropped operations that were not synchronized; changes dropped because of being out of scope, or no changes needed for synchronization. The log also shows the entries that were involved in the synchronization process.

* Sync Failed Operations Log

  Provides a list of synchronization operations that have failed.

* Resync Log

  Provides summaries or details of synchronized entries and any missing entries in the Sync Destination.

* Resync Error Log

  Provides error information for `resync` operations.

---

---
title: PingDirectory server troubleshooting information
description: This topic applies only to the PingDirectory server.
component: pingdirectory
version: 11.1
page_id: pingdirectory:troubleshooting_the_pingdirectory_suite_of_products:pd_ds_dir_server_troubleshoot_info
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/troubleshooting_the_pingdirectory_suite_of_products/pd_ds_dir_server_troubleshoot_info.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
page_aliases: ["pd_ds_error_logs.adoc", "pd_ds_server_out_log.adoc", "pd_ds_debug_log.adoc", "pd_ds_replication_repair_log.adoc", "pd_ds_config_audit_log_config_archive.adoc", "pd_ds_access_audit_log.adoc", "pd_ds_setup_log.adoc", "pd_ds_tool_log.adoc", "pd_ds_je_info_je_config_files.adoc", "pd_ds_ldap_sdk_log.adoc"]
section_ids:
  error-log: Error log
  server-out-log: server.out log
  debug-log: Debug log
  replication-repair-log: Replication repair log
  config-audit-log-and-the-configuration-archive: Config audit log and the configuration archive
  access-and-audit-log: Access and audit log
  setup-log: Setup log
  tool-log: Tool log
  je-info-and-je-config-files: je.info and je.config files
  ldap-sdk-debug-log: LDAP SDK debug log
---

# PingDirectory server troubleshooting information

|   |                                                      |
| - | ---------------------------------------------------- |
|   | This topic applies only to the PingDirectory server. |

The PingDirectory server has a comprehensive default set of log files and monitor entries that are useful when troubleshooting a particular server problem.

## Error log

By default, this log file is available at `logs/errors` below the server install root, and it provides information about warnings, errors, and other significant events that occur within the server. Several messages are written to this file on startup and shutdown, but while the server is running, there is normally little information written to it. However, if a problem occurs, the server writes information about that problem to this file.

The following is an example of a message that might be written to the error log:

```
[11/Apr/2011:10:31:53.783 -0500] category=CORE severity=NOTICE msgID=458887 msg="The Directory Server has started successfully"
```

The category field provides information about the area of the server from which the message was generated. Available categories include: ACCESS\_CONTROL, ADMIN, ADMIN\_TOOL, BACKEND, CONFIG, CORE, DSCONFIG, EXTENSIONS, PROTOCOL, SCHEMA, JEB, SYNC, LOG, PLUGIN, PROXY, QUICKSETUP, REPLICATION, RUNTIME\_INFORMATION, TASK, THIRD\_PARTY, TOOLS, USER\_DEFINED, UTIL, and VERSION.

The severity field provides information about how severe the server considers the problem to be. Available severities include:

* `DEBUG`: Used for messages that provide verbose debugging information and do not indicate any kind of problem. Note that this severity level is rarely used for error logging, because the server provides a separate debug logging facility.

* `INFORMATION`: Used for informational messages that can be useful from time to time but aren't normally something that administrators need to see.

* `MILD_WARNING`: Used for problems that the server detects, which can indicate something unusual occurred, but the warning doesn't prevent the server from completing the task it was working on. These warnings aren't normally something that should be of concern to administrators.

* `MILD_ERROR`: Used for problems detected by the server that prevented it from completing some processing normally but that aren't considered to be a significant problem requiring administrative action.

* `NOTICE`: Used for information messages about significant events that occur within the server and are considered important enough to warrant making available to administrators under normal conditions.

* `SEVERE_WARNING`: Used for problems that the server detects that might lead to bigger problems in the future and should be addressed by administrators.

* `SEVERE_ERROR`: Used for significant problems that have prevented the server from successfully completing processing and are considered important.

* `FATAL_ERROR`: Used for critical problems that might leave the server unable to continue processing operations normally.

The messages written to the error log can be filtered based on their severities. The error log publisher has a `default-severity` property, which can be used to specify the severity of messages logged regardless of their category. By default, this includes the NOTICE, SEVERE\_WARNING, SEVERE\_ERROR, and FATAL\_ERROR severities.

You can override these severities on a per-category basis using the `override-severity` property. If this property is used, then each value should consist of a category name followed by an equal sign and a comma-delimited set of severities that should be logged for messages in that category. For example, the following override severity would enable logging at all severity levels in the PROTOCOL category:

```
protocol=debug,information,mild-warning,mild-error,notice,severe-warning,severe-error,fatal-error
```

For the purposes of this configuration property, any underscores in category or severity names should be replaced with dashes. Also, severities aren't inherently hierarchical, so enabling the DEBUG severity for a category won't automatically enable logging at the INFORMATION, MILD\_WARNING, or MILD\_ERROR severities.

The error log configuration can be altered on the fly using tools like `dsconfig`, the admin console, or the LDIF connection handler, and changes will take effect immediately. You can configure multiple error logs that are active in the server at the same time, writing to different log files with different configurations. For example, a new error logger can be activated with a different set of default severities to debug a short-term problem, and then that logger can be removed after the problem is resolved so that the normal error log doesn't contain any of the more verbose information.

## server.out log

The `server.out` file holds any information written to standard output or standard error while the server is running. Normally, it includes several messages written at startup and shutdown, as well as information about any administrative alerts generated while the server is running. In most cases, this information is also written to the error log. The `server.out` file can also contain output generated by the JVM. For example, if garbage collection debugging is enabled, or if a stack trace is requested via "kill -QUIT" as described in a later section, then output is written to this file.

## Debug log

The debug log provides a means of obtaining information that can be used for troubleshooting problems but is not necessary or desirable to have available while the server is functioning normally. As a result, the debug log is disabled by default, but it can be enabled and configured at any time.

Some of the most notable configuration properties for the debug log publisher include:

* `enabled`: Indicates whether debug logging is enabled. By default, it is disabled.

* `log-file`: Specifies the path to the file to be written. By default, debug messages are written to the `logs/debug` file.

* `default-debug-level`: Specifies the minimum log level for debug messages that should be written. The default value is "error," which only provides information about errors that occur during processing (for example, exception stack traces). Other supported debug levels include warning, info, and verbose. Unlike error log severities, the debug log levels are hierarchical. Configuring a specified debug level enables any debugging at any higher levels. For example, configuring the info debug level automatically enables the warning and error levels.

* `default-debug-category`: Specifies the categories for debug messages that should be written. Some of the most useful categories include caught (provides information and stack traces for any exceptions caught during processing), database-access (provides information about operations performed in the underlying database), protocol (provides information about ASN.1 and LDAP communication performed by the server), and data (provides information about raw data read from or written to clients).

As with the error and access logs, multiple debug loggers can be active in the server at any time with different configurations and log files to help isolate information that might be relevant to a particular problem.

|   |                                                                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Enabling one or more debug loggers can have a significant impact on server performance. We recommend that debug loggers be enabled only when necessary, and then be scoped so that only pertinent debug information is recorded. |

Debug targets can be used to further pare down the set of messages generated. For example, you can specify that the debug logs be generated only within a specific class or package. If you need to enable the debug logger, you should work with your authorized support provider to best configure the debug target and interpret the output.

## Replication repair log

The replication repair log is written to `logs/replication` by default and records information about processing performed by the replication repair service. This log is used to resolve replication conflicts that can arise. For example, if the same entry is modified at the same time on two different systems, or if an attempt is made to create entries with the same DN at the same time on two different systems, the PingDirectory server records these events.

## Config audit log and the configuration archive

The configuration audit log provides a record of any changes made to the server configuration while the server is online. This information is written to the `logs/config-audit.log` file and provides information about the configuration change in the form that can be used to perform the operation in a non-interactive manner with the `dsconfig` command. Other information written for each change includes:

* Time the configuration change was made.

* Connection ID and operation ID for the corresponding change, which can be used to correlate it with information in the access log.

* DN of the user requesting the configuration change and the method by which that user authenticated to the server.

* Source and destination addresses of the client connection.

* Command that can be used to undo the change and revert to the previous configuration for the associated configuration object.

In addition to information about the individual changes that are made to the configuration, the server maintains complete copies of all previous configurations. These configurations are provided in the `config/archived-configs` directory and are gzip-compressed copies of the `config/config.ldif` file in use before the configuration change was made. The file names contain timestamps that indicate when that configuration was first used.

## Access and audit log

The access log provides information about operations processed within the server. The default access log file is written to `logs/access`, but multiple access loggers can be active at the same time, each writing to different log files and using different configurations.

By default, a single access log message is generated, which combines the elements of request, forward, and result messages. If an error is encountered while attempting to process the request, then one or more forward-failed messages can also be generated.

```
[01/Jun/2011:11:10:19.692 -0500] CONNECT conn=49 from="127.0.0.1" to="127.0.0.1"
  protocol="LDAP+TLS" clientConnectionPolicy="default"
[01/Jun/2011:11:10:19.764 -0500] BIND RESULT conn=49 op=0 msgID=1 version="3"
  dn="cn=Directory Manager" authType="SIMPLE" resultCode=0 etime=0.401
  authDN="cn=Directory Manager,cn=Root DNs,cn=config" clientConnectionPolicy="default"
[01/Jun/2011:11:10:19.769 -0500] SEARCH RESULT conn=49 op=1 msgID=2
  base="ou=People,dc=example,dc=com" scope=2 filter="(uid=1)" attrs="ALL"
  resultCode=0 etime=0.549 entriesReturned=1
[01/Jun/2011:11:10:19.788 -0500] DISCONNECT conn=49 reason="Client Unbind"
```

Each log message includes a timestamp indicating when it was written, followed by the operation type, the connection ID (which is used for all operations processed on the same client connection), the operation ID (which can be used to correlate the request and response log messages for the operation), and the message ID used in LDAP messages for this operation.

The remaining content for access log messages varies based on the type of operation being processed, and whether it is a request or a result message. Request messages generally include the most pertinent information from the request, but generally omit information that is sensitive or not useful.

Result messages include a `resultCode` element that indicates whether the operation was successful or if failed and an `etime` element that indicates the length of time in milliseconds that the server spent processing the operation. Other elements that might be present include the following:

* `origin=replication`: Operation that was processed as a result of data synchronization (for example, replication) rather than a request received directly from a client.

* `message`: Text that was included in the `diagnosticMessage` field of the response sent to the client.

* `additionalInfo`: Additional information about the operation that was not included in the response sent back to the client.

* `authDN – DN` of the user that authenticated to the server (typically only included in bind result messages).

* `authzDN – DN` of an alternate authorization identify used when processing the operation (for example, if the proxied authorization control was included in the request).

* `authFailureID`: Unique identifier associated with the authentication failure reason (only included in non-successful bind result messages).

* `authFailureReason`: Information about the reason that a bind operation failed that might be useful to administrators but was not included in the response to the client for security reasons.

* `responseOID`: OID included in an extended response returned to the client.

* `entriesReturned`: Number of matching entries returned to the client for a search operation.

* `unindexed=true`: Indicates that the associated search operation could not be sufficiently processed using server indexes and a significant traversal through the database was required.

Note that this is not an exhaustive list, and elements that are not listed here can also be present in access log messages. The LDAP SDK for Java provides an API for parsing access log messages and provides access to all elements that they can contain.

The server provides a second access log implementation called the audit log, which is used to provide detailed information about write operations (add, delete, modify, and modify DN) processed within the server. If the audit log is enabled, the entire content of the change is written to the audit log file (which defaults to `logs/audit`) in LDIF form.

The server also provides a very rich classification system that can be used to filter the content for access log files. This can be helpful when debugging problems with client applications, because it can restrict log information to operations processed only by a particular application (for example, based on IP address and/or authentication DN), only failed operations, or only operations taking a long time to complete, and so on.

## Setup log

The `setup` command writes a log file providing information about the processing that it performs. By default, this log file is written to `logs/setup.log`, although a different name might be used if a file with that name already exists because the `setup` command has already been run. The full path to the setup log file is provided when the `setup` command has completed.

## Tool log

Many of the administrative tools provided with the server (for example, `import-ldif`, `export-ldif`, `backup`, `restore`, and so on) can take a significant length of time to complete write information to standard output or standard error or both while the tool is running. They also write additional output to files in the `logs/tools` directory (for example, `logs/tools/ import-ldif.log`). The information written to these log files can be useful for diagnosing problems encountered while they were running. When running using the server tasks interface, log messages generated while the task is running can alternately be written to the server error log file.

## je.info and je.config files

The primary datastore used by the PingDirectory server is the Oracle Berkeley DB Java Edition (JE). The PingDirectory server provides two primary sources of information about processing within the database. The first is logging performed by the JE code itself, and is written into the

`je.info.0` file in the server containing the database files (for example, `db/userRoot/je.info.0`). In the event of a problem within JE itself, useful information about the nature of the problem can be written to this log. The level of information written to this log file is controlled by the `db-logging-level` property in the backend configuration object. It uses the standard Java logging framework for logging messages, so the standard SEVERE, WARNING, INFO, CONFIG, FINE, FINER, and FINEST levels are available.

The second is configuration information used when opening the database environment. When the backend database environment is opened, then the PingDirectory server will also write a file named `je.config` in the server containing the database files (for example, `db/userRoot/je.config`) with information about the configuration used.

## LDAP SDK debug log

This log can be used to help examine the communication between the PingDirectory server and the PingDirectoryProxy server. It contains information about exceptions that occur during processing, problems establishing and terminating network connections, and problems that occur during the reading and writing of LDAP messages and LDIF entries. You can configure the types of debugging that should be enabled, the debug level that should be used, and whether debug messages should include stack traces. As for other file-based loggers, you can also specify the rotation and retention policies.

---

---
title: Problems with SSL communication
description: Enable TLS debugging in the server to troubleshoot Secure Sockets Layer (SSL) communication issues:
component: pingdirectory
version: 11.1
page_id: pingdirectory:troubleshooting_the_pingdirectory_suite_of_products:pd_sync_probs_ssl_comm
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/troubleshooting_the_pingdirectory_suite_of_products/pd_sync_probs_ssl_comm.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Problems with SSL communication

Enable TLS debugging in the server to troubleshoot Secure Sockets Layer (SSL) *(tooltip: \<div class="paragraph">
\<p>A protocol for authenticated and encrypted links between networked machines, typically over HTTPS. SSL was deprecated in 1999 in favor of Transport Layer Security (TLS).\</p>
\</div>)* communication issues:

```shell
$ dsconfig create-debug-target \
  --publisher-name "File-Based Debug Logger" \
  --target-name
com.unboundid.directory.server.extensions.TLSConnectionSecurityProvider \
  --set debug-level:verbose \
  --set include-throwable-cause:true
```

```shell
$ dsconfig set-log-publisher-prop \
  --publisher-name "File-Based Debug Logger" \
  --set enabled:true \
  --set default-debug-level:disabled
```

In the `java.properties` file, add `-Djavax.net.debug=ssl` to the `start-ds` line, and run `bin/dsjavaproperties` to make the option take effect on a scheduled server restart.

---

---
title: Problems with the admin console
description: If a problem arises when trying to use the admin console, then potential reasons for the problem can include the following:
component: pingdirectory
version: 11.1
page_id: pingdirectory:troubleshooting_the_pingdirectory_suite_of_products:pd_ds_problems_admin_console
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/troubleshooting_the_pingdirectory_suite_of_products/pd_ds_problems_admin_console.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 12, 2024
---

# Problems with the admin console

If a problem arises when trying to use the admin console, then potential reasons for the problem can include the following:

* The web application container used to host the console is not running. If an error occurs while trying to start it, then consult the logs for the web application container.

* If a problem occurs while trying to authenticate to the web application container, then make sure that the target PingDirectory server is online. If it is online, then the access log can provide information about the reasons for the authentication failure.

* If a problem occurs while attempting to interact with the PingDirectoryProxy server instance using the admin console, then the access and error logs for that PingDirectory server instance might provide additional information about the underlying problem.

---

---
title: "Problems with the admin console: JVM memory issues"
description: Console runs out of memory (PermGen). An inadequate PermSize setting in the server, while hosting web applications like the admin console can result in errors like this in the error log:
component: pingdirectory
version: 11.1
page_id: pingdirectory:troubleshooting_the_pingdirectory_suite_of_products:pd_ds_probs_admin_console_jvm_memory
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/troubleshooting_the_pingdirectory_suite_of_products/pd_ds_probs_admin_console_jvm_memory.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
---

# Problems with the admin console: JVM memory issues

**Console runs out of memory (PermGen)**. An inadequate PermSize setting in the server, while hosting web applications like the admin console can result in errors like this in the error log:

```
[02/Mar/2016:07:50:27.017 -0600] threadID=2 category=UTIL
    severity=SEVERE_ERROR msgID=-1 msg="The server experienced an unexpected
    error. Please report this problem and include this log file.
    OutOfMemoryError: PermGen space
    ()\ncom.unboundid.directory.server.core.DirectoryServer.uncaughtException
    (DirectoryServer.java:15783)\njava.lang.ThreadGroup.uncaughtException
    (ThreadGroup.java:1057)\njava.lang.ThreadGroup.uncaughtException
    (ThreadGroup.java:1052)\njava.lang.ThreadGroup.uncaughtException
    (ThreadGroup.java:1052)\njava.lang.Thread.dispatchUncaughtException
    (Thread.java:1986)\nBuild revision: 22496\n"
```

This is only relevant for servers running Java 7.

---

---
title: Problems with the HTTP Connection Handler
description: This topic applies only to the PingDirectory server.
component: pingdirectory
version: 11.1
page_id: pingdirectory:troubleshooting_the_pingdirectory_suite_of_products:pd_ds_probs_http_connection_handler
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/troubleshooting_the_pingdirectory_suite_of_products/pd_ds_probs_http_connection_handler.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Problems with the HTTP Connection Handler

|   |                                                      |
| - | ---------------------------------------------------- |
|   | This topic applies only to the PingDirectory server. |

When problems with the HTTP Connection Handler occur, first look at the HTTP connection handler log to diagnose the issue. The following section shows HTTP log examples when various errors occur.

* **Failed Request Due to a Non-Existent Resource**. The server receives a status code 404, which indicates the server could not match the URI.

  ```
  [15/Mar/2012:17:39:39 -0500] RESULT requestID=0 from="10.2.1.113:52958"
  method="GET" url="https://10.2.1.113:443/Aleph/Users/uid=user.1,ou=people,
  dc=example,dc=com" requestHeader="Host: x2270-11.example.lab"
  requestHeader="Accept: / " requestHeader="User-Agent: curl/7.21.6
  (i386-pc-centos2.10) libcurl/7.21.6 OpenSSL/1.0.0d zlib/1.2.5 libidn/1.22
  libssh2/1.2.7" authorizationType="Basic" statusCode=404 etime=81.484
  responseContentLength=103 responseHeader="Access-Control-Allow-Credentials:true"
  responseContentType="application/json"
  ```

* **Failed Request due to a Malformed Request Body**. The server receives a status code 400, which indicates that the request had a malformed syntax in its request body.

  ```
  [15/Mar/2012:17:47:23-0500] RESULT requestID=10 from="10.2.1.113:55284"
  method="POST" url="https://10.2.1.113:443/Aleph/Users" requestHeader="Host:
  x2270-11.example.lab" requestHeader="Expect: 100-continue"
  requestHeader="Accept: / " requestHeader="Content-Type: application/json"
  requestHeader="User-Agent: curl/ 7.21.6 (i386-pc-centos2.10) libcurl/7.21.6
  OpenSSL/1.0.0d zlib/1.2.5 libidn/1.22 libssh2/1.2.7" authorizationType="Basic"
  requestContentType="application/json" requestContentLength=5564 statusCode=400
  etime=15.272 responseContentLength=133 responseContentType="application/json"
  ```

* **Failed Request due to an unsupported HTTP method**. The server receives a status code 405, which indicates that the specified method (for example, "PATCH") in the request line is not allowed for the resource identified in the URI.

  ```
  [15/Mar/2012:17:48:59-0500] RESULT requestID=11 from="10.2.1.113:55763"
  method="PATCH" url="https://10.2.1.113:443/Aleph/Users" requestHeader="Host:
  x2270-11.example.lab" requestHeader="Accept: / " requestHeader="Content-Type:
  application/json" requestHeader="User-Agent: curl/7.21.6 (i386-pc-centos2.10)
  libcurl/7.21.6 OpenSSL/1.0.0d zlib/1.2.5 libidn/1.22 libssh2/1.2.7"
  authorization-Type="Basic" requestContentType="application/json" statusCode=405
  etime=6.807 responseContentLength=0 responseHeader="Allow: POST, GET, OPTIONS, HEAD"
  ```

* **Failed Request due to an Unsupported Media Type**. The server receives a status code 415, which indicates that the request entity is in a format that is not supported by the requested resource.

  ```
  [15/Mar/2012:17:44:45-0500] RESULT requestID=4 from="10.2.1.113:54493"
  method="POST" url="https://10.2.1.113:443/Aleph/Users" requestHeader="Host:
  x2270-11.example.lab" requestHeader="Accept: / " requestHeader="Content-Type:
  application/atom+xml" requestHeader="User-Agent: curl/7.21.6 (i386-pc-centos2.10)
  libcurl/7.21.6 OpenSSL/1.0.0d zlib/1.2.5 libidn/1.22 libssh2/1.2.7"
  authorizationType="Basic" requestContentType="application/atom+xml"
  requestContentLength=3 statusCode=415 etime=6.222 responseContentLength=1402
  responseHeader="Cache-Control: must-revalidate,no-cache,no-store"
  responseContentType="text/html;charset=ISO-8859-1"
  ```

* **Failed Request due to an Authentication Error**. The server receives a status code 401, which indicates that the request requires user authentication.

  ```
  [15/Mar/2012:17:46:06-0500] RESULT requestID=8 from="10.2.1.113:54899"
  method="GET" url="https://10.2.1.113:443/Aleph/Schemas" requestHeader="Host:
  x2270-11.example.lab" requestHeader="Accept: / " requestHeader="User-Agent:
  curl/7.21.6 (i386-pc-centos2.10) libcurl/7.21.6 OpenSSL/1.0.0d zlib/1.2.5
  libidn/1.22 libssh2/ 1.2.7" authorizationType="Basic" statusCode=401
  etime=2.751 responseContentLength=63 responseHeader="WWW-Authenticate: Basic
  realm=SCIM" responseHeader="Access-Control-Allow-Credentials: true"
  responseContentType="application/json"
  ```

---

---
title: Providing information for support cases
description: If a problem arises that you are unable to fully diagnose and correct on your own, then contact your authorized support provider for assistance. To ensure that the problem can be addressed as quickly as possible, be sure to provide all of the information that the support personnel might need to fully understand the underlying cause by running the collect-support-data tool, and then sending the generated zip file to your authorized support provider. It is good practice to run this tool and send the ZIP file to your authorized support provider before any corrective action has taken place.
component: pingdirectory
version: 11.1
page_id: pingdirectory:troubleshooting_the_pingdirectory_suite_of_products:pd_ds_provide_info_support_cases
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/troubleshooting_the_pingdirectory_suite_of_products/pd_ds_provide_info_support_cases.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
---

# Providing information for support cases

If a problem arises that you are unable to fully diagnose and correct on your own, then contact your authorized support provider for assistance. To ensure that the problem can be addressed as quickly as possible, be sure to provide all of the information that the support personnel might need to fully understand the underlying cause by running the `collect-support-data` tool, and then sending the generated zip file to your authorized support provider. It is good practice to run this tool and send the ZIP file to your authorized support provider before any corrective action has taken place.