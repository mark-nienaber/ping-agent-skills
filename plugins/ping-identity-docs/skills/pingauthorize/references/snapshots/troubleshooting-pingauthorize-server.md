---
title: Advanced HTTP event logging
description: The PingAuthorize Server provides advanced HTTP event logging through the file-based trace logger to help diagnose slowdowns in HTTP request processing.
component: pingauthorize
version: 11.1
page_id: pingauthorize:troubleshooting_pingauthorize_server:paz_advanced_http_logging_monitoring
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/troubleshooting_pingauthorize_server/paz_advanced_http_logging_monitoring.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 26, 2026
section_ids:
  http-request-lifecycle: HTTP request lifecycle
  enabling-http-event-logging: Enabling HTTP event logging
  steps: Steps
  steps-2: Steps
---

# Advanced HTTP event logging

The PingAuthorize Server provides advanced HTTP event logging through the file-based trace logger to help diagnose slowdowns in HTTP request processing.

By capturing the full lifecycle of HTTP requests, you can identify performance bottlenecks and fine-tune the server for your workload.

## HTTP request lifecycle

The typical HTTP request lifecycle in the PingAuthorize Server is as follows:

1. The server accepts a low-level channel.

   This begins the request lifecycle at the lowest level of the network stack.

   * Example log:

     ```
     HTTP-EVENT CHANNEL channelID=89 msg="accepting channel"
     ```

2. The client establishes a TCP socket with the server.

   This creates the foundational network connection.

   * Example log:

     ```
     HTTP-EVENT SOCKET socketID=90 remotePort="63418" localPort="8443" msg="opened"
     ```

3. An HTTP connection is established over the socket.

   The server is now ready to listen for HTTP-specific traffic.

   * Example log:

     ```
     HTTP-EVENT CONNECTION connectionID=90 channelID=90 socketID=89 msg="open"
     ```

4. The server begins processing the client request.

   The server receives the request and assigns it to a handler thread.

   * Example log:

     ```
     HTTP-EVENT REQUEST-PROCESSING requestHash=1453742073 connectionID=90 channelID=90 socketID=89 method=POST URL="http://localhost:8443/governance-engine" msg="begin request"

     HTTP-EVENT REQUEST-PROCESSING requestHash=1453742073 connectionID=90 channelID=90 socketID=89 method=POST URL="http://localhost:8443/governance-engine" msg="dispatching request"
     ```

5. The server finishes processing the request and sends a response.

   |   |                                                                                                                                           |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------- |
   |   | This log entry is especially important for performance analysis, as it contains the total request processing duration and the queue time. |

   * Example log:

     ```
     HTTP-EVENT REQUEST-PROCESSING requestID=146 correlationID="7fed277a-c867-4571-9f6d-591722f8754c" requestHash=1453742073 connectionID=90 channelID=90 socketID=89 method=POST URL="https://localhost:8443/governance-engine" totalDurationMs=167 queueDurationMs=1 requestDurationMs=45 requestContentLength=8 responseDurationMs=0 responseContentLength=281 requestBeginTime="23/Jun/2025:20:46:52.037 -0500" dispatchTime="23/Jun/2025:20:46:52.037 -0500" requestEndTime="23/Jun/2025:20:46:52.082 -0500" responseBeginTime="23/Jun/2025:20:46:52.202 -0500" responseEndTime="23/Jun/2025:20:46:52.202 -0500" requestCompleteTime="23/Jun/2025:20:46:52.204 -0500" msg="complete processing"
     ```

6. The server closes the connection.

   After sending the response, the server can close the HTTP connection. For persistent connections, this step might be delayed until a timeout or until the client closes it.

   * Example log:

     ```
     HTTP-EVENT CONNECTION connectionID=89 channelID=89 totalDurationMs=6 openTime="23/Jun/2025:20:46:52.029 -0500" closeTime="23/Jun/2025:20:46:52.035 -0500" msg="close"
     ```

7. The server closes the underlying TCP socket.

   The server terminates the low-level network socket, freeing up the resource.

   * Example log:

     ```
     HTTP-EVENT SOCKET socketID=90 remotePort="63418" localPort="8443" totalDurationMs=4 incomingBytes=0 outgoingBytes=0 socketOpenedTime="23/Jun/2025:20:46:52.029 -0500" socketClosedTime="23/Jun/2025:20:46:52.033 -0500" msg="closed"
     ```

Each HTTP event includes a unique identifier that allows you to trace the full lifecycle of a request and pinpoint exactly where delays occur, whether in connection setup, thread queuing, or request handling. When correlation ID tracking is enabled, the `correlationID` field in `request-processing` complete events lets you cross-reference the request against related entries in the debug trace and policy decision logs. Learn more in [Managing HTTP correlation IDs](../pingauthorize_server_administration_guide/paz_manage_http_corr_ids.html).

## Enabling HTTP event logging

To trace the complete lifecycle of HTTP requests, configure the `http-event` property in the file-based trace logger.

You can individually enable the following HTTP event types:

| HTTP event type      | Description                                                                                                                                                                                     |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `socket`             | Logs when a TCP socket is opened, closed, or reused. The close event includes the total duration the socket was open.                                                                           |
| `connection`         | Logs when an HTTP connection is opened, closed, or reused. The close event includes the total duration of the connection.                                                                       |
| `channel`            | Logs low-level channel events related to the connection.                                                                                                                                        |
| `request-processing` | Logs when request processing starts and finishes. The finish event includes the total request processing duration and the queue time (the time the request spent waiting for a handler thread). |

|   |                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The queue time calculation logged by `request-processing` events might be less accurate in high-throughput scenarios where sockets are reused for multiple requests. |

You can use the administrative console or `dsconfig` to enable detailed HTTP event logging.

|   |                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------- |
|   | High-volume logging can impact performance, so you should only enable event types relevant to your troubleshooting goals. |

By default, the file-based trace logger writes messages to the `logs/trace.log` file.

* Admin console

* dsconfig

### Steps

1. Go to **Configuration > Logging, Monitoring, and Notifications > Log Publishers**.

2. Click **File-Based Trace Logger**.

3. Select the **Enabled** checkbox if the logger isn't already enabled.

4. Scroll down to the **Log Messages To Include** section, and under **HTTP Event**, select event types to include in the trace log.

   ![Screen capture of the HTTP Event configuration property in the file-based trace logger.](_images/paz_http_event_logging_monitoring.png)

5. Click **Save**.

### Steps

* Use the `dsconfig set-log-publisher-prop` command with the `--add http-event` argument to enable specific HTTP event types.

  The following example enables logging for socket and request processing events:

  ```shell
  dsconfig set-log-publisher-prop \
    --publisher-name "File-Based Trace Logger" \
    --add http-event:socket \
    --add http-event:request-processing
  ```

---

---
title: Common problems and potential solutions
description: This section describes a number of different types of problems that can occur and common potential causes for them.
component: pingauthorize
version: 11.1
page_id: pingauthorize:troubleshooting_pingauthorize_server:paz_common_probs_potential_sols
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/troubleshooting_pingauthorize_server/paz_common_probs_potential_sols.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 22, 2023
---

# Common problems and potential solutions

This section describes a number of different types of problems that can occur and common potential causes for them.

---

---
title: Conditions for automatic server shutdown
description: All PingAuthorize Server instances will shut down in an out-of-memory condition, a low-disk-space error state, or if they run out of file descriptors.
component: pingauthorize
version: 11.1
page_id: pingauthorize:troubleshooting_pingauthorize_server:paz_conditions_auto_server_shutdown
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/troubleshooting_pingauthorize_server/paz_conditions_auto_server_shutdown.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 24, 2023
---

# Conditions for automatic server shutdown

All PingAuthorize Server instances will shut down in an out-of-memory condition, a low-disk-space error state, or if they run out of file descriptors.

The server will enter lockdown mode on unrecoverable database environment errors, but can be configured to shutdown instead with this setting:

```shell
$ dsconfig set-global-configuration-prop \
            --set unrecoverable-database-error-mode:initiate-server-shutdown
```

---

---
title: Detecting expensive HTTP threads
description: The HTTP Connection Handler can detect expensive threads that spend an unusually long time processing HTTP requests.
component: pingauthorize
version: 11.1
page_id: pingauthorize:troubleshooting_pingauthorize_server:paz_detecting_expensive_threads
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/troubleshooting_pingauthorize_server/paz_detecting_expensive_threads.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2025
section_ids:
  how-it-works: How it works
  configuring-expensive-thread-detection: Configuring expensive thread detection
  steps: Steps
  steps-2: Steps
  analyzing-thread-dump-files: Analyzing thread dump files
  thread-dump-file-management: Thread dump file management
