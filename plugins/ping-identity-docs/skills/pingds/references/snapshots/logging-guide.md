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

---

---
title: Log HTTP access to files
description: Configure PingDS HTTP access logging in JSON format or the W3C extended log format, including field configuration and transaction ID tracking.
component: pingds
version: 8.1
page_id: pingds:logging-guide:http-access
canonical_url: https://docs.pingidentity.com/pingds/8.1/logging-guide/http-access.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["REST API", "Troubleshooting"]
section_ids:
  log-common-audit-http-json: JSON format
  log-http-access: Standard HTTP format
---

# Log HTTP access to files

## JSON format

When you install DS using procedures from [Installation](../install-guide/preface.html), the default JSON-based HTTP access log file is `logs/http-access.audit.json`. The name of the access log publisher in the configuration is `Json File-Based HTTP Access Logger`.

The sample DS Docker image logs to standard output instead of files. This makes it easy to read log messages with the `docker logs` command, and is a pattern you should follow when creating your own DS Docker images. The name of the LDAP access log publisher configuration in the sample image is `Console HTTP Access Logger`:

1. Decide whether to trust transaction IDs sent by client applications, used to correlate requests as they traverse multiple servers.

   Client applications using the common audit event framework send transaction IDs with their requests. The transaction IDs correlate audit events, tracing the request through multiple applications.

   Transaction IDs are sent over LDAP using an internal DS request control. They are sent over HTTP in an HTTP header.

   By default, DS servers do not trust transaction IDs sent with client application requests.

   When a server trusts transaction IDs from client application requests, outgoing requests reuse the incoming ID. For each outgoing request in the transaction, the request's transaction ID has the form `original-transaction-id/sequence-number`, where sequence-number reflects the position of the request in the series of requests for this transaction. For example, if the original-transaction-id is `abc123`, the first outgoing request has the transaction ID `abc123/0`, the second `abc123/1`, the third `abc123/2`, and so on. This lets you distinguish specific requests within a transaction when correlating audit events from multiple services.

   To trust transactions, set the advanced global server property, `trust-transaction-ids:true`:

   ```console
   $ dsconfig \
    set-global-configuration-prop \
    --advanced \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --set trust-transaction-ids:true \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

2. Edit the default HTTP access log publisher as necessary.

   The following example enables the default log publisher for DS installed locally, not in a Docker image:

   ```console
   $ dsconfig \
    set-log-publisher-prop \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --publisher-name "Json File-Based HTTP Access Logger" \
    --set enabled:true \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

## Standard HTTP format

