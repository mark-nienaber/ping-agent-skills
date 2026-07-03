---
title: Audit logging
description: Understand how PingAM captures and manages audit logs for security, compliance, and troubleshooting across multiple topics and event handlers
component: pingam
version: 8.1
page_id: pingam:monitoring:audit-logging
canonical_url: https://docs.pingidentity.com/pingam/8.1/monitoring/audit-logging.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Compliance"]
page_aliases: ["security-guide:audit-logs.adoc", "security-guide:audit-logging.adoc", "monitoring-guide:audit-logging.adoc"]
section_ids:
  log_messages: Log messages
  audit-log-topics: Audit topics
  log-mgmt-agents: Web and Java agent audit events
---

# Audit logging

AM's common REST-based audit logging service captures key auditing events, critical for system security, troubleshooting, and regulatory compliance.

Audit logs gather operational information about events that occur within an AM deployment. They track processes and security data, such as authentication mechanisms, system access, user and administrator activity, error messages, and configuration changes.

The audit logging service provides a versatile and rich feature set:

* Global and realm-based log configuration

  You can configure audit logging globally, which ensures that all realms inherit your global log settings. You can also configure audit logging by realm, which allows you to set different log settings for each realm.

* Audit event handlers

  The audit logging service supports a variety of audit event handlers that allow you to write logs to different types of datastores. You can find a list of event handlers available in AM in [Configuring audit event handlers](implementing-audit.html#configuring-audit-event-handlers).

* Audit event buffering

  By default, AM writes each log message separately as they are generated. AM supports message buffering, a type of batch processing, that stores log messages in memory and flushes the buffer after a preconfigured time interval or after a certain number of log messages reaches the configured threshold value.

* Tamper-evident logging

  For the CSV audit event handler, you can digitally sign audits to enable the detection of tampering.

* Log rotation and retention policies

  AM rotates JSON and CSV audit logs when it reaches a specified maximum size. You can also configure a time-based rotation policy, which disables the max-size rotation policy and implements log rotation based on a preconfigured time sequence. AM also provides the option to disable log rotation completely for these file types. AM doesn't support external log rotation for JSON and CSV audit logs.

  For Syslog, JDBC, and JMS handlers, AM doesn't control log rotation and retention as they are handled by each respective service.

* Allowlist and denylist support

  The audit logging service supports allowlist and denylist-filtering to show or hide sensitive values or fields in logs, such as HTTP headers, query parameters, cookies, profile attributes, or the entire field value.

* Reverse DNS lookup

  The audit logging service supports a reverse DNS lookup feature for network troubleshooting purposes. Reverse DNS lookup is disabled by default because it reduces operation throughput.

## Log messages

AM writes log messages generated from audit events triggered by its instances, web or Java agents, and connected Ping Advanced Identity Software implementations.

The audit logging service uses a structured message format that adheres to a consistent log structure across the Ping Advanced Identity Software. This common structure allows correlation between log messages of the different platform components if the transaction IDs are *trusted*. Find more information in [Trust transaction headers](implementing-audit.html#configuring-trusttransactionheader-system-property).

|   |                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Although the PingDS JSON logger is enabled by default, transaction IDs are not trusted by default. You must set `trust-transaction-ids:true` to correlate DS log messages with AM log messages. For more information, see [Log LDAP Access to Files > JSON Format](https://docs.pingidentity.com/pingds/8.1/logging-guide/ldap-access.html#log-common-audit-ldap-json) in the DS documentation. |

## Audit topics

AM assigns log messages to four different audit topics. A *topic* is a category of audit log event that has a one-to-one mapping with a schema type.

The following table shows the different event topics and associated audit log files for AM's default audit logging configuration, which uses a JSON audit event handler:

**Audit log topics**

| Event topic    | File name                   | Description                                                                                                                                                                                                                                                                     |
| -------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Access         | `access.audit.json`         | Captures who, what, when, and output for every access request.                                                                                                                                                                                                                  |
| Activity       | `activity.audit.json`       | Captures state changes to objects that have been created, updated, or deleted by end users (that is, non-administrators). Session, user profile, and device profile changes are captured in the logs.                                                                           |
| Authentication | `authentication.audit.json` | Captures when and how a subject is authenticated and related events.                                                                                                                                                                                                            |
| Configuration  | `config.audit.json`         | Captures configuration changes to the product with a timestamp and by whom. Note that the `userId` indicating the subject who made the configuration change is not captured in the `config.audit.json` but can be tracked using the `transactionId` in the `access.audit.json`. |

## Web and Java agent audit events

Web and Java agents log audit events for security, troubleshooting, and regulatory compliance. You can store web or Java agent audit event logs in the following ways:

* **Remotely**. Log audit events to the audit event handler configured in the AM realm.

* **Locally**. Log audit events to a file in the web or Java agent installation directory.

Learn more in the [Web Agents Maintenance Guide](https://docs.pingidentity.com/web-agents/2025.3/maintenance-guide/auditing.html) and the [Java Agents Maintenance Guide](https://docs.pingidentity.com/java-agents/2025.3/maintenance-guide/auditing.html).

---

---
title: Audit logging reference
description: Understand the audit log format, event names, and schema properties that PingAM writes for audit events triggered by its components and other PingOne Advanced Identity Cloud products
component: pingam
version: 8.1
page_id: pingam:monitoring:audit-logging-ref
canonical_url: https://docs.pingidentity.com/pingam/8.1/monitoring/audit-logging-ref.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Monitoring"]
page_aliases: ["security-guide:sec-maint-audit-ref.adoc", "monitoring-guide:audit-logging-ref.adoc"]
section_ids:
  audit-log-format: Audit log format
  access-log-format: Access log format
  activity-log-format: Activity log format
  authentication-log-format: Authentication log format
  config-log-format: Config log format
  audit-log-event-names: Audit log events
  audit-log-components: Audit log components
  audit-log-whitelist: Audit log fields
  access_log_fields: Access log fields
  activity_log_fields: Activity log fields
  authentication_log_fields: Authentication log fields
  config_log_fields: Config log fields
  jdbc-audit-log-tables: JDBC audit log tables
  table-jdbc-audit-log-auditaccess: am_auditaccess
  table-jdbc-audit-log-auditauthentication: am_auditauthentication
  table-jdbc-audit-log-auditactivity: am_auditactivity
  table-jdbc-audit-log-auditconfig: am_auditconfig
---

# Audit logging reference

AM writes log messages generated from audit events triggered by its components, instances, and other Ping Advanced Identity Software products.

## Audit log format

This section presents the audit log format for each topic-based file, event names, and audit constants used in its log messages.

### Access log format

| Schema property             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `_id`                       | A universally unique identifier (UUID) for the message object, such as `a568d4fe-d655-49a8-8290-bfc02095bec9-491`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `timestamp`                 | The timestamp when AM logged the message, in UTC format to millisecond precision: `yyyy-MM-ddTHH:mm:ss.msZ`. For example: `2025-03-14T00:16:04.653Z`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `eventName`                 | The name of the audit event. For example, `AM-ACCESS-ATTEMPT` and `AM-ACCESS-OUTCOME`. Find a list of audit event names in [Audit log events](#audit-log-event-names).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `transactionId`             | The UUID of the transaction, which identifies an external request when it comes into the system boundary. Any events generated while handling that request will be assigned that transaction ID, so that you may see the same transaction ID even for different audit event topics. For example, `9c9e8d5c-2941-4e61-9c3c-8a990088e801`.Trusted AM deployments with multiple instances, components, and Ping Advanced Identity Software products can propagate the transaction ID through each call across the stack. AM reads the `X-ForgeRock-TransactionId` HTTP header and appends an integer to the transaction ID. Note that this feature is disabled by default. When enabled, this feature should filter the `X-ForgeRock-TransactionId` HTTP header for connections from untrusted sources.                                                                                                                                                            |
| `user.id`                   | The universal identifier for authenticated users. For example, `id=bjensen,ou=user,o=alpha,ou=services,dc=example,dc=com`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `trackingIds`               | A unique random string generated as an alias for each AM session ID and OAuth 2.0 token. For example, `[ "45b17894529cf74301" ]`.For OAuth 2.0 tokens, whenever AM generates an access or grant token, it also generates unique random value and logs it as an alias. In this way, it is possible to trace back an access token back to its originating grant token, trace the grant token back to the session in which it was created, and then trace how the session was authenticated. An example of a `trackingIds` property in an OAuth 2.0/OpenID Connect 1.0 environment is:```
[ "1979edf68543ead001", "8878e51a-f2aa-464f-b1cc-b12fd6daa415", "3df9a5c3-8d1e-4ee3-93d6-b9bbe58163bc" ]
```	If the cross-upgrade session reference property is enabled, trackingIds will also contain a unique constant session identifier for session creation and upgrade events.                                                                                     |
| `server.ip`                 | The IP address of the AM server. For example, `127.0.0.1`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `server.port`               | The port number used by the AM server. For example, `8443`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `client.host`               | The client hostname. This field is only populated if reverse DNS lookup is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `client.ip`                 | The client IP address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `client.port`               | The client port number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `authorizationId.roles`     | The list of roles for the authorized user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `authorizationId.component` | The component part of the authorized ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `request.protocol`          | The protocol associated with the request operation. Possible values: `CREST`, `PLL`, `SAML2`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `request.operation`         | The request operation. For common REST operations, possible values are: `READ`, `ACTION`, `QUERY`.For PLL operations, possible values are: `LoginIndex`, `SubmitRequirements`, `GetSession`, `REQUEST_ADD_POLICY_LISTENER`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `request.detail`            | The detailed information about the request operation. For example:- `{"action":"idFromSession"}`

- `{"action":"validateGoto"}`

- `{"action":"validate"}`

- `{"action":"logout"}`

- `{"action":"schema"}`

- `{"action":"template"}`The following examples show different authentication flows:- For an OAuth 2.0 app tree flow:

  ```json
  {
    "oAuth2Client": "myClient",
    "configuredService": "oauth2Tree"
  }
  ```

- For a SAML 2.0 app tree flow:

  ```json
  {
    "spEntity": "serviceprovider1",
    "idpEntity": "identityprovider1",
    "configuredService": "samlTree"
  }
  ```

- For a SAML 2.0 flow where AM is the hosted IdP and the user has successfully authenticated:

  ```json
  {
    "spEntity": "serviceprovider1",
    "flowInitiator": "IDP",
    "idpEntity": "identityprovider1",
    "userID": "id=bjensen,ou=user,o=alpha,ou=services,dc=example,dc=com",
    "nameID": "V5Xa3AO+5xbxUfPSF73imsTYu3Rm"
  }
  ``` |
| `http.method`               | The HTTP method requested by the client. For example, `GET`, `POST`, `PUT`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `http.path`                 | The path of the HTTP request. For example, `https://am.example.com:8443/am/json/realms/root/authenticate`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `http.queryParameters`      | The HTTP query parameter string. For example:- `{ "_action": [ "idFromSession" ] }`

- `{ "_queryFilter": [ "true" ] }`

- `{ "_action": [ "validate" ] }`

- `{ "_action": [ "logout" ] }`

- `{ "realm": [ "/alpha" ] }`

- `{ "_action": [ "validateGoto" ] }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `http.request.headers`      | The HTTP header for the request. For example:```json
{
   "accept":[
      "application/json, text/javascript, */*; q=0.01"
   ],
   "Accept-API-Version":[
      "protocol=1.0"
   ],
   "accept-encoding":[
      "gzip, deflate"
   ],
   "accept-language":[
      "en-US;q=1,en;q=0.9"
   ],
   "cache-control":[
      "no-cache"
   ],
   "connection":[
      "Keep-Alive"
   ],
   "content-length":[
      "0"
   ],
   "host":[
      "am.example.com"
   ],
   "pragma":[
      "no-cache"
   ],
   "referer":[
      "https://am.example.com/am/XUI/"
   ],
   "user-agent":[
      "Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0"
   ],
   "x-nosession":[
      "true"
   ],
   "x-requested-with":[
      "XMLHttpRequest"
   ],
   "x-username":[
      "anonymous"
   ]
}
```                                                                                                                                         |
| `http.request.cookies`      | A JSON map of key-value pairs and appears as its own property to allow for denylisting fields or values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `http.response.cookies`     | Not used in AM.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `response.status`           | The response status of the request. For example, `SUCCESS`, `FAILURE`, or null.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `response.statusCode`       | The response status code, depending on the protocol. For common REST, HTTP failure codes are displayed but not HTTP success codes. For PLL endpoints, PLL error codes are displayed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `response.detail`           | The message associated with `response.statusCode`. For example, the `response.statusCode` of `401` has a `response.detail` of `{ "reason": "Unauthorized" }`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `response.elapsedTime`      | The time to execute the access event, usually in millisecond precision.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `response.elapsedTimeUnits` | The elapsed time units of the response. For example, `MILLISECONDS`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `component`                 | The AM service utilized. For example, `Server Info`, `Users`, `Config`, `Session`, `Authentication`, `Policy`, `OAuth`, `SAML2`, `Web Policy Agent`, or `Java Policy Agent`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `realm`                     | The realm where the operation occurred. For example, the Top Level Realm (`/`) or the sub-realm name (`/alpha`).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

### Activity log format

| Property        | Description                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `_id`           | A universally unique identifier (UUID) for the message object, such as `a568d4fe-d655-49a8-8290-bfc02095bec9-487`.                                                                                                                                                                                                                                                                                                     |
| `timestamp`     | The timestamp when AM logged the message, in UTC format to millisecond precision: `yyyy-MM-ddTHH:mm:ss.msZ`. For example: `2025-03-14T00:16:04.652Z`                                                                                                                                                                                                                                                                   |
| `eventName`     | The name of the audit event. For example, `AM-SESSION_CREATED`, `AM-SESSION-LOGGED_OUT`, `AM-IDENTITY-CHANGE`. Find a list of audit event names in [Audit log events](#audit-log-event-names).                                                                                                                                                                                                                         |
| `transactionId` | The UUID of the transaction, which identifies an external request when it comes into the system boundary. Any events generated while handling that request will be assigned that transaction ID, so that you may see the same transaction ID for same even for different audit event topics. For example, `9c9e8d5c-2941-4e61-9c3c-8a990088e801`.                                                                      |
| `user.id`       | The universal identifier for authenticated users. For example, `id=bjensen,ou=user,o=alpha,ou=services,dc=example,dc=com`.                                                                                                                                                                                                                                                                                             |
| `trackingIds`   | An array containing a random context ID that identifies the session and a random string generated from an OAuth 2.0/OpenID Connect 1.0 flow that could track an access token ID or an grant token ID. For example, `[ "45b17894529cf74301" ]`.	If the cross-upgrade session reference property is enabled, trackingIds will also contain a unique constant session identifier for session creation and upgrade events. |
| `runAs`         | The user to run the activity as. May be used in delegated administration. For example, `id=amadmin,ou=user,ou=am-config`.                                                                                                                                                                                                                                                                                              |
| `objectId`      | The identifier of an object that has been created, updated, or deleted. For logging sessions, the session `trackingId` is used in this field. For example, `[ "45b17894529cf74301" ]`                                                                                                                                                                                                                                  |
| `operation`     | The state change operation invoked: `CREATE`, `MODIFY`, or `DELETE`.                                                                                                                                                                                                                                                                                                                                                   |
| `before`        | Not used.                                                                                                                                                                                                                                                                                                                                                                                                              |
| `after`         | Not used.                                                                                                                                                                                                                                                                                                                                                                                                              |
| `changedFields` | Not used.                                                                                                                                                                                                                                                                                                                                                                                                              |
| `revision`      | Not used.                                                                                                                                                                                                                                                                                                                                                                                                              |
| `component`     | The AM service utilized. For example, `Session` or `Self-Service`.                                                                                                                                                                                                                                                                                                                                                     |
| `realm`         | The realm where the operation occurred. For example, the Top Level Realm (`/`) or the sub-realm name (`/alpha`).                                                                                                                                                                                                                                                                                                       |

### Authentication log format

| Property        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `_id`           | A universally unique identifier (UUID) for the message object, such as `a568d4fe-d655-49a8-8290-bfc02095bec9-485`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `timestamp`     | The timestamp when AM logged the message, in UTC format to millisecond precision: `yyyy-MM-ddTHH:mm:ss.msZ`. For example: `2025-03-14T00:16:04.640Z`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `eventName`     | The name of the audit event. For example, `AM-LOGOUT` and `AM-NODE-LOGIN-COMPLETED`. Find a list of audit event names in [Audit log events](#audit-log-event-names).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `transactionId` | The UUID of the transaction, which identifies an external request when it comes into the system boundary. Any events generated while handling that request will be assigned that transaction ID, so that you may see the same transaction ID even for different audit event topics. For example, `9c9e8d5c-2941-4e61-9c3c-8a990088e801`.                                                                                                                                                                                                                                                                                                                                                                                                                |
| `user.id`       | The universal identifier for authenticated users. For example, `id=bjensen,ou=user,o=alpha,ou=services,dc=example,dc=com`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `trackingIds`   | An array containing a unique random context ID. For example:- For OAuth 2.0/OpenID Connect flows, it identifies the session and a random string generated that can track an access token ID or a grant token ID.

- For authentication trees, it identifies an authentication tree flow.	If the cross-upgrade session reference property is enabled, trackingIds will also contain a unique constant session identifier for session creation and upgrade events.                                                                                                                                                                                                                                                                                        |
| `result`        | The result for an authentication tree.Possible values are `SUCCESSFUL` or `FAILED`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `principal`     | The array of accounts used to authenticate, such as `[ "amadmin" ]` and `[ "bjensen" ]`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `context`       | Not used                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `entries`       | The JSON representation of the authentication tree or node details. AM creates an event as each node completes and a final event at the end of the tree. For example:```json
{
  "entries": [
    {
      "info": {
        "nodeOutcome": "outcome",
        "treeName": "ldapService",
        "displayName": "User Name Collector",
        "nodeType": "UsernameCollectorNode",
        "nodeId": "cfcd2084-95d5-35ef-a6e7-dff9f98764db",
        "version": "2.0",
        "authLevel": "0"
      }
    }
  ]
}
```	By default, version is logged only for node versions greater than 1.0. To log version for all node versions, add the org.forgerock.am.auth.node.versioning.enable.v1.audit.detail advanced server property and set it to true. |
| `component`     | The AM service utilized. For example, `Authentication`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `realm`         | The realm where the operation occurred. For example, the Top Level Realm (`/`) or the sub-realm name (`/alpha`).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

### Config log format

| Property        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `_id`           | A universally unique identifier (UUID) for the message object. For example, `6a568d4fe-d655-49a8-8290-bfc02095bec9-843`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `timestamp`     | The timestamp when AM logged the message, in UTC format to millisecond precision: `yyyy-MM-ddTHH:mm:ss.msZ`. For example, `2025-03-14T00:21:03.490Z`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `eventName`     | The name of the audit event. For example, `AM-CONFIG-CHANGE`. Find a list of audit event names in [Audit log events](#audit-log-event-names).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `transactionId` | The UUID of the transaction, which identifies an external request when it comes into the system boundary. Any events generated while handling that request will be assigned that transaction ID, so that you may see the same transaction ID for different audit event topics. For example, `301d1a6e-67f9-4e45-bfeb-5e4047a8b432`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `user.id`       | Not used.You can determine the value for this field by linking to the access event using the same `transactionId`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `trackingIds`   | Not used.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `runAs`         | The user to run the activity as. May be used in delegated administration. For example, `id=amadmin,ou=user,ou=am-config`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `objectId`      | The identifier of a system object that has been created, modified, or deleted. For example, `ou=iPlanetAMAuthService,ou=services,o=alpha,ou=services,dc=example,dc=com`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `operation`     | The state change operation invoked: `CREATE`, `MODIFY`, or `DELETE`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `before`        | The JSON representation of the object prior to the activity. For example:```json
{
    "sunKeyValue": [
      "entryNodeId=e301438c-0bd0-429c-ab0c-66126501069a",
      "nodes={}",
      "staticNodes={}"
    ]
}
```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `after`         | The JSON representation of the object after the activity. For example:```json
{
    "sunKeyValue": [
      "entryNodeId=8058f432-b319-410b-afbb-c532f9a111b7",
      "innerTreeOnly=false",
      "enabled=true",
      "noSession=false",
      "mustRun=false",
      "uiConfig=",
      "staticNodes={\"startNode\":{\"x\":50,\"y\":25},\"70e691a5-1e33-4ac3-a356-e7b6d60d92e0\":{\"x\":777,\"y\":377},\"e301438c-0bd0-429c-ab0c-66126501069a\":{\"x\":1087,\"y\":109}}",
      "nodes={\"4c8bb786-80c5-424b-b75f-b66e54741177\":{\"displayName\":\"Password Collector\",\"nodeType\":\"PasswordCollectorNode\",\"x\":214,\"y\":178.984375,\"connections\":{\"outcome\":\"cd0253de-f473-45fc-a431-78575c2b2a4f\"}},\"8058f432-b319-410b-afbb-c532f9a111b7\":{\"displayName\":\"Username Collector\",\"nodeType\":\"UsernameCollectorNode\",\"x\":206,\"y\":123.984375,\"connections\":{\"outcome\":\"4c8bb786-80c5-424b-b75f-b66e54741177\"}},\"cd0253de-f473-45fc-a431-78575c2b2a4f\":{\"displayName\":\"Data Store Decision\",\"nodeType\":\"DataStoreDecisionNode\",\"x\":599,\"y\":198.984375,\"connections\":{\"true\":\"70e691a5-1e33-4ac3-a356-e7b6d60d92e0\",\"false\":\"e301438c-0bd0-429c-ab0c-66126501069a\"}}}"
    ]
}
``` |
| `changedFields` | The fields that were changed. For example, `[ "nodes" ]`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `revision`      | Not used.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `component`     | Not used.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `realm`         | The realm where the operation occurred. For example, the Top Level Realm (`/`) or the sub-realm name (`/alpha`).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

## Audit log events

This table summarizes the predefined events for each topic:

| Topic            | Event name                                | Event description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---------------- | ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `access`         | `AM-ACCESS_ATTEMPT`                       | When AM starts handling an HTTP request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `access`         | `AM-ACCESS-OUTCOME`                       | When AM finishes handling an HTTP request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `activity`       | `AM-BACK-CHANNEL-LOGOUT`                  | Event for an OIDC back-channel logout.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `activity`       | `AM-CONNECTION-FACTORY-CLOSED`            | Event for closing a connection factory.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `activity`       | `AM-CONNECTION-UPDATE`                    | Event for a state change for the connection factory, such as when configuration changes lead to an attempt to reconnect.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `activity`       | `AM-GROUP-CHANGE`                         | When a group is changed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `activity`       | `AM-IDENTITY-CHANGE`                      | When an identity is updated, such as a change to an attribute.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `activity`       | `AM-KEY-MANAGER-RELOAD-NOTIFICATION`      | Key Manager reload event.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `activity`       | `AM-LOGOUT-USER-TOKEN`                    | When a user is logged out by their username (client-side sessions only).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `activity`       | `AM-NEW-CONNECTION-FACTORY`               | Event for creating a new connection factory.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `activity`       | `AM-SELFSERVICE-REGISTRATION-COMPLETED`   | When the self-service registration process is complete.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `activity`       | `AM-SELFSERVICE-PASSWORDCHANGE-COMPLETED` | When the self-service password reset process is complete.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `activity`       | `AM-SESSION-CREATED`                      | When an authenticated session is created.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `activity`       | `AM-SESSION-DESTROYED`                    | When an authenticated session is destroyed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `activity`       | `AM-SESSION-IDLE_TIMED_OUT`               | When an authenticated session has been inactive for longer than configured idle timeout duration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `activity`       | `AM-SESSION-LOGGED_OUT`                   | Event for the explicit logout of an authenticated session.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `activity`       | `AM-SESSION-MAX_TIMED_OUT`                | When an authenticated session exceeds the maximum configured lifetime.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `activity`       | `AM-SESSION-PROPERTY_CHANGED`             | When an authenticated session property changes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `activity`       | `AM-TOKEN-EXCHANGE`                       | Event for an OAuth 2.0 token exchange.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `authentication` | `AM-BACK-CHANNEL-INITIALIZE`              | Event for the initiation of a [backchannel authentication](../am-authentication/backchannel-authentication.html) request.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `authentication` | `AM-LOGOUT`                               | Event for an authentication process logout.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `authentication` | `AM-NODE-LOGIN-COMPLETED`                 | Event for the successful or failed completion of an authentication node login.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `authentication` | `AM-TREE-LOGIN-STARTED`                   | Logged when authentication through a tree starts. If the tree includes a node that suspends the authentication journey, this event is logged again after the suspension with a result of `continue`.                                                                                                                                                                                                                                                                                                                                                                         |
| `authentication` | `AM-TREE-LOGIN-COMPLETED`                 | Logged when an authentication journey completes, whether successful or not.- If authentication completes successfully, the event has a `result` of `SUCCESS`.

- If authentication fails, the event has a `result` of `FAILED`.

- If the authentication ends in an *exception* (usually due to a misconfiguration in the journey), the event has a `result` of `FAILED` with the following additional field:

  `exception: "An exception occurred during the authentication process"`

  These exceptions let you troubleshoot logins that failed due to misconfiguration. |
| `config`         | `AM-BOOT-JSON-UPDATED`                    | When the `boot.json` file is updated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `config`         | `AM-CONFIG-CHANGE`                        | When the AM configuration is updated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

## Audit log components

This table lists the predefined audit event components that make up log messages:

| Event component        | AM component, service, or feature          |
| ---------------------- | ------------------------------------------ |
| `AM agents`            | Web and Java agents                        |
| `Audit`                | Auditing service                           |
| `Authentication`       | Authentication service                     |
| `Batch`                | Batch service                              |
| `Boot Json`            | Boot.json component                        |
| `Config`               | Configuration                              |
| `CORS`                 | CORS preflight component                   |
| `CTS`                  | Core Token Service                         |
| `Dashboard`            | Dashboard service                          |
| `Devices`              | Trusted devices                            |
| `Documentation`        | API documentation component                |
| `Groups`               | Groups component                           |
| `ID Repo`              | ID repo event component                    |
| `Monitoring`           | Monitoring                                 |
| `Oath`                 | Mobile authentication                      |
| `OAuth`                | OAuth 2.0, OpenID Connect 1.0, and UMA     |
| `Policy`               | Policies                                   |
| `Push`                 | Push Notification service                  |
| `Radius`               | RADIUS server                              |
| `Realms`               | Realms and sub-realms                      |
| `Record`               | Recording service                          |
| `SAML2`                | SAML 2.0                                   |
| `Script`               | Scripting service                          |
| `Secrets`              | Secrets component                          |
| `Self-Service`         | User Self-Service service                  |
| `Service Config Cache` | Service Config Cache audit event component |
| `Server Info`          | Server information service                 |
| `Session`              | Session service                            |
| `STS`                  | REST Secure Token Service                  |
| `Things`               | Internet of Things component               |
| `Users`                | Users component                            |

## Audit log fields

The following tables list all the available fields that you can use to filter audit logs. The log fields are listed in JSON notation.

Some fields may contain sensitive information and aren't suitable for recording in audit logs. By default, AM has a preconfigured allowlist that defines which object fields can be logged.

The table indicates which fields appear on the default allowlist. If an allowlisted field contains an object, then listing the field means the whole object is allowlisted.

### Access log fields

| Field                                                           | Allowlisted by default |
| --------------------------------------------------------------- | ---------------------- |
| `/access/_id`                                                   | Yes                    |
| `/access/client/ip`                                             | Yes                    |
| `/access/client/port`                                           | Yes                    |
| `/access/access/component`                                      |                        |
| `/access/eventName`                                             | Yes                    |
| `/access/http/request/cookies/Domain`                           |                        |
| `/access/http/request/cookies/Expires`                          |                        |
| `/access/http/request/cookies/HttpOnly`                         |                        |
| `/access/http/request/cookies/JSESSIONID`                       |                        |
| `/access/http/request/cookies/Max-Age`                          |                        |
| `/access/http/request/cookies/NTID`                             |                        |
| `/access/http/request/cookies/OAUTH_REQUEST_ATTRIBUTES`         |                        |
| `/access/http/request/cookies/ORIG_URL`                         |                        |
| `/access/http/request/cookies/Path`                             |                        |
| `/access/http/request/cookies/amlbcookie`                       |                        |
| `/access/http/request/cookies/authId`                           |                        |
| `/access/http/request/cookies/iPlanetDirectoryPro`              |                        |
| `/access/http/request/headers/accept`                           | Yes                    |
| `/access/http/request/headers/accept-api-version`               | Yes                    |
| `/access/http/request/headers/accept-encoding`                  |                        |
| `/access/http/request/headers/accept-language`                  |                        |
| `/access/http/request/headers/authorization`                    |                        |
| `/access/http/request/headers/cache-control`                    |                        |
| `/access/http/request/headers/connection`                       |                        |
| `/access/http/request/headers/content-length`                   |                        |
| `/access/http/request/headers/content-type`                     | Yes                    |
| `/access/http/request/headers/host`                             | Yes                    |
| `/access/http/request/headers/if-match`                         |                        |
| `/access/http/request/headers/if-none-match`                    |                        |
| `/access/http/request/headers/iplanetdirectorypro`              |                        |
| `/access/http/request/headers/oidc_id_token`                    |                        |
| `/access/http/request/headers/origin`                           |                        |
| `/access/http/request/headers/referer`                          |                        |
| `/access/http/request/headers/upgrade-insecure-requests`        |                        |
| `/access/http/request/headers/user-agent`                       | Yes                    |
| `/access/http/request/headers/user`                             |                        |
| `/access/http/request/headers/x-forgerock-transactionid`        |                        |
| `/access/http/request/headers/x-forwarded-for`                  | Yes                    |
| `/access/http/request/headers/x-forwarded-host`                 | Yes                    |
| `/access/http/request/headers/x-forwarded-port`                 | Yes                    |
| `/access/http/request/headers/x-forwarded-proto`                | Yes                    |
| `/access/http/request/headers/x-nosession`                      |                        |
| `/access/http/request/headers/x-openam-password`                |                        |
| `/access/http/request/headers/x-openam-username`                |                        |
| `/access/http/request/headers/x-original-uri`                   | Yes                    |
| `/access/http/request/headers/x-password`                       |                        |
| `/access/http/request/headers/x-real-ip`                        | Yes                    |
| `/access/http/request/headers/x-request-id`                     | Yes                    |
| `/access/http/request/headers/x-requested-with`                 | Yes                    |
| `/access/http/request/headers/x-scheme`                         | Yes                    |
| `/access/http/request/headers/x-username`                       |                        |
| `/access/http/request/method`                                   | Yes                    |
| `/access/http/request/path`                                     | Yes                    |
| `/access/http/request/queryParameters/ForceAuth`                |                        |
| `/access/http/request/queryParameters/_action`                  |                        |
| `/access/http/request/queryParameters/_fields`                  |                        |
| `/access/http/request/queryParameters/_pageSize`                |                        |
| `/access/http/request/queryParameters/_queryFilter`             |                        |
| `/access/http/request/queryParameters/_queryId`                 |                        |
| `/access/http/request/queryParameters/access_token`             |                        |
| `/access/http/request/queryParameters/acr`                      |                        |
| `/access/http/request/queryParameters/agent_realm`              |                        |
| `/access/http/request/queryParameters/assertion`                |                        |
| `/access/http/request/queryParameters/authIndexType`            | Yes                    |
| `/access/http/request/queryParameters/authIndexValue`           | Yes                    |
| `/access/http/request/queryParameters/client_id`                |                        |
| `/access/http/request/queryParameters/client_secret`            |                        |
| `/access/http/request/queryParameters/cnf_key`                  |                        |
| `/access/http/request/queryParameters/code`                     |                        |
| `/access/http/request/queryParameters/code_challenge`           |                        |
| `/access/http/request/queryParameters/code_challenge_method`    |                        |
| `/access/http/request/queryParameters/code_verifier`            |                        |
| `/access/http/request/queryParameters/composite_advice`         | Yes                    |
| `/access/http/request/queryParameters/csrf`                     |                        |
| `/access/http/request/queryParameters/decision`                 |                        |
| `/access/http/request/queryParameters/device_code`              |                        |
| `/access/http/request/queryParameters/forUI`                    |                        |
| `/access/http/request/queryParameters/goto`                     |                        |
| `/access/http/request/queryParameters/grant_type`               |                        |
| `/access/http/request/queryParameters/id_token`                 |                        |
| `/access/http/request/queryParameters/iss`                      |                        |
| `/access/http/request/queryParameters/level`                    | Yes                    |
| `/access/http/request/queryParameters/nonce`                    |                        |
| `/access/http/request/queryParameters/oauth_token`              |                        |
| `/access/http/request/queryParameters/oauth_verifier`           |                        |
| `/access/http/request/queryParameters/password`                 |                        |
| `/access/http/request/queryParameters/prompt`                   |                        |
| `/access/http/request/queryParameters/realm`                    |                        |
| `/access/http/request/queryParameters/redirect_uri`             |                        |
| `/access/http/request/queryParameters/refresh_token`            |                        |
| `/access/http/request/queryParameters/rel`                      |                        |
| `/access/http/request/queryParameters/request`                  |                        |
| `/access/http/request/queryParameters/resource`                 | Yes                    |
| `/access/http/request/queryParameters/response_type`            |                        |
| `/access/http/request/queryParameters/role`                     | Yes                    |
| `/access/http/request/queryParameters/save_consent`             |                        |
| `/access/http/request/queryParameters/scope`                    |                        |
| `/access/http/request/queryParameters/service`                  | Yes                    |
| `/access/http/request/queryParameters/sessionUpgradeSSOTokenId` |                        |
| `/access/http/request/queryParameters/state`                    |                        |
| `/access/http/request/queryParameters/token`                    |                        |
| `/access/http/request/queryParameters/user`                     | Yes                    |
| `/access/http/request/queryParameters/user_code`                |                        |
| `/access/http/request/queryParameters/username`                 |                        |
| `/access/http/request/secure`                                   | Yes                    |
| `/access/realm`                                                 |                        |
| `/access/request/detail/action`                                 | Yes                    |
| `/access/request/operation`                                     | Yes                    |
| `/access/request/protocol`                                      | Yes                    |
| `/access/response/detail/active`                                | Yes                    |
| `/access/response/detail/application_type`                      | Yes                    |
| `/access/response/detail/client_id`                             | Yes                    |
| `/access/response/detail/objectId`                              | Yes                    |
| `/access/response/detail/reason`                                | Yes                    |
| `/access/response/detail/redirect_uris`                         | Yes                    |
| `/access/response/detail/revision`                              | Yes                    |
| `/access/response/detail/scope`                                 | Yes                    |
| `/access/response/detail/scope`                                 | Yes                    |
| `/access/response/detail/token_type`                            | Yes                    |
| `/access/response/detail/username`                              | Yes                    |
| `/access/response/elapsedTime`                                  | Yes                    |
| `/access/response/elapsedTimeUnits`                             | Yes                    |
| `/access/response/status`                                       | Yes                    |
| `/access/response/statusCode`                                   | Yes                    |
| `/access/server/ip`                                             | Yes                    |
| `/access/server/port`                                           | Yes                    |
| `/access/timestamp`                                             | Yes                    |
| `/access/trackingIds`                                           | Yes                    |
| `/access/transactionId`                                         | Yes                    |
| `/access/userId`                                                | Yes                    |

### Activity log fields

| Field                                                  | Allowlisted by default |
| ------------------------------------------------------ | ---------------------- |
| `/activity/_id`                                        | Yes                    |
| `/activity/after/_id`                                  |                        |
| `/activity/after/_username`                            |                        |
| `/activity/after/assignedDashboard`                    | Yes                    |
| `/activity/after/cn`                                   | Yes                    |
| `/activity/after/commonName`                           | Yes                    |
| `/activity/after/createTimestamp`                      |                        |
| `/activity/after/dn`                                   |                        |
| `/activity/after/givenName`                            | Yes                    |
| `/activity/after/inetUserStatus`                       | Yes                    |
| `/activity/after/iplanet-am-session-max-caching-time`  |                        |
| `/activity/after/iplanet-am-session-max-idle-time`     |                        |
| `/activity/after/iplanet-am-session-max-session-time`  |                        |
| `/activity/after/iplanet-am-session-quota-limit`       |                        |
| `/activity/after/iplanet-am-user-alias-list`           | Yes                    |
| `/activity/after/iplanet-am-user-login-status`         | Yes                    |
| `/activity/after/kbaInfo`                              |                        |
| `/activity/after/kbaInfoAttempts`                      | Yes                    |
| `/activity/after/lastEmailSent`                        |                        |
| `/activity/after/mail`                                 |                        |
| `/activity/after/memberof`                             | Yes                    |
| `/activity/after/modifyTimestamp`                      |                        |
| `/activity/after/o`                                    | Yes                    |
| `/activity/after/oath2faEnabled`                       | Yes                    |
| `/activity/after/oathDeviceProfiles`                   |                        |
| `/activity/after/objectClass`                          | Yes                    |
| `/activity/after/organizationName`                     | Yes                    |
| `/activity/after/organizationUnitName`                 | Yes                    |
| `/activity/after/ou`                                   | Yes                    |
| `/activity/after/push2faEnabled`                       | Yes                    |
| `/activity/after/pushDeviceProfiles`                   |                        |
| `/activity/after/sn`                                   | Yes                    |
| `/activity/after/sunAMAuthInvalidAttemptsData`         | Yes                    |
| `/activity/after/surname`                              | Yes                    |
| `/activity/after/uid`                                  | Yes                    |
| `/activity/after/uniqueMember`                         | Yes                    |
| `/activity/after/userid`                               | Yes                    |
| `/activity/after/userPassword`                         |                        |
| `/activity/after/webauthnDeviceProfiles`               |                        |
| `/activity/before/assignedDashboard`                   | Yes                    |
| `/activity/before/cn`                                  | Yes                    |
| `/activity/before/commonName`                          | Yes                    |
| `/activity/before/givenName`                           | Yes                    |
| `/activity/before/inetUserStatus`                      | Yes                    |
| `/activity/before/iplanet-am-session-max-caching-time` |                        |
| `/activity/before/iplanet-am-session-max-idle-time`    |                        |
| `/activity/before/iplanet-am-session-max-session-time` |                        |
| `/activity/before/iplanet-am-session-quota-limit`      |                        |
| `/activity/before/iplanet-am-user-alias-list`          | Yes                    |
| `/activity/before/iplanet-am-user-login-status`        | Yes                    |
| `/activity/before/kbaInfo`                             |                        |
| `/activity/before/kbaInfoAttempts`                     | Yes                    |
| `/activity/before/lastEmailSent`                       |                        |
| `/activity/before/memberof`                            | Yes                    |
| `/activity/before/modifyTimestamp`                     |                        |
| `/activity/before/o`                                   | Yes                    |
| `/activity/before/oath2faEnabled`                      | Yes                    |
| `/activity/before/objectClass`                         | Yes                    |
| `/activity/before/organizationName`                    | Yes                    |
| `/activity/before/organizationUnitName`                | Yes                    |
| `/activity/before/ou`                                  | Yes                    |
| `/activity/before/push2faEnabled`                      | Yes                    |
| `/activity/before/sn`                                  | Yes                    |
| `/activity/before/sunAMAuthInvalidAttemptsData`        | Yes                    |
| `/activity/before/surname`                             | Yes                    |
| `/activity/before/uid`                                 | Yes                    |
| `/activity/before/uniqueMember`                        | Yes                    |
| `/activity/before/userid`                              | Yes                    |
| `/activity/before/userPassword`                        |                        |
| `/activity/changedFields`                              | Yes                    |
| `/activity/component`                                  | Yes                    |
| `/activity/eventName`                                  | Yes                    |
| `/activity/objectId`                                   | Yes                    |
| `/activity/operation`                                  | Yes                    |
| `/activity/realm`                                      | Yes                    |
| `/activity/revision`                                   | Yes                    |
| `/activity/runAs`                                      | Yes                    |
| `/activity/timestamp`                                  | Yes                    |
| `/activity/trackingIds`                                | Yes                    |
| `/activity/transactionId`                              | Yes                    |
| `/activity/userId`                                     | Yes                    |

### Authentication log fields

| Field              | Allowlisted by default |
| ------------------ | ---------------------- |
| `/authentication/` | Yes                    |

### Config log fields

| Field                            | Allowlisted by default |
| -------------------------------- | ---------------------- |
| `/config/_id`                    | Yes                    |
| `/config/after/modifytimestamp`  |                        |
| `/config/after/objectclass`      |                        |
| `/config/after/ou`               |                        |
| `/config/after/sunKeyValue`      |                        |
| `/config/after/sunserviceID`     |                        |
| `/config/after/sunsmspriority`   |                        |
| `/config/after/sunxmlKeyValue`   |                        |
| `/config/before/modifytimestamp` |                        |
| `/config/before/objectclass`     |                        |
| `/config/before/ou`              |                        |
| `/config/before/sunKeyValue`     |                        |
| `/config/before/sunserviceID`    |                        |
| `/config/before/sunsmspriority`  |                        |
| `/config/before/sunxmlKeyValue`  |                        |
| `/config/changedFields`          | Yes                    |
| `/config/component`              | Yes                    |
| `/config/eventName`              | Yes                    |
| `/config/objectId`               | Yes                    |
| `/config/operation`              | Yes                    |
| `/config/realm`                  | Yes                    |
| `/config/revision`               | Yes                    |
| `/config/runAs`                  | Yes                    |
| `/config/timestamp`              | Yes                    |
| `/config/trackingIds`            | Yes                    |
| `/config/transactionId`          | Yes                    |
| `/config/userId`                 |                        |

## JDBC audit log tables

AM writes audit events to relational databases using the JDBC audit event handler. This section presents the columns for each audit table.

|   |                                                                                                                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The data sizes specified in the following tables are only a guide and may need to be increased to suit your configuration.For example, the `userid` field could require a size larger than the suggested `VARCHAR(255)`, depending on the length of your base DNs and user IDs. |

### am\_auditaccess

| Column                         | Datatype               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------ | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `id`                           | `VARCHAR(56) NOT NULL` | A universally unique identifier (UUID) for the message object, such as `a568d4fe-d655-49a8-8290-bfc02095bec9-491`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `timestamp_`                   | `VARCHAR(29) NULL`     | The timestamp when AM logged the message, in UTC format to millisecond precision: `yyyy-MM-ddTHH:mm:ss.msZ`. For example: `2025-03-14T00:16:04.653Z`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `transactionid`                | `VARCHAR(255) NULL`    | The UUID of the transaction, which identifies an external request when it comes into the system boundary. Any events generated while handling that request will be assigned that transaction ID, so that you may see the same transaction ID for different audit event topics. For example, `9c9e8d5c-2941-4e61-9c3c-8a990088e801`.Trusted AM deployments with multiple instances, components, and Ping Advanced Identity Software products can propagate a transaction ID through each call across the platform. AM reads the `X-ForgeRock-TransactionId` HTTP header and appends an integer to the transaction ID. Note that this feature is disabled by default. When enabled, this feature should filter the `X-ForgeRock-TransactionId` HTTP header for connections from untrusted sources.                         |
| `eventname`                    | `VARCHAR(255)`         | The name of the audit event. For example, `AM-ACCESS-ATTEMPT` and `AM-ACCESS-OUTCOME`. Find a list of audit event names in [Audit log events](#audit-log-event-names).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `userid`                       | `VARCHAR(255) NULL`    | The universal identifier for the authenticated user. For example, `id=bjensen,ou=user,o=alpha,ou=services,dc=example,dc=com`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `trackingids`                  | `MEDIUMTEXT`           | The tracking IDs of the event, used by all topics.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `server_ip`                    | `VARCHAR(40)`          | The IP address of the AM server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `server_port`                  | `VARCHAR(5)`           | The port number used by the AM server. For example, `8443`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `client_host`                  | `VARCHAR(255)`         | The client hostname. This column is only populated if reverse DNS lookup is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `client_ip`                    | `VARCHAR(40)`          | The client IP address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `client_port`                  | `VARCHAR(5)`           | The client port number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `request_protocol`             | `VARCHAR(255) NULL`    | The protocol associated with the request operation. Possible values: `CREST` and `PLL`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `request_operation`            | `VARCHAR(255) NULL`    | The request operation.For common REST operations, possible values: `READ`, `ACTION`, `QUERY`.For PLL operations, possible values: `LoginIndex`, `SubmitRequirements`, `GetSession`, `REQUEST_ADD_POLICY_LISTENER`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `request_detail`               | `TEXT NULL`            | The detailed information about the request operation. For example:- `{"action":"idFromSession"}`

- `{"action":"validateGoto"}`

- `{"action":"validate"}`

- `{"action":"logout"}`

- `{"action":"schema"}`

- `{"action":"template"}`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `http_request_secure`          | `BOOLEAN NULL`         | The HTTP method requested by the client. For example, `true` or `false`. Note that `false` does not mean the client connection is insecure as there may be a reverse proxy terminating the HTTPS connection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `http_request_method`          | `VARCHAR(7) NULL`      | The HTTP method requested by the client. For example, `GET`, `POST`, `PUT`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `http_request_path`            | `VARCHAR(255) NULL`    | The path of the HTTP request. For example, `https://am.example.com:8443/am/json/realms/root/authenticate`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `http_request_queryparameters` | `MEDIUMTEXT NULL`      | The HTTP query parameter string. For example:- `{ "_action": [ "idFromSession" ] }`

- `{ "_queryFilter": [ "true" ] }`

- `{ "_action": [ "validate" ] }`

- `{ "_action": [ "logout" ] }`

- `{ "realm": [ "/alpha" ] }`

- `{ "_action": [ "validateGoto" ] }`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `http_request_headers`         | `MEDIUMTEXT NULL`      | The HTTP headers for the request. For example:```json
{
   "accept":[
      "application/json, text/javascript, */*; q=0.01"
   ],
   "Accept-API-Version":[
      "protocol=1.0"
   ],
   "accept-encoding":[
      "gzip, deflate"
   ],
   "accept-language":[
      "en-US;q=1,en;q=0.9"
   ],
   "cache-control":[
      "no-cache"
   ],
   "connection":[
      "Keep-Alive"
   ],
   "content-length":[
      "0"
   ],
   "host":[
      "am.example.com"
   ],
   "pragma":[
      "no-cache"
   ],
   "referer":[
      "https://am.example.com/am/XUI/"
   ],
   "user-agent":[
      "Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0"
   ],
   "x-nosession":[
      "true"
   ],
   "x-requested-with":[
      "XMLHttpRequest"
   ],
   "x-username":[
      "anonymous"
   ]
}
``` |
| `http_request_cookies`         | `MEDIUMTEXT NULL`      | A JSON map of key-value pairs and appears as its own property to allow for denylisting fields or values. For example:```none
"cookies": "amlbcookie=01;
iPlanetDirectoryPro=\"AQIC5wM2LY....*AAJTSQACMfwT...*\";
iPlanetDirectoryPro=eyJ0eXAiOiJK....eyJzdWIiOiJkZ..."
```The line feeds and truncated values in the example are for readability purposes.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `http_response_headers`        | `MEDIUMTEXT NULL`      | Captures the headers returned by AM to the client (that is, the inverse of `http_request_headers`). AM doesn't currently populate this field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `response_status`              | `VARCHAR(10) NULL`     | The response status of the request. For example, `SUCCESS`, `FAILURE`, `ALLOWED`, `DENIED`, or `NULL`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `response_statuscode`          | `VARCHAR(255) NULL`    | The response status code, depending on the protocol.For common REST, HTTP failure codes are displayed but not HTTP success codes.For PLL endpoints, PLL error codes are displayed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `response_detail`              | `TEXT NULL`            | The message associated with the response status code. For example, a response status code of 401 has a response detail of `{ "reason": "Unauthorized" }`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `response_elapsedtime`         | `VARCHAR(255) NULL`    | The time to execute the access event, usually in millisecond precision.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `response_elapsedtimeunits`    | `VARCHAR(255) NULL`    | The elapsed time units of the response. For example, `MILLISECONDS`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `component`                    | `VARCHAR(255) NULL`    | The AM service utilized. For example, `Server Info`, `Users`, `Config`, `Session`, `Authentication`, `Policy`, `OAuth`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `realm`                        | `VARCHAR(255) NULL`    | The realm where the operation occurred. For example, the Top Level Realm (`/`) or the sub-realm name (`/alpha`).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

### am\_auditauthentication

| Column          | Datatype               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `id`            | `VARCHAR(56) NOT NULL` | A universally unique identifier (UUID) for the message object, such as `a568d4fe-d655-49a8-8290-bfc02095bec9-491`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `timestamp_`    | `VARCHAR(29) NULL`     | The timestamp when AM logged the message, in UTC format to millisecond precision: `yyyy-MM-ddTHH:mm:ss.msZ`. For example: `2025-03-14T00:16:04.653Z`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `transactionid` | `VARCHAR(255) NULL`    | The UUID of the transaction, which identifies an external request when it comes into the system boundary. Any events generated while handling that request will be assigned that transaction ID, so that you may see the same transaction ID for different audit event topics. For example, `9c9e8d5c-2941-4e61-9c3c-8a990088e801`.Trusted AM deployments with multiple instances, components, and Ping Advanced Identity Software products can propagate a transaction ID through each call across the platform. AM reads the `X-ForgeRock-TransactionId` HTTP header and appends an integer to the transaction ID. Note that this feature is disabled by default. When enabled, this feature should filter the `X-ForgeRock-TransactionId` HTTP header for connections from untrusted sources. |
| `eventname`     | `VARCHAR(255) NULL`    | The name of the audit event. For example, `AM-NODE-LOGIN-COMPLETED` and `AM-LOGOUT`. Find a list of audit event names in [Audit log events](#audit-log-event-names).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `userid`        | `VARCHAR(255) NULL`    | The universal identifier for authenticated users. For example, `id=bjensen,ou=user,o=alpha,ou=services,dc=example,dc=com`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `trackingids`   | `MEDIUMTEXT`           | The tracking IDs of the event, used by all topics.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `result`        | `VARCHAR(255) NULL`    | The result for an authentication tree.Possible values are `SUCCESSFUL` or `FAILED`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `principals`    | `MEDIUMTEXT`           | The array of accounts used to authenticate, such as `[ "amadmin" ]` and `[ "bjensen" ]`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `context`       | `MEDIUMTEXT`           | Not used.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `entries`       | `MEDIUMTEXT`           | The JSON representation of the authentication tree or node details. AM creates an event as each node completes and a final event at the end of the tree. For example:```json
{
  "entries": [
    {
      "info": {
        "nodeOutcome": "outcome",
        "treeName": "ldapService",
        "displayName": "User Name Collector",
        "nodeType": "UsernameCollectorNode",
        "nodeId": "cfcd2084-95d5-35ef-a6e7-dff9f98764db",
        "version": "2.0",
        "authLevel": "0"
      }
    }
  ]
}
```	By default, version is logged only for node versions greater than 1.0. To log version for all node versions, add the org.forgerock.am.auth.node.versioning.enable.v1.audit.detail advanced server property and set it to true.                                          |
| `component`     | `VARCHAR(255) NULL`    | The AM service utilized. For example, `Server Info`, `Users`, `Config`, `Session`, `Authentication`, `Policy`, `OAuth`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `realm`         | `VARCHAR(255) NULL`    | The realm where the operation occurred. For example, the Top Level Realm (`/`) or the sub-realm name (`/alpha`).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

### am\_auditactivity

| Column          | Datatype               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| --------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `id`            | `VARCHAR(56) NOT NULL` | A universally unique identifier (UUID) for the message object, such as `a568d4fe-d655-49a8-8290-bfc02095bec9-491`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `timestamp_`    | `VARCHAR(29) NOT NULL` | The timestamp when AM logged the message, in UTC format to millisecond precision: `yyyy-MM-ddTHH:mm:ss.msZ`. For example: `2025-03-14T00:16:04.653Z`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `transactionid` | `VARCHAR(255) NULL`    | The UUID of the transaction, which identifies an external request when it comes into the system boundary. Any events generated while handling that request will be assigned that transaction ID, so that you may see the same transaction ID for different audit event topics. For example, `9c9e8d5c-2941-4e61-9c3c-8a990088e801`.Trusted AM deployments with multiple instances, components, and Ping Advanced Identity Software products can propagate a transaction ID through each call across the platform. AM reads the `X-ForgeRock-TransactionId` HTTP header and appends an integer to the transaction ID. Note that this feature is disabled by default. When enabled, this feature should filter the `X-ForgeRock-TransactionId` HTTP header for connections from untrusted sources.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `eventname`     | `VARCHAR(255) NULL`    | The name of the audit event. For example, `AM-SESSION-CREATED` and `AM-SESSION-DESTROYED`. Find a list of audit event names in [Audit log events](#audit-log-event-names).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `userid`        | `VARCHAR(255) NULL`    | The universal identifier for authenticated users. For example, `id=bjensen,ou=user,o=alpha,ou=services,dc=example,dc=com`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `trackingids`   | `MEDIUMTEXT`           | The tracking IDs of the event, used by all topics.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `runas`         | `VARCHAR(255) NULL`    | The user to run the activity as. May be used in delegated administration. For example, `id=amadmin,ou=user,ou=am-config`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `objectid`      | `VARCHAR(255) NULL`    | The identifier of a system object that has been created, modified, or deleted. For example, `ou=iPlanetAMAuthService,ou=services,o=alpha,ou=services,dc=example,dc=com`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `operation`     | `VARCHAR(255) NULL`    | The state change operation invoked: `CREATE`, `MODIFY`, or `DELETE`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `beforeObject`  | `MEDIUMTEXT NULL`      | The JSON representation of the object prior to the activity. For example:```json
{
    "sunKeyValue": [
      "entryNodeId=e301438c-0bd0-429c-ab0c-66126501069a",
      "nodes={}",
      "staticNodes={}"
    ]
}
```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `afterObject`   | `MEDIUMTEXT NULL`      | The JSON representation of the object after the activity. For example:```json
{
    "sunKeyValue": [
      "entryNodeId=8058f432-b319-410b-afbb-c532f9a111b7",
      "innerTreeOnly=false",
      "enabled=true",
      "noSession=false",
      "mustRun=false",
      "uiConfig=",
      "staticNodes={\"startNode\":{\"x\":50,\"y\":25},\"70e691a5-1e33-4ac3-a356-e7b6d60d92e0\":{\"x\":777,\"y\":377},\"e301438c-0bd0-429c-ab0c-66126501069a\":{\"x\":1087,\"y\":109}}",
      "nodes={\"4c8bb786-80c5-424b-b75f-b66e54741177\":{\"displayName\":\"Password Collector\",\"nodeType\":\"PasswordCollectorNode\",\"x\":214,\"y\":178.984375,\"connections\":{\"outcome\":\"cd0253de-f473-45fc-a431-78575c2b2a4f\"}},\"8058f432-b319-410b-afbb-c532f9a111b7\":{\"displayName\":\"Username Collector\",\"nodeType\":\"UsernameCollectorNode\",\"x\":206,\"y\":123.984375,\"connections\":{\"outcome\":\"4c8bb786-80c5-424b-b75f-b66e54741177\"}},\"cd0253de-f473-45fc-a431-78575c2b2a4f\":{\"displayName\":\"Data Store Decision\",\"nodeType\":\"DataStoreDecisionNode\",\"x\":599,\"y\":198.984375,\"connections\":{\"true\":\"70e691a5-1e33-4ac3-a356-e7b6d60d92e0\",\"false\":\"e301438c-0bd0-429c-ab0c-66126501069a\"}}}"
    ]
}
``` |
| `changedfields` | `VARCHAR(255) NULL`    | The columns that were changed. For example, `[ "nodes" ]`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `rev`           | `VARCHAR(255) NULL`    | Not used.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `component`     | `VARCHAR(255) NULL`    | The AM service utilized. For example, `Server Info`, `Users`, `Config`, `Session`, `Authentication`, `Policy`, `OAuth`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `realm`         | `VARCHAR(255) NULL`    | The realm where the operation occurred. For example, the Top Level Realm (`/`) or the sub-realm name (`/alpha`).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

### am\_auditconfig

| Column          | Datatype               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| --------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `id`            | `VARCHAR(56) NOT NULL` | A universally unique identifier (UUID) for the message object, such as `a568d4fe-d655-49a8-8290-bfc02095bec9-491`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `timestamp_`    | `VARCHAR(29) NULL`     | The timestamp when AM logged the message, in UTC format to millisecond precision: `yyyy-MM-ddTHH:mm:ss.msZ`. For example: `2025-03-14T00:16:04.653Z`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `transactionid` | `VARCHAR(255) NULL`    | The UUID of the transaction, which identifies an external request when it comes into the system boundary. Any events generated while handling that request will be assigned that transaction ID, so that you may see the same transaction ID for different audit event topics. For example, `9c9e8d5c-2941-4e61-9c3c-8a990088e801`.Trusted AM deployments with multiple instances, components, and Ping Advanced Identity Software products can propagate a transaction ID through each call across the platform. AM reads the `X-ForgeRock-TransactionId` HTTP header and appends an integer to the transaction ID. Note that this feature is disabled by default. When enabled, this feature should filter the `X-ForgeRock-TransactionId` HTTP header for connections from untrusted sources.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `eventname`     | `VARCHAR(255) NULL`    | The name of the audit event. For example, `AM-CONFIG-CHANGE`. Find a list of audit event names in [Audit log events](#audit-log-event-names).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `userid`        | `VARCHAR(255) NULL`    | The universal identifier for authenticated users. For example, `id=bjensen,ou=user,o=alpha,ou=services,dc=example,dc=com`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `trackingids`   | `MEDIUMTEXT`           | The tracking IDs of the event, used by all topics.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `runas`         | `VARCHAR(255) NULL`    | The user to run the activity as. May be used in delegated administration. For example, `id=amadmin,ou=user,ou=am-config`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `objectid`      | `VARCHAR(255) NULL`    | The identifier of a system object that has been created, modified, or deleted. For example, `ou=iPlanetAMAuthService,ou=services,o=alpha,ou=services,dc=example,dc=com`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `operation`     | `VARCHAR(255) NULL`    | The state change operation invoked: `CREATE`, `MODIFY`, or `DELETE`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `beforeObject`  | `MEDIUMTEXT NULL`      | The JSON representation of the object prior to the activity. For example:```json
{
    "sunKeyValue": [
      "entryNodeId=e301438c-0bd0-429c-ab0c-66126501069a",
      "nodes={}",
      "staticNodes={}"
    ]
}
```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `afterObject`   | `MEDIUMTEXT NULL`      | The JSON representation of the object after the activity. For example:```json
{
    "sunKeyValue": [
      "entryNodeId=8058f432-b319-410b-afbb-c532f9a111b7",
      "innerTreeOnly=false",
      "enabled=true",
      "noSession=false",
      "mustRun=false",
      "uiConfig=",
      "staticNodes={\"startNode\":{\"x\":50,\"y\":25},\"70e691a5-1e33-4ac3-a356-e7b6d60d92e0\":{\"x\":777,\"y\":377},\"e301438c-0bd0-429c-ab0c-66126501069a\":{\"x\":1087,\"y\":109}}",
      "nodes={\"4c8bb786-80c5-424b-b75f-b66e54741177\":{\"displayName\":\"Password Collector\",\"nodeType\":\"PasswordCollectorNode\",\"x\":214,\"y\":178.984375,\"connections\":{\"outcome\":\"cd0253de-f473-45fc-a431-78575c2b2a4f\"}},\"8058f432-b319-410b-afbb-c532f9a111b7\":{\"displayName\":\"Username Collector\",\"nodeType\":\"UsernameCollectorNode\",\"x\":206,\"y\":123.984375,\"connections\":{\"outcome\":\"4c8bb786-80c5-424b-b75f-b66e54741177\"}},\"cd0253de-f473-45fc-a431-78575c2b2a4f\":{\"displayName\":\"Data Store Decision\",\"nodeType\":\"DataStoreDecisionNode\",\"x\":599,\"y\":198.984375,\"connections\":{\"true\":\"70e691a5-1e33-4ac3-a356-e7b6d60d92e0\",\"false\":\"e301438c-0bd0-429c-ab0c-66126501069a\"}}}"
    ]
}
``` |
| `changedfields` | `VARCHAR(255) NULL`    | The columns that were changed. For example, `[ "nodes" ]`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `rev`           | `VARCHAR(255)`         | Not used.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `component`     | `VARCHAR(255) NULL`    | The AM service utilized. For example, `Server Info`, `Users`, `Config`, `Session`, `Authentication`, `Policy`, `OAuth`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `realm`         | `VARCHAR(255) NULL`    | The realm where the operation occurred. For example, the Top Level Realm (`/`) or the sub-realm name (`/alpha`).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

---

---
title: Common REST monitoring
description: Query PingAM monitoring metrics using the common REST framework at the `/json/metrics/api` endpoint
component: pingam
version: 8.1
page_id: pingam:monitoring:monitoring-crest
canonical_url: https://docs.pingidentity.com/pingam/8.1/monitoring/monitoring-crest.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["REST API", "Monitoring"]
page_aliases: ["maintenance-guide:monitoring-crest.adoc", "monitoring-guide:monitoring-crest.adoc"]
section_ids:
  enable-crest: Enable the common REST monitoring interface
---

# Common REST monitoring

Common REST refers to the REST framework supported by all Ping Advanced Identity Software products. AM exposes an endpoint that lets REST clients gather information about your AM installation in JSON format.

When [enabled](#enable-crest), AM makes the common REST-formatted metrics available at the `/json/metrics/api` endpoint.

For example, to query all monitoring metrics:

```bash
$ curl \
--request GET \
--header 'Content-Type: application/json' \
--header 'iPlanetDirectoryPro: P8Eri6d…​xAAA.*' \
'https://am.example.com:8443/am/json/metrics/api?_queryFilter=true&_prettyPrint=true'
{
  "result" : [ {
    "_id" : "session.authentication-client-based.get-matching-sessions.failure",
    "count" : 0,
    "max" : 0.0,
    "mean" : 0.0,
    "min" : 0.0,
    "p50" : 0.0,
    "p75" : 0.0,
    "p95" : 0.0,
    "p98" : 0.0,
    "p99" : 0.0,
    "p999" : 0.0,
    "stddev" : 0.0,
    "m15_rate" : 0.0,
    "m1_rate" : 0.0,
    "m5_rate" : 0.0,
    "mean_rate" : 0.0,
    "duration_units" : "milliseconds",
    "rate_units" : "calls/second",
    "total" : 0.0,
    "_type" : "timer"
  },
  …​
```

To output values for a specific metric, use the format `/json/metric/api/metric name`.

For example:

```bash
$ curl \
--request GET \
--header 'Content-Type: application/json' \
--header 'iPlanetDirectoryPro: P8Eri6d…​xAAA.*' \
'https://am.example.com:8443/am/json/metrics/api/authentication.success'
{
    "_id":"authentication.success",
    "m15_rate":2.3882880682497324E-4,
    "m1_rate":1.0818067450729532E-12,
    "m5_rate":3.057223961594952E-5,
    "mean_rate":1.072595825176473E-4,
    "units":"events/second",
    "total":9.0,
    "count":9,
    "_type":"summary"
}
```

For monitoring metrics reference, refer to [Monitoring metrics](monitoring-metrics.html).

## Enable the common REST monitoring interface

1. Ensure you have [enabled monitoring](monitoring-am.html#enable-monitoring).

2. Go to Configure > Global Services > Monitoring.

3. On the Secondary Configurations tab, click `crest`.

4. Set CREST to Enabled.

5. Click Save Changes.

---

---
title: Debug logging
description: Enable debug logging in PingAM to troubleshoot issues, configure logging levels for specific classes, and choose between temporary Logback.jsp settings or persistent logback.xml configuration
component: pingam
version: 8.1
page_id: pingam:monitoring:debug-logging
canonical_url: https://docs.pingidentity.com/pingam/8.1/monitoring/debug-logging.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Troubleshooting"]
page_aliases: ["maintenance-guide:debug-logging.adoc", "monitoring-guide:debug-logging.adoc"]
section_ids:
  to-enable-debug-logging-logback: Temporarily enable debug logging with Logback.jsp
  persistent-logging-logback-xml: Persistent debug logging with logback.xml
  config-basic-logging: Configure basic debug logging
  output-stdout: Output to stdout
  output-multiple-locations: Output to multiple locations
  format-log-files: Format log files
  control-exception-log-length: Control exception log length
  log-rotate-debug: Rotate debug logs
  log-debug-defaults: Change the startup debug settings
  log-debug-levels: Set the default debug level
  log-debug-directory: Set the default debug directory
  log-debug-single-file: Combine log messages in a single file
---

# Debug logging

AM services capture a variety of information in debug logs. Unlike audit log records, debug log records are unstructured. Debug logs contain different types of information that is useful when troubleshooting AM, including stack traces.

AM uses [Logback](https://logback.qos.ch/) as the handler for debug logging, making it easily customizable. For example, the level of debug log record output is configurable, as is the storage location and format.

AM lets you enable the debug log level for specific classes in the AM code base. This can be useful when you must turn on debug logging in a production system where you want to avoid excessive logging, but must gather messages when you reproduce a problem.

You can choose the level of logging from the following options:

* `Off`

  No debug messages are logged.

* `Error`

  Debug messages signifying that an error has occurred are logged.

  This is the default level.

* `Warning`

  Debug messages signifying potentially harmful situations are logged.

* `Information`

  Debug messages that contain coarse-grained information about the status of AM are logged.

* `Debug`

  Debug messages that contain fine-grained information useful for troubleshooting AM are logged.

* `Trace`

  All debug messages are logged.

Create *loggers* to specify the debug level for a class, and choose where the output is recorded. The logger used by a feature in AM is hierarchical, based on the class creating the debug messages. The most specific logger is used, which is the logger whose path most closely matches the class that is creating the log messages.

For example, if you knew there was an issue in an authentication node, you could enable trace-level debug logging in `org.forgerock.openam.core.rest.authn.trees`. If you aren't sure where the problem lies, you can choose a broader option, for example `org.forgerock.openam.core.rest.authn`.

The least-specific, catch-all logger is named `ROOT`.

AM also logs information related to client interactions using the `org.apache.http.wire` and `org.apache.http.headers` appenders. The information they collect is useful, for example, when you are developing authentication scripts or when your environment requires STS transformations.

By default, these appenders are always set to the `Warning` level unless logging is disabled.

Learn more in the [org.forgerock.allow.http.client.debug](../setup/deployment-configuration-reference.html#appenders-debug) advanced server property.

You can configure debug logging temporarily by using the AM admin UI, or you can create a file in the AM classpath with persistent debug configuration.

## Temporarily enable debug logging with `Logback.jsp`

These steps let you temporarily capture debug messages, until the next time AM or the container in which it runs is restarted.

1. In the AM admin UI, go to `Logback.jsp` in the root context of the AM installation, for example `https://am.example.com:8443/am/Logback.jsp`.

   No links to this page are provided in the AM admin UI.

   |   |                                                                                                                                                      |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Only the `amAdmin` administrator account can access the `Logback.jsp` page and alter the debug settings; delegated administrators don't have access. |

   The page displays all the appenders and their associated debug loggers.

   > **Collapse: Logback.jsp logger names**
   >
   > The following lists contain the available logger names ordered by their associated appender:
   >
   > > **Collapse: Authentication**
   > >
   > > ```
   > > Authentication service, framework, Auth modules, Callbacks, JAAS, API
   > > com.sun.identity.authentication.spi.AMLoginModule,
   > > org.forgerock.openam.core.rest.authn.callbackhandlers,
   > > com.sun.identity.authentication.spi.AMAuthCallBackImpl,
   > > com.sun.identity.authentication.service.AuthContextLookup,
   > > com.sun.identity.authentication.util,
   > > org.forgerock.openam.authentication.service.LoginContextFactory,
   > > com.sun.identity.authentication.server.AuthContextLocal,
   > > com.sun.identity.authentication.service.AMAccountLockout,
   > > com.sun.identity.authentication.service.LoginState,
   > > com.sun.identity.authentication.UI.LoginViewBean,
   > > com.sun.identity.authentication.client,
   > > org.forgerock.openam.core.rest.authn.trees,
   > > com.sun.identity.authentication.spi.FirstTimeLogin,
   > > org.forgerock.openam.auth,
   > > org.forgerock.openam.authentication.service.SessionPropertyUpgrader,
   > > com.sun.identity.authentication.UI.AuthExceptionViewBean,
   > > com.sun.identity.authentication.spi.ReplayPasswd,
   > > com.sun.identity.authentication.config,
   > > com.sun.identity.authentication.share,
   > > org.forgerock.openam.authentication.SessionUpgradeVerifier,
   > > com.sun.identity.authentication.service.DSAMECallbackHandler,
   > > com.sun.identity.authentication.spi.AMModuleProperties,
   > > org.forgerock.openam.utils.MappingUtils,
   > > com.sun.identity.authentication.UI.AuthenticationServletBase,
   > > com.sun.identity.authentication.service.AuthenticationPrincipalDataRetrieverFactory,
   > > com.sun.identity.authentication.UI.LogoutViewBean,
   > > com.iplanet.security,
   > > com.sun.identity.authentication.internal,
   > > com.sun.identity.authentication.AuthContext,
   > > com.sun.identity.policy.plugins.AuthenticatedSharedAgents,
   > > org.forgerock.openam.ldap.LDAPAuthUtils,
   > > com.sun.identity.authentication.UI.AuthViewBeanBase,
   > > org.forgerock.openam.authentication.modules,
   > > com.iplanet.services.cdm,
   > > org.forgerock.openam.authentication.service.AuthUtilsWrapper,
   > > com.sun.identity.policy.plugins.AuthenticatedAgents,
   > > com.sun.identity.authentication.spi.JwtReplayPassword,
   > > com.sun.identity.policy.plugins.AllowedAgents,
   > > com.sun.identity.authentication.service.AuthenticationServiceAttributeCache,
   > > com.sun.identity.authentication.jaas,
   > > com.sun.identity.authentication.service.AuthD,
   > > org.forgerock.openam.core.rest.authn.core,
   > > org.forgerock.openam.scripting.api,
   > > com.sun.identity.common.ISAccountLockout,
   > > org.forgerock.openam.core.rest.authn.RestAuthCallbackHandlerFactory,
   > > org.forgerock.openam.core.rest.authn.RestAuthCallbackHandlerManager,
   > > org.forgerock.openam.webhook,
   > > com.iplanet.services.cdc,
   > > com.sun.identity.authentication.modules,
   > > org.forgerock.openam.core.rest.authn.http.AuthenticationServiceV1,
   > > com.sun.identity.authentication.service.AuthUtils,
   > > com.sun.identity.policy.plugins.AuthenticatedSharedAgentsCondition,
   > > org.forgerock.openam.authentication.service.JAASModuleDetector,
   > > org.forgerock.openam.core.rest.authn.RestAuthenticationHandler
   > > ```
   >
   > > **Collapse: Configuration**
   > >
   > > ```
   > > Service Configuration, Delegation, SMS Schema, SMS repository, plugins
   > > com.sun.identity.sm.ServiceSchemaManager,
   > > com.iplanet.services.ldap.event.EventService,
   > > com.sun.identity.sm.SMSSchema,
   > > com.sun.identity.tools,
   > > com.sun.identity.sm.SMSUtils,
   > > com.sun.identity.common.configuration.ServerConfigXMLObserver,
   > > com.sun.identity.sm.ServiceSchema,
   > > com.sun.identity.delegation,
   > > com.sun.identity.sm.OrganizationConfigManager,
   > > com.sun.identity.sm.ldap,
   > > com.sun.identity.sm.SMSNotificationManager,
   > > com.sun.identity.sm.PluginSchema,
   > > com.sun.identity.sm.AttributeValidator,
   > > com.sun.identity.sm.ServiceConfigManagerImpl,
   > > com.sun.identity.sm.ServiceConfigImpl,
   > > com.sun.identity.sm.SMSPropertiesObserver,
   > > com.sun.identity.sm.OrganizationConfigManagerImpl,
   > > com.sun.identity.sm.AuthenticationServiceNameProviderImpl,
   > > org.forgerock.openam.xui.XUIFilter,
   > > com.sun.identity.sm.ServiceSchemaImpl,
   > > com.sun.identity.setup,
   > > com.sun.identity.sm.AttributeSchemaState,
   > > com.sun.identity.sm.ServiceInstanceImpl,
   > > org.forgerock.openam.auditors,
   > > com.sun.identity.workflow,
   > > com.sun.identity.sm.ServiceConfigManager,
   > > org.forgerock.openam.sm.validation,
   > > com.sun.identity.common.configuration.SessionSiteNames,
   > > com.sun.identity.sm.ServiceConfig,
   > > com.sun.identity.sm.SMServlet,
   > > com.sun.identity.sm.ServiceManager,
   > > com.sun.identity.common.configuration.ServerPropertyValidator,
   > > com.sun.identity.sm.SMSEntry,
   > > com.sun.identity.sm.PluginConfig,
   > > org.forgerock.openam.utils.OpenAMSettingsImpl,
   > > com.sun.identity.sm.jaxrpc,
   > > com.sun.identity.sm.DNMapper,
   > > com.sun.identity.sm.SMSException,
   > > com.sun.identity.sm.SMSEventListenerManager,
   > > org.forgerock.openam.utils.MapHelper,
   > > com.sun.identity.sm.ServiceInstance,
   > > com.sun.identity.config.util,
   > > com.sun.identity.sm.CachedSubEntries,
   > > com.sun.identity.sm.PluginConfigImpl,
   > > com.sun.identity.authentication.service.ConfiguredSocialAuthServices,
   > > com.sun.identity.sm.ServiceSchemaManagerImpl,
   > > com.sun.identity.sm.CachedSMSEntry,
   > > com.sun.identity.sm.CreateServiceConfig,
   > > com.sun.identity.sm.AttributeSchema,
   > > com.sun.identity.sm.PluginSchemaImpl
   > > ```
   >
   > > **Collapse: CoreSystem**
   > >
   > > ```
   > > Core infrastructure services, PLL, cookies, naming, logging, upgrade, Scripting
   > > com.sun.identity.monitoring,
   > > com.sun.identity.saml2.idpdiscovery,
   > > com.sun.identity.security.cert.CRLValidator,
   > > org.forgerock.openam.xacml.v3.rest,
   > > org.forgerock.openam.core.rest.SelfServiceUserUiRolePredicate,
   > > org.forgerock.openam.core.rest.cts,
   > > org.forgerock.openam.sm.datalayer.impl.ldap.LdapSearchHandler,
   > > org.forgerock.openam.security,
   > > com.sun.identity.plugin.monitoring.impl,
   > > org.forgerock.openam.sm.datalayer.providers,
   > > com.zaxxer.hikari,
   > > org.forgerock.openam.uma.UmaUserUiRolePredicate,
   > > com.sun.identity.common.RequestUtils,
   > > org.forgerock.openam.entitlement.rest.SubjectAttributesResourceV1,
   > > org.forgerock.openam.services.baseurl,
   > > org.forgerock.openam.core.rest.IdentityRestUtils,
   > > org.forgerock.openam.core.rest.UserGroupsResource,
   > > org.forgerock.openam.oauth2.rest,
   > > com.sun.identity.authentication.UI.taglib,
   > > org.forgerock.openam.core.rest.docs,
   > > com.sun.identity.log,
   > > org.forgerock.openam.core.rest.AllAuthenticatedUsersResource,
   > > org.forgerock.openam.utils.WhitelistObjectInputStream,
   > > org.forgerock.openam.core.rest.dashboard,
   > > com.sun.identity.common.SystemTimerPool,
   > > org.forgerock.openam.core.rest.session.AnyOfAuthzModule,
   > > org.forgerock.openam.rest,
   > > org.forgerock.openam.core.rest.sms,
   > > com.sun.identity.common.admin,
   > > org.forgerock.openam.shared.resourcename,
   > > com.sun.identity.security.AdminTokenAction,
   > > org.forgerock.openam.uma.rest.UmaPolicyResourceAuthzFilter,
   > > org.forgerock.openam.shared.concurrency,
   > > org.forgerock.openam.core.rest.session.SessionResourcePrivilegeAuthzModule,
   > > org.forgerock.openam.entitlement.rest.ResourceTypesResource,
   > > org.forgerock.openam.uma.rest.UmaPolicyServiceImpl,
   > > org.forgerock.openam.entitlement.rest.DecisionCombinersResource,
   > > com.sun.identity.common.HttpURLConnectionManager,
   > > org.forgerock.openam.sm.datalayer.impl.SeriesTaskExecutor,
   > > org.forgerock.openam.network.ipv4.IPv4AddressRange,
   > > org.forgerock.openam.audit,
   > > org.forgerock.audit,
   > > com.sun.identity.common.DNUtils,
   > > org.forgerock.openam.utils.IPRange,
   > > org.forgerock.openam.services.RestSecurity,
   > > org.forgerock.openam.core.rest.IdentityResourceV4,
   > > org.forgerock.openam.core.rest.IdentityResourceV3,
   > > com.sun.identity.security.SecurityDebug,
   > > org.forgerock.openam.backstage,
   > > org.forgerock.openam.core.rest.server,
   > > org.forgerock.openam.utils.ClientUtils,
   > > org.forgerock.openam.core.rest.IdentityResourceV2,
   > > org.forgerock.openam.entitlement.rest.ApplicationV1Filter,
   > > org.forgerock.openam.core.rest.IdentityResourceV1,
   > > org.forgerock.openam.core.rest.devices,
   > > org.forgerock.openam.entitlement.rest.ApplicationsResource,
   > > com.sun.identity.policy.util.Gateway,
   > > com.sun.identity.shared.jaxrpc,
   > > org.forgerock.openam.forgerockrest,
   > > com.iplanet.am.util,
   > > com.iplanet.services.comm,
   > > org.forgerock.openam.core.rest.authn.AuditHelper,
   > > org.forgerock.openam.sm.datalayer.impl.PooledTaskExecutor,
   > > org.forgerock.openam.ldap.LdifUtils,
   > > org.forgerock.openam.core.rest.session.action.LogoutByHandleActionHandler,
   > > org.forgerock.openam.sm.datalayer.impl.ldap.LdapQueryBuilder,
   > > com.sun.identity.shared.search,
   > > org.forgerock.openam.entitlement.rest.SubjectTypesResource,
   > > com.sun.identity.shared.encode.CookieUtils,
   > > com.iplanet.services.naming,
   > > org.forgerock.openam.cors,
   > > com.sun.identity.idsvcs,
   > > com.sun.identity.jaxrpc,
   > > org.forgerock.openam.http,
   > > org.forgerock.openam.shared.guice,
   > > org.forgerock.openam.utils.AMKeyProvider,
   > > org.forgerock.openam.utils.AuthLevelUtils,
   > > org.forgerock.openam.shared.security.whitelist,
   > > org.forgerock.openam.notifications,
   > > com.sun.identity.policy.util.GatewayServletUtils,
   > > org.forgerock.openam.core.sms,
   > > org.forgerock.openam.blacklist,
   > > com.sun.identity.common.configuration.AgentConfiguration,
   > > org.forgerock.openam.entitlement.rest.ApplicationTypesResource,
   > > org.forgerock.openam.monitoring,
   > > com.sun.identity.common.ResourceLookup,
   > > org.forgerock.openam.entitlement.rest.PolicyV1Filter,
   > > com.sun.identity.authentication.server.AuthXMLRequestParser,
   > > org.forgerock.openam.entitlement.rest.wrappers,
   > > com.sun.identity.security.cert.AMCertStore,
   > > org.forgerock.openam.sm.datalayer.impl.SimpleTaskExecutor,
   > > com.sun.identity.shared.locale,
   > > com.sun.identity.shared.whitelist,
   > > org.forgerock.openam.sm.datalayer.impl.ldap.CTSDJLDAPv3PersistentSearch,
   > > com.sun.identity.protocol,
   > > org.forgerock.openam.scripting.rest,
   > > org.forgerock.openam.entitlement.rest.ConditionTypesResource,
   > > org.forgerock.openam.core.rest.record,
   > > com.sun.identity.security.cert.AMCertPath,
   > > org.forgerock.openam.utils.ServiceConfigUtils,
   > > com.sun.identity.authentication.server.AuthXMLRequest
   > > ```
   >
   > > **Collapse: Federation**
   > >
   > > ```
   > > Federated SSO, protocols (WS-Federation, SAML2), Metadata, Hub, Circle of Trust
   > > com.sun.identity.wsfederation.profile,
   > > com.sun.identity.saml2.servlet,
   > > com.sun.identity.saml2.plugins.SAML2PluginsUtils,
   > > com.sun.identity.plugin.datastore,
   > > com.sun.identity.saml2.logging,
   > > com.sun.identity.saml2.protocol,
   > > com.sun.identity.saml2.common,
   > > com.sun.identity.saml2.plugins.DefaultAccountMapper,
   > > org.forgerock.openam.federation,
   > > com.sun.identity.wsfederation.plugins.DefaultSPAttributeMapper,
   > > com.sun.identity.saml2.plugins.DefaultSPAccountMapper,
   > > com.sun.identity.wsfederation.plugins.whitelist,
   > > com.sun.identity.saml2.profile,
   > > com.sun.identity.wsfederation.plugins.DefaultLibrarySPAccountMapper,
   > > com.sun.identity.saml2.plugins.SAML2IDPProxyFRImpl,
   > > com.sun.identity.wsfederation.key,
   > > com.sun.identity.multiprotocol,
   > > com.sun.identity.saml2.plugins.SAML2IDPProxyImpl,
   > > com.sun.identity.wsfederation.servlet,
   > > com.sun.identity.xacml,
   > > com.sun.identity.plugin.monitoring.MonitorManager,
   > > com.sun.identity.saml2.plugins.DefaultIDPAuthnContextMapper,
   > > com.sun.identity.wsfederation.plugins.DefaultAccountMapper,
   > > com.sun.identity.saml2.plugins.DefaultAttributeMapper,
   > > com.sun.identity.wsfederation.plugins.DefaultAttributeMapper,
   > > org.forgerock.openam.authentication.Saml2SessionUpgradeHandler,
   > > com.sun.identity.saml2.ecp,
   > > org.forgerock.openam.wsfederation,
   > > com.sun.identity.federation,
   > > org.forgerock.openam.saml2,
   > > jsp.saml2,
   > > com.sun.identity.saml2.plugins.DefaultIDPECPSessionMapper,
   > > com.sun.identity.saml2.plugins.DefaultLibrarySPAccountMapper,
   > > com.sun.identity.plugin.log,
   > > com.sun.identity.saml,
   > > com.sun.identity.wsfederation.meta,
   > > com.sun.identity.wsfederation.plugins.DefaultIDPAuthenticationMethodMapper,
   > > com.sun.identity.saml2.plugins.DefaultFedletAdapter,
   > > com.sun.identity.saml2.plugins.DefaultLibraryIDPAttributeMapper,
   > > com.sun.identity.saml2.xmlenc,
   > > com.sun.identity.saml2.plugins.DefaultSPAttributeMapper,
   > > com.sun.identity.saml2.plugins.DefaultSPAuthnContextMapper,
   > > com.sun.identity.saml2.xmlsig,
   > > com.sun.identity.liberty.ws.security,
   > > com.sun.identity.plugin.session.SessionManager,
   > > com.sun.identity.wsfederation.plugins.DefaultIDPAccountMapper,
   > > com.sun.identity.plugin.session.impl.FMSessionProvider,
   > > com.sun.identity.saml2.key,
   > > com.sun.identity.wsfederation.logging,
   > > com.sun.identity.saml2.plugins.DefaultIDPAccountMapper,
   > > com.sun.identity.wsfederation.plugins.DefaultADFSPartnerAccountMapper,
   > > com.sun.identity.saml2.assertion,
   > > com.sun.identity.wsfederation.plugins.DefaultIDPAttributeMapper,
   > > com.sun.identity.plugin.session.impl.FedletSessionProvider,
   > > com.sun.identity.saml2.meta,
   > > com.sun.identity.plugin.configuration,
   > > com.sun.identity.saml2.soapbinding,
   > > com.sun.identity.wsfederation.common,
   > > com.sun.identity.cot
   > > ```
   >
   > > **Collapse: IdRepo**
   > >
   > > ```
   > > Identity Repositories, Datastores, plugins
   > > com.sun.identity.common.ISResourceBundle,
   > > com.iplanet.am.sdk,
   > > org.forgerock.openam.idrepo.ldap.DJLDAPv3Repo,
   > > org.forgerock.openam.shared.security.crypto,
   > > com.iplanet.sso.SSOTokenManager,
   > > com.iplanet.services.ldap.DefaultDataStoreConfigurationManager,
   > > com.sun.identity.idm,
   > > org.forgerock.openam.idrepo.ldap.helpers.DirectoryHelper,
   > > com.sun.identity.shared.encode.Hash,
   > > org.forgerock.openam.core.realms,
   > > org.forgerock.openam.shared.security.ThreadLocalSecureRandom,
   > > com.iplanet.services.ldap.event.LDAPv3PersistentSearch,
   > > org.forgerock.openam.idrepo.ldap.psearch,
   > > com.sun.identity.security.ServerInstanceAction,
   > > org.forgerock.openam.identity,
   > > org.forgerock.openam.ldap.LDAPUtils
   > > ```
   >
   > > **Collapse: OAuth2Provider**
   > >
   > > ```
   > > OAuth 2.0 Provider
   > > org.forgerock.openam.oauth2.OpenAMClientRegistrationStore,
   > > org.forgerock.openam.oauth2.secrets,
   > > org.forgerock.openidconnect,
   > > org.forgerock.openam.oauth2.resources.ResourceSetLabelRegistration,
   > > org.forgerock.openam.oauth2.OAuth2GlobalSettings,
   > > org.forgerock.openam.oauth2.OpenAMClientRegistration,
   > > org.forgerock.openam.oauth2.ciba,
   > > org.forgerock.openam.oauth2.requesturis,
   > > org.forgerock.openam.oauth2.OAuth2AuditLogger,
   > > org.forgerock.openam.oauth2.token,
   > > org.forgerock.openam.oauth2.IdentityManager,
   > > org.forgerock.openam.oauth2.IgAgentClientRegistration,
   > > org.forgerock.openam.oauth2.jwks,
   > > org.forgerock.oauth2,
   > > org.forgerock.openam.utils.RealmNormaliser,
   > > org.forgerock.openam.oauth2.AgentClientRegistration,
   > > org.forgerock.openam.oauth2.ClientCredentialsReader,
   > > org.forgerock.openam.oauth2.remoteconsent,
   > > org.forgerock.openam.oauth2.OpenAMScopeValidator,
   > > org.forgerock.openam.oauth2.OAuth2Monitor
   > > ```
   >
   > > **Collapse: OpenDJ-SDK**
   > >
   > > ```
   > > Directory Server SDK
   > > org.forgerock.opendj.ldif,
   > > org.forgerock.opendj.asn1,
   > > com.forgerock.opendj.util,
   > > com.forgerock.opendj.ldap,
   > > org.forgerock.opendj.ldap,
   > > org.forgerock.opendj.util
   > > ```
   >
   > > **Collapse: OtherLogging**
   > >
   > > ```
   > > Miscellaneous logs
   > > org.forgerock.openam.secrets.SecretIdChoiceValues,
   > > org.forgerock.am.iot.IntrospectTokenActionHandler,
   > > com.sun.identity.sm.SmsObjectResolver,
   > > org.forgerock.config.resolvers,
   > > org.forgerock.openam.services.datastore,
   > > org.forgerock.openam.utils.JCECipherProvider,
   > > org.forgerock.config.resolvers.SystemPropertyResolver,
   > > com.sun.identity.policy.plugins,
   > > org.forgerock.openam.entitlement.rest,
   > > org.forgerock.openam.services.datastore.DataStoreConsistencyFilter,
   > > org.forgerock.openam.oauth2.saml2,
   > > org.forgerock.secrets.propertyresolver.PropertyResolverSecretStore,
   > > org.forgerock.openam.headers.DisableSameSiteCookiesFilter,
   > > org.forgerock.openam.oauth2.resources,
   > > org.forgerock.openam.uma.rest,
   > > org.forgerock.openam.integration.idm.IdmClientIdRepo,
   > > org.forgerock.am.health.HealthCheckService,
   > > com.sun.identity.shared,
   > > org.forgerock.openam.network.ipv4,
   > > com.forgerock,
   > > org.forgerock.openam.core.rest.session,
   > > org.forgerock.util.encode.Base64url,
   > > org.forgerock.openam.core.rest,
   > > com.iplanet.services.ldap.ServerGroup,
   > > org.forgerock.am.iot.ThingsResource,
   > > org.forgerock.openam.uma,
   > > org.forgerock.openam.secrets.config.GoogleKeyManagementServiceSecretStore,
   > > org.forgerock.api.models.Resource,
   > > org.forgerock.openam.oauth2.saml2.core.Saml2GrantTypeHandler,
   > > com.sun.identity.configuration.ConfigFedMonitoring,
   > > org.forgerock.openam.setup.BootstrapSubstitutionService,
   > > org.forgerock.util.promise,
   > > org.forgerock.config.resolvers.EnvironmentVariableResolver,
   > > org.forgerock.config.util,
   > > org.forgerock.openam.scripting.ScriptEngineConfigurator,
   > > org.forgerock.openam.oauth2.guice,
   > > org.forgerock.openam.scripting.persistence,
   > > org.forgerock.api.models.Items,
   > > org.forgerock.openam.homedirectory.HomeDirectoryUtils,
   > > org.forgerock.openam.selfservice,
   > > com.iplanet.services,
   > > org.forgerock.openam.scripting.ThreadPoolScriptEvaluator,
   > > jsp,
   > > org.forgerock.am.health.ReadinessCheckEndpoint,
   > > io.swagger.models.parameters.AbstractSerializableParameter,
   > > org.forgerock.openam.social,
   > > com.sun.identity.plugin.monitoring,
   > > org.forgerock.openam.services.MailService,
   > > OAuth2Factory,
   > > org.apache.http.headers,
   > > org.forgerock.json,
   > > org.forgerock.openam.oauth2.OAuth2UrisFactory,
   > > com.sun.identity.shared.encode,
   > > org.forgerock.http.swagger,
   > > com.iplanet,
   > > com.sun.identity.common.configuration,
   > > org.forgerock.json.resource.InterfaceCollectionInstance,
   > > org.forgerock.json.resource.http.HttpUtils,
   > > org.forgerock.openam.uma.UmaProviderSettingsFactory,
   > > org.forgerock.openam.utils,
   > > org.forgerock.openam.scripting,
   > > org.forgerock.openam.uma.rest.UmaEnabledFilter,
   > > org.forgerock.openam.sts.publish.rest.RestSTSSetupListener,
   > > org.forgerock.util.encode.Base64,
   > > com.zaxxer,
   > > org.forgerock.openam.oauth2.guice.OAuth2GuiceModule,
   > > org.forgerock.openam.social.idp.SocialIdpJwksSecretsProvider,
   > > org.forgerock.secrets,
   > > org.forgerock.util.promise.Promises,
   > > org.forgerock.secrets.SecretReference,
   > > org.forgerock.openam.sts.publish.common.STSInstanceConfigStoreBase,
   > > io.swagger.models.parameters,
   > > org.forgerock.openam.sts.publish.common,
   > > io.swagger,
   > > org.forgerock.openam.oauth2.pop,
   > > org.forgerock.openam.sm.datalayer,
   > > org.forgerock.openam.social.idp.choiceValues.AllowedJweAlgorithms,
   > > org.forgerock.http,
   > > oauth2,
   > > org.forgerock.openam.service.datastore.LdapDataStoreService,
   > > org.forgerock.http.filter,
   > > org.apache.http.wire,
   > > org.forgerock.http.swagger.OpenApiRequestFilter,
   > > org.forgerock.openam.xui,
   > > org.forgerock.api.models,
   > > com.iplanet.services.ldap.event,
   > > org.forgerock.json.jose.jws.SigningManager,
   > > com.sun.identity.shared.xml.XMLUtils,
   > > org.forgerock.http.oauth2,
   > > org.forgerock.util.promise.PromiseImpl,
   > > org.forgerock.openam.secrets,
   > > org.forgerock.openam.sts.publish.service,
   > > org.forgerock.openam.sm.config.ConsoleConfigHandlerImpl,
   > > org.forgerock.openam.integration.idm,
   > > com.sun.identity.authentication,
   > > io.swagger.models,
   > > org.forgerock.openam.selfservice.SelfServiceRequestHandler,
   > > org.forgerock.am.health.LivenessCheckEndpoint,
   > > com.sun.identity.sm.RootSuffixProvider,
   > > org.forgerock.am.iot,
   > > idRepoAuditor,
   > > org.forgerock.openam.sm.datalayer.impl,
   > > org.forgerock.http.util,
   > > com.sun.identity.plugin.session.impl,
   > > com.sun.identity.common,
   > > org.forgerock.openam.utils.PerThreadCache,
   > > com.sun.identity.shared.xml,
   > > org.forgerock.openam.service.datastore,
   > > com.sun.identity.shared.datastruct,
   > > org.forgerock.json.jose.jws,
   > > com.sun.identity.common.configuration.ConfigurationObserver,
   > > com.sun.identity.configuration,
   > > org.forgerock.http.filter.TransactionIdInboundFilter,
   > > frRest,
   > > org.forgerock.secrets.propertyresolver,
   > > org.apache,
   > > org.forgerock.openam.service,
   > > org.forgerock.openam.secrets.SecretsUtils,
   > > org.forgerock.openam.utils.LogUtils,
   > > ROOT,
   > > com.sun.identity.common.ShutdownManager,
   > > org.forgerock.am.iot.GetAccessTokenActionHandler,
   > > org.forgerock.openam.core.rest.authn,
   > > org.forgerock.openam.scripting.persistence.config.consumer.ScriptTypeAdapter,
   > > com.sun,
   > > org.forgerock.util.i18n,
   > > org.forgerock.openam.entitlement.service.ApplicationServiceImpl,
   > > com.sun.identity.policy.plugins.PrefixResourceName,
   > > com.sun.identity.wsfederation.plugins,
   > > org.forgerock.openam.secrets.config.GoogleSecretManagerSecretStoreProvider,
   > > org.forgerock.api.transform,
   > > org,
   > > org.forgerock.util.encode,
   > > com.sun.identity.sm.SmsWrapperObject,
   > > org.forgerock.openam.sm.config,
   > > org.forgerock.openam.scripting.sandbox,
   > > org.forgerock.openam.shared.security,
   > > org.forgerock.api.transform.OpenApiTransformer,
   > > org.forgerock.http.oauth2.ResourceServerFilter,
   > > org.forgerock.openam.headers,
   > > com.sun.identity,
   > > org.forgerock.openam.core.rest.authn.http,
   > > org.forgerock.openam.errors,
   > > org.forgerock.openam.idrepo.ldap.helpers,
   > > org.forgerock.openam.secrets.config.SecretsPlugin,
   > > org.forgerock.http.protocol.Form,
   > > org.forgerock.json.resource,
   > > org.forgerock.util.i18n.PreferredLocales,
   > > com.iplanet.services.ldap,
   > > com.sun.identity.sm.schema.ParsedSchema,
   > > org.forgerock.openam.scripting.service.ScriptChoiceValues,
   > > org.forgerock.openam.sts.publish.rest.RestSTSInstancePublisherImpl,
   > > org.forgerock.openam.errors.AgentResourceExceptionMappingHandler,
   > > org.forgerock.config.resolvers.FlatFileResolver,
   > > org.forgerock.http.routing,
   > > org.forgerock.openam.oauth2.pop.MutualTlsConfirmationMethod,
   > > org.forgerock.openam.scripting.StandardScriptEvaluator,
   > > org.forgerock.am.iot.IotClientRegistrationStore,
   > > org.forgerock.http.servlet.Servlet3Adapter,
   > > org.forgerock.openam.idrepo,
   > > org.forgerock.config,
   > > ldapUrl,
   > > org.forgerock.json.resource.InterfaceSingletonHandler,
   > > org.forgerock.openam.secrets.config,
   > > org.forgerock.openam.sm.DefaultAnnotatedServiceRegistry,
   > > org.forgerock.am.health,
   > > org.forgerock.caf.authentication.framework,
   > > org.forgerock.am.iot.GetUserTokenActionHandler,
   > > com.sun.identity.authentication.UI.LoginLogoutMapping,
   > > org.forgerock.openam.config,
   > > io,
   > > org.forgerock.caf.authentication,
   > > org.forgerock.openam.sm,
   > > org.forgerock.openam.sm.ServiceSchemaRegistrar,
   > > org.forgerock.api.models.Operation,
   > > org.forgerock.http.protocol,
   > > org.forgerock.util.DirectoryWatcher,
   > > com.sun.identity.security,
   > > org.forgerock.openam.entitlement,
   > > org.forgerock.openam.oauth2.ClientCertificateHeaderFormat,
   > > org.forgerock.am.iot.GetUserCodeActionHandler,
   > > org.forgerock.openam.shared,
   > > org.forgerock.http.servlet,
   > > org.forgerock.api.CrestApiProducer,
   > > org.forgerock.openam.sm.annotations.SchemaBuilder,
   > > org.forgerock.openam.scripting.sandbox.RhinoSandboxClassShutter,
   > > org.forgerock.util.xml,
   > > com.sun.identity.authentication.service.ConfiguredIdentityTypes,
   > > org.forgerock.openam.xacml,
   > > org.forgerock.openam.scripting.service.GlobalScriptChoiceValues,
   > > com.iplanet.services.ldap.Server,
   > > com.sun.identity.sm,
   > > org.forgerock.openam.sts.publish.rest.RestSTSPublishServiceListener,
   > > org.forgerock.secrets.AllowedKeyUsageConstraint,
   > > org.forgerock.openam.oauth2.jar,
   > > org.forgerock.openam.oauth2.OAuth2Utils,
   > > org.forgerock.openam.sm.health.FbcLivenessCheck,
   > > org.forgerock.json.resource.http,
   > > org.forgerock.openam.idrepo.ldap,
   > > com.sun.identity.authentication.UI,
   > > com.iplanet.services.util,
   > > com.sun.identity.liberty.ws,
   > > com.sun.identity.authentication.server,
   > > org.forgerock.util,
   > > com.iplanet.sso,
   > > org.forgerock.openam.sm.health.PluginStartupCheck,
   > > org.forgerock.guice.core.InjectorFactory,
   > > org.forgerock.openam.sm.datalayer.impl.ldap,
   > > org.forgerock.openam.sts.publish,
   > > org.forgerock.macaroons,
   > > org.forgerock.openam.selfservice.SelfServiceTreesResource,
   > > com,
   > > org.forgerock.openam.scripting.service.StandardScriptStoreFactory,
   > > org.forgerock.openam.scripting.persistence.config,
   > > org.forgerock.openam.validation,
   > > com.sun.identity.authentication.service,
   > > com.sun.identity.sm.SMSThreadPool,
   > > org.forgerock.openam.validation.RequestEntitySizeVerificationFilter,
   > > org.forgerock.util.promise.Promises$CompletedPromise,
   > > com.sun.identity.authentication.service.AuthConfigMonitor,
   > > org.forgerock.am,
   > > org.forgerock.openam.scripting.service,
   > > org.forgerock.api,
   > > org.forgerock.http.header.SetCookieHeader,
   > > org.forgerock.macaroons.SerializationFormatV2,
   > > org.forgerock.am.iot.IotService,
   > > org.forgerock.openam.ldap,
   > > com.iplanet.am,
   > > com.sun.identity.plugin,
   > > org.forgerock.macaroons.SerializationFormatV1,
   > > com.sun.identity.plugin.session,
   > > org.forgerock.openam.services,
   > > org.forgerock.util.xml.XMLUtils,
   > > org.forgerock.openam.oauth2.saml2.core,
   > > org.forgerock.openam.social.idp,
   > > org.forgerock.openam.config.ServiceComponentConfigBuilder,
   > > org.forgerock.openam.core.rest.session.action,
   > > com.sun.identity.liberty,
   > > org.forgerock.openam.homedirectory,
   > > org.forgerock.openam.scripting.StandardScriptEngineManager,
   > > org.forgerock.openam.secrets.Secrets,
   > > org.forgerock.caf.authentication.framework.AuthenticationFramework,
   > > org.forgerock.json.jose.utils.Utils,
   > > org.forgerock.openam.social.idp.SocialIdentityProviders,
   > > org.forgerock.openam.core.rest.authn.AuthIdHelper,
   > > org.forgerock.openam.oauth2,
   > > org.forgerock.openam.core.CoreWrapper,
   > > org.forgerock.guice,
   > > org.forgerock.http.protocol.Entity,
   > > org.forgerock.openam.sts.publish.service.RestSTSPublishServiceRequestHandler,
   > > org.forgerock.openam.scripting.persistence.config.consumer,
   > > org.forgerock.openam.network,
   > > org.forgerock.http.header,
   > > org.forgerock.openam.entitlement.service,
   > > org.forgerock.openam.integration,
   > > com.sun.identity.common.SystemTimer,
   > > org.forgerock.openam.core,
   > > com.sun.identity.sm.SmsChangesLogger,
   > > org.forgerock.openam.sm.datalayer.impl.CtsConnectionCheck,
   > > org.forgerock.openam.sts,
   > > com.sun.identity.authentication.server.AuthXMLHandler,
   > > org.forgerock.openam.sm.annotations,
   > > org.forgerock.config.resolvers.PropertyResolvers,
   > > org.forgerock.secrets.SecretsProvider,
   > > com.sun.identity.policy,
   > > com.sun.identity.wsfederation,
   > > org.forgerock.json.resource.http.HttpAdapter,
   > > org.forgerock.http.util.Uris,
   > > com.sun.identity.shared.datastruct.CollectionHelper,
   > > org.forgerock.guice.core,
   > > org.forgerock,
   > > org.forgerock.openam.sts.publish.rest,
   > > org.forgerock.openam.social.idp.choiceValues,
   > > com.iplanet.services.util.Crypt,
   > > com.sun.identity.config,
   > > org.forgerock.json.resource.InterfaceCollectionHandler,
   > > org.forgerock.openam,
   > > jsp.realmSelection,
   > > org.forgerock.openam.service.datastore.SmsDataStoreLookup,
   > > com.sun.identity.authentication.service.AMLoginContext,
   > > com.sun.identity.authentication.spi,
   > > org.forgerock.config.util.JsonValuePropertyEvaluator,
   > > org.forgerock.openam.xacml.v3,
   > > org.forgerock.http.routing.Router,
   > > com.iplanet.services.ldap.LDAPUser,
   > > com.sun.identity.policy.util,
   > > org.apache.http,
   > > com.sun.identity.sm.schema,
   > > org.forgerock.http.servlet.HttpFrameworkServlet,
   > > org.forgerock.openam.setup,
   > > org.forgerock.openam.social.idp.DefaultOpenIdConnectRelyingPartySettings,
   > > org.forgerock.openam.headers.SecureCookieFilter,
   > > com.iplanet.services.util.JCEEncryption,
   > > org.forgerock.json.jose,
   > > org.forgerock.openam.oauth2.OAuth2NotificationPublisher,
   > > com.sun.identity.security.cert,
   > > org.forgerock.json.jose.utils,
   > > org.forgerock.caf,
   > > org.forgerock.openam.oauth2.jar.JarAuthorizeRequestValidator,
   > > org.forgerock.openam.sm.health,
   > > org.forgerock.config.resolvers.ChainedPropertyResolver
   > > ```
   >
   > > **Collapse: Plugins**
   > >
   > > ```
   > > Plugin Framework
   > > org.forgerock.openam.plugins
   > > ```
   >
   > > **Collapse: Policy**
   > >
   > > ```
   > > Policy Framework,Subject, Condition, Resource Attributes, XACML, Plugins, API
   > > com.sun.identity.policy.PolicyManager,
   > > com.sun.identity.policy.plugins.Organization,
   > > com.sun.identity.policy.SharedSubject,
   > > com.sun.identity.policy.ActionDecision,
   > > com.sun.identity.policy.ResourceManager,
   > > com.sun.identity.policy.plugins.IDRepoResponseProvider,
   > > com.sun.identity.policy.plugins.AuthSchemeCondition,
   > > com.sun.identity.policy.plugins.LEAuthLevelCondition,
   > > com.sun.identity.policy.PolicyCache,
   > > com.sun.identity.policy.PolicyDecision,
   > > org.forgerock.openam.entitlement.monitoring,
   > > com.sun.identity.policy.ProxyPolicyEvaluatorFactory,
   > > com.sun.identity.policy.Rule,
   > > com.sun.identity.policy.ResourceComparatorValidator,
   > > com.sun.identity.policy.plugins.IPCondition,
   > > com.sun.identity.policy.ProxyPolicyEvaluator,
   > > com.sun.identity.policy.remote,
   > > com.sun.identity.policy.ValidationErrorHandler,
   > > org.forgerock.openam.entitlement.rest.EntitlementsExceptionMappingHandler,
   > > org.forgerock.openam.network.ipv6,
   > > com.sun.identity.policy.Subjects,
   > > com.sun.identity.policy.plugins.PeerOrgReferral,
   > > com.sun.identity.policy.Policy,
   > > com.sun.identity.policy.ActionSchema,
   > > org.forgerock.openam.idrepo.ldap.helpers.ADHelper,
   > > org.forgerock.openam.entitlement.configuration,
   > > com.sun.identity.policy.plugins.SubOrgReferral,
   > > com.sun.identity.policy.plugins.AuthenticateToRealmCondition,
   > > org.forgerock.openam.entitlement.indextree,
   > > com.sun.identity.policy.SubjectEvaluationCache,
   > > org.forgerock.openam.uma.rest.UserPolicyResource,
   > > com.sun.identity.policy.plugins.OrgReferral,
   > > com.sun.identity.policy.plugins.LDAPUsers,
   > > com.sun.identity.policy.plugins.UserSelfCheckCondition,
   > > com.sun.identity.policy.ResponseProviderTypeManager,
   > > com.sun.identity.policy.plugins.LDAPFilterCondition,
   > > com.sun.identity.policy.plugins.SimpleTimeCondition,
   > > com.sun.identity.policy.ResponseProviders,
   > > org.forgerock.openam.xacml.v3.resources,
   > > com.sun.identity.policy.PolicyUtils,
   > > com.sun.identity.policy.plugins.SessionCondition,
   > > org.forgerock.openam.entitlement.CachingEntitlementCondition,
   > > com.sun.identity.policy.plugins.AMIdentitySubject,
   > > com.sun.identity.policy.Referrals,
   > > com.sun.identity.policy.ResourceIndexManager,
   > > com.sun.identity.policy.plugins.AuthLevelCondition,
   > > com.sun.identity.policy.plugins.LDAPConnectionPools,
   > > com.sun.identity.policy.plugins.AuthenticateToServiceCondition,
   > > com.sun.identity.policy.plugins.AuthRoleCondition,
   > > com.sun.identity.policy.plugins.AMIdentityMembershipCondition,
   > > com.sun.identity.entitlement,
   > > com.sun.identity.policy.PolicyEvaluatorFactory,
   > > com.sun.identity.policy.plugins.SessionPropertyCondition,
   > > org.forgerock.openam.entitlement.PolicyConstants,
   > > com.sun.identity.policy.PolicyEvaluator,
   > > com.sun.identity.policy.ServiceTypeManager,
   > > com.sun.identity.policy.ServiceType,
   > > com.sun.identity.policy.ResourceResult,
   > > com.sun.identity.policy.plugins.ResourceEnvIPCondition,
   > > org.forgerock.openam.entitlement.conditions,
   > > com.sun.identity.policy.ConditionTypeManager,
   > > com.sun.identity.policy.PolicyConfig,
   > > com.sun.identity.policy.plugins.LDAPGroups,
   > > org.forgerock.openam.network.ipv4.IPv4Condition,
   > > com.sun.identity.policy.SubjectTypeManager,
   > > org.forgerock.openam.entitlement.utils,
   > > com.sun.identity.policy.util.PolicyDecisionUtils,
   > > org.forgerock.openam.entitlement.PolicySetNotificationConsumer,
   > > com.sun.identity.policy.Conditions,
   > > org.forgerock.openam.core.rest.authn.http.AuthenticationServiceV2,
   > > com.sun.identity.policy.ReferralTypeManager,
   > > org.forgerock.openam.entitlement.rest.PolicyResource,
   > > org.forgerock.openam.entitlement.rest.JsonPolicyParser
   > > ```
   >
   > > **Collapse: Push**
   > >
   > > ```
   > > Push Notification
   > > org.forgerock.openam.services.push
   > > ```
   >
   > > **Collapse: Radius**
   > >
   > > ```
   > > RADIUS server
   > > org.forgerock.openam.radius
   > > ```
   >
   > > **Collapse: Session**
   > >
   > > ```
   > > Session framework, session management, SSOToken, session failover, API
   > > org.forgerock.openam.core.rest.session.action.SetPropertyActionHandler,
   > > org.forgerock.openam.core.rest.session.action.GetPropertyActionHandler,
   > > org.forgerock.openam.core.rest.session.SessionResource,
   > > com.sun.identity.sm.ServerIDValidator,
   > > org.forgerock.openam.cts,
   > > org.forgerock.openam.core.rest.session.action.LogoutActionHandler,
   > > org.forgerock.openam.dpro,
   > > com.iplanet.sso.providers,
   > > org.forgerock.openam.core.rest.session.action.ValidateActionHandler,
   > > org.forgerock.openam.core.rest.session.action.GetSessionPropertiesActionHandler,
   > > org.forgerock.openam.session,
   > > org.forgerock.openam.sm.datalayer.impl.ldap.ExternalLdapConfig,
   > > org.forgerock.openam.core.rest.session.action.UpdateSessionPropertiesActionHandler,
   > > org.forgerock.openam.core.rest.session.SSOTokenPartialSessionFactory,
   > > org.forgerock.openam.sm.SMSConfigurationFactory,
   > > org.forgerock.openam.sm.datalayer.impl.SeriesTaskExecutorThread,
   > > com.iplanet.dpro,
   > > com.sun.identity.plugin.session.impl.FMSessionNotification,
   > > org.forgerock.openam.core.rest.session.action.GetPropertyNamesActionHandler,
   > > org.forgerock.openam.core.rest.session.SessionResourceUtil,
   > > org.forgerock.openam.core.rest.session.SessionResourceV2,
   > > com.sun.identity.sm.SiteIDValidator,
   > > org.forgerock.openam.core.rest.session.action.DeletePropertyActionHandler
   > > ```
   >
   > > **Collapse: UmaProvider**
   > >
   > > ```
   > > UMA provider
   > > org.forgerock.openam.oauth2.AccessTokenProtectionFilter,
   > > org.forgerock.openam.uma.UmaSettingsImpl,
   > > org.forgerock.openam.uma.icg,
   > > org.forgerock.openam.uma.PendingRequestEmailTemplate,
   > > org.forgerock.openam.uma.rest.UmaPolicyApplicationListener,
   > > org.forgerock.openam.uma.rest.UmaResourceSetRegistrationHook,
   > > org.forgerock.openam.oauth2.resources.labels,
   > > org.forgerock.openam.uma.UmaProviderSettingsImpl,
   > > org.forgerock.openam.uma.UmaGrantTypeHandler,
   > > org.forgerock.openam.uma.rest.UmaLabelResource,
   > > org.forgerock.openam.uma.PendingRequestsService,
   > > org.forgerock.openam.uma.audit
   > > ```
   >
   > > **Collapse: WebServices**
   > >
   > > ```
   > > Web services security (WSS), STS, Identity Services
   > > com.sun.identity.liberty.ws.paos,
   > > com.sun.identity.liberty.ws.common,
   > > com.sun.identity.policy.plugins.WebServicesClients,
   > > com.sun.identity.liberty.ws.soapbinding,
   > > com.sun.identity.authentication.spi.WSSReplayPasswd
   > > ```
   >
   > > **Collapse: amUpgrade**
   > >
   > > ```
   > > Upgrade framework
   > > com.sun.identity.sm.ServiceSchemaModifications,
   > > org.forgerock.openam.upgrade,
   > > com.sun.identity.common.configuration.ServerConfiguration,
   > > com.sun.identity.config.upgrade,
   > > com.sun.identity.security.cert.AMCRLStore
   > > ```

   There is an example [logback.xml](#example-logback) file, which defines similar appenders and loggers.

2. To set the logging level for all loggers that output to a particular appender:

   1. Select the name of the appender from the Appender drop-down list.

   2. Select the debug level from the Level drop-down list.

   3. Click Apply.

3. To set the logging level for a class or package:

   1. Select the name of the individual logger from the Logger drop-down list, or select the global `ROOT` logger to set the level for all loggers.

      The current debug level is shown in the Level field.

      |   |                                                                                                                                                                                                                                                                                       |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Scripts that create debug messages have their own logger created after the script has executed at least once.The name of the logger has the format: `scripts.<context>.<uuid>.(<name>)`.For example, `scripts.OIDC_CLAIMS.36863ffb-40ec-48b9-94b1-9a99f71cc3b5.(OIDC Claims Script)`. |

   2. Select a new debug level from the Level drop-down list.

   3. Click Apply.

   When you apply any changes to the logger settings, a `Logger settings updated` message is shown at the top of the `Logback.jsp` page.

   |   |                                                                                                                                                                                                                                                                                                   |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Changes made in `Logback.jsp` apply immediately, but aren't permanently stored. Restarting AM or the container in which it runs resets the levels.You can configure the default settings that'll apply when AM starts up. Learn more in [Change the startup debug settings](#log-debug-defaults). |

4. As soon as you have reproduced the problem you are investigating, return to the `Logback.jsp` page and revert the logger levels to the previous settings, to avoid filling up disk space.

## Persistent debug logging with `logback.xml`

Debug logging can be enabled and persisted in AM by configuring a `logback.xml` file. This file describes the classes for which to capture debug messages, and the destination, or *appender*, where the output is stored.

You can find more information about configuring Logback in [Logback configuration](https://logback.qos.ch/manual/configuration.html) in the *Logback Documentation*.

### Configure basic debug logging

Follow these steps to configure basic persistent debug logging in AM, using a `logback.xml` file:

1. Create a `logback.xml` file in the AM classpath, for example, in `/path/to/tomcat/webapps/am/WEB-INF/classes/`.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | To view or use an existing file with example loggers and appenders, place the following `logback.xml` in your classpath and set the paths for your environment.> **Collapse: Example**
   >
   > ```xml
   > <configuration>
   >  <!--    amUpgrade  -->
   >  <appender name="amUpgrade" class="ch.qos.logback.core.FileAppender">
   >   <file>/path/to/debug/amUpgrade</file>
   >   <encoder>
   >    <pattern>%lo{5}: %d{ISO8601}: Thread[%t]: TransactionId[%X{transactionId}]%n%level: %m%n%ex</pattern>
   >   </encoder>
   >  </appender>
   >  <logger name="com.sun.identity.sm.ServiceSchemaModifications" level="Error" >
   >   <appender-ref ref="amUpgrade"/>
   >  </logger>
   >  <logger name="com.sun.identity.common.configuration.ServerConfiguration" level="Error" >
   >   <appender-ref ref="amUpgrade"/>
   >  </logger>
   >  <logger name="com.sun.identity.wsfederation.plugins.DefaultIDPAccountMapper" level="Error" >
   >   <appender-ref ref="amUpgrade"/>
   >  </logger>
   >  <logger name="com.sun.identity.saml2.plugins.DefaultIDPAccountMapper" level="Error" >
   >   <appender-ref ref="amUpgrade"/>
   >  </logger>
   >  <logger name="com.sun.identity.config.upgrade" level="Error" >
   >   <appender-ref ref="amUpgrade"/>
   >  </logger>
   >  <logger name="com.sun.identity.saml2.plugins.DefaultLibrarySPAccountMapper" level="Error" >
   >   <appender-ref ref="amUpgrade"/>
   >  </logger>
   >  <logger name="com.sun.identity.wsfederation.plugins.DefaultADFSPartnerAccountMapper" level="Error" >
   >   <appender-ref ref="amUpgrade"/>
   >  </logger>
   >  <logger name="com.sun.identity.wsfederation.plugins.DefaultIDPAttributeMapper" level="Error" >
   >   <appender-ref ref="amUpgrade"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.upgrade" level="Error" >
   >   <appender-ref ref="amUpgrade"/>
   >  </logger>
   >  <logger name="com.sun.identity.wsfederation.plugins.DefaultSPAttributeMapper" level="Error" >
   >   <appender-ref ref="amUpgrade"/>
   >  </logger>
   >  <logger name="com.sun.identity.saml2.plugins.DefaultSPAccountMapper" level="Error" >
   >   <appender-ref ref="amUpgrade"/>
   >  </logger>
   >  <logger name="com.sun.identity.saml2.plugins.DefaultLibraryIDPAttributeMapper" level="Error" >
   >   <appender-ref ref="amUpgrade"/>
   >  </logger>
   >  <logger name="com.sun.identity.security.cert.AMCRLStore" level="Error" >
   >   <appender-ref ref="amUpgrade"/>
   >  </logger>
   >  <logger name="com.sun.identity.saml2.plugins.DefaultSPAttributeMapper" level="Error" >
   >   <appender-ref ref="amUpgrade"/>
   >  </logger>
   >  <logger name="com.sun.identity.wsfederation.plugins.DefaultLibrarySPAccountMapper" level="Error" >
   >   <appender-ref ref="amUpgrade"/>
   >  </logger>
   >
   >  <!--    Authentication  -->
   >  <appender name="Authentication" class="ch.qos.logback.core.FileAppender">
   >   <file>/path/to/debug/Authentication</file>
   >   <encoder>
   >    <pattern>%lo{5}: %d{ISO8601}: Thread[%t]: TransactionId[%X{transactionId}]%n%level: %m%n%ex</pattern>
   >   </encoder>
   >  </appender>
   >  <logger name="com.sun.identity.authentication.spi.AMLoginModule" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.authn.callbackhandlers" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="com.sun.identity.authentication.spi.AMAuthCallBackImpl" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="com.sun.identity.authentication.service.AuthContextLookup" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="com.sun.identity.authentication.util" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.authentication.service.LoginContextFactory" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="com.sun.identity.authentication.server.AuthContextLocal" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="com.sun.identity.authentication.service.AMAccountLockout" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="com.sun.identity.authentication.service.LoginState" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="com.sun.identity.authentication.UI.LoginViewBean" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="com.sun.identity.authentication.client" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.authn.trees" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="com.sun.identity.authentication.spi.FirstTimeLogin" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.auth" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.authentication.service.SessionPropertyUpgrader" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="com.sun.identity.authentication.UI.AuthExceptionViewBean" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="com.sun.identity.authentication.spi.ReplayPasswd" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="com.sun.identity.authentication.config" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="com.sun.identity.authentication.share" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.authentication.SessionUpgradeVerifier" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="com.sun.identity.authentication.service.DSAMECallbackHandler" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="com.sun.identity.authentication.spi.AMModuleProperties" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.utils.MappingUtils" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="com.sun.identity.authentication.UI.AuthenticationServletBase" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="com.sun.identity.authentication.service.AuthenticationPrincipalDataRetrieverFactory"
   >          level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="com.sun.identity.authentication.UI.LogoutViewBean" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="com.iplanet.security" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="com.sun.identity.authentication.internal" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="com.sun.identity.authentication.AuthContext" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.plugins.AuthenticatedSharedAgents" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.ldap.LDAPAuthUtils" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="com.sun.identity.authentication.UI.AuthViewBeanBase" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.authentication.modules" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="com.iplanet.services.cdm" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.authentication.service.AuthUtilsWrapper" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.plugins.AuthenticatedAgents" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="com.sun.identity.authentication.spi.JwtReplayPassword" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.plugins.AllowedAgents" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="com.sun.identity.authentication.service.AuthenticationServiceAttributeCache" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="com.sun.identity.authentication.jaas" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="com.sun.identity.authentication.service.AuthD" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.authn.core" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.scripting.api" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="com.sun.identity.common.ISAccountLockout" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.authn.RestAuthCallbackHandlerFactory" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.authn.RestAuthCallbackHandlerManager" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.webhook" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="com.iplanet.services.cdc" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="com.sun.identity.authentication.modules" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.authn.http.AuthenticationServiceV1" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="com.sun.identity.authentication.service.AuthUtils" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.plugins.AuthenticatedSharedAgentsCondition" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.authentication.service.JAASModuleDetector" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.authn.RestAuthenticationHandler" level="Error" >
   >   <appender-ref ref="Authentication"/>
   >  </logger>
   >
   >  <!--    Configuration   -->
   >  <appender name="Configuration" class="ch.qos.logback.core.FileAppender">
   >   <file>/path/to/debug/Configuration</file>
   >   <encoder>
   >    <pattern>%lo{5}: %d{ISO8601}: Thread[%t]: TransactionId[%X{transactionId}]%n%level: %m%n%ex</pattern>
   >   </encoder>
   >  </appender>
   >  <logger name="com.sun.identity.sm.ServiceSchemaManager" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.iplanet.services.ldap.event.EventService" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.sm.SMSSchema" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.tools" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.sm.SMSUtils" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.common.configuration.ServerConfigXMLObserver" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.sm.ServiceSchema" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.delegation" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.sm.OrganizationConfigManager" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.sm.ldap" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.sm.SMSNotificationManager" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.sm.PluginSchema" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.sm.AttributeValidator" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.sm.ServiceConfigManagerImpl" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.sm.ServiceConfigImpl" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.sm.SMSPropertiesObserver" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.sm.OrganizationConfigManagerImpl" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.sm.AuthenticationServiceNameProviderImpl" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.xui.XUIFilter" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.sm.ServiceSchemaImpl" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.setup" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.sm.AttributeSchemaState" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.sm.ServiceInstanceImpl" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.auditors" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.workflow" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.sm.ServiceConfigManager" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.sm.validation" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.common.configuration.SessionSiteNames" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.sm.ServiceConfig" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.sm.SMServlet" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.sm.ServiceManager" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.common.configuration.ServerPropertyValidator" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.sm.SMSEntry" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.sm.PluginConfig" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.utils.OpenAMSettingsImpl" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.sm.jaxrpc" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.sm.DNMapper" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.sm.SMSException" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.sm.SMSEventListenerManager" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.utils.MapHelper" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.sm.ServiceInstance" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.config.util" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.sm.CachedSubEntries" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.sm.PluginConfigImpl" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.authentication.service.ConfiguredSocialAuthServices" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.sm.ServiceSchemaManagerImpl" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.sm.CachedSMSEntry" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.sm.CreateServiceConfig" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.sm.AttributeSchema" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >  <logger name="com.sun.identity.sm.PluginSchemaImpl" level="Error" >
   >   <appender-ref ref="Configuration"/>
   >  </logger>
   >
   >  <!--    CoreSystem  -->
   >  <appender name="CoreSystem" class="ch.qos.logback.core.FileAppender">
   >   <file>/path/to/debug/CoreSystem</file>
   >   <encoder>
   >    <pattern>%lo{5}: %d{ISO8601}: Thread[%t]: TransactionId[%X{transactionId}]%n%level: %m%n%ex</pattern>
   >   </encoder>
   >  </appender>
   >  <logger name="com.sun.identity.monitoring" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="com.sun.identity.saml2.idpdiscovery" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="com.sun.identity.security.cert.CRLValidator" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.xacml.v3.rest" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.SelfServiceUserUiRolePredicate" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.cts" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.sm.datalayer.impl.ldap.LdapSearchHandler" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.security" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="com.sun.identity.plugin.monitoring.impl" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.sm.datalayer.providers" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="com.zaxxer.hikari" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.uma.UmaUserUiRolePredicate" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="com.sun.identity.common.RequestUtils" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.entitlement.rest.SubjectAttributesResourceV1" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.services.baseurl" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.IdentityRestUtils" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.UserGroupsResource" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.oauth2.rest" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="com.sun.identity.authentication.UI.taglib" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.docs" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="com.sun.identity.log" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.AllAuthenticatedUsersResource" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.utils.WhitelistObjectInputStream" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.dashboard" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="com.sun.identity.common.SystemTimerPool" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.session.AnyOfAuthzModule" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.rest" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.sms" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="com.sun.identity.common.admin" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.shared.resourcename" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="com.sun.identity.security.AdminTokenAction" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.uma.rest.UmaPolicyResourceAuthzFilter" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.shared.concurrency" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.session.SessionResourcePrivilegeAuthzModule" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.entitlement.rest.ResourceTypesResource" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.uma.rest.UmaPolicyServiceImpl" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.entitlement.rest.DecisionCombinersResource" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="com.sun.identity.common.HttpURLConnectionManager" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.sm.datalayer.impl.SeriesTaskExecutor" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.network.ipv4.IPv4AddressRange" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.audit" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.audit" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="com.sun.identity.common.DNUtils" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.utils.IPRange" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.services.RestSecurity" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.IdentityResourceV4" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.IdentityResourceV3" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="com.sun.identity.security.SecurityDebug" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.backstage" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.server" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.utils.ClientUtils" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.IdentityResourceV2" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.entitlement.rest.ApplicationV1Filter" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.IdentityResourceV1" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.devices" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.entitlement.rest.ApplicationsResource" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.util.Gateway" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="com.sun.identity.shared.jaxrpc" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.forgerockrest" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="com.iplanet.am.util" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="com.iplanet.services.comm" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.authn.AuditHelper" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.sm.datalayer.impl.PooledTaskExecutor" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.ldap.LdifUtils" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.session.action.LogoutByHandleActionHandler" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.sm.datalayer.impl.ldap.LdapQueryBuilder" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="com.sun.identity.shared.search" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.entitlement.rest.SubjectTypesResource" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="com.sun.identity.shared.encode.CookieUtils" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="com.iplanet.services.naming" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.cors" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="com.sun.identity.idsvcs" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="com.sun.identity.jaxrpc" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.http" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.shared.guice" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.utils.AMKeyProvider" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.utils.AuthLevelUtils" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.shared.security.whitelist" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.notifications" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.util.GatewayServletUtils" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.sms" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.blacklist" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="com.sun.identity.common.configuration.AgentConfiguration" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.entitlement.rest.ApplicationTypesResource" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.monitoring" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="com.sun.identity.common.ResourceLookup" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.entitlement.rest.PolicyV1Filter" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="com.sun.identity.authentication.server.AuthXMLRequestParser" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.entitlement.rest.wrappers" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="com.sun.identity.security.cert.AMCertStore" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.sm.datalayer.impl.SimpleTaskExecutor" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="com.sun.identity.shared.locale" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="com.sun.identity.shared.whitelist" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.sm.datalayer.impl.ldap.CTSDJLDAPv3PersistentSearch" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="com.sun.identity.protocol" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.scripting.rest" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.entitlement.rest.ConditionTypesResource" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.record" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="com.sun.identity.security.cert.AMCertPath" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.utils.ServiceConfigUtils" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >  <logger name="com.sun.identity.authentication.server.AuthXMLRequest" level="Error" >
   >   <appender-ref ref="CoreSystem"/>
   >  </logger>
   >
   >  <!--    Federation  -->
   >  <appender name="Federation" class="ch.qos.logback.core.FileAppender">
   >   <file>/path/to/debug/Federation</file>
   >   <encoder>
   >    <pattern>%lo{5}: %d{ISO8601}: Thread[%t]: TransactionId[%X{transactionId}]%n%level: %m%n%ex</pattern>
   >   </encoder>
   >  </appender>
   >  <logger name="com.sun.identity.wsfederation.profile" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.saml2.servlet" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.saml2.plugins.SAML2PluginsUtils" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.plugin.datastore" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.saml2.logging" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.saml2.protocol" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.saml2.common" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.saml2.plugins.DefaultAccountMapper" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.federation" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.wsfederation.plugins.whitelist" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.saml2.profile" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.saml2.plugins.SAML2IDPProxyFRImpl" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.wsfederation.key" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.multiprotocol" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.saml2.plugins.SAML2IDPProxyImpl" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.wsfederation.servlet" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.xacml" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.plugin.monitoring.MonitorManager" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.saml2.plugins.DefaultIDPAuthnContextMapper" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.wsfederation.plugins.DefaultAccountMapper" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.saml2.plugins.DefaultAttributeMapper" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.wsfederation.plugins.DefaultAttributeMapper" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.authentication.Saml2SessionUpgradeHandler" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.saml2.ecp" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.wsfederation" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.federation" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.saml2" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="jsp.saml2" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.saml2.plugins.DefaultIDPECPSessionMapper" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.plugin.log" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.saml" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.wsfederation.meta" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.wsfederation.plugins.DefaultIDPAuthenticationMethodMapper" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.saml2.plugins.DefaultFedletAdapter" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.saml2.xmlenc" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.saml2.plugins.DefaultSPAuthnContextMapper" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.saml2.xmlsig" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.liberty.ws.security" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.plugin.session.SessionManager" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.plugin.session.impl.FMSessionProvider" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.saml2.key" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.wsfederation.logging" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.saml2.assertion" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.plugin.session.impl.FedletSessionProvider" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.saml2.meta" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.plugin.configuration" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.saml2.soapbinding" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.wsfederation.common" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >  <logger name="com.sun.identity.cot" level="Error" >
   >   <appender-ref ref="Federation"/>
   >  </logger>
   >
   >  <!--    IdRepo  -->
   >  <appender name="IdRepo" class="ch.qos.logback.core.FileAppender">
   >   <file>/path/to/debug/IdRepo</file>
   >   <encoder>
   >    <pattern>%lo{5}: %d{ISO8601}: Thread[%t]: TransactionId[%X{transactionId}]%n%level: %m%n%ex</pattern>
   >   </encoder>
   >  </appender>
   >  <logger name="com.sun.identity.common.ISResourceBundle" level="Error" >
   >   <appender-ref ref="IdRepo"/>
   >  </logger>
   >  <logger name="com.iplanet.am.sdk" level="Error" >
   >   <appender-ref ref="IdRepo"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.idrepo.ldap.DJLDAPv3Repo" level="Error" >
   >   <appender-ref ref="IdRepo"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.shared.security.crypto" level="Error" >
   >   <appender-ref ref="IdRepo"/>
   >  </logger>
   >  <logger name="com.iplanet.sso.SSOTokenManager" level="Error" >
   >   <appender-ref ref="IdRepo"/>
   >  </logger>
   >  <logger name="com.iplanet.services.ldap.DefaultDataStoreConfigurationManager" level="Error" >
   >   <appender-ref ref="IdRepo"/>
   >  </logger>
   >  <logger name="com.sun.identity.idm" level="Error" >
   >   <appender-ref ref="IdRepo"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.idrepo.ldap.helpers.DirectoryHelper" level="Error" >
   >   <appender-ref ref="IdRepo"/>
   >  </logger>
   >  <logger name="com.sun.identity.shared.encode.Hash" level="Error" >
   >   <appender-ref ref="IdRepo"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.realms" level="Error" >
   >   <appender-ref ref="IdRepo"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.shared.security.ThreadLocalSecureRandom" level="Error" >
   >   <appender-ref ref="IdRepo"/>
   >  </logger>
   >  <logger name="com.iplanet.services.ldap.event.LDAPv3PersistentSearch" level="Error" >
   >   <appender-ref ref="IdRepo"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.idrepo.ldap.psearch" level="Error" >
   >   <appender-ref ref="IdRepo"/>
   >  </logger>
   >  <logger name="com.sun.identity.security.ServerInstanceAction" level="Error" >
   >   <appender-ref ref="IdRepo"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.identity" level="Error" >
   >   <appender-ref ref="IdRepo"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.ldap.LDAPUtils" level="Error" >
   >   <appender-ref ref="IdRepo"/>
   >  </logger>
   >
   >  <!--    OAuth2Provider  -->
   >  <appender name="OAuth2Provider" class="ch.qos.logback.core.FileAppender">
   >   <file>/path/to/debug/OAuth2Provider</file>
   >   <encoder>
   >    <pattern>%lo{5}: %d{ISO8601}: Thread[%t]: TransactionId[%X{transactionId}]%n%level: %m%n%ex</pattern>
   >   </encoder>
   >  </appender>
   >  <logger name="org.forgerock.openam.oauth2.OpenAMClientRegistrationStore" level="Error" >
   >   <appender-ref ref="OAuth2Provider"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.oauth2.secrets" level="Error" >
   >   <appender-ref ref="OAuth2Provider"/>
   >  </logger>
   >  <logger name="org.forgerock.openidconnect" level="Error" >
   >   <appender-ref ref="OAuth2Provider"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.oauth2.resources.ResourceSetLabelRegistration" level="Error" >
   >   <appender-ref ref="OAuth2Provider"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.oauth2.OAuth2GlobalSettings" level="Error" >
   >   <appender-ref ref="OAuth2Provider"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.oauth2.OpenAMClientRegistration" level="Error" >
   >   <appender-ref ref="OAuth2Provider"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.oauth2.ciba" level="Error" >
   >   <appender-ref ref="OAuth2Provider"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.oauth2.requesturis" level="Error" >
   >   <appender-ref ref="OAuth2Provider"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.oauth2.OAuth2AuditLogger" level="Error" >
   >   <appender-ref ref="OAuth2Provider"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.oauth2.token" level="Error" >
   >   <appender-ref ref="OAuth2Provider"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.oauth2.IdentityManager" level="Error" >
   >   <appender-ref ref="OAuth2Provider"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.oauth2.IgAgentClientRegistration" level="Error" >
   >   <appender-ref ref="OAuth2Provider"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.oauth2.jwks" level="Error" >
   >   <appender-ref ref="OAuth2Provider"/>
   >  </logger>
   >  <logger name="org.forgerock.oauth2" level="Error" >
   >   <appender-ref ref="OAuth2Provider"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.utils.RealmNormaliser" level="Error" >
   >   <appender-ref ref="OAuth2Provider"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.oauth2.AgentClientRegistration" level="Error" >
   >   <appender-ref ref="OAuth2Provider"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.oauth2.ClientCredentialsReader" level="Error" >
   >   <appender-ref ref="OAuth2Provider"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.oauth2.remoteconsent" level="Error" >
   >   <appender-ref ref="OAuth2Provider"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.oauth2.OpenAMScopeValidator" level="Error" >
   >   <appender-ref ref="OAuth2Provider"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.oauth2.OAuth2Monitor" level="Error" >
   >   <appender-ref ref="OAuth2Provider"/>
   >  </logger>
   >
   >  <!--    OpenDJ-SDK  -->
   >  <appender name="OpenDJ-SDK" class="ch.qos.logback.core.FileAppender">
   >   <file>/path/to/debug/OpenDJ-SDK</file>
   >   <encoder>
   >    <pattern>%lo{5}: %d{ISO8601}: Thread[%t]: TransactionId[%X{transactionId}]%n%level: %m%n%ex</pattern>
   >   </encoder>
   >  </appender>
   >  <logger name="org.forgerock.opendj.ldif" level="Error" >
   >   <appender-ref ref="OpenDJ-SDK"/>
   >  </logger>
   >  <logger name="org.forgerock.opendj.asn1" level="Error" >
   >   <appender-ref ref="OpenDJ-SDK"/>
   >  </logger>
   >  <logger name="com.forgerock.opendj.util" level="Error" >
   >   <appender-ref ref="OpenDJ-SDK"/>
   >  </logger>
   >  <logger name="com.forgerock.opendj.ldap" level="Error" >
   >   <appender-ref ref="OpenDJ-SDK"/>
   >  </logger>
   >  <logger name="org.forgerock.opendj.ldap" level="Error" >
   >   <appender-ref ref="OpenDJ-SDK"/>
   >  </logger>
   >  <logger name="org.forgerock.opendj.util" level="Error" >
   >   <appender-ref ref="OpenDJ-SDK"/>
   >  </logger>
   >
   >  <!--    Plugins     -->
   >  <appender name="Plugins" class="ch.qos.logback.core.FileAppender">
   >   <file>/path/to/debug/Plugins</file>
   >   <encoder>
   >    <pattern>%lo{5}: %d{ISO8601}: Thread[%t]: TransactionId[%X{transactionId}]%n%level: %m%n%ex</pattern>
   >   </encoder>
   >  </appender>
   >  <logger name="org.forgerock.openam.plugins" level="Error" >
   >   <appender-ref ref="Plugins"/>
   >  </logger>
   >
   >  <!--    Policy  -->
   >  <appender name="Policy" class="ch.qos.logback.core.FileAppender">
   >   <file>/path/to/debug/Policy</file>
   >   <encoder>
   >    <pattern>%lo{5}: %d{ISO8601}: Thread[%t]: TransactionId[%X{transactionId}]%n%level: %m%n%ex</pattern>
   >   </encoder>
   >  </appender>
   >  <logger name="com.sun.identity.policy.PolicyManager" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.plugins.Organization" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.SharedSubject" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.ActionDecision" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.ResourceManager" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.plugins.IDRepoResponseProvider" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.plugins.AuthSchemeCondition" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.plugins.LEAuthLevelCondition" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.PolicyCache" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.PolicyDecision" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.entitlement.monitoring" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.ProxyPolicyEvaluatorFactory" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.Rule" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.ResourceComparatorValidator" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.plugins.IPCondition" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.PolicyContinuousListener" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.ProxyPolicyEvaluator" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.remote" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.ValidationErrorHandler" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.entitlement.rest.EntitlementsExceptionMappingHandler" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.network.ipv6" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.Subjects" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.plugins.PeerOrgReferral" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.Policy" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.ActionSchema" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.idrepo.ldap.helpers.ADHelper" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.entitlement.configuration" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.plugins.SubOrgReferral" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.plugins.AuthenticateToRealmCondition" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.entitlement.indextree" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.plugins.LDAPRoles" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.SubjectEvaluationCache" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.uma.rest.UserPolicyResource" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.plugins.OrgReferral" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.plugins.LDAPUsers" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.plugins.UserSelfCheckCondition" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.ResponseProviderTypeManager" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.plugins.LDAPFilterCondition" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.plugins.SimpleTimeCondition" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.ResponseProviders" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.xacml.v3.resources" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.PolicyUtils" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.plugins.SessionCondition" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.entitlement.CachingEntitlementCondition" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.plugins.AMIdentitySubject" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.Referrals" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.ResourceIndexManager" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.plugins.AuthLevelCondition" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.plugins.LDAPConnectionPools" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.plugins.AuthenticateToServiceCondition" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.plugins.AuthRoleCondition" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.plugins.AMIdentityMembershipCondition" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.entitlement" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.PolicyEvaluatorFactory" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.plugins.SessionPropertyCondition" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.entitlement.PolicyConstants" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.PolicyEvaluator" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.ServiceTypeManager" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.ServiceType" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.ResourceResult" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.plugins.ResourceEnvIPCondition" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.entitlement.conditions" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.ConditionTypeManager" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.PolicyConfig" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.plugins.LDAPGroups" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.network.ipv4.IPv4Condition" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.SubjectTypeManager" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.entitlement.utils" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.util.PolicyDecisionUtils" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.entitlement.PolicySetNotificationConsumer" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.Conditions" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.authn.http.AuthenticationServiceV2" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.ReferralTypeManager" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.entitlement.rest.PolicyResource" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.entitlement.rest.JsonPolicyParser" level="Error" >
   >   <appender-ref ref="Policy"/>
   >  </logger>
   >
   >  <!--    Push    -->
   >  <appender name="Push" class="ch.qos.logback.core.FileAppender">
   >   <file>/path/to/debug/Push</file>
   >   <encoder>
   >    <pattern>%lo{5}: %d{ISO8601}: Thread[%t]: TransactionId[%X{transactionId}]%n%level: %m%n%ex</pattern>
   >   </encoder>
   >  </appender>
   >  <logger name="org.forgerock.openam.services.push" level="Error" >
   >   <appender-ref ref="Push"/>
   >  </logger>
   >
   >  <!--    Radius  -->
   >  <appender name="Radius" class="ch.qos.logback.core.FileAppender">
   >   <file>/path/to/debug/Radius</file>
   >   <encoder>
   >    <pattern>%lo{5}: %d{ISO8601}: Thread[%t]: TransactionId[%X{transactionId}]%n%level: %m%n%ex</pattern>
   >   </encoder>
   >  </appender>
   >  <logger name="org.forgerock.openam.radius" level="Error" >
   >   <appender-ref ref="Radius"/>
   >  </logger>
   >
   >  <!--    Session  -->
   >  <appender name="Session" class="ch.qos.logback.core.FileAppender">
   >   <file>/path/to/debug/Session</file>
   >   <encoder>
   >    <pattern>%lo{5}: %d{ISO8601}: Thread[%t]: TransactionId[%X{transactionId}]%n%level: %m%n%ex</pattern>
   >   </encoder>
   >  </appender>
   >  <logger name="org.forgerock.openam.core.rest.session.action.SetPropertyActionHandler" level="Error" >
   >   <appender-ref ref="Session"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.session.action.GetPropertyActionHandler" level="Error" >
   >   <appender-ref ref="Session"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.session.SessionResource" level="Error" >
   >   <appender-ref ref="Session"/>
   >  </logger>
   >  <logger name="com.sun.identity.sm.ServerIDValidator" level="Error" >
   >   <appender-ref ref="Session"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.cts" level="Error" >
   >   <appender-ref ref="Session"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.session.action.LogoutActionHandler" level="Error" >
   >   <appender-ref ref="Session"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.dpro" level="Error" >
   >   <appender-ref ref="Session"/>
   >  </logger>
   >  <logger name="com.iplanet.sso.providers" level="Error" >
   >   <appender-ref ref="Session"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.session.action.ValidateActionHandler" level="Error" >
   >   <appender-ref ref="Session"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.session.action.GetSessionPropertiesActionHandler"
   >          level="Error" >
   >   <appender-ref ref="Session"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.session" level="Error" >
   >   <appender-ref ref="Session"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.sm.datalayer.impl.ldap.ExternalLdapConfig" level="Error" >
   >   <appender-ref ref="Session"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.session.action.UpdateSessionPropertiesActionHandler"
   >          level="Error" >
   >   <appender-ref ref="Session"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.session.SSOTokenPartialSessionFactory" level="Error" >
   >   <appender-ref ref="Session"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.sm.SMSConfigurationFactory" level="Error" >
   >   <appender-ref ref="Session"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.sm.datalayer.impl.SeriesTaskExecutorThread" level="Error" >
   >   <appender-ref ref="Session"/>
   >  </logger>
   >  <logger name="com.iplanet.dpro" level="Error" >
   >   <appender-ref ref="Session"/>
   >  </logger>
   >  <logger name="com.sun.identity.plugin.session.impl.FMSessionNotification" level="Error" >
   >   <appender-ref ref="Session"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.session.action.GetPropertyNamesActionHandler" level="Error" >
   >   <appender-ref ref="Session"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.session.SessionResourceUtil" level="Error" >
   >   <appender-ref ref="Session"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.session.SessionResourceV2" level="Error" >
   >   <appender-ref ref="Session"/>
   >  </logger>
   >  <logger name="com.sun.identity.sm.SiteIDValidator" level="Error" >
   >   <appender-ref ref="Session"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.core.rest.session.action.DeletePropertyActionHandler" level="Error" >
   >   <appender-ref ref="Session"/>
   >  </logger>
   >
   >  <!--    UmaProvider     -->
   >  <appender name="UmaProvider" class="ch.qos.logback.core.FileAppender">
   >   <file>/path/to/debug/UmaProvider</file>
   >   <encoder>
   >    <pattern>%lo{5}: %d{ISO8601}: Thread[%t]: TransactionId[%X{transactionId}]%n%level: %m%n%ex</pattern>
   >   </encoder>
   >  </appender>
   >  <logger name="org.forgerock.openam.oauth2.AccessTokenProtectionFilter" level="Error" >
   >   <appender-ref ref="UmaProvider"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.uma.UmaSettingsImpl" level="Error" >
   >   <appender-ref ref="UmaProvider"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.uma.PendingRequestEmailTemplate" level="Error" >
   >   <appender-ref ref="UmaProvider"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.uma.rest.UmaPolicyApplicationListener" level="Error" >
   >   <appender-ref ref="UmaProvider"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.uma.rest.UmaResourceSetRegistrationHook" level="Error" >
   >   <appender-ref ref="UmaProvider"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.oauth2.resources.labels" level="Error" >
   >   <appender-ref ref="UmaProvider"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.uma.UmaProviderSettingsImpl" level="Error" >
   >   <appender-ref ref="UmaProvider"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.uma.UmaGrantTypeHandler" level="Error" >
   >   <appender-ref ref="UmaProvider"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.uma.rest.UmaLabelResource" level="Error" >
   >   <appender-ref ref="UmaProvider"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.uma.PendingRequestsService" level="Error" >
   >   <appender-ref ref="UmaProvider"/>
   >  </logger>
   >  <logger name="org.forgerock.openam.uma.audit" level="Error" >
   >   <appender-ref ref="UmaProvider"/>
   >  </logger>
   >
   >  <!--    WebServices     -->
   >  <appender name="WebServices" class="ch.qos.logback.core.FileAppender">
   >   <file>/path/to/debug/WebServices</file>
   >   <encoder>
   >    <pattern>%lo{5}: %d{ISO8601}: Thread[%t]: TransactionId[%X{transactionId}]%n%level: %m%n%ex</pattern>
   >   </encoder>
   >  </appender>
   >  <logger name="com.sun.identity.liberty.ws.paos" level="Error" >
   >   <appender-ref ref="WebServices"/>
   >  </logger>
   >  <logger name="com.sun.identity.liberty.ws.common" level="Error" >
   >   <appender-ref ref="WebServices"/>
   >  </logger>
   >  <logger name="com.sun.identity.policy.plugins.WebServicesClients" level="Error" >
   >   <appender-ref ref="WebServices"/>
   >  </logger>
   >  <logger name="com.sun.identity.liberty.ws.soapbinding" level="Error" >
   >   <appender-ref ref="WebServices"/>
   >  </logger>
   >  <logger name="com.sun.identity.authentication.spi.WSSReplayPasswd" level="Error" >
   >   <appender-ref ref="WebServices"/>
   >  </logger>
   >
   >  <!--    OtherLogging rotation created so that ROOT could be set without outputting same debug to all files     -->
   >  <appender name="OtherLogging" class="ch.qos.logback.core.rolling.RollingFileAppender">
   >   <rollingPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedRollingPolicy">
   >    <file>/path/to/debug/OtherLogging</file>
   >    <fileNamePattern>/path/to/debug/OtherLogging.%d{yyyy-MM-dd}-%i</fileNamePattern>
   >    <maxFileSize>1GB</maxFileSize>
   >   </rollingPolicy>
   >   <encoder>
   >    <pattern>%lo{5}: %d{ISO8601}: Thread[%t]: TransactionId[%X{transactionId}]%n%level: %m%n%ex</pattern>
   >   </encoder>
   >  </appender>
   >  <root level="Error">
   >   <appender-ref ref="OtherLogging" />
   >  </root>
   > </configuration>
   > ```Download [`logback.xml`](../_attachments/logback.xml). |

2. In your empty `logback.xml` file, add a top-level element called `configuration`.

   For example:

   ```xml
   <configuration>
   </configuration>
   ```

   This element will contain the configuration of the loggers and appenders, added in later steps.

   * To instruct AM to periodically check the `logback.xml` file for changes, and apply them to the running instance, add both a `scan` and a `scanPeriod` attribute to the `<configuration>` element. For example:

     ```xml
     <configuration scan="true" scanPeriod="30 seconds">
     </configuration>
     ```

     |   |                                                                                                                                                                                                                                                                                                               |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If AM isn't configured to scan the `logback.xml` file for changes, you'll need to restart the instance to pick up any changes.You can set the `scanPeriod` attribute to a longer time period, for example one hour, so you don't have to restart a running system when you need to alter the debugging level. |

     Learn more in [Automatically reloading configuration file upon modification](https://logback.qos.ch/manual/configuration.html#autoScan) in the *Logback Documentation*.

   * To troubleshoot issues when configuring debug logging using the `logback.xml` file, add a `debug` attribute, set to `true`, to the `<configuration>` element. For example:

     ```xml
     <configuration debug="true">
     </configuration>
     ```

     AM records debug logging status information to the default log file for the container in which it's running. For example, in Tomcat, status messages about the configuration of logback are recorded in the `Catalina.out` file.

     Learn more in [Status data](https://logback.qos.ch/manual/configuration.html#dumpingStatusData) in the *Logback Documentation*.

3. Define one or more appenders in the `<configuration>` element.

   The following example appender logs messages to a file named `debug.out` in the default AM debug directory:

   ```xml
   <configuration>
     <appender name="DEBUG.OUT" class="ch.qos.logback.core.FileAppender">
       <file>am/var/debug/debug.out</file>
       <encoder>
         <pattern>%lo{5}: %d{ISO8601}: Thread[%t]: TransactionId[%X{transactionId}]%n%level: %m%n%ex</pattern>
       </encoder>
     </appender>
   </configuration>
   ```

   The pattern in the above example creates debug log entries that are identical to the output produced by previous versions of AM, including the transaction ID to aid with tracking events as they occur throughout the system.

   |   |                                                                                                                                                                  |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can also define an appender that uses the JsonLayout class to include the transaction ID automatically. Learn more in [Format log files](#format-log-files). |

4. Define one or more loggers in the `<configuration>` element.

   Loggers specify which classes to capture debug messages from, including any sub-classes. They also specify the level of debug information to capture, and which appender is used to store the output.

   This example logger applies the `Debug` level to the `scripts.OIDC_CLAIMS.36863ffb-40ec-48b9-94b1-9a99f71cc3b5.(OIDC Claims Script)`. Script loggers are only created after the script has executed at least once. The output is recorded in the file specified in the `debug.out` appender, created in an earlier step:

   ```xml
   <configuration>
     <appender name="DEBUG.OUT" class="ch.qos.logback.core.FileAppender">
       <file>am/var/debug/debug.out</file>
       <encoder>
         <pattern>%lo{5}: %d{ISO8601}: Thread[%t]: TransactionId[%X{transactionId}]%n%level: %m%n%ex</pattern>
       </encoder>
     </appender>
     <logger name="scripts.OIDC_CLAIMS.36863ffb-40ec-48b9-94b1-9a99f71cc3b5.(OIDC Claims Script)" level="Debug" >
       <appender-ref ref="DEBUG.OUT" />
     </logger>
   </configuration>
   ```

5. Define a single `<root>` catch-all element in the `<configuration>` element, to specify the global logging level for all classes that don't match any of the loggers defined in the `logback.xml` file.

   ```xml
   <configuration>
     <appender name="DEBUG.OUT" class="ch.qos.logback.core.FileAppender">
       <file>am/var/debug/debug.out</file>
       <encoder>
         <pattern>%lo{5}: %d{ISO8601}: Thread[%t]: TransactionId[%X{transactionId}]%n%level: %m%n%ex</pattern>
       </encoder>
     </appender>
     <logger name="scripts.OIDC_CLAIMS.36863ffb-40ec-48b9-94b1-9a99f71cc3b5.(OIDC Claims Script)" level="Debug" >
       <appender-ref ref="DEBUG.OUT" />
     </logger>
     <root level="Error">
       <appender-ref ref="DEBUG.OUT" />
     </root>
   </configuration>
   ```

6. Save your changes.

   The changes are applied the next time you restart AM, or the container in which it runs.

   |   |                                                                                                                                                                                                                                                                             |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you are editing an existing `logback.xml` that AM has already loaded, and contains the `scan="true"` attribute, you don't need to reboot.Instead, wait for the amount of time specified in the `scanPeriod` attribute, and the new configuration will be loaded into AM. |

7. To confirm the configuration from the `logback.xml` file has loaded, go to the `Logback.jsp` file, for example at `https://am.example.com:8443/am/Logback.jsp`, which reflects the configuration found:

   ![Logback.jsp reflecting the configuration in logback.xml](_images/logback-page-from-xml.png)

   Any changes made in the `Logback.jsp` are temporary and aren't persisted to the `logback.xml` file.

### Output to stdout

Configure `logback.xml` to send logging to standard output. For example, for Apache Tomcat deployments, console output is typically redirected to the Tomcat logging file, `catalina.out`.

This example configuration captures all debug-level logging using the default `<root>` element, and redirects it to the STDOUT appender:

```xml
<configuration>
  <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender"> (1)
    <encoder>
      <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
    </encoder>
  </appender>
  <root level="Debug">                                                 (2)
    <appender-ref ref="STDOUT" />
  </root>
</configuration>
```

1. To configure this example, create the following elements:

   |       |                                                                                     |
   | ----- | ----------------------------------------------------------------------------------- |
   | **1** | An `<appender>` that uses the `ch.qos.logback.core.ConsoleAppender` class.          |
   | **2** | A `<logger>`, or a `<root>` element as shown here, referencing the STDOUT appender. |

2. Save your changes as described in [Configure basic debug logging](#config-basic-logging).

3. Check that debug logging is now output to stdout. For example:

   `tail -f $TOMCAT_HOME/logs/catalina.out`

### Output to multiple locations

You can direct debug logging to more than one output location by defining multiple appenders and loggers. However, you can't define more than one root element.

This example defines loggers for the `com.sun.identity.sm.ServiceInstance` and `org.forgerock.openam.utils.MapHelper` classes that output debug logging to file using the DEBUG.OUT appender.

All warning-level logging is also directed to standard output using the STDOUT appender.

```xml
<configuration>
  <appender name="DEBUG.OUT" class="ch.qos.logback.core.FileAppender"> (1)
    <file>am/var/debug/debug.out</file>
    <encoder>
      <pattern>%lo{5}: %d{ISO8601}: Thread[%t]: TransactionId[%X{transactionId}]%n%level: %m%n%ex</pattern>
    </encoder>
  </appender>
  <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender"> (2)
    <encoder>
      <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
    </encoder>
  </appender>
  <logger name="com.sun.identity.sm.ServiceInstance" level="Debug"> (3)
      <appender-ref ref="DEBUG.OUT" />
    </logger>
  <logger name="org.forgerock.openam.utils.MapHelper" level="Debug">  (3)
    <appender-ref ref="DEBUG.OUT" />
  </logger>
  <root level="Warning">                                                 (4)
    <appender-ref ref="STDOUT" />
  </root>
</configuration>
```

1. To configure this example, create the following elements:

   |       |                                                                                     |
   | ----- | ----------------------------------------------------------------------------------- |
   | **1** | An `<appender>` that uses the `ch.qos.logback.core.FileAppender` class.             |
   | **2** | An `<appender>` that uses the `ch.qos.logback.core.ConsoleAppender` class.          |
   | **3** | A `<logger>` for each script, referencing the DEBUG.OUT appender.                   |
   | **4** | A `<logger>`, or a `<root>` element as shown here, referencing the STDOUT appender. |

2. Save and verify your changes as described in [Configure basic debug logging](#config-basic-logging).

### Format log files

The `org.forgerock.openam.logback.JsonLayout` class extends Logback JSON layout functionality by adding the transaction ID to the JSON output.

This example shows how you can include the JsonLayout class to format your log files:

```xml
<appender name="JSON" class="ch.qos.logback.core.rolling.RollingFileAppender"> (1)
  <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
    <fileNamePattern>am/var/debug/debugLog.%d{yyyy_MM_dd}.json</fileNamePattern>
    <maxHistory>7</maxHistory>
  </rollingPolicy>
  <encoder class="ch.qos.logback.core.encoder.LayoutWrappingEncoder">          (2)
    <layout class="org.forgerock.openam.logback.JsonLayout">                   (3)
      <jsonFormatter class="ch.qos.logback.contrib.jackson.JacksonJsonFormatter"> (4)
        <prettyPrint>true</prettyPrint>
      </jsonFormatter>
      <timestampFormat>yyyy-MM-dd' 'HH:mm:ss.SSS</timestampFormat>
      <appendLineSeparator>true</appendLineSeparator>
    </layout>
  </encoder>
</appender>
```

1. To configure this example, create the following elements:

   |       |                                                                                                        |
   | ----- | ------------------------------------------------------------------------------------------------------ |
   | **1** | An `<appender>` that uses the `ch.qos.logback.core.rolling.RollingFileAppender` class.                 |
   | **2** | An `<encoder>` that uses the `ch.qos.logback.core.encoder.LayoutWrappingEncoder` class.                |
   | **3** | A `<layout>` element that uses the `org.forgerock.openam.logback.JsonLayout` class.                    |
   | **4** | A `<jsonFormatter>` element that uses the `ch.qos.logback.contrib.jackson.JacksonJsonFormatter` class. |

2. Save and verify your changes as described in [Configure basic debug logging](#config-basic-logging).

   The use of the JsonLayout class results in the addition of a `transactionId` at the top level of the log entry.

   For example:

   ```json
   {
     "timestamp" : "2024-12-16 15:39:44.562",
     "level" : "ERROR",
     "thread" : "http-nio-8080-exec-6",
     "mdc" : {
       "transactionId" : "eb0664cc-4615-461e-973a-64a1fc4f659a-34695"
     },
     "logger" : "org.forgerock.openam.core.rest.authn.trees.AuthTrees",
     "message" : "Exception in processing the tree",
     "context" : "default",
     "transactionId" : "eb0664cc-4615-461e-973a-64a1fc4f659a-34695"
   }
   ```

### Control exception log length

The `org.forgerock.openam.logback.AmThrowableProxyConverter` class lets you control the length of logged exceptions.

Long stack traces can rapidly increase the size of your log files. Use the `AmThrowableProxyConverter` class to reduce the length of logged stack traces while retaining the information necessary to debug errors.

Add this class to the JsonLayout class. For example:

```xml
<layout class="org.forgerock.openam.logback.JsonLayout">
  <jsonFormatter class="ch.qos.logback.contrib.jackson.JacksonJsonFormatter">
    <prettyPrint>true</prettyPrint>
  </jsonFormatter>
  <throwableProxyConverter class="org.forgerock.openam.logback.AmThrowableProxyConverter">
    <length>short</length>
  </throwableProxyConverter>
  <timestampFormat>yyyy-MM-dd' 'HH:mm:ss.SSS</timestampFormat>
  <appendLineSeparator>true</appendLineSeparator>
</layout>
```

The length can be one of the following:

* `short`: AM logs only the essential information from the stack trace.

* `full`: AM logs the full stack trace.

* Any integer: AM logs the number of lines corresponding to the integer.

Setting the length to `0` means that AM doesn't log stack traces.

### Rotate debug logs

Logback provides built-in support for a number of log file rotation schemes, including time- and-size based rotation. If you have configured AM with a `logback.xml` file, you can configure log file rotation in the appenders, as follows:

1. In the `<configuration>` element, create an appender that uses the `ch.qos.logback.core.rolling.RollingFileAppender` class, for example:

   ```xml
   <appender name="DAILYLOG" class="ch.qos.logback.core.rolling.RollingFileAppender">
     <encoder>
       <pattern>%lo{5}: %d{ISO8601}: Thread[%t]: TransactionId[%X{transactionId}]%n%level: %m%n%ex</pattern>
     </encoder>
   </appender>
   ```

   Within the appender, specify whether to rotate based on time, and optionally also size, as follows:

   * To rotate the log files based only on time, add a `<rollingPolicy>` element to the appender, which uses the `ch.qos.logback.core.rolling.TimeBasedRollingPolicy` class.

     Include a `<fileNamePattern>` element that defines when the log files should roll over, and the naming convention.

     For example, the following appender rolls the log file over at midnight each day, and includes the date in the filename:

     ```xml
     <appender name="DAILYLOG" class="ch.qos.logback.core.rolling.RollingFileAppender">
       <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
         <fileNamePattern>am/var/debug/dailyLog.%d{yyyy-MM-dd}.log</fileNamePattern>
       </rollingPolicy>
       <encoder>
         <pattern>%lo{5}: %d{ISO8601}: Thread[%t]: TransactionId[%X{transactionId}]%n%level: %m%n%ex</pattern>
       </encoder>
     </appender>
     ```

   * To rotate the log files based on both time and size, add a `<rollingPolicy>` element to the appender, which uses the `ch.qos.logback.core.rolling.SizeAndTimeBasedRollingPolicy` class.

     Include a `<fileNamePattern>` element that defines when the log files should roll over, and where the counter for rolling over based on size occurs, specified by including `%i`. You must also include a `<maxFileSize>` element to define the maximum size of the log files.

     For example, the following appender rolls the log file over at midnight each day, but earlier if the file reaches 2 gigabytes in size, and includes the date in the filename:

     ```xml
     <appender name="DAILYLOG2GB" class="ch.qos.logback.core.rolling.RollingFileAppender">
       <rollingPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedRollingPolicy">
         <fileNamePattern>am/var/debug/dailyLog2GB.%d{yyyy-MM-dd}-%i.log</fileNamePattern>
         <maxFileSize>2GB</maxFileSize>
       </rollingPolicy>
       <encoder>
         <pattern>%lo{5}: %d{ISO8601}: Thread[%t]: TransactionId[%X{transactionId}]%n%level: %m%n%ex</pattern>
       </encoder>
     </appender>
     ```

2. Save and verify your changes as described in [Configure basic debug logging](#config-basic-logging).

   Debug log files will roll over each night, and also if they reach the 2GB size limit. The file names will contain the date, and a counter to signify the order in which they were written.

## Change the startup debug settings

You can configure the settings that are applied when AM starts up and there is no `logback.xml` file present.

The settings specified as defaults will be reflected in the `Logback.jsp` file, for example at `https://am.example.com:8443/am/Logback.jsp`. However, they won't override the configuration contained with a custom `logback.xml` file.

### Set the default debug level

These steps set the default debug level used by all loggers, when AM starts up:

1. In the AM admin UI, go to Deployment > Servers > *server name* > General > Debugging.

2. Select an option from the Debug Level field.

   The default level for debug logging is `Error`. This level is appropriate for normal production operations, in which case no debug log messages are expected.

   Setting the debug log level to `Warning` increases the volume of messages. Setting the debug log level to `Message` dumps detailed trace messages.

   Unless told to do so by Ping Identity support, don't use `Warning` or `Message` levels as a default in production. Instead, set the levels on a per-class basis.

3. Save your changes.

   Changes are applied immediately.

### Set the default debug directory

These steps set the default directory used to store debug log files:

1. In the AM admin UI, go to Deployment > Servers > *server name* > General > Debugging.

2. Enter a directory in which to store log files in the Debug Directory field.

   The default value is as follows:

   * Unix/Linux

   * Windows

   `%BASE_DIR%/var/debug`

   `BASE_DIR` is the local PingAM directory; for example `/path/to/am`.

   `%BASE_DIR%\var\debug`

   `BASE_DIR` is the local PingAM directory; for example `/path/to/am`.

   |   |                                                                                                                       |
   | - | --------------------------------------------------------------------------------------------------------------------- |
   |   | Make sure the specified folder can be written to by the account that is running AM or the container in which it runs. |

3. Save your changes.

   The changes are applied the next time you restart AM, or the container in which it runs.

### Combine log messages in a single file

These steps log all debug messages to a single `debug.out` file:

1. In the AM admin UI, go to Deployment > Servers > *server name* > General > Debugging.

2. Set the Merge Debug Files property to `On`.

3. Save your changes.

   Changes are applied immediately.

   All debug log messages are written to a single debug file named `debug.out`. The file is located in the directory specified in the Debug Directory property. Learn more in [Set the default debug directory](#log-debug-directory).

---

---
title: Graphite monitoring
description: Send PingAM monitoring metrics to Graphite for storage and graphing
component: pingam
version: 8.1
page_id: pingam:monitoring:monitoring-graphite
canonical_url: https://docs.pingidentity.com/pingam/8.1/monitoring/monitoring-graphite.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Monitoring"]
page_aliases: ["monitoring-guide:monitoring-graphite.adoc"]
section_ids:
  enable-graphite: Enable the Graphite monitoring interface
---

# Graphite monitoring

Graphite is third-party software used for storing monitoring data, and rendering graphs of the data. For more information about installing and running Graphite, see the [Graphite documentation](https://graphiteapp.org/#overview).

For monitoring metrics reference, refer to [Monitoring metrics](monitoring-metrics.html).

## Enable the Graphite monitoring interface

1. Ensure you have [enabled monitoring](monitoring-am.html#enable-monitoring).

2. Go to Configure > Global Services > Monitoring.

3. On the Secondary Configurations tab, click Add a Secondary Configuration.

4. Select Graphite Reporter.

5. Specify the Name and Hostname of the Graphite instance to push the metrics data to.

6. Click Create.

---

---
title: Implement audit logging
description: Configure audit logging in PingAM with global or realm-specific event handlers to track security events and system activity
component: pingam
version: 8.1
page_id: pingam:monitoring:implementing-audit
canonical_url: https://docs.pingidentity.com/pingam/8.1/monitoring/implementing-audit.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Security", "Setup &amp; Configuration", "Monitoring"]
page_aliases: ["security-guide:implementing-audit.adoc", "monitoring-guide:implementing-audit.adoc"]
section_ids:
  configuring-audit-logging: Configure audit logging
  configure-global-audit-logging: Global audit logging
  configure-realm-audit-logging: Realm-specific audit logging
  configuring-audit-event-handlers: Configure audit event handlers
  configuring-json-audit-event-handlers: JSON audit event handler
  configuring-csv-audit-event-handlers: CSV audit event handler
  configuring-syslog-audit-event-handlers: Syslog audit event handler
  implementing-jdbc-audit-event-handlers: JDBC audit event handler
  prepare-audit-logging-jdbc: Prepare for JDBC audit logging
  configure-audit-logging-jdbc: Configure a JDBC audit event handler
  configuring-jms-audit-event-handlers: JMS audit event handler
  prepare-audit-logging-jms: Prepare for JMS audit logging
  configure-jms-audit-event-handler: Configure a JMS audit event handler
  configuring-trusttransactionheader-system-property: Trust transaction headers
---

# Implement audit logging

When you implement the audit logging service, decide whether you require specific audit systems per realm, or if a global configuration suits your deployment. Next, determine which event handlers suit your needs from those supported by AM. Refer to the following sections for more information:

* [Configure audit logging](#configuring-audit-logging)

* [Configure audit event handlers](#configuring-audit-event-handlers)

* [Trust transaction headers](#configuring-trusttransactionheader-system-property), to configure the propagation of transaction IDs across the Ping Advanced Identity Software.

## Configure audit logging

AM's default audit event handler is the JSON audit event handler, which comes configured and enabled for the global audit logging service. The global configuration is used to control audit logging in realms that do not have the audit logging service added to them. AM also supports configuring an audit logging service on a per-realm basis.

The JSON audit event handler stores its JSON log files under `/path/to/am/var/audit/`.

* To modify the global audit logging configuration, refer to [Global audit logging](#configure-global-audit-logging).

* To override the global audit logging configuration for a realm, refer to [Realm-specific audit logging](#configure-realm-audit-logging).

### Global audit logging

1. In the AM admin UI, go to Configure > Global Services > Audit Logging.

2. Configure the following options on the Global Attributes tab:

   * Activate Audit logging to start the audit logging feature.

   * In the Field whitelist filters and Field blacklist filters lists, enter any values to include (allowlist) or exclude (denylist) from the audit event logs.

     AM has a predefined allowlist that only records values that do not contain sensitive information. Use the filters to override the built-in list, or to hide additional values that you do not want recorded.

     |   |                                                                                                                                                                                                                                                                                                                                                      |
     | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | You can suppress logging certain event types to improve performance. These event types aren't logged, regardless of the configuration of the filter lists.To suppress audit event types, list the events as values of the `org.forgerock.openam.audit.identity.activity.events.blacklist` [advanced server property](../setup/server-advanced.html). |

     For information about the fields that appear in the default allowlist, refer to [Audit log default allowlist](audit-logging-ref.html#audit-log-whitelist).

     To specify an additional field or value to be allowlisted, or denylisted, add a value using a JSON pointer-like syntax that starts with the event topic (`access`, `activity`, `authentication`, or `config`), followed by the field name, or the path to the value in the field.

     The lists allow two types of filtering:

     * Filter fields in events.

       Fine-grained event filtering lets you capture or hide specific information such as HTTP headers, query parameters, or potentially sensitive data.

       For example, if you are logging identity changes (`AM-IDENTITY-CHANGE` has been removed from the `org.forgerock.openam.audit.identity.activity.events.blacklist` property) you could filter out the surnames of user identities by hiding the sn field from activity events.

       To hide surname values before and after an identity change, you would add the following JSON pointers to the Field blacklist filters property:

       ```
       /activity/before/sn
       /activity/after/sn
       ```

       To hide the original surname (before a change), you would add only \`/activity/before/sn \` to the Field blacklist filters property.

     * Filter specific values in fields that store key-value pairs as JSON, such as the HTTP headers, query parameters, and cookies.

       For example, to include the `Accept-Language` value in the http.request.headers field in *access* events, add the following pointer to the Field whitelist filters list:

       ```
       /access/http/request/headers/accept-language
       ```

   * Click Save Changes.

     For information on configuring audit logging properties, refer to [Audit logging](../setup/services-configuration.html#global-audit).

3. On the Secondary Configurations tab, you can edit the configuration of the Global JSON Handler and create new audit event handlers.

   For more information, refer to [Configure audit event handlers](#configuring-audit-event-handlers).

### Realm-specific audit logging

You can configure the audit logging service for realms, allowing you to configure realm-specific log locations and handler types.

When the audit logging service is added to a realm, it inherits the configuration defined under Configure > Global Services > Audit Logging > Realm Defaults. Properties configured explicitly in the realm-level service override the realm defaults.

To configure the audit logging service in a realm, perform the following steps:

1. Go to Realms > *realm name* > Services.

2. Click Add a Service.

3. From the Choose a service type drop-down list, choose Audit Logging.

4. Click Create.

   On the Audit Logging Service page, configure the Audit Logging Service as follows:

   1. Ensure audit logging is Enabled.

      In the Field whitelist filters and Field blacklist filters lists, enter any values to include (allowlist) or exclude (denylist) from the audit event logs.

      AM has a predefined allowlist that only records values that do not contain sensitive information. Use the filters to override the built-in list, or to hide additional values that you do not want recorded.

      |   |                                                                                                                                                                                                                                                                                                                                                      |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | You can suppress logging certain event types to improve performance. These event types aren't logged, regardless of the configuration of the filter lists.To suppress audit event types, list the events as values of the `org.forgerock.openam.audit.identity.activity.events.blacklist` [advanced server property](../setup/server-advanced.html). |

      For information about the fields that appear in the default allowlist, refer to [Audit log default allowlist](audit-logging-ref.html#audit-log-whitelist).

      To specify an additional field or value to be allowlisted, or denylisted, add a value using a JSON pointer-like syntax that starts with the event topic (`access`, `activity`, `authentication`, or `config`), followed by the field name, or the path to the value in the field.

      The lists allow two types of filtering:

      * Filter fields in events.

        Fine-grained event filtering lets you capture or hide specific information such as HTTP headers, query parameters, or potentially sensitive data.

        For example, if you are logging identity changes (`AM-IDENTITY-CHANGE` has been removed from the `org.forgerock.openam.audit.identity.activity.events.blacklist` property) you could filter out the surnames of user identities by hiding the sn field from activity events.

        To hide surname values before and after an identity change, you would add the following JSON pointers to the Field blacklist filters property:

        ```
        /activity/before/sn
        /activity/after/sn
        ```

        To hide the original surname (before a change), you would add only \`/activity/before/sn \` to the Field blacklist filters property.

      * Filter specific values in fields that store key-value pairs as JSON, such as the HTTP headers, query parameters, and cookies.

        For example, to include the `Accept-Language` value in the http.request.headers field in *access* events, add the following pointer to the Field whitelist filters list:

        ```
        /access/http/request/headers/accept-language
        ```

   2. Click Save.

      For information on configuring audit logging properties, refer to [Audit logging](../setup/services-configuration.html#global-audit).

5. On the Secondary Configurations tab, choose Add a Secondary Configuration.

   Choose an event handler from the list.

   For more information about supported event handlers and how to configure then, refer to [Configure audit event handlers](#configuring-audit-event-handlers).

## Configure audit event handlers

AM supports the following types of audit event handlers:

**Audit event handlers**

| Audit event handler type | Publishes to          | How to configure                                                       |
| ------------------------ | --------------------- | ---------------------------------------------------------------------- |
| JSON                     | JSON files            | [JSON audit event handler](#configuring-json-audit-event-handlers)     |
| CSV (*Deprecated*)       | CSV files             | [CSV audit event handler](#configuring-csv-audit-event-handlers)       |
| Syslog (*Deprecated*)    | The syslog daemon     | [Syslog audit event handler](#configuring-syslog-audit-event-handlers) |
| JDBC (*Deprecated*)      | A relational database | [JDBC audit event handler](#implementing-jdbc-audit-event-handlers)    |
| JMS (*Deprecated*)       | JMS topics            | [JMS audit event handler](#configuring-jms-audit-event-handlers)       |

### JSON audit event handler

1. In the AM admin UI, determine whether to create the event handler in a realm or use the default global event handler, then take one of the following actions:

   * To create the event handler in the global configuration, go to Configure > Global Services > Audit Logging.

     Note that the JSON audit event handler is already configured in the global configuration. Click it to change its properties.

   * To create the event handler in a realm, go to Realms > *realm name* > Services > Audit Logging.

2. On the Secondary Configurations tab, click Global JSON Handler or the Edit icon on the right if present. If no handler is present, click Add a Secondary Configuration, and choose JSON.

3. On the New JSON configuration page, enter a name for the event handler. For example, `JSON Audit Event Handler`.

4. (Optional) In the Rotation Times field, enter a time duration after midnight to trigger file rotation, in seconds. For example, you can provide a value of `3600` to trigger rotation at 1:00 AM. Negative durations are not supported.

5. Click Create.

   After the JSON audit event handler is created, several configuration tabs appear. To configure the event handler, perform the following steps:

6. On the General Handler Configuration tab, enable the event handler and configure the topics for your audit logs:

   * Choose Enabled to activate the event handler, if disabled.

   * Choose the [audit log topics](audit-logging.html#audit-log-topics) for your audit logs.

   * Click Save Changes.

7. On the JSON Configuration tab, configure JSON options:

   * Override the default location of your logs if necessary, and save your changes. The default value is as follows:

     * Unix/Linux

     * Windows

     `%BASE_DIR%/var/audit`

     `BASE_DIR` is the local PingAM directory; for example `/path/to/am`.

     `%BASE_DIR%\var\audit`

     `BASE_DIR` is the local PingAM directory; for example `/path/to/am`.

     |   |                                                                                                                                                                             |
     | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | You must configure a different log directory for each JSON audit event handler instance. If two instances are writing to the same file, it can interfere with log rotation. |

   * Enable ElasticSearch JSON Format Compatible to direct AM to generate JSON formats that are compatible with the ElasticSearch format.

   * In the File Rotation Retention Check Interval field, edit the time interval (seconds) to check the time-base file rotation policies.

   * Click Save Changes.

8. On the File Rotation tab, configure how files are rotated when they reach a specified file size or time interval:

   * Enable Rotation Enabled to activate file rotation. If file rotation is disabled, AM ignores log rotation and appends to the same file.

   * In the Maximum File Size field, enter the maximum size of an audit file before rotation.

   * (Optional). In the File Rotation Prefix field, enter an arbitrary string that will be prefixed to every audit log to identify it. This parameter is used when time-based or size-based rotation is enabled.

   * In the File Rotation Suffix field, enter a timestamp suffix based on the Java SimpleDateFormat that will be added to every audit log. This parameter is used when time-based or size-based log rotation is enabled. The default value is `-yyyy.MM.dd-kk.mm.ss`.

   * In the Rotation Interval field, enter a time interval to trigger audit log file rotation in seconds. A negative or zero value disables this feature.

   * (Optional) In the Rotation Times field, enter a time duration after midnight to trigger file rotation, in seconds. For example, you can provide a value of `3600` to trigger rotation at 1:00 AM. Negative durations are not supported.

   * Click Save Changes.

9. On the File Retention tab, configure how long log files should be retained in your system:

   * In the Maximum Number of Historical Files field, enter a number for allowed backup audit files. A value of `-1` indicates an unlimited number of files and disables the pruning of old history files.

   * In the Maximum Disk Space field, enter the maximum amount of disk space that the audit files can use. A negative or zero value indicates that this policy is disabled.

   * In the Minimum Free Space Required field, enter the minimum amount of disk space required to store audit files. A negative or zero value indicates that this policy is disabled.

   * Click Save Changes.

10. On the Buffering tab, configure whether log events should be buffered in memory before they are written to the JSON file:

    * In the Batch Size field, enter the maximum number of audit log events that can be buffered.

    * In the Write interval field, enter the time interval in milliseconds at which buffered events are written to a file.

    * Click Save Changes.

### CSV audit event handler

|   |                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------- |
|   | This audit event handler is [deprecated](https://docs.pingidentity.com/pingam/release-notes/stability.html#interface-stability). |

|   |                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Due to the security concerns of opening CSV files with Excel, OpenOffice, and other spreadsheet programs, it is recommended that you open CSV files with alternative software, such as a text editor. |

1. In the AM admin UI, determine whether to create the event handler in a realm or use the default global event handler, then take one of the following actions:

   * To create the event handler in the global configuration, go to Configure > Global Services > Audit Logging.

     Note that the CSV audit event handler is already configured in the global configuration. Click its name to change its properties.

   * To create the event handler in a realm, go to Realms > *realm name* > Services > Audit Logging.

2. On the Secondary Configurations tab, click Add a Secondary Configuration. Choose CVS from the list.

   On the New CVS page, enter the basic configuration for the new handler by performing the following actions:

3. Enter a name for the event handler. For example, `CSV Audit Event Handler`.

4. (Optional) In the Rotation Times field, enter a time duration after midnight to trigger file rotation, in seconds. For example, you can provide a value of `3600` to trigger rotation at 1:00 AM. Negative durations are not supported.

5. Enable or disable the Buffering option.

6. Click Create.

   After the CSV audit event handler is created, several configuration tabs appear. To configure the event handler, perform the following steps:

7. On the General Handler Configuration tab, enable the event handler and configure the topics for your audit logs:

   * Click Enabled to activate the event handler, if disabled.

   * Choose the [audit log topics](audit-logging.html#audit-log-topics) for your audit logs.

   * Click Save.

8. On the CSV Configuration tab, override the default location of your logs if necessary, and click Save Changes. The default value is as follows:

   * Unix/Linux

   * Windows

   `%BASE_DIR%/var/audit`, where `BASE_DIR` is the local PingAM directory; for example `/path/to/am`.

   `%BASE_DIR%\var\audit`, where `BASE_DIR` is the local PingAM directory; for example `/path/to/am`.

   |   |                                                                                                                                                                                           |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Configure a different log directory for each CVS audit event handler instance. If two instances are writing to the same file, it can interfere with log rotation and tamper-evident logs. |

9. On the File Rotation tab, configure how files are rotated when they reach a specified file size or time interval:

   * Click Rotation Enabled to activate file rotation. If file rotation is disabled, AM ignores log rotation and appends to the same file.

   * In the Maximum File Size field, enter the maximum size of an audit file before rotation.

   * (Optional). In the File Rotation Prefix field, enter an arbitrary string that will be prefixed to every audit log to identify it. This parameter is used when time-based or size-based rotation is enabled.

   * In the File Rotation Suffix field, enter a timestamp suffix based on the Java SimpleDateFormat that will be added to every audit log. This parameter is used when time-based or size-based log rotation is enabled. The default value is `-yyyy.MM.dd-kk.mm.ss`.

   * In the Rotation Interval field, enter a time interval to trigger audit log file rotation in seconds. A negative or zero value disables this feature.

   * (Optional) In the Rotation Times field, enter a time duration after midnight to trigger file rotation, in seconds. For example, you can provide a value of `3600` to trigger rotation at 1:00 AM. Negative durations are not supported.

   * Click Save Changes.

10. On the File Retention tab, configure how long log files should be retained in your system:

    * In the Maximum Number of Historical Files field, enter a number for allowed backup audit files. A value of `-1` indicates an unlimited number of files and disables the pruning of old history files.

    * In the Maximum Disk Space field, enter the maximum amount of disk space that the audit files can use. A negative or zero value indicates that this policy is disabled.

    * In the Minimum Free Space Required field, enter the minimum amount of disk space required to store audit files. A negative or zero value indicates that this policy is disabled.

    * Click Save Changes.

11. On the Buffering tab, configure whether log events should be buffered in memory before they are written to the CSV file:

    * Click Buffering Enabled to activate buffering.

      When buffering is enabled, all audit events are put into an in-memory buffer (one per handled topic), so that the original thread that generated the event can fulfill the requested operation, rather than wait for I/O to complete. A dedicated thread (one per handled topic) constantly pulls events from the buffer in batches and writes them to the CSV file. If the buffer becomes empty, the dedicated thread goes to sleep until a new item gets added. The default buffer size is `5000` bytes.

    * Enable the Flush Each Event Immediately option to write all buffered events before flushing.

      When the dedicated thread accesses the buffer, it copies the contents to an array to reduce contention, and then iterates through the array to write to the CSV file. The bytes written to the file can be buffered again in Java classes and the underlying operating system.

      When the Flush Each Event Immediately option is enabled, AM flushes the bytes after each event is written. If the feature is disabled (default), the Java classes and underlying operation system determine when to flush the bytes.

    * Click Save Changes.

12. On the Tamper Evident Configuration tab, configure whether to detect audit log tampering:

    * Click Is Enabled to activate the tamper evident feature for CSV logs.

      When tamper evident logging is enabled, AM generates an HMAC digest for each audit log event and inserts it into each audit log entry. The digest detects any addition or modification to an entry.

      AM also supports another level of tamper evident security by periodically adding a signature entry to a new line in each CSV file. The entry signs the preceding block of events, so that verification can establish if any of these blocks have been added, removed, or edited by some user.

    * In the Certificate Store Location field, enter the location of the keystore AM will use to sign the CSV logs, by default `%BASE_DIR%/%SERVER_URI%/Logger.jks`.

      The recommended approach is to create two keystores:

      * A keystore for AM to use. This keystore is configured in the Certificate Store Location field and must contain a signing key pair called `signature` and an HMAC key called `password`.

      * A keystore for the verification tool. This keystore must contain the HMAC `password` key, and the public key of the `signature` key pair.

    You can use a simple script to create your keystores, for example: [create-keystore.sh](../_attachments/create-keystore.sh).

    * In the Certificate Store Password field, enter the password of the keystore.

    * In the Signature Interval field, enter a value in seconds for AM to generate and add a new signature to the audit log entry.

    * Click Save Changes.

### Syslog audit event handler

|   |                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------- |
|   | This audit event handler is [deprecated](https://docs.pingidentity.com/pingam/release-notes/stability.html#interface-stability). |

AM can publish audit events to a syslog server, which is based on a widely-used logging protocol. You can configure your syslog settings on the AM admin UI.

1. In the AM admin UI, determine whether to create the event handler in a realm or use the default global event handler, then take one of the following actions:

   * To create the event handler in the global configuration, go to Configure > Global Services > Audit Logging.

   * To create the event handler in a realm, go to Realms > *realm name* > Services > Audit Logging.

2. On the Secondary Configurations tab, click Add a Secondary Configuration. Choose Syslog from the list.

   On the New Syslog page, enter the basic configuration for the new handler by performing the following actions:

3. Enter a name for the event handler. For example, `Syslog Audit Event Handler`.

4. In the Server hostname field, enter the hostname or IP address of the receiving syslog server.

5. In the Server port field, enter the port of the receiving syslog server.

6. In the Connection timeout field, enter the number of seconds to connect to the syslog server. If the server has not responded in the specified time, a connection timeout occurs.

7. Enable or disable the Buffering option.

8. Click Create.

   After the syslog audit event handler is created, several configuration tabs appear. To configure the event handler, perform the following steps:

9. On the General Handler Configuration tab, enable the event handler and configure the topics for your audit logs:

   * Click Enabled to activate the event handler, if disabled.

   * Choose the [audit log topics](audit-logging.html#audit-log-topics) for your audit logs.

   * Click Save Changes.

10. On the Audit Event Handler Factory tab, keep the default class name for the audit event handler.

11. On the Syslog Configuration tab, configure the main syslog event handler properties:

    * In the Server hostname field, enter the hostname or IP address of the receiving syslog server.

    * In the Server port field, enter the port of the receiving syslog server.

    * In the Connection timeout field, enter the number of seconds to connect to the syslog server. If the server has not responded in the specified time, a connection timeout occurs.

    * From the Transport Protocol drop-down list, choose TCP or UDP.

    * Choose the facility.

      A syslog message includes a PRI field that is calculated from the facility and severity values. All topics set the severity to `INFORMATIONAL` but you can choose the facility from the Facility drop-down list:

      **Syslog Facilities**

      | Facility | Description                            |
      | -------- | -------------------------------------- |
      | AUTH     | Security or authorization messages     |
      | AUTHPRIV | Security or authorization messages     |
      | CLOCKD   | Clock daemon                           |
      | CRON     | Scheduling daemon                      |
      | DAEMON   | System daemons                         |
      | FTP      | FTP daemon                             |
      | KERN     | Kernel messages                        |
      | LOCAL0   | Local use 0 (local0)                   |
      | LOCAL1   | Local use 1 (local1)                   |
      | LOCAL2   | Local use 2 (local2)                   |
      | LOCAL3   | Local use 3 (local3)                   |
      | LOCAL4   | Local use 4 (local4)                   |
      | LOCAL5   | Local use 5 (local5)                   |
      | LOCAL6   | Local use 6 (local6)                   |
      | LOCAL7   | Local use 7 (local7)                   |
      | LOGALERT | Log alert                              |
      | LOGAUDT  | Log audit                              |
      | LPR      | Line printer subsystem                 |
      | MAIL     | Mail system                            |
      | NEWS     | Network news subsystem                 |
      | NTP      | Network time protocol                  |
      | SYSLOG   | Internal messages generated by syslogd |
      | USER     | User-level messages                    |
      | UUCP     | Unix-to-unix-copy (UUCP) subsystem     |

    * Click Save Changes.

12. On the Buffering tab, configure whether you want buffering or not:

    * Click Buffering Enabled to activate it.

      When buffering is enabled, all audit events that get generated are formatted as syslog messages and put into a queue. A dedicated thread constantly pulls events from the queue in batches and transmits them to the syslog server. If the queue becomes empty, the dedicated thread goes to sleep until a new item gets added. The default queue size is `5000`.

    * Click Save Changes.

### JDBC audit event handler

|   |                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------- |
|   | This audit event handler is [deprecated](https://docs.pingidentity.com/pingam/release-notes/stability.html#interface-stability). |

You can configure AM to write audit logs to Oracle, MySQL, PostgreSQL, or other JDBC databases. AM writes audit log records to the following tables: `am_auditaccess`, `am_auditactivity`, `am_auditauthentication`, and `am_auditconfig`. For more information on the JDBC table formats for each of the logs, refer to [JDBC audit log tables](audit-logging-ref.html#jdbc-audit-log-tables).

Before configuring the JDBC audit event handler, you must perform several steps to allow AM to log to the database:

#### Prepare for JDBC audit logging

1. Create tables in the relational database in which you will write the audit logs. The SQL for Oracle, PostgreSQL, and MySQL table creation is in the `audit.sql` file under `/path/to/tomcat/webapps/am/WEB-INF/template/sql/db-type`.

   If you are using a different relational database, tailor one of the provided `audit.sql` files to conform to your database's SQL syntax.

2. JDBC audit logging requires a database user with read and write privileges for the audit tables. Do one of the following:

   * Identify an existing database user and grant that user privileges for the audit tables.

   * Create a new database user with read and write privileges for the audit tables.

3. Obtain the JDBC driver from your database vendor. Place the JDBC driver `.zip` or `.jar` file in the container's `WEB-INF/lib` classpath.

   For example, place the JDBC driver in `/path/to/tomcat/webapps/am/WEB-INF/lib` if you use Apache Tomcat.

The following procedure describes how to configure a JDBC audit event handler. Perform the following steps after you have created audit log tables in your database and installed the JDBC driver in the AM web container:

#### Configure a JDBC audit event handler

1. In the AM admin UI, determine whether to create the event handler in a realm or use the default global event handler, then take one of the following actions:

   * To create the event handler in the global configuration, go to Configure > Global Services > Audit Logging.

   * To create the event handler in a realm, go to Realms > *realm name* > Services > Audit Logging.

2. On the Secondary Configurations tab, click Add a Secondary Configuration. Choose JDBC from the list.

   Enter the basic configuration for the new handler by performing the following actions:.

3. Enter a name for the event handler. For example, `JDBC Audit Event Handler`.

4. In the JDBC Database URL field, enter the URL for your database server. For example, `jdbc:oracle:thin:@//host.example.com:1521/ORCL`.

5. In the JDBC Driver field, enter the classname of the driver to connect to the database. For example:

   1. `oracle.jdbc.driver.OracleDriver` - for Oracle databases

   2. `com.mysql.jdbc.Driver` - for MySQL databases

   3. `org.postgresql.Driver` - for PostgreSQL databases

6. In the Database Username field, enter the username to authenticate to the database server.

   This user must have read and write privileges for the audit tables.

7. In the Database Password field, enter the password used to authenticate to the database server.

8. Enable or disable the Buffering option.

9. Click Create.

   After the JDBC audit event handler is created, several configuration tabs appear. To configure the event handler, perform the following steps:

10. On the General Handler Configuration tab, enable the handler and configure the topics for your audit logs:

    * Click Enabled to activate the event handler, if disabled.

    * Choose the [audit log topics](audit-logging.html#audit-log-topics) for your audit logs.

    * Click Save.

11. On the Audit Event Handler Factory tab, enter the fully-qualified class name of your custom JDBC audit event handler and save your changes.

12. On the Database Configuration tab, configure the main JDBC event handler properties:

    * From the Database Type drop-down list, choose the audit database type. The default value is `Oracle`.

    * In the JDBC Database URL field, enter the URL for your database server. For example, `jdbc:oracle:thin:@//host.example.com:1521/ORCL`.

    * In the JDBC Driver field, enter the classname of the driver to connect to the database. For example:

      1. `oracle.jdbc.driver.OracleDriver` - for Oracle databases

      2. `com.mysql.jdbc.Driver` - for MySQL databases

      3. `org.postgresql.Driver` - for PostgreSQL databases

    * In the Database Username field, enter the username to authenticate to the database server.

      This user must have read and write privileges for the audit tables.

    * In the Database Password field, enter the password used to authenticate to the database server.

    * In the Connection Timeout field, enter the maximum wait time before failing the connection.

    * In the Maximum Connection Idle Timeout field, enter the maximum idle time in seconds before the connection is closed.

    * In the Maximum Connection Time field, enter the maximum time in seconds for a connection to stay open.

    * In the Minimum Idle Connections field, enter the minimum number of idle connections allowed in the connection pool.

    * In the Maximum Connections field, enter the maximum number of connections in the connection pools.

    * Click Save.

13. On the Buffering tab, configure the buffering settings:

    * Click Buffering Enabled to start audit event buffering.

    * In the Buffer Size field, set the size of the event buffer queue where events should queue up before being written to the database.

      If the queue reaches full capacity, the process will block until a write occurs.

    * In the Write Interval field, set the interval in seconds in which buffered events are written to the database.

    * In the Writer Threads field, set the number of threads used to write the buffered events.

    * In the Max Batched Events field, set the maximum number of batched statements the database can support per connection.

    * Click Save Changes.

### JMS audit event handler

|   |                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------- |
|   | This audit event handler is [deprecated](https://docs.pingidentity.com/pingam/release-notes/stability.html#interface-stability). |

AM supports audit logging to a JMS message broker. JMS is a Java API for sending messages between clients using a publish and subscribe model as follows:

* AM audit logging to JMS requires that the JMS message broker supports using JNDI to locate a JMS connection factory. Refer to your JMS message broker documentation to verify that you can make connections to your broker by using JNDI before attempting to implement an AM JMS audit handler.

* AM acts as a JMS publisher client, publishing JMS messages containing audit events to a JMS *topic*.

  AM and JMS use the term *topic* differently. An *AM audit topic* is a category of audit log event that has an associated one-to-one mapping to a schema type. A *JMS topic* is a distribution mechanism for publishing messages delivered to multiple subscribers.

* A JMS subscriber client, which is not part of the AM software and must be developed and deployed separately from AM, subscribes to the JMS topic to which AM publishes audit events. The client then receives the audit events over JMS and processes them as desired.

Before configuring the JMS audit event handler, you must perform several steps to allow AM to publish audit events as a JMS client:

#### Prepare for JMS audit logging

1. Obtain JNDI connection properties that AM requires to connect to your JMS message broker. The specific connection properties vary depending on the broker. Refer to your JMS message broker documentation for details.

   For example, connecting to an Apache ActiveMQ message broker requires the following properties:

   **Example Apache ActiveMQ JNDI Connection Properties**

   | Property Name                 | Example Value                                            |
   | ----------------------------- | -------------------------------------------------------- |
   | `java.naming.factory.initial` | `org.apache.activemq.jndi.ActiveMQInitialContextFactory` |
   | `java.naming.provider.url`    | `tcp://localhost:61616`                                  |
   | `topic.audit`                 | `audit`                                                  |

2. Obtain the JNDI lookup name of the JMS connection factory for your JMS message broker.

   For example, for Apache ActiveMQ, the JNDI lookup name is `ConnectionFactory`.

3. Obtain the JMS client `.jar` file from your JMS message broker vendor. Add the `.jar` file to AM's classpath by placing it in the `WEB-INF/lib` directory.

   For example, place the JMS client `.jar` file in `/path/to/tomcat/webapps/am/WEB-INF/lib` if you use Apache Tomcat.

The following procedure describes how to configure a JMS audit event handler.

If your JMS message broker requires an SSL connection, you might need to perform additional, broker-dependent configuration tasks. For example, you might need to import a broker certificate into the AM keystore, or provide additional JNDI context properties.

Refer to your JMS message broker documentation for specific requirements for making SSL connections to your broker, and implement them as needed in addition to the steps in the following procedure.

Perform the following steps after you have installed the JMS client `.jar` file in the AM web container:

#### Configure a JMS audit event handler

1. In the AM admin UI, determine whether to create the event handler in a realm or use the default global event handler, then take one of the following actions:

   * To create the event handler in the global configuration, go to Configure > Global Services > Audit Logging.

   * To create the event handler in a realm, go to Realms > *realm name* > Services > Audit Logging.

2. On the Secondary Configurations tab, click Add a Secondary Configuration. Choose JMS from the list.

3. On the New JMS Configuration page, enter the basic configuration for the new handler by performing the following actions:

4. Enter a name for the event handler. For example, `JMS Audit Event Handler`.

5. Click Create.

   After the JMS audit event handler is created, several configuration tabs appear. To configure the event handler, perform the following steps:

6. On the General Handler Configuration tab, enable the handler and configure the topics for your audit logs:

   * Click Enabled to activate the event handler, if disabled.

   * Choose the [audit log topics](audit-logging.html#audit-log-topics) for your audit logs.

   * Click Save Changes.

7. On the Audit Event Handler Factory tab, keep the default class name for the audit event handler.

8. On the JMS Configuration tab, configure the main JMS event handler properties:

   * From the Delivery Mode drop-down list, choose the JMS delivery mode.

     With persistent delivery, the JMS provider ensures that messages are not lost in transit in case of a provider failure by logging messages to storage when they are sent. Therefore, persistent delivery mode guarantees JMS message delivery, while non-persistent mode provides better performance.

     The default delivery mode is `NON_PERSISTENT` delivery. Therefore, if your deployment requires delivery of every audit event to JMS subscriber clients, be sure to set the configuration to `PERSISTENT` delivery.

   * From the Session Mode drop-down list, choose the default setting, `AUTO`, unless your JMS broker implementation requires otherwise. Refer to your broker documentation for more information.

   * Specify properties that AM will use to connect to your JMS message broker as key-value pairs in the JNDI Context Properties field.

     AM is configured for the `audit` JNDI lookup name and JMS topic, but you can modify or delete this configuration, or add new key-value pairs. To add new key-value pairs, fill the Key and Value fields and click Add.

   * In the JMS Topic Name field, enter the name of the JMS topic to which AM will publish messages containing audit events.

     Subscriber clients that process AM audit events must subscribe to this topic.

   * In the JMS Connection Factory Name field, specify the JNDI lookup name of the JMS connection factory.

   * Click Save Changes.

9. On the Batch Events tab, configure how log events should be batched before they are published to the JMS message broker:

   * In the Capacity field, specify the maximum capacity of the publishing queue. Execution is blocked if the queue size reaches capacity.

   * In the Max Batched field, specify the maximum number of events to be delivered when AM publishes the events to the JMS message broker.

   * In the Writing Interval field, specify the interval (in seconds) between transmissions to JMS.

   * Click Save Changes.

## Trust transaction headers

AM supports the propagation of the transaction ID across the ForgeRock platform, such as from DS or IDM to AM, using the HTTP header `X-ForgeRock-TransactionId`. The `X-ForgeRock-TransactionId` header is automatically set in all outgoing HTTP calls from one ForgeRock product to another. You can also set this header from your own applications or scripts calling into the ForgeRock platform.

By default, the `org.forgerock.http.TrustTransactionHeader` system property is set to `false`, so that a malicious actor cannot flood the system with requests using the same transaction ID header to hide their tracks. Setting `org.forgerock.http.TrustTransactionHeader` to `true` trusts any incoming `X-ForgeRock-TransactionId` headers.

1. In the AM admin UI, go to Configure > Server Defaults > Advanced and scroll to the bottom of the list.

2. In the PROPERTY NAME column, add `org.forgerock.http.TrustTransactionHeader`. In the corresponding PROPERTY VALUE column, enter true.

3. Click + to add the property and save your work.

   Your AM instance will now accept incoming `X-ForgeRock-TransactionId` headers, which can be tracked in the audit logs.

4. Repeat this procedure for all servers that require this property.

---

---
title: JMX monitoring
description: Deprecated. Configure PingAM to accept Java Management Extension (JMX) client connections for monitoring, typically on port 9999
component: pingam
version: 8.1
page_id: pingam:monitoring:monitoring-jmx
canonical_url: https://docs.pingidentity.com/pingam/8.1/monitoring/monitoring-jmx.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Monitoring"]
page_aliases: ["maintenance-guide:monitoring-jmx.adoc", "monitoring-guide:monitoring-jmx.adoc"]
---

# JMX monitoring

|   |                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------- |
|   | This functionality is [deprecated](https://docs.pingidentity.com/pingam/release-notes/stability.html#interface-stability). |

You can configure AM to let you listen for Java Management Extension (JMX) clients, by default on port 9999. Go to Configure > Global Services > Monitoring in the AM admin UI and make sure both Monitoring Status and Monitoring RMI interface status are enabled.

A number of tools support JMX, including `jvisualvm` and `jconsole`. When you use `jconsole` to browse AM MBeans for example, the default URL for the AM running on the local system is `service:jmx:rmi:///jndi/rmi://localhost:9999/server`.

```bash
$ jconsole service:jmx:rmi:///jndi/rmi://localhost:9999/server &
```

To browse MBeans, connect to your web application container, and go to the AM MBeans. By default, JMX monitoring for the container is likely to be accessible only locally, using the process ID.

![You can monitor an instance over JMX.](_images/jconsole-to-openam.png)Figure 1. JConsole browsing MBeans

Also refer to [Monitoring and Management Using JMX Technology](https://docs.oracle.com/en/java/javase/25/management/monitoring-and-management-using-jmx-technology.html) for instructions on how to connect remotely, how to use SSL, and so on.

|   |                                                                                                                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | JMX has a limitation in that some Operations and CTS tables cannot be properly serialized from AM to JMX. As a result, only a portion of AM's monitoring information is available through JMX.Use Prometheus, Graphite, or common REST monitoring if possible. |

For monitoring metrics reference, refer to [Monitoring metrics](monitoring-metrics.html).

---

---
title: MBean monitoring (legacy)
description: Deprecated. Configure PingAM to access a web-based view of MBeans on port 8082 for legacy monitoring purposes
component: pingam
version: 8.1
page_id: pingam:monitoring:monitoring-web-pages
canonical_url: https://docs.pingidentity.com/pingam/8.1/monitoring/monitoring-web-pages.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Monitoring"]
page_aliases: ["maintenance-guide:monitoring-web-pages.adoc", "monitoring-guide:monitoring-web-pages.adoc"]
---

# MBean monitoring (legacy)

|   |                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------- |
|   | This legacy functionality is [deprecated](https://docs.pingidentity.com/pingam/release-notes/stability.html#interface-stability). |

You can configure AM to let you access a web-based view of AM MBeans on port 8082 where the core server runs, such as `https://am.example.com:8443/`. Go to Configure > Global Services > Monitoring in the AM admin UI and make sure both Monitoring Status and Monitoring HTTP interface status are enabled.

The default authentication file lets you authenticate over HTTP as user `demo`, password `changeit`. The user name and password are kept in the file specified, with the password encrypted:

```bash
$ cat openam/security/openam_mon_auth
demo AQICMBCKlwx6G3vzK3TYYRbtTpNYAagVIPNP
```

If you make changes to the authentication file, you must restart AM for the changes to take effect.

![You can monitor an instance through a web browser.](_images/web-based-monitoring.png)Figure 1. MBeans in a browser

---

---
title: Monitor AM instances
description: Monitor PingAM instances and gather monitoring data using health check endpoints and monitoring service
component: pingam
version: 8.1
page_id: pingam:monitoring:monitoring-am
canonical_url: https://docs.pingidentity.com/pingam/8.1/monitoring/monitoring-am.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Monitoring"]
page_aliases: ["maintenance-guide:monitoring-am.adoc", "monitoring-guide:monitoring-am.adoc"]
section_ids:
  check-instance-status: Check the status of an AM instance
  enable-monitoring: Enable monitoring in the console
---

# Monitor AM instances

AM provides a number of interfaces for you to check the status of AM instances and to gather monitoring data. This section describes the steps to enable monitoring and use the monitoring endpoints.

## Check the status of an AM instance

In certain deployments, such as Kubernetes, it can be useful to poll endpoints to check if an instance is running, and ready to handle requests. You can determine the status of an AM instance by using the following endpoints:

* `/json/health/live`

  Use the `live` endpoint to determine if AM instances are up and running.

  If the instance is running the endpoint returns an HTTP status code of `200`. If not, it returns a `503` response.

  For example, use the following `curl` command to determine when an AM instance is alive:

  ```bash
  $ curl --include --retry 10 --retry-connrefused 'https://am.example.com:8443/am/json/health/live'
  Warning: Transient problem: connection refused Will retry in 1 seconds. 10
  Warning: retries left.
  Warning: Transient problem: connection refused Will retry in 2 seconds. 9
  Warning: retries left.
  Warning: Transient problem: connection refused Will retry in 4 seconds. 8
  Warning: retries left.
  HTTP/1.1 200
  X-Frame-Options: SAMEORIGIN
  X-Content-Type-Options: nosniff
  Cache-Control: private
  Content-API-Version: resource=1.0
  Content-Length: 0
  Date: Mon, 09 Nov 2020 12:22:38 GMT
  ```

* `/json/health/ready`

  Use the `ready` endpoint to determine if AM instances are ready to process requests.

  If the instance is ready to process requests, the endpoint returns an HTTP status code of `200`. If not, it returns a `503` response.

  For example, use the following `curl` command to determine when an AM instance is ready to process requests:

  ```bash
  $ curl --include --retry 10 --retry-connrefused 'https://am.example.com:8443/am/json/health/ready'
  Warning: Transient problem: connection refused Will retry in 1 seconds. 10
  Warning: retries left.
  Warning: Transient problem: connection refused Will retry in 2 seconds. 9
  Warning: retries left.
  Warning: Transient problem: connection refused Will retry in 4 seconds. 8
  Warning: retries left.
  Warning: Transient problem: connection refused Will retry in 8 seconds. 7
  Warning: retries left.
  HTTP/1.1 200
  X-Frame-Options: SAMEORIGIN
  X-Content-Type-Options: nosniff
  Cache-Control: private
  Content-API-Version: resource=1.0
  Content-Length: 0
  Date: Mon, 09 Nov 2020 12:45:03 GMT
  ```

> **Collapse: Deprecated  page**
>
> AM provides a deprecated `isAlive.jsp` page, to check whether AM is up. Point your application to the file under the deployment URL, such as `https://am.example.com:8443/am/isAlive.jsp`.
>
> If you get a success code (with `Server is ALIVE:` in the body of the page returned), then the instance is in operation.
>
> The `isAlive.jsp` page is deprecated and will be removed in a future release. Update your environment to use the `live` and `ready` endpoints instead.

|   |                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The endpoints and `isAlive.jsp` page do not require authentication. You might want to restrict public access, and only allow access from internal infrastructure. |

## Enable monitoring in the console

To query some of the monitoring endpoints, such as Prometheus or CREST, you must enable the Monitoring service:

1. In the AM admin UI, go to Configure > Global Services > Monitoring.

2. Set `Monitoring Status` to enabled.

3. Click Save Changes.

Learn about configuring the service in [Monitoring service](../setup/services-configuration.html#global-monitoring-configuration).

---

---
title: Monitor with Prometheus
description: Configure Prometheus to monitor PingAM metrics and gather performance data from your deployment
component: pingam
version: 8.1
page_id: pingam:monitoring:monitoring-prometheus
canonical_url: https://docs.pingidentity.com/pingam/8.1/monitoring/monitoring-prometheus.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Monitoring"]
page_aliases: ["maintenance-guide:monitoring-prometheus.adoc", "monitoring-guide:monitoring-prometheus.adoc"]
section_ids:
  prometheus_endpoints: Prometheus endpoints
  configure_prometheus: Configure Prometheus
  enable-prometheus: Enable Prometheus monitoring
---

# Monitor with Prometheus

[Prometheus](https://prometheus.io/docs/introduction/overview) is third-party software used for gathering and processing monitoring data.

|   |                                                                                                                                                                                                                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Prometheus can monitor and process AM metrics but your deployment might benefit from further analysis and visualization. You can use tools such as Grafana to create customized charts and graphs based on the information Prometheus collects.Learn more about installing and running Grafana in the [Grafana documentation](https://grafana.com/docs/grafana/latest/). |

## Prometheus endpoints

AM exposes endpoints that Prometheus uses to gather metrics from the AM instance.

When you [enable Prometheus monitoring](#enable-prometheus), AM makes the Prometheus-formatted metrics available at the following endpoints:

* `/metrics/prometheus`

  The path of this endpoint is format-agnostic, but the response payload is identical to that from the `/json/metrics/prometheus` endpoint.

  Although this endpoint is new, it is also *deprecated* in this release and support for its use will be removed in a future release. Move to the `/metrics/prometheus/0.0.4` endpoint as soon as convenient.

* `/metrics/prometheus/0.0.4`

  The path of this endpoint is format-agnostic, but the response payload is slightly different to that from the `/metrics/prometheus` endpoint.

  Metrics that were previously suffixed with `_total` are suffixed with `_sum`, which conforms better to the latest version of Prometheus. For example:

  * `/metrics/prometheus/0.0.4` returns the metric `am_authorization_policy_set_evaluate_seconds_sum{outcome=outcome,policy_set=policy-set,}`

  * `/metrics/prometheus` returns the metric `am_authorization_policy_set_evaluate_seconds_total{outcome=outcome,policy_set=policy-set,}`

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `/json/metrics/prometheus` endpoint is deprecated. If you're using this endpoint, change your Prometheus configuration to use one of the new endpoints:* If your deployment doesn't rely on the response payload provided from the `/json/metrics/prometheus` endpoint, move straight to the `/metrics/prometheus/0.0.4` endpoint.

* If your deployment relies on the exact response payload provided from the `/json/metrics/prometheus` endpoint, move to the `/metrics/prometheus` endpoint first. Adapt your deployment to expect the different payload then move to the `/metrics/prometheus/0.0.4` endpoint. |

## Configure Prometheus

Configure Prometheus to monitor the AM endpoints in the Prometheus configuration file, `prometheus.yml`.

Learn more about configuring Prometheus in the [Prometheus configuration documentation](https://prometheus.io/docs/prometheus/latest/configuration/configuration/).

Learn more about PingAM monitoring metrics in [Monitoring metrics](monitoring-metrics.html).

## Enable Prometheus monitoring

1. Ensure you have [enabled monitoring](monitoring-am.html#enable-monitoring).

2. Go to Configure > Global Services > Monitoring.

3. On Secondary Configurations tab, click `prometheus`, then select Enabled.

4. In the Authentication Type menu, select one of the following options:

   * None. Prometheus doesn't need to authenticate when accessing the endpoint.

   * HTTP Basic. Prometheus must authenticate using a username and a password when accessing the endpoint.

5. If you selected HTTP Basic, specify a Username and Password.

   |   |                                                                                                                 |
   | - | --------------------------------------------------------------------------------------------------------------- |
   |   | If you set a Secret Label Identifier and AM finds a matching secret in a secret store, the Password is ignored. |

6. For greater security, define a Secret Label Identifier to use a secret in a secret store and rotate the secret periodically.

   AM uses this identifier to create a specific secret label, using the template `am.services.monitoring.prometheus.identifier.secret` where identifier is the value of Secret Label Identifier.

   The identifier can only contain alphanumeric characters `a-z`, `A-Z`, `0-9`, and periods (`.`). It can't start or end with a period.

   Learn more about using secrets in [Map and rotate secrets](../security/secret-mapping.html).

7. Save your work.

---

---
title: Monitoring and logs
description: Monitor PingAM instances and gather troubleshooting information through included interfaces, debug logging, and audit logging
component: pingam
version: 8.1
page_id: pingam:monitoring:preface
canonical_url: https://docs.pingidentity.com/pingam/8.1/monitoring/preface.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Monitoring", "Troubleshooting"]
page_aliases: ["index.adoc", "monitoring-guide:preface.adoc"]
---

# Monitoring and logs

This section describes how to check the status of an PingAM instance and how to gather monitoring and troubleshooting information.

[icon: chart-bar, set=fad, size=3x]

#### [Monitor instances](monitoring-am.html)

Monitor AM through any of the included interfaces.

[icon: bug, set=fad, size=3x]

#### [Enable debug logging](debug-logging.html)

Gather troubleshooting information.

[icon: user-secret, set=fad, size=3x]

#### [Audit logging](audit-logging.html)

Capture auditing events for system security and compliance.

---

---
title: Monitoring metrics
description: Monitor PingAM metrics through REST, JMX, Graphite, and Prometheus interfaces using summary and timer metric types
component: pingam
version: 8.1
page_id: pingam:monitoring:monitoring-metrics
canonical_url: https://docs.pingidentity.com/pingam/8.1/monitoring/monitoring-metrics.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Monitoring"]
page_aliases: ["maintenance-guide:monitoring-metrics.adoc", "monitoring-guide:monitoring-metrics.adoc"]
section_ids:
  metric-types: Metric types
  Summary: Summary
  Timer: Timer
  Gauge: Gauge
  DistinctCounter: Distinct counter
  ref-authentication-metrics: Authentication metrics
  ref-authorization-metrics: Authorization metrics
  ref-blacklisting-metrics: Denylisting metrics
  ref-CTS-metrics: CTS metrics
  ref-JVM-metrics: JVM metrics
  ref-oauth2-metrics: OAuth 2.0 metrics
  ref-scripting-metrics: Scripting metrics
  ref-session-metrics: Session metrics
  ref-script-cache-metrics: Script cache metrics
---

# Monitoring metrics

This section describes the monitoring metrics for common REST, JMX, or Graphite interfaces as well as the Prometheus monitoring metrics.

## Metric types

The following metric types are available.

### Summary

The summary metric samples observations, providing a count of observations, sum total of observed amounts, average rate of events, and moving average rates across sliding time windows.

* Fields

* Prometheus fields

| Field       | Description                                                                                                                       |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `_id`       | The metric ID.                                                                                                                    |
| `_type`     | The metric type.                                                                                                                  |
| `count`     | The number of events recorded for this metric.                                                                                    |
| `total`     | The sum of the values of events recorded for this metric.	As the increment is always 1, the total and the count are always equal. |
| `m1_rate`   | The one-minute average rate.                                                                                                      |
| `m5_rate`   | The five-minute average rate.                                                                                                     |
| `m15_rate`  | The fifteen-minute average rate.                                                                                                  |
| `mean_rate` | The average rate.                                                                                                                 |
| `units`     | A description of the units the metric is presented in.                                                                            |

***Example***

```json
{
  "_id" : "authentication.success",
  "_type" : "summary",
  "count" : 2,
  "total" : 2.0,
  "m1_rate" : 3.2668341885586836E-14,
  "m5_rate" : 7.794695663154025E-5,
  "m15_rate" : 0.01377545747021923,
  "mean_rate" : 8.238608027596704E-4,
  "units" : "events/second"
}
```

The Prometheus endpoints don't provide rate-based statistics because rates can be calculated from the time-series data.

| Field    | Description                                                                                                                |
| -------- | -------------------------------------------------------------------------------------------------------------------------- |
| `# TYPE` | The metric ID and type formatted as a comment.                                                                             |
| `_count` | The number of events recorded.                                                                                             |
| `_sum`   | The sum of the number of events recorded.	This metric is output as \_total for the deprecated /metrics/prometheus endpoint |

***Example***

```none
# TYPE am_authentication summary
am_authentication_count{outcome="success"} 2.0
am_authentication_sum{outcome="success"} 2.0
```

### Timer

The timer metric combines rate and duration information.

* Fields

* Prometheus fields

| Field            | Description                                                   |
| ---------------- | ------------------------------------------------------------- |
| `_id`            | The metric ID.                                                |
| `_type`          | The metric type.                                              |
| `count`          | The number of events recorded for this metric.                |
| `total`          | The sum of the durations recorded for this metric.            |
| `min`            | The minimum duration recorded for this metric.                |
| `max`            | The maximum duration recorded for this metric.                |
| `mean`           | The mean average duration recorded for this metric.           |
| `stddev`         | The standard deviation of durations recorded for this metric. |
| `duration_units` | The units used for measuring the durations in the metric.     |
| `p50`            | 50% of the durations recorded are at or below this value.     |
| `p75`            | 75% of the durations recorded are at or below this value.     |
| `p95`            | 95% of the durations recorded are at or below this value.     |
| `p98`            | 98% of the durations recorded are at or below this value.     |
| `p99`            | 99% of the durations recorded are at or below this value.     |
| `p999`           | 99.9% of the durations recorded are at or below this value.   |
| `m1_rate`        | The one-minute average rate.                                  |
| `m5_rate`        | The five-minute average rate.                                 |
| `m15_rate`       | The fifteen-minute average rate.                              |
| `mean_rate`      | The average rate.                                             |
| `rate_units`     | The units used for measuring the rate of the metric.          |

|   |                                                                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Duration-based values, such as `min`, `max`, and `p50`, are weighted towards newer data. By representing approximately the last five minutes of data, the timers make it easier to see recent changes in behavior, rather than a uniform average of recordings since the server was started. |

***Example***

```json
{
  "_id" : "cts.connection.success",
  "_type" : "timer",
  "count" : 486,
  "total" : 80.0,
  "min" : 0.0,
  "max" : 1.0,
  "mean" : 0.1905615495053855,
  "stddev" : 0.39274399467782056,
  "duration_units" : "milliseconds",
  "p50" : 0.0,
  "p75" : 0.0,
  "p95" : 1.0,
  "p98" : 1.0,
  "p99" : 1.0,
  "p999" : 1.0,
  "m1_rate" : 0.1819109974890356,
  "m5_rate" : 0.05433445522996721,
  "m15_rate" : 0.03155662103953588,
  "mean_rate" : 0.020858521722211427,
  "rate_units" : "calls/second"
}
```

The Prometheus endpoints don't provide rate-based statistics because rates can be calculated from the time-series data.

| Field                | Description                                                                                                                |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `# TYPE`             | The metric ID, and type. Formatted as a comment.	The Timer metric type is reported as a Summary type.                      |
| `_count`             | The number of events recorded.                                                                                             |
| `_sum`               | The sum of the number of events recorded.	This metric is output as \_total for the deprecated /metrics/prometheus endpoint |
| `{quantile="0.5"}`   | 50% of the durations are at or below this value.                                                                           |
| `{quantile="0.75"}`  | 75% of the durations are at or below this value.                                                                           |
| `{quantile="0.95"}`  | 95% of the durations are at or below this value.                                                                           |
| `{quantile="0.98"}`  | 98% of the durations are at or below this value.                                                                           |
| `{quantile="0.99"}`  | 99% of the durations are at or below this value.                                                                           |
| `{quantile="0.999"}` | 99.9% of the durations are at or below this value.                                                                         |

|   |                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Duration-based quantile values are weighted towards newer data. By representing approximately the last five minutes of data, the timers make it easier to see recent changes in behavior, rather than a uniform average of recordings since the server was started. |

***Example***

```none
# TYPE am_cts_connection_seconds summary
am_cts_connection_seconds{outcome="success",quantile="0.5",} 0.0
am_cts_connection_seconds{outcome="success",quantile="0.75",} 0.0
am_cts_connection_seconds{outcome="success",quantile="0.95",} 0.001
am_cts_connection_seconds{outcome="success",quantile="0.98",} 0.001
am_cts_connection_seconds{outcome="success",quantile="0.99",} 0.001
am_cts_connection_seconds{outcome="success",quantile="0.999",} 0.001
am_cts_connection_count{outcome="success",} 492.0
am_cts_connection_seconds_sum{outcome="success",} 0.081
```

### Gauge

The gauge metric is a numerical value that can increase or decrease. The value for a gauge is calculated when requested, and represents the state of the metric at that specific time.

* Fields

* Prometheus fields

| Field   | Description                      |
| ------- | -------------------------------- |
| `_id`   | The metric ID.                   |
| `_type` | The metric type.                 |
| `value` | The current value of the metric. |

***Example***

```json
{
  "_id" : "jvm.used-memory",
  "_type" : "gauge",
  "value" : 2.13385216E9
}
```

| Field         | Description                                                                  |
| ------------- | ---------------------------------------------------------------------------- |
| `# TYPE`      | The metric ID, and type. Formatted as a comment.                             |
| `{Metric ID}` | The current value. Large values may be represented in scientific E-notation. |

***Example***

```none
# TYPE am_jvm_used_memory_bytes gauge
am_jvm_used_memory_bytes 2.13385216E9
```

### Distinct counter

Metric providing an estimate of the number of *unique* values recorded.

For example, this could be used to estimate the number of unique users who have authenticated, or unique client IP addresses.

|   |                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `DistinctCounter` metric is calculated per instance of AM, and can't be aggregated across multiple instances to get a site-wide view. |

* Fields

* Prometheus fields

| Field   | Description                                                                                                            |
| ------- | ---------------------------------------------------------------------------------------------------------------------- |
| `_id`   | The metric ID.                                                                                                         |
| `_type` | The metric type. Note that the `distinctCounter` type is reported as a `gauge` type. The output formats are identical. |
| `value` | The calculated estimate of the number of unique values recorded in the metric.                                         |

***Example***

```json
{
  "_id" : "authentication.unique-uuid.success",
  "_type" : "gauge",
  "value" : 3.0
}
```

| Field         | Description                                                                                                                                            |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `# TYPE`      | The metric ID, and type. Note that the `distinctCounter` type is reported as a `gauge` type. The output formats are identical. Formatted as a comment. |
| `{Metric ID}` | The calculated estimate of the number of unique values recorded in the metric.                                                                         |

***Example***

```none
# TYPE am_authentication_unique_uuid gauge
am_authentication_unique_uuid{outcome="success"} 3.0
```

## Authentication metrics

AM exposes the following authentication-related monitoring metrics:

* Authentication metrics

* Prometheus authentication metrics

| Name                                 | Type            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------ | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `authentication.outcome`             | Summary         | Rate of successful/unsuccessful/timed-out authentication flows.The count of successful authentications is incremented when an authentication journey completes successfully. Likewise, the authentication count for failure outcomes is incremented for failed authentication journeys.For example, the authorization code flow requires a user session to exist and could redirect the user to a journey for authentication. The completion of this authentication step would then update the count.The client credentials grant, however, doesn't use a journey for authentication and, therefore, doesn't increment the count. |
| `authentication.module.outcome`      | Summary         | This metric was used only for authentication with modules and chains and is no longer documented.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `authentication.unique-uuid.success` | DistinctCounter | Count of unique identities that have successfully logged in.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

|   |                                                                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The deprecated `/metrics/prometheus` endpoint uses `_total` in metric names. The `/metrics/prometheus/0.0.4` endpoint uses `_sum` in metric names, which conforms with the latest Prometheus version. This table shows only the `/metrics/prometheus/0.0.4` endpoint metrics. |

| Name                                                             | Type    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---------------------------------------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `am_authentication_count{outcome=outcome,}`                      | Summary | Rate of successful/unsuccessful/timed-out authentication flows (count).The count of successful authentications is incremented when an authentication journey completes successfully. Likewise, the authentication count for failure outcomes is incremented for failed authentication journeys.For example, the authorization code flow requires a user session to exist and could redirect the user to a journey for authentication. The completion of this authentication step would then update the count.The client credentials grant, however, doesn't use a journey for authentication and, therefore, doesn't increment the count. |
| `am_authentication_module_count{module=module,outcome=outcome,}` | Summary | This metric was used only for authentication with modules and chains and is no longer documented.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `am_authentication_module_sum{module=module,outcome=outcome,}`   | Summary | This metric was used only for authentication with modules and chains and is no longer documented.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `am_authentication_sum{outcome=outcome,}`                        | Summary | Rate of successful/unsuccessful/timed-out authentication flows (total).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `am_authentication_unique_uuid{outcome=outcome,}`                | Gauge   | Count of unique identities which have successfully logged in.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

**Authentication metrics labels**

| Label     | Values                                |
| --------- | ------------------------------------- |
| `outcome` | * `success`

* `failure`

* `timeout` |

## Authorization metrics

AM exposes the following authorization-related monitoring metrics after a policy evaluation takes place:

* Authorization metrics

* Prometheus authorization metrics

| Name                                                                 | Type    | Description                                                                                                                |
| -------------------------------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------- |
| `authorization.policy-set.policy-set.evaluate.action.action.outcome` | Summary | Rate of policy evaluation allowed/denied actions returned under a given policy set                                         |
| `authorization.policy-set.policy-set.evaluate.advice.advice-type`    | Summary | Rate of policy evaluation advice types returned under a given policy set.                                                  |
| `authorization.policy-set.evaluate.subject-cache.size`               | Gauge   | Number of cached subject membership relationships.                                                                         |
| `authorization.policy-set.policy-set.evaluate.outcome`               | Timer   | Rate of successful/unsuccessful policy evaluation calls under a given policy set and time taken to perform this operation. |
| `authorization.policy-set.policy-set.policy.policy-operation`        | Gauge   | Number of policies created/updated/deleted under a given policy set since this AM instance started.                        |

|   |                                                                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The deprecated `/metrics/prometheus` endpoint uses `_total` in metric names. The `/metrics/prometheus/0.0.4` endpoint uses `_sum` in metric names, which conforms with the latest Prometheus version. This table shows only the `/metrics/prometheus/0.0.4` endpoint metrics. |

| Name                                                                                                           | Type    | Description                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `am_authorization_policy_set_policy_count{operation=policy-operation,policy_set=policy-set,}`                  | Summary | Number of policies created/updated/deleted under a given policy set since this AM instance was started. (Summary)                  |
| `am_authorization_policy_set_policy_sum{operation=policy-operation,policy_set=policy-set,}`                    | Summary | Number of policies created/updated/deleted under a given policy set since this AM instance was started. (Summary)                  |
| `am_authorization_policy_set_evaluate_subject_cache_size`                                                      | Summary | Number of cached subject membership relationships.                                                                                 |
| `am_authorization_policy_set_evaluate_seconds{outcome=outcome,policy_set=policy-set,quantile=quantile,}`       | Summary | Rate of successful/unsuccessful policy evaluation calls under a given policy set and time taken to perform this operation. (Timer) |
| `am_authorization_policy_set_evaluate_count{outcome=outcome,policy_set=policy-set,}`                           | Summary | Rate of successful/unsuccessful policy evaluation calls under a given policy set and time taken to perform this operation. (Timer) |
| `am_authorization_policy_set_evaluate_seconds_sum{outcome=outcome,policy_set=policy-set,}`                     | Summary | Rate of successful/unsuccessful policy evaluation calls under a given policy set and time taken to perform this operation. (Timer) |
| `am_authorization_policy_set_evaluate_action_sum{action_type=action,outcome="allow",policy_set=policy-set,}`   | Summary | Rate of policy evaluation allowed/denied actions being returned under a given policy set (total).                                  |
| `am_authorization_policy_set_evaluate_action_count{action_type=action,outcome="allow",policy_set=policy-set,}` | Summary | Rate of policy evaluation allowed/denied actions being returned under a given policy set (count).                                  |
| `am_authorization_policy_set_evaluate_advice{policy_set=policy-set,advice-type=advice-type,}`                  | Summary | Rate of policy evaluation advice types being returned under a given policy set.                                                    |
| `am_authorization_policy_set_evaluate_advice_count{policy_set=policy-set,advice-type,}`                        | Summary | Rate of policy evaluation advice types being returned under a given policy set (count).                                            |
| `am_authorization_policy_set_evaluate_advice_sum{policy_set=policy-set,advice-type=advice-type}`               | Summary | Rate of policy evaluation advice types being returned under a given policy set (total).                                            |

**Authorization metrics labels**

| Label              | Values                                                                                                                                                 |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `action`           | Name of the action as specified in the policy, for example:- `GET`

- `GRANT`

- `MODIFY`

- `DELEGATE`

- `READ`                                      |
| `advice-type`      | Name of the policy condition advice, for example:- `AuthSchemeConditionAdvice`

- `AuthenticateToServiceConditionAdvice`

- `AuthLevelConditionAdvice` |
| `outcome`          | * `success`

* `allow`                                                                                                                                 |
| `policy-operation` | Type of operation performed on the policy, for example:* `create`

* `delete`

* `update`                                                              |
| `policy-set`       | Name of the policy set, for example:* `iPlanetAMWebAgentService`

* `oauth2Scopes`                                                                     |
| `quantile`         | Refer to [Timer](#Timer) for `quantile` values.                                                                                                        |

## Denylisting metrics

AM exposes the following denylisting monitoring metrics:

* Denylisting metrics

* Prometheus denylisting metrics

| Name                                                | Type    | Description                                            |
| --------------------------------------------------- | ------- | ------------------------------------------------------ |
| `denylist type.blacklist.bloomfilter.check.outcome` | Summary | Rate of bloom filter denylist checks.                  |
| `denylist type.blacklist.cts.search.outcome`        | Timer   | Tracks time to search CTS for denylist entries         |
| `denylist type.blacklist.cts.search.result`         | Summary | Rate of denylist entries returned by searches.         |
| `denylist type.blacklist.cache.check.cache outcome` | Summary | Rate of cache hits/misses of the denylist cache layer. |
| `denylist type.blacklist.check.check outcome`       | Summary | Rate of denylist checks.                               |

|   |                                                                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The deprecated `/metrics/prometheus` endpoint uses `_total` in metric names. The `/metrics/prometheus/0.0.4` endpoint uses `_sum` in metric names, which conforms with the latest Prometheus version. This table shows only the `/metrics/prometheus/0.0.4` endpoint metrics. |

| Name                                                                                               | Type    | Description                                             |
| -------------------------------------------------------------------------------------------------- | ------- | ------------------------------------------------------- |
| `am_blacklist_cts_search_count{blacklist_type=denylist type,outcome=outcome,}`                     | Summary | Tracks time to search CTS for denylist entries (count). |
| `am_blacklist_cts_search_result_count{blacklist_type=denylist type,}`                              | Summary | Rate of denylist entries returned by searches (count).  |
| `am_blacklist_cts_search_result_sum{blacklist_type=denylist type,}`                                | Summary | Rate of denylist entries returned by searches (total).  |
| `am_blacklist_cts_search_seconds_sum{blacklist_type=denylist type,outcome=outcome,}`               | Summary | Tracks time to search CTS for denylist entries (count). |
| `am_blacklist_cts_search_seconds{blacklist_type=denylist type,outcome=outcome,quantile=quantile,}` | Summary | Tracks time to search CTS for denylist entries.         |
| am\_blacklist\_bloomfilter\_check{blacklist\_type=denylist type,outcome=outcome}                   | Summary | Rate of bloom filter denylist checks.                   |
| am\_blacklist\_cache{blacklist\_type=denylist type,outcome=cache outcome}                          | Summary | Rate of cache hits/misses of the denylist cache layer.  |
| am\_blacklist\_check{blacklist\_type=denylist type,outcome=check outcome}                          | Summary | Rate of denylist checks.                                |

**Denylisting metrics labels**

| Label           | Values                                                                  |
| --------------- | ----------------------------------------------------------------------- |
| `denylist type` | * `session_client_based`

* `oauth2`                                    |
| `outcome`       | - `success`

- `failure`                                                |
| `cache outcome` | * `hit`

* `miss`                                                       |
| `check outcome` | - `true` The token is denylisted

- `false` The token is not denylisted |
| `quantile`      | Refer to [Timer](#Timer) for `quantile` values.                         |

## CTS metrics

AM exposes the following CTS-related monitoring metrics:

* CTS metrics

* Prometheus CTS metrics

| Name                                                       | Type    | Description                                                                                        |
| ---------------------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------- |
| `cts.connection.outcome`                                   | Timer   | Rate of successful/unsuccessful CTS connections to DS and time taken to obtain the connection.     |
| `cts.connection.state.status`                              | Counter | The number of connections in each state.                                                           |
| `cts.reaper.cache.size`                                    | Gauge   | Number of entries in the token reaper cache.                                                       |
| `cts.reaper.cache.cts reaper token type.deletion.outcome`  | Summary | Rate of successful/unsuccessful token deletions from cache by token type.                          |
| `cts.reaper.search.cts reaper token type.deletion.outcome` | Summary | Rate of successful/unsuccessful token deletions from search by token type.                         |
| `cts.reaper.search.outcome`                                | Timer   | Rate of successful/unsuccessful searches and time taken to perform this operation.                 |
| `cts.task.cts reaper token type.operation.outcome`         | Summary | Rate of successful/unsuccessful CTS operation types, by token type and time taken to perform them. |

|   |                                                                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The deprecated `/metrics/prometheus` endpoint uses `_total` in metric names. The `/metrics/prometheus/0.0.4` endpoint uses `_sum` in metric names, which conforms with the latest Prometheus version. This table shows only the `/metrics/prometheus/0.0.4` endpoint metrics. |

| Name                                                                                                  | Type    | Description                                                                                                |
| ----------------------------------------------------------------------------------------------------- | ------- | ---------------------------------------------------------------------------------------------------------- |
| `am_cts_connection_count{outcome=outcome,}`                                                           | Summary | Rate of successful/unsuccessful CTS connections to DS and time taken to obtain the connection.             |
| `am_cts_connection_seconds_sum{outcome=outcome,}`                                                     | Summary | Rate of successful/unsuccessful CTS connections to DS and time taken to obtain the connection (total).     |
| `am_cts_connection_seconds{outcome=outcome,quantile=quantile,}`                                       | Summary | Rate of successful/unsuccessful CTS connections to DS and time taken to obtain the connection.             |
| `am_cts_connection_state{status=status,}`                                                             | Counter | The number of connections in each state.                                                                   |
| `am_cts_reaper_cache_size`                                                                            | Gauge   | Number of entries in the token reaper cache.                                                               |
| `am_cts_reaper_deletion_sum{outcome=outcome,reaper_type="cache",token_type=cts reaper token type,}`   | Summary | Number of token deletions from cache by token type (total).                                                |
| `am_cts_reaper_deletion_count{outcome=outcome,reaper_type="cache",token_type=cts reaper token type,}` | Summary | Number of token deletions from cache by token type (count).                                                |
| `am_cts_reaper_search_count{outcome=outcome,}`                                                        | Summary | Time taken to perform searches by CTS reaper (count).                                                      |
| `am_cts_reaper_search_seconds_sum{outcome=outcome,}`                                                  | Summary | Time taken to perform searches by CTS reaper (total).                                                      |
| `am_cts_reaper_search_seconds{outcome=outcome,quantile=quantile,}`                                    | Summary | Time taken to perform searches by CTS reaper.                                                              |
| `am_cts_task_count{operation=operation,outcome=outcome,token_type=token-type,}`                       | Summary | Rate of successful/unsuccessful CTS operation types, by token type and time taken to perform them.         |
| `am_cts_task_pending{operation=operation,}`                                                           | Counter | Tracks number of active create operations.                                                                 |
| `am_cts_task_seconds_sum{operation=operation,outcome=outcome,token_type=token-type,}`                 | Summary | Rate of successful/unsuccessful CTS operation types, by token type and time taken to perform them (total). |
| `am_cts_task_seconds{operation=operation,outcome=outcome,token_type=token-type,quantile=quantile,}`   | Summary | Rate of successful/unsuccessful CTS operation types, by token type and time taken to perform them.         |

**CTS metrics labels**

| Label                   | Values                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cts reaper token type` | * `cluster-notification`

* `session`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `operation`             | - `create`

- `delete`

- `partial-query`

- `patch`

- `query`

- `read`

- `update`

- `upsert`                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `outcome`               | * `success`

* `failure`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `quantile`              | Refer to [Timer](#Timer) for `quantile` values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `status`                | - `out`

- `pending`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `token_type`            | * `authentication-whitelist`

* `back-channel-authentication-state`

* `cluster-notification`

* `logout-user`

* `oauth2-blacklist`

* `oauth2-csrf-protection`

* `oauth2-grant-set`

* `oauth2-stateless-grant`

* `oauth2-stateless`

* `oauth2`

* `push-notification`

* `request-uri-object`

* `resource-set`

* `rest`

* `saml2`

* `session-blacklist`

* `session`

* `sts`

* `suspended-auth-session`

* `transaction`

* `uma-audit-entry`

* `uma-pending-request`

* `uma-permission-ticket`

* `uma-requesting-party`

* `unknown` |

## JVM metrics

AM exposes the JVM-related monitoring metrics covered in this section.

|   |                                                                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | These metrics may depend on the JVM version and configuration. In particular, garbage-collector-related metrics depend on the garbage collector that the server uses. The garbage-collector metric names are *unstable*, and can change even in a minor JVM release. |

The following JVM metrics are all [Gauge](#Gauge) metrics.

* JVM metrics

* Prometheus JVM metrics

| Name                                                                | Description                                                                                                                                |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `jvm.available-cpus`                                                | Number of processors available to the Java virtual machine.                                                                                |
| `jvm.class-loading.loaded`                                          | Number of classes loaded since the Java virtual machine started.                                                                           |
| `jvm.class-loading.unloaded`                                        | Number of classes unloaded since the Java virtual machine started.                                                                         |
| `jvm.free-used-memory`                                              | Amount of free memory.                                                                                                                     |
| `jvm.used-memory`                                                   | Amount of used memory.                                                                                                                     |
| `jvm.max-memory`                                                    | Maximum amount of memory.                                                                                                                  |
| `jvm.garbage-collector.Copy.count`                                  | Number of collections performed by the "copy" garbage collection algorithm.                                                                |
| `jvm.garbage-collector.Copy.time`                                   | Approximate accumulated time taken by the "copy" garbage collection algorithm.                                                             |
| `jvm.garbage-collector.MarkSweepCompact.count`                      | Number of collections performed by the "mark sweep" garbage collection algorithm.                                                          |
| `jvm.garbage-collector.MarkSweepCompact.time`                       | Approximate accumulated time taken by the "mark sweep" garbage collection algorithm.                                                       |
| `jvm.memory-usage.heap.init`                                        | Amount of heap memory the Java virtual machine initially requested from the operating system.                                              |
| `jvm.memory-usage.heap.max`                                         | Maximum amount of heap memory the Java virtual machine attempts to use.                                                                    |
| `jvm.memory-usage.heap.committed`                                   | Amount of heap memory committed for the Java virtual machine to use.                                                                       |
| `jvm.memory-usage.heap.used`                                        | Amount of heap memory used by the Java virtual machine.                                                                                    |
| `jvm.memory-usage.heap.usage`                                       | Percentage of heap memory used out of the maximum available.                                                                               |
| `jvm.memory-usage.non-heap.init`                                    | Amount of non-heap memory the Java virtual machine initially requested from the operating system.                                          |
| `jvm.memory-usage.non-heap.max`                                     | Maximum amount of non-heap memory the Java virtual machine attempts to use.                                                                |
| `jvm.memory-usage.non-heap.committed`                               | Amount of non-heap memory that is committed for the Java virtual machine to use.                                                           |
| `jvm.memory-usage.non-heap.used`                                    | Amount of non-heap memory used by the Java virtual machine.                                                                                |
| `jvm.memory-usage.non-heap.usage`                                   | Percentage of non-heap memory used out of the maximum available.                                                                           |
| `jvm.memory-usage.pools.Compressed-Class-Space.init`                | Amount of "compressed class space" memory the Java virtual machine initially requested from the operating system.                          |
| `jvm.memory-usage.pools.Compressed-Class-Space.max`                 | Maximum amount of "compressed class space" memory the Java virtual machine attempts to use.                                                |
| `jvm.memory-usage.pools.Compressed-Class-Space.committed`           | Amount of "compressed class space" memory committed for the Java virtual machine to use.                                                   |
| `jvm.memory-usage.pools.Compressed-Class-Space.used`                | Amount of "compressed class space" memory used by the Java virtual machine.                                                                |
| `jvm.memory-usage.pools.Compressed-Class-Space.usage`               | Percentage of "compressed class space" memory used out of the maximum available.                                                           |
| `jvm.memory-usage.pools.CodeHeap-'non-nmethods'.init`               | Amount of CodeHeap "non-nmethods" memory the Java virtual machine initially requested from the operating system.                           |
| `jvm.memory-usage.pools.CodeHeap-'non-nmethods'.max`                | Maximum amount of CodeHeap "non-nmethods" memory the Java virtual machine attempts to use.                                                 |
| `jvm.memory-usage.pools.CodeHeap-'non-nmethods'.committed`          | Amount of CodeHeap "non-nmethods" memory committed for the Java virtual machine to use.                                                    |
| `jvm.memory-usage.pools.CodeHeap-'non-nmethods'.used`               | Amount of CodeHeap "non-nmethods" memory used by the Java virtual machine.                                                                 |
| `jvm.memory-usage.pools.CodeHeap-'non-nmethods'.usage`              | Percentage of CodeHeap "non-nmethods" memory used out of the maximum available.                                                            |
| `jvm.memory-usage.pools.CodeHeap-'non-profiled-nmethods'.init`      | Amount of CodeHeap "non-profiled-nmethods" memory the Java virtual machine initially requested from the operating system.                  |
| `jvm.memory-usage.pools.CodeHeap-'non-profiled-nmethods'.max`       | Maximum amount of CodeHeap "non-profiled-nmethods" memory the Java virtual machine attempts to use.                                        |
| `jvm.memory-usage.pools.CodeHeap-'non-profiled-nmethods'.committed` | Amount of CodeHeap "non-profiled-nmethods" memory committed for the Java virtual machine to use.                                           |
| `jvm.memory-usage.pools.CodeHeap-'non-profiled-nmethods'.used`      | Amount of CodeHeap "non-profiled-nmethods" memory used by the Java virtual machine.                                                        |
| `jvm.memory-usage.pools.CodeHeap-'non-profiled-nmethods'.usage`     | Percentage of CodeHeap "non-profiled-nmethods" memory used out of the maximum available.                                                   |
| `jvm.memory-usage.pools.CodeHeap-'profiled-nmethods'.init`          | Amount of CodeHeap "profiled-nmethods" memory the Java virtual machine initially requested from the operating system.                      |
| `jvm.memory-usage.pools.CodeHeap-'profiled-nmethods'.max`           | Maximum amount of CodeHeap "profiled-nmethods" memory the Java virtual machine attempts to use.                                            |
| `jvm.memory-usage.pools.CodeHeap-'profiled-nmethods'.committed`     | Amount of CodeHeap "profiled-nmethods" memory committed for the Java virtual machine to use.                                               |
| `jvm.memory-usage.pools.CodeHeap-'profiled-nmethods'.used`          | Amount of CodeHeap "profiled-nmethods" memory used by the Java virtual machine.                                                            |
| `jvm.memory-usage.pools.CodeHeap-'profiled-nmethods'.usage`         | Percentage of CodeHeap "profiled-nmethods" memory used out of the maximum available.                                                       |
| `jvm.memory-usage.pools.Metaspace.init`                             | Amount of "metaspace" memory the Java virtual machine initially requested from the operating system.                                       |
| `jvm.memory-usage.pools.Metaspace.max`                              | Maximum amount of "metaspace" memory the Java virtual machine attempts to use.                                                             |
| `jvm.memory-usage.pools.Metaspace.committed`                        | Amount of "metaspace" memory committed for the Java virtual machine to use.                                                                |
| `jvm.memory-usage.pools.Metaspace.used`                             | Amount of "metaspace" memory used by the Java virtual machine.                                                                             |
| `jvm.memory-usage.pools.Metaspace.usage`                            | Percentage of "metaspace" memory used out of the maximum available.                                                                        |
| `jvm.memory-usage.pools.Eden-Space.init`                            | Amount of "eden space" memory the Java virtual machine initially requested from the operating system.                                      |
| `jvm.memory-usage.pools.Eden-Space.max`                             | Maximum amount of "eden space" memory (young generation) the Java virtual machine attempts to use.                                         |
| `jvm.memory-usage.pools.Eden-Space.committed`                       | Amount of "eden space" memory (young generation) committed for the Java virtual machine to use.                                            |
| `jvm.memory-usage.pools.Eden-Space.used-after-gc`                   | Amount of "eden space" memory (young generation) after the last time garbage collection recycled unused objects in this memory pool.       |
| `jvm.memory-usage.pools.Eden-Space.used`                            | Amount of "eden space" memory (young generation) used by the Java virtual machine.                                                         |
| `jvm.memory-usage.pools.Eden-Space.usage`                           | Percentage of "eden space" memory (young generation) used out of the maximum available.                                                    |
| `jvm.memory-usage.pools.Tenured-Gen.init`                           | Amount of "tenured generation" (old generation) memory the Java virtual machine initially requested from the operating system.             |
| `jvm.memory-usage.pools.Tenured-Gen.max`                            | Maximum amount of "tenured generation" (old generation) memory the Java virtual machine attempts to use.                                   |
| `jvm.memory-usage.pools.Tenured-Gen.committed`                      | Amount of "tenured generation" memory (old generation) committed for the Java virtual machine to use.                                      |
| `jvm.memory-usage.pools.Tenured-Gen.used-after-gc`                  | Amount of "tenured generation" memory (old generation) after the last time garbage collection recycled unused objects in this memory pool. |
| `jvm.memory-usage.pools.Tenured-Gen.used`                           | Amount of "tenured generation" memory (old generation) used by the Java virtual machine.                                                   |
| `jvm.memory-usage.pools.Tenured-Gen.usage`                          | Percentage of "tenured generation" memory (old generation) used out of the maximum available.                                              |
| `jvm.memory-usage.pools.Survivor-Space.init`                        | Amount of "survivor space" memory (young generation) the Java virtual machine initially requested from the operating system.               |
| `jvm.memory-usage.pools.Survivor-Space.max`                         | Maximum amount of "survivor space" memory (young generation) the Java virtual machine attempts to use.                                     |
| `jvm.memory-usage.pools.Survivor-Space.committed`                   | Amount of "survivor space" memory (young generation) committed for the Java virtual machine to use.                                        |
| `jvm.memory-usage.pools.Survivor-Space.used-after-gc`               | Amount of "survivor space" memory (young generation) after the last time garbage collection recycled unused objects in this memory pool.   |
| `jvm.memory-usage.pools.Survivor-Space.used`                        | Amount of "survivor space" memory (young generation) used by the Java virtual machine.                                                     |
| `jvm.memory-usage.pools.Survivor-Space.usage`                       | Percentage of "survivor space" memory (young generation) used out of the maximum available.                                                |
| `jvm.memory-usage.total.committed`                                  | Amount of memory committed for the Java virtual machine to use.                                                                            |
| `jvm.memory-usage.total.init`                                       | Amount of memory the Java virtual machine initially requested from the operating system.                                                   |
| `jvm.memory-usage.total.max`                                        | Maximum amount of memory the Java virtual machine attempts to use.                                                                         |
| `jvm.memory-usage.total.used`                                       | Amount of memory used by the Java virtual machine.                                                                                         |
| `jvm.thread-state.blocked.count`                                    | Number of threads in the BLOCKED state.                                                                                                    |
| `jvm.thread-state.count`                                            | Number of live threads including both daemon and non-daemon threads.                                                                       |
| `jvm.thread-state.daemon.count`                                     | Number of live daemon threads.                                                                                                             |
| `jvm.thread-state.new.count`                                        | Number of threads in the NEW state.                                                                                                        |
| `jvm.thread-state.runnable.count`                                   | Number of threads in the RUNNABLE state.                                                                                                   |
| `jvm.thread-state.terminated.count`                                 | Number of threads in the TERMINATED state.                                                                                                 |
| `jvm.thread-state.timed_waiting.count`                              | Number of threads in the TIMED\_WAITING state.                                                                                             |
| `jvm.thread-state.waiting.count`                                    | Number of threads in the WAITING state.                                                                                                    |

| Name                                                                    | Description                                                                                                                                |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `am_jvm_available_cpus`                                                 | Number of processors available to the Java virtual machine.                                                                                |
| `am_jvm_class_loading_loaded`                                           | Number of classes loaded since the Java virtual machine started.                                                                           |
| `am_jvm_class_loading_unloaded`                                         | Number of classes unloaded since the Java virtual machine started.                                                                         |
| `am_jvm_free_used_memory_bytes`                                         | Amount of free memory.                                                                                                                     |
| `am_jvm_used_memory_bytes`                                              | Amount of used memory.                                                                                                                     |
| `am_jvm_max_memory_bytes`                                               | Maximum amount of memory.                                                                                                                  |
| `am_jvm_garbage_collector_copy_count`                                   | Number of collections performed by the "copy" garbage collection algorithm.                                                                |
| `am_jvm_garbage_collector_copy_time`                                    | Approximate accumulated time taken by the "copy" garbage collection algorithm.                                                             |
| `am_jvm_garbage_collector_markSweepCompact_count`                       | Number of collections performed by the "mark sweep" garbage collection algorithm.                                                          |
| `am_jvm_garbage_collector_markSweepCompact_time`                        | Approximate accumulated time taken by the "mark sweep" garbage collection algorithm.                                                       |
| `am_jvm_memory_usage_heap_init`                                         | Amount of heap memory the Java virtual machine initially requested from the operating system.                                              |
| `am_jvm_memory_usage_heap_max`                                          | Maximum amount of heap memory the Java virtual machine attempts to use.                                                                    |
| `am_jvm_memory_usage_heap_committed`                                    | Amount of heap memory committed for the Java virtual machine to use.                                                                       |
| `am_jvm_memory_usage_heap_used`                                         | Amount of heap memory used by the Java virtual machine.                                                                                    |
| `am_jvm_memory_usage_heap_usage`                                        | Percentage of heap memory used out of the maximum available.                                                                               |
| `am_jvm_memory_usage_non_heap_init`                                     | Amount of non\_heap memory the Java virtual machine initially requested from the operating system.                                         |
| `am_jvm_memory_usage_non_heap_max`                                      | Maximum amount of non\_heap memory the Java virtual machine attempts to use.                                                               |
| `am_jvm_memory_usage_non_heap_committed`                                | Amount of non\_heap memory that is committed for the Java virtual machine to use.                                                          |
| `am_jvm_memory_usage_non_heap_used`                                     | Amount of non\_heap memory used by the Java virtual machine.                                                                               |
| `am_jvm_memory_usage_non_heap_usage`                                    | Percentage of non\_heap memory used out of the maximum available.                                                                          |
| `am_jvm_memory_usage_pools_compressed_Class_Space_init`                 | Amount of "compressed class space" memory the Java virtual machine initially requested from the operating system.                          |
| `am_jvm_memory_usage_pools_compressed_Class_Space_max`                  | Maximum amount of "compressed class space" memory the Java virtual machine attempts to use.                                                |
| `am_jvm_memory_usage_pools_compressed_Class_Space_committed`            | Amount of "compressed class space" memory committed for the Java virtual machine to use.                                                   |
| `am_jvm_memory_usage_pools_compressed_Class_Space_used`                 | Amount of "compressed class space" memory used by the Java virtual machine.                                                                |
| `am_jvm_memory_usage_pools_compressed_Class_Space_usage`                | Percentage of "compressed class space" memory used out of the maximum available.                                                           |
| `am_jvm_memory_usage_pools_codeheapnon_nmethodsinit`                    | Amount of CodeHeap "non\_nmethods" memory the Java virtual machine initially requested from the operating system.                          |
| `am_jvm_memory_usage_pools_codeheap__non_nmethods\__max`                | Maximum amount of CodeHeap "non\_nmethods" memory the Java virtual machine attempts to use.                                                |
| `am_jvm_memory_usage_pools_codeheap__non_nmethods__committed`           | Amount of CodeHeap "non\_nmethods" memory committed for the Java virtual machine to use.                                                   |
| `am_jvm_memory_usage_pools_codeheap__non_nmethods\__used`               | Amount of CodeHeap "non\_nmethods" memory used by the Java virtual machine.                                                                |
| `am_jvm_memory_usage_pools_codeheap__non_nmethods\__usage`              | Percentage of CodeHeap "non\_nmethods" memory used out of the maximum available.                                                           |
| `am_jvm_memory_usage_pools_codeheap__non_profiled_nmethods\__init`      | Amount of CodeHeap "non\_profiled\_nmethods" memory the Java virtual machine initially requested from the operating system.                |
| `am_jvm_memory_usage_pools_codeheap__non_profiled_nmethods\__max`       | Maximum amount of CodeHeap "non\_profiled\_nmethods" memory the Java virtual machine attempts to use.                                      |
| `am_jvm_memory_usage_pools_codeheap__non_profiled_nmethods\__committed` | Amount of CodeHeap "non\_profiled\_nmethods" memory committed for the Java virtual machine to use.                                         |
| `am_jvm_memory_usage_pools_codeheap__non_profiled_nmethods\__used`      | Amount of CodeHeap "non\_profiled\_nmethods" memory used by the Java virtual machine.                                                      |
| `am_jvm_memory_usage_pools_codeheap__non_profiled_nmethods\__usage`     | Percentage of CodeHeap "non\_profiled\_nmethods" memory used out of the maximum available.                                                 |
| `am_jvm_memory_usage_pools_codeheap__profiled_nmethods\__init`          | Amount of CodeHeap "profiled\_nmethods" memory the Java virtual machine initially requested from the operating system.                     |
| `am_jvm_memory_usage_pools_codeheap__profiled_nmethods\__max`           | Maximum amount of CodeHeap "profiled\_nmethods" memory the Java virtual machine attempts to use.                                           |
| `am_jvm_memory_usage_pools_codeheap__profiled_nmethods\__committed`     | Amount of CodeHeap "profiled\_nmethods" memory committed for the Java virtual machine to use.                                              |
| `am_jvm_memory_usage_pools_codeheap__profiled_nmethods\__used`          | Amount of CodeHeap "profiled\_nmethods" memory used by the Java virtual machine.                                                           |
| `am_jvm_memory_usage_pools_codeheap__profiled_nmethods\__usage`         | Percentage of CodeHeap "profiled\_nmethods" memory used out of the maximum available.                                                      |
| `am_jvm_memory_usage_pools_metaspace_init`                              | Amount of "metaspace" memory the Java virtual machine initially requested from the operating system.                                       |
| `am_jvm_memory_usage_pools_metaspace_max`                               | Maximum amount of "metaspace" memory the Java virtual machine attempts to use.                                                             |
| `am_jvm_memory_usage_pools_metaspace_committed`                         | Amount of "metaspace" memory committed for the Java virtual machine to use.                                                                |
| `am_jvm_memory_usage_pools_metaspace_used`                              | Amount of "metaspace" memory used by the Java virtual machine.                                                                             |
| `am_jvm_memory_usage_pools_metaspace_usage`                             | Percentage of "metaspace" memory used out of the maximum available.                                                                        |
| `am_jvm_memory_usage_pools.Eden_Space_init`                             | Amount of "eden space" memory the Java virtual machine initially requested from the operating system.                                      |
| `am_jvm_memory_usage_pools.Eden_Space_max`                              | Maximum amount of "eden space" memory (young generation) the Java virtual machine attempts to use.                                         |
| `am_jvm_memory_usage_pools.Eden_Space_committed`                        | Amount of "eden space" memory (young generation) committed for the Java virtual machine to use.                                            |
| `am_jvm_memory_usage_pools.Eden_Space_used_after_gc`                    | Amount of "eden space" memory (young generation) after the last time garbage collection recycled unused objects in this memory pool.       |
| `am_jvm_memory_usage_pools.Eden_Space_used`                             | Amount of "eden space" memory (young generation) used by the Java virtual machine.                                                         |
| `am_jvm_memory_usage_pools.Eden_Space_usage`                            | Percentage of "eden space" memory (young generation) used out of the maximum available.                                                    |
| `am_jvm_memory_usage_pools_tenured_Gen_init`                            | Amount of "tenured generation" (old generation) memory the Java virtual machine initially requested from the operating system.             |
| `am_jvm_memory_usage_pools_tenured_Gen_max`                             | Maximum amount of "tenured generation" (old generation) memory the Java virtual machine attempts to use.                                   |
| `am_jvm_memory_usage_pools_tenured_Gen_committed`                       | Amount of "tenured generation" memory (old generation) committed for the Java virtual machine to use.                                      |
| `am_jvm_memory_usage_pools_tenured_Gen_used_after_gc`                   | Amount of "tenured generation" memory (old generation) after the last time garbage collection recycled unused objects in this memory pool. |
| `am_jvm_memory_usage_pools_tenured_Gen_used`                            | Amount of "tenured generation" memory (old generation) used by the Java virtual machine.                                                   |
| `am_jvm_memory_usage_pools_tenured_Gen_usage`                           | Percentage of "tenured generation" memory (old generation) used out of the maximum available.                                              |
| `am_jvm_memory_usage_pools.Survivor_Space_init`                         | Amount of "survivor space" memory (young generation) the Java virtual machine initially requested from the operating system.               |
| `am_jvm_memory_usage_pools.Survivor_Space_max`                          | Maximum amount of "survivor space" memory (young generation) the Java virtual machine attempts to use.                                     |
| `am_jvm_memory_usage_pools.Survivor_Space_committed`                    | Amount of "survivor space" memory (young generation) committed for the Java virtual machine to use.                                        |
| `am_jvm_memory_usage_pools.Survivor_Space_used_after_gc`                | Amount of "survivor space" memory (young generation) after the last time garbage collection recycled unused objects in this memory pool.   |
| `am_jvm_memory_usage_pools.Survivor_Space_used`                         | Amount of "survivor space" memory (young generation) used by the Java virtual machine.                                                     |
| `am_jvm_memory_usage_pools.Survivor_Space_usage`                        | Percentage of "survivor space" memory (young generation) used out of the maximum available.                                                |
| `am_jvm_memory_usage_total_committed`                                   | Amount of memory committed for the Java virtual machine to use.                                                                            |
| `am_jvm_memory_usage_total_init`                                        | Amount of memory the Java virtual machine initially requested from the operating system.                                                   |
| `am_jvm_memory_usage_total_max`                                         | Maximum amount of memory the Java virtual machine attempts to use.                                                                         |
| `am_jvm_memory_usage_total_used`                                        | Amount of memory used by the Java virtual machine.                                                                                         |
| `am_jvm_thread_state_blocked_count`                                     | Number of threads in the BLOCKED state.                                                                                                    |
| `am_jvm_thread_state_count`                                             | Number of live threads including both daemon and non\_daemon threads.                                                                      |
| `am_jvm_thread_state_daemon_count`                                      | Number of live daemon threads.                                                                                                             |
| `am_jvm_thread_state_new_count`                                         | Number of threads in the NEW state.                                                                                                        |
| `am_jvm_thread_state_runnable_count`                                    | Number of threads in the RUNNABLE state.                                                                                                   |
| `am_jvm_thread_state_terminated_count`                                  | Number of threads in the TERMINATED state.                                                                                                 |
| `am_jvm_thread_state_timed_waiting_count`                               | Number of threads in the TIMED\_WAITING state.                                                                                             |
| `am_jvm_thread_state_waiting_count`                                     | Number of threads in the WAITING state.                                                                                                    |

## OAuth 2.0 metrics

AM exposes the following OAuth 2.0 monitoring metrics:

* OAuth 2.0 metrics

* Prometheus OAuth 2.0 metrics

| Name                               | Type    | Description                                                                  |
| ---------------------------------- | ------- | ---------------------------------------------------------------------------- |
| `oauth2.grant.grant-type`          | Summary | Rate of OAuth 2.0 grant completion by grant type.                            |
| `oauth2.grant.revoke`              | Summary | Rate of OAuth 2.0 grant revocation                                           |
| `oauth2.token.token-type.issue`    | Summary | Rate of OAuth 2.0 token issuance by token type.                              |
| `oauth2.token.access-token.revoke` | Summary | Rate of OAuth 2.0 access token revocation.                                   |
| `oauth2.token.read-as-jwt.outcome` | Timer   | Rate of successfully/unsuccessfully reading OAuth 2.0 JSON Web Tokens (JWT). |

|   |                                                                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The deprecated `/metrics/prometheus` endpoint uses `_total` in metric names. The `/metrics/prometheus/0.0.4` endpoint uses `_sum` in metric names, which conforms with the latest Prometheus version. This table shows only the `/metrics/prometheus/0.0.4` endpoint metrics. |

| Name                                                                      | Type    | Description                                                                          |
| ------------------------------------------------------------------------- | ------- | ------------------------------------------------------------------------------------ |
| `am_oauth2_grant_count{grant_type=grant-type,}`                           | Summary | Rate of OAuth 2.0 grant completion by grant type (count).                            |
| `am_oauth2_grant_revoke_count{grant_type="unknown",}`                     | Summary | Rate of OAuth 2.0 grant revocation for unknown grant types (count).                  |
| `am_oauth2_grant_revoke_sum{grant_type="unknown",}`                       | Summary | Rate of OAuth 2.0 grant revocation for unknown grant types (total).                  |
| `am_oauth2_grant_sum{grant_type=grant-type,}`                             | Summary | Rate of OAuth 2.0 grant completion by grant type (total).                            |
| `am_oauth2_token_issue_count{token_type=token-type,}`                     | Summary | Rate of OAuth 2.0 token issuance by token type (count).                              |
| `am_oauth2_token_issue_sum{token_type=token-type,}`                       | Summary | Rate of OAuth 2.0 token issuance by token type (total).                              |
| `am_oauth2_token_read_as_jwt_count{outcome=outcome,}`                     | Summary | Rate of successfully/unsuccessfully reading OAuth 2.0 JSON Web Tokens (JWT) (count). |
| `am_oauth2_token_read_as_jwt_seconds_sum{outcome=outcome,}`               | Summary | Rate of successfully/unsuccessfully reading OAuth 2.0 JSON Web Tokens (JWT) (total). |
| `am_oauth2_token_read_as_jwt_seconds{outcome=outcome,quantile=quantile,}` | Summary | Rate of successfully/unsuccessfully reading OAuth 2.0 JSON Web Tokens (JWT).         |
| `am_oauth2_token_revoke_count{token_type="access-token",}`                | Summary | Rate of OAuth 2.0 access token revocation (count)                                    |
| `am_oauth2_token_revoke_sum{token_type="access-token",}`                  | Summary | Rate of OAuth 2.0 access token revocation (total)                                    |

**OAuth 2.0 metrics labels**

| Label        | Values                                                                                                                                                                                             |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `grant-type` | * `authorization-code`

* `back-channel`

* `client-credentials`

* `device-code`

* `implicit`

* `jwt-bearer`

* `refresh`

* `resource-owner-password`

* `saml2`

* `token-exchange`

* `uma2` |
| `outcome`    | - `success`

- `failure`                                                                                                                                                                           |
| `token-type` | * `access-token`

* `authorization-code`

* `device-code`

* `id-token`

* `ops`

* `permission-ticket`

* `refresh-token`                                                                         |

## Scripting metrics

AM exposes the following metrics for monitoring the scripting threadpool:

* Scripting metrics

* Prometheus scripting metrics

| Name                                                      | Type    | Description                                                                                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `scripting.threadpool.max.threads.count.script-context`   | Gauge   | The maximum number of threads in the pool.                                                                                                                                                                                                                                                                                                                                  |
| `scripting.threadpool.min.threads.count.script-context`   | Gauge   | The minimum number of threads in the pool.                                                                                                                                                                                                                                                                                                                                  |
| `scripting.threadpool.max.queue.size.script-context`      | Gauge   | The maximum number of script executions that can be queued before the pool starts rejecting them.                                                                                                                                                                                                                                                                           |
| `scripting.threadpool.rejected.count.script-context`      | Counter | The number of script executions that have been rejected by the pool.                                                                                                                                                                                                                                                                                                        |
| `scripting.threadpool.threads.count.state.script-context` | Gauge   | The number of threads for each of the following [`states`](#state):* `active`

  Threads that are actively executing scripts in the thread pool.

  This count indicates the current usage of the thread pool.

* `blocked`

  Threads that are blocked from the thread pool and are currently waiting to execute.

  This count indicates the scripting engine queue size. |

| Name                                                                         | Type    | Description                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------------------------------------------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `am_scripting_threadpool_max_threads_count{context=script-context,}`         | Gauge   | The maximum number of threads in the pool.                                                                                                                                                                                                                                                                                                                                  |
| `am_scripting_threadpool_min_threads_count{context=script-context,}`         | Gauge   | The minimum number of threads in the pool.                                                                                                                                                                                                                                                                                                                                  |
| `am_scripting_threadpool_max_queue_size{context=script-context,}`            | Gauge   | The maximum number of script executions that can be queued before the pool starts rejecting them.                                                                                                                                                                                                                                                                           |
| `am_scripting_threadpool_rejected_count{context=script-context,}`            | Counter | The number of script executions that have been rejected by the pool.                                                                                                                                                                                                                                                                                                        |
| `am_scripting_threadpool_threads_count{context=script-context,state=state,}` | Gauge   | The number of threads for each of the following [`states`](#state):- `active`

  Threads that are actively executing scripts in the thread pool.

  This count indicates the current usage of the thread pool.

- `blocked`

  Threads that are blocked from the thread pool and are currently waiting to execute.

  This count indicates the scripting engine queue size. |

**Scripting 2.0 metrics labels**

| Label            | Values                                                                                                                                              |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `script-context` | A [supported script context](../am-scripting/manage-scripts-rest.html) value; for example, `AUTHENTICATION_TREE_DECISION_NODE` or `OAUTH2_MAY_ACT`. |
| []()`state`      | * `active`

* `blocked`                                                                                                                             |

## Session metrics

AM exposes the following session-related monitoring metrics:

* Session metrics

* Prometheus session metrics

| Name                                             | Type    | Description                                                                                                               |
| ------------------------------------------------ | ------- | ------------------------------------------------------------------------------------------------------------------------- |
| `session.session-type.session-operation.outcome` | Timer   | Rate of successful/unsuccessful outcomes for this particular operation type and the time taken to perform this operation. |
| `session.session-type.lifetime`                  | Timer   | Rate of session lifetimes.                                                                                                |
| `session.authentication-in-memory.store.size`    | Gauge   | Number of journey sessions stored in the in-memory authentication session store.                                          |
| `session.cts-based.cache.eviction`               | Summary | Rate of evictions from the session cache. (Summary)                                                                       |
| `session.cts-based.cache.session-outcome`        | Summary | Rate of cache hits/misses for the session cache.                                                                          |
| `session.cts-based.cache.size`                   | Gauge   | Number of sessions in the session cache.                                                                                  |

|   |                                                                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The deprecated `/metrics/prometheus` endpoint uses `_total` in metric names. The `/metrics/prometheus/0.0.4` endpoint uses `_sum` in metric names, which conforms with the latest Prometheus version. This table shows only the `/metrics/prometheus/0.0.4` endpoint metrics. |

| Name                                                                                                           | Type    | Description                                                                                                     |
| -------------------------------------------------------------------------------------------------------------- | ------- | --------------------------------------------------------------------------------------------------------------- |
| `am_session_count{operation=session-operation,outcome=session-outcome,session_type=session-type,}`             | Summary | Rate of successful/unsuccessful sessions for idle/max timeout and time taken to perform this operation (count). |
| `am_session_cts_based_cache_count{outcome=session-outcome,}`                                                   | Summary | Number of cache hits/misses in the session cache (count).                                                       |
| `am_session_cts_based_cache_eviction_count`                                                                    | Summary | Rate of evictions from the session cache.                                                                       |
| `am_session_cts_based_cache_eviction_sum`                                                                      | Summary | Rate of evictions from the session cache (total).                                                               |
| `am_session_cts_based_cache_size`                                                                              | Gauge   | Number of sessions in the session cache.                                                                        |
| `am_session_cts_based_cache_sum{outcome=session-outcome,}`                                                     | Summary | Number of cache hits/misses in the session cache (total).                                                       |
| `am_session_lifetime_count{session_type=session-type,}`                                                        | Summary | Rate of session lifetimes (count).                                                                              |
| `am_session_lifetime_seconds_sum{session_type=session-type,}`                                                  | Summary | Lifetime of session, by session type (total).                                                                   |
| `am_session_lifetime_seconds{session_type=session-type,quantile=quantile,}`                                    | Summary | Lifetime of session, by session type.                                                                           |
| `am_session_seconds_sum{operation=session-operation,outcome=outcome,session_type=session-type,}`               | Summary | Rate of OAuth 2.0 grant completion by grant type (count).                                                       |
| `am_session_seconds{operation=session-operation,outcome=outcome,session_type=session-type,quantile=quantile,}` | Summary | Tracks service time for successful/unsuccessful sessions by operation and session type.                         |
| `am_session_store_size{session_type="authentication-in-memory",}`                                              | Gauge   | Number of journey sessions stored in the in-memory authentication session store.                                |
| `am_session_sum{operation=session-operation,session_type=session-type,}`                                       | Summary | Rate of successful/unsuccessful sessions for idle/max timeout and time taken to perform this operation (total). |

**Session 2.0 metrics labels**

| Label                    | Values                                                                                                                                                                                                                                                                                                                               |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `operation`              | * `check-exists`

* `create`

* `dereference-restricted-token-id`

* `destroy`

* `get-matching-sessions`

* `get-restricted-token-id`

* `get-valid-sessions`

* `is-applicable`

* `logout`

* `refresh`

* `register-listener`

* `register-pll-listener`

* `resolve`

* `set-external-property`

* `set-property`

* `validate` |
| `outcome`                | - `success`

- `failure`                                                                                                                                                                                                                                                                                                             |
| `` `session-operation `` | * `idle-timeout`

* `max-timeout`                                                                                                                                                                                                                                                                                                    |
| `session-outcome`        | - `hit`

- `miss`                                                                                                                                                                                                                                                                                                                    |
| `session-type`           | * `authentication-client-based`

* `authentication-cts-based`

* `authentication-in-memory`

* `client-based`

* `cts-based`                                                                                                                                                                                                         |

## Script cache metrics

AM exposes the following metrics for monitoring [script caches](../am-scripting/cache-manager.html):

* Script cache metrics

* Prometheus script cache metrics

| Name                          | Type  | Description                                                                                                     |
| ----------------------------- | ----- | --------------------------------------------------------------------------------------------------------------- |
| `script.cache.eviction`       | Gauge | Returns the number of times an entry has been evicted. This count doesn't include manual invalidations.         |
| `script.cache.hit`            | Gauge | The number of times cache lookup methods have returned a cached value.                                          |
| `script.cache.invalidate`     | Gauge | The number of times the `invalidate` method has been called on the cache to invalidate a key manually.          |
| `script.cache.invalidate.all` | Gauge | The number of times the `invalidateAll` method has been called on the cache to invalidate all entries manually. |
| `script.cache.load.failure`   | Gauge | The number of times cache lookup methods threw an exception while loading a new value.                          |
| `script.cache.load.time`      | Gauge | The total number of seconds the cache has spent loading new values.                                             |
| `script.cache.load.count`     | Gauge | The total number of times that cache lookup methods attempted to load new values.                               |
| `script.cache.memory.bytes`   | Gauge | The estimated memory size of the cache in bytes.                                                                |
| `script.cache.miss`           | Gauge | The number of times cache lookup methods have returned an uncached (newly loaded) value, or null.               |
| `script.cache.size`           | Gauge | The approximate number of entries in the cache.                                                                 |

|   |                                                                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The deprecated `/metrics/prometheus` endpoint uses `_total` in metric names. The `/metrics/prometheus/0.0.4` endpoint uses `_sum` in metric names, which conforms with the latest Prometheus version. This table shows only the `/metrics/prometheus/0.0.4` endpoint metrics. |

| Name                                | Type  | Description                                                                                                     |
| ----------------------------------- | ----- | --------------------------------------------------------------------------------------------------------------- |
| `am_script_cache_eviction`          | Gauge | Returns the number of times an entry has been evicted. This count doesn't include manual invalidations.         |
| `am_script_cache_hit`               | Gauge | The number of times cache lookup methods have returned a cached value.                                          |
| `am_script_cache_invalidate`        | Gauge | The number of times the `invalidate` method has been called on the cache to invalidate a key manually.          |
| `am_script_cache_invalidate_all`    | Gauge | The number of times the `invalidateAll` method has been called on the cache to invalidate all entries manually. |
| `am_script_cache_load_failure`      | Gauge | The number of times Cache lookup methods threw an exception while loading a new value.                          |
| `am_script_cache_load_time_seconds` | Gauge | The total number of seconds the cache has spent loading new values.                                             |
| `am_script_cache_load_count`        | Gauge | The total number of times that Cache lookup methods attempted to load new values.                               |
| `am_script_cache_memory_bytes`      | Gauge | The estimated memory size of the cache in bytes.                                                                |
| `am_script_cache_miss`              | Gauge | The number of times cache lookup methods have returned an uncached (newly loaded) value, or null.               |
| `am_script_cache_size`              | Gauge | The approximate number of entries in the cache.                                                                 |

---

---
title: Monitoring reference
description: Reference information for monitoring PingAM instances, including service configuration and metrics
component: pingam
version: 8.1
page_id: pingam:monitoring:monitoring-reference
canonical_url: https://docs.pingidentity.com/pingam/8.1/monitoring/monitoring-reference.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Monitoring"]
page_aliases: ["maintenance-guide:monitoring-reference.adoc", "monitoring-guide:monitoring-reference.adoc"]
---

# Monitoring reference

The following links provide reference information about monitoring an AM instance:

* [Monitoring service configuration](../setup/services-configuration.html#global-monitoring-configuration)

* [Monitoring metrics](monitoring-metrics.html)

---

---
title: Trace incoming and outgoing requests
description: Monitor request flow through PingAM using distributed tracing with OpenTelemetry to identify bottlenecks, errors, and optimize application performance
component: pingam
version: 8.1
page_id: pingam:monitoring:trace-requests
canonical_url: https://docs.pingidentity.com/pingam/8.1/monitoring/trace-requests.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Distributed Tracing"]
page_aliases: ["maintenance-guide:distributed-tracing.adoc", "monitoring-guide:trace-requests.adoc"]
section_ids:
  which_requests_are_traced: Which requests are traced?
  understand_a_trace_object: Understand a trace object
  enable_and_disable_distributed_tracing: Enable and disable distributed tracing
  enable-tracing: Enable distributed tracing
  disable-tracing: Disable distributed tracing
  configure-distributed-tracing: Configure distributed tracing
  secure-trace-exports: Secure trace exports
  visualize_traces_with_jaeger: Visualize traces with Jaeger
  example_visualization_with_jaeger: Example visualization with Jaeger
  correlate_traces_with_audits: Correlate traces with audits
---

# Trace incoming and outgoing requests

When a user interacts with Ping Advanced Identity Software, the request can travel through multiple services before it completes. *Distributed tracing* lets you monitor the request flow through Ping Advanced Identity Software.

Tracing provides a single view of a request's journey and makes it easier to locate bottlenecks and errors. If issues arise, tracing makes it easier to identify the service causing the problem. It's more efficient and effective than sifting through isolated logs.

By identifying slow services, tracing helps you optimize application performance and reduce debugging time. This improves the end user experience as users are less likely to encounter errors or slow loading times.

AM supports the [OpenTelemetry framework](https://opentelemetry.io/docs/what-is-opentelemetry/) (OTEL) for collecting distributed tracing data.

|   |                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The interface stability for OpenTelemetry support is *Evolving*.The plugin configuration, the content of spans, the span name, and the span attributes are all subject to change without prior notice. |

## Which requests are traced?

AM supports distributed tracing for the following request types:

* Incoming HTTP requests

* Outgoing HTTP requests to PingIDM (Ping Advanced Identity Software deployments only)

* Outgoing LDAP requests

  These requests are searchable and identifiable for the following LDAP operations:

  * ADD

  * MODIFY

  * SEARCH

  * DELETE

  * BIND

* Outgoing scripting HTTP requests

## Understand a trace object

This section provides a brief overview of an OTEL trace object. Learn more about trace objects in [Traces](https://opentelemetry.io/docs/concepts/signals/traces/).

A *trace* represents the path of a request through an application. A trace is made up of one or more *spans*.

Each span includes the following elements:

* `traceId` representing the trace that the span is part of

* `spanId` a unique ID for that span

* `parentSpanId` the ID of the originating request

The *root span* indicates the start and end of an entire operation. The `parentSpanId` of the root span is `null` because the root span isn't part of an existing trace.

Subsequent spans in the trace have their own unique `spanId`. Their `traceId` is the same as that of the root span. Their `parentId` matches the `spanId` of the root span.

> **Collapse: Example trace object**
>
> ```json
> {
>   "spans":[
>     {
>       "traceId":"8c3ebde938a6cf04f5bb34dd03135d45",
>       "spanId":"335776e2b57ee9cf",
>       "parentSpanId":"4065c5580cf47c7",
>       "name":"HTTP POST /am/json/alpha/authenticate",
>       "kind":1,
>       "startTimeUnixNano":"1718811677526761641",
>       "endTimeUnixNano":"1718811677526761641",
>       "attributes":[],
>       "events":[],
>       "Links":[],
>       "status":{
>         "code":1
>       },
>       "flags":257
>     }
>   ]
> }
> ```

Learn more in [Traces](https://opentelemetry.io/docs/concepts/signals/traces/) in the OpenTelemetry documentation.

## Enable and disable distributed tracing

Distributed tracing is disabled by default.

* [Enable distributed tracing](#enable-tracing)

* [Disable distributed tracing](#disable-tracing)

### Enable distributed tracing

1. Stop AM or the container in which it runs.

2. In the `/path/to/am/config` directory, create a `deployment/trace` directory. For example:

   * Linux

   * Windows

   ```bash
   $ mkdir -p /path/to/am/config/deployment/trace
   ```

   ```powershell
   PS C:\Users\Administrator> New-Item -ItemType Directory 'C:\path\to\am\config\deployment\trace'
   ```

3. In the `deployment/trace` directory, create a file named `config.json` with, at least, the following contents:

   ```json
   {
     "tracing": {
       "enabled": true
     }
   }
   ```

   Find information on additional configuration properties in [Configure distributed tracing](#configure-distributed-tracing).

   |   |                                                                                                                           |
   | - | ------------------------------------------------------------------------------------------------------------------------- |
   |   | If the content of `config.json` is invalid JSON, distributed tracing remains disabled, even if you set `"enabled": true`. |

4. Restart AM or the container in which it runs.

### Disable distributed tracing

1. Stop AM or the container in which it runs.

2. In the `/path/to/am/config/deployment/trace/config.json` file, set `"enabled": false`.

3. Restart AM or the container in which it runs.

## Configure distributed tracing

The Ping Advanced Identity Software supports a common set of configuration properties for OpenTelemetry support.

|   |                                                                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * The stability of this configuration interface is classified as [evolving](https://docs.pingidentity.com/pingam/release-notes/stability.html#interface-stability).

* Any changes to the configuration require a server restart. |

To change the default OpenTelemetry configuration, add the configuration properties to your `/path/to/am/config/deployment/trace/config.json` file, for example:

```json
{
  "tracing": {
    "enabled": true,
    "resourceAttributes": {
      "service.instance.id": "am-server-1"
    },
    "exporter": {
      "config": {
        "headers": {
          "X-CUSTOM-HEADER": "custom-value"
        }
      }
    },
    "spanLimits": {
      "maxNumberOfAttributesPerEvent": 128
      }
    }
  }
}
```

> **Collapse: Distributed tracing configuration properties**
>
> * enabled: boolean, optional
>
>   Set to `true` to enable OpenTelemetry tracing.
>
>   Default: `false`
>
> * resourceAttributes: object, optional
>
>   A map of additional resource attributes for processing traces. Find more information in the OpenTelemetry documentation on [Semantic Attributes with SDK-provided Default Value](https://opentelemetry.io/docs/specs/semconv/resource/#semantic-attributes-with-sdk-provided-default-value).
>
>   For example, if there are multiple AM instances in a deployment, you could set the `"service.instance.id"` resource attribute differently for each one to distinguish between them:
>
>   ```json
>   {
>       "resourceAttributes": {
>           "service.instance.id": "am-server-1"
>       }
>   }
>   ```
>
> * exporter: object, optional
>
>   Configuration for the exporter, which pushes traces to the OpenTelemetry service:
>
>   * type: string, optional
>
>     Set to `otlp` for OpenTelemetry Protocol (OTLP) support. This is currently the only supported protocol.
>
>     Default: `otlp`
>
>   * config: object, optional
>
>     Endpoint and timeout configuration:
>
>     * `compressionMethod`: *enumeration, optional*
>
>       Method used to compress trace data; either `gzip` or `none`.
>
>       Default: `gzip`
>
>     * `connectionTimeout`: *duration, optional*
>
>       Time out a connection to the endpoint after this duration.
>
>       Default: 10 seconds.
>
>     * `endpoint`: *string, optional*
>
>       The endpoint to publish traces to.
>
>       For HTTPS, AM trusts the default JVM CAs. To override this, set the `-Djavax.net.ssl.trustStore` and associated JVM settings when starting AM. Learn more about the optional settings in the [Java Secure Socket Extension (JSSE) Reference Guide](https://docs.oracle.com/en/java/javase/25/security/java-secure-socket-extension-jsse-reference-guide.html).
>
>       AM doesn't support TLS configuration for the tracing endpoint at this time.
>
>       Default: `http://localhost:4318/v1/traces`
>
>     * `headers`: *object, optional*
>
>       Map of additional headers to include in the export span request.
>
>       The following example sets the authorization header, `Authorization: Bearer ${bearer.token}`:
>
>       ```none
>       "headers": { "Authorization": "Bearer ${bearer.token}" }
>       ```
>
>     * `retries`: *object, optional*
>
>       Defines a retry policy for the export span requests.
>
>       Default: Enabled
>
>       * `backoffMultiplier`: *number, optional* Multiplier for the backoff wait time before retries.
>
>         Default: 1.5
>
>       * `enabled`: *boolean, optional*
>
>         Retry failed requests.
>
>         Default: `true`
>
>       * `initialBackoff`: *duration, optional*
>
>         How long to wait before the first retry.
>
>         Default: 1 second
>
>       * `maxAttempts`: *number, optional*
>
>         Maximum number of retries.
>
>         Default: 5
>
>       * `maxBackoff`: *duration, optional*
>
>         Maximum wait time between retries.
>
>         Default: 5 seconds
>
>     * `"timeout"`: *duration, optional*
>
>       Time out a request to publish data to the endpoint after this duration.
>
>       Default: 10 seconds.
>
>   * `batch`: *object, optional*
>
>     Enable and configure batch processing for trace data.
>
>     * `compressionMethod`: *enumeration, optional*
>
>       Method used to compress trace data; either `gzip` or `none`.
>
>       Default: `gzip`
>
>     * `enabled`: *boolean, optional*
>
>       Leave batch processing enabled in deployment.
>
>       Default: `true`
>
>     * `exporterTimeout`: *duration, optional*
>
>       Time out a data exporter after this duration.
>
>       Default: 30 seconds
>
>     * `exportUnsampledSpans`: *boolean, optional*
>
>       Whether to report on unsampled spans.
>
>       Default: `false`
>
>     * `maxExportBatchSize`: *number, optional*
>
>       Maximum number of spans in a batch.
>
>       Default: 512
>
>     * `maxQueueSize`: *number, optional*
>
>       Maximum number of spans to queue before dropping them.
>
>       Default: 2048
>
>     * `scheduleDelay`: *duration, optional*
>
>       Maximum interval between sending batches of trace data.
>
>       Default: 50 seconds
>
> * `sampler`: *object, optional*
>
>   Configuration for sampling spans.
>
>   * `ratio`: *number, optional*
>
>     For ratio-based types, a percentage of spans to process.
>
>     Default: 50 (percent)
>
>   * `type`: *string, optional*
>
>     The sampler strategy to use is one of the following:
>
>     * `alwaysOn`: Send every span for processing.
>
>     * `alwaysOff`: Never send any span for processing.
>
>     * `traceIdRatio`: Sample the specified ratio of spans, deterministically based on the trace IDs of the spans.
>
>     * `parentBasedAlwaysOn`: Always send the span for processing if the parent span was sampled. (Default)
>
>     * `parentBasedAlwaysOff`: Never send the span for processing if the parent span was sampled.
>
>     * `parentBasedTraceIdRatio`: Send the specified ratio of spans for processing if the parent span was sampled.
>
> * `spanLimits`: *object, optional*
>
>   Configuration for limits enforced when recording spans.
>
>   * `maxNumberOfAttributes`: *number, optional*
>
>     The maximum number of attributes per span.
>
>     Default: 128
>
>   * `maxNumberOfAttributesPerEvent`: *number, optional*
>
>     The maximum number of metadata items (attributes) attached to a span per event. An event is an annotation to span at a particular, meaningful point in time during the span's duration.
>
>     Default: 128
>
>   * `maxNumberOfAttributesPerLink`: *number, optional*
>
>     The maximum number of attributes per link.
>
>     Default: 128
>
>   * `maxNumberOfEvents`: *number, optional*
>
>     The maximum number of events per span.
>
>     Default: 128
>
>   * `maxNumberOfLinks`: *number, optional*
>
>     The maximum number of links per span. Links associate the current span with one or more other spans.
>
>     Default: 128

## Secure trace exports

To protect trace exports, configure a secure connection between AM and the trace collector.

These steps assume you're using the OpenTelemetry (OTel) Collector, but you can choose any trace collector. Adjust the steps accordingly.

Configuring a secure connection involves the following steps:

1. Configure the collector to receive traces over HTTPS.

   Specify the path to your collector's TLS certificate and private key and, optionally, the path to the CA certificate.

   If you're using the OTel collector, read OTel's collector documentation for information on [configuring TLS](https://github.com/open-telemetry/opentelemetry-collector/blob/main/config/configtls/README.md).

2. In the `/path/to/am/config/deployment/trace/config.json` file, make sure the exporter endpoint references HTTPS. For example:

   ```json
   {
       "tracing": {
           "enabled": true,
           "exporter": {
               "config": {
                   "endpoint": "https://otelcol.localtest.me:4318/v1/traces"
               }
           }
       }
   }
   ```

3. Add the trace collector's TLS certificate to the AM truststore. For example:

   ```bash
   $ keytool \
   -importcert \
   -file /path/to/cert_file.pem \
   -keystore /path/to/am/security/keystores/truststore
   ```

4. Restart AM or the container in which it runs.

## Visualize traces with Jaeger

You can use [Jaeger](https://www.jaegertracing.io/docs/1.56/getting-started/) to collect trace data directly from AM (or from your chosen telemetry collector) and to visualize that trace data.

### Example visualization with Jaeger

This example assumes a local AM deployment in Apache Tomcat.

1. Start Jaeger.

   Jaeger runs in a Docker container. Start Jaeger with a command similar to the following:

   ```bash
   docker run --rm --name jaeger \
     -p 5778:5778 \
     -p 16686:16686 \
     -p 4317:4317 \
     -p 4318:4318 \
     -p 14250:14250 \
     -p 14268:14268 \
     -p 9411:9411 \
     jaegertracing/jaeger:2.0.0 \
     --set receivers.otlp.protocols.http.endpoint=0.0.0.0:4318
   ```

2. Go through an AM authentication flow.

   This example authenticates the `amAdmin` user:

   ```bash
   * curl \
   --request POST \
   --header "Content-Type: application/json" \
   --header "X-OpenAM-Username: amadmin" \
   --header 'X-OpenAM-Password: password' \
   --header "Accept-API-Version: resource=2.0, protocol=1.0" \
   "https://am.example.com:8443/am/json/realms/root/authenticate"*
   ```

3. Navigate to Jaeger's UI at <http://localhost:16686/>.

4. Under Service select `am` (or the context path where you deployed AM) then click Find Traces.

   ![jaeger ui](../maintenance/_images/jaeger-ui.png)

5. Click the trace for the `HTTP POST` request to the `authenticate` endpoint to view the traces for the authentication flow:

   ![jaeger post request](../maintenance/_images/jaeger-post-request.png)

   Note the `forgerock.transaction_id 8156ce8c-c5f4-4f59-ba59-9dd41d654f68-54971`. This is the ID you'll use to correlate the trace with the AM audit logs.

## Correlate traces with audits

Distributed tracing doesn't change the AM audit logs in any way.

However, when you enable distributed tracing, you can enrich the traces to include audit transaction IDs in their metadata. If a request includes a transaction identifier and a *span* is created for that request, the span metadata is enriched with the transaction identifier. This lets you correlate requests between traces and audit logs to determine which requests are taking longer than anticipated and identify any bottlenecks.

In the previous example, the `forgerock.transaction_id` was `8156ce8c-c5f4-4f59-ba59-9dd41d654f68-54971` for the authentication request.

The entry in the `authentication.audit.json` file for that request is as follows:

```json
{
  "_id": "8156ce8c-c5f4-4f59-ba59-9dd41d654f68-54986",
  "timestamp": "2024-11-21T12:30:22.561Z",
  "eventName": "AM-LOGIN-COMPLETED",
  "transactionId": "8156ce8c-c5f4-4f59-ba59-9dd41d654f68-54971",
  "trackingIds": [
    "8156ce8c-c5f4-4f59-ba59-9dd41d654f68-54974"
  ],
  "userId": "id=amadmin,ou=user,dc=am,dc=example,dc=com",
  "principal": [
    "amadmin"
  ],
 ...
}
```

Note the correlation between the `forgerock.transaction_id` in the trace and the `transactionId` in the log entry.