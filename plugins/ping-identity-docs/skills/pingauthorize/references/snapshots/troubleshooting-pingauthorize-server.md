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
