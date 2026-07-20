---
title: About Server Clustering
description: This section introduces the server clustering functionality of PingFederate.
component: pingfederate
version: 13.1
page_id: pingfederate:server_clustering_guide:pf_server_clustering_guide
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/server_clustering_guide/pf_server_clustering_guide.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 10, 2024
---

# About Server Clustering

This section introduces the server clustering functionality of PingFederate.

Use this guide to learn the following concepts and tasks for deploying PingFederate server clusters:

* [Overview of clustering](pf_overview_cluster.html)

* [Cluster protocol architecture](pf_cluster_protoc_architec.html)

* [Runtime state-management architectures](pf_runtime_state_manage_achitec.html)

* [Runtime state-management services](pf_runtime_state_manage_serv.html)

* [Deploying cluster servers](pf_deploying_cluster_servers.html)

* [Deploying provisioning failover](pf_deploy_provis_failover.html)

* [Configuration synchronization](pf_config_synchroniz.html)

---

---
title: Account Locking Service
description: The PingFederate Account Locking Service includes account lockout prevention and password spraying prevention.
component: pingfederate
version: 13.1
page_id: pingfederate:server_clustering_guide:pf_acc_lock_service
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/server_clustering_guide/pf_acc_lock_service.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  related-links: Related links
---

# Account Locking Service

The PingFederate Account Locking Service includes account lockout prevention and password spraying prevention.

Account lockout protection prevents user accounts from locking at the underlying user repository based on too many failed authentication attempts. It also adds a layer of protection against brute force and dictionary attacks because the user is locked out for a time period when the number of failed attempts exceeds the threshold. This protection is enabled in many areas of PingFederate, including the HTML Form Adapter, the Username Token Processor, the OAuth resource owner password credentials grant type, and the native authentication scheme for the administrative console and API.

Password spraying prevention adds a layer of defense against the attack pattern where bad actors try to gain access to protected resources by using the same password, typically weak or compromised, against multiple accounts from multiple locations. When enabled, PingFederate tracks the number of failed login attempts per password. When the number of failures for a particular password reaches a threshold, that password is temporarily locked out. Password spraying prevention applies to the HTML Form Adapter, the Username Token Processor, and the OAuth 2.0 resource owner password credentials grant type.

When PingFederate is in clustered mode, the service proxy uses a group remote procedure call (RPC)-based implementation. The configuration file is`<pf_install>/pingfederate/server/default/conf/cluster-account-locking.conf`.

This service supports both the adaptive clustering and directed clustering.

For adaptive clustering, PingFederate shares state information with a replica set. If region identifiers are defined, PingFederate shares state information among multiple replica sets across regions. You can override this default behavior in the `<pf_install>/pingfederate/server/default/conf/cluster-adaptive.conf` file.

For directed clustering, PingFederate shares state information across all nodes, which helps in scenarios where PingFederate is deployed behind a load balancing infrastructure without sticky sessions.

## Related links

* [Account lockout protection](../administrators_reference_guide/pf_account_lockout_protection.html)

* [Password spraying prevention](../administrators_reference_guide/pf_password_spray_prevent.html)

* [Adaptive clustering](pf_adaptiv_cluster.html)

* [Directed clustering](pf_directed_cluster.html)

---

---
title: Active and passive administrative console endpoints
description: The active and passive administrative console endpoints allow an admin to monitor the status of active and passive admin consoles, and promote a passive admin console to the active role.
component: pingfederate
version: 13.1
page_id: pingfederate:server_clustering_guide:pf_active_passive_admin_console_endpoints
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/server_clustering_guide/pf_active_passive_admin_console_endpoints.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 15, 2024
section_ids:
  endpoint-clusterstatus: "Endpoint: cluster/status"
  endpoint-clusteradminnodestatus: "Endpoint: cluster/adminNode/status"
  endpoint-clusteradminnoderoleactive: "Endpoint: cluster/adminNode/role/active"
---

# Active and passive administrative console endpoints

The active and passive administrative console endpoints allow an admin to monitor the status of active and passive admin consoles, and promote a passive admin console to the active role.

Learn more about constructing requests for the following endpoints in the Swagger documentation bundled with PingFederate.

## Endpoint: cluster/status

Returns information about the status of each node in the cluster, including admin nodes and engines.

`HTTP Status: 200`

```json
{
  "nodes": [
    {
      "address": "127.0.0.1:7600",
      "mode": "CLUSTERED_CONSOLE",
      "index": 1,
      "nodeGroup": "node_group_A",
      "version": "12.1",
      "configurationTimestamp": "2024-06-17T17:11:05.442Z",
      "replicationStatus": "SUCCEEDED",
      "adminConsoleInfo": {
        "consoleRole": "ACTIVE",
        "consoleRoleLastUpdateDate": "2024-06-17T17:05:34.461Z",
        "configSyncStatus": "SUCCEEDED",
        "configSyncTimestamp": "2024-06-17T17:11:12.137Z"
    }
  },
    {
    "address": "127.0.0.1:7603",
    "mode": "CLUSTERED_CONSOLE",
    "index": 2,
    "nodeGroup": "node_group_B",
    "version": "12.1",
    "configurationTimestamp": "2024-06-17T17:11:05.442Z",
    "replicationStatus": "SUCCEEDED",
    "adminConsoleInfo": {
      "consoleRole": "PASSIVE",
      "consoleRoleLastUpdateDate": "2024-06-17T16:57:11.811Z",
      "configSyncStatus": "SUCCEEDED",
      "configSyncTimestamp": "2024-06-17T17:11:12.250Z"
    }
  },
  {
    "address": "127.0.0.1:7602",
    "mode": "CLUSTERED_ENGINE",
    "index": 100,
    "nodeGroup": "",
    "version": "12.1",
    "nodeTags": "",
    "configurationTimestamp": "2024-06-17T17:11:05.442Z",
    "replicationStatus": "SUCCEEDED"
  }
],
  "lastConfigUpdateTime": "2024-06-17T17:11:13.000Z",
  "lastReplicationTime": "2024-06-17T17:11:05.442Z",
  "currentNodeIndex": 2,
  "replicationRequired": true,
  "mixedMode": false
}
```

## Endpoint: cluster/adminNode/status

Get this administrative console's role and synchronization status.

`HTTP Status: 200`

```json
{
  "consoleRole": "PASSIVE",
  "consoleRoleLastUpdateDate": "2024-06-17T16:57:11.811Z",
  "configSyncStatus": "SUCCEEDED",
  "configSyncTimestamp": "2024-06-17T17:07:42.243Z"
}
```

## Endpoint: cluster/adminNode/role/active

Update this administrative console node's role to active. Can respond with warnings related to the update process.

`HTTP Status: 200`

```json
{
  "warnings": [
    "Currently no active admin console node in cluster to attempt synchronization with."
  ]
}
```

---

---
title: Active and passive administrative nodes
description: PingFederate allows you to create an active admin console and one or more passive backup admin consoles.
component: pingfederate
version: 13.1
page_id: pingfederate:server_clustering_guide:pf_active_passive_admin_nodes
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/server_clustering_guide/pf_active_passive_admin_nodes.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 15, 2024
---

# Active and passive administrative nodes

PingFederate allows you to create an active admin console and one or more passive backup admin consoles.

The active admin node houses the admin console on which you interact with PingFederate and that governs PingFederate functions.

Passive admin consoles live on alternate server nodes. Their configurations are regularly synchronized to match the configuration of the active admin node.

When passive admin consoles are synchronized, PingFederate copies the changes to configuration and connection files from the active admin console to the passive console nodes, similar to the way [replication](../administrators_reference_guide/pf_replicat_config.html) works. When you promote a passive console to active, it has the same configuration and can seamlessly take over your PingFederate cluster.

Most administrative functions are disabled on passive nodes. The following command line tools are available on passive nodes:

* `calculatehash.sh/.bat`

* `clusterkey.sh/.bat`

* `collect-support-data.sh/.bat`

* `obfuscate.sh/.bat`

* `logfilter.sh/.bat`

* `configkeymgr.sh/.bat`

The following tools will return incorrect results and should not be used on passive nodes:

* `provmgr.sh/.bat`

* `hsmpass.sh/.bat`

* `usercount.sh/.bat`