For HTTP requests, you can configure an access logger that uses the [Extended Log File Format](https://www.w3.org/TR/WD-logfile.html), a W3C working draft. The default log file is `logs/http-access`:

1. Enable the standard format HTTP access logger:

   ```console
   $ dsconfig \
    set-log-publisher-prop \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --publisher-name "File-Based HTTP Access Logger" \
    --set enabled:true \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

   The following example shows an excerpt of an HTTP access log with space reformatted:

   ```none
   - <client-ip> bjensen  <datestamp> GET  /users/bjensen HTTP/1.1 200 <user-agent> 3  40
   - <client-ip> bjensen  <datestamp> GET  /users/scarter HTTP/1.1 200 <user-agent> 4   9
   - <client-ip> -        <datestamp> GET  /users/missing HTTP/1.1 401 <user-agent> 5   0
   - <client-ip> kvaughan <datestamp> POST /users         HTTP/1.1 200 <user-agent> 6 120
   ```

   Missing values are replaced with `-`. Tabs separate the fields, and if a field contains a tab character, then the field is surrounded with double quotes. DS software repeats double quotes in the field to escape them.

   Configure the `log-format` property to set the fields. The default fields are shown here in the order they occur in the log file:

   | Field              | Description                                                                                                                                                                                                                                                                                   |
   | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | `cs-host`          | Client hostname.                                                                                                                                                                                                                                                                              |
   | `c-ip`             | Client IP address.                                                                                                                                                                                                                                                                            |
   | `cs-username`      | Username used to authenticate.                                                                                                                                                                                                                                                                |
   | `x-datetime`       | Completion timestamp for the HTTP request.Configure with the `log-record-time-format` property.                                                                                                                                                                                               |
   | `cs-method`        | HTTP method requested by the client.                                                                                                                                                                                                                                                          |
   | `cs-uri`           | URI requested by the client.                                                                                                                                                                                                                                                                  |
   | `cs-uri-stem`      | URL-encoded path requested by the client.                                                                                                                                                                                                                                                     |
   | `cs-uri-query`     | URL-encoded query parameter string requested by the client.                                                                                                                                                                                                                                   |
   | `cs-version`       | HTTP version requested by the client.                                                                                                                                                                                                                                                         |
   | `sc-status`        | HTTP status code for the operation.                                                                                                                                                                                                                                                           |
   | `cs(User-Agent)`   | User-Agent identifier.                                                                                                                                                                                                                                                                        |
   | `x-connection-id`  | Connection ID used for DS internal operations.When using this field to match HTTP requests with internal operations in the LDAP access log, set the access log advanced property, `suppress-internal-operations:false`. By default, internal operations do not appear in the LDAP access log. |
   | `x-etime`          | Execution time in milliseconds needed by DS to service the HTTP request.                                                                                                                                                                                                                      |
   | `x-transaction-id` | The common audit event framework transaction ID for the request.This defaults to `0`, unless you configure the server to trust transaction IDs.                                                                                                                                               |

   The following additional fields are supported:

   | Field            | Description                         |
   | ---------------- | ----------------------------------- |
   | `c-port`         | Client port number.                 |
   | `s-computername` | Server name writing the access log. |
   | `s-ip`           | Server IP address.                  |
   | `s-port`         | Server port number.                 |

---

---
title: Log LDAP access to files
description: Configure PingDS LDAP access logging in JSON, filtered JSON, or backwards-compatible format, including logging modifications to directory entries.
component: pingds
version: 8.1
page_id: pingds:logging-guide:ldap-access
canonical_url: https://docs.pingidentity.com/pingds/8.1/logging-guide/ldap-access.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["LDAP", "Troubleshooting"]
section_ids:
  log-common-audit-ldap-json: JSON format
  log-common-audit-filtered-ldap-json: Filtered JSON format
  log-common-audit-ldap-json-mods: Log modifications
  log-ldap-access: Backwards-compatible format
---

# Log LDAP access to files

## JSON format

When you install DS using procedures from [Installation](../install-guide/preface.html), the primary JSON-based LDAP access log file is `logs/ldap-access.audit.json`. The name of the access log publisher in the configuration is `Json File-Based Access Logger`.

The sample DS Docker image logs to standard output instead of files. This makes it easy to read log messages with the `docker logs` command, and is a pattern you should follow when creating your own DS Docker images. The name of the External LDAP access log publisher configuration in the sample image is `Console LDAP Access Logger`.

Primary access logs include messages for each LDAP operation. They can grow quickly, but are particularly useful for analyzing overall client behavior:

1. Decide whether to trust transaction IDs sent by client applications, used to correlate requests as they traverse multiple servers.

   Client applications using the common audit event framework send transaction IDs with their requests. The transaction IDs correlate audit events, tracing the request through multiple applications.

   Transaction IDs are sent over LDAP using an internal DS request control. They are sent over HTTP in an HTTP header.

   By default, DS servers do not trust transaction IDs sent with client application requests.

   When a server trusts transaction IDs from client application requests, outgoing requests reuse the incoming ID. For each outgoing request in the transaction, the request's transaction ID has the form `original-transaction-id/sequence-number`, where sequence-number reflects the position of the request in the series of requests for this transaction. For example, if the original-transaction-id is `abc123`, the first outgoing request has the transaction ID `abc123/0`, the second `abc123/1`, the third `abc123/2`, and so on. This lets you distinguish specific requests within a transaction when correlating audit events from multiple services.

   To trust transactions, set the advanced global server property, `trust-transaction-ids:true`:

   ```console
   $ dsconfig \
    set-global-configuration-prop \
    --advanced \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --set trust-transaction-ids:true \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

2. Edit the default access log publisher as necessary.

   The following example applies the default settings for DS installed locally, not in a Docker image:

   ```console
   $ dsconfig \
    set-log-publisher-prop \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --publisher-name "Json File-Based Access Logger" \
    --set enabled:true \
    --add "rotation-policy:24 Hours Time Limit Rotation Policy" \
    --add "rotation-policy:Size Limit Rotation Policy" \
    --set "retention-policy:File Count Retention Policy" \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

## Filtered JSON format

DS servers write messages to a filtered access log file, `logs/filtered-ldap-access.audit.json`. This log grows more slowly than the primary access log. It includes only messages about the following:

* Administrative requests related to backing up and restoring data, scheduling tasks, and reading and writing configuration settings

* Authentication failures

* Requests from client applications that are misbehaving

* Requests that take longer than one second for the server to process

* Search requests that return more than 1000 entries

* Unindexed searches

Follow these steps to change the configuration:

1. Edit the filtered access log publisher as necessary.

   The following example updates the configuration to hide controls in log records:

   ```console
   $ dsconfig \
    set-log-publisher-prop \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --publisher-name "Filtered Json File-Based Access Logger" \
    --set log-controls:false \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

2. Edit the filtering criteria as necessary.

   The following commands list the relevant default filtering criteria settings for the filtered access log:

   ```none
   $ dsconfig \
    get-access-log-filtering-criteria-prop \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --publisher-name "Filtered Json File-Based Access Logger" \
    --criteria-name "Administrative Requests" \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   log-record-type                        : add, bind, compare, delete, extended,
                                          : modify, rename, search
   request-target-dn-equal-to             : "**,cn=config", "**,cn=tasks",
                                          : cn=config, cn=tasks

   $ dsconfig \
    get-access-log-filtering-criteria-prop \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --publisher-name "Filtered Json File-Based Access Logger" \
    --criteria-name "Auth Failures" \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   log-record-type                        : add, bind, compare, delete, extended,
                                          : modify, rename, search
   response-result-code-equal-to          : 7, 8, 13, 48, 49, 50, 123

   $ dsconfig \
    get-access-log-filtering-criteria-prop \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --publisher-name "Filtered Json File-Based Access Logger" \
    --criteria-name "Long Requests" \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   log-record-type                        : add, bind, compare, delete, extended,
                                          : modify, rename, search
   response-etime-greater-than            : 1000

   $ dsconfig \
    get-access-log-filtering-criteria-prop \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --publisher-name "Filtered Json File-Based Access Logger" \
    --criteria-name "Misbehaving Clients" \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   log-record-type                        : add, bind, compare, delete, extended,
                                          : modify, rename, search
   response-result-code-equal-to          : 1, 2, 17, 18, 19, 21, 34, 60, 61, 64,
                                          : 65, 66, 67, 69

   $ dsconfig \
    get-access-log-filtering-criteria-prop \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --publisher-name "Filtered Json File-Based Access Logger" \
    --criteria-name "Searches Returning 1000+ Entries" \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   log-record-type                        : search
   search-response-nentries-greater-than  : 1000

   $ dsconfig \
    get-access-log-filtering-criteria-prop \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --publisher-name "Filtered Json File-Based Access Logger" \
    --criteria-name "Unindexed Searches" \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   log-record-type                        : search
   search-response-is-indexed             : false
   ```

   For details about the LDAP result codes listed in the criteria, refer to [LDAP result codes](../ldap-reference/ldap-result-codes.html).

   For details about how filtering works, refer to [Access log filtering](about-logs.html#log-filtering).

## Log modifications

You can configure a DS log publisher for JSON-based or Console LDAP access logs to record the attributes targeted by modification requests.

The following example enables the default `Json File-Based Access Logger` to log modifications in its log file, `logs/ldap-access.audit.json`:

```console
$ dsconfig \
 set-log-publisher-prop \
 --publisher-name "Json File-Based Access Logger" \
 --set log-modified-attribute-values:true \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
```

The example uses the default settings for the related advanced properties:

* `exclude-values-of-attributes` includes `authPassword` and `userPassword` to avoid logging hashed passwords.

* `include-values-of-attributes` isn't set.

When a client application requests a modification, DS includes the modifications in the audit event message `request` object. The following example shows an extract of the audit event message for a request changing Babs's `description` to `New description`:

```json
{
  "request": {
    "protocol": "LDAPS",
    "operation": "MODIFY",
    "dn": "uid=bjensen,ou=people,dc=example,dc=com",
    "modifications": [{
      "modification": "replace",
      "attribute": "description",
      "values": ["New description"]
    }]
  }
}
```

## Backwards-compatible format

|   |                                                          |
| - | -------------------------------------------------------- |
|   | The interface stability of this feature is *Deprecated*. |

This access log format was the default for older DS servers. Use this log format if you already have software configured to consume that format. The default log file is `logs/access`:

1. Enable the LDAP access logger:

   ```console
   $ dsconfig \
    set-log-publisher-prop \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --publisher-name "File-Based Access Logger" \
    --set enabled:true \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

   By default, this access log contains a message for each request, and a message for each response. It also includes messages for connection and disconnection.

   Write messages only on responses by setting the `log-format:combined` property. The setting is useful when filtering messages based on response criteria. It causes the server to log one message per operation, rather than one for each request and response.

---

---
title: Logging
description: Overview of PingDS server logging, covering log types and options for HTTP access and LDAP access logging.
component: pingds
version: 8.1
page_id: pingds:logging-guide:preface
canonical_url: https://docs.pingidentity.com/pingds/8.1/logging-guide/preface.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Troubleshooting"]
page_aliases: ["index.adoc"]
---

# Logging

These pages cover DS server logs and logging options.

[icon: copy, set=fas, size=3x]

#### [Logs](about-logs.html)

Understand server logs.

[icon: cloud, set=fas, size=3x]

#### [HTTP](http-access.html)

Configure HTTP logs.

[icon: sitemap, set=fas, size=3x]

#### [LDAP](ldap-access.html)

Configure LDAP logs.

---

---
title: Manage logs
description: Configure PingDS log output to stdout or JSON, rotate and retain log files, enable audit logs, filter log messages, and set up tamper-evident logging.
component: pingds
version: 8.1
page_id: pingds:logging-guide:manage-logs
canonical_url: https://docs.pingidentity.com/pingds/8.1/logging-guide/manage-logs.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["LDAP", "REST API", "Troubleshooting", "Setup &amp; Configuration"]
section_ids:
  log-common-audit-stdout: Log access to standard output
  log-error-stdout: Log errors to standard output
  log-error-json: Log error messages as JSON
  log-rotation: Rotate and retain logs
  log-ldap-audit: Enable an audit log
  log-filtering-exclude-dsconfig: Filter out administrative messages
  log-filtering-audit-config: Audit configuration changes
  log-common-audit-whitelist: Allow log message fields
  log-common-audit-blacklist: Deny log message fields
  log-common-audit-keystore: Make tampering evident
---

# Manage logs

## Log access to standard output

This procedure applies only to Common Audit file-based logs, and when you install DS using procedures from [Installation](../install-guide/preface.html).

The sample DS Docker image creates these console access loggers by default:

* `Console LDAP Access Logger`

* `Console HTTP Access Logger`

A JSON stdout handler sends messages to standard output.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Only use this logger when running the server with `start-ds --noDetach`.When running as a daemon without the `--noDetach` option, the server also logs the messages to the file, `/path/to/opendj/logs/server.out`. The server has no mechanism for rotating or removing the `server.out` log file, which is only cleared when the server starts.As a result, using the JSON stdout handler when running the server without the `--noDetach` option can cause the server to eventually run out of disk space. |

1. Decide whether to trust transaction IDs sent by client applications, used to correlate requests as they traverse multiple servers.

   Client applications using the common audit event framework send transaction IDs with their requests. The transaction IDs correlate audit events, tracing the request through multiple applications.

   Transaction IDs are sent over LDAP using an internal DS request control. They are sent over HTTP in an HTTP header.

   By default, DS servers do not trust transaction IDs sent with client application requests.

   When a server trusts transaction IDs from client application requests, outgoing requests reuse the incoming ID. For each outgoing request in the transaction, the request's transaction ID has the form `original-transaction-id/sequence-number`, where sequence-number reflects the position of the request in the series of requests for this transaction. For example, if the original-transaction-id is `abc123`, the first outgoing request has the transaction ID `abc123/0`, the second `abc123/1`, the third `abc123/2`, and so on. This lets you distinguish specific requests within a transaction when correlating audit events from multiple services.

   To trust transactions, set the advanced global server property, `trust-transaction-ids:true`:

   ```console
   $ dsconfig \
    set-global-configuration-prop \
    --advanced \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --set trust-transaction-ids:true \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

2. Create one or more external JSON configuration files for the handler:

   1. For HTTP access log messages, save the following in `opendj/config/audit-handlers/hdap-access-stdout.json`

      ```json
      {
        "class": "org.forgerock.audit.handlers.json.stdout.JsonStdoutAuditEventHandler",
        "config": {
          "enabled": true,
          "name": "http.access.stdout",
          "elasticsearchCompatible": false,
          "topics": ["http-access"]
        }
      }
      ```

   2. For LDAP access log messages, save the following in `opendj/config/audit-handlers/ldap-access-stdout.json`

      ```json
      {
        "class": "org.forgerock.audit.handlers.json.stdout.JsonStdoutAuditEventHandler",
        "config": {
          "enabled": true,
          "name": "ldap.access.stdout",
          "elasticsearchCompatible": false,
          "topics": ["ldap-access"]
        }
      }
      ```

   The `"elasticsearchCompatible"` setting has this effect:

   * When `false`, the message ID field is named `_id`.

   * When `true`, the message ID field is named `_eventId`.

3. Create log publisher configurations for the access logs:

   1. Use this log publisher configuration for HTTP access logging:

      ```console
      $ dsconfig \
       create-log-publisher \
       --publisher-name "Console HTTP Access Logger" \
       --type external-http-access \
       --set enabled:true \
       --set config-file:config/audit-handlers/hdap-access-stdout.json \
       --hostname localhost \
       --port 4444 \
       --bindDN uid=admin \
       --bindPassword password \
       --trustStorePath /path/to/opendj/config/keystore \
       --trustStoreType PKCS12 \
       --trustStorePassword:file /path/to/opendj/config/keystore.pin \
       --no-prompt
      ```

   2. Use this log publisher configuration for LDAP access logging:

      ```console
      $ dsconfig \
       create-log-publisher \
       --publisher-name "Console LDAP Access Logger" \
       --type external-access \
       --set enabled:true \
       --set config-file:config/audit-handlers/ldap-access-stdout.json \
       --hostname localhost \
       --port 4444 \
       --bindDN uid=admin \
       --bindPassword password \
       --trustStorePath /path/to/opendj/config/keystore \
       --trustStoreType PKCS12 \
       --trustStorePassword:file /path/to/opendj/config/keystore.pin \
       --no-prompt
      ```

## Log errors to standard output

A `console-error` logger sends messages to standard output.

This procedure applies only when you install DS using procedures from [Installation](../install-guide/preface.html). The sample DS Docker image creates a `Console Error Logger` by default.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Only use this logger when running the server with `start-ds --noDetach`.When running as a daemon without the `--noDetach` option, the server also logs the messages to the file, `/path/to/logs/server.out`. The server has no mechanism for rotating or removing the `server.out` log file, which is only cleared when the server starts.As a result, using the JSON stdout handler when running the server without the `--noDetach` option can cause the server to eventually run out of disk space. |

1. Switch to a `console-error` logger while the server is offline:

   ```console
   $ stop-ds
   $ dsconfig \
    delete-log-publisher \
    --publisher-name "File-Based Error Logger" \
    --offline \
    --configFile /path/to/opendj/config/config.ldif \
    --no-prompt
   $ dsconfig \
    create-log-publisher \
    --type console-error \
    --publisher-name "Console Error Logger" \
    --set enabled:true \
    --set default-severity:notice \
    --set override-severity:SYNC=INFO \
    --offline \
    --configFile /path/to/opendj/config/config.ldif \
    --no-prompt
   $ start-ds --noDetach
   ```

## Log error messages as JSON

By default, error log messages start with a timestamp, followed by space-separated `field=value` pairs, where the last `msg` field contains free-form text. The format is human-readable, but can be less convenient to parse than standard JSON.

You can set the error log publisher property `json-output:true` to cause the publisher to generate JSON messages:

1. Stop DS.

2. Move existing, free-form text error log files.

3. Change to JSON output.

   The following command changes the default error log publisher configuration while DS is stopped:

   ```console
   $ dsconfig \
    set-log-publisher-prop \
    --publisher-name "File-Based Error Logger" \
    --set json-output:true \
    --offline \
    --configFile /path/to/opendj/config/config.ldif \
    --no-prompt
   ```

4. Start DS.

## Rotate and retain logs

Each file-based log has a rotation policy and a retention policy.

The rotation policy specifies when to rotate a log file based on a time, log file age, or log file size. Rotated logs have a rotation timestamp appended to their name.

The retention policy specifies whether to retain logs based on the number of logs, their size, or how much free space should be left on the disk.

1. List log rotation policies:

   ```console
   $ dsconfig \
    list-log-rotation-policies \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

   > **Collapse: Show output**
   >
   > ```
   > Log Rotation Policy                 : Type       : file-size-limit : rotation-interval : time-of-day
   > ------------------------------------:------------:-----------------:-------------------:------------
   > 24 Hours Time Limit Rotation Policy : time-limit : -               : 1 d               : -
   > 7 Days Time Limit Rotation Policy   : time-limit : -               : 1 w               : -
   > Fixed Time Rotation Policy          : fixed-time : -               : -                 : 2359
   > Size Limit Rotation Policy          : size-limit : 100 mb          : -                 : -
   > ```

2. List log retention policies:

   ```console
   $ dsconfig \
    list-log-retention-policies \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

   > **Collapse: Show output**
   >
   > ```
   > Log Retention Policy             : Type            : disk-space-used : free-disk-space : number-of-files
   > ---------------------------------:-----------------:-----------------:-----------------:----------------
   > File Count Retention Policy      : file-count      : -               : -               : 10
   > Free Disk Space Retention Policy : free-disk-space : -               : 500 mb          : -
   > Size Limit Retention Policy      : size-limit      : 500 mb          : -               : -
   > ```

3. View the policies that apply to a given log with the `dsconfig get-log-publisher-prop` command.

   The following example shows that the server keeps 10 access log files, rotating either each day or when the log size reaches 100 MB:

   ```console
   $ dsconfig \
    get-log-publisher-prop \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --publisher-name "Json File-Based Access Logger" \
    --property retention-policy \
    --property rotation-policy \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

   > **Collapse: Show output**
   >
   > ```
   > Property         : Value(s)
   > -----------------:----------------------------------------------------------------
   > retention-policy : File Count Retention Policy
   > rotation-policy  : 24 Hours Time Limit Rotation Policy, Size Limit Rotation Policy
   > ```

4. Use the `dsconfig` command to create, update, delete, and assign log rotation and retention policies. Set the policy that applies to a logger with the `dsconfig set-log-publisher-prop` command.

|   |                                                                                                                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When using access logs based on the common audit event framework, you can only configure one of each type of retention or rotation policy.This means you can configure only one file count, free disk space, and size limit log retention policy. You can configure only one fixed time, size limit, and time limit log rotation policy. |

## Enable an audit log

1. Enable a file-based audit logger:

   ```console
   $ dsconfig \
    set-log-publisher-prop \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --publisher-name "File-Based Audit Logger" \
    --set enabled:true \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

2. Wait for, or make a change to directory data.

   The following example changes a description:

   ```console
   $ ldapmodify \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN "uid=bjensen,ou=People,dc=example,dc=com" \
    --bindPassword hifalutin << EOF
   dn: uid=bjensen,ou=People,dc=example,dc=com
   changetype: modify
   replace: description
   description: New description
   EOF
   ```

   The audit log records the changes as shown in the following excerpt:

   ```console
   # <datestamp>; conn=<number>; op=<number>
   dn: cn=File-Based Audit Logger,cn=Loggers,cn=config
   changetype: modify
   replace: ds-cfg-enabled
   ds-cfg-enabled: true
   -

   # <datestamp>; conn=<number>; op=<number>
   dn: uid=bjensen,ou=people,dc=example,dc=com
   changetype: modify
   add: description
   description: New description
   -
   ```

   Audit logs record changes in LDIF format. This means that when an LDAP entry is deleted, the audit log records only its DN.

## Filter out administrative messages

A common development troubleshooting technique consists of sending client requests while tailing the access log:

```console
$ tail -f /path/to/opendj/logs/ldap-access.audit.json
```

When the `dsconfig` command accesses the configuration, the access log records this. Such messages can prevent you from noticing the messages of interest from client applications.

You can filter access log messages for administrative connections to the administration port:

1. Configure access log filtering criteria:

   ```console
   $ dsconfig \
    create-access-log-filtering-criteria \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --publisher-name "Json File-Based Access Logger" \
    --criteria-name "Exclude LDAPS on 4444" \
    --type generic \
    --set connection-port-equal-to:4444 \
    --set connection-protocol-equal-to:ldaps \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

2. Activate filtering to exclude administrative messages:

   ```console
   $ dsconfig \
    set-log-publisher-prop \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --publisher-name "Json File-Based Access Logger" \
    --set filtering-policy:exclusive \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

   The publisher filters messages about administrative requests to the administration port.

## Audit configuration changes

This example demonstrates how to set up an audit log file to track changes to the server configuration.

Audit log change records have timestamped comments with connection and operation IDs. You can use these to correlate the changes with messages in access logs:

1. Create an audit log publisher:

   ```console
   $ dsconfig \
    create-log-publisher \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --publisher-name "File-Based Server Configuration Audit Log" \
    --type file-based-audit \
    --set enabled:true \
    --set filtering-policy:inclusive \
    --set log-file:logs/config-audit \
    --set rotation-policy:"24 Hours Time Limit Rotation Policy" \
    --set rotation-policy:"Size Limit Rotation Policy" \
    --set retention-policy:"File Count Retention Policy" \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

2. Create log filtering criteria for the logger that matches operations targeting `cn=config`:

   ```console
   $ dsconfig \
    create-access-log-filtering-criteria \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --publisher-name "File-Based Server Configuration Audit Log" \
    --criteria-name "Record changes to cn=config" \
    --set request-target-dn-equal-to:"**,cn=config" \
    --set request-target-dn-equal-to:"cn=config" \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

   The server now writes to the audit log file, `/path/to/opendj/logs/config-audit`, whenever an administrator changes the server configuration. The following example output shows the resulting LDIF that defines the log filtering criteria:

   ```ldif
   # <datestamp>; conn=<id>; op=<id>
   dn: cn=Record changes to cn=config,cn=Filtering Criteria,cn=File-Based Server Configuration Audit Log,cn=Loggers,cn=config
   changetype: add
   objectClass: top
   objectClass: ds-cfg-access-log-filtering-criteria
   cn: Record changes to cn=config
   ds-cfg-request-target-dn-equal-to: **,cn=config
   ds-cfg-request-target-dn-equal-to: cn=config
   createTimestamp: <timestamp>
   creatorsName: editable:dsAdminDN["uid=admin"]
   entryUUID: <uuid>
   ```

## Allow log message fields

1. When an object is passed in a Common Audit event, it might contain information that should not be logged. By default, the Common Audit implementation uses a whitelist to specify which fields of the event appear:

   1. For Common Audit HTTP access log publishers, edit the `log-field-whitelist` property.

      The following fields appear by default, with each field listed by its JSON path. You cannot change the default whitelist.

      If a whitelisted field contains an object, then listing the field means the whole object is whitelisted:

      * `/_id`

      * `/timestamp`

      * `/eventName`

      * `/transactionId`

      * `/trackingIds`

      * `/userId`

      * `/client`

      * `/server`

      * `/http/request/secure`

      * `/http/request/method`

      * `/http/request/path`

      * `/http/request/headers/accept`

      * `/http/request/headers/accept-api-version`

      * `/http/request/headers/content-type`

      * `/http/request/headers/host`

      * `/http/request/headers/user-agent`

      * `/http/request/headers/x-forwarded-for`

      * `/http/request/headers/x-forwarded-host`

      * `/http/request/headers/x-forwarded-port`

      * `/http/request/headers/x-forwarded-proto`

      * `/http/request/headers/x-original-uri`

      * `/http/request/headers/x-real-ip`

      * `/http/request/headers/x-request-id`

      * `/http/request/headers/x-requested-with`

      * `/http/request/headers/x-scheme`

      * `/request`

      * `/response`

   2. LDAP access loggers do not support whitelisting.

      By default, all fields are whitelisted.

## Deny log message fields

When an object is passed in a Common Audit event, it might contain information that should not be logged. Loggers allow all fields that are safe to log by default. The whitelist is processed before the blacklist, so blacklist settings overwrite the whitelist defaults:

1. Blacklist individual fields in common audit access logs to prevent the fields from appearing in messages.

   The following example prevents all request headers from appearing in JSON HTTP access logs:

   ```console
   $ dsconfig \
    set-log-publisher-prop \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --publisher-name "Json File-Based HTTP Access Logger" \
    --set log-field-blacklist:/http/response/headers \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

   The blacklist values are JSON paths to the fields in log messages.

## Make tampering evident

This procedure applies only to Common Audit-based logs.

Tamper-evident logging depends on a public key/private key pair and a secret key. The Common Audit framework accesses the keys in a JCEKS-type keystore. Follow these steps to prepare the keystore:

1. Store the password for the keystore in a file you can protect:

   ```console
   $ cat /path/to/opendj/config/audit-keystore.pin
   password
   ```

2. Generate a key pair in the keystore.

   The keystore holds a signing key with the alias `Signature`. Generate the key with the `RSA` key algorithm, and the `SHA256withRSA` signature algorithm.

   The following example uses the default file name:

   ```console
   $ keytool \
    -genkeypair \
    -keyalg RSA \
    -sigalg SHA256withRSA \
    -alias "Signature" \
    -dname "CN=ds.example.com,O=Example Corp,C=FR" \
    -keystore /path/to/opendj/config/audit-keystore \
    -storetype JCEKS \
    -storepass:file /path/to/opendj/config/audit-keystore.pin \
    -keypass:file /path/to/opendj/config/audit-keystore.pin
   ```

   You can configure the file name with the log publisher `key-store-file` property.

3. Generate a secret key in the keystore.

   The keystore holds a symmetric key with the alias `Password`. Generate the key with the `HmacSHA256` key algorithm, and 256-bit key size.

   The following example uses the default file name:

   ```console
   $ keytool \
    -genseckey \
    -keyalg HmacSHA256 \
    -keysize 256 \
    -alias "Password" \
    -keystore /path/to/opendj/config/audit-keystore \
    -storetype JCEKS \
    -storepass:file /path/to/opendj/config/audit-keystore.pin \
    -keypass:file /path/to/opendj/config/audit-keystore.pin
   ```

   You can configure the file name with the log publisher `key-store-file` property.

4. Verify that the keystore contains signature and password keys:

   ```console
   $ keytool \
    -list \
    -keystore /path/to/opendj/config/audit-keystore \
    -storetype JCEKS \
    -storepass:file /path/to/opendj/config/audit-keystore.pin
   ```

   > **Collapse: Show output**
   >
   > ```
   > password, <date>, SecretKeyEntry,
   > signature, <date>, PrivateKeyEntry,
   > Certificate fingerprint (SHA-256): <fingerprint>
   > ```