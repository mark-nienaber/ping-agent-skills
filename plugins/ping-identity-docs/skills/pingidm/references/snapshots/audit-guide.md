---
title: Access event topic properties
description: A reference of all properties available in the PingIDM access audit event topic, including request, response, server, and client fields
component: pingidm
version: 8.1
page_id: pingidm:audit-guide:access-event-prop
canonical_url: https://docs.pingidentity.com/pingidm/8.1/audit-guide/access-event-prop.html
llms_txt: https://docs.pingidentity.com/pingidm/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Audit", "Logs", "Access", "Event", "Properties"]
---

# Access event topic properties

| Event Property                 | Description                                                                                                     |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `_id`                          | UUID for the message object, such as `"0419d364-1b3d-4e4f-b769-555c3ca098b0"`.                                  |
| `timestamp`                    | Time that IDM logged the message, in UTC format; for example, `"2020-05-18T08:48:00.160Z"`.                     |
| `eventName`                    | Name of the audit event: `access` for this log.                                                                 |
| `transactionId`                | UUID of the transaction; the same transaction might display for the same event in different audit event topics. |
| `userId`                       | User ID.                                                                                                        |
| `trackingId`                   | A unique value for the object being tracked.                                                                    |
| `server.ip`                    | IP address of the IDM server.                                                                                   |
| `server.port`                  | Port number used by the IDM server.                                                                             |
| `client.ip`                    | Client IP address.                                                                                              |
| `client.port`                  | Client port number.                                                                                             |
| `request.protocol`             | Protocol for request, typically Common REST.                                                                    |
| `request.operation`            | Common REST operation taken on the object; for example, UPDATE, DELETE, or ACTION.                              |
| `request.detail`               | Typically, details for an ACTION request.                                                                       |
| `http.request.secure`          | Boolean for request security.                                                                                   |
| `http.request.method`          | HTTP method requested by the client.                                                                            |
| `http.request.path`            | Path of the HTTP request.                                                                                       |
| `http.request.queryParameters` | Parameters sent in the HTTP request, such as a key/value pair.                                                  |
| `http.request.headers`         | HTTP headers for the request (optional).                                                                        |
| `http.request.cookies`         | HTTP cookies for the request (optional).                                                                        |
| `http.response.headers`        | HTTP response headers (optional).                                                                               |
| `response.status`              | Normally, SUCCESSFUL, FAILED, or null.                                                                          |
| `response.statusCode`          | SUCCESS in `response.status` leads to a null `response.statusCode`; FAILURE leads to a 400-level error.         |
| `response.detail`              | Message associated with `response.statusCode`, such as Not Found or Internal Server Error.                      |
| `response.elapsedTime`         | Time to execute the access event.                                                                               |
| `response.elapsedTimeUnits`    | Units for response time.                                                                                        |
| `roles`                        | IDM roles associated with the request.                                                                          |
