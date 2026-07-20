---
title: Audit the deployment
description: Configure PingAM Web Agent audit logging for security and compliance, including remote, local, and combined audit modes and log format details.
component: web-agents
version: 2026
page_id: web-agents:maintenance-guide:auditing
canonical_url: https://docs.pingidentity.com/web-agents/2026/maintenance-guide/auditing.html
llms_txt: https://docs.pingidentity.com/web-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
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

Learn more in AM's [Global audit logging](https://docs.pingidentity.com/pingam/8.1/monitoring/implementing-audit.html#configure-global-audit-logging).

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

The audit log format uses the log structure shared by the Ping Advanced Identity Software. Learn more in [Audit log format](https://docs.pingidentity.com/pingam/8.1/monitoring/audit-logging-ref.html#audit-log-format) in AM's *Security guide*.

Web Agent supports propagation of the transaction ID across the Ping Advanced Identity Software, using the HTTP header `X-ForgeRock-TransactionId`. Learn more in [Trust transaction headers](https://docs.pingidentity.com/pingam/8.1/monitoring/implementing-audit.html#configuring-trusttransactionheader-system-property) in AM's *Security guide*.

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

---

---
title: Maintenance guide
description: Recurring administrative operations for PingAM Web Agent, including auditing, monitoring, connection tuning, notifications, and key rotation.
component: web-agents
version: 2026
page_id: web-agents:maintenance-guide:preface
canonical_url: https://docs.pingidentity.com/web-agents/2026/maintenance-guide/preface.html
llms_txt: https://docs.pingidentity.com/web-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["index.adoc"]
---

# Maintenance guide

This guide describes how to perform recurring administrative operations in Web Agent.

---

---
title: Monitor services
description: Monitor PingAM Web Agent performance using the Prometheus endpoint, with metrics for policy decisions, cache operations, connections, and request latencies.
component: web-agents
version: 2026
page_id: web-agents:maintenance-guide:monitoring
canonical_url: https://docs.pingidentity.com/web-agents/2026/maintenance-guide/monitoring.html
llms_txt: https://docs.pingidentity.com/web-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  monitor-prometheus: Monitor with Prometheus
  access-prometheus-endpoint: Access the Prometheus endpoint
  monitor-types: Monitoring types
  prometheus-metrics: Metrics at the Prometheus endpoint
  notification-metrics: Notification metrics
  policy-decision-metrics: Policy decision metrics
  cache-metrics: Cache metrics
  connections-metrics: Connection metrics
  request-metrics: Request metrics
  monitor-endpoint: Monitor with the monitoring endpoint (deprecated)
  access-monitoring-endpoint: Access the monitoring endpoint
  monitor-metrics: Metrics at the monitoring endpoint (deprecated)
---

# Monitor services

The following sections describe how to set up and maintain monitoring in your deployment to ensure appropriate performance and service availability.

## Monitor with Prometheus

Web Agent automatically exposes a monitoring endpoint where Prometheus can scrape metrics in a standard Prometheus format (version 0.0.4).

You can find information about installing and running Prometheus in the [Prometheus documentation](https://prometheus.io/docs/introduction/overview/).

The Prometheus endpoint is protected by HTTP Basic Authentication. To access it, provide the agent URL, and the agent profile name and password. Always use HTTPS for secure connections to client applications.

The metrics returned are described in [Metrics at the Prometheus endpoint](#prometheus-metrics).

|   |                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Tools such as Grafana are available to create customized charts and graphs based on the information collected by Prometheus. Learn more on the [Grafana website](https://grafana.com). |

### Access the Prometheus endpoint

1. Install a Web Agent as described in the [Installation](../installation-guide/preface.html), and use the agent to protect a web application. For example, set up the example in [Policy enforcement](../user-guide/pep.html).

2. Access the Prometheus endpoint as follows, where `https://agent.example.com:443` is the agent URL, `web-agent` is the agent profile name and `password` is the agent profile password:

   ```none
   $ curl https://agent.example.com:443/agent/metrics --user web-agent:password
   ```

   The metrics are displayed:

   ```none
   # TYPE policy_change counter
   # HELP policy_change_total number of policy updates
   policy_change_total{topic="notification"} 0
   # TYPE config_change counter
   # HELP config_change_total number of configuration changes
   config_change_total{topic="notification"} 0
   # TYPE not_enforced counter
   # HELP not_enforced_total number of requests that were not enforced
   not_enforced_total{topic="enforcement"} 0
   ...
   ```

## Monitoring types

This section describes the data types used in monitoring:

* Counter

  Cumulative metric for a numerical value that only increases.

* Gauge

  Metric for a numerical value that can increase or decrease.

  The value for a gauge is calculated when requested and represents the state of the metric at that specific time.

* Histogram

  Metric that samples observations, counts them in buckets, and provides a sum of all observed values.

## Metrics at the Prometheus endpoint

### Notification metrics

Web Agent exposes the following notification-related monitoring metrics:

| Metric                | [Type](#monitor-types) | Description                                                                                     |
| --------------------- | ---------------------- | ----------------------------------------------------------------------------------------------- |
| policy\_change\_total | Counter                | Number of policy change notifications received from Advanced Identity Cloud or AM.              |
| config\_change\_total | Counter                | Number of agent configuration change notifications received from Advanced Identity Cloud or AM. |

### Policy decision metrics

Web Agent exposes the following policy decision monitoring metrics:

| Metric                       | [Type](#monitor-types) | Description                                                                                                                                                                                                                                                                     |
| ---------------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| not\_enforced\_total         | Counter                | Number of requests that weren't enforced by the agent because of the not-enforced URL lists.                                                                                                                                                                                    |
| not\_authorised\_total       | Counter                | Number of requests denied by policy.                                                                                                                                                                                                                                            |
| not\_authenticated\_total    | Counter                | Number of requests requiring authentication.	Compare this metric to the authenticated\_return\_total metric. When authenticated\_return\_total is very low, it can indicate a Denial of Service (DoS) attack, where repeated requests are made with no authentication attempts. |
| authenticated\_return\_total | Counter                | Number of requests returning after authentication.                                                                                                                                                                                                                              |
| local\_decision\_total       | Counter                | Number of policy decisions the agent makes locally.                                                                                                                                                                                                                             |
| remote\_decision\_total      | Counter                | Number of policy decisions the agent requests from Advanced Identity Cloud or AM.                                                                                                                                                                                               |
| cache\_decision\_total       | Counter                | Number of policy decisions the agent takes from the cache when the [AM\_POLICY\_CACHE\_MODE](../user-guide/configure-envvars.html#envvar-AM_POLICY_CACHE_MODE) environment variable is set to `on`.                                                                             |
| url\_cache\_decision\_total  | Counter                | Number of policy decisions the agent takes from the URL cache when the [AM\_POLICY\_CACHE\_MODE](../user-guide/configure-envvars.html#envvar-AM_POLICY_CACHE_MODE) environment variable is set to `off`.                                                                        |

### Cache metrics

Web Agent exposes the following cache-related monitoring metrics:

| Metric               | [Type](#monitor-types) | Description                                   |
| -------------------- | ---------------------- | --------------------------------------------- |
| cache\_write\_total  | Counter                | Number of session cache writes.               |
| cache\_update\_total | Counter                | Number of session cache updates.              |
| cache\_read\_total   | Counter                | Number of session cache reads.                |
| cache\_miss\_total   | Counter                | Number of sessions not found in cache.        |
| cache\_delete\_total | Counter                | Number of sessions deleted from cache.        |
| cache\_expiry\_total | Counter                | Number of sessions expired from cache.        |
| cache\_fault\_total  | Counter                | Number of sessions that couldn't be cached.   |
| cache\_occupancy     | Gauge                  | Proportion of session cache that is occupied. |

### Connection metrics

Web Agent exposes the following connection-related monitoring metrics:

| Metric                   | [Type](#monitor-types) | Description                          |
| ------------------------ | ---------------------- | ------------------------------------ |
| connection\_total        | Counter                | Number of connections created.       |
| connection\_reuse\_total | Counter                | Number of cached connections reused. |

### Request metrics

Web Agent exposes the following request monitoring metrics:

| Metric                    | [Type](#monitor-types) | Description                                             |
| ------------------------- | ---------------------- | ------------------------------------------------------- |
| policy\_request\_seconds  | Histogram              | Histogram of policy request times in seconds.           |
| session\_request\_seconds | Histogram              | Histogram of session request times in seconds.          |
| config\_request\_seconds  | Histogram              | Histogram of configuration request times in seconds.    |
| agent\_time\_seconds      | Histogram              | Histogram of agent time in request pipeline in seconds. |

## Monitor with the monitoring endpoint (deprecated)

|   |                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------- |
|   | The monitoring endpoint described in this section is deprecated. Use it only for diagnostics, in conjunction with Support. |

A monitoring endpoint provides access to metrics for operations within the agent and between the agent an AM.

The monitoring endpoint is protected by HTTP Basic Authentication. To access it, provide the agent URL, and the agent profile name and password. Always use HTTPS for secure connections to client applications.

Metrics are displayed as a JSON response, with the fields described in [Metrics at the monitoring endpoint (deprecated)](#monitor-metrics).

### Access the monitoring endpoint

1. Install a Web Agent as described in the [Installation](../installation-guide/preface.html), and use the agent to protect a web application. For example, set up the example in [Policy enforcement](../user-guide/pep.html).

2. Access the agent monitoring endpoint as follows, where `https://agent.example.com:443` is the agent URL, and `web-agent` is the agent profile name.

   ```none
   $ curl https://agent.example.com:443/agent/monitor --user web-agent

   Enter host password for user 'web-agent':
   ```

3. Enter the agent profile password to display the metrics:

   ```json
   {
     "cache-invalidation": {
       "policy": 0,
       "profile": 1
     },
     "policy-decisions": {
       "neu": 0,
       "local": 0,
       "remote": 2,
       "cache": 0
       },
     "gc": {
       "runs": 1,
       "released": 0,
       "release-deferred": 0,
       "fill": 0.000000
     },
     "cache-operations": {
       "writes": 0,
       "rewrites": 2,
       "reads": 2,
       "misses": 0,
       "deletes": 0,
       "write-faults": 0,
       "expired": 0,
       "occupancy": 0
     },
     "connections": {
       "added": 2,
       "reused": 3
     }
   }
   ```

### Metrics at the monitoring endpoint (deprecated)

| Metric               | Submetric         | Count of                                                                                                                              |
| -------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `cache-invalidation` | `policy`          | Number of policy change notifications received from AM.                                                                               |
|                      | `profile`         | Number of agent configuration change notifications received from AM.                                                                  |
| `policy-decisions`   | `neu`             | Number of requests that were not enforced by the agent because of the not-enforced URL lists.                                         |
|                      | `local`           | Number of policy decisions the agent makes locally.                                                                                   |
|                      | `remote`          | Number of policy decisions the agent requests from AM.                                                                                |
|                      | `cache`           | Number of policy decisions the agent takes from the cache.                                                                            |
| `gc`                 | `runs`            | Number of garbage collection runs.                                                                                                    |
|                      | `released`        | Number of cache entries released during garbage collection runs.                                                                      |
|                      | `release-defered` | Number of entries with release deferred until the next garbage collection run.                                                        |
|                      | `fill`            | Floating point value between 0 and 1, representing the proportion of cache that is free after the most the recent garbage collection. |
| `cache-operations`   | `writes`          | Number of writes to cache.                                                                                                            |
|                      | `rewrites`        | Number of updates to cache.                                                                                                           |
|                      | `reads`           | Number of reads from cache.                                                                                                           |
|                      | `misses`          | Number of failed searches of the cache.                                                                                               |
|                      | `deletes`         | Number of deletes from cache.                                                                                                         |
|                      | `write-faults`    | Number of cache writes that fail because the cache is full.                                                                           |
|                      | `expired`         | Number of expired cache entries.                                                                                                      |
|                      | `occupancy`       | Proportion of cache that is occupied.                                                                                                 |
| `connections`        | `added`           | Number of new connections made.                                                                                                       |
|                      | `reused`          | Number of times existing connections were reused.                                                                                     |

---

---
title: Notifications
description: Configure PingAM Web Agent to receive WebSocket notifications from PingAM for configuration, session, and policy changes.
component: web-agents
version: 2026
page_id: web-agents:maintenance-guide:notifications
canonical_url: https://docs.pingidentity.com/web-agents/2026/maintenance-guide/notifications.html
llms_txt: https://docs.pingidentity.com/web-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  disable_notifications: Disable notifications
---

# Notifications

AM sends the following notifications to Web Agent through WebSockets:

* Configuration notifications

  When the administrator makes a change to a hot-swappable agent configuration property, AM sends a notification to the agent to reread the agent profile from AM.

  Configuration notifications apply when the agent profile is stored in AM's configuration data store.

  For more information about the cache, refer to [Configuration cache](../user-guide/caching.html#configuration-cache).

* Session Notifications

  When a client logs out, or a CTS-based session expires, AM sends a notification to the agent to remove the client's entry from the session cache.

  For more information about the cache, refer to [Session and policy decision cache](../user-guide/caching.html#session-cache).

* Policy Notifications

  When an administrator changes a policy, AM sends a notification to the agent to flush the session and policy decision cache, and the policy cache. [Enable Notifications](../properties-reference/com.sun.identity.agents.config.notification.enable.html) controls whether the AM server sends notifications to connected agents. It is enabled by default.

  For more information about the cache, refer to [Session and policy decision cache](../user-guide/caching.html#session-cache) and [Policy cache](../user-guide/caching.html#policy-cache).

In configurations with load balancers and reverse proxies, make sure the load balancers and reverse proxies support WebSockets.

The AM advanced server configuration property, `org.forgerock.openam.notifications.agents.enabled`, controls whether the AM server sends notifications to connected agents. This property is enabled by default.

## Disable notifications

|   |                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Notifications are enabled by default. Before disabling notifications, consider the impact on security if the agent is not notified of changes in AM. |

1. On the AM admin UI, select Realms > *Realm Name* > Applications > Agents > Web > *Agent Name*.

2. On the Global tab, deselect the following options to disable notifications:

   * [Enable Notifications](../properties-reference/com.sun.identity.agents.config.notification.enable.html)

     After changing this property, restart the web server where the agent runs.

   * [Enable Notifications of Agent Configuration Change](../properties-reference/com.sun.identity.agents.config.change.notification.enable.html)

---

---
title: Rotate keys
description: Rotate PingAM Web Agent encryption keys using agentadmin --k --rotate to limit key exposure and maintain security compliance.
component: web-agents
version: 2026
page_id: web-agents:maintenance-guide:rotate-keys
canonical_url: https://docs.pingidentity.com/web-agents/2026/maintenance-guide/rotate-keys.html
llms_txt: https://docs.pingidentity.com/web-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Maintenance", "Configuration", "Keys &amp; Certificates"]
section_ids:
  why_and_when_to_rotate_keys: Why and when to rotate keys
  steps_for_rotating_keys: Steps for rotating keys
  considerations_if_key_rotation_fails: Considerations if key rotation fails
---

# Rotate keys

Key rotation is the process of generating a new version of a key, assigning that version, and then deprovisioning the old key.

## Why and when to rotate keys

Regular key rotation is a security consideration that is sometimes required for internal business compliance. Regularly rotate keys to:

* Limit the amount of data protected by a single key.

* Reduce dependence on specific keys, making it easier to migrate to stronger algorithms.

* Prepare for when a key is compromised. The first time you try key rotation shouldn't be during a real-time recovery.

Key revocation is a type of key rotation done exceptionally if you suspect that a key has been compromised. To decide when to revoke a key, consider the following points:

* If limited use of the old keys can be tolerated, provision the new keys and then deprovision the old keys. Messages produced before the new keys are provisioned are impacted.

* If use of the old keys can't be tolerated, deprovision the old keys before you provision the new keys. The system is unusable until new keys are provisioned.

## Steps for rotating keys

1. Stop the web server.

2. View a list of Web Agent instances, using the [`agentadmin --l`](../installation-guide/agentadmin.html#agentadmin-l) command.

3. Rotate the keys for a Web Agent instance, using the [`agentadmin --k --rotate agent-instance`](../installation-guide/agentadmin.html#agentadmin-k) command.

   The following example rotates keys for the instance `agent_3`:

   * Unix

   * Windows

   ```
   $ cd /path/to/web_agents/apache24_agent/bin/
   $ ./agentadmin --k --rotate agent_3

   Performing key rotation for instance: agent_3

   Instance config directory: /path/to/web_agents/apache24_agent/instances/agent_3
   Loading agent.conf…​done
   Loading current credentials…​done
   Generating new encryption key…​done
   Encrypting current credentials with new encryption key:
   	- Encrypting agent profile password with new key…​done
   	- Encrypting certificate password with new key…​done
   	- Encrypting http proxy password with new key…​done
   Performing file operations:
   Gathering file information for agent-key.conf
   Gathering file information for agent-password.conf
   Backing up key file to agent-key.conf.bak
   Backing up password file to agent-password.conf.bak
   Writing new key to agent-key.conf…​done
   Writing new ciphertexts to agent-password.conf…​done
   Successfully wrote new key and passwords to disk

   Removing backup agent-key.conf.bak…​done
   Removing backup agent-password.conf.bak…​done

   Key rotation was successful for instance: agent_3
   ```

   ```
   C:\> cd web_agents\iis_agent\bin
   C:\web_agents\iis_agent\bin> agentadmin.exe --k --rotate agent_3

   Performing key rotation for instance: agent_3

   Instance config directory: …​
   Loading agent.conf…​done
   Loading current credentials…​done
   Generating new encryption key…​done
   Encrypting current credentials with new encryption key:
   	- Encrypting agent profile password with new key…​done
   	- Encrypting certificate password with new key…​done
   	- Encrypting http proxy password with new key…​done
   Backing up key file to agent-key.conf.bak
   Backing up password file to agent-password.conf.bak
   Writing new key to agent-key.conf…​done
   Writing new ciphertexts to agent-password.conf…​done
   Successfully wrote new key and passwords to disk

   Removing backup agent-key.conf.bak…​done
   Removing backup agent-password.conf.bak…​done

   Key rotation was successful for instance: agent_3
   ```

## Considerations if key rotation fails

* If key rotation fails while the agent is updating `agent-password.conf` or `agent-key.conf`, the rotate command tries to revert to the original files.

* If the rotate command can't revert to the original files, manually move `agent-password.conf.bak` and `agent-key.conf.bak` to `agent-password.conf` and `agent-key.conf`.

* After a failed key rotation on Windows, look for and delete `.bak` files. Windows can't rename a file as `.bak` if a `.bak` file already exists.

---

---
title: Troubleshoot
description: Troubleshoot PingAM Web Agent issues including WebSocket failures, TLS problems, startup errors, log permissions, and common configuration mistakes.
component: web-agents
version: 2026
page_id: web-agents:maintenance-guide:troubleshooting
canonical_url: https://docs.pingidentity.com/web-agents/2026/maintenance-guide/troubleshooting.html
llms_txt: https://docs.pingidentity.com/web-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["user-guide:troubleshooting.adoc"]
section_ids:
  get-info-about-problem: Get information about the problem
  websocket-issues: WebSocket issues
  validate-agent: Validate the agent
  check-websocket-jars-are-loading: Check the WebSocket jars are loading
  test-websocket-connection: Test the WebSocket connection
  tls-key-logging: TLS key logging
  apache_web_agent_example: Apache Web Agent example
  common-issues-solutions: Common issues and solutions
  installation-upgrade: Installation and upgrade
  start-up: Start up
  logs: Logs
  other-issues: Other issues
---

# Troubleshoot

Ping Identity provides support services, professional services, training, and partner services to help you set up and maintain your deployments. Learn more in [Getting support](https://docs.pingidentity.com/web-agents/release-notes/support.html).

## Get information about the problem

When you are trying to solve a problem, save time by asking the following questions:

* How do you reproduce the problem?

* What behavior do you expect, and what behavior do you see?

* When did the problem start occurring?

* Are there circumstances in which the problem doesn't occur?

* Is the problem permanent, intermittent, getting better, getting worse, or staying the same?

If you contact us for help, include the following information with your request:

* Description of the problem, including when the problem occurs and its impact on your operation.

* The product version and build information.

* Steps you took to reproduce the problem.

* Relevant access and error logs, stack traces, and core dumps.

* Description of the environment, including the following information:

  * Machine type

  * Operating system and version

  * Web server and version

  * Java version

  * Patches or other software that might affect the problem

## WebSocket issues

If you're experiencing issues with WebSocket connections, perform the following troubleshooting steps:

* [Validate the agent](#validate-agent)

* [Check the WebSocket jars are loading](#check-websocket-jars-are-loading)

* [Test the WebSocket connection](#test-websocket-connection)

### Validate the agent

The `agentadmin --V` command performs a number of checks, including WebSocket tests. Learn more in [agentadmin --V](../installation-guide/agentadmin.html#vi).

The results of the tests are output to the command line and show tests as `ok` or `not ok` depending on whether they passed, for example:

```none
...
validate_system_resources: ok
validate_session_profile: skipped
Agent websocket open error: error (6)
validate_websocket_connection: not ok
...
```

You can find further information about the tests and detailed results in the Validator log (`validate_nn.log` located in the agent `/log` directory).

### Check the WebSocket jars are loading

You can check the jars are being loaded on the AM Tomcat as follows:

1. Run the noisy command from the Tomcat `bin` directory, for example:

   ```none
   $ cd /path/to/tomcat/bin
   $ lsof | grep websocket
   ```

   * If the WebSocket jars are loading, you'll see responses similar to the following:

     ```none
     java 1014 root mem REG 8,1 225632 2097375 /usr/local/tomcat/lib/tomcat-websocket.jar
     java 1014 root mem REG 8,1 36905 2097376 /usr/local/tomcat/lib/websocket-api.jar
     java 1014 root 38r REG 8,1 36905 2097376 /usr/local/tomcat/lib/websocket-api.jar
     ...
     ```

   * If the WebSocket jars aren't loading, you won't see them listed.

2. Add the following option to the Tomcat startup script (`setenv.sh`) to view further details about the Java WebSocket API loading:

   ```none
   JAVA_OPTS=-verbose:class
   ```

   The Java WebSocket API is bundled with Tomcat.

3. Restart the web container.

4. Review the `catalina.out` log file for WebSocket details. For example, you'll see entries similar to the following if the WebSocket API is available:

   ```none
   $ cat ../logs/catalina.out | grep websocket

   [Loaded org.forgerock.openam.notifications.websocket.JsonValueDecoder from file:/path/to/tomcat/webapps/am/WEB-INF/lib/openam-notifications-websocket-7.5.0.jar]

   [Loaded org.forgerock.openam.notifications.websocket.NotificationsWebSocketConfigurator from file:/path/to/tomcat/webapps/am/WEB-INF/lib/openam-notifications-websocket-7.5.0.jar]

   [Loaded javax.websocket.EncodeException from file:/path/to/tomcat/lib/websocket-api.jar]

   ...
   ```

|   |                                                                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `openam-notifications-websocket-x.x.x.jar` is required for WebSockets to work. If it's missing, you'll see `404` responses. To resolve this, verify your Tomcat configuration or contact your System Administrator for further assistance. |

### Test the WebSocket connection

You can test the WebSocket connection by sending the agent's token to the notifications endpoint using curl. This test generates a response similar to what is output in the Validator log.

1. Authenticate as the agent to return the agent's token:

   ```none
   $ curl \
   --request POST \
   --header "X-OpenAM-Username: agent-id" \ (1)
   --header "X-OpenAM-Password: password" \ (2)
   --header "Content-Type: application/json" \
   --header "Accept-API-Version: resource=2.1" \
   'https://am.example.com:8443/am/json/realms/root/realms/alpha/authenticate?auth-service' (3)
   ```

   |       |                                                                                                                                                                                                                                                                                                                                        |
   | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **1** | Replace *agent-id* with the ID of the agent profile you created.                                                                                                                                                                                                                                                                       |
   | **2** | Replace *password* with the agent password.                                                                                                                                                                                                                                                                                            |
   | **3** | Replace *auth-service* with either `authIndexType=module&authIndexValue=Application` or `authIndexType=service&authIndexValue=Agent` depending on whether you [authenticate](../installation-guide/pre-installation.html#authenticate-agent-idc) using the default non-configurable authentication module or a journey called `Agent`. |

   If authentication is successful, the response includes the `tokenId` that corresponds to the agent session and the URL to which the agent would normally be redirected. For example:

   ```json
   {
        "tokenId":"AQIC5wM...​TU3OQ*",
        "successUrl":"/am/console",
        "realm":"/alpha"
   }
   ```

2. Send the agent's token to the notifications endpoint, for example:

   ```none
   $ curl \
   --verbose \
   --show-headers \
   --no-buffer \
   --header "Connection: Upgrade" \
   --header "Upgrade: websocket" \
   --header "Host: agent.example.com:443" \
   --header "Origin: https://notagent.example.com:8443" \
   --header "Sec-WebSocket-Key: SGVsbG8sIHdvcmxkIQ==" \
   --header "Sec-WebSocket-Version: 13" \
   --header "iPlanetDirectoryPro: AQIC5wM…​​TU3OQ*"
   'https://am.example.com:8443/am/notifications'
   ```

   The notifications endpoint applies some login processing logic using a servlet filter and returns one of the following responses:

   * 101 response

     A `101` response indicates everything is ok. It confirms the request is valid, it has been upgraded successfully, and the WebSockets connection is working correctly.

     > **Collapse: Example 101 response**
     >
     > ```none
     > * Trying 198.51.100.0...
     > * TCP_NODELAY set
     > * Connected to am.example.com (198.51.100.0) port 8443 (#0)
     > > GET /am/notifications HTTP/1.1
     > > Host: agent.example.com:443
     > > User-Agent: curl/8.71.0
     > > Accept: */*
     > > Connection: Upgrade
     > > Upgrade: websocket
     > > Origin: https://notagent.example.com:8443
     > > Sec-WebSocket-Key: SGVsbG8sIHdvcmxkIQ==
     > > Sec-WebSocket-Version: 13
     > > iPlanetDirectoryPro: AQIC5wM…​​TU3OQ*
     >
     > >
     >
     > < HTTP/1.1 101
     > HTTP/1.1 101
     > < X-Frame-Options: SAMEORIGIN
     > X-Frame-Options: SAMEORIGIN
     > < Upgrade: websocket
     > Upgrade: websocket
     > < Connection: upgrade
     > Connection: upgrade
     > < Sec-WebSocket-Accept: qGEgH3En71di5rrssAZTmtRTyFk=
     > Sec-WebSocket-Accept: qGEgH3En71di5rrssAZTmtRTyFk=
     > < Date: Mon, 21 Oct 2024 17:38:15 GMT
     > Date: Mon, 21 Oct 2024 17:38:15 GMT
     > ```

   * 403 response

     A `403 Access Forbidden` response means the agent has failed to establish a WebSocket connection with AM. You'll see `401` responses for this issue in the logs.

     A common reason for a `403` or `401` response is a mismatch between the agent cookie name and the cookie name in AM. The [agent cookie name](../properties-reference/com.sun.identity.agents.config.cookie.name.html) is used to construct the request sent to the notifications endpoint and must match what AM is expecting. Learn more in [Cookies](../user-guide/cookie-reset.html).

   * 404 response

     A `404` response typically means the WebSocket request has not been upgraded but the request sent to the notifications endpoint is valid. Possible causes for a `404` response are:

     * A network issue such as incorrectly configured load balancers or reverse proxies.

     * A Tomcat issue such as a missing `openam-notifications-websocket-x.x.x.jar`.

## TLS key logging

You can log TLS keys to help troubleshoot and diagnose TLS issues between the agent and AM.

To log TLS keys, you must:

1. Set the [Enable TLS key logging](../properties-reference/org.forgerock.agents.config.tls.keylog.enable.html) property to `true`.

2. Specify the name of the SSL key log file in the [AM\_SSL\_KEYLOG\_FILE](../user-guide/configure-envvars.html#am-ssl-keylog-file) environment variable.

|   |                                                                                                                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Only enable TLS key logging when advised by Support. After troubleshooting, disable key logging and remove the SSL key log file.The SSL key log file contains potentially sensitive TLS transaction data and should be protected from unauthorized access. |

### Apache Web Agent example

1. Set the `org.forgerock.agents.config.tls.keylog.enable` property to `true` in the `agent.conf` file.

2. Set the `AM_SSL_KEYLOG_FILE` environment variable to a suitable file in the `setenv.sh` file. The agent must have write access to this file.

3. Restart the web server.

4. Start a packet capture using [tcpdump](https://www.tcpdump.org) on the agent. For example, where AM is listening on port 4443:

   `tcpdump -i enp0s8 -s 0 -w /tmp/apache-agent-am.pcap 'port 4443'`

5. Make requests to the agent to initiate traffic from the agent to AM.

6. Stop the packet capture.

7. Unset the `AM_SSL_KEYLOG_FILE` environment variable in the `setenv.sh` file.

8. Set the `org.forgerock.agents.config.tls.keylog.enable` property to `false` in the `agent.conf` file.

9. Restart the web server.

10. Send the SSL key log file and packet capture to Support for troubleshooting.

11. Remove the SSL key log file from your system.

## Common issues and solutions

|   |                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `agentadmin` command offers a validation mode for the agent that can help you troubleshoot issues in your environment; for example, after an agent upgrade or a network change. Learn more in [agentadmin --V](../installation-guide/agentadmin.html#vi). |

### Installation and upgrade

> **Collapse: Shared memory errors during upgrade or installation**
>
> * Question
>
>   During upgrade or installation, what should I do if I get shared memory errors?
>
> * Answer
>
>   1. Stop the web server where the agent is installed.
>
>   2. Delete the following shared memory files:
>
>      * `/dev/shm/am_cache_0`
>
>      * `/dev/shm/am_log_data_0`
>
>        Depending on your configuration, the files could be named differently.
>
>   3. Start the agent.

> **Collapse: Error installing agents with SELinux**
>
> * Question
>
>   I am trying to install Web Agent on a server with SELinux enabled in `enforcing` mode, and I am getting error messages after installation or the web server doesn't start up. What happened?
>
> * Answer
>
>   When installing Web Agent on Linux or Unix servers, you must ensure that the user that runs the web server process has read and write permissions for the agent installation directory and files.
>
>   If SELinux is enabled in `enforcing` mode, you must also ensure that SELinux is configured to allow the web server process to perform read and write operations to the agent installation directory and files. By default, SELinux only allows the web server process to read files in well-known authorized locations, such as the `/var/www/html` directory.
>
>   For environments where security can be more relaxed, consider setting SELinux or the `httpd_t` context in `permissive` mode for troubleshooting purposes.
>
>   You can find details about configuring SELinux in the Linux documentation.

> **Collapse: Failure after installation**
>
> * Question
>
>   After starting a web agent installation, I see a failure in the logs:
>
> ```none
> [../resources/troubleshooting/troubleshooting.bash:#web-agent-install]
> ```
>
> * Answer
>
>   Web Agent installation, can fail if AM's validation of the agent configuration exceeds the default timeout of 4 seconds.
>
> You can set the `AM_NET_TIMEOUT` environment variable to change the default timeout, and then rerun the installation.

> **Collapse: Errors after upgrade**
>
> * Question
>
>   I have upgraded my agent and, in the logs, I can see errors similar to the following:
>
> ```none
> redirect_uri_mismatch. The redirection URI provided doesn't match a pre-registered value.
> com.iplanet.sso.SSOException: Invalid Agent Root URL
> com.iplanet.sso.SSOException: Goto URL not valid for the agent Provider ID
> ```
>
> What should I do?
>
> * Answer
>
>   Web Agent accepts only requests sent to the URL specified by the Agent Root URL for CDSSO property. For example, `https://agent.example.com:443`.
>
>   As a security measure, Web Agent prevents you from accessing the agent on URLs not defined in the Agent Root URL for CDSSO property. Add entries to this property when:
>
>   * Accessing the agent through different protocols. For example, `http://agent.example.com/` and `https://agent.example.com/`.
>
>   * Accessing the agent through different virtual host names. For example, `https://agent.example.com/` and `https://internal.example.com/`.
>
>   * Accessing the agent through different ports. For example, `https://agent.example.com/` and `https://agent.example.com:8443/`.

> **Collapse: Configuration not updated after upgrade**
>
> * Question
>
>   I have upgraded my Unix Apache or IBM HTTP Server Web Agent, and even though notifications are enabled, the agent doesn't update its configuration. What is happening?
>
> * Answer
>
>   Set the web agent logging level to the maximum by performing the following steps:
>
>   1. Set the environment variable `AM_SYSTEM_LOG_LEVEL` to `ALL` in your command line session. For example:
>
>      ```
>      $ export AM_SYSTEM_LOG_LEVEL=ALL
>      ```
>
>   2. Restart the Apache or IBM HTTP server.
>
>   3. Check the logs generated in the `/path/to/web_agents/agent_type/log/system_n.log` file.
>
>      Sometimes stopping or upgrading an agent doesn't clean the pipe file the agent uses to communicate with AM. If the newly started agent can't create the pipe to communicate with AM because it already exists, the agent would log messages like the following:
>
>      ```none
>      …​ UTC   DEBUG [1:10551398][source/monitor.c:503]monitor startup
>      …​ UTC   ERROR [102:10551398]monitor unable to get semaphore
>      …​ UTC   DEBUG [304:10551398][source/config.c:295]config_initialise():  agent configuration read from cache, agent: / agent profile name
>      ```
>
> If you see similar error messages, perform the following steps to delete the pipe file:
>
> 1. Stop the Apache or IBM HTTP server.
>
> 2. Change directories to the `/tmp` directory.
>
> 3. Delete the `monitor.pipe` file.
>
> 4. Restart the Apache or IBM HTTP server.

### Start up

> **Collapse: Apache agent start up**
>
> * Question
>
>   I have installed the Unix Apache Web Agent, and neither Apache HTTP Server nor the agent start up or log any message. If I remove the agent, the Apache HTTP Server starts again. What can be the problem?
>
> * Answer
>
>   To troubleshoot Web Agent or a web server that doesn't start, set the agent logging level to the maximum by performing the following steps:
>
>   1. Set the environment variable `AM_SYSTEM_LOG_LEVEL` to `All` in your command line session. For example:
>
>      ```
>      $ export AM_SYSTEM_LOG_LEVEL=ALL
>      ```
>
>   2. Restart the Apache HTTP Server.
>
>   3. Check the logs generated in the `/path/to/web_agents/agent_type/log/system_n.log`.
>
>      Web Agent reserves memory for the policy and session cache based on the `AM_MAX_SESSION_CACHE_SIZE` environment variable. If the server where the agent is installed doesn't have enough shared memory available, the web agent may log messages like the following:
>
>      ```none
>      017-11-10 12:06:00.492 +0000   DEBUG [1:7521][source/shared.c:1451]am_shm_create2() about to create block-clusters_0, size 1074008064
>      2017-11-10 12:06:00.492 +0000   ERROR [1:7521]am_shm_create2(): ftruncate failed, error: 28
>      ```
>
>      The error message means the web agent tries to reserve 1074008064 bytes of memory, but there isn't enough shared memory available. Several reasons may explain why the shared memory is running low, such as:
>
>      * A new application or additional workload may be stretching the server resources to the limit.
>
>        In this case, ensure that the server has enough shared memory available to satisfy the need of all the applications.
>
>      * A web agent may not have been able to release its shared memory after stopping. Therefore, even if the shared memory is technically not in use, it is still reserved and can't be reassigned unless freed.
>
>        Different operating systems manage the shared memory in different ways. Refer to your operating system documentation for information about checking shared memory usage.
>
>        You can reduce the amount of memory the web agent reserves for the session and policy cache by setting the `AM_MAX_SESSION_CACHE_SIZE` environment variable to a value between 1048576 (1 MB) and 1074008064 bytes (1 GB). Learn more in [Environment variables](../user-guide/configure-envvars.html).
>
>        Troubleshooting a component that doesn't start and doesn't generate logs may be difficult to diagnose. Contact Support for more help and information.

> **Collapse: Apache fails to start due to permission errors**
>
> * Question
>
>   Apache fails to start and I see errors similar to the following in the Apache logs:
>
>   ```bash
>   [amagent:error] validate_necessary_file_permissions: FATAL startup error: no access to /opt/web_agents/apache24_agent/lib/../log error: 13 (Permission denied)
>   [amagent:error] validate_necessary_file_permissions: [ACTION] Please ensure that the user: [www-data (uid:33)] has access to: /opt/web_agents/apache24_agent/lib/../log/
>   [amagent:error] amagent_init_servers server: 127.0.1.1:0 FAILED Agent Preflight validation, result: (13) Permission denied
>   [:emerg] AH00020: Configuration Failed, exiting
>   ```
>
> * Answer
>
>   The Web Agent runs preflight checks on startup and couldn't access one or more agent directories. For example, if the log directory is owned by root when Apache runs as a non-root user.
>
>   To fix the issue, check the ownership and permissions of the agent directories and ensure the user running Apache has the required access.
>
>   If you need to bypass the preflight checks temporarily, for example to diagnose a startup problem, set the [`AmBypassPreflightChecks` directive](../installation-guide/apache.html#apache-bypass-preflight) to `On` in your Apache configuration.

### Logs

> **Collapse: Logs not written**
>
> * Question
>
>   Why are logs not being written to `/log/system_0.log` and `/log/monitor_0.pipe` files? I am seeing this error:
>
> ```none
> unable to open event channel
> ```
>
> * Answer
>
>   It is likely that the agent doesn't have permission to be able to write to the `/log/system_0.log` and `/log/monitor_0.pipe` log files.
>
>   This can occur if you used the `agentadmin --V[i]` validator command using a user account that is different to the account used to run your web server.
>
>   Run the validator command as the same user that runs the web server, for example, by using the `sudo` command.
>
>   To fix the issue, change the ownership of these files to match the user or group that is running your web server.

> **Collapse: Can't rotate logs**
>
> * Question
>
>   My web server and Web Agent are installed as root, and the agent can't rotate logs. I am seeing this error:
>
> ```none
> Could not rotate log file ... (error: 13)
> ```
>
> What should I do?
>
> * Answer
>
>   If the web server is running with a non-root user, for example, the `daemon` user, you must ensure that user has the following permissions:
>
>   * Read Permission:
>
>     * `/web_agents/agent_name/lib`
>
>   * Read and Write Permission:
>
>     * `/web_agents/agent_name/instances/agent_nnn`
>
>     * `/web_agents/agent_name/log`
>
>   Apply execute permissions on the folders listed above, recursively, for the user that runs the web server.
>
>   For IIS or ISAPI agents, change the ownership of the files using the `agentadmin --o` command. Learn more in [agentadmin command](../installation-guide/agentadmin.html).
>
>   |   |                                                                                                                                          |
>   | - | ---------------------------------------------------------------------------------------------------------------------------------------- |
>   |   | You may also see similar issues if SELinux is enabled in `enforcing` mode, and it isn't configured to allow access to agent directories. |

### Other issues

> **Collapse: HTTP headers are ignored**
>
> * Question
>
>   When I map a response or attribute to an HTTP header, using the following properties, why is the header ignored:
>
>   * [Session Attribute Map](../properties-reference/com.sun.identity.agents.config.session.attribute.mapping.html)
>
>   * [Response Attribute Map](../properties-reference/com.sun.identity.agents.config.response.attribute.mapping.html)
>
>   * [Profile Attribute Map](../properties-reference/com.sun.identity.agents.config.profile.attribute.mapping.html)
>
> * Answer
>
>   When injecting information into HTTP headers, do not use underscores (`_`) in the header name. Underscores are incompatible with systems that run CGI scripts, and the header can be silently dropped.

> **Collapse: Port 80 used as default**
>
> * Question
>
>   My Apache HTTP server isn't using port 80. When I install Web Agent it defaults to port 80. How do I fix this?
>
> * Answer
>
>   You probably set `ServerName` in the Apache HTTP Server configuration to the host name, but did not specify the port number.
>
>   Instead, set both the host name and port number for `ServerName` in the configuration. For example, if you have Apache HTTP Server configured to listen on port 8080, then set `ServerName` appropriately as in the following excerpt:
>
> ```none
> <VirtualHost *:8080>
> ServerName www.localhost.example:8080
> ```

> **Collapse: Protection against phishing attacks**
>
> * Question
>
>   How do I increase security against possible phishing attacks through open redirect?
>
> * Answer
>
>   You can specify a list of valid URL resources against which AM validates the `goto` and `gotoOnFail` URL using the Valid `goto` URL Resource service.
>
>   AM only redirects a user if the `goto` and `gotoOnFail` URL matches any of the resources specified in this setting. If no setting is present, it is assumed that the `goto` and `gotoOnFail` URL is valid.
>
>   To set the Valid `goto` URL Resources, use the AM admin UI, and go to Realms > *Realm Name* > Services > Add > Validation Service, and then add one or more valid `goto` URLs.
>
>   You can use the "\*" wildcard to define resources, where "\*" matches all characters except "?". For example, you can use the wildcards, such as `https://website.example.com/*` or `https://website.example.com/*?*`. For more specific patterns, use resource names with wildcards as described in [Configuring success and failure redirection URLs](https://docs.pingidentity.com/pingam/8.1/am-authentication/redirection-url-precedence.html).

> **Collapse: Infinite redirection loops**
>
> * Question
>
>   I have client-based (stateless) sessions configured in AM, and I am getting infinite redirection loops. In the `debug.log` file I can see messages similar to the following:
>
>   ```none
>   ... +0000 ERROR [c5319caa-beeb-5a44-a098-d5575e768348]state identifier not present in authentication state
>   ... +0000 WARNING [c5319caa-beeb-5a44-a098-d5575e768348]unable to verify pre-authentication cookie
>   ... +0000 WARNING [c5319caa-beeb-5a44-a098-d5575e768348]convert_request_after_authn_post(): unable to retrieve pre-authentication request data
>   ... +0000 DEBUG [c5319caa-beeb-5a44-a098-d5575e768348] exit status: forbidden (3), HTTP status: 403, subrequest 0
>   ```
>
>   What is happening?
>
> * Answer
>
>   The redirection loop happens because the client-based (stateless) session cookie is surpassing the maximum supported browser header size. Since the cookie is incomplete, AM can't validate it.
>
>   To ensure the session cookie doesn't surpass the browser supported size, configure either signing and compression or encryption and compression.
>
>   Learn more in AM's [Security guide](https://docs.pingidentity.com/pingam/8.1/security/session-state-configure-cookie-security.html#policy_agent5_client-based).

> **Collapse: Custom pages aren't displayed**
>
> * Question
>
>   After upgrade, the default Apache welcome page appears instead of my custom error pages. What should I do?
>
> * Answer
>
>   Check your Apache `ErrorDocument` configuration. If the custom error pages are not in the document root of the Apache HTTP Server, enclose the `ErrorDocument` directives in `Directory` elements. For example:
>
> ```none
> <Directory "/web/docs">
>    ErrorDocument 403 myCustom403Page.html
> </Directory>
> ```
>
> You can find details about `ErrorDocument` in the [Apache](https://httpd.apache.org) documentation.

> **Collapse: Agent not protecting a website**
>
> * Question
>
>   My Web Agent isn't protecting my website. In the logs, I can see errors similar to the following:
>
> ```none
> ... -0500  ERROR [86169084-5648-6f4d-a706-30f5343d9220]config_fetch():  failed to load configuration for agent: myagent myagent, error -24
> ... -0500  ERROR [86169084-5648-6f4d-a706-30f5343d9220]amagent_auth_handler(): failed to get agent configuration instance, error: invalid agent session*
> ```
>
> What is happening?
>
> * Answer
>
>   The Web Agent is unable to log in to AM. Possible causes are:
>
>   * Network connection between the agent and AM is unavailable.
>
>   * The [AM Connection URL](../properties-reference/com.sun.identity.agents.config.naming.url.html) property, which specifies the AM URL may be misconfigured.

> **Collapse: Agent not protecting a website**
>
> * Question
>
>   My Web Agent isn't protecting my website. In the `debug.log` file I can see messages similar to the following:
>
> ```none
> ... GMT DEBUG [162ba6eb-cf88-3d7f-f92c-ee8b21971b4c]: (source/oidc.c:265) agent_realm doesn't have the expected value: JWT
>    {
>    "sub":"bjensen",
>    "auditTrackingId":"267d1f56-0b97-4830-ae91-6be4b8b7099f-5840",
>    "iss":"https://am.example.com:8443/am/oauth2/alpha",
>    "tokenName":"id_token",
>    "nonce":"D3AE96656D6D634489AF325D90C435A2",
>    "aud":"webagent",
>    "s_hash":"rxwxIoqDFiwt4MxSwiBa-w",
>    "azp":"webagent",
>    "auth_time":1561600459,
>    "forgerock":{
>    "ssotoken":"wi8tHql...MQAA*",
>    "suid":"267d1f56-0b97-4830-ae91-6be4b8b7099f-5647"
>    },
>    "realm":"/alpha",
>    "exp":1561607661,
>    "tokenType":"JWTToken",
>    "iat":1561600461,
>    "agent_realm":"/alpha"
>    }
> ... GMT WARNING [162ba6eb-cf88-3d7f-f92c-ee8b21971b4c]: redirect_after_authn(): unable to validate JWT
> ```
>
> What is happening?
>
> * Answer
>
>   If you configured the agent profile in a realm other than AM's top-level realm (`/`), you must configure the agent `com.sun.identity.agents.config.organization.name` bootstrap property with the realm where the agent profile is located. For example, `/alpha`.
>
>   Realm names are case-sensitive. Failure to set the realm name exactly as configured in AM causes the agent to fail to recognize the realm.

> **Collapse: Can't access protected resources**
>
> * Question
>
>   I am getting HTTP 403 Forbidden messages when accessing protected resources, and I can see errors similar to the following in the `debug.log` file:
>
> ```none
> ... GMT WARNING [69d4632c-82af-b853-0f340vb7b754]: too many pending authentications
> ... GMT ERROR  [69d4632c-82af-76da-b853-0f340vb7b754]: save_pre_authn_state(): unable to save state for request
> ```
>
> What is happening?
>
> * Answer
>
>   Agents store the progress of authentication with AM in the pre-authentication cookie, `agent-authn-tx`. This cookie has a maximum size of 4096 bytes, and can fill up if the agent receives many parallel unauthenticated requests to access protected resources.
>
>   Learn more in [Enable Multivalue for Pre-Authn Cookie](../properties-reference/org.forgerock.openam.agents.config.multivalue.pre.authn.cookies.html).

> **Collapse: Can't access protected resources**
>
> * Question
>
>   I am getting HTTP 403 Forbidden messages when accessing the Web Agent.
>
> * Answer
>
>   Make sure the Web Agent is executable:
>
>   1. In the terminal where the Web Agent is running, go to `/opt/web_agents`.
>
>   2. Review and, if necessary, change the permissions for the directory:

> **Collapse: WebSocket connections**
>
> * Question
>
>   I am seeing errors such as the following:
>
>   ```none
>   WARNING: Failed to create new WebSocket connection, backing off
>   org.forgerock.openam.agents.notifications.websocket.WebSocketConnectionException: Failed to create connection
>   ```
>
> * Answer
>
>   Make sure any load balancers or reverse proxies configured in your environment support WebSocket protocols.

---

---
title: Tune connections
description: Enable and tune connection pooling between PingAM Web Agent and PingAM to reduce connection overhead and improve performance.
component: web-agents
version: 2026
page_id: web-agents:maintenance-guide:connection-pooling
canonical_url: https://docs.pingidentity.com/web-agents/2026/maintenance-guide/connection-pooling.html
llms_txt: https://docs.pingidentity.com/web-agents/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Tune connections

Use a connection pool between Web Agent and AM to cache and reuse connections, and so reduce the overhead of creating new connections. The agent can use an array of connections concurrently, with multiple request threads.

To enable connection pooling, set [Enable Connection Pooling](../properties-reference/org.forgerock.agents.config.connection.pool.enable.html) to `true`. Test and tune the performance of your deployment with connection pooling before you use it in a production environment.

The following image shows the architecture of a connection pool:

![Connection pool](_images/connection-pool.svg)

The following image shows the flow of information when a request is treated in a connection pool:

![Data flow when a request is treated in a connection pool](_images/connection-pool-flow.svg)

When a client makes a request, the agent intercepts the request and uses the connection pool to connect to AM. If a connection is available, the agent uses that connection. The client is unaware of the connection reuse.

If a connection is not available, and fewer than 1024 connections are in use, the agent creates and uses a new connection. If 1024 connections are already in use, the request waits until an existing connection is released, or a new connection can be created.

When 1024 connections are in use, the agent creates additional temporary connections. Connections can be closed by AM/IDC, but the agent reopens them when it detects that they are closed.

When the request is complete, the agent closes the connection to the pool, but retains the physical connection. The connection is then available to requests with the same connection parameters.

Consider the following for connection pooling:

* The connection pool can contain up to 1024 cached connections

* When more than 1024 connections are required, the agent creates temporary connection.

* By default, connections timeout after four seconds of waiting for a response. To change this value, configure [Connection Timeout](../properties-reference/com.sun.identity.agents.config.connect.timeout.html)

* Tune [Connection Timeout](../properties-reference/com.sun.identity.agents.config.connect.timeout.html) so that it is:

  * Long enough for systems to respond, and therefore prevent unnecessary failures

  * As short as possible to minimize the time to wait after a network failure

* To reduce the overhead of making new connections and SSL handshakes, set the HTTP keep-alive headers for AM containers or reverse proxies to longer than [Connection Timeout](../properties-reference/com.sun.identity.agents.config.connect.timeout.html).