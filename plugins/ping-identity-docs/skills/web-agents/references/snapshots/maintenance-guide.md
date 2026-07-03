---
title: Audit the deployment
description: Configure PingAM Web Agent audit logging for security and compliance, including remote, local, and combined audit modes and log format details.
component: web-agents
version: 2026
page_id: web-agents:maintenance-guide:auditing
canonical_url: https://docs.pingidentity.com/web-agents/2026/maintenance-guide/auditing.html
section_ids:
  remote_and_local_auditing: Remote and local auditing
  remote_auditing: Remote auditing
  local_auditing: Local auditing
  remote_and_local_auditing_2: Remote and local auditing
  audit_event_logs: Audit event logs
  audit-configure: Configure auditing
---

# Audit the deployment

Web Agent logs audit events for security, troubleshooting, and regulatory compliance.

## Remote and local auditing

### Remote auditing

In remote auditing, the agent logs events to the audit event handler configured in the AM realm. In an environment with several AM servers, the agent writes audit logs to the AM server that satisfies the agent request for client authentication or resource authorization.

The agent logs audit events remotely **only** when AM's global audit logging is enabled and configured in the realm where the agent runs.

Set up global audit logging in the AM admin UI:

1. In the AM admin UI, go to Configure > Global Services > Audit logging.

2. Enable Audit logging.

3. Enter values to include in Field whitelist filters or Field blacklist filters.

The following example path in the Field whitelist filters list includes the `Accept-Language` value in the http.request.headers field in *access* events:

```
/access/http/request/headers/accept-language
```

Learn more in AM's [Global audit logging](https://docs.pingidentity.com/pingam/8.1/security/implementing-audit.html#configure-global-audit-logging).

### Local auditing

In local auditing, the agent logs audit events in JSON format to `/path/to/web_agents/agent_type/instances/agent_n/logs/audit/audit.log`.

An example agent log file is `/path/to/web_agents/apache24_agent/instances/agent_1/logs/audit/audit.log`.

### Remote *and* local auditing

In remote and local auditing, the agent logs audit events in the following locations:

* To `/path/to/web_agents/agent_type/instances/agent_n/logs/audit/audit.log`

* To the audit event handler configured in the AM realm in which the agent profile is configured.

## Audit event logs

Audit logs are written in UTF-8 format. The following example shows an audit event log for successful access to a resource:

```json
{
   "timestamp":"2023-10-30T11:56:57Z",
   "eventName":"AM-ACCESS-OUTCOME",
   "transactionId":"608...77e",
   "userId":"id=bjensen,ou=user,dc=example,dc=com",
   "trackingIds":[
      "fd5...095",
      "fd5...177"
   ],
   "component":"Web Policy Agent",
   "realm":"/",
   "server":{
      "ip":"127.0.0.1",
      "port":8020
   },
   "request":{
      "protocol":"HTTP/1.1",
      "operation":"GET"
   },
   "http":{
      "request":{
         "secure":false,
         "method":"GET",
         "path":"/examples",
         "cookies":{
            "am-auth-jwt":"eyJ...iOi[...]"
            "i18next":"en",
            "amlbcookie":"01",
            "iPlanetDirectoryPro":"Ts2...oxR[...]"
         }
      }
   },
   "response":{
      "status":"DENIED"
   },
   "_id":"fd5...703" //This ID is internal to AM and available only in remote logs.
}
```

The audit log format uses the log structure shared by the Ping Advanced Identity Software. Learn more in [Audit log format](https://docs.pingidentity.com/pingam/8.1/security/sec-maint-audit-ref.html#audit-log-format) in AM's *Security guide*.

Web Agent supports propagation of the transaction ID across the Ping Advanced Identity Software, using the HTTP header `X-ForgeRock-TransactionId`. Learn more in [Trust transaction headers](https://docs.pingidentity.com/pingam/8.1/security/implementing-audit.html#configuring-trusttransactionheader-system-property) in AM's *Security guide*.

## Configure auditing

By default, auditing is disabled. Configure audit logging as follows:

1. On the AM admin UI, select Realms > *Realm Name* > Applications > Agents > Web > *Agent Name*.

2. On the Global tab, select the following options to select the type of audit events to log and the audit location. By default, auditing is disabled:

   * [Audit Access Types](../properties-reference/com.sun.identity.agents.config.audit.accesstype.html)

   * [Audit Log Location](../properties-reference/com.sun.identity.agents.config.log.disposition.html)

3. In `agent.conf`, optionally configure [Audit Path as Full URL](../properties-reference/com.sun.identity.agents.config.audit.path.fullurl.html) to log the full URL of the HTTP request. If not configured, only the path component of the HTTP request is logged.

4. In `agent.conf`, optionally configure the following properties to manage the location and size of the log files:

   * [Local Agent Audit File Name](../properties-reference/com.sun.identity.agents.config.local.audit.logfile.html)

   * [Local Audit Log Rotation Size](../properties-reference/com.sun.identity.agents.config.local.log.size.html)

   |   |                                                                                   |
   | - | --------------------------------------------------------------------------------- |
   |   | After changing a bootstrap property, restart the web server where the agent runs. |