You can manually promote passive nodes to active status using either the user interface or the admin API.

|   |                                                                                    |
| - | ---------------------------------------------------------------------------------- |
|   | You can only have one active admin console at a time in your PingFederate cluster. |

---

---
title: Adaptive clustering
description: Adaptive clustering automatically distributes session-state information to multiple nodes. Administrators do not have to modify individual configuration files to specify which nodes should participate in tracking user sessions.
component: pingfederate
version: 13.1
page_id: pingfederate:server_clustering_guide:pf_adaptiv_cluster
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/server_clustering_guide/pf_adaptiv_cluster.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 18, 2025
section_ids:
  other-advanced-settings: Other advanced settings
  related-links: Related links
---

# Adaptive clustering

Adaptive clustering automatically distributes session-state information to multiple nodes. Administrators do not have to modify individual configuration files to specify which nodes should participate in tracking user sessions.

In essence, each session receives an address from within an internally-defined range. For redundancy, multiple nodes store each session. These nodes form a replica set. Any node that receives a request and must look up or store session-state information can do so by calculating the address of the session and reaching out to the corresponding replica set.

As individual nodes join and leave the cluster, adaptive clustering redistributes session-state information to maintain the replica set throughout the cluster.

The default size of a replica set is three, which provides redundancy in case two nodes fail and ensures that a single node's slow response time doesn't delay requests. The `replication.factor` setting is in the `<pf_install>/pingfederate/server/default/conf/cluster-adaptive.conf` file.

Enable adaptive clustering by setting the `pf.cluster.adaptive` property in the `run.properties` file to `true`. This is the default state in new installations. For upgrades, if such property is not found or is set to `false`, the system disables adaptive clustering and enables directed clustering instead. To enable or disable adaptive clustering, set the `pf.cluster.adaptive` property to `true` or `false` on each node and then restart PingFederate. The `run.properties` file is in the `<pf_install>/pingfederate/bin` directory.

|   |                                                                                                                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | After making changes to the `cluster-adaptive.conf` and the `run.properties` files, you must manually repeat the changes to all nodes in the cluster. The configuration replication process does not push these files across the cluster. When you are finished, restart PingFederate to apply the changes. |

|   |                                                                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Adaptive clustering doesn't support the SAML 2.0 single logout (SLO) profile using the SOAP binding. If you've configured one or more SAML 2.0 connections to support SLO using SOAP, you must either share all nodes or designate state servers deployment strategies in directed clustering. Learn more in [Directed clustering](pf_directed_cluster.html). |

## Other advanced settings

Fine-tune each runtime state-management service implementation separately by modifying a configuration file located in the `<pf_install>/pingfederate/server/default/conf` directory. After making changes in these files, you must apply the changes to all nodes in the cluster manually.

|   |                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The adaptive clustering concept isn't applicable to the Artifact-Message Persistence and Retrieval Service, which shares messages with any node that requests the message. As needed, you can modify other applicable properties, such as the `rpc.timeout` property. Learn more in [Artifact-Message Persistence and Retrieval Service](pf_artif_mess_persis_retriev_service.html). |

The following tables indicate the configuration file that applies to each implementation and the applicable properties. See the indicated sections for detailed information about each implementation.

**Configuration file and service implementation**

| Configuration file                         | RPC-based service implementation                                                                |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| `cluster-account-locking.conf`             | [Account Locking Service](pf_acc_lock_service.html)                                             |
| `cluster-artifact.conf`                    | [Artifact-Message Persistence and Retrieval Service](pf_artif_mess_persis_retriev_service.html) |
| `cluster-assertion-replay-prevention.conf` | [Assertion Replay Prevention Service](pf_assertion_replay_prevention_service.html)              |
| `cluster-idp-session-registry.conf`        | [IdP Session Registry Service](pf_idp_session_registry_service.html)                            |
| `cluster-inter-request-state.conf`         | [Inter-Request State-Management (IRSM) Service](pf_irsm_service.html)                           |
| `cluster-session-revocation.conf`          | [Back-Channel Session Revocation Service](pf_bac_chann_sess_revoc_service.html)                 |
| `cluster-sp-session-registry.conf`         | [SP Session Registry Service](pf_sp_sess_regist_service.html)                                   |

**Property description**

| Property                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| -------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `rpc.timeout`                                                                          | How long, in milliseconds, this node waits before timing out unresponsive RPC invocations. The default value is `500`, or half a second.                                                                                                                                                                                                                                                                                                                                                                                                       |
| `synchronous.retrieve.majority.only`                                                   | Indicates how many responses to wait for when making synchronous remote procedure calls. When set to `true`, this node waits for the majority of the local replica set to respond. When set to `false`, it waits for all recipients to respond. `true` is the default value.&#xA;&#xA;This property is not applicable to the Account Locking Service and not found in the cluster-account-locking.conf file.                                                                                                                                   |
| `bulk.revoked.sris.timeout` (found only in the `cluster-session-revocation.conf` file) | A node downloads a full revocation list from another node during startup or when it rejoins a cluster after being disconnected from it, for example due to a temporary network issue. This setting determines the amount of time in milliseconds PingFederate waits before aborting the download and reporting a timeout error.The default value is `10000`, which is 10 seconds.                                                                                                                                                              |
| `read.local.only` (found only in the `cluster-session-revocation.conf` file)           | Determines how PingFederate should process queries for revocation status.When set to `true`, PingFederate processes queries for revocation status locally. When set to `false`, the processing node pulls revocation status from other engine nodes in the cluster, subject to the **rpc.timeout** value. `true` is the default value.&#xA;&#xA;When adding a session to the revocation list, the processing node always propagates the information to all engine nodes in the cluster. Learn more in Back-Channel Session Revocation Service. |

|   |                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | When you have enabled adaptive clustering, PingFederate ignores other properties found in these configuration files—namely `preferred.node.indices` and `preferred.node.group.id`. The latter is only in the `cluster-idp-session-registry.conf` file. |

## Related links

* [Deploying cluster servers](pf_deploying_cluster_servers.html)

---

---
title: Artifact-Message Persistence and Retrieval Service
description: PingFederate's Artifact-Message Persistence and Retrieval Service keeps track of one-time keys and associated data compliant with SAML and OAuth 2.0 standards.
component: pingfederate
version: 13.1
page_id: pingfederate:server_clustering_guide:pf_artif_mess_persis_retriev_service
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/server_clustering_guide/pf_artif_mess_persis_retriev_service.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 15, 2023
section_ids:
  group-rpc-based-retrieval: Group RPC-based retrieval
  saml-2-0-indexing-local-memory: SAML 2.0 indexing (local memory)
---

# Artifact-Message Persistence and Retrieval Service

PingFederate's Artifact-Message Persistence and Retrieval Service keeps track of one-time keys and associated data compliant with SAML and OAuth 2.0 standards.

The following standards require PingFederate to relay data to partners using a reference-style data transportation model and to guarantee that the reference keys are valid for one-time use only.

* SAML artifact binding

  PingFederate sends an artifact to the partner when transmitting SAML-outbound messages using the artifact binding. Later, the partner returns to PingFederate to exchange the artifact for the actual message. If the request is valid, PingFederate delivers the message and invalidates the artifact.

* OAuth 2.0 authorization grant type

  When processing an authorization request from an OAuth client that uses the authorization code grant type, PingFederate returns a code to the client based on specification. The client then includes that code in its token request to PingFederate to obtain an access token. If the request is valid, PingFederate delivers the access token and invalidates the code.

