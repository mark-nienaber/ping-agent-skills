---
title: About logs
description: Overview of PingDS log types — access, audit, errors, and server — and the common audit event framework with message formats and filtering.
component: pingds
version: 8.1
page_id: pingds:logging-guide:about-logs
canonical_url: https://docs.pingidentity.com/pingds/8.1/logging-guide/about-logs.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Features", "LDAP", "Troubleshooting"]
section_ids:
  log-common-audit: Access log format
  log-filtering: Access log filtering
---

# About logs

| Type                                                                                                                                                                                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| access log *(tooltip: \<div class="paragraph">&#xA;\<p>A server log tracing the operations the server processes including timestamps, connection information, and information about the operation itself.\</p>&#xA;\</div>)* | Messages about clients accessing the server.Each message includes a datestamp, information about the connection, and information about the operation.DS servers implement access logs for HTTP and LDAP.It is possible to configure multiple access logs at the same time. Do not enable multiple *unfiltered* file-based access loggers for the same protocol, however. This can put significant write load on the disk subsystem for access log files, because every client request results in at least one new log message.                                                                                                                                                                                                                                                                                                                                                                   |
| audit log *(tooltip: \<div class="paragraph">&#xA;\<p>A server access log with changes in LDIF format.\</p>&#xA;\</div>)*                                                                                                    | Records changes to directory data in LDAP Data Interchange Format (LDIF) *(tooltip: \<div class="paragraph">&#xA;\<p>An IETF standard file format for representing LDAP directory content and modifications to directory content. Typically used to import and export LDAP-based directory information.\</p>&#xA;\</div>)*.DS servers implement an audit log as a special type of file-based access log. By default, the server writes messages to `opendj/logs/audit`.For an example, refer to [Enable an audit log](manage-logs.html#log-ldap-audit).                                                                                                                                                                                                                                                                                                                                          |
| errors log *(tooltip: \<div class="paragraph">&#xA;\<p>A server log tracing server events, error conditions, and warnings, categorized and identified by severity.\</p>&#xA;\</div>)*                                        | Messages tracing server events, error conditions, and warnings, categorized and identified by severity.By default, this is a file-based log, written to `opendj/logs/errors`.Messages have the following format:```
[datestamp] category=category severity=severity msgID=ID number msg=message string
```For lists of server messages by category, refer to [Log message reference](../log-reference/index.html).DS error log message severity levels are:- `ERROR` (highest severity)

- `WARNING`

- `NOTICE`

- `INFO`

- `DEBUG` (lowest severity)To log debug-level messages for a category of interest, refer to [Debug-level logging](../maintenance-guide/troubleshooting.html#troubleshoot-enable-debug-logging).Use the external changelog to get notifications about changes to directory data. For details, refer to [Changelog for notifications](../config-guide/changelog.html). |
| Server                                                                                                                                                                                                                       | Messages about server events since startup.This is a file-based log, written to `opendj/logs/server.out`. A `opendj/logs/server.pid` process ID file is also available when the server is running.Messages in this file have the same format as error log messages.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

You configure logging using log publishers. Log publishers determine which messages to publish, where to publish them, and what output format to use.

DS server logging supports extensibility through a common audit event framework. The framework deals with any event you can audit, not only the data updates recorded in a directory audit log. The framework provides log handlers for publishing to local files or to remote systems.

## Access log format

DS servers support a common audit event framework. The log message formats are compatible for all products using the framework. The framework uses transaction IDs to correlate requests as they traverse the platform. This makes it easier to monitor activity and to enrich reports:

* The framework is built on audit event handlers. Audit event handlers can encapsulate their own configurations. Audit event handlers are the same in each product in the Ping Identity Platform. You can plug in custom handlers that comply with the framework without having to upgrade the server.

* The framework includes handlers for logging to local files and to external services.

  Although the framework supports multiple topics, DS software currently supports handling only access events. DS software divides access events into `ldap-access` events and `http-access` events.

* Common audit transaction IDs are not recorded by default. To record transaction IDs in the access logs, configure the DS server to trust them.

LDAP events have the following format:

```none
{
  "eventName": "DJ-LDAP",
  "client": {
    "ip": string,                         // Client IP address
    "port": number                        // Client port number
  },
  "server": {
    "ip": string,                         // Server IP address
    "port": number                        // Server port number
  },
  "request": {                            // LDAP request
    "attrs": [ string ],                  // Requested attributes
    "authType": string,                   // Bind type such as "SIMPLE"
    "connId": number,                     // Connection ID
    "controls": [{                        // Request controls
      "control": string,                  // Control name or OID
      "critical": boolean,                // true, false
      "value": string                     // Base64-encoded
    }],
    "deleteOldRDN": boolean,              // For a modify DN request
    "dn": string,                         // Bind DN
    "filter": string,                     // Search filter
    "idToAbandon": number,                // ID to use to abandon operation
    "message": string,                    // Localized request message
    "modifications": [{                   // Attributes targeted for modification1
      "modification": string,             // Modification type
      "attribute": string,                // Targeted attribute
      "values": [ string ]                // Modification values
    }]
    "msgId": number,                      // Message ID
    "name": string,                       // Operation name
    "newRDN": string,                     // For a modify DN request
    "newSup": string,                     // For a modify DN request
    "oid": string,                        // Operation name or OID
    "operation": string,                  // Examples: "CONNECT", "BIND", "SEARCH", "TLS"
    "opType": "sync",                     // Replication operation
    "protocol": string,                   // "LDAP", "LDAPS"
    "runAs": string,                      // Authorization ID
    "scope": string,                      // Search scope such as "sub"
    "version": string                     // Version "2", "3"
  },
  "response": {
    "additionalItems": object             // Additional information
    "controls": [{                        // Response controls
      "control": string,                  // Control name or OID
      "critical": boolean                 // true, false
    }],
    "elapsedTime": number,                // Total time queuing and processing the request
    "elapsedQueueingTime": number,        // Time the request spent waiting in the queue
    "elapsedProcessingTime": number,      // Time actively processing the request
    "elapsedTimeUnits": string,           // Time unit such as "MILLISECONDS"
    "entrySize": number,                  // Size in bytes of the largest entry
                                          // read from disk while processing
                                          // the operation
    "totalEntriesSize": number,           // Total size in bytes of all entries
                                          // read from disk while processing
                                          // the search operation
    "maskedMessage": string,              // Real, masked result message
    "maskedResult": string,               // Real, masked result code
    "nentries": number,                   // Number of entries returned
    "reason": string,                     // Reason for disconnect
    "status": string,                     // "SUCCESSFUL", "FAILED"
    "statusCode": string                  // For example, "0" for success
  },
  "security": {                           // Connection security, such as TLS handshake data
    "protocol": string,                   // Protocol, such as "TLSv1.3"
    "cipher": string,                     // Cipher suite
    "ssf": number                         // Security strength factor
  },
  "timestamp": string,                    // UTC date
  "transactionId": string,                // Unique ID for the transaction
  "userId": string,                       // User who requested the operation
  "_id": string                           // Unique ID for the operation
}
```

1 When the advanced configuration property for the log publisher `log-modified-attribute-values:true`, DS logs an array of attributes targeted by modification requests. Each item indicates:

* The modification type: `add`, `delete`, `increment`, or `replace`.

* The attribute name.

* The values for the modification, if allowed according to the log publisher configuration.

  Set one of the advanced attributes `exclude-values-of-attributes` or `include-values-of-attributes` to specify which attribute values DS logs.

HTTP events have the following format:

```none
{
  "eventName": "DJ-HTTP",
  "client": {
    "ip": string,                         // Client IP address
    "port": number                        // Client port number
  },
  "server": {
    "ip": string,                         // Server IP address
    "port": number                        // Server port number
  },
  "http": {                               // HTTP request and response
    "request": {
      "secure": boolean,                  // HTTP: false; HTTPS: true
      "method": string,                   // Examples: "GET", "POST", "PUT"
      "path": string,                     // URL
      "queryParameters": map,             // map: { key-string: [ value-string ] }
      "cookies": map                      // map: { key-string: [ value-string ] }
    },
    "response": {
      "headers": map                      // map: { key-string: [ value-string ] }
    }
  },
  "response": {
    "detail": string,                     // Human-readable information
    "elapsedTime": number,                // Total time queuing and processing the request
    "elapsedTimeUnits": string,           // Time unit such as "MILLISECONDS"
    "status": string,                     // "SUCCESSFUL", "FAILED"
    "statusCode": string                  // For example, "0" for success
  },
  "timestamp": string,                    // UTC date
  "transactionId": string,                // Unique ID for the transaction
  "trackingIds": [ string ],              // Unique IDs from the transaction context
  "userId": string,                       // User who requested the operation
  "_id": string                           // Unique ID for the operation
}
```

## Access log filtering

With the default access log configuration (no filtering), for every client application request, the server writes at least one message to its access log. This volume of logging gives you the information to analyze overall access patterns, or to audit access when you do not know in advance what you are looking for.

When you do know what you are looking for, log filtering lets you throttle logging to focus on what you want to read. You specify the criteria for a filtering policy, and apply the policy to a log publisher.

Log filtering policies use the following criteria:

* Client IP address

* Operation type

  * LDAP abandon operation (abandon) *(tooltip: \<div class="paragraph">
    \<p>Stop processing a request in progress and drop the connection without a reply to the client application.\</p>
    \</div>)*

  * LDAP add operation (add) *(tooltip: \<div class="paragraph">
    \<p>Adds a new entry or entries to the directory.\</p>
    \</div>)*

  * LDAP bind operation (bind) *(tooltip: \<div class="paragraph">
    \<p>Authenticates the client application. The server uses the identity to make authorization decisions.\</p>
    \</div>)*

  * LDAP compare operation (compare) *(tooltip: \<div class="paragraph">
    \<p>Compares a specified attribute value with the value stored on an entry in the directory.\</p>
    \</div>)*

  * connect

  * LDAP delete operation (delete) *(tooltip: \<div class="paragraph">
    \<p>Removes an existing entry or entries from the directory.\</p>
    \</div>)*

  * disconnect

  * LDAP extended operation (extended operation) *(tooltip: \<div class="paragraph">
    \<p>An LDAP operation not included in the original standards.\</p>
    \</div>)*

  * LDAP modify operation (modify) *(tooltip: \<div class="paragraph">
    \<p>Changes one or more attributes of an entry.\</p>
    \</div>)*

  * LDAP modify DN operation (rename) *(tooltip: \<div class="paragraph">
    \<p>Changes the distinguished name of an entry.\</p>
    \</div>)*

  * LDAP search operation (search) *(tooltip: \<div class="paragraph">
    \<p>Return entries based on an LDAP filter, a base DN, and a scope.\</p>
    \</div>)*

  * LDAP unbind operation (unbind) *(tooltip: \<div class="paragraph">
    \<p>Release resources at the end of a session.\</p>
    \</div>)*

* Minimum entry size

* Port number

* Protocol used

* Response time, queuing time, and processing time

* Result codes (only log error results, for example)

* Search response criteria (number of entries returned, unindexed search, and others)

* Target DN

* TLS handshakes

* User bind DN and group membership

A log publisher's filtering policy determines whether to include or exclude log messages that match the criteria.

Refer to the examples in [Filter out administrative messages](manage-logs.html#log-filtering-exclude-dsconfig) and [Audit configuration changes](manage-logs.html#log-filtering-audit-config).