---

# Detecting expensive HTTP threads

The HTTP Connection Handler can detect expensive threads that spend an unusually long time processing HTTP requests. This helps identify potential performance bottlenecks and responsiveness issues in the PingAuthorize Server.

When request processing takes longer than a configured threshold, the PingAuthorize Server can automatically generate a thread dump. A thread dump is a snapshot of all active application threads, indicating whether each thread is actively running, blocked waiting for a resource, or waiting for another task to complete. Thread dumps also include the sequence of method calls each thread is currently executing.

This diagnostic information is helpful for troubleshooting slowdowns caused by issues such as:

* Delays in connecting to external data sources

* Long-running policy evaluations

* Resource contention or deadlocks

* Infrastructure problems affecting responsiveness

Analyzing a thread dump enables you to pinpoint the specific operations responsible for performance degradation.

## How it works

The PingAuthorize Server uses the following process to detect expensive threads:

1. At a regular interval, the server checks the status of all active HTTP threads.

2. If a thread is still handling the same request it was processing during the previous check, the server flags that thread as expensive.

3. If the number of concurrently expensive threads meets a configured threshold, the server creates a thread dump.

4. Each thread dump is saved as a separate file in the `/logs/thread-dumps` directory. To avoid excessive logging, the server waits for a configured interval before creating another thread dump.

   Thread dump files are named with the following format:

   `expensive-operation-dump-<timestamp>.log`

   |   |                                                                  |
   | - | ---------------------------------------------------------------- |
   |   | The thread dump file path and naming format aren't configurable. |

## Configuring expensive thread detection

The HTTP Connection Handler provides the following settings for configuring expensive thread detection:

| Setting name                                  | `dsconfig` parameter name                   | Description                                                                                                                                                                                                                                                            | Default value |
| --------------------------------------------- | ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| **Expensive Thread Check Interval**           | `expensive-thread-check-interval`           | Specifies how frequently the server checks thread activity. If a thread is processing the same request for two consecutive checks, the server flags it as expensive.&#xA;&#xA;You must specify a non-zero value for this setting to enable expensive thread detection. | `0 ms`        |
| **Expensive Thread Minimum Concurrent Count** | `expensive-thread-minimum-concurrent-count` | Specifies the minimum number of simultaneously expensive threads required to generate a thread dump.                                                                                                                                                                   | `1`           |
| **Expensive Thread Hold Off Interval**        | `expensive-thread-hold-off-interval`        | Specifies the cooldown period the server waits after creating a thread dump before it can create another. This setting helps prevent excessive disk usage.                                                                                                             | `60000 ms`    |

You can configure expensive thread detection with the administrative console or with the `dsconfig` command.

* Admin console

* dsconfig

### Steps

1. Go to **System > Connection Handlers**.

2. Click **HTTP Connection Handler** or **HTTPS Connection Handler**.

3. Scroll down and configure the following:

   * **Expensive Thread Check Interval**

   * **Expensive Thread Minimum Concurrent Count**

   * **Expensive Thread Hold Off Interval**

### Steps

* Run the `dsconfig set-connection-handler-prop` command with the following arguments:

  ```shell
  dsconfig set-connection-handler-prop \
    --handler-name "HTTP Connection Handler" \
    --set "expensive-thread-check-interval:<time-interval> ms" \
    --set "expensive-thread-minimum-concurrent-count:<thread-count>" \
    --set "expensive-thread-hold-off-interval:<time-interval> ms"
  ```

|   |                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------- |
|   | You must restart the server or the HTTP Connection Handler for the expensive thread detection settings to take effect. |

## Analyzing thread dump files

Each thread dump file is organized into three main parts:

* Header summary: Provides context about why the thread dump was generated. It includes the name of the detector that triggered the dump, the number of expensive threads identified, and the time interval over which they were detected.

* Expensive thread list: Lists the threads flagged as expensive immediately after the summary. Each entry includes a thread ID, thread name, and correlation ID to help trace related request activity across other logs.

  |   |                                              |
  | - | -------------------------------------------- |
  |   | Save the thread IDs for use during analysis. |

* Full stack trace: Shows a complete snapshot of all threads running in the PingAuthorize Server's Java process at the time of the thread dump. This section provides detailed request context to help identify performance bottlenecks or blocked threads.

  Use the thread IDs from the expensive thread list to locate and analyze each expensive thread's state.

For example, the following header summary and expensive thread list identify a single expensive thread, detected over an interval of 5000 milliseconds:

```
HTTP Connection Handler :80 worker Expensive HTTP Thread Detector (10.3.0.0-20250611152739.000Z-364a3822) detected that 1 threads were found to be processing the same HTTP request over an interval of at least 5000 ms:
* Thread id=176 name='HTTP Connection Handler :80 worker 6 (10.3.0.0-20250611152739.000Z-364a3822) requestID=0 correlationID="3bf39de1-7bc4-4937-b99a-62785a41f55d"
```

The following is a truncated version of the expensive thread's stack trace entry:

```
"HTTP Connection Handler :80 worker 6 (10.3.0.0-20250611152739.000Z-364a3822)" priority=5 id=176
   java.lang.Thread.State: WAITING
        at java.base@17.0.10/jdk.internal.misc.Unsafe.park(Native Method)
        at java.base@17.0.10/java.util.concurrent.locks.LockSupport.park(LockSupport.java:211)
        at java.base@17.0.10/java.util.concurrent.CompletableFuture$Signaller.block(CompletableFuture.java:1864)
        at java.base@17.0.10/java.util.concurrent.ForkJoinPool.unmanagedBlock(ForkJoinPool.java:3465)
        at java.base@17.0.10/java.util.concurrent.ForkJoinPool.managedBlock(ForkJoinPool.java:3436)
        at java.base@17.0.10/java.util.concurrent.CompletableFuture.waitingGet(CompletableFuture.java:1898)
        at java.base@17.0.10/java.util.concurrent.CompletableFuture.get(CompletableFuture.java:2072)
        at app//com.pingidentity.authorize.decisionengine2.evaluation.effects.Inner.get(Inner.java:32)
```