The Reference ID Adapter from the [Agentless Integration Kit](https://docs.pingidentity.com/integrations/agentless/pf_agentless_ik.html) also applies the same data transportation model and one-time-use restriction in its drop-off and pick-up operations.

In a standard environment, the PingFederate server saves the data in memory, generates a key for the data, and sends the key to the partner. The Artifact-Message Persistence and Retrieval Service keeps track of the key and the associated data until the partner contacts the PingFederate server to exchange the key for the data.

## Group RPC-based retrieval

When multiple PingFederate servers are deployed to form a cluster, the keys and their data are saved in the server that creates them. Because they are not replicated to other PingFederate servers, it is possible for a key resolution request to arrive at a server that does not contain the requested data. To handle this scenario, the Artifact-Message Persistence and Retrieval Service uses a group Remote Procedure Call (RPC) retrieval approach, where the server handling the key resolution request determines the data-hosting server based on the key value and contacts the appropriate server to retrieve the requested data. This group RPC implementation is compatible with the SAML artifact binding, the OAuth 2.0 authorization code grant type, and the Reference ID Adapter.

|   |                                                                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The Artifact-Message Persistence and Retrieval Service also supports a local memory approach for SAML 2.0. This approach is only suitable in clustered environments where the OAuth 2.0 authorization code grant type and the Reference ID Adapter are not in use. |

When PingFederate is in clustered mode, the service proxy selects a group RPC-based implementation, which takes advantage of node indexing but not the preferred-nodes concept. Sticky-session load-balancing strategies are not effective when the key request and its subsequent key resolution request can come from different locations.

Although this implementation does not take advantage of adaptive clustering or the preferred-nodes concept, you can configure the RPC time-out in the `<pf_install>/pingfederate/server/default/conf/cluster-artifact.conf` file.

## SAML 2.0 indexing (local memory)

A SAML 2.0 federation entitycan support multiple artifact resolution services, each identified by a unique index number. Artifacts include this index, and a federation partner must send the artifact resolution request to the appropriate endpoint for that index. This means that servers do not need to share information concerning the artifact.

With this approach, partners must know about each of your backend servers. Generally, this means providing partners with a list that includes multiple artifact-resolution service endpoints with the corresponding indices.

|   |                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingFederate does not automatically generate this information; an administrator must create it and send it to partners who are using the artifact binding. |

For example, if you have four servers in a cluster, the list might look like this:

```
<ArtifactResolutionService Binding="..." Location="https://node1/idp/ARS.ssaml2" index="1"/>
<ArtifactResolutionService Binding="..." Location="https://node2/idp/ARS.ssaml2" index="2"/>
<ArtifactResolutionService Binding="..." Location="https://node3/idp/ARS.ssaml2" index="3"/>
<ArtifactResolutionService Binding="..." Location="https://node4/idp/ARS.ssaml2" index="4"/>
```

In this case, the index corresponds to the node index configured in the `run.properties` file on each individual server. This service encodes the node index in the artifact handle when running in a clustered mode (it will always use an index of `0` in standalone mode).

Partners also need direct access to each ARS endpoint, which can complicate your configuration of load balancers, proxies, and firewalls. This approach cannot be used for SAML 1.x, or with adapters that utilize PingFederate's artifact-data management.

To use this approach for SAML 2.0 federation deployments, edit the `<pf_install>/pingfederate/server/default/conf/service-points.conf` file and change the implementation for the `artifact.store` service point to the class name `org.sourceid.saml20.service.impl.localmemory.ArtifactPersistenceServiceMapImpl`.

---

---
title: Assertion Replay Prevention Service
description: The Assertion Replay Prevention Service tracks POST assertions to prevent replay.
component: pingfederate
version: 13.1
page_id: pingfederate:server_clustering_guide:pf_assertion_replay_prevention_service
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/server_clustering_guide/pf_assertion_replay_prevention_service.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 17, 2026
section_ids:
  related-links: Related links
---

# Assertion Replay Prevention Service

The Assertion Replay Prevention Service tracks POST assertions to prevent replay.

SAML standards specify that when a service provider (SP) *(tooltip: \<div class="paragraph">
\<p>In SAML, an entity that receives and accepts an authentication assertion issued by an IdP, typically for the purpose of allowing access to a protected resource.\</p>
\</div>)* receives assertions from the POST binding, the SP should keep track of each assertion for the duration of its validity to ensure that it is not replayed (that is, intercepted by a third party and re-posted). For OAuth and OpenID Connect, PingFederate can mandate a unique signed JSON Web Token (JWT) *(tooltip: \<div class="paragraph">
\<p>An IETF standard container format for a JSON object used for the secure exchange of content, such as identity or entitlement information. You can find the industry standard in \<a href="https\://datatracker.ietf.org/doc/html/rfc7519">RFC 7519\</a>.\</p>
\</div>)* from the client for each request when the client is configured to authenticate with the private\_key\_jwt or client\_secret\_jwt client authentication method. PingFederate delegates these responsibilities to the Assertion Replay Prevention Service.

When PingFederate is in clustered mode, the service proxy uses a group RPC-based, preferred-nodes implementation. The configuration file is `<pf_install>/pingfederate/server/default/conf/cluster-assertion-replay-prevention.conf`.

The Assertion Replay Prevention Service supports both adaptive clustering and directed clustering.

For adaptive clustering, PingFederate shares token (assertion or JWT) information with a replica set. If region identifiers are defined, PingFederate shares token information among multiple replica sets across regions. You can optionally override this default behavior in the configuration file for adaptive clustering.

For directed clustering, you must choose between the sharing all nodes and designating state servers deployment strategies in directed clustering for this service.

The service proxy uses the class `org.sourceid.saml20.service.impl.grouprpc.AssertionReplayPreventionServiceGroupRpcImpl`.

Unlike other services, the Assertion Replay Prevention Service fulfills only a security condition, rather than supporting normal SSO functionality, because there might be situations where the priority placed on cluster performance outweighs the priority placed on this security check. If you are in this situation, you have the option to change the implementation for the service point `AssertionReplayPreventionService` in the `<pf_install>/pingfederate/server/default/conf/service-points.conf` file to one of these classes:

* `org.sourceid.saml20.service.impl.localmemory.AssertionReplayPreventionSvcInMemoryImpl`

  This is the implementation used in standalone mode. It performs all the appropriate replay checks but does not share any data with other nodes. A replay attempt routed to the same server node would fail, but other nodes would not have sufficient information to stop the transaction.

* `org.sourceid.saml20.service.impl.localmemory.AssertionReplayPreventionServiceNullImpl`

  This implementation disables assertion-replay prevention. Use with caution when performance is an absolute priority.

## Related links

* [Adaptive clustering](pf_adaptiv_cluster.html)

* [Directed clustering](pf_directed_cluster.html)

---

---
title: Back-Channel Session Revocation Service
description: PingFederate uses the Back-Channel Session Revocation Service to provide OAuth clients the capabilities to add sessions to the revocation list and to query the revocation status.
component: pingfederate
version: 13.1
page_id: pingfederate:server_clustering_guide:pf_bac_chann_sess_revoc_service
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/server_clustering_guide/pf_bac_chann_sess_revoc_service.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  fifo-memory-management-scheme: FIFO memory management scheme
  related-links: Related links
---

# Back-Channel Session Revocation Service

PingFederate uses the Back-Channel Session Revocation Service to provide OAuth clients the capabilities to add sessions to the revocation list and to query the revocation status.

When PingFederate is in clustered mode, the service proxy uses a group remote procedure call (RPC)-based implementation. When adding a session to its revocation list, the processing node always propagates the information to all engine nodes in the cluster. This allows you to choose whether queries are processed locally or after collecting information from other engine nodes.

Processing queries locally results in faster response times for engine nodes in well-connected networks. Requiring data from other engine nodes adds a layer of protection against inconsistency among engine nodes revocation lists due to network outages.

You can configure the RPC timeout and other settings in the `<pf_install>/pingfederate/server/default/conf/cluster-session-revocation.conf` file.

The service proxy uses the class `org.sourceid.saml20.service.impl.grouprpc.SessionRevocationServiceGroupRpcImpl`.

You can store Session Revocation Service data in a Redis cache, which will retain the data during upgrades or in case of a cluster restart. Learn more in [Storing PingFederate data with Redis](../administrators_reference_guide/pf_storing_pf_data_redis.html).

## FIFO memory management scheme

To ensure the revocation list does not result in excessive memory usage, the Back-Channel Session Revocation Service employs a First-In, First-Out (FIFO) algorithm to purge old data. When the maximum size is reached, the oldest entries are automatically removed.

The maximum number of sessions is configurable by the `SessionRevocationServiceMapImpl.max.revoked.sris` setting in the `<pf_install>/pingfederate/server/default/conf/size-limits.conf` file. The default value is `50000`.

The FIFO memory manager operates in addition to the **Session Revocation Lifetime** setting, which is globally configured in the **Authentication > Sessions** menu.

## Related links

* [Back-Channel Session Revocation](../administrators_reference_guide/pf_backchannel_sess_revocat.html)

* [Session Revocation API endpoint](../developers_reference_guide/pf_session_revocation_api_endpoint.html)

* [Runtime state-management architectures](pf_runtime_state_manage_achitec.html)

* [Configuring authorization server settings](../administrators_reference_guide/help_authorizationserversettingstasklet_oauthauthorizationserversettingsstate.html)

---

---
title: Cluster protocol architecture
description: PingFederate's cluster-protocol services manage discovery, cluster messaging, connectivity failure detection, membership, and merging of split clusters.
component: pingfederate
version: 13.1
page_id: pingfederate:server_clustering_guide:pf_cluster_protoc_architec
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/server_clustering_guide/pf_cluster_protoc_architec.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  cluster-discovery: Cluster discovery
  failure-detection: Failure detection
---

# Cluster protocol architecture

PingFederate's cluster-protocol services manage discovery, cluster messaging, connectivity failure detection, membership, and merging of split clusters.

|   |                                                                                                                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Nodes in the cluster must be able to communicate with one another over both the cluster bind port and the cluster failure detection port. This communication requirement remains true regardless of the chosen cluster discovery method or runtime state-management architecture. |

## Cluster discovery

PingFederate supports two cluster discovery methods.

* Static discovery

  Static discovery is suitable for a small cluster with about five to six engine nodes. Configuration requires no external component. You must configure each node with at least one expected node in a cluster. In practice, the initial discovery list should contain all nodes known in advance in the cluster, including itself, to increase the likelihood of new members finding and joining the cluster.

* Dynamic discovery

  Dynamic discovery is well-suited for environments where traffic volume may spike and require additional resources during peak hours. Instead of configuring a static list of known nodes ahead of time, configure new nodes to pull cluster membership information from a centralized repository. Because safe storage and ready accessibility of the information by all nodes is crucial, PingFederate supports IAM roles for Amazon Elastic Compute Cloud (Amazon EC2), Amazon Simple Storage Service (Amazon S3), and OpenStack Swift. The dynamic discovery method requires only a one-time setup. Once configured, maintaining a static discovery list requires no coordination effort.

Regardless of the discovery method, as individual nodes join and leave the cluster, the cluster-protocol service synchronizes the new membership information across all nodes.

## Failure detection

The failure detection mechanism detects network connectivity failures by establishing TCP connections with other nodes at their cluster failure detection ports and sending occasional network messages. When a node detects a failure, it propagates the condition to other nodes, sharing new membership information across the cluster.

|   |                                                                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | If you deploy any networking devices, such as a firewall, between nodes, you must configure them to allow inbound TCP connections to the cluster failure detection ports, and not to terminate these connections based on their potentially low volumes of network activities. |

---

---
title: Configuration synchronization
description: All nodes in a PingFederate clustered environment must have the same configuration settings, as set through the administrative console. You can use any of the following methods to ensure that configuration data is synchronized on all cluster nodes.
component: pingfederate
version: 13.1
page_id: pingfederate:server_clustering_guide:pf_config_synchroniz
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/server_clustering_guide/pf_config_synchroniz.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
---

# Configuration synchronization

All nodes in a PingFederate clustered environment must have the same configuration settings, as set through the administrative console. You can use any of the following methods to ensure that configuration data is synchronized on all cluster nodes.

* Push from the administrative console.

* Deploy configuration archive.

* Make a RESTful API call to the `/cluster` administrative API endpoint.

* Make a web service call to the `/pf-mgmt-ws/ws/ConfigReplication` Connection Management Service endpoint.

|   |                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Changes made directly to configuration files must be replicated manually across the cluster, as applicable. If the PingFederate servers are running, you must restart them after you replicate the changes. |

---

---
title: Configuration-archive deployment
description: Uploading configuration archives is an alternate method of copying configurations to clustered PingFederate servers.
component: pingfederate
version: 13.1
page_id: pingfederate:server_clustering_guide:pf_config_archiv_deploy
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/server_clustering_guide/pf_config_archiv_deploy.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 5, 2023
section_ids:
  runtime-state-management-services: Runtime state-management services
---

# Configuration-archive deployment

Uploading configuration archives is an alternate method of copying configurations to clustered PingFederate servers.

After you configure or reconfigure the console, you can also update cluster nodes by downloading a configuration archive from the **System > Server > Configuration Archive** window and then deploying it either manually or using a scripted process to the `<pf_install>/pingfederate/server/default/data/drop-in-deployer` directory on each cluster node or provisioning-failover server.

To enable automatic replication of a configuration data archive to server nodes, you must enable the `replicate.after.drop.in.deploy` attribute in the `cluster-config-replication.conf` file to `true`. Learn more in [Upgrading configuration data](../upgrading_pingfederate/pf_upgrading_config_data.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you use the drop-in deployment process:- To ensure successful importation of the configuration archive file with this process, you must rename the file `data.zip`.

- If the data archive is from an older version, PingFederate will automatically upgrade archive data to be compatible with the current version. Learn more in [Upgrading configuration data](../upgrading_pingfederate/pf_upgrading_config_data.html).

- On startup, the heartbeat endpoint will not return `200` until the archive import completes. If you have configured a health check or probe that can trigger a restart of the server, crash loop behavior can result. Review the configuration of these checks to ensure time thresholds are set appropriately. |

A configuration archive contains the same information sent during the [configuration push](pf_console_config_push.html) from the administrative console.

## Runtime state-management services

If you have configured one of the following runtime state-management services on the engine nodes, you must manually migrate the configuration files to the engine nodes. The configuration files are locted at `<pf_install>/pingfederate/server/default/conf`

**Configuration file and service implementation**

| Configuration file                         | RPC-based service implementation                                                                |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| `cluster-account-locking.conf`             | [Account Locking Service](pf_acc_lock_service.html)                                             |
| `cluster-artifact.conf`                    | [Artifact-Message Persistence and Retrieval Service](pf_artif_mess_persis_retriev_service.html) |
| `cluster-assertion-replay-prevention.conf` | [Assertion Replay Prevention Service](pf_assertion_replay_prevention_service.html)              |
| `cluster-idp-session-registry.conf`        | [IdP Session Registry Service](pf_idp_session_registry_service.html)                            |
| `cluster-inter-request-state.conf`         | [Inter-Request State-Management (IRSM) Service](pf_irsm_service.html)                           |
| `cluster-session-revocation.conf`          | [Back-Channel Session Revocation Service](pf_bac_chann_sess_revoc_service.html)                 |
| `cluster-sp-session-registry.conf`         | [SP Session Registry Service](pf_sp_sess_regist_service.html)                                   |

---

---
title: Configuring active and passive administrative nodes
description: Learn how to configure active and passive admin consoles in the admin UI.
component: pingfederate
version: 13.1
page_id: pingfederate:server_clustering_guide:pf_configuring_active_passive_admin_nodes
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/server_clustering_guide/pf_configuring_active_passive_admin_nodes.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 23, 2026
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
---

# Configuring active and passive administrative nodes

Learn how to configure active and passive admin consoles in the admin UI.

## Before you begin

If you're upgrading from a single-console cluster to a cluster with active and passive consoles:

* Make a copy of the original console to use in creating passive consoles. This ensures that the passive consoles have the same configuration data archive as the original console, which reduces the size of the initial synchronization. This is similar to exporting and importing a [configuration archive](../administrators_reference_guide/help_configurationarchivetasklet_selectimportexportstate.html).

* Delete the `pingfederate/server/default/data/instance/admin-node-mode.xml` file from the new passive node, if it exists.

* Because the synchronization action only copies over configuration and license settings, similar to replication engines, you must manually adjust the properties and configuration files for the passive nodes.

## About this task

To configure active and passive admin consoles:

## Steps

1. Edit the clustering properties of each node in the `<pf_install>/pingfederate/bin/run.properties` file.

   |   |                                                                                                                                                                                                           |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You must update the `pf.cluster.node.index` property for each passive console. If you use the static discovery list, you must also update the list to include the new index values for each passive node. |

   Learn more in [Deploying cluster servers](pf_deploying_cluster_servers.html).

2. Enable and configure active and passive admin consoles in the `pingfederate/server/default/conf/cluster-admin-nodes-sync.conf` file.

   |   |                                                                                                                    |
   | - | ------------------------------------------------------------------------------------------------------------------ |
   |   | Review each property in this file to make sure the values for each node are correctly configured for your cluster. |

   The following table describes each file property:

   | Property                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | `enabled`                                         | Whether the active/passive admin nodes feature is enabled.Values are `true` or `false`.                                                                                                                                                                                                                                                                                                                                                                                         |
   | `passive.node.data.sync.interval.secs`            | The interval in seconds between requests from the passive node to the active node to pull the saved configuration.The default value is `10`.                                                                                                                                                                                                                                                                                                                                    |
   | `rpc.synchronization.data.timeout.milliseconds`   | The time in milliseconds before a data synchronization request times out.The default value is `20000`.                                                                                                                                                                                                                                                                                                                                                                          |
   | `passive.node.configuration.reload.interval.secs` | The interval in seconds between configuration reloads on a passive node.The reload process locks the admin console from performing other tasks, and the process can be time-consuming, so reloads are not performed after every synchronization.Reloads are performed periodically to allow you to discover configuration issues from the `server.log` file, if they arise.This value should be greater than `passive.node.data.sync.interval.secs`.The default value is `300`. |
   | `active.node.last.successful.sync.warning`        | The interval in seconds since the active node's last successful synchronization with a passive node before a warning is issued on the active admin console.This value should be greater than the value for `passive.node.data.sync.interval.secs`.The default value is `25`.                                                                                                                                                                                                    |

3. (Optional) If you're planning a fresh setup of PingFederate with active and passive admin consoles and hardware security modules (HSMs):

   1. Decide which passive console will become active.

   2. Start the designated passive console.

   3. Switch the designated passive console to become active.

      Refer to step 5 or [Active and passive administrative console endpoints](pf_active_passive_admin_console_endpoints.html) for instructions on switching a passive console to active.

   4. After the active console is started, start the remaining consoles.

      This ensures that the passive consoles can retrieve the default SSL server certificate from the active console so that passive consoles can start successfully.

4. For new installations of PingFederate, run the initial setup wizard on the node that you want to make active when you first start your cluster.

   Learn more in [Setting up PingFederate](../getting_started_with_pingfederate/pf_setting_up_pf.html).

   |   |                                                                                                                                                                                                                                                                                                        |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Run the initial setup wizard only on the passive node that you intend to make active.After the wizard completes, it will automatically switch the console you run it on to an active node. Because you can only have one active admin node at a time, do not run the wizard on multiple passive nodes. |

5. For existing PingFederate installations, switch a node to active mode:

   1. Make sure the active/passive admin nodes feature is enabled in all of the admin nodes by setting the `enabled` parameter to `true` in the `pingfederate/server/default/conf/cluster-admin-nodes-sync.conf` file on each node.

   2. Go to the UI of the admin console you want to make active. PingFederate will direct you to the **Cluster Management** page.

   3. Click **Switch to Active**.

---

---
title: Configuring multi-region support
description: Define region identfiers and configure cross-region settings for multi-region PingFederate server clusters.
component: pingfederate
version: 13.1
page_id: pingfederate:server_clustering_guide:pf_config_multi_region_supp
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/server_clustering_guide/pf_config_multi_region_supp.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  steps: Steps
  example: Example:
  result: Result:
---

# Configuring multi-region support

Define region identfiers and configure cross-region settings for multi-region PingFederate server clusters.

## Steps

1. To define a region identifier for a given node, update the `node.group.id` value in the `<pf_install>/pingfederate/server/default/conf/cluster-adaptive.conf` file, which is a per-server configuration.

   ### Example:

   For example, if you have five engine nodes in the West Coast and six engine nodes in the East Coast, you can update the `node.group.id` value to `W` for each of the West Coast nodes and `E` for each of the six nodes in the East Coast.

   1. Restart PingFederate after making changes to the `cluster-adaptive.conf` file.

      ### Result:

      Once defined, the identifiers for all nodes are displayed on the **System > Server > Cluster Management** menu.

2. To configure cross-region support for individual areas, follow the inline instructions in the `cluster-adaptive.conf` file to update the relevant setting values.

---

---
title: Console configuration push
description: When multiple PingFederate servers are set up to run as a cluster, the administrative console provides a Cluster Management window.
component: pingfederate
version: 13.1
page_id: pingfederate:server_clustering_guide:pf_console_config_push
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/server_clustering_guide/pf_console_config_push.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
---

# Console configuration push

When multiple PingFederate servers are set up to run as a cluster, the administrative console provides a **Cluster Management** window.

Whenever applicable changes are made through the administrative console, a message appears at top of the console as a reminder to go to the **Cluster Management** window and to replicate the current console configuration to all server nodes in the cluster.

|   |                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You must also use the **Replicate Configuration** window to initiate the transmission of the license file from the console node to all server nodes. |

The **Cluster Management** window is also useful for verifying the current member servers of your PingFederate cluster.

---

---
title: Defining subclusters
description: Subclustering improves efficient scaling by limiting session-state communication to other nodes within a subcluster.
component: pingfederate
version: 13.1
page_id: pingfederate:server_clustering_guide:pf_defining_subclust
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/server_clustering_guide/pf_defining_subclust.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: March 23, 2023
---

# Defining subclusters

Subclustering improves efficient scaling by limiting session-state communication to other nodes within a subcluster.

Node indices can be configured to divide a cluster into subgroups, or subclusters, of a few nodes each. Using this configuration, each node in a subcluster shares session-state information only with other members of the subcluster. This approach requires a network traffic management solution to persist, or stick, user sessions so that each subsequent request from the same user is directed to the same set of nodes.

The advantage of this approach is that cluster throughput scales more linearly, because the creation of an additional subcluster will not degrade the performance of any other group.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The underlying cluster protocol still requires that all nodes are able to communicate with one another. The topology here is only an optimization for the runtime state-management services that support the concept of preferred nodes.Additionally, this architecture does not support OpenID Connect back-channel logout or the SAML 2.0 single logout (SLO) profile using the SOAP binding. If you need to use either of these capabilities, you must choose between sharing all nodes and designating state servers deployment strategies in directed clustering.This architecture also does not support the capability to revoke sessions after password change or reset. If you are using this capability, you are limited to the sharing all nodes and designating state servers deployment strategies. |

The following diagram illustrates the subcluster approach.

![Runtime state-management architecture: Defining subclusters](_images/bxn1564003647639.png)

In this example, the `preferred.node.indices` property of each server in the cluster lists the indices of all nodes in its subgroup (including itself). Requests are directed to all nodes but the load balancer directs user sessions to the same subcluster.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When PingFederate acts as an OAuth authorization server (AS) and the access token management instance uses a reference token data model, the resource server (RS) must send a request to PingFederate to de-reference the access token for the corresponding identity and security information. Because the OAuth clients and the RS send their requests separately, PingFederate shares reference token information among all engine nodes despite any state server or subcluster setup. |

---

---
title: Deploying cluster servers
description: A PingFederate cluster consists of multiple nodes, each of which are likely running on a dedicated host system.
component: pingfederate
version: 13.1
page_id: pingfederate:server_clustering_guide:pf_deploying_cluster_servers
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/server_clustering_guide/pf_deploying_cluster_servers.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 23, 2026
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result
---

# Deploying cluster servers

A PingFederate cluster consists of multiple nodes, each of which are likely running on a dedicated host system.

## About this task

In a cluster, there are two types of nodes: engine nodes and administrative console nodes. Engine nodes service end-user traffic, and multiple nodes are recommended to ensure high availability for your deployment. Only one administrative console node can be active in a given cluster. This node provides the user interface and administrative API that you can use to configure the cluster. Additionally, the administrative console node manages the following runtime functions:

* Performing periodic configuration archive backup

* Cleaning expired persistent authentication sessions

* Cleaning expired access grants

* Updating connections from metadata URLs, including PingOne SP connections if configured, and sending email notifications

* Performing automatic rotation of signing certificates if enabled

|   |                                                                                                                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Additional steps are required to set up failover for provisioning. If you are grouping servers exclusively to provide for provisioning failover, skip these steps and refer to [Deploy provisioning failover](pf_deploy_provis_failover.html). |

These steps describe how to configure and deploy clustered PingFederate servers by editing each node in the `<pf_install>/pingfederate/bin/run.properties`.

## Steps

1. Install PingFederate on each server in a cluster.

2. Edit the clustering properties of each node in the `<pf_install>/pingfederate/bin/run.properties` file. The following table provides information about each property:

   | Property                                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | `pf.operational.mode`                                           | Controls the operational mode of the PingFederate server. PingFederate supports the following modes:- `STANDALONE` (default)

     This server is a standalone instance that operates as the administrative console and runtime engine.&#xA;&#xA;The value STANDALONE should only be used in a cluster where session-state management is not needed for any reason and configuration-archive deployment is used as the configuration synchronization method.- `CLUSTERED_CONSOLE`

     This server is part of a cluster and operates only the administrative console.

     &#xA;&#xA;By default, only one node in a cluster can run the administrative console. If the active/passive admin nodes feature is enabled, you can have more than one CLUSTERED\_CONSOLE.

   - `CLUSTERED_ENGINE`

     This server is part of a cluster and operates only as the runtime engine.                                                                                                                                                                                                                                                                                                                            |
   | `pf.cluster.node.index`                                         | Defines a unique index number for the server in a cluster. The index number is used to identify peers and optimize inter-node communication. The allowed range is `0` - `65535`.If no value is set for the node index, the system assigns an auto-generated value in the range of `0` to `2147483647`.This property has no default value. If you specify an index number, you can configure instances of the Cluster Node Authentication Selector and place them in authentication policies to customize authentication requirements based on the runtime node servicing a request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
   | `pf.cluster.auth.pwd`                                           | Sets the password that each node in the cluster must use to authenticate when joining the cluster. This prevents unauthorized nodes from joining a cluster. You can leave this value blank, but all nodes in the cluster must have the same value.You can also use the obfuscate utility to obfuscate your password. Learn more in [Configuring forward proxy server settings](../administrators_reference_guide/pf_configure_forward_proxy_server_settings.html).&#xA;&#xA;Consider using a randomly-generated password with 22 or more alphanumeric characters. A strong, obfuscated, Jgroups cluster password can be generated with the clusterkey utility (clusterkey.bat for Windows and clusterkey.sh for Linux), located in the \<pf\_install>/pingfederate/bin directory.All nodes in a cluster must share the same value, blank or otherwise.                                                                                                                                                                                                                                                                                                                                      |
   | `pf.cluster.encrypt`                                            | Indicates whether to encrypt network traffic sent between nodes in a cluster. The possible values are `true` or `false` (default).When set to `true`, communication within the cluster is encrypted with a symmetric key derived from the value of the `pf.cluster.auth.pwd` property.&#xA;&#xA;When the pf.cluster.encrypt property is set to true, you must provide a value for the pf.cluster.auth.pwd property. Otherwise PingFederate aborts during its startup process.All nodes in a cluster must have the same value for this property.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
   | `pf.cluster.encryption.keysize`                                 | The length of the key that PingFederate takes into consideration when deriving the symmetric key from the value of the `pf.cluster.auth.pwd` property for the purpose of encrypting network traffic sent between nodes in a cluster. Required only when the `pf.cluster.encrypt` is set to `true`.All nodes in a cluster must have the same value set for this property.The default value is `128`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
   | `pf.cluster.bind.address`                                       | Defaults to `NON_LOOPBACK`, which leaves the system to choose an available non-loopback IP address. Alternatively, enter an IP address of the network interface to which the cluster communication should bind. For machines with more than one network interface, provide a specific IP address.You can use this property to increase performance (particularly with UDP) and improve security by segmenting cluster-communication traffic onto a private network or VLAN.&#xA;&#xA;Besides NON\_LOOPBACK or an IP address, you can also use other values supported by JGroups. For more information, see the bind\_addr special values in JGroups documentation.	&#xA;&#xA;This field doesn't support DNS name. Use the default value NON\_LOOPBACK or replace it with an IP address.                                                                                                                                                                                                                                                                                                                                                                                                     |
   | `pf.cluster.bind.port`                                          | Specifies the port associated with the `pf.cluster.bind.address` property or with the default network interface used.This is the port used by other cluster members during their discovery process, usually via the `pf.cluster.tcp.discovery.initial.hosts` property.The default value is `7600`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
   | `pf.cluster.failure.detection.bind.port`                        | Indicates the bind port of a server socket that's opened on the given node and used by other nodes as part of the cluster's failure-detection mechanisms. If set to `0` or unspecified, a random available port is used. The default value is `7700`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   | `pf.cluster.transport.protocol`                                 | Indicates the transport protocol used for cluster communication. Values are `udp` or `tcp`. The default value is *tcp*. All nodes in a cluster must have the same value set for this property.Use UDP when IP multicasting is enabled in the network environment and the majority of cluster traffic is point-to-full-group. You must also configure both the `pf.cluster.mcast.group.address` and `pf.cluster.mcast.group.port` properties.Use TCP for geographically dispersed servers or when multicast isn't available or disabled for some other reason. For example, when using routers that don't support multicast messaging. TCP might also be appropriate if your cluster configuration employs more point-to-point or point-to-few messaging than point-to-group.You must also configure the `pf.cluster.tcp.discovery.inital.hosts` property.&#xA;&#xA;This property is a reference to a protocol-stack XML configuration file located in the \<pf\_install>/pingfederate/server/default/conf/ directory. Two stacks are provided: one for UDP multicast and one for TCP. You can customize either stack or add to it as needed by modifying the associated configuration file. |
   | `pf.cluster.mcast.group.address`                                | Defines the IP address shared among nodes in the same cluster for UDP multicast communication; required when UDP is set as the transport protocol. The valid range is `224.0.0.0` - `239.255.255.255`. Some addresses in this range are reserved for other purposes. This property is not used for TCP.All nodes in a cluster must have the same value set for this property.The default value is *239.16.96.69*.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   | `pf.cluster.mcast.group.port`                                   | Defines the port in conjunction with the `pf.cluster.mcast.group.address` property value. This property is not used for TCP configurations.All nodes in a cluster must have the same value set for this property.The default value is `7601`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
   | `pf.cluster.tcp.discovery.initial.hosts`                        | Designates a static list of PingFederate servers to be contacted for cluster membership information when discovering, joining, and rejoining the cluster. This value is required when TCP is set as the transport protocol. The value is a comma-separated list of host names (or IP addresses) and their cluster bind ports, for example, `host1[7600],10.0.1.4[7600],host7[1033],10.0.9.45[2231]`.When using static discovery, add at least one node for the cluster to know in advance. This property should contain all nodes in the cluster (including itself) to increase the likelihood of new members finding and joining the cluster.When using dynamic discovery, leave this property blank and enable dynamic discovery in the `<pf_install>/pingfederate/server/default/conf/tcp.xml` file. Learn more in [Enabling dynamic discovery for clustering](pf_enabling_dynamic_discovery_clustering.html).                                                                                                                                                                                                                                                                           |
   | `pf.cluster.adaptive`                                           | Indicates whether runtime state-management services should use the adaptive clustering architecture.The default value is `true` for new installations and `false` for upgrades.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
   | `pf.cluster.diagnostics.enabled`                                | `false` turns off JGroups diagnostics. `true` turns it on.The default value is `false`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   | `pf.cluster.diagnostics.addr` and `pf.cluster.diagnostics.port` | The multicast address and port this node listens on for diagnostic messages.The default values are `224.0.75.75` and `7500`, respectively. Do not change the default values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
   | `node.tags`                                                     | Defines the tags associated with this node.Configuration is optional. When configured, PingFederate considers this property when processing requests. For example, you can use tags to determine the datastore location that this PingFederate node communicates with. You can also use tags in conjunction with authentication selectors and policies to define authentication requirements.Node tags only apply to engine nodes (CLUSTERED\_ENGINE). If you configure a node tag for the admin node (CLUSTERED\_ADMIN), it won't appear in the **Cluster Management** overview\.You can specify one tag.```
   node.tags=north
   ```You can also specify a list of prioritized, space-separated tags.```
   node.tags=1 123 234
   ```Tags can't contain spaces.                                                                                                                                                                                                                                                                                                                                                                                                                                     |

3. (Optional) Edit configuration files in each node that control the cluster protocol and runtime state-management service. For more information, see [Runtime state-management architectures](pf_runtime_state_manage_achitec.html) and [Runtime state-management services](pf_runtime_state_manage_serv.html).

4. (Optional) If outbound provisioning is configured for your site and you want to provide failover capabilities, identify and configure the provisioning failover nodes. For more information, see [Deploy provisioning failover](pf_deploy_provis_failover.html).

5. Start or restart PingFederate on all nodes.

6. Sign on to the administrative console.

7. If you haven't done so, import your PingFederate license. Learn more in [License management](../administrators_reference_guide/help_licensemanagementtasklet_licensemanagementstate.html).

8. On the **System > Server > Cluster Management** page, click **Replicate Configuration** to push the license information from the console node to all engine nodes.

## Result

After you set up the clustered environment, you can start configuring PingFederate through the administrative console. When PingFederate detects a change, it prompts you to replicate the configuration to all engine nodes.

---

---
title: Deploying provisioning failover
description: After configuring outbound provisioning, you can set up one or more PingFederate failover servers specifically for provisioning backup.
component: pingfederate
version: 13.1
page_id: pingfederate:server_clustering_guide:pf_deploy_provis_failover
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/server_clustering_guide/pf_deploy_provis_failover.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 8, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Deploying provisioning failover

After configuring outbound provisioning, you can set up one or more PingFederate failover servers specifically for provisioning backup.

## About this task

Provisioning runtime processing and failover is independent of single sign-on (SSO) or single logout (SLO) runtime processing and server clustering. However, if you are already deploying, or have deployed, a cluster for federation-protocol runtime processing, you can use a subset of those servers for provisioning failover. Alternatively, you can mix the configuration or set up provisioning-failover servers independently.

|   |                                                                                             |
| - | ------------------------------------------------------------------------------------------- |
|   | Each server in the failover network must be configured to use the same relational database. |

|   |                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Use the built-in HSQLDB only for trial or training environments. For testing and production environments, always use a secured external storage solution for proper functioning in a clustered environment.Testing involving HSQLDB is not a valid test. In both testing and production, it might cause various problems due to its limitations and HSQLDB involved cases are not supported by Ping Identity. |

## Steps

1. Select two or more runtime instances of PingFederate to configure for provisioning failover.

2. For each server instance, edit provisioning properties in the `<pf_install>/pingfederate/bin/run.properties` file as follows:

   | Property                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   | ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | `pf.provisioner.mode`                | The status of outbound provisioning. Allowed values are:- `OFF` (default)

     Outbound provisioning is disabled.

   - `STANDALONE`

     Provisioning is enabled, without failover.

   - `FAILOVER`

     Provisioning is enabled, with failover.

     &#xA;&#xA;The value STANDALONE cannot be used for failover configuration. This property must be set to FAILOVER on the primary and secondary servers.                                                                                                                                                                                                                                                                                                                                                                                                             |
   | `provisioner.node.id`                | The unique index number of the provisioning server.Each server must have a unique index number, which is used to prioritize which server is currently active and which is next in line in case of a failure. Values are any number.If no `provisioner.node.id` value is specified, PingFederate will use the `pf.cluster.node.index` value as the provisioner node ID.If no `pf.cluster.node.index` is specified, PingFederate will automatically generate an index.&#xA;&#xA;The primary active primary server should have an index number of 1. The lowest value in the environment becomes the primary.&#xA;&#xA;These node IDs are not required to start at 1, but it is recommended that they start at 1. The number must not exceed the maximum integer value supported by Java, which is 2147483647. |
   | `provisioner.failover. grace.period` | The time interval (in seconds) between the first indication that a node is dead and failover to the next server in line. The time period should be greater than the **Synchronization Frequency** set in the **System > Server > Protocol Settings > Outbound Provisioning** tab on the administrative console.The default value is `600`, which is 10 minutes.                                                                                                                                                                                                                                                                                                                                                                                                                                             |

   |   |                                                                                                                                                                                                                                                                     |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You must seperately configure the failover properties in the `run.properties` file on each provisioning server, because the `run.properties` file is not copied among the provisioning servers automatically or as part of the **Replicate Configuration** process. |

3. Start or restart all of the PingFederate servers.

4. If you have not already done so, set up an external database to facilitate provisioning and then update the **Provisioning Data Store** setting on the **System > Server > Protocol Settings > Outbound Provisioning** tab. See [Configuring outbound provisioning settings](../administrators_reference_guide/pf_configuring_outbound_provisioning_settings.html) for more information.

5. After configuration, if the provisioning servers belong to the same PingFederate clustered environment, go to the **System > Server**. In the **Cluster Management** window, replicate the new **Provisioning Data Store** setting to all nodes. If the provisioning servers are individual PingFederate servers, for each provisioning server, create a datastore connection to the same external database and update the **Provisioning Data Store** setting manually.

---

---
title: Designating state servers
description: A state servers clustering deployment model improves scalabiltity by reducing communication between nodes.
component: pingfederate
version: 13.1
page_id: pingfederate:server_clustering_guide:pf_design_state_server
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/server_clustering_guide/pf_design_state_server.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 2, 2024
---

# Designating state servers

A state servers clustering deployment model improves scalabiltity by reducing communication between nodes.

You can select a few engine nodes as state servers. This deployment approach scales better than the all-nodes approach because additional nodes do not require connections to every existing node, they only require a connection between each server and each state server.

Configure this deployment by setting the `preferred.node.indices` of other servers in a group to those of the state servers. Configure the load balancer to isolate the state-server nodes from end-user traffic.

|   |                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The underlying cluster protocol still requires that all nodes are able to communicate with one another. The topology here is only an optimization for the runtime state-management services that support the concept of preferred nodes. |

The following diagram illustrates the state-server approach.

![Runtime state-management architecture: Designating state servers](_images/nmh1564003645652.png)

In this example, the two state-server nodes have indices of 1 and 2. The `preferred.node.indices` property of the engine nodes handling requests would be `preferred.node.indices=1,2`.

Because the state servers are not processing transactions (based on the setup of the load balancer), the `preferred.node.indices` property for them is not used and can be left blank.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When PingFederate acts as an OAuth authorization server (AS) and the access token management instance uses a reference token data model, the resource server (RS) must send a request to PingFederate to de-reference the access token for the corresponding identity and security information. Because the OAuth clients and the RS send their requests separately, PingFederate shares reference token information among all engine nodes despite any state server or subcluster setup. |

---

---
title: Directed clustering
description: This topic provides an overview of manual configuration of PingFederate sever nodes through directed clustering.
component: pingfederate
version: 13.1
page_id: pingfederate:server_clustering_guide:pf_directed_cluster
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/server_clustering_guide/pf_directed_cluster.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  preferred-node-indices: Preferred node indices
---

# Directed clustering

This topic provides an overview of manual configuration of PingFederate sever nodes through directed clustering.

Directed clustering allows administrators to manually specify which PingFederate nodes should participate in tracking user sessions. Most group Remote Procedure Call (RPC)-based service implementations make use of a preferred-nodes concept, which assigns each node a list of other nodes, identified by index, with which it shares session-state information.

Each service implementation is controlled separately by a configuration file located in the `<pf_install>/pingfederate/server/default/conf` directory. You must replicate any changes manually for each cluster node.

The following tables indicate the configuration file that applies to each implementation and the applicable properties.

|   |                                                                                             |
| - | ------------------------------------------------------------------------------------------- |
|   | The Artifact-Message Persistence and Retrieval Service uses only the `rpc.timeout` setting. |

**Configuration file and service implementation**

| Configuration file                         | RPC-based service implementation                                                                |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| `cluster-account-locking.conf`             | [Account Locking Service](pf_acc_lock_service.html)                                             |
| `cluster-artifact.conf`                    | [Artifact-Message Persistence and Retrieval Service](pf_artif_mess_persis_retriev_service.html) |
| `cluster-assertion-replay-prevention.conf` | [Assertion Replay Prevention Service](pf_assertion_replay_prevention_service.html)              |
| `cluster-idp-session-registry.conf`        | [IdP Session Registry Service](pf_idp_session_registry_service.html)                            |
| `cluster-inter-request-state.conf`         | [Inter-Request State-Management (IRSM) Service](pf_irsm_service.html)                           |
| `cluster-session-revocation.conf`          | [Back-Channel Session Revocation Service](pf_bac_chann_sess_revoc_service.html)                 |
| `cluster-sp-session-registry.conf`         | [SP Session Registry Service](pf_sp_sess_regist_service.html)                                   |

**Property description**

| Property                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `preferred.node.indices`                                                              | A comma-separated list of indices identifying the nodes with which this node shares session-state information for the associated service. If left blank, this node sends session-state information to all nodes in the cluster as it processes SSO and logout requests.The Artifact-Message Persistence and Retrieval Service and the Back-Channel Session Revocation Service do not support this parameter.Ignored when adaptive clustering is enabled.This property has no default value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `preferred.node.group.id`(found only in the `cluster-idp-session-registry.conf` file) | An alphanumeric group ID for a subcluster. If specified, each subcluster must have a unique group ID. At startup, PingFederate validates that the group ID is not already registered in the cluster by another list of preferred nodes. If the validation fails, PingFederate aborts the startup process and exits.When the group ID is specified, the session identifier contains the information about the originating subcluster. This is helpful in deployments where PingFederate has been configured to manage authentication sessions on the **Authentication > Policies > Sessions** window. When an engine node receives a request to query and extend a session, it can route the request to the corresponding subcluster based on the session identifier value.If subclusters are configured without specifying group IDs, a request to query and extend a session is processed on the subcluster that received the revocation status request, which may be different from the subcluster where the session is being tracked. As a result, the session could reach the idle timeout sooner than expected.Ignored when adaptive clustering is enabled.This property has no default value. |
| `rpc.timeout`                                                                         | How long, in milliseconds, this node waits before timing out unresponsive RPC invocations.The default value is `500`, or half a second.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `synchronous.retrieve.majority.only`                                                  | Indicates how many responses to wait for when making synchronous remote procedure calls.```
When set to [.codeph]``true``, this node waits for the majority of recipients to respond. When set to [.codeph]``false``, it waits for all recipients to respond.
```The default value is `true`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `bulk.revoked.sris.timeout`(found only in the `cluster-session-revocation.conf` file) | Determines the amount of time (in milliseconds) PingFederate waits before aborting the download of revocation lists and reporting a timeout error. The default value is `10000`, or 10 seconds. NOTE: A node downloads a full revocation list from another node during startup or when it rejoins a cluster after being disconnected from it.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `read.local.only`(found only in the `cluster-session-revocation.conf` file)           | Determines how PingFederate processes queries for revocation status.When set to `true`, queries for revocation status are processed locally. When `false`, the processing node pulls revocation status from other engine nodes in the cluster (subject to the **rpc.timeout** value).&#xA;&#xA;When adding a session to the revocation list, the processing node always propagates the information to all engine nodes in the cluster. See Back-Channel Session Revocation Service for more information.The default value is `true`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

## Preferred node indices

Configuring the `preferred.node.indices` property can reduce the network communications and memory footprint. However, transaction volume and distribution can affect the resulting configuration. For more information on performance tuning, see [About Performance Tuning](../performance_tuning_guide/pf_about_performance_tuning.html).

Individual services within a single cluster deployment can use different preferred nodes, meaning you can set different values for the `preferred.node.indices` property for each service.

Using preferred nodes can translate into a variety of deployment configurations. The following sections discuss three primary strategies to consider for meeting your network requirements:

* [Sharing all nodes](pf_sharing_nodes.html)

* [Designating state servers](pf_design_state_server.html)

* [Defining subclusters](pf_defining_subclust.html)

|   |                                                                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | It is possible to configure overrides for authentication-adapter processing based on the runtime node servicing a request. See [Configuring the Cluster Node Authentication Selector](../administrators_reference_guide/pf_config_cluster_node_auth_selector.html) for more information. |

---

---
title: Dynamic cluster discovery
description: Instead of configuring a static list of known PingFederate nodes in advance, dynamic cluster discovery lets you configure new nodes to pull cluster membership information from a centralized repository.
component: pingfederate
version: 13.1
page_id: pingfederate:server_clustering_guide:pf_dynamic_cluster_discovery
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/server_clustering_guide/pf_dynamic_cluster_discovery.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: February 23, 2023
section_ids:
  dynamic-cluster-discovery-protocols: Dynamic cluster discovery protocols
  discovery-mechanisms-versus-runtime-state-management-architectures: Discovery mechanisms versus runtime state-management architectures
  related-links: Related links
---

# Dynamic cluster discovery

Instead of configuring a static list of known PingFederate nodes in advance, dynamic cluster discovery lets you configure new nodes to pull cluster membership information from a centralized repository.

Dynamic discovery is well-suited for environments where traffic volume could spike and require additional resources during peak hours. Because safe storage and ready accessibility of the information by all nodes is crucial, PingFederate supports identity and access management (IAM) roles for Amazon Elastic Compute Cloud (Amazon EC2), Amazon Simple Storage Service (Amazon S3), and OpenStack Swift. The dynamic discovery method requires only a one-time setup.

For information about configuring dynamic cluster discovery, see [Enabling dynamic discovery for clustering](pf_enabling_dynamic_discovery_clustering.html).

## Dynamic cluster discovery protocols

In addition to the static cluster discovery protocol, `TCPPING`, PingFederate supports the following dynamic discovery protocols:

* `NATIVE_S3_PING`

* `DNS_PING`

* `AWS_PING`

* `SWIFT_PING`

|   |                                                                                                                                                                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `S3_PING` discovery method has been deprecated because of the Amazon Web Services (AWS) deprecation of the SigV2 signing method. When deployed in AWS, the recommended discovery method is `NATIVE_S3_PING`. See the [JGroups documentation](http://www.jgroups.org/manual4/index.html) for alternatives when deployed in other environments. |

`NATIVE_S3_PING` and `SWIFT_PING` enable the flexibility to use both public and private cloud storage. PingFederate maintains cluster membership information in a centralized repository, a bucket in Amazon Simple Storage Service (Amazon S3) or a container in an OpenStack infrastructure.

PingFederate contacts the repository for a list of nodes. If PingFederate receives at least one node, a cluster exists, and it joins the cluster and updates the repository with its information, including its IP address. If PingFederate receives no node, it forms a new cluster and updates the repository with its information so that the next node can find the new cluster. When PingFederate shuts down, it removes itself from the list and pushes an update to the repository.

`NATIVE_S3_PING` uses the AWS SDK and provides a stable connection by using built-in security features, such as obtaining credentials through IAM server instance profiles. This protocol is the recommended dynamic discovery mechanism when you're running in AWS but aren't using Kubernetes.

`DNS_PING` uses DNS `A` or `SRV` records to perform discovery. This protocol is the recommended dynamic discovery mechanism when using Kubernetes. For more information, see the JGroups documentation about the [DNS\_PING](http://www.jgroups.org/manual4/index.html#_dns_ping) protocol.

`AWS_PING` lets you scale your PingFederate infrastructure using Amazon EC2 instances in the AWS cloud, in one or multiple regions. PingFederate queries AWS for a list of eligible EC2 instances. If PingFederate receives at least one node, a cluster exists, and it joins that cluster. If PingFederate receives no node, it forms a new cluster.

You must enable permissions to `ec2:Describe*` actions in the AWS IAM role assigned to the EC2 instance or associate them with the access\_key parameter that you provide as part of the dynamic discovery configuration. You can also use a combination of tags and filters, in which case only EC2 instances that satisfy both criteria are returned.

## Discovery mechanisms versus runtime state-management architectures

Discovery mechanisms are separate from runtime state-management architectures. Discovery mechanisms determine how to find nodes to retrieve cluster information for the purpose of joining and rejoining a cluster. Runtime state-management architectures determine which nodes session-state information is shared to and fetched from.

PingFederate supports adaptive clustering and directed clustering runtime state-management architectures. When opting for dynamic discovery, consider enabling adaptive clustering whenever possible. If multiple regions are involved, configure multi-region support for adaptive clustering as well. For more information and configuration steps, see [Adaptive clustering](pf_adaptiv_cluster.html).

Regardless of the chosen runtime state-management architecture, all nodes must still be able to communicate with other nodes for clustering-protocol messages. For more information, see [Runtime state-management architectures](pf_runtime_state_manage_achitec.html).

## Related links

* [Deploying cluster servers](pf_deploying_cluster_servers.html)