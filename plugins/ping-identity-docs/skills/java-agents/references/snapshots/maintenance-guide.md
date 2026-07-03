---
title: Audit the deployment
description: Configure PingAM Java Agent auditing using the Commons Audit Framework, with remote, local, or combined audit event logging and field filtering.
component: java-agents
version: 2026
page_id: java-agents:maintenance-guide:auditing
canonical_url: https://docs.pingidentity.com/java-agents/2026/maintenance-guide/auditing.html
section_ids:
  remote_and_local_auditing: Remote and local auditing
  remote_auditing: Remote auditing
  local_auditing: Local auditing
  remote_and_local_auditing_2: Remote and local auditing
  audit_event_logs: Audit event logs
  audit-configure: Configure auditing
  audit-include-exclude: Include or exclude elements from the audit logs
---

# Audit the deployment

Auditing is managed by the Commons Audit Framework to log audit events for security, troubleshooting, and regulatory compliance. Audit logs are written in UTF-8 format.

## Remote and local auditing

### Remote auditing

In remote auditing, the agent logs audit events to the audit event handler configured in the AM realm. In an environment with several AM servers, the agent writes audit logs to the AM server that satisfies the agent request for client authentication or resource authorization.

The agent logs audit events remotely **only** when AM's global audit logging is enabled and configured in the realm where the agent runs.

Set up global audit logging in the AM admin UI:

1. In the AM admin UI, go to Configure > Global Services > Audit logging.

2. Enable Audit logging.

3. Enter values to include in Field whitelist filters or Field blacklist filters.

The following example path in the Field whitelist filters list includes the `Accept-Language` value in the http.request.headers field in *access* events:

```
/access/http/request/headers/accept-language
```

Learn more from AM's [Global audit logging](https://docs.pingidentity.com/pingam/8.1/security-guide/implementing-audit.html#configure-global-audit-logging).

### Local auditing

In local auditing, the agent logs audit events in JSON format to a file in the agent installation directory, `/path/to/java_agents/agent_type/Agent_n/logs/audit`.

### Remote *and* local auditing

In remote and local auditing, the agent logs audit events in the following locations:

* To a file in the agent installation directory.

* To the audit event handler configured in the AM realm in which the agent profile is configured.

## Audit event logs

When a request matches a not-enforced rule, the agent doesn't log an audit event for that request. Otherwise, the agent logs an audit event according to the configuration described in [Configure auditing](#audit-configure) and [Include or exclude elements from the audit logs](#audit-include-exclude).

The following example shows an audit event log for successful access to a resource:

```json
{
  "_id": "...", //This ID is internal to AM and available only in remote logs.
  "timestamp": "...",
  "eventName": "AM-ACCESS-OUTCOME",
  "transactionId": "...",
  "trackingIds": [
    "...",
    "..."
  ],
  "userId":"id=bjensen,ou=user,dc=example,dc=com",
  "client": {
    "ip": "...",
    "port": ...
  },
  "server": {
    "ip": "...",
    "port": 8020
  },
  "http": {
    "request": {
      "secure": false,
      "method": "GET",
      "path":"http://my.example.com:8020/examples/",
      "headers": {
        "accept": [
          "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
        ],
        "host": [
          "my.example.com:8020"
        ],
        "user-agent": [
          "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
        ]
      }
    }
  },
  "request": {
    "protocol": "HTTP/1.1",
    "operation": "GET"
  },
  "response": {
    "status": "SUCCESSFUL",
    "statusCode": "302",
    "elapsedTime": 25,
    "elapsedTimeUnits": "MILLISECONDS"
  },
  "component": "Java Policy Agent"
}
```

The audit log format uses the log structure shared by the Ping Advanced Identity Software. Learn more from [Audit log format](https://docs.pingidentity.com/pingam/8.1/security-guide/sec-maint-audit-ref.html#audit-log-format) in AM's *Security guide*.

Java Agent supports propagation of the transaction ID across the Ping Advanced Identity Software, using the HTTP header `X-ForgeRock-TransactionId`. Learn more from [Trust transaction headers](https://docs.pingidentity.com/pingam/8.1/security-guide/implementing-audit.html#configuring-trusttransactionheader-system-property) in AM's *Security guide*.

## Configure auditing

In the AM admin UI, access the audit configuration at Realms > *Realm Name* > Applications > Agents > Java > *Agent Name* > Global > Audit. Use the following properties to configure auditing:

* [Audit Access Types](../properties-reference/org.forgerock.agents.audit.what.html): Select the type of messages to log. For example, select `LOG_ALL` to log access allowed and access denied events.

* [Audit Log Location](../properties-reference/org.forgerock.agents.audit.where.html): Select whether to write the audit logs locally to the agent installation (`LOCAL`), remotely to AM (`REMOTE`), or to both places (`ALL`). For example, keep `REMOTE` to log audit events to the AM instances.

* [Enable Local Audit Log Rotation](../properties-reference/org.forgerock.agents.local.audit.log.rotation.enabled.html): Select whether to rotate the audit logs when they reach a maximum size.

* [Local Audit Log Rotation Size](../properties-reference/org.forgerock.agents.local.audit.log.rotation.bytes.html): Specify the maximum size of logs before rotation.

## Include or exclude elements from the audit logs

|   |                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Before you include non-safelisted audit event fields in the logs, consider the impact on security. Inclusion of some headers, query parameters, or cookies could cause credentials or tokens to be logged, and allow anyone with access to the logs to impersonate the holder of these credentials or tokens. |

To prevent logging of sensitive data for an audit event, the Common Audit Framework uses a safelist to specify which audit event fields appear in the logs. By default, only safelisted audit event fields are included in the logs.

Use [Audit Log Include Paths](../properties-reference/org.forgerock.agents.audit.include.path.list.html) and [Audit Log Exclude Paths](../properties-reference/org.forgerock.agents.audit.exclude.path.list.html) to include or exclude elements from the audit logs.

[Audit Log Exclude Paths](../properties-reference/org.forgerock.agents.audit.exclude.path.list.html) takes precedence over [Audit Log Include Paths](../properties-reference/org.forgerock.agents.audit.include.path.list.html). If a path is specified by both properties, the corresponding audit event field is excluded.

The following example excludes Header1 but includes Header2 and Cookie1:

```
org.forgerock.agents.audit.exclude.path.list[0]=/access/http/request/headers/Header1Name
org.forgerock.agents.audit.include.path.list[0]=/access/http/request/headers/Header2Name
org.forgerock.agents.audit.include.path.list[1]=/access/http/request/cookies/Cookie1Name
```