A thread state of `WAITING` indicates the thread is idle, waiting indefinitely for another thread to perform an action. Learn more about thread states in the [`Enum Thread.State` reference](https://docs.oracle.com/javase/8/docs/api/java/lang/Thread.State.html) in the Java documentation.

## Thread dump file management

The PingAuthorize Server doesn't automatically manage the thread dump files it creates. You must implement your own retention policy for these files, including any log rotation, compression, or cleanup.

In a containerized deployment, make sure a mechanism is in place, such as a volume mount, to persist thread dump files and make them available for analysis outside the container.

---

---
title: General troubleshooting methodology
description: When you detect a problem, use the following general methodology to isolate the problem.
component: pingauthorize
version: 11.1
page_id: pingauthorize:troubleshooting_pingauthorize_server:paz_general_troubleshoot_method
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/troubleshooting_pingauthorize_server/paz_general_troubleshoot_method.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 22, 2023
---

# General troubleshooting methodology

When you detect a problem, use the following general methodology to isolate the problem.

1. Run the `bin/status` tool or look at the server status in the Administrative Console. The `status` tool provides a summary of the server's current state with key metrics and a list of recent alerts.

2. Look in the server logs. In particular, view the following logs:

   * `logs/errors`

   * `logs/failed-ops`

   * `logs/expensive-ops`

3. Use system commands such as `vmstat` and `iostat` to determine if the server is bottlenecked on a system resource like CPU or disk throughput.

4. For server performance issues (especially intermittent ones like spikes in response time), enable the `periodic-stats-logger` to help isolate problems, because it stores important server performance information on a per-second basis. The `periodic-stats-logger` can save the information in a `.csv` file that can be loaded into a spreadsheet.

   The information this logger makes available is very configurable. You can create multiple loggers for different types of information or a different frequency of logging (for example, hourly data in addition to per-second data). For more information, see [About Periodic Stats Loggers](../pingauthorize_server_administration_guide/paz_prof_server_perf_stats.html).

5. For more advanced users, run the `collect-support-data` tool on the system, unzip the archive, and look through the collected information. This is often useful when administrators most familiar with the data platform do not have direct access to the systems where the production servers are running. They can examine the `collect-support-data` archive on a different server. For more information, see [Working with the collect-support-data tool](paz_working_with_collect_support_data.html).

|   |                                                                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Run the `collect-support-data` tool whenever you can't easily identify the cause of a problem. You can pass this information to your authorized support provider for assistance in identifying and addressing the root cause of the issue. |

---

---
title: Java diagnostic information
description: In addition to the tools listed in the previous section, the JVM can provide additional diagnostic information in response to certain events.
component: pingauthorize
version: 11.1
page_id: pingauthorize:troubleshooting_pingauthorize_server:paz_java_diagnostic_info
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/troubleshooting_pingauthorize_server/paz_java_diagnostic_info.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 28, 2025
section_ids:
  jvm-crash-diagnostic-information: JVM crash diagnostic information
---

# Java diagnostic information

In addition to the tools listed in the previous section, the JVM can provide additional diagnostic information in response to certain events.

## JVM crash diagnostic information

If the JVM crashes, then it generates a fatal error log with information about the state of the JVM at the time of the crash. By default, this file is named `hs_err_pid<processID>.log` and is written into the base directory of the PingAuthorize Server installation. This file includes information on the underlying cause of the JVM crash, information about the threads running and Java heap at the time of the crash, the options provided to the JVM, environment variables that were set, and information about the underlying system.

---

---
title: Java troubleshooting tools
description: The Java Development Kit provides a number of tools for obtaining information about Java applications and diagnosing problems. These tools are not included with the Java Runtime Environment, so the full Java Development Environment should always be installed and used to run the server.
component: pingauthorize
version: 11.1
page_id: pingauthorize:troubleshooting_pingauthorize_server:paz_java_troubleshoot_tools
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/troubleshooting_pingauthorize_server/paz_java_troubleshoot_tools.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 28, 2025
section_ids:
  jps: jps
  jstack: jstack
  jmap: jmap
  jhat: jhat
  jstat: jstat
---

# Java troubleshooting tools

The Java Development Kit provides a number of tools for obtaining information about Java applications and diagnosing problems. These tools are not included with the Java Runtime Environment, so the full Java Development Environment should always be installed and used to run the server.

## jps

The `jps` tool is a Java-specific version of the UNIX `ps` tool. It can be used to obtain a list of all Java processes currently running and their respective process identifiers. When invoked by a non-root user, it will list only Java processes running as that user. When invoked by a root user, it lists all Java processes on the system.

This tool can be used to see if PingAuthorize Server is running and if a process ID has been assigned to it. This process ID can be used in conjunction with other tools to perform further analysis.

This tool can be run without any arguments, but some of the more useful arguments include:

* `-v`

  Includes the arguments passed to the Java Virtual Machine (JVM) *(tooltip: \<div class="paragraph">
  \<p>A virtual machine that allows a computer to run Java programs and programs that are compiled to Java bytecode.\</p>
  \</div>)* for the processes that are listed.

* `-m`

  Includes the arguments passed to the main method for the processes that are listed.

* `-l` (lowercase L)

  Includes the fully qualified name for the main class rather than only the base class name.

## jstack

The `jstack` tool is used to obtain a stack trace of a running Java process, or optionally from a core file generated if the JVM happens to crash. A stack trace can be extremely valuable when trying to debug a problem, because it provides information about all threads running and exactly what each thread is doing at the point in time that the stack trace was obtained.

Stack traces are helpful when diagnosing problems in which the server appears to be hung or behaving slowly. Java stack traces are generally more helpful than native stack traces, because Java threads can have user-friendly names (as do the threads used by the server), and the frame of the stack trace may include the line number of the source file to which it corresponds. This is useful when diagnosing problems and often allows them to be identified and resolved quickly.

To obtain a stack trace from a running JVM, use the command:

```
jstack  <processID>
```

Replace `<processID>` with the process ID of the target JVM as returned by the `jps` command.

To obtain a stack trace from a core file from a Java process, use the command:

```
jstack  <pathToJava>  <pathToCore>
```

Replace `<pathToJava>` with the path to the Java command from which the core file was created, and replace `<pathToCore>` with the path to the core file to examine. In either case, the stack trace is written to standard output and includes the names and call stacks for each of the threads that were active in the JVM.

In many cases, no additional options are necessary. The `-l` option can be added to obtain a long listing, which includes additional information about locks owned by the threads. The `-m` option can be used to include native frames in the stack trace.

## jmap

The `jmap` tool is used to obtain information about the memory consumed by the JVM. It is very similar to the native `pmap` tool provided by many operating systems. As with the `jstack` tool, `jmap` can be invoked against a running Java process by providing the process ID or against a core file. For example:

```
jmap  <processID>
jmap  <pathToJava>  <pathToCore>
```

Some of the additional arguments include:

* `-dump:``live,format=b,file=filename`

  Dumps the live heap data to a file that can be examined by the `jhat` tool.

* `-heap`

  Provides a summary of the memory used in the Java heap, along with information about the garbage collection algorithm in use.

* `-histo:``live`

  Provides a count of the number of objects of each type contained in the heap. If the `live` option is included, then only live objects are included; otherwise, the count includes objects that are no longer in use and are garbage collected.

## jhat

The `jhat` (Java Heap Analysis Tool) utility provides the ability to analyze the contents of the Java heap. It can be used to analyze a heap dump file, which is generated if PingAuthorize Server encounters an `out of memory` error (as a result of the `-XX:``+HeapDumpOnOutOfMemoryError` JVM option) or from the use of the `jmap` command with the `-dump` option.

The `jhat` tool acts as a web server that can be accessed by a browser to query the contents of the heap. Several predefined queries are available to help determine the types of objects consuming significant amounts of heap space, and it also provides a custom query language (OQL, the Object Query Language) for performing more advanced types of analysis.

The `jhat` tool can be launched with the path to the heap dump file. For example:

```
jhat  </path/to/heap.dump>
```

This command causes the `jhat` web server to begin listening on port 7000. It can be accessed in a browser at <http://localhost:7000> (or http\://*\<address>*:7000 from a remote system). An alternate port number can be specified using the `-port` option. For example:

```
jhat -port 1234  </path/to/heap.dump>
```

To issue custom OQL searches, access the web interface using the URL <http://localhost:7000/oql/> (the trailing slash must be provided). Additional information about the OQL syntax may be obtained in the web interface at <http://localhost:7000/oqlhelp/>.

## jstat

The `jstat` tool is used to obtain a variety of statistical information from the JVM, much like the `vmstat` utility, which can be used to obtain CPU utilization information from the operating system. The general manner to invoke it is as follows:

```
jstat  <type>  <processID>  <interval>
```

The *\<interval>* option specifies the length of time in milliseconds between lines of output. The *\<processID>* option specifies the process ID of the JVM used to run PingAuthorize Server, which can be obtained by running `jps` (as mentioned previously). The *\<type>* option specifies the type of output that should be provided. Some of the most useful types include:

* `-class`

  Provides information about class loading and unloading.

* `-compile`

  Provides information about the activity of the JIT complex.

* `-printcompilation`

  Provides information about JIT method compilation.

* `-gc`

  Provides information about the activity of the garbage collector.

* `-gccapacity`

  Provides information about memory region capacities.

---

---
title: PingAuthorize Server logs for troubleshooting and monitoring
description: PingAuthorize Server has a comprehensive default set of log files and monitor entries that are useful when troubleshooting a particular server problem.
component: pingauthorize
version: 11.1
page_id: pingauthorize:troubleshooting_pingauthorize_server:paz_dir_server_troubleshoot_info
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/troubleshooting_pingauthorize_server/paz_dir_server_troubleshoot_info.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 28, 2025
section_ids:
  error-log: Error log
  server-out-log: server.out log
  debug-log: Debug log
  config-audit-log-and-the-configuration-archive: Config audit log and the configuration archive
  setup-log: Setup log
  tool-log: Tool log
---

# PingAuthorize Server logs for troubleshooting and monitoring

PingAuthorize Server has a comprehensive default set of log files and monitor entries that are useful when troubleshooting a particular server problem.

## Error log

By default, this log file is available at `logs/errors` below the server install root, and it provides information about warnings, errors, and other significant events that occur within the server. A number of messages are written to this file on startup and shutdown, but while the server is running, there is normally little information written to it. In the event that a problem does occur, the server writes information about that problem to this file.

The following is an example of a message that might be written to the error log:

```
[11/Apr/2011:10:31:53.783 -0500] category=CORE severity=NOTICE msgID=458887 msg="The  {pingauthorize}  Server has started successfully."
```

The category field provides information about the area of the server from which the message was generated. Available categories include:

```
ACCESS_CONTROL, ADMIN, ADMIN_TOOL, BACKEND, CONFIG, CORE, DSCONFIG, EXTENSIONS, PROTOCOL, SCHEMA, JEB, SYNC, LOG, PLUGIN, PROXY, QUICKSETUP, REPLICATION, RUNTIME_INFORMATION, TASK, THIRD_PARTY, TOOLS, USER_DEFINED, UTIL, VERSION
```

The severity field provides information about how severe the server considers the problem to be. Available severities include:

* `DEBUG`

  Used for messages that provide verbose debugging information and do not indicate any kind of problem. Note that this severity level is rarely used for error logging, because the server provides a separate debug logging facility.

* `INFORMATION`

  Used for informational messages that can be useful from time to time but are not normally something that administrators need to see.

* `MILD_WARNING`

  Used for problems that the server detects, which can indicate something unusual occurred, but the warning does not prevent the server from completing the task it was working on. These warnings are not normally something that should be of concern to administrators.

* `MILD_ERROR`

  Used for problems detected by the server that prevented it from completing some processing normally but that are not considered to be a significant problem requiring administrative action.

* `NOTICE`

  Used for information messages about significant events that occur within the server and are considered important enough to warrant making available to administrators under normal conditions.

* `SEVERE_WARNING`

  Used for problems that the server detects that might lead to bigger problems in the future and should be addressed by administrators.

* `SEVERE_ERROR`

  Used for significant problems that have prevented the server from successfully completing processing and are considered important.

* `FATAL_ERROR`

  Used for critical problems that arise which might leave the server unable to continue processing operations normally.

The messages written to the error log can be filtered based on their severities in two ways. First, the error log publisher has a `default-severity` property, which can be used to specify the severity of messages logged regardless of their category. By default, this includes the `NOTICE`, `SEVERE_WARNING`, `SEVERE_ERROR`, and `FATAL_ERROR` severities.

You can override these severities on a per-category basis using the `override-severity` property. If this property is used, then each value should consist of a category name followed by an equal sign and a comma-delimited set of severities that should be logged for messages in that category. For example, the following override severity would enable logging at all severity levels in the `PROTOCOL` category:

```
protocol=debug,information,mild-warning,mild-error,notice,severe-warning,severe-error,fatal-error
```

Note that for the purposes of this configuration property, any underscores in category or severity names should be replaced with dashes. Also, severities are not inherently hierarchical, so enabling the `DEBUG` severity for a category will not automatically enable logging at the `INFORMATION`, `MILD_WARNING`, or `MILD_ERROR` severities.

The error log configuration can be altered on the fly using tools like `dsconfig`, the Administrative Console, or the LDIF connection handler, and changes will take effect immediately. You can configure multiple error logs that are active in the server at the same time, writing to different log files with different configurations. For example, a new error logger can be activated with a different set of default severities to debug a short-term problem, and then that logger can be removed after the problem is resolved, so that the normal error log does not contain any of the more verbose information.

## server.out log

The `server.out` file holds any information written to standard output or standard error while the server is running. Normally, it includes a number of messages written at startup and shutdown, as well as information about any administrative alerts generated while the server is running. In most cases, this information is also written to the error log. The `server.out` file can also contain output generated by the JVM. For example, if garbage collection debugging is enabled, or if a stack trace is requested via `kill -QUIT` as described in a later section, then output is written to this file.

## Debug log

The debug log provides a means of obtaining information that can be used for troubleshooting problems but is not necessary or desirable to have available while the server is functioning normally. As a result, the debug log is disabled by default, but it can be enabled and configured at any time.

Some of the most notable configuration properties for the debug log publisher include:

* `enabled`

  Indicates whether debug logging is enabled. By default, it is disabled.

* `log-file`

  Specifies the path to the file to be written. By default, debug messages are written to the `logs/debug` file.

* `debug-level`

  Specifies the minimum log level for debug messages that should be written. The default value is `error`, which only provides information about errors that occur during processing (for example, exception stack traces). Other supported debug levels include `warning`, `info`, and `verbose`. Note that unlike error log severities, the debug log levels are hierarchical. Configuring a specified debug level enables any debugging at any higher levels. For example, configuring the `info` debug level automatically enables the `warning` and `error` levels.

* `debug-category`

  Specifies the categories for debug messages that should be written. Some of the most useful categories include `caught` (provides information and stack traces for any exceptions caught during processing), `database-access` (provides information about operations performed in the underlying database), `protocol` (provides information about ASN.1 and LDAP communication performed by the server), and `data` (provides information about raw data read from or written to clients).

As with the error and access logs, multiple debug loggers can be active in the server at any time with different configurations and log files to help isolate information that might be relevant to a particular problem. Debug targets can be used to further pare down the set of messages generated. For example, you can specify that the debug logs be generated only within a specific class or package.

|   |                                                                                                                                                                                                                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Enabling one or more debug loggers can have a significant impact on server performance. Enable debug loggers only when necessary, and scope them so that only pertinent debug information is recorded. If you need to enable the debug logger, you should work with your authorized support provider to best configure the debug target and interpret the output. |

## Config audit log and the configuration archive

The configuration audit log provides a record of any changes made to the server configuration while the server is online. This information is written to the `logs/config-audit.log` file and provides information about the configuration change in the form that can be used to perform the operation in a non-interactive manner with the `dsconfig` command. Other information written for each change includes:

* Time that the configuration change was made

* Connection ID and operation ID for the corresponding change, which can be used to correlate it with information in the access log

* DN of the user requesting the configuration change and the method by which that user authenticated to the server

* Source and destination addresses of the client connection

* Command that can be used to undo the change and revert to the previous configuration for the associated configuration object

In addition to information about the individual changes that are made to the configuration, the server maintains complete copies of all previous configurations. These configurations are provided in the `config/archived-configs` directory and are gzip-compressed copies of the `config/config.ldif` file in use before the configuration change was made. The file names contain timestamps that indicate when that configuration was first used.

## Setup log

The `setup` tool writes a log file providing information about the processing that it performs. By default, this log file is written to `logs/setup.log` although a different name may be used if a file with that name already exists, because the `setup` tool has already been run. The full path to the setup log file is provided when the `setup` tool has completed.

## Tool log

Many of the administrative tools provided with the server (for example, `import-ldif`, `export-ldif`, `backup`, `restore`, etc.) can take a significant length of time to complete writing information to standard output or standard error (or both) while the tool is running. They also write additional output to files in the `logs/tools` directory (for example, `logs/tools/ import-ldif.log`). The information written to these log files can be useful for diagnosing problems encountered while they were running. When running using the server tasks interface, log messages generated while the task is running can alternately be written to the server error log file.

---

---
title: Problems with the administrative console
description: To troubleshoot problems with the administrative console, consider these potential causes:
component: pingauthorize
version: 11.1
page_id: pingauthorize:troubleshooting_pingauthorize_server:paz_problems_admin_console
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/troubleshooting_pingauthorize_server/paz_problems_admin_console.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 28, 2025
section_ids:
  jvm-memory-issues: JVM memory issues
---

# Problems with the administrative console

To troubleshoot problems with the administrative console, consider these potential causes:

* The web application container used to host the console is not running. If an error occurs while trying to start it, then consult the logs for the web application container.

* If a problem occurs while trying to authenticate to the web application container, then make sure that the target PingAuthorize Server is online. If it is online, then the access log may provide information about the reasons for the authentication failure.

## JVM memory issues

For servers running Java 7 and hosting web applications like the administrative console, an inadequate **PermSize** setting might cause an `OutOfMemoryError` related to `PermGen space`, as shown in the following error log example:

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

---

---
title: Problems with the HTTP Connection Handler
description: When problems with the HTTP Connection Handler occur, first look at the HTTP connection handler log to diagnose the issue.
component: pingauthorize
version: 11.1
page_id: pingauthorize:troubleshooting_pingauthorize_server:paz_probs_http_connection_handler
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/troubleshooting_pingauthorize_server/paz_probs_http_connection_handler.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 28, 2023
---

# Problems with the HTTP Connection Handler

When problems with the HTTP Connection Handler occur, first look at the HTTP connection handler log to diagnose the issue.

The following HTTP log examples detail various errors that can occur related to the HTTP Connection Handler:

* Failed request due to a non-existent resource

  The server receives a status code 404, which indicates the server could not match the URI:

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

* Failed request due to a malformed request body

  The server receives a status code 400, which indicates that the request had malformed syntax in its request body:

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

* Failed request due to an unsupported HTTP method

  The server receives a status code 405, which indicates that the specified HTTP method (e.g., `"PATCH"`) in the request line is not allowed for the resource identified in the URI:

  ```
  [15/Mar/2012:17:48:59-0500] RESULT requestID=11 from="10.2.1.113:55763"
  method="PATCH" url="https://10.2.1.113:443/Aleph/Users" requestHeader="Host:
  x2270-11.example.lab" requestHeader="Accept: / " requestHeader="Content-Type:
  application/json" requestHeader="User-Agent: curl/7.21.6 (i386-pc-centos2.10)
  libcurl/7.21.6 OpenSSL/1.0.0d zlib/1.2.5 libidn/1.22 libssh2/1.2.7"
  authorization-Type="Basic" requestContentType="application/json" statusCode=405
  etime=6.807 responseContentLength=0 responseHeader="Allow: POST, GET, OPTIONS, HEAD"
  ```

* Failed request due to an unsupported media type

  The server receives a status code 415, which indicates that the request entity is in a format that is not supported by the requested resource:

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

* Failed request due to an authentication error

  The server receives a status code 401, which indicates that the request requires user authentication:

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
description: If you are unable to fully diagnose with the server, contact your authorized support provider for assistance.
component: pingauthorize
version: 11.1
page_id: pingauthorize:troubleshooting_pingauthorize_server:paz_provide_info_support_cases
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/troubleshooting_pingauthorize_server/paz_provide_info_support_cases.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 28, 2023
---

# Providing information for support cases

If you are unable to fully diagnose with the server, contact your authorized support provider for assistance.

To ensure that a problem can be addressed as quickly as possible, provide all of the information that the support personnel might need to understand the underlying cause. Run the `collect-support-data` tool, and then send the generated `.zip` file to your authorized support provider.

|   |                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------- |
|   | It is good practice to run this tool and send the `.zip` file to your authorized support provider before you take any corrective action. |

---

---
title: The server has crashed or shut itself down
description: If the server has crashed or shut itself down, first check the current server state by using the bin/server-state command.
component: pingauthorize
version: 11.1
page_id: pingauthorize:troubleshooting_pingauthorize_server:paz_server_crash_shut_down
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/troubleshooting_pingauthorize_server/paz_server_crash_shut_down.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 29, 2023
---

# The server has crashed or shut itself down

If the server has crashed or shut itself down, first check the current server state by using the `bin/server-state` command.

If PingAuthorize Server was previously running but is no longer active, then the potential causes include the following:

* PingAuthorize Server was shut down by an administrator. Unless the server was forcefully terminated (for example, using `kill -9`), then messages are written to the `error` and `server.out` logs explaining the reason for the shutdown.

* PingAuthorize Server was shut down when the underlying system crashed or was rebooted. If this is the case, then running the `uptime` command on the underlying system shows that it was recently booted.

* The PingAuthorize Server process was terminated by the underlying operating system for some reason (for example, the out-of-memory killer on Linux). If this happens, then a message is written to the system error log.

* PingAuthorize Server decided to shut itself down in response to a serious problem. At present, this should only occur if the server has detected that the amount of usable disk space has become critically low, or if significant errors during processing have left the server without any remaining worker threads to process operations. If this happens, then messages are written to the `error` and `server.out` logs (if disk space is available) to provide the reason for the shutdown.

* The JVM in which PingAuthorize Server was running crashed. If this happens, then the JVM should dump a fatal error log (an `hs_err_pid<processID>.log` file) and potentially a core file.

In the event that the operating system itself crashed or terminated the process, then you should work with your operating system vendor to diagnose the underlying problem. If the JVM crashed or the server shut itself down for a reason that is not clear, then contact your authorized support provider for further assistance.

---

---
title: The server is slow to respond to client requests
description: If the server is running and does respond to clients, but clients take a long time to receive responses, then the problem can be attributable to a number of potential problems.
component: pingauthorize
version: 11.1
page_id: pingauthorize:troubleshooting_pingauthorize_server:paz_server_slow_respond_client_requests
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/troubleshooting_pingauthorize_server/paz_server_slow_respond_client_requests.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 18, 2025
---

# The server is slow to respond to client requests

If the server is running and does respond to clients, but clients take a long time to receive responses, then the problem can be attributable to a number of potential problems.

|   |                                                                                                                                                                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | In these cases, use the Periodic Stats Logger, which is a valuable tool to get per-second monitoring information on the server. The Periodic Stats Logger can save the information in `.csv` format for easy viewing in a spreadsheet. For more information, see [About Periodic Stats Loggers](../pingauthorize_server_administration_guide/paz_prof_server_perf_stats.html). |

The potential problems that cause slow responses to client requests are as follows:

* The server is not optimally configured for the type of requests being processed, or clients are requesting inefficient operations.

  If this is the case, then the access log should show that operations are taking a long time to complete and they will likely be unindexed. Updating the server configuration to better suit the requests or altering the requests to make them more efficient could help alleviate the problem.

  Review the expensive operations access log in `logs/expensive-ops`, which by default logs operations that take longer than 1 second. You can also run the `bin/status` command or view the status in the Administrative Console to see the server's `Work Queue` information (also see the following case).

* The server is overwhelmed with client requests and has amassed a large backlog of requests in the work queue.

  This can be the result of a configuration problem (for example, too few worker threads configured), or it can be necessary to provision more systems on which to run the server software. Symptoms of this problem appear similar to those experienced when the server is asked to process inefficient requests, but looking at the details of the requests in the access log show that they are not necessarily inefficient requests.

  Run the `bin/status` command to view the `Work Queue` information. If everything is performing well, you should not see a large queue size or a server that is near 100% busy. The `% Busy` statistic is calculated as the percentage of worker threads that are busy processing operations. For example:

  ```
             --- Work Queue ---
             : Recent : Average : Maximum
  -----------:--------:---------:--------
  Queue Size : 10	 : 1       : 10
  % Busy     : 17     : 14      : 100
  ```

  You can also view the expensive operations access log in `logs/expensive-ops`, which by default logs operations that take longer than 1 second.

* The server is not configured to fully cache all of the data in the server, or the cache is not yet primed.

  In this case, `iostat` reports a very high disk utilization. This can be resolved by configuring the server to fully cache all data and to load database contents into memory on startup. If the underlying system does not have enough memory to fully cache the entire data set, then it might not be possible to achieve optimal performance for operations that need data which is not contained in the cache. Learn more in [Tuning for disk-bound deployments](https://docs.pingidentity.com/pingdirectory/10.3/pingdirectory_server_administration_guide/pd_ds_tune_for_disk_bound_deployments.html).

* If the JVM is not properly configured, then it will need to perform frequent garbage collection and periodically pause execution of the Java code that it is running.

  In that case, the server error log should report that the server has detected a number of pauses and can include tuning recommendations to help alleviate the problem.

* If the server is configured to use a large percentage of the memory in the system, then it is possible that the system has gotten low on available memory and has begun swapping.

  In this case, `iostat` should report very high utilization for disks used to hold swap space, and commands like `cat /proc/meminfo` on Linux can report a large amount of swap memory in use. Another cause of swapping is if swappiness is not set to `0` on Linux. For more information, see [Disabling file system swapping](../installing_and_uninstalling_pingauthorize/paz_prepare_linux_env.html#disable_system_swapping).

* If another process on the system is consuming a significant amount of CPU time, then it can adversely impact the ability of the server to process requests efficiently.

  Isolating the processes (for example, using processor sets) or separating them onto different systems can help eliminate this problem.

---

---
title: The server is unresponsive
description: If the server process is running and appears to be accepting connections, but doesn't respond to requests received on those connections, first check the current server state by using the bin/server-state command.
component: pingauthorize
version: 11.1
page_id: pingauthorize:troubleshooting_pingauthorize_server:paz_server_unresponsive
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/troubleshooting_pingauthorize_server/paz_server_unresponsive.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 24, 2023
---

# The server is unresponsive

If the server process is running and appears to be accepting connections, but doesn't respond to requests received on those connections, first check the current server state by using the `bin/server-state` command.

|   |                                                                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If it appears that the problem is with the server software or the JVM in which it is running, then you need to work with your authorized support provider to fully diagnose the problem and determine the best course of action to correct it. |

If the server is unresponsive, then potential reasons for this behavior include:

* If all worker threads are busy processing other client requests, then new requests that arrive will be forced to wait in the work queue until a worker thread becomes available. If this is the case, then a stack trace obtained using the `jstack` command shows that all of the worker threads are busy and none of them are waiting for new requests to process.

  A dedicated thread pool can be used for processing administrative operations. This thread pool enables diagnosis and corrective action if all other worker threads are processing operations. To request that operations use the administrative thread pool, using the `ldapsearch` command for example, include the `--useAdministrativeSession` option. The requester must have the `use-admin-session` privilege (included for root users). By default, eight threads are available for this purpose. This can be changed with the `num-administrative-session-worker-threads` property in the work queue configuration.

  |   |                                                                                                                                                                                                                                                            |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If all of the worker threads are tied up processing the same operation for a long time, the server will also issue an alert that it might be deadlocked, which might not actually be the case. All threads might be tied up processing unindexed searches. |

* If a request handler is stuck performing some expensive processing for a client connection, then other requests sent to the server on connections associated with that request handler are forced to wait until the request handler is able to read data on those connections. If this is the case, then only some of the connections can experience this behavior (unless there is only a single request handler, in which it will impact all connections), and stack traces obtained using the `jstack` command show that a request handler thread is continuously blocked rather than waiting for new requests to arrive. Note that this scenario is a theoretical problem and one that has not appeared in production.

* If the JVM in which the server is running is not properly configured, then it can be forced to spend a significant length of time performing garbage collection, and in severe cases, could cause significant interruptions in the execution of Java code. In such cases, a stack trace obtained from a `pstack` of the native process should show that most threads are idle, but at least one thread performing garbage collection is active. It is also likely that one or a small number of CPUs are 100% busy while all other CPUs are mostly idle. The server will also issue an alert after detecting a long JVM pause (due to garbage collection). The alert will include details of the pause.

* If the JVM in which the server is running has hung for some reason, then the `pstack` utility should show that one or more threads are blocked and unable to make progress. In such cases, the system CPUs should be mostly idle.

* If a network or firewall configuration problem arises, then attempts to communicate with the server cannot be received by the server. In that case, a network sniffer like `snoop` or `tcpdump` should show that packets sent to the system on which the server is running are not receiving TCP acknowledgement.

* If the system on which the server is running has become hung or lost power with a graceful shutdown, then the behavior is often similar to that of a network or firewall configuration problem.

---

---
title: The server returns error responses to client requests
description: If a large number of client requests are receiving error responses, then review the logs/failed-ops log, which is an access log only for failed operations.
component: pingauthorize
version: 11.1
page_id: pingauthorize:troubleshooting_pingauthorize_server:paz_server_returnes_error_responses_client_requests
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/troubleshooting_pingauthorize_server/paz_server_returnes_error_responses_client_requests.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 28, 2023
---

# The server returns error responses to client requests

If a large number of client requests are receiving error responses, then review the `logs/failed-ops` log, which is an access log only for failed operations.

The potential reasons for the error responses include the following:

* If clients are requesting operations that legitimately should fail (for example, they are targeting entries that do not exist, are attempting to update entries in a way that would violate the server schema, or are performing some other type of inappropriate operation), then the problem is likely with the client and not the server.

* If the PingAuthorize Server work queue is configured with a maximum capacity, and that capacity has been reached, then the server begins rejecting all new requests until space is available in the work queue. In this case, you might need to alter the server configuration, the client requests, or both so that they can be processed more efficiently. Alternatively, you might need to add additional server instances to handle some of the workload.

* If an internal error occurs within the server while processing a client request, then the server terminates the connection to the client and logs a message about the problem that occurred. This should not happen under normal circumstances. Contact your authorized support provider for help with diagnosing and correcting the problem.

* If the server has an issue while interacting with the underlying database (for example, an attempt to read from or write to disk failed because of a disk problem or lack of available disk space), then the server can begin returning errors for all attempts to interact with the database. This will continue until you close and re-open the back end and give the database a chance to recover itself. For information about this type of issue, review the `je.info.*` file in the database directory.

---

---
title: The server will not accept client connections
description: If the server does not appear to be accepting connections from clients, you can first check the current server state by using the bin/server-state command.
component: pingauthorize
version: 11.1
page_id: pingauthorize:troubleshooting_pingauthorize_server:paz_server_will_not_accept_client_connections
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/troubleshooting_pingauthorize_server/paz_server_will_not_accept_client_connections.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 24, 2023
---

# The server will not accept client connections

If the server does not appear to be accepting connections from clients, you can first check the current server state by using the `bin/server-state` command.

Potential reasons the server won't accept client connections include the following:

* The server is not running.

* The underlying system on which the server is installed is not running.

* The server is running but is not reachable as a result of a network or firewall configuration problem. If that is the case, then connection attempts should time out rather than be rejected.

* If the server is configured to allow secure communication via SSL or StartTLS, then a problem with the key manager and/or trust manager configuration can cause connections to be rejected. If that is the case, then messages should be written to the server access log for each failed connection attempt.

* If the server has been configured with a maximum allowed number of connections, then it can be that the maximum number of allowed client connections are already established. If that is the case, then messages should be written to the server access log for each rejected connection attempt.

* If the server is configured to restrict access based on the address of the client, then messages should be written to the server access log for each rejected connection attempt.

* If a connection handler encounters a significant error, then it can stop listening for new requests. If this occurs, then a message should be written to the server error log with information about the problem. You can also restart the server to address this condition.

---

---
title: The server will not run setup
description: If the setup tool does not run properly, some of the most common reasons include the following:
component: pingauthorize
version: 11.1
page_id: pingauthorize:troubleshooting_pingauthorize_server:paz_server_will_not_run_setup
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/troubleshooting_pingauthorize_server/paz_server_will_not_run_setup.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 28, 2025
section_ids:
  a-suitable-java-environment-is-not-available: A suitable Java environment is not available
  unexpected-arguments-provided-to-the-jvm: Unexpected arguments provided to the JVM
  the-server-has-already-been-configured-or-used: The server has already been configured or used
---

# The server will not run setup

If the `setup` tool does not run properly, some of the most common reasons include the following:

## A suitable Java environment is not available

The server requires that Java be installed on the system and made available to the server, and it must be installed prior to running `setup`. If the `setup` tool does not detect that a suitable Java environment is available, it will refuse to run.

To ensure that this does not happen, the `setup` tool should be invoked with an explicitly defined value for the *JAVA\_HOME* environment variable that specifies the path to the Java installation that should be used. For example:

```
env JAVA_HOME=/ds/java ./setup
```

If the previous command doesn't solve the issue, the value specified in the provided *JAVA\_HOME* environment variable might have been overridden by another environment variable. In that case, try the following command, which should override any other environment variables that can be set:

```
env UNBOUNDID_JAVA_HOME="/ds/java" UNBOUNDID_JAVA_BIN="" ./setup
```

## Unexpected arguments provided to the JVM

If the `setup` script attempts to launch the `java` command with an invalid set of Java arguments, it might prevent the JVM from starting. By default, no special options are provided to the JVM when running `setup`, but this might not be the case if either the *JAVA\_ARGS* or *UNBOUNDID\_JAVA\_ARGS* environment variable is set. If the `setup` tool displays an error message that indicates that the Java environment could not be started with the provided set of arguments, then invoke the following command before trying to re-run `setup`:

```
unset JAVA_ARGS UNBOUNDID_JAVA_ARGS
```

## The server has already been configured or used

The `setup` tool is only intended to provide the initial configuration for the server. It refuses to run if it detects that the `setup` tool has already been run, or if an attempt has been made to start the server prior to running the `setup` tool. This protects an existing server installation from being inadvertently updated in a manner that could harm an existing configuration or data set.

If the server has been previously used, and if you want to perform a fresh installation, it is recommended that you first remove the existing installation, create a new one, and run `setup` in that new installation. However, if you are confident that there is nothing of value in the existing installation (for example, if a previous attempt to run `setup` failed to complete successfully, but it will refuse to run again), follow these cleanup steps to allow the `setup` program to run:

* Remove the `config/config.ldif` file and replace it with the `config/update/config.ldif.<revision>` file containing the initial configuration.

* Remove any files or subdirectories below the `db` directory if they exist.

* Remove the `config/java.properties` file if it exists.

* Remove the `lib/setup-java-home` script (or `lib\setup-java-home.bat` file on Microsoft Windows) if it exists.

---

---
title: The server will not start
description: If the server does not start, then there are a number of potential causes.
component: pingauthorize
version: 11.1
page_id: pingauthorize:troubleshooting_pingauthorize_server:paz_server_will_not_start
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/troubleshooting_pingauthorize_server/paz_server_will_not_start.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 29, 2025
section_ids:
  the-server-or-other-administrative-tool-is-already-running: The server or other administrative tool is already running
  there-is-not-enough-memory-available: There is not enough memory available
  an-invalid-java-environment-or-jvm-option-was-used: An invalid Java Environment or JVM option was used
  an-invalid-command-line-option-was-provided: An invalid command-line option was provided
  the-server-has-an-invalid-configuration: The server has an invalid configuration
  you-do-not-have-sufficient-permissions: You do not have sufficient permissions
---

# The server will not start

If the server does not start, then there are a number of potential causes.

## The server or other administrative tool is already running

Only a single instance of the server can run at any time from the same installation root. If an instance is already running, then subsequent attempts to start the server will fail. Similarly, some other administrative operations can also prevent the server from being started. In such cases, the attempt to start the server should fail with a message like the following:

```json
{pingauthorize}  Server could not acquire an exclusive lock on file
/{pingauthorize}/locks/server.lock: The exclusive lock requested for file
/{pingauthorize}/locks/server.lock was not granted, which indicates
that another process already holds a shared or exclusive lock on that
file. This generally means that another instance of this server is already
running
```

If the server is not running (and is not in the process of starting up or shutting down), and there are no other tools running that could prevent the server from being started, and the server still believes that it is running, then it is possible that a previously held lock was not properly released. In that case, you can try removing all of the files in the `locks` directory before attempting to start the server.

|   |                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you wish to have multiple instances running at the same time on the same system, then you should create a completely separate installation in another location on the file system. |

## There is not enough memory available

When the server is started, the JVM attempts to allocate all memory that it has been configured to use. If there is not enough free memory available on the system, then the server generates an error message that indicates that the server could not be started with the specified set of arguments.

|   |                                                                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | It's possible that an invalid option was provided to the JVM (as described in the following potential causes), but if that same set of JVM arguments has already been used successfully to run the server, then it is more likely that the system does not have enough memory available. |

There are a number of potential causes for this issue:

* If the amount of memory in the underlying system has changed (for example, system memory has been removed, or the server is running in a zone, or other type of virtualized container, and a change has been made to the amount of memory that container is allowed to use), then the server might need to be re-configured to use a smaller amount of memory than had been previously configured.

* Another process running on the system is consuming a significant amount of memory, so that there is not enough free memory available to start the server. If this is the case, then either terminate the other process to make more memory available for the server, or reconfigure the server to reduce the amount of memory that it attempts to use.

* The server was just shut down and an attempt was made to immediately restart it. In some cases, if the server is configured to use a significant amount of memory, then it can take a few seconds for all of the memory that had been in use by the server, when it was previously running, to be released back to the operating system. In that case, run the `vmstat` command and wait until the amount of free memory stops growing before attempting to restart the server.

* If the system is configured with one or more memory-backed file systems, verify whether any large files might be consuming a significant amount of memory in any of those locations. If so, remove them or relocate them to a disk-based file system.

* For Linux systems only, there could be a mismatch between the huge pages setting for the JVM and the huge pages reserved in the operating system.

|   |                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If nothing else works, and there is still not enough free memory to allow the JVM to start, then as a last resort, try rebooting the system. |

## An invalid Java Environment or JVM option was used

If an attempt to start the server fails with an error message indicating that no valid Java environment could be found, or indicates that the Java environment could not be started with the configured set of options, then you should first ensure that enough memory is available on the system as described previously. If there is a sufficient amount of memory available, then other causes for this error can include the following:

* The Java installation that was previously used to run the server no longer exists (for example, an updated Java environment was installed and the old installation was removed). In that case, update the `config/java.properties` file to reference to path to the new Java installation and run the `bin/dsjavaproperties` command to apply that change.

* The Java installation used to run the server has been updated, and the server is trying to use the correct Java installation, but one or more of the options that had worked with the previous Java version no longer work with the new version. In that case, it is recommended that the server be re-configured to use the previous Java version, so that it can be run while investigating which options should be used with the new installation.

* If an *UNBOUNDID\_JAVA\_HOME* or *UNBOUNDID\_JAVA\_BIN* environment variable is set, then its value might override the path to the Java installation used to run the server as defined in the `config/java.properties` file. Similarly, if an *UNBOUNDID\_JAVA\_ARGS* environment variable is set, then its value might override the arguments provided to the JVM. If this is the case, then explicitly unset the *UNBOUNDID\_JAVA\_HOME*, *UNBOUNDID\_JAVA\_BIN*, and *UNBOUNDID\_JAVA\_ARGS* environment variables before trying to start the server.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Any time the `config/java.properties` file is updated, the `bin/dsjavaproperties` tool must be run to apply the new configuration. If a problem with the previous Java configuration prevents the `bin/dsjavaproperties` tool from running properly, then it can be necessary to remove the `lib/set-java-home` script (or `lib\set-java-home.bat` file on Microsoft Windows) and invoke the `bin/dsjavaproperties` tool with an explicitly-defined path to the Java environment, as in the following example:```
env UNBOUNDID_JAVA_HOME=/{pingauthorize}/java bin/dsjavaproperties
``` |

## An invalid command-line option was provided

You might provide a small number of arguments when running the `bin/start-server` command, but in most cases, none are required. If you provided one or more command-line arguments for the `bin/start-server` command, and any one of them is not recognized, then the server provides an error message indicating that an argument was not recognized and displays version information. In that case, correct or remove the invalid argument and try to start the server again.

## The server has an invalid configuration

If you make a change to the server configuration using an officially-supported tool like `dsconfig` or the administrative console, the server should validate that configuration change before applying it. However, it is possible that a configuration change can appear to be valid at the time that it is applied but does not work as expected when the server is restarted. Alternately, a change in the underlying system can cause a previously-valid configuration to become invalid.

In most cases involving an invalid configuration, the server displays (and writes to the error log) a message that explains the problem. This might be sufficient to identify the problem and understand what action needs to be taken to correct it. If the startup failure does not provide enough information to identify the problem with the configuration, then look in the `logs/config-audit.log` file to see what recent configuration changes have been made with the server online, or in the `config/archived-configs` directory to see if there might have been a recent configuration change resulting from a direct change made to the configuration file itself, rather than through a supported configuration interface.

If the server does not start as a result of a recent invalid configuration change, then it can be possible to start the server using the configuration that was in place the last time that the server started successfully (for example, the last known-good configuration). This can be achieved using the `--useLastKnownGoodConfig` option. For example:

```shell
$ bin/start-server --useLastKnownGoodConfig
```

If it has been a long time since the server was started and a number of configuration changes have been made since that time, then the last known-good configuration can be significantly out of date. In such cases, it can be preferable to manually repair the configuration.

If there is no last known-good configuration, if the server no longer starts with the last known-good configuration, or if the last known-good configuration is significantly out of date, then manually update the configuration by editing the `config/config.ldif` file.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Before editing the `config/config.ldif` file, ensure that the server is offline and make a copy of the existing configuration. You might wish to discuss the configuration change with your authorized support representative before applying it to ensure that you understand the correct change that needs to be made.In addition to manually editing the configuration file, you can look at previous archived configurations to see if the most recent one works. You can also use the `ldif-diff` tool to compare the configurations in the archive to the current configuration and review the differences. |

## You do not have sufficient permissions

The server should only be started by the user or role used to initially install the server. In most cases, if an attempt is made to start the server as a user or role other than the one used to create the initial configuration, the server fails to start, because the user doesn't have sufficient permissions to access files owned by the other user, such as database and log files.

However, if a non-root user installs the server and then the root account starts the server, it becomes impossible for a non-root user to start the server. This is because newly created files are owned by root and can't be written to by other users.

If the server is unintentionally started by root, or if you wish to change the user account that should be used to run the server, change ownership on all files in the server installation so that they are owned by the user or role under which the server should run. For example, if the server should be run as the `ds` user in the `other` group, then run the following command as the root user:

```
chown -R ds:other /ds/the
```

---

---
title: Troubleshooting AWS IAM authentication issues
description: Learn how to fix common errors when setting up AWS IAM authentication for ElastiCache attribute and service caches.
component: pingauthorize
version: 11.1
page_id: pingauthorize:troubleshooting_pingauthorize_server:paz_troubleshoot_aws_iam_auth_issues
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/troubleshooting_pingauthorize_server/paz_troubleshoot_aws_iam_auth_issues.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 25, 2026
section_ids:
  failed-to-generate-iam-auth-token: Failed to generate IAM auth token
  iam-auth-is-incompatible-with-a-static-password: IAM auth is incompatible with a static password
  iam-auth-requires-a-non-blank-username: IAM auth requires a non-blank username
  accessdeniedexception: AccessDeniedException
  unable-to-connect-to-external-redis-cache-wrongpass-version: Unable to connect to external Redis cache (WRONGPASS version)
  unable-to-connect-to-external-redis-cache-no-host-addresses: Unable to connect to external Redis cache (No host addresses)
---

# Troubleshooting AWS IAM authentication issues

Learn how to fix common errors when setting up AWS Identity and Access Management (IAM) authentication for ElastiCache [attribute](../pingauthorize_policy_administration_guide/paz_attr_caching.html) and [service](../pingauthorize_policy_administration_guide/paz_service_caching.html) caches.

You can find more information about ElastiCache IAM authentication in [Configuring Trust Framework attribute caching for development](../pingauthorize_server_administration_guide/paz_tf_attribute_cache_external.html) and [Configuring Trust Framework attribute caching for production](../pingauthorize_server_administration_guide/paz_tf_attribute_cache_embedded.html).

Errors are logged in different locations depending on when they occur and which PDP mode is in use:

* **Startup errors** (incompatible config, failed connection, `AccessDeniedException`):

  * *Embedded PDP mode*: The PingAuthorize Server remains running but raises a `pdp-unavailable` administrative alert. The server records alert and exception details in `logs/errors`. The PDP becomes unavailable for policy evaluation until the issue is resolved.

  * *External PDP mode*: The Policy Editor fails to start and logs errors to `logs/authorize-pe.log`.

* **Runtime errors** (IAM token generation failures during normal operation):

  * *Embedded PDP mode*: The PingAuthorize Server logs these errors to `logs/trace` (the file-based trace logger). You must enable the trace logger to record these messages.

  * *External PDP mode*: The Policy Editor logs these errors to `logs/authorize-pe.log`.

The following sections are organized by error message. Each section contains information about how to identify the problem, what the problem is, and how to solve the problem.

## `Failed to generate IAM auth token`

* Indicators

  * *Embedded PDP mode*: Check `logs/trace`.

  * *External PDP mode*: Check `logs/authorize-pe.log`.

    The message typically appears alongside a `NoCredentialProviders` or similar AWS SDK error.

* Problem

  The AWS SDK couldn't resolve valid credentials to generate the IAM auth token.

* Solution

  Confirm the following, based on your environment:

  * If running on Amazon EKS, confirm that IAM roles for service accounts (IRSA) is configured correctly. The AWS SDK checks for IRSA credentials before falling back to instance profile credentials.

  * If running on Amazon EC2 (outside EKS), confirm that an IAM role or instance profile is attached to the instance or service.

  * If region auto-detection fails, set the `AWS_REGION` environment variable.

## `IAM auth is incompatible with a static password`

* Indicators

  * *Embedded PDP mode*: The PingAuthorize Server records a `pdp-unavailable` alert in `logs/errors`. The server continues running, but the cache is unavailable.

  * *External PDP mode*: The Policy Editor records this error in `logs/authorize-pe.log` and fails to start.

* Problem

  Both a static password and IAM authentication are configured simultaneously.

  * *Embedded PDP mode*: `use-iam-auth` is set to `true` on the external cache, and a `password` is provided.

  * *External PDP mode*: `useIamAuth` is set to `true` in the `options.yml` file's `cacheConfig` and a `password` is provided.

* Solution

  Remove the password.

  * *Embedded PDP mode*: Clear the `password` property on the external attribute cache with `dsconfig` or the admin console.

  * *External PDP mode*: Remove the `password` field from `cacheConfig`.

## `IAM auth requires a non-blank username`

* Indicators

  * *Embedded PDP mode*: The PingAuthorize Server records a `pdp-unavailable` alert in `logs/errors`. The server continues running, but the cache is unavailable.

  * *External PDP mode*: The Policy Editor records this error in `logs/authorize-pe.log` and fails to start.

* Problem

  IAM authentication is enabled, but no username is provided.

  * *Embedded PDP mode*: `use-iam-auth` is set to `true` on the external cache, but `username` is missing or blank.

  * *External PDP mode*: `useIamAuth` is set to `true` in the `options.yml` file's `cacheConfig`, but `username` is missing or blank.

* Solution

  Set `username` to the ElastiCache user ID.

  * *Embedded PDP mode*: Set the `username` property on the external attribute cache with `dsconfig` or the admin console.

  * *External PDP mode*: Set `username` in `cacheConfig`.

## `AccessDeniedException`

* Indicators

  * *Embedded PDP mode*: The PingAuthorize Server records a `pdp-unavailable` alert in `logs/errors`. The server continues running, but the cache is unavailable.

  * *External PDP mode*: The Policy Editor records this error in `logs/authorize-pe.log` and fails to start.

* Problem

  AWS denied the node discovery call because the IAM principal doesn't have the `elasticache:DescribeCacheClusters` permission.

* Solution

  Add the missing permission to the IAM policy and restart the PDP.

## `Unable to connect to external Redis cache` (`WRONGPASS` version)

* Indicators

  * *Embedded PDP mode*: The PingAuthorize Server records a `WRONGPASS` message in `logs/trace` and a `pdp-unavailable` administrative alert in `logs/errors`. The server continues running.

  * *External PDP mode*: The Policy Editor fails to start and records a `WRONGPASS` message in `logs/authorize-pe.log`.

* Problem

  ElastiCache rejected the IAM token because either the IAM principal lacks the `elasticache:Connect` permission or IAM authentication isn't enabled on the ElastiCache user.

* Solution

  Confirm the following, then restart the PDP:

  * The IAM policy covers both the replication group and the user Amazon Resource Names (ARNs).

  * The replication group's user group contains the ElastiCache user, and IAM auth is enabled on that user.

## `Unable to connect to external Redis cache` (No host addresses)

* Indicators

  * *Embedded PDP mode*: The connection error with no host addresses is visible in `logs/trace`, and the PingAuthorize Server records a `pdp-unavailable` administrative alert in `logs/errors`. The server continues running.

  * *External PDP mode*: The Policy Editor fails to start and records the connection error in `logs/authorize-pe.log`.

* Problem

  No cluster nodes were found for the configured replication group ID.

  * *Embedded PDP mode*: Check the `redis-replication-group-id` property on the external attribute cache.

  * *External PDP mode*: Check the `replicationGroupId` value in `cacheConfig`.

* Solution

  Make sure that:

  * The replication group ID is correct for your PDP mode (see previous).

  * The IAM principal has the `elasticache:DescribeCacheClusters` permission in the correct AWS region.

---

---
title: Troubleshooting PingAuthorize Server
description: You can capture diagnostic data to help troubleshoot issues with PingAuthorize Server or a supporting component, such as the Java Virtual Machine (JVM), the operating system, or the hardware.
component: pingauthorize
version: 11.1
page_id: pingauthorize:troubleshooting_pingauthorize_server:paz_troubleshoot_server
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/troubleshooting_pingauthorize_server/paz_troubleshoot_server.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 25, 2025
---

# Troubleshooting PingAuthorize Server

You can capture diagnostic data to help troubleshoot issues with PingAuthorize Server or a supporting component, such as the Java Virtual Machine (JVM), the operating system, or the hardware.

With this data, you can troubleshoot the problem quickly to determine the underlying cause and the best course of action to resolve it.

Learn about troubleshooting decision requests and responses in the following:

* [Visualizing a policy decision response](../pingauthorize_policy_administration_guide/paz_visualize_pol_resp.html)

* [Policy Decision Logger](../pingauthorize_server_administration_guide/paz_enable_detailed_logging.html#policy_decision_logger)

* [Configuring the Decision Response View](../pingauthorize_server_administration_guide/paz_config_decision_response_view.html)