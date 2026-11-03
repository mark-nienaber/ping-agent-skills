---
title: Advanced HTTP event logging
description: Configure advanced HTTP event logging in the PingAuthorize Server to trace the full HTTP request lifecycle and diagnose performance slowdowns.
component: pingauthorize
version: 11.1
page_id: pingauthorize:troubleshooting_pingauthorize_server:paz_advanced_http_logging_monitoring
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/troubleshooting_pingauthorize_server/paz_advanced_http_logging_monitoring.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-06T00:00:00Z
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
description: Review common PingAuthorize Server problems and their potential solutions.
component: pingauthorize
version: 11.1
page_id: pingauthorize:troubleshooting_pingauthorize_server:paz_common_probs_potential_sols
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/troubleshooting_pingauthorize_server/paz_common_probs_potential_sols.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-05T00:00:00Z
---

# Common problems and potential solutions

This section describes a number of different types of problems that can occur and common potential causes for them.

---

---
title: Conditions for automatic server shutdown
description: Review a list of conditions that trigger the PingAuthorize Server to shut down automatically.
component: pingauthorize
version: 11.1
page_id: pingauthorize:troubleshooting_pingauthorize_server:paz_conditions_auto_server_shutdown
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/troubleshooting_pingauthorize_server/paz_conditions_auto_server_shutdown.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-05T00:00:00Z
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
description: Configure the PingAuthorize Server to detect expensive HTTP threads and generate thread dumps to help diagnose performance bottlenecks.
component: pingauthorize
version: 11.1
page_id: pingauthorize:troubleshooting_pingauthorize_server:paz_detecting_expensive_threads
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/troubleshooting_pingauthorize_server/paz_detecting_expensive_threads.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-05T00:00:00Z
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
description: Troubleshoot the PingAuthorize Server using logs, system commands, the periodic stats logger, and the status and collect-support-data tools.
component: pingauthorize
version: 11.1
page_id: pingauthorize:troubleshooting_pingauthorize_server:paz_general_troubleshoot_method
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/troubleshooting_pingauthorize_server/paz_general_troubleshoot_method.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-05T00:00:00Z
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
description: Access JVM diagnostic information from the PingAuthorize Server, including crash dump files.
component: pingauthorize
version: 11.1
page_id: pingauthorize:troubleshooting_pingauthorize_server:paz_java_diagnostic_info
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/troubleshooting_pingauthorize_server/paz_java_diagnostic_info.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-05T00:00:00Z
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
description: Use Java Development Kit tools such as jps, jstack, jmap, jhat, and jstat to troubleshoot Java applications.
component: pingauthorize
version: 11.1
page_id: pingauthorize:troubleshooting_pingauthorize_server:paz_java_troubleshoot_tools
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/troubleshooting_pingauthorize_server/paz_java_troubleshoot_tools.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-05T00:00:00Z
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
title: Problems with the admin console
description: Troubleshoot problems with the PingAuthorize Server admin console, including startup failures and authentication errors.
component: pingauthorize
version: 11.1
page_id: pingauthorize:troubleshooting_pingauthorize_server:paz_problems_admin_console
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/troubleshooting_pingauthorize_server/paz_problems_admin_console.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-05T00:00:00Z
---

# Problems with the admin console

To troubleshoot problems with the admin console, consider these potential causes:

* The web application container used to host the console isn't running. If an error occurs while trying to start it, consult the logs for the web application container.

* If a problem occurs while trying to authenticate to the web application container, make sure the target PingAuthorize Server is online. If it is online, the access log might provide information about the reasons for the authentication failure.

---

---
title: The server has crashed or shut itself down
description: Diagnose why the PingAuthorize Server crashed or shut down unexpectedly.
component: pingauthorize
version: 11.1
page_id: pingauthorize:troubleshooting_pingauthorize_server:paz_server_crash_shut_down
canonical_url: https://docs.pingidentity.com/pingauthorize/11.1/troubleshooting_pingauthorize_server/paz_server_crash_shut_down.html
llms_txt: https://docs.pingidentity.com/pingauthorize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-05T00:00:00Z
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