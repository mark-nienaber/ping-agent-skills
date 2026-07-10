---
title: About indexes
description: Understand how PingDS uses indexes to respond quickly to LDAP searches, and how indexes are maintained when directory data changes.
component: pingds
version: 8.1
page_id: pingds:config-guide:idx-about
canonical_url: https://docs.pingidentity.com/pingds/8.1/config-guide/idx-about.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-02T15:53:44Z
keywords: ["Features", "LDAP", "Setup &amp; Configuration"]
section_ids:
  role_of_an_index: Role of an index
  index_implementation: Index implementation
  how_ds_uses_indexes: How DS uses indexes
  unindexed-searches: Unindexed searches
  index-updates: How DS updates indexes
  changing_an_index_doesnt_reindex_existing_data: Changing an index doesn't reindex existing data
  rebuilding_indexes: Rebuilding indexes
---

# About indexes

A basic, standard directory feature is the ability to respond quickly to searches.

An LDAP search specifies the information that directly affects how long the directory might take to respond:

* The base DN for the search.

  The more specific the base DN, the less information to check during the search. For example, a request with base DN `dc=example,dc=com` potentially involves checking many more entries than a request with base DN `uid=bjensen,ou=people,dc=example,dc=com`.

* The scope of the search.

  A subtree or one-level scope targets many entries, whereas a base search is limited to one entry.

* The search filter to match.

  A search filter asserts that for an entry to match, it has an attribute that corresponds to some value. For example, `(cn=Babs Jensen)` asserts that `cn` must have a value that equals `Babs Jensen`.

  A directory server would waste resources checking all entries for a match. Instead, directory servers maintain indexes to expedite checking for a match.

LDAP directory servers disallow searches that cannot be handled expediently using indexes. Maintaining appropriate indexes is a key aspect of directory administration.

## Role of an index

The role of an index is to answer the question, "Which entries have an attribute with this corresponding value?"

Each index is therefore specific to an attribute.

Each index is also specific to the comparison implied in the search filter. For example, a directory server maintains distinct indexes for exact (equality) matching and for substring matching. The types of indexes are explained in [Index types](idx-types.html). Furthermore, indexes are configured in specific directory backends.

## Index implementation

An index is implemented as a tree of key-value pairs. The key is a form of the value to match, such as `babs jensen`. The value is a list of IDs for entries that match the key. The figure that follows shows an equality (case ignore exact match) index with five keys from a total of four entries. If the data set were large, there could be more than one entry ID per key:

![An index is implemented as a tree of key-value pairs.](../_images/equality-index.png)

## How DS uses indexes

This example illustrates how DS uses an index.

When the search filter is `(cn=Babs Jensen)`, DS retrieves the IDs for entries whose CN matches `Babs Jensen` by looking them up in the equality index of the CN attribute. (For a complex filter, it might optimize the search by changing the order in which it uses the indexes.) A successful result is zero or more entry IDs. These are the candidate result entries.

For each candidate, DS retrieves the entry by ID from a system index called `id2entry`. As its name suggests, this index returns an entry for an entry ID. If there is a match, and the client application has the right to access the data, DS returns the search result. It continues this process until no candidates are left.

## Unindexed searches

If there are no indexes that correspond to a search request, DS must check for a match against every entry in the scope of the search. Evaluating every entry for a match is referred to as an unindexed search *(tooltip: \<div class="paragraph">
\<p>A search operation for which the server has no appropriate index.\</p>
\</div>)*.

An unindexed search is an expensive operation, particularly for large directories. A server refuses unindexed searches unless the user has specific permission to make such requests. The permission to perform an unindexed search is granted with the `unindexed-search` privilege. This privilege is reserved for the directory superuser by default. It should not be granted lightly.

If the number of entries is smaller than the default resource limits, you can still perform what appear to be unindexed searches, meaning searches with filters for which no index appears to exist. That is because the `dn2id` index returns all user data entries without hitting a resource limit that would make the search unindexed.

Use cases that may call for unindexed searches include the following:

* An application must periodically retrieve a very large amount of directory data all at once through an LDAP search.

  For example, an application performs an LDAP search to retrieve everything in the directory once a week as part of a batch job that runs during off-peak hours.

  Make sure the application has no resource limits. Learn more in [Enforce limits](../use-cases/limits.html).

* A directory data administrator occasionally browses directory data through a graphical UI without initially knowing what they are looking for or how to narrow the search.

  Big indexes let you work around this problem. They facilitate searches where large numbers of entries match. For example, big indexes can help when paging through all the employees in a large company, or all the users in the state of California. Learn more in [Big index](idx-types.html#big-indexes) and [Indexes for attributes with few unique values](idx-config.html#use-big-indexes).

  Alternatively, DS directory servers can use an appropriately configured VLV index to sort results for an unindexed search. Learn more in [VLV for paged server-side sort](idx-config.html#vlv-for-paged-sss).

## How DS updates indexes

DS updates indexes when directory data changes. When you import data from LDIF or when an application adds, modifies, or deletes an entry, DS updates each affected index based on its configuration.

DS updates indexes while the server is online. This has a cost, and the cost is the reason to maintain only indexes applications actually use. Updating an unindexed attribute is faster than updating an indexed attribute.

### Changing an index doesn't reindex existing data

You, the administrator, define how DS indexes attributes. You configure which attributes to index and the type of indexes to maintain for each attribute.

You can [change index configurations at any time](idx-config.html).

DS doesn't automatically reindex existing data when you change an index configuration, however. "Automatic" index updates only happen when directory data changes.

### Rebuilding indexes

After changing an index configuration, you can manually [rebuild indexes](idx-config.html#rebuild-index), forcing DS to update indexes for the existing directory data.

Importing data from LDIF, which replaces the data in a backend, also forces DS to index all the data.

---

---
title: About replication
description: Understand how PingDS replication works, including eventually consistent updates, replication topology, port use, and connection selection.
component: pingds
version: 8.1
page_id: pingds:config-guide:repl-about
canonical_url: https://docs.pingidentity.com/pingds/8.1/config-guide/repl-about.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Features", "LDAP", "Replication", "Setup &amp; Configuration"]
section_ids:
  repl-enable: Ready to replicate
  repl-per-base-dn: Replication per base DN
  repl-network-operations: Port use and operations
  repl-connection-selection: Replication connection selection
---

# About replication

Replication *(tooltip: \<div class="paragraph">
\<p>Data synchronization to ensure all participating servers eventually share a consistent set of directory data.\</p>
\</div>)* is the process of copying updates between DS servers so all directory servers eventually converge on identical copies of directory data. DS servers that replicate their data are replicas *(tooltip: \<div class="paragraph">
\<p>A directory server configured to use replication.\</p>
\</div>)*. Since replication is *eventually convergent*, different replicas can be momentarily out of sync. If you lose an individual replica, or even an entire data center, the remaining replicas continue to provide service. Applications can still write changes to the directory data. Replication brings the replicas back in sync when the problem is repaired.

Replication uses a DS-specific protocol that works only between DS replicas. It replays update operations quickly, storing historical change data to resolve most conflicts automatically. For example, if two client applications separately update a user entry to change the phone number, replication can identify the latest change, and apply it on all replicas without human intervention. To prevent the historical change data from growing forever, DS replicas purge historical data that is older than a configurable interval (default: three days).

DS software supports replication over fast and slow networks. For advanced deployments across multiple sites with many replicas and slow links, consider standalone servers. For details, refer to [Install standalone servers (advanced)](../install-guide/setup-rs.html).

Replication is resilient to host clock anomalies. You should, however, aim to keep server clocks synchronized using `ntpd`, for example. Keeping replica clocks synchronized helps prevent issues when validating certificates for secure connections, and makes it easier to compare timestamps from multiple replicas. Replication is designed to overcome the following issues:

* Clock skew between different replicas.

  Replication adjusts for skew automatically, and using `ntpd` further mitigates this.

  Very large skew, such as replicating with a system whose clock was started at 0 (January 1, 1970), can cause problems.

* Forward and backward clock adjustments on a single replica.

  Replication adjusts for these automatically.

  Very large changes, such as abruptly setting the clock back an entire day, can cause problems.

* Timezone differences and adjustments.

  Replication uses UTC time.

Very large host clock anomalies can result in the following symptoms:

* SSL certificate validation errors, when the clocks are far enough apart that the validity dates cannot be correctly compared.

* Problems with time-based settings in access control instruction subjects, and with features that depend on timestamps, such as password age and last login attributes.

* Misleading changelog timestamps and replication-related monitoring data.

* Incorrect replication conflict resolution.

* Incorrect replication purge delay calculation.

## Ready to replicate

When you set up a server, you can specify the following:

* The replication port.

  If specified, the setup process configures the server as a replication server.

* The bootstrap replication servers' host:port combinations.

  When the server starts, it contacts the bootstrap replication servers to discover other replicas and replication servers.

Setup profiles that create backends for schema and directory data configure replication domains for their base DNs. The server is ready to replicate that directory data when it starts up.

Replication initialization depends on the state of the data in the replicas.

DS replication shares changes, not data. When a replica applies an update, it sends a message to its replication server. The replication server forwards the update to all other replication servers, and to its replicas. The other replication servers do the same, so the update is eventually propagated to all replicas.

Each replica eventually converges on the same data by applying each update and resolving conflicts in the same way. As long as each replica starts from the same initial state, each replica eventually converges on the same state. It is crucial, therefore, for each replica to begin in the same initial state. Replicas cannot converge by following exactly the same steps from different initial states.

Internally, DS replicas store a shorthand form of the initial state called a generation ID. The generation ID is a hash of the first 1000 entries in a backend. If the replicas' generation IDs match, the servers can replicate data without user intervention. If the replicas' generation IDs do not match for a given backend, you must manually initialize replication between them to force the same initial state on all replicas.

If necessary, and before starting the servers, further restrict TLS protocols and cipher suites on all servers. This forces the server to use only the restricted set of protocols and cipher suites. For details, refer to [TLS settings](../security-guide/connections.html#tls-protocols-cipher-suites).

## Replication per base DN

The primary unit of replication is the replication domain. A replication domain has a base DN, such as `dc=example,dc=com`.

The set of DS replicas and replication servers sharing one or more replication domains is a replication topology. Replication among these servers applies to all the data under the domain's base DN.

The following example topology replicates `dc=example,dc=com`, `dc=example,dc=org`, and `dc=example,dc=net`. All the replication servers in a topology are fully connected, replicating the same data under each base DN:

![The three replication domains are configured correctly.](../_images/repl-topologies-right.png)Figure 1. Correct replication configuration

Replication doesn't support separate, independent domains for the same base DN in the same topology. For example, you can't replicate two `dc=example,dc=org` domains with different data in the same topology:

![The data in a replication domain must match thoughout the topology.](../_images/repl-topologies-wrong.png)Figure 2. Incorrect replication configuration

When you set up a replication domain, replicate the data under the base DN among all the servers in the topology. If the data under a base DN is different on different servers, configure the servers appropriately:

| Difference                                                | Use this                                                                                                                                     |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Different data under the same base DN.                    | Separate replication topologies.In other words, put the replicas and replication servers in independent deployments unless the data matches. |
| Some replicas have only part of the data under a base DN. | [Subtree replication (advanced)](repl-subtree.html)                                                                                          |
| Some replicas have only a subset of LDAP attributes.      | [Fractional replication (advanced)](repl-fractional.html)                                                                                    |

Replication depends on the directory schema under `cn=schema`. If applications require specific, non-standard schema definitions or can update the LDAP schema online, replicate `cn=schema` with the other base DNs.

## Port use and operations

DS servers listen on dedicated ports for administrative requests and for replication requests. These dedicated ports must remain open to remote requests from configuration tools and from other servers. *Make sure that firewall software allows connections to the administration and replication ports from all connecting servers.*

DS server configuration tools securely connect to administration ports. Administrative connections are short-lived.

DS replicas connect to DS replication ports for replication requests. A server listening on a replication port is called a replication server, whether it's running inside the same process as a directory server or on a separate host system. Replication connections are long-lived. Each DS replica connects to a replication server upon initialization and then at startup time. The replica keeps the connection open to push and receive updates, although it can connect to another replication server.

The command to initialize replication uses the administrative port, and initialization uses the replication port:

![Initialization involves both ports.](../_images/init-repl.svg)Figure 3. Manual replication initialization

DS replicas push updates to and receive updates from replication servers over replication connections. When processing an update, a replica (DS) pushes it to the replication server (RS) it is connected to. The replication server pushes the update to connected replicas and to other replication servers. Replicas always connect through replication servers.

A replica with a replication port and a changelog plays both roles (DS/RS), normally connecting to its own replication server. A standalone replica (DS) connects to a remote replication server (RS). The replication servers connect to each other. The following figure shows the flow of messages between standalone replicas and replication servers.

![Replication pushes changes over the connection to the replication port.](../_images/update.svg)Figure 4. Data replication

The command to monitor replication status uses the administration ports on multiple servers to connect and read monitoring information, as shown in the following sequence diagram:

![The dsreplication status command connects to multiple servers.](../_images/status.svg)

## Replication connection selection

DS servers can provide both directory services and replication services. The two services are not the same, even if they usually run alongside each other in the same DS server.

Replication relies on the replication service provided by DS replication servers. DS directory servers (replicas) publish changes made to their data, and subscribe to changes published by other replicas. The replication service manages replication data only, sending and receiving replication messages. A replication server receives, sends, and stores only changes to directory data, not the data itself.

The directory service manages directory data. It responds to requests, and stores directory data and historical information. For each replicated base DN, such as `dc=example,dc=com` or `cn=schema`, the directory service publishes changes to and subscribes to changes from a replication service. The directory service resolves any conflicts that arise when reconciling changes from other replicas, using the historical information about changes to resolve the conflicts. (Conflict resolution is the responsibility of the directory server rather than the replication server.)

After a directory server connects to a replication topology, it connects to one replication server at a time for a given domain. The replication server provides the directory server with the list of all replication servers for that base DN. Given this list, the directory server selects its preferred replication server when starting up, when it loses the current connection, or when the connection becomes unresponsive.

For each replicated base DN, a directory server prefers to connect to a replication server:

1. In the same JVM as the directory server.

2. In the same group as the directory server.

   By default, if no replication server in the same group is available, the directory server chooses a replication server from any available group.

   To define the order of failover across replication groups, set the global configuration property, [group-id-failover-order](../configref/objects-global.html#group-id-failover-order). When this property is set and no replication server is available in the directory server's group, the directory server chooses a replication server from the next group in the list.

3. With the same initial data under the base DN as the directory server.

4. If initial data was the same, a replication server with all the latest changes from the directory server.

5. With the most available capacity relative to other eligible replication servers.

   Available capacity depends on how many replicas in the topology are already connected to the replication server, and what proportion of all replicas ought to be connected to the replication server.

   To determine what proportion ought to be connected, a directory server uses replication server weight. When configuring a replication server, you can assign it a weight (default: 1). The weight property takes an integer that indicates capacity relative to other replication servers. For example, a weight of 2 indicates a replication server that can handle twice as many connected replicas as one with weight 1.

   The proportion that ought to be connected is `(replication server weight)/(sum of replication server weights)`. If there are four replication servers with weight 1, the proportion for each is 1/4.

Consider a `dc=example,dc=com` topology with five directory servers connected to replication servers A, B, and C, where:

* Two directory servers are connected to replication server A.

* Two directory servers are connected to replication server B.

* One directory server is connected to replication server C.

Replication server C is the server with the most available capacity. All other criteria being equal, replication server C is the server to connect to when another directory server joins the topology.

The directory server regularly updates the list of replication servers in case it must reconnect. As available capacity can change dynamically, a directory server can reconnect to another replication server to balance the replication load in the topology. For this reason, the server can also end up connected to different replication servers for different base DNs.

---

---
title: About request handling
description: Overview of how PingDS connection handlers accept and route client requests through the core server to backends.
component: pingds
version: 8.1
page_id: pingds:config-guide:request-handling
canonical_url: https://docs.pingidentity.com/pingds/8.1/config-guide/request-handling.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["LDAP", "Setup &amp; Configuration", "Troubleshooting"]
---

# About request handling

DS servers listen for client requests using connection handlers. A connection handler interacts with client applications, accepting connections, reading requests, and sending responses. Most connection handlers expose configurable listen ports with security settings. The security settings point to other configuration objects, so two connection handlers can share the same certificate and private key, for example.

DS servers use different ports for different protocols. For example, a directory server might listen on port `389` for LDAP requests, port `443` for HTTPS requests, and port `4444` for administration requests. Because DS servers use a different connection handler for each port, DS servers have several connection handlers enabled.

The `setup` command lets you initially configure connection handlers for LDAP or LDAPS, HTTP or HTTPS, and administrative traffic. The `dsconfig` command offers full access to all connection handler configurations.

When a client application opens a secure connection to a server, the JVM has responsibility for transport layer security negotiations. You can configure how connection handlers access keys required during the negotiations. You can also configure which clients on the network are allowed to use the connection handler. For details, refer to the [reference documentation](../configref/objects-connection-handler.html).

Connection handlers receive incoming requests, and pass them along for processing by the core server subsystem.

For example, an LDAP connection handler enqueues requests to the core server, which in turn requests data from the appropriate backend as necessary. For more information about backends, refer to [Data storage](import-export.html). The core server returns the LDAP response.

![LDAP request processing occurs in the core directory server.](../_images/ldap.svg)Figure 1. LDAP Requests

An HTTP connection handler translates each request to LDAP. Internally, the core server subsystem processes the resulting LDAP requests.

![An HTTP connection handler translates to LDAP based on its configuration.](../_images/http.svg)Figure 2. HTTP Requests

DS servers support other types of connection handlers, as described in the reference documentation.

When deploying a server, decide which listen ports to expose over which networks. Determine how you want to secure the connections, as described in [Secure connections](../security-guide/connections.html).

---

---
title: Add a new replica
description: Add a new PingDS replica using setup profiles, optionally importing LDIF or restoring a backup offline before starting the server.
component: pingds
version: 8.1
page_id: pingds:config-guide:repl-add-replica
canonical_url: https://docs.pingidentity.com/pingds/8.1/config-guide/repl-add-replica.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Features", "LDAP", "Replication"]
---

# Add a new replica

Adding a new replica means [installing a new DS server](../install-guide/preface.html).

* If you have the user data as LDAP Data Interchange Format (LDIF) *(tooltip: \<div class="paragraph">
  \<p>An IETF standard file format for representing LDAP directory content and modifications to directory content. Typically used to import and export LDAP-based directory information.\</p>
  \</div>)* and can import it using one of the setup profiles, set the new replica up with the appropriate setup profiles, importing the data from LDIF at setup time.

* If you must import user data from LDIF you can't import through a setup profile, or you opt to get the user data by restoring backup files from another replica:

  1. Set the new replica up with the appropriate setup profiles, *omitting the `setup --start` option to prevent the new server from starting*.

  2. With the new replica stopped, [import the LDIF *offline*](import-export.html#import-ldif) or [restore the data from backup *offline*](../maintenance-guide/backup-restore.html#restore-offline).

  3. Start the new replica.

     |   |                                                                                                                              |
     | - | ---------------------------------------------------------------------------------------------------------------------------- |
     |   | If you accidentally started the new replica before you restored the data from backup, remove the new replica and start over. |

---

---
title: Administrative and unified access
description: Configure the PingDS administration port and unified connection handlers to accept both LDAP and HTTP requests on the same port.
component: pingds
version: 8.1
page_id: pingds:config-guide:admin-access
canonical_url: https://docs.pingidentity.com/pingds/8.1/config-guide/admin-access.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Features", "Setup &amp; Configuration"]
section_ids:
  the_administration_port: The administration port
  additional_unified_connection_handlers: Additional unified connection handlers
---

# Administrative and unified access

The administration port and unified connection handler ports accept both LDAP and HTTP requests.

## The administration port

DS servers require you specify an administration port when setting up the server. This documentation shows the default administration port as `4444`.

Use this port to manage the server configuration and run server tasks. You can use the same port for administrative HTTPS requests, such as Prometheus queries and Kubernetes probes.

The setup process creates an administration connector for the port. The administration connector accepts both LDAPS and HTTPS requests.

DS uses the keys generated at setup time to protect administrative connections. Client applications should trust the generated DS CA certificate to establish secure connections.

## Additional unified connection handlers

You can configure a unified connection handler to listen for LDAP and HTTP on the same port. A unified connection handler accepts either cleartext (LDAP and HTTP) or TLS (LDAPS and HTTPS) requests, not both.

The following command creates a unified connection handler to listen on port `2389` for LDAP and HTTP:

```console
$ dsconfig \
 create-connection-handler \
 --handler-name "LDAP-HTTP" \
 --type unified \
 --set enabled:true \
 --set listen-port:2389 \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
```

The new connection handler accepts requests as soon as you create it.

---

---
title: Attribute uniqueness
description: Configure the PingDS unique attribute plugin to enforce attribute value uniqueness across entries and replicas.
component: pingds
version: 8.1
page_id: pingds:config-guide:attribute-uniqueness
canonical_url: https://docs.pingidentity.com/pingds/8.1/config-guide/attribute-uniqueness.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Features", "LDAP", "Setup &amp; Configuration"]
section_ids:
  enable-unique-uids: Enable unique UIDs
  enable-unique-attributes: Make other attributes unique
  unique-attributes-scoped: Scope uniqueness
  unique-attributes-repl: Use uniqueness with replication
---

# Attribute uniqueness

Some attribute values must remain unique. For example, if you use `uid` as the RDN for millions of user entries, you must avoid two or more identical `uid` values. As another example, if credit card or mobile numbers are stored on directory attributes, you want to be certain that neither is shared with another customer.

DS servers use the unique attribute plugin to ensure attribute value uniqueness. In a deployment with multiple replicas and unique attributes, direct updates for each unique attribute to a single replica at a time as described below.

## Enable unique UIDs

By default, the unique attribute plugin is configured to ensure unique `uid` values:

1. Set the base DN where the `uid` should have unique values, and enable the plugin:

   ```console
   $ dsconfig \
    set-plugin-prop \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --plugin-name "UID Unique Attribute" \
    --set base-dn:ou=people,dc=example,dc=com \
    --set enabled:true \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

   You can optionally specify unique values across multiple base DNs:

   ```console
   $ dsconfig \
    set-plugin-prop \
    --hostname localhost \
    --port 4444 \
    --bindDn uid=admin \
    --bindPassword password \
    --plugin-name "UID Unique Attribute" \
    --set enabled:true \
    --add base-dn:ou=people,dc=example,dc=com \
    --add base-dn:ou=people,dc=example,dc=org \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

2. Check your work:

   ```console
   $ ldapmodify \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN uid=admin \
    --bindPassword password << EOF
   dn: uid=ajensen,ou=People,dc=example,dc=com
   changetype: modify
   add: uid
   uid: bjensen
   EOF
   ```

   > **Collapse: Show output**
   >
   > ```
   > # The LDAP modify request failed: 19 (Constraint Violation)
   > # Additional Information:  A unique attribute conflict was detected for attribute uid: value bjensen already exists in entry uid=bjensen,ou=People,dc=example,dc=com
   > ```

   If you have set up multiple base DNs, check your work as follows:

   ```console
   $ ldapmodify \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN uid=admin \
    --bindPassword password << EOF
   dn: uid=bjensen,ou=People,dc=example,dc=org
   objectClass: top
   objectClass: person
   objectClass: organizationalPerson
   objectClass: inetOrgPerson
   cn: Babs
   sn: Jensen
   uid: bjensen
   EOF
   ```

   > **Collapse: Show output**
   >
   > ```
   > # The LDAP modify request failed: 19 (Constraint Violation)
   > # Additional Information:  A unique attribute conflict was detected for attribute uid: value bjensen already exists in entry uid=bjensen,ou=People,dc=example,dc=com
   > ```

## Make other attributes unique

You can configure the unique attribute plugin for use with any attributes, not just `uid`:

1. Before you set up the plugin, index the attribute for equality.

   For instructions, refer to [Configure indexes](idx-config.html).

2. Set up the plugin configuration for your attribute using one of the following alternatives:

   1. Add the attribute to an existing plugin configuration:

      ```console
      $ dsconfig \
       set-plugin-prop \
       --hostname localhost \
       --port 4444 \
       --bindDN uid=admin \
       --bindPassword password \
       --plugin-name "UID Unique Attribute" \
       --add type:telephoneNumber \
       --trustStorePath /path/to/opendj/config/keystore \
       --trustStoreType PKCS12 \
       --trustStorePassword:file /path/to/opendj/config/keystore.pin \
       --no-prompt
      ```

      Choose this alternative if you want each value to be unique across all configured attributes.

   2. Create a new plugin configuration:

      ```console
      $ dsconfig \
       create-plugin \
       --hostname localhost \
       --port 4444 \
       --bindDN uid=admin \
       --bindPassword password \
       --plugin-name "Unique phone numbers" \
       --type unique-attribute \
       --set enabled:true \
       --set base-dn:ou=people,dc=example,dc=com \
       --set type:telephoneNumber \
       --trustStorePath /path/to/opendj/config/keystore \
       --trustStoreType PKCS12 \
       --trustStorePassword:file /path/to/opendj/config/keystore.pin \
       --no-prompt
      ```

      Choose this alternative if values only need to be unique within the context of a particular attribute.

3. Check your work:

   ```console
   $ ldapmodify \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN uid=admin \
    --bindPassword password << EOF
   dn: uid=ajensen,ou=People,dc=example,dc=com
   changetype: modify
   replace: telephoneNumber
   telephoneNumber: +1 828 555 1212

   dn: uid=bjensen,ou=People,dc=example,dc=com
   changetype: modify
   replace: telephoneNumber
   telephoneNumber: +1 828 555 1212
   EOF
   ```

   > **Collapse: Show output**
   >
   > ```
   > # MODIFY operation successful for DN uid=ajensen,ou=People,dc=example,dc=com
   >
   > # The LDAP modify request failed: 19 (Constraint Violation)
   > # Additional Information:  A unique attribute conflict was detected for attribute telephoneNumber: value +1 828 555 1212 already exists in entry uid=ajensen,ou=People,dc=example,dc=com
   > ```

## Scope uniqueness

In some cases, attributes must be unique, but only in the context of a particular base DN. For example, `uid` values must be unique under `dc=example,dc=com` and under `dc=example,dc=org`. But it is okay to have `uid=bjensen,ou=people,dc=example,dc=com` and `uid=bjensen,ou=people,dc=example,dc=org`:

1. If the attribute you target is not indexed for equality by default, index the attribute for equality.

   Refer to [Configure indexes](idx-config.html) for instructions.

2. For each base DN, set up a configuration entry that ensures the target attribute values are unique:

   ```console
   $ dsconfig \
    create-plugin \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --plugin-name "Unique Example.com UIDs" \
    --type unique-attribute \
    --set enabled:true \
    --set base-dn:dc=example,dc=com \
    --set type:uid \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   $ dsconfig \
    create-plugin \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --plugin-name "Unique Example.org UIDs" \
    --type unique-attribute \
    --set enabled:true \
    --set base-dn:dc=example,dc=org \
    --set type:uid \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

3. Check your work:

   ```console
   $ ldapmodify \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN uid=admin \
    --bindPassword password << EOF
   dn: uid=unique,ou=People,dc=example,dc=com
   uid: unique
   givenName: Unique
   objectClass: person
   objectClass: organizationalPerson
   objectClass: inetOrgPerson
   objectClass: top
   cn: Unique Person
   sn: Person
   userPassword: 1Mun1qu3

   dn: uid=unique,ou=People,dc=example,dc=org
   uid: unique
   givenName: Unique
   objectClass: person
   objectClass: organizationalPerson
   objectClass: inetOrgPerson
   objectClass: top
   cn: Unique Person
   sn: Person
   userPassword: 1Mun1qu3

   dn: uid=copycat,ou=People,dc=example,dc=com
   uid: unique
   uid: copycat
   givenName: Copycat
   objectClass: person
   objectClass: organizationalPerson
   objectClass: inetOrgPerson
   objectClass: top
   cn: Copycat Person
   sn: Person
   userPassword: copycopy
   EOF
   ```

   > **Collapse: Show output**
   >
   > ```
   > # ADD operation successful for DN uid=unique,ou=People,dc=example,dc=com
   >
   > # The LDAP modify request failed: 19 (Constraint Violation)
   > # Additional Information:  A unique attribute conflict was detected for attribute uid: value unique already exists in entry uid=unique,ou=People,dc=example,dc=com
   > ```

## Use uniqueness with replication

The unique attribute plugin only ensures uniqueness on the replica where the attribute is updated. If client applications write the same attribute value separately at the same time on different replicas, both replicas might use the same "unique" value, especially if the network is down between the replicas:

1. Configure the plugin identically on all replicas.

2. To avoid duplicate values where possible, use DS directory proxy to direct all updates of the unique attribute to the same replica.

---

---
title: Bootstrap replication servers
description: "Configure bootstrap replication servers in PingDS, and add or remove them from other servers' bootstrap settings."
component: pingds
version: 8.1
page_id: pingds:config-guide:repl-bootstrap
canonical_url: https://docs.pingidentity.com/pingds/8.1/config-guide/repl-bootstrap.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Features", "LDAP", "Replication", "Setup &amp; Configuration"]
section_ids:
  add-bootstrap-replication-server: Add a bootstrap replication server
  remove-bootstrap-replication-server: Remove a bootstrap replication server
---

# Bootstrap replication servers

A *bootstrap replication server* is one of the replication servers in a deployment.

Every deployment with multiple replicas must have one or more bootstrap replication servers:

* When starting up, a DS server contacts a bootstrap replication server to discover the remaining DS servers in the deployment.

* Being a bootstrap replication server doesn't significantly increase resource use.

  After startup, a server gets its information about the remaining servers in the deployment from any replication server.

* Use at least two bootstrap replication servers for availability.

  You don't need more as long as all other DS servers can contact one of the bootstrap replication servers.

* A replication server takes on the role when other servers configure it as a bootstrap replication server.

  Specify the same list of bootstrap servers each time you set up a replica.

## Add a bootstrap replication server

After you add a replication server to a deployment, add it to the other servers' [bootstrap-replication-server](../configref/objects-replication-synchronization-provider.html#bootstrap-replication-server) settings.

Apply these steps for each server whose configuration references the new replication server to add:

1. Add the bootstrap replication server to the server's configuration:

   ```console
   $ dsconfig \
    set-synchronization-provider-prop \
    --provider-name "Multimaster Synchronization" \
    --add bootstrap-replication-server:new-rs.example.com:8989 \
    --hostname replica.example.com \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

2. If the server uses property value substitution to load the list of replication bootstrap servers from the environment, restart the server for the changes to take effect.

## Remove a bootstrap replication server

After you remove a replication server from a deployment, remove it from other servers' `bootstrap-replication-server` settings.

Apply these steps for each server whose configuration references the replication server that you removed:

1. Remove the bootstrap replication server from the server's configuration:

   ```console
   $ dsconfig \
    set-synchronization-provider-prop \
    --provider-name "Multimaster Synchronization" \
    --remove bootstrap-replication-server:removed-rs.example.com:8989 \
    --hostname replica.example.com \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

2. If the server uses property value substitution to load the list of replication bootstrap servers from the environment, restart the server for the changes to take effect.

---

---
title: Changelog for notifications
description: Enable and configure the PingDS external changelog for change notification, encryption, and access control.
component: pingds
version: 8.1
page_id: pingds:config-guide:changelog
canonical_url: https://docs.pingidentity.com/pingds/8.1/config-guide/changelog.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Features", "LDAP", "Replication", "Setup &amp; Configuration"]
section_ids:
  enable-ecl: Enable the external changelog
  encrypt-ecl: Encrypt changelog data
  read-ecl-as-regular-user: Let a user read the changelog
  ecl-add-attributes: Include unchanged attributes
  ecl-exclude-domain: Exclude a domain
  ecl-legacy-format: Internet-Draft change numbers
  ecl-configure-changenumber-indexer: Change number indexing
---

# Changelog for notifications

Some applications require notification when directory data updates occur. For example, an application might need to sync directory data with another database, or the application might need to kick off other processing when certain updates occur. DS replication servers provide an external changelog that replications can use to read changes. This mechanism is more scalable and robust than LDAP persistent searches.

By default, changelog database files are found under the `opendj/changelogDb` directory.

|   |                                                                                                                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Do not compress, tamper with, or otherwise alter changelog database files directly, unless specifically instructed to do so by a qualified technical support engineer.External changes to changelog database files can render them unusable by the server. |

## Enable the external changelog

DS servers that have a replication server port and an LDAP port publish an external changelog over LDAP:

| Ports Configured   | Examples       | Notes                                                                                                                                                                                                            |
| ------------------ | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| LDAP or LDAPS port | `1389`, `1636` | LDAP client applications use the LDAP or LDAPS port to read changelog data.A standalone replication server may not have an LDAP or LDAPS port configured.                                                        |
| Replication port   | `8989`         | Servers with replication ports maintain a changelog for their own use. The changelog is exposed over LDAP under the base DN, `cn=changelog`.Standalone directory servers do not maintain a changelog by default. |

1. Make sure an LDAP or LDAPS port is configured so that LDAP client applications can read the changelog.

2. Depending on the server configuration, enable the changelog one of the following ways:

   1. For servers with replication ports, make sure replication is properly configured.

      The following example shows how the directory superuser can read the changelog:

      ```console
      $ ldapsearch \
       --hostname localhost \
       --port 1636 \
       --useSsl \
       --trustStorePath /path/to/opendj/config/keystore \
       --trustStoreType PKCS12 \
       --trustStorePassword:file /path/to/opendj/config/keystore.pin \
       --bindDN uid=admin \
       --bindPassword password \
       --baseDN cn=changelog \
       --searchScope base \
       --control "ecl:true" \
       "(&)"
      ```

      > **Collapse: Show output**
      >
      > ```
      > dn: cn=changelog
      > objectclass: top
      > objectclass: container
      > cn: changelog
      > ```

      |   |                                                                                                                                                                         |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | The external changelog (`cn=changelog`) doesn't support the [Simple Paged Results](https://www.rfc-editor.org/info/rfc2696) LDAP control (OID: 1.2.840.113556.1.4.319). |

   2. For standalone directory servers without replication ports, you can manually enable the changelog. These steps cause the server to begin maintaining a replication changelog, which consumes disk space:

      * Update the default replication synchronization configuration entry as in the following example:

        ```console
        $ dsconfig \
         set-synchronization-provider-prop \
         --provider-name "Multimaster Synchronization" \
         --set bootstrap-replication-server:localhost:8989 \
         --hostname localhost \
         --port 4444 \
         --bindDN uid=admin \
         --bindPassword password \
         --trustStorePath /path/to/opendj/config/keystore \
         --trustStoreType PKCS12 \
         --trustStorePassword:file /path/to/opendj/config/keystore.pin \
         --no-prompt
        ```

      * Create a replication server configuration entry as in the following example:

        ```console
        $ dsconfig \
         create-replication-server \
         --provider-name "Multimaster Synchronization" \
         --set replication-port:8989 \
         --hostname localhost \
         --port 4444 \
         --bindDN uid=admin \
         --bindPassword password \
         --trustStorePath /path/to/opendj/config/keystore \
         --trustStoreType PKCS12 \
         --trustStorePassword:file /path/to/opendj/config/keystore.pin \
         --no-prompt
        ```

      * Create a replication domain configuration entry as in the following example:

        ```console
        $ dsconfig \
         create-replication-domain \
         --provider-name "Multimaster Synchronization" \
         --domain-name "Example.com" \
         --set base-dn:dc=example,dc=com \
         --hostname localhost \
         --port 4444 \
         --bindDN uid=admin \
         --bindPassword password \
         --trustStorePath /path/to/opendj/config/keystore \
         --trustStoreType PKCS12 \
         --trustStorePassword:file /path/to/opendj/config/keystore.pin \
         --no-prompt
        ```

3. Make sure the user who needs to read changelog data has the `changelog-read` privilege, and has access to read entries under `cn=changelog`.

   For details, refer to [Let a user read the changelog](#read-ecl-as-regular-user).

## Encrypt changelog data

DS servers do not encrypt changelog data on disk by default. Any user with system access to read directory files can potentially read external changelog data.

In addition to preventing read access by other users, you can configure confidentiality for changelog data. When confidentiality is enabled, the server encrypts changelog records before storing them on disk. The server decrypts changelog records before returning them to client applications.

|   |                                                                                                                                                                  |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Encrypting stored directory data does not prevent it from being sent over the network in the clear.Use secure connections to protect data sent over the network. |

DS servers encrypt data using symmetric keys. Servers generate symmetric keys when needed and store them, encrypted with the shared master key, with the data they encrypt. As long as servers have the same shared master key, any server can recover symmetric keys needed to decrypt data.

Symmetric keys for (deprecated) reversible password storage schemes are the exception to this rule. When you configure a reversible password storage scheme, enable the `adminRoot` backend, and configure a replication domain for `cn=admin data`.

Encrypting and decrypting data require cryptographic processing that reduces throughput, and extra space for larger encrypted values. Tests with default settings show that the cost of enabling confidentiality can be quite modest. Your results can vary based on the host system hardware, the JVM, and the settings for `cipher-transformation` and `cipher-key-length`. Make sure you test your deployment to qualify the impact of confidentiality before changing settings in production.

Follow these steps to enable confidentiality:

1. Before you enable confidentiality on a replication server for the changelog data, first enable confidentiality for data stored in directory backends.

   For details, refer to [Data encryption](../security-guide/data.html).

2. Enable changelog confidentiality with the default encryption settings:

   ```console
   $ dsconfig \
    set-replication-server-prop \
    --provider-name "Multimaster Synchronization" \
    --set confidentiality-enabled:true \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

   Encryption applies to the entire changelog regardless of the confidentiality settings for each domain.

   After confidentiality is enabled, new changelog records are encrypted. DS servers do not rewrite old records in encrypted form.

3. If necessary, adjust additional confidentiality settings.

   Use the same cipher suite for changelog confidentiality and data confidentiality.

   The default settings for confidentiality are `cipher-transformation: AES/GCM/NoPadding`, and `cipher-key-length: 128`. This means the algorithm is the Advanced Encryption Standard (AES), and the cipher mode is Galois/Counter Mode (GCM). The syntax for the `cipher-transformation` is `algorithm/mode/padding`. You must specify the *algorithm*, *mode*, and *padding*. When the algorithm does not require a mode, use `NONE`. When the algorithm does not require padding, use `NoPadding`.

## Let a user read the changelog

For a user to read the changelog, the user must have access to read, search, and compare changelog attributes, might have access to use the control to read the external changelog, and must have the `changelog-read` privilege.

1. Give the user access to read and search the changelog.

   The following example adds two global ACIs *(tooltip: \<div class="paragraph">
   \<p>An instruction or rule that can be used to grant or deny access to users to perform operations on a server.\</p>
   \</div>)*. The first ACI gives `My App` read access to root DSE attributes that hold information about the changelog. The second ACI gives `My App` read access to the changelog data:

   ```console
   $ dsconfig \
    set-access-control-handler-prop \
    --add global-aci:"(target=\"ldap:///\")\
   (targetattr=\"changeLog||firstChangeNumber||lastChangeNumber||lastExternalChangeLogCookie\")\
   (version 3.0; acl \"My App can access changelog attributes on root DSE\"; \
   allow (read,search,compare) \
   userdn=\"ldap:///cn=My App,ou=Apps,dc=example,dc=com\";)" \
    --add global-aci:"(target=\"ldap:///cn=changelog\")(targetattr=\"*||+\")\
   (version 3.0; acl \"My App can access cn=changelog\"; \
   allow (read,search,compare) \
   userdn=\"ldap:///cn=My App,ou=Apps,dc=example,dc=com\";)" \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

   The IDM liveSync feature requires access to the root DSE attributes `changeLog`, `firstChangeNumber`, and `lastChangeNumber`.

2. Give the user access to use the public changelog exchange control.

   The following example adds a global ACI to give `My App` access to use the control:

   ```console
   $ dsconfig \
    set-access-control-handler-prop \
    --add global-aci:"(targetcontrol=\"Ecl\")\
   (version 3.0; acl \"My App control access\"; \
   allow (read) \
   userdn=\"ldap:///cn=My App,ou=Apps,dc=example,dc=com\";)" \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

3. Give the user the `changelog-read` privilege:

   ```console
   $ ldapmodify \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN uid=admin \
    --bindPassword password << EOF
   dn: cn=My App,ou=Apps,dc=example,dc=com
   changetype: modify
   add: ds-privilege-name
   ds-privilege-name: changelog-read
   EOF
   ```

4. Check that the user can read the changelog:

   ```console
   $ ldapsearch \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN uid=admin \
    --bindPassword password \
    --baseDN cn=changelog \
    --control "ecl:true" \
    "(&)" \
    changes changeLogCookie targetDN
   ```

   |   |                                                                                                                                                                         |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The external changelog (`cn=changelog`) doesn't support the [Simple Paged Results](https://www.rfc-editor.org/info/rfc2696) LDAP control (OID: 1.2.840.113556.1.4.319). |

## Include unchanged attributes

The changes returned from a search on the external changelog include only what was actually changed. If you have applications that need additional attributes published with every changelog entry, regardless of whether the attribute itself has changed, specify those with the `ecl-include` and `ecl-include-for-deletes` properties:

1. Set the attributes to include for all update operations:

   ```console
   $ dsconfig \
    set-replication-domain-prop \
    --provider-name "Multimaster Synchronization" \
    --domain-name dc=example,dc=com \
    --set ecl-include:"@person" \
    --set ecl-include:entryUUID \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

   The `entryUUID` can be useful, for example, to ensure integrity when entries are renamed.

2. Set the attributes to include for deletes:

   ```console
   $ dsconfig \
    set-replication-domain-prop \
    --provider-name "Multimaster Synchronization" \
    --domain-name dc=example,dc=com \
    --add ecl-include-for-deletes:"*" \
    --add ecl-include-for-deletes:"+" \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

   With the default configuration, the changelog records only the DN of the deleted entry.

## Exclude a domain

Exclude domains to prevent applications that read the external changelog from having to process update notifications for entries that are not relevant to them:

1. Change the replication server configuration to exclude the domain by base DN.

   The following example prevents the changelog from sending notifications about Example.com entries:

   ```console
   $ dsconfig \
    set-replication-server-prop \
    --provider-name "Multimaster Synchronization" \
    --set changelog-enabled-excluded-domains:dc=example,dc=com \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

## Internet-Draft change numbers

The external changelog can support applications using the [Internet-Draft: Definition of an Object Class to Hold LDAP Change Records](https://datatracker.ietf.org/doc/html/draft-good-ldap-changelog-04) instead of changelog cookies.

The implementation has these characteristics:

* Replication servers must perform [Change number indexing](#ecl-configure-changenumber-indexer) to get the objects specified for this format.

* Change numbers described in the Internet-Draft are simple numbers, not cookies.

* Changelog numbers are ordered locally for each DS server. Each server keeps its own count. The same change numbers can refer to different changes on different servers. For example, if you manually initialize a server from another, the last change numbers are likely to differ.

The following example shows different last change numbers for two such servers:

```console
$ ldapsearch \
 --hostname existing-ds.example.com \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=admin \
 --bindPassword password \
 --baseDN "" \
 --searchScope base \
 "(&)" lastChangeNumber
```

> **Collapse: Show output**
>
> ```
> dn:
> lastChangeNumber: 285924
>
> Result Code:  0 (Success)
> ```

```console
$ ldapsearch \
 --hostname new-ds.example.com \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=admin \
 --bindPassword password \
 --baseDN "" \
 --searchScope base \
 "(&)" lastChangeNumber
```

> **Collapse: Show output**
>
> ```
> dn:
> lastChangeNumber: 198643
>
> Result Code:  0 (Success)
> ```

## Change number indexing

By default, replication servers let applications use cookies instead of change numbers when searching the changelog.

Adjust the replication server `changelog-enabled` settings appropriately on each replication server in your deployment:

* If applications need change notifications and use changelog cookies, leave the default setting `changelog-enabled: enabled-cookie-mode-only`.

* If applications need change notifications and use change numbers, use `changelog-enabled: enabled`.

  |   |                                                                                                                                            |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | Change number indexing requires more CPU, disk access, and storage. Enable it only when applications require change number-based browsing. |

* If no applications need notifications, use `changelog-enabled: disabled`.

* If applications need notifications for some domains but not for others, refer to [Exclude a domain](#ecl-exclude-domain).

---

---
title: Collective attributes
description: Configure PingDS collective attributes to automatically inherit attribute values across directory entries.
component: pingds
version: 8.1
page_id: pingds:config-guide:collective-attrs
canonical_url: https://docs.pingidentity.com/pingds/8.1/config-guide/collective-attrs.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Features", "LDAP", "Setup &amp; Configuration"]
section_ids:
  example-collective-attrs-cos: Class of service
  example-dept-from-manager: Inherit from the manager
  example-inherit-from-locality: Inherit from the locality
  example-inherit-from-parent: Inherit from a parent entry
  rename-attr: Rename an attribute
  subentry-scope: About subentry scope
---

# Collective attributes

Collective attributes provide a standard mechanism for inheriting attribute values. DS servers support standard collective attributes, described in [RFC 3671](https://www.rfc-editor.org/info/rfc3671). The inherited values appear on all the entries in a subtree, optionally filtered by object class. Standard collective attribute type names have the prefix `c-`.

DS servers extend collective attributes to make them easier to use. You can define any DS attribute as collective with the `;collective` attribute option. Use LDAP filters in the subtree specification for fine-grained control over which entries inherit the values.

You establish an inheritance relationship between entries by specifying one of the following:

* Which attribute holds the DN of the entry to inherit attributes from.

* How to construct the RDN of the entry to inherit attributes from.

## Class of service

This example defines attributes that depend on the user's service level.

This example shows collective attributes that depend on a `classOfService` attribute value:

* For entries with `classOfService: bronze`, `mailQuota` is 1 GB, and `diskQuota` is 10 GB.

* For entries with `classOfService: silver`, `mailQuota` is 5 GB, and `diskQuota` is 50 GB.

* For entries with `classOfService: gold`, `mailQuota` is 10 GB, and`diskQuota` is 100 GB.

You define collective attributes in the user data using an LDAP subentry. As a result, collective attribute settings are replicated. Collective attributes use attributes defined in the directory schema. The following LDAP Data Interchange Format (LDIF) *(tooltip: \<div class="paragraph">
\<p>An IETF standard file format for representing LDAP directory content and modifications to directory content. Typically used to import and export LDAP-based directory information.\</p>
\</div>)* shows the schema definitions:

```ldif
dn: cn=schema
changetype: modify
add: attributeTypes
attributeTypes: ( example-class-of-service-attribute-type
NAME 'classOfService'
EQUALITY caseIgnoreMatch
ORDERING caseIgnoreOrderingMatch
SUBSTR caseIgnoreSubstringsMatch
SYNTAX 1.3.6.1.4.1.1466.115.121.1.15
SINGLE-VALUE
USAGE userApplications
X-ORIGIN 'DS Documentation Examples' )
-
add: attributeTypes
attributeTypes: ( example-class-of-service-disk-quota
NAME 'diskQuota'
EQUALITY caseIgnoreMatch
ORDERING caseIgnoreOrderingMatch
SUBSTR caseIgnoreSubstringsMatch
SYNTAX 1.3.6.1.4.1.1466.115.121.1.15
USAGE userApplications
X-ORIGIN 'DS Documentation Examples' )
-
add: attributeTypes
attributeTypes: ( example-class-of-service-mail-quota
NAME 'mailQuota'
EQUALITY caseIgnoreMatch
ORDERING caseIgnoreOrderingMatch
SUBSTR caseIgnoreSubstringsMatch
SYNTAX 1.3.6.1.4.1.1466.115.121.1.15
USAGE userApplications
X-ORIGIN 'DS Documentation Examples' )
-
add: objectClasses
objectClasses: ( example-class-of-service-object-class
NAME 'cos'
SUP top
AUXILIARY
MAY ( classOfService $ diskQuota $ mailQuota )
X-ORIGIN 'DS Documentation Examples' )
```

The collective attribute definitions set the quotas depending on class of service:

```ldif
dn: cn=Bronze Class of Service,dc=example,dc=com
objectClass: collectiveAttributeSubentry
objectClass: extensibleObject
objectClass: subentry
objectClass: top
cn: Bronze Class of Service
diskQuota;collective: 10 GB
mailQuota;collective: 1 GB
subtreeSpecification: { base "ou=People", specificationFilter "(classOfService=bronze)" }

dn: cn=Silver Class of Service,dc=example,dc=com
objectClass: collectiveAttributeSubentry
objectClass: extensibleObject
objectClass: subentry
objectClass: top
cn: Silver Class of Service
diskQuota;collective: 50 GB
mailQuota;collective: 5 GB
subtreeSpecification: { base "ou=People", specificationFilter "(classOfService=silver)" }

dn: cn=Gold Class of Service,dc=example,dc=com
objectClass: collectiveAttributeSubentry
objectClass: extensibleObject
objectClass: subentry
objectClass: top
cn: Gold Class of Service
diskQuota;collective: 100 GB
mailQuota;collective: 10 GB
subtreeSpecification: { base "ou=People", specificationFilter "(classOfService=gold)" }
```

When the collective attributes are defined, you observe the results on user entries. Before trying this example, set up a directory server with the `ds-evaluation` profile:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 --baseDN dc=example,dc=com \
 "(uid=bjensen)" \
 classOfService mailQuota diskQuota
```

> **Collapse: Show output**
>
> ```
> dn: uid=bjensen,ou=People,dc=example,dc=com
> classOfService: bronze
> mailQuota: 1 GB
> diskQuota: 10 GB
> ```

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 --baseDN dc=example,dc=com \
 "(uid=kvaughan)" \
 classOfService mailQuota diskQuota
```

> **Collapse: Show output**
>
> ```
> dn: uid=kvaughan,ou=People,dc=example,dc=com
> classOfService: silver
> mailQuota: 5 GB
> diskQuota: 50 GB
> ```

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 --baseDN dc=example,dc=com \
 "(uid=scarter)" \
 classOfService mailQuota diskQuota
```

> **Collapse: Show output**
>
> ```
> dn: uid=scarter,ou=People,dc=example,dc=com
> classOfService: gold
> mailQuota: 10 GB
> diskQuota: 100 GB
> ```

## Inherit from the manager

This example demonstrates how to set an employee's department number using the manager's department number.

The employee-manager relationship is defined by the employee's `manager` attribute. Each `manager` attribute specifies the DN of a manager's entry. The server looks up the manager's department number to set the attribute on the employee's entry.

The collective attribute subentry specifies that users inherit department number from their manager:

```ldif
dn: cn=Inherit Department Number From Manager,dc=example,dc=com
objectClass: top
objectClass: subentry
objectClass: inheritedCollectiveAttributeSubentry
objectClass: inheritedFromDNCollectiveAttributeSubentry
cn: Inherit Department Number From Manager
subtreeSpecification: { base "ou=People", specificationFilter "(objectClass=posixAccount)" }
inheritFromDNAttribute: manager
inheritAttribute: departmentNumber
```

Babs Jensen's manager is Torrey Rigden:

```ldif
dn: uid=bjensen,ou=People,dc=example,dc=com
manager: uid=trigden, ou=People, dc=example,dc=com
```

Torrey's department number is 3001:

```ldif
dn: uid=trigden,ou=People,dc=example,dc=com
departmentNumber: 3001
```

Babs inherits her department number from Torrey. Before trying this example, set up a directory server with the `ds-evaluation` profile:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 --baseDN dc=example,dc=com \
 "(uid=bjensen)" \
 departmentNumber
```

> **Collapse: Show output**
>
> ```
> dn: uid=bjensen,ou=People,dc=example,dc=com
> departmentNumber: 3001
> ```

## Inherit from the locality

This example demonstrates how to set a user's default language preferences and street address based on locality.

For this example, the relationship between entries is based on locality. The collective attribute subentry specifies how to construct the RDN of the entry with the values to inherit:

```ldif
dn: cn=Inherit From Locality,dc=example,dc=com
objectClass: top
objectClass: subentry
objectClass: inheritedCollectiveAttributeSubentry
objectClass: inheritedFromRDNCollectiveAttributeSubentry
cn: Inherit From Locality
subtreeSpecification: { base "ou=People", specificationFilter "(objectClass=posixAccount)" }
inheritFromBaseRDN: ou=Locations
inheritFromRDNAttribute: l
inheritFromRDNType: l
inheritAttribute: preferredLanguage
inheritAttribute: street
collectiveConflictBehavior: real-overrides-virtual
```

The RDN of the entry from which to inherit attributes is `l=localityName,ou=Locations`, where localityName is the value of the `l` (`localityName`) attribute on the user's entry.

In other words, if the user's entry has `l: Bristol`, then the RDN of the entry from which to inherit attributes starts with `l=Bristol,ou=Locations`. The actual entry looks like this:

```ldif
dn: l=Bristol,ou=Locations,dc=example,dc=com
objectClass: top
objectClass: locality
objectClass: extensibleObject
l: Bristol
street: Broad Quay House, Prince Street
preferredLanguage: en-gb
```

The subentry specifies that the inherited attributes are preferred language and street address.

The object class `extensibleObject` allows the entry to take a preferred language. The object class `extensibleObject` means, "Let me add whatever attributes I want." The best practice is to add a custom auxiliary object class instead. The example uses shortcut `extensibleObject` for simplicity.

Notice the last line of the collective attribute subentry:

```
collectiveConflictBehavior: real-overrides-virtual
```

This line indicates that when a collective attribute clashes with a real attribute, the real value takes precedence over the virtual, collective value. You can set `collectiveConflictBehavior` to `virtual-overrides-real` for the opposite precedence, or to `merge-real-and-virtual` to keep both sets of values.

In this example, users can set their own language preferences. When users set language preferences manually, the user's settings override the locality-based setting.

Sam Carter is located in Bristol. Sam has specified no preferred languages:

```ldif
dn: uid=scarter,ou=People,dc=example,dc=com
l: Bristol
```

Sam inherits the street address and preferred language from the Bristol locality. Before trying this example, set up a directory server with the `ds-evaluation` profile:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 --baseDN dc=example,dc=com \
 "(uid=scarter)" \
 preferredLanguage street
```

> **Collapse: Show output**
>
> ```
> dn: uid=scarter,ou=People,dc=example,dc=com
> preferredLanguage: en-gb
> street: Broad Quay House, Prince Street
> ```

Babs's locality is San Francisco. Babs prefers English, but also knows Korean:

```ldif
dn: uid=bjensen,ou=People,dc=example,dc=com
preferredLanguage: en, ko;q=0.8
l: San Francisco
```

Babs inherits the street address from the San Francisco locality, but keeps her language preferences:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 --baseDN dc=example,dc=com \
 "(uid=bjensen)" \
 preferredLanguage street
```

> **Collapse: Show output**
>
> ```
> dn: uid=bjensen,ou=People,dc=example,dc=com
> preferredLanguage: en, ko;q=0.8
> street: 201 Mission Street Suite 2900
> ```

## Inherit from a parent entry

This example demonstrates how to inherit a description from the parent entry.

The following collective attribute subentry specifies that entries inherit a description from their parent unless they already have a description:

```ldif
dn: cn=Inherit Description From Parent,dc=example,dc=com
objectClass: top
objectClass: subentry
objectClass: inheritedCollectiveAttributeSubentry
objectClass: inheritedFromDNCollectiveAttributeSubentry
cn: Inherit Description From Parent
subtreeSpecification: { base "", minimum 2, specificationFilter "(objectClass=posixAccount)" }
inheritFromDNAttribute: entryDN
inheritFromDNParent: 1
inheritAttribute: description
collectiveConflictBehavior: real-overrides-virtual
```

In this example, `inheritFromDNAttribute` uses the virtual attribute `entryDN`. The setting `inheritFromDNParent: 1` indicates that the server should locate the parent entry by removing one leading RDN from the `entryDN`. (To inherit from the grandparent entry, you would specify `inheritFromDNParent: 2`, for example.)

Sam Carter's entry has no description attribute, and so inherits the parent's description:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 --baseDN dc=example,dc=com \
 "(uid=scarter)" \
 description
```

> **Collapse: Show output**
>
> ```
> dn: uid=scarter,ou=People,dc=example,dc=com
> description: Description on ou=People
> description: Served by my favorite directory server
> ```

Babs Jensen's entry already has a description attribute, and so does not inherit from the parent:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 --baseDN dc=example,dc=com \
 "(uid=bjensen)" \
 description
```

> **Collapse: Show output**
>
> ```
> dn: uid=bjensen,ou=People,dc=example,dc=com
> description: Original description
> ```

## Rename an attribute

You can rename a collective attribute with a special form of `inheritAttribute` value. In the collective attribute subentry, set:

```
inheritAttribute: <collective-attribute>:<inherited-attribute>
```

The following example inherits the `postalAddress` from the manager with the RFC 3671 name, `c-PostalAddress`:

```ldif
dn: cn=Inherit postal address from manager,dc=example,dc=com
objectClass: top
objectClass: subentry
objectClass: inheritedCollectiveAttributeSubentry
objectClass: inheritedFromDNCollectiveAttributeSubentry
cn: Inherit postal address from manager
subtreeSpecification: { base "ou=People", specificationFilter "(objectClass=posixAccount)" }
inheritFromDNAttribute: manager
inheritAttribute: postalAddress:c-PostalAddress
```

|   |                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The \<collective-attribute> must be defined in the LDAP schema.If the client uses the \<inherited-attribute to filter or sort, it must also be defined in the schema.In this example, the default LDAP schema defines both attributes. |

Try the example with the following steps:

1. Add the subentry:

   ```console
   $ ldapmodify \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN uid=admin \
    --bindPassword password << EOF
   dn: cn=Inherit postal address from manager,dc=example,dc=com
   objectClass: top
   objectClass: subentry
   objectClass: inheritedCollectiveAttributeSubentry
   objectClass: inheritedFromDNCollectiveAttributeSubentry
   cn: Inherit postal address from manager
   subtreeSpecification: { base "ou=People", specificationFilter "(objectClass=posixAccount)" }
   inheritFromDNAttribute: manager
   inheritAttribute: postalAddress:c-PostalAddress
   EOF
   ```

2. Add a `postalAddress` to the manager's entry:

   ```console
   $ ldapmodify \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN uid=admin \
    --bindPassword password << EOF
   dn: uid=trigden,ou=people,dc=example,dc=com
   changetype: modify
   add: postalAddress
   postalAddress: 1234 Main St.$Anytown, CA 12345$USA
   EOF
   ```

3. Read `c-PostalAddress` on the employee's entry:

   ```console
   $ ldapsearch \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
    --bindPassword bribery \
    --baseDN dc=example,dc=com \
    "(uid=bjensen)" \
    c-PostalAddress
   ```

   > **Collapse: Show output**
   >
   > ```
   > dn: uid=bjensen,ou=People,dc=example,dc=com
   > c-PostalAddress: 1234 Main St., CA 12345
   > ```

## About subentry scope

[LDAP subentries](https://www.rfc-editor.org/info/rfc3672) reside with the user data and so the server replicates them. Subentries hold operational data. They are not visible in search results unless explicitly requested. This section describes how a subentry's `subtreeSpecification` attribute defines the scope of the subtree that the subentry applies to.

An LDAP subentry's subtree specification identifies a subset of entries in a branch of the DIT. The subentry scope is these entries. In other words, these are the entries that the subentry affects.

The attribute value for a `subtreeSpecification` optionally includes the following parameters:

* `base`

  Indicates the entry, *relative to the subentry's parent*, at the base of the subtree.

  By default, the base is the subentry's parent.

* `specificationFilter`

  Indicates an LDAP filter. Entries matching the filter are in scope.

  DS servers extend the standard implementation to allow any search filter, not just an assertion about the `objectClass` attribute.

  By default, all entries under the base entry are in scope.

The following illustration shows this for an example collective attribute subentry:

![A subentry's subtreeSpecification defines the scope of the subtree that the subentry applies to.](../_images/subtree-specification.png)

Notice that the base of `ou=People` on the subentry `cn=Silver Class of Service,dc=example,dc=com` indicates that the base entry is `ou=People,dc=example,dc=com`.

The filter `"(classOfService=silver)"` means that Kirsten Vaughan and Sam Carter's entries are in scope. Babs Jensen's entry, with `classOfService: bronze` does not match and is therefore not in scope. The `ou=People` organizational unit entry does not have a `classOfService` attribute, and so is not in scope, either.

---

---
title: Configuration
description: Landing page for PingDS configuration documentation, with links to guides on HTTP, LDAP, storage, indexes, replication, and proxy.
component: pingds
version: 8.1
page_id: pingds:config-guide:preface
canonical_url: https://docs.pingidentity.com/pingds/8.1/config-guide/preface.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Features", "LDAP", "Setup &amp; Configuration"]
page_aliases: ["index.adoc"]
---

# Configuration

These pages show you how to configure DS server features.

[icon: cloud, set=fas, size=3x]

#### [HTTP](http-access.html)

Access DS over HTTP.

[icon: sitemap, set=fas, size=3x]

#### [LDAP](ldap-access.html)

Access DS over LDAP.

[icon: hdd, set=fas, size=3x]

#### [Storage](import-export.html)

Manage DS data.

[icon: list, set=fas, size=3x]

#### [Indexes](indexing.html)

Index DS data.

[icon: clone, set=fas, size=3x]

#### [Replication](replication.html)

Replicate DS data.

[icon: exchange-alt, set=fas, size=3x]

#### [LDAP Proxy](proxy.html)

Configure proxy features.

---

---
title: Configure indexes
description: Configure standard, JSON, and virtual list view indexes in PingDS using dsconfig, and rebuild indexes after configuration changes.
component: pingds
version: 8.1
page_id: pingds:config-guide:idx-config
canonical_url: https://docs.pingidentity.com/pingds/8.1/config-guide/idx-config.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-02T15:53:44Z
keywords: ["Features", "LDAP", "Setup &amp; Configuration"]
section_ids:
  configure-standard-index: Standard indexes
  create-index-example: New index
  approx-index-example: Approximate index
  extensible-match-index-example: Extensible match index
  use-big-indexes: Indexes for attributes with few unique values
  configure-json-index: Custom indexes for JSON
  index-json-attribute: Index JSON attributes
  json-index-example: JSON query matching rule index
  json-token-index-example: JSON equality matching rule index
  configure-vlv: Virtual list view index
  vlv-for-paged-sss: VLV for paged server-side sort
  rebuild-index: Rebuild indexes
  automate-index-rebuilds: Automate index rebuilds
  rebuild-index-example: Rebuild an index
  rebuild-all: Avoid rebuilding all indexes at once
  index-entry-limits: Index entry limits
  check-index-entry-limits: Check index entry limits
  over-the-limit-can-be-fine: On over index-entry-limit keys
  change-index-entry-limit: Index entry limit changes
---

# Configure indexes

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | You configure indexes with the `dsconfig` command in online or offline mode.DS doesn't automatically reindex existing data when you change an index configuration, however. "Automatic" index updates [only happen when directory data changes](idx-about.html#index-updates).After configuring an index, you can manually [rebuild the index](#rebuild-index) to force DS to update indexes from the existing directory data. |

The `dsconfig --help-database` command lists subcommands for creating, reading, updating, and deleting index configuration.

|   |                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Indexes are per directory backend rather than per base DN. To maintain separate indexes for different base DNs on the same server, put the entries in different backends. |

## Standard indexes

### New index

The following example creates a new equality index for the `description` attribute:

```console
$ dsconfig \
 create-backend-index \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --backend-name dsEvaluation \
 --index-name description \
 --set index-type:equality \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
```

### Approximate index

The following example adds an approximate index for the `sn` (surname) attribute:

```console
$ dsconfig \
 set-backend-index-prop \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --backend-name dsEvaluation \
 --index-name sn \
 --add index-type:approximate \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
```

Approximate indexes depend on the Double Metaphone matching rule.

### Extensible match index

DS servers support matching rules defined in LDAP RFCs. They also define DS-specific extensible matching rules.

The following are DS-specific extensible matching rules:

* Name: `ds-mr-double-metaphone-approx`

  Double Metaphone Approximate Match described at <http://aspell.net/metaphone/>. The DS implementation always produces a single value rather than one or possibly two values.

  Configure approximate indexes as described in [Approximate index](#approx-index-example).

  Find an example using this matching rule in [Approximate match](../ldap-guide/search-ldap.html#approximate-match-search).

* Name: `ds-mr-user-password-exact`

  User password exact matching rule used to compare encoded bytes of two hashed password values for exact equality.

* Name: `ds-mr-user-password-equality`

  User password matching rule implemented as the user password exact matching rule.

* Name: `partialDateAndTimeMatchingRule`

  Partial date and time matching rule for matching parts of dates in time-based searches.

  Find an example using this matching rule in [Active accounts](../ldap-guide/search-ldap.html#extensible-match-search).

* Name: `relativeTimeOrderingMatch.gt`

  Greater-than relative time matching rule for time-based searches.

  Find an example using this matching rule in [Active accounts](../ldap-guide/search-ldap.html#extensible-match-search).

* Name: `relativeTimeOrderingMatch.lt`

  Less-than relative time matching rule for time-based searches.

  Find an example using this matching rule in [Active accounts](../ldap-guide/search-ldap.html#extensible-match-search).

The following example configures an extensible matching rule index for "later than" and "earlier than" generalized time matching on the `ds-last-login-time` attribute:

```console
$ dsconfig \
 create-backend-index \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --backend-name dsEvaluation \
 --set index-type:extensible \
 --set index-extensible-matching-rule:1.3.6.1.4.1.26027.1.4.5 \
 --set index-extensible-matching-rule:1.3.6.1.4.1.26027.1.4.6 \
 --index-name ds-last-login-time \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
```

Notice the `index-extensible-matching-rule` setting takes an OID, not the name of the matching rule.

## Indexes for attributes with few unique values

[Big indexes](idx-types.html#big-indexes) fit the case where many, many entries have the same attribute value.

The default DS evaluation profile generates 100,000 user entries with addresses in the United States, so some `st` (state) attributes are shared by 4000 or more users. With a regular equality index, searches for some states reach the [index entry limit](#index-entry-limits), causing unindexed searches. A big index avoids this problem.

The following commands configure an equality index for the state attribute, and then build the new index:

```console
$ dsconfig \
 create-backend-index \
 --backend-name dsEvaluation \
 --index-name st \
 --set index-type:big-equality \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
$ rebuild-index \
 --baseDn dc=example,dc=com \
 --index st \
 --hostname localhost \
 --port 4444 \
 --bindDn uid=admin \
 --bindPassword password \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin
```

Once the index is ready, a client application can page through all the users in a state with an indexed search:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=bjensen,ou=People,dc=example,dc=com \
 --bindPassword hifalutin \
 --baseDn dc=example,dc=com \
 --simplePageSize 5 \
 "(st=CA)" \
 cn
```

> **Collapse: Show output**
>
> ```
> dn: uid=user.9,ou=People,dc=example,dc=com
> cn: Abbe Abbate
>
> dn: uid=user.123,ou=People,dc=example,dc=com
> cn: Aili Aksel
>
> dn: uid=user.124,ou=People,dc=example,dc=com
> cn: Ailina Akyurekli
>
> dn: uid=user.132,ou=People,dc=example,dc=com
> cn: Ainslee Alary
>
> dn: uid=user.264,ou=People,dc=example,dc=com
> cn: Alphen Angell
>
> Press RETURN to continue
> ```

When creating a big index that uses an extensible matching rule, model your work on the example in [Extensible match index](#extensible-match-index-example). Use the following options to set the index type and the matching rule. You must set at least one `big-index-extensible-matching-rule`:

* `--set index-type:big-extensible`

* `--set big-index-extensible-matching-rule:OID`

  Notice the `big-index-extensible-matching-rule` setting takes an OID, not the name of the matching rule.

  The *OID* must specify an equality matching rule for big indexes. For example, to create a big index for the `sn` (surname) attribute with `caseIgnoreMatch`, use `--set big-index-extensible-matching-rule:2.5.13.2`. To create a big index for password storage schemes, use `--set big-index-extensible-matching-rule:1.3.6.1.4.1.36733.2.1.4.14`.

## Custom indexes for JSON

DS servers support attributes containing JSON objects. JSON objects have their own structure and call for special index configuration.

The following schema excerpt defines a `json` attribute with case-insensitive matching:

```ldif
attributeTypes: ( json-attribute-oid NAME 'json'
  SYNTAX 1.3.6.1.4.1.36733.2.1.3.1 EQUALITY caseIgnoreJsonQueryMatch
  X-ORIGIN 'DS Documentation Examples' )
```

When configuring indexes for JSON attributes, you can index individual JSON fields or the entire object. If the JSON objects have a unique identifier field, you can even index only the unique ID to optimize equality searches.

The more data you index, the more server resources DS uses to maintain the index:

* When storing a JSON object in an LDAP attribute, avoid storing the same data in separate LDAP attributes.

  DS can index both the JSON object and the separate LDAP attributes, but storing and indexing duplicate data wastes server resources.

* By default, DS maintains index keys for each field of a JSON object. This can waste server resources.

  When you know all the JSON fields applications' search filters use, [index only those fields](#json-index-example).

  For JSON objects with a unique identifier field, [index only that field for equality matching](#json-token-index-example). In this case, DS can quickly check whether two objects match by comparing their identifiers.

* Use single-valued JSON attributes unless applications require storing multiple objects.

  When LDAP attributes have multiple values, DS indexes each value—​each JSON object in this case. For equivalent index configurations, a single-valued LDAP attribute means less data to index than a multivalued version of the same LDAP attribute.

  The [LDAP schema](schema.html#json-in-ldap) determines whether a JSON attribute is single-valued.

### Index JSON attributes

The examples that follow demonstrate these steps:

1. Use the schema definition and the information in the following table to configure a custom schema provider for the attribute's matching rule where possible:

   | Matching rule in schema definition                  | Fields in search filter       | Custom schema provider required?                                         |
   | --------------------------------------------------- | ----------------------------- | ------------------------------------------------------------------------ |
   | `caseExactJsonQueryMatch``caseIgnoreJsonQueryMatch` | Any JSON field                | No                                                                       |
   | Custom JSON query matching rule                     | Specific JSON field or fields | YesUse a [JSON query matching rule index](#json-index-example).          |
   | Custom JSON equality or ordering matching rule      | Specific field(s)             | YesUse a [JSON equality matching rule index](#json-token-index-example). |

   A custom schema provider applies to all attributes using this matching rule.

2. Add the schema definition for the JSON attribute.

3. Configure the index for the JSON attribute.

4. Add the JSON attribute values in the directory data.

### JSON query matching rule index

This example illustrates the steps in [Index JSON attributes](#index-json-attribute).

|   |                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------ |
|   | If you installed a directory server with the `ds-evaluation` profile, the custom index configuration is already present. |

The following command configures a custom, case-insensitive JSON query matching rule. This only maintains keys for the `access_token` and `refresh_token` fields:

```console
$ dsconfig \
 create-schema-provider \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --provider-name "Custom JSON Query Matching Rule" \
 --type json-query-equality-matching-rule \
 --set enabled:true \
 --set case-sensitive-strings:false \
 --set ignore-white-space:true \
 --set matching-rule-name:caseIgnoreOAuth2TokenQueryMatch \
 --set matching-rule-oid:1.3.6.1.4.1.36733.2.1.4.1.1 \
 --set indexed-field:access_token \
 --set indexed-field:refresh_token \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
```

The following commands add schemas for an `oauth2Token` attribute that uses the matching rule:

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=admin \
 --bindPassword password << EOF
dn: cn=schema
changetype: modify
add: attributeTypes
attributeTypes: ( oauth2token-attribute-oid NAME 'oauth2Token'
  SYNTAX 1.3.6.1.4.1.36733.2.1.3.1 EQUALITY caseIgnoreOAuth2TokenQueryMatch
  SINGLE-VALUE X-ORIGIN 'DS Documentation Examples' )
-
add: objectClasses
objectClasses: ( oauth2token-attribute-oid NAME 'oauth2TokenObject' SUP top
  AUXILIARY MAY ( oauth2Token ) X-ORIGIN 'DS Documentation Examples' )
EOF
```

The following command configures an index using the custom matching rule implementation:

```console
$ dsconfig \
 create-backend-index \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --backend-name dsEvaluation \
 --index-name oauth2Token \
 --set index-type:equality \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
```

[Rebuild the index](#rebuild-index) to populate the new index from existing directory data.

Find an example of how a client application could use this index in [JSON query filters](../ldap-guide/search-ldap.html#json-search).

### JSON equality matching rule index

This example illustrates the steps in [Index JSON attributes](#index-json-attribute).

|   |                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------ |
|   | If you installed a directory server with the `ds-evaluation` profile, the custom index configuration is already present. |

The following command configures a custom, case-insensitive JSON equality matching rule, `caseIgnoreJsonTokenIdMatch`:

```console
$ dsconfig \
 create-schema-provider \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --provider-name "Custom JSON Token ID Matching Rule" \
 --type json-equality-matching-rule \
 --set enabled:true \
 --set case-sensitive-strings:false \
 --set ignore-white-space:true \
 --set matching-rule-name:caseIgnoreJsonTokenIDMatch \
 --set matching-rule-oid:1.3.6.1.4.1.36733.2.1.4.4.1 \
 --set json-keys:id \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
```

Notice that this example defines a matching rule with OID `1.3.6.1.4.1.36733.2.1.4.4.1`. In production deployments, use a numeric OID allocated for your own organization.

The following commands add schemas for a `jsonToken` attribute, where the unique identifier is in the "id" field of the JSON object:

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=admin \
 --bindPassword password << EOF
dn: cn=schema
changetype: modify
add: attributeTypes
attributeTypes: ( jsonToken-attribute-oid NAME 'jsonToken'
  SYNTAX 1.3.6.1.4.1.36733.2.1.3.1 EQUALITY caseIgnoreJsonTokenIDMatch
  SINGLE-VALUE X-ORIGIN 'DS Documentation Examples' )
-
add: objectClasses
objectClasses: ( json-token-object-class-oid NAME 'JsonTokenObject' SUP top
  AUXILIARY MAY ( jsonToken ) X-ORIGIN 'DS Documentation Examples' )
EOF
```

The following command configures an index using the custom matching rule implementation:

```console
$ dsconfig \
 create-backend-index \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --backend-name dsEvaluation \
 --index-name jsonToken \
 --set index-type:equality \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
```

[Rebuild the index](#rebuild-index) to populate the new index from existing directory data.

Find an example of how a client application could use this index in [JSON assertions](../ldap-guide/search-ldap.html#json-token-search).

## Virtual list view index

The following example shows how to create a VLV index. This example applies where GUI users browse user accounts, sorting on surname then given name:

```console
$ dsconfig \
 create-backend-vlv-index \
 --hostname localhost \
 --port 4444 \
 --bindDn uid=admin \
 --bindPassword password \
 --backend-name dsEvaluation \
 --index-name people-by-last-name \
 --set base-dn:ou=People,dc=example,dc=com \
 --set filter:"(|(givenName=*)(sn=*))" \
 --set scope:single-level \
 --set sort-order:"+sn +givenName" \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
```

|   |                                                                                                                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When referring to a VLV index after creation, you must add `vlv.` as a prefix. In other words, if you named the VLV index `people-by-last-name`, refer to it as `vlv.people-by-last-name` when rebuilding indexes, changing index properties such as the index entry limit, or verifying indexes. |

### VLV for paged server-side sort

A special VLV index lets the server return sorted results. For example, users page through an entire directory database in a GUI. The user does not filter the data before displaying what is available.

The VLV index must have the following characteristics:

* Its filter must be "always true," `(&)`.

* Its scope must cover the search scope of the requests.

* Its base DN must match or be a parent of the base DN of the search requests.

* Its sort order must match the sort keys of the requests in the order they occur in the requests, starting with the first sort key used in the request.

  For example, if the sort order of the VLV index is `+l +sn +cn`, then it works with requests having the following sort orders:

  * `+l +sn +cn`

  * `+l +sn`

  * `+l`

  * Or none for single-level searches.

  The VLV index sort order can include additional keys not present in a request.

The following example commands demonstrate creating and using a VLV index to sort paged results by locality, surname, and then full name. The `l` attribute is not indexed by default. This example makes use of the `rebuild-index` command described below. The directory superuser is not subject to resource limits on the LDAP search operation:

```console
$ dsconfig \
 create-backend-vlv-index \
 --hostname localhost \
 --port 4444 \
 --bindDn uid=admin \
 --bindPassword password \
 --backend-name dsEvaluation \
 --index-name by-name \
 --set base-dn:ou=People,dc=example,dc=com \
 --set filter:"(&)" \
 --set scope:subordinate-subtree \
 --set sort-order:"+l +sn +cn" \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
$ rebuild-index \
 --hostname localhost \
 --port 4444 \
 --bindDn uid=admin \
 --bindPassword password \
 --baseDn dc=example,dc=com \
 --index vlv.by-name \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDn uid=admin \
 --bindPassword password \
 --baseDn dc=example,dc=com \
 --sortOrder +l,+sn,+cn \
 --simplePageSize 5 \
 "(&)" \
 cn l sn
```

> **Collapse: Show output**
>
> ```
> dn: uid=user.93953,ou=People,dc=example,dc=com
> cn: Access Abedi
> l: Abilene
> sn: Abedi
>
> dn: uid=user.40283,ou=People,dc=example,dc=com
> cn: Achal Abernathy
> l: Abilene
> sn: Abernathy
>
> dn: uid=user.67240,ou=People,dc=example,dc=com
> cn: Alaine Alburger
> l: Abilene
> sn: Alburger
>
> dn: uid=user.26994,ou=People,dc=example,dc=com
> cn: Alastair Alexson
> l: Abilene
> sn: Alexson
>
> dn: uid=user.53853,ou=People,dc=example,dc=com
> cn: Alev Allen
> l: Abilene
> sn: Allen
>
> Press RETURN to continue ^C
> ```

You can also list the results with HDAP:

```console
$ curl \
 --get \
 --cacert ca-cert.pem \
 --user uid=admin:password \
 --data '_queryFilter=true' \
 --data '_fields=cn,l,sn' \
 --data '_sortKeys=l,sn,cn' \
 --data '_pageSize=5' \
 --data '_prettyPrint=true' \
 --data 'scope=sub' \
 'https://localhost:8443/hdap/dc=com/dc=example/ou=People'
```

> **Collapse: Show output**
>
> ```
> {
>   "result" : [ {
>     "_id" : "dc=com/dc=example/ou=People/uid=user.93953",
>     "_rev" : "<revision>",
>     "cn" : [ "Access Abedi" ],
>     "l" : [ "Abilene" ],
>     "sn" : [ "Abedi" ]
>   }, {
>     "_id" : "dc=com/dc=example/ou=People/uid=user.40283",
>     "_rev" : "<revision>",
>     "cn" : [ "Achal Abernathy" ],
>     "l" : [ "Abilene" ],
>     "sn" : [ "Abernathy" ]
>   }, {
>     "_id" : "dc=com/dc=example/ou=People/uid=user.67240",
>     "_rev" : "<revision>",
>     "cn" : [ "Alaine Alburger" ],
>     "l" : [ "Abilene" ],
>     "sn" : [ "Alburger" ]
>   }, {
>     "_id" : "dc=com/dc=example/ou=People/uid=user.26994",
>     "_rev" : "<revision>",
>     "cn" : [ "Alastair Alexson" ],
>     "l" : [ "Abilene" ],
>     "sn" : [ "Alexson" ]
>   }, {
>     "_id" : "dc=com/dc=example/ou=People/uid=user.53853",
>     "_rev" : "<revision>",
>     "cn" : [ "Alev Allen" ],
>     "l" : [ "Abilene" ],
>     "sn" : [ "Allen" ]
>   } ],
>   "resultCount" : 5,
>   "pagedResultsCookie" : "<cookie>",
>   "totalPagedResultsPolicy" : "NONE",
>   "totalPagedResults" : -1,
>   "remainingPagedResults" : -1
> }
> ```

## Rebuild indexes

When you first import directory data, the directory server builds the indexes as part of the import process. DS servers maintain indexes automatically, updating them as directory data changes.

Only rebuild an index manually when it is necessary to do so. Rebuilding valid indexes wastes server resources, and is disruptive for client applications.

|   |                                                                                                                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When you rebuild an index while the server is online, the index appears as untrusted and unavailable while the server rebuilds it.A search request that relies on an index in this state *may temporarily fail as an unindexed search*. |

However, you must manually intervene when you:

* Create a new index for a new directory attribute.

* Create a new index for an existing directory attribute.

* Change the server configuration in a way that affects the index, for example, by changing [Index entry limits](#index-entry-limits).

* Verify an existing index, and find that it has errors or is not in a valid state.

### Automate index rebuilds

To automate the process of rebuilding indexes, use the `--rebuildUntrusted` option. This rebuilds only untrusted indexes, and does not affect valid indexes:

```console
$ rebuild-index \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --baseDN dc=example,dc=com \
 --rebuildUntrusted \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin
```

### Rebuild an index

When you make a change that affects an index configuration, manually rebuild the index.

Individual indexes appear as untrusted and are unavailable while the server rebuilds them. A search request that relies on an index in this state *may temporarily fail as an unindexed search*.

The following example rebuilds an untrusted `cn` index immediately with the server online.

While the server is rebuilding the `cn` index, *search requests that would normally succeed may fail*:

```console
$ rebuild-index \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --baseDN dc=example,dc=com \
 --index cn \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin
```

### Avoid rebuilding all indexes at once

Rebuilding multiple trusted indexes at once is disruptive. Only do it when a change has affected all indexes.

If you use the `--rebuildAll` option, first take the backend offline, stop the server, or, at minimum, make sure that no applications connect to the server while it is rebuilding indexes.

## Index entry limits

An index is a tree of key-value pairs. The key is what the search is trying to match. The value is a list of entry IDs.

As the number of entries in the directory grows, the list of entry IDs for some keys can become very large. For example, every entry in the directory has `objectClass: top`. If the directory maintains a substring index for `mail`, the number of entries ending in `.com` could be huge.

A directory server therefore defines an index entry limit *(tooltip: \<div class="paragraph">
\<p>The maximum number of entries listed for an index key, beyond which the server stops maintaining the list for that key.\</p>
\</div>)*. When the number of entry IDs for a key exceeds the limit, the server stops maintaining a list of IDs for that key. The limit effectively means a search using only that key is unindexed. Searches using other keys in the same index are not affected.

The following figure shows a fragment from a substring index for the `mail` attribute. The number of email addresses ending in `com` has exceeded the index entry limit. For the other substring keys, the entry ID lists are still maintained. To save space, the entry IDs are not shown in the figure.

![Illustration of the index entry limit reached for the substring .COM](../_images/index-entry-limit.png)

Ideally, the limit is set at the point where it becomes more expensive to maintain the entry ID list for a key, and to perform an indexed search than to perform an unindexed search. In practice, the limit is a tradeoff, with a default index entry limit value of 4000. Keep the default setting unless you have good reason to change it.

### Check index entry limits

The following steps show how to get information about indexes where the index entry limit is exceeded for some keys. In this case, the directory server holds 100,000 user entries.

Use the `backendstat show-index-status` command:

1. (Optional) Stop DS servers before you use the `backendstat` command:

   ```console
   $ stop-ds
   ```

2. Non-zero values in the **Over** column of the output table indicate the number of keys for which the `index-entry-limit` setting has been exceeded. The keys that are over the limit are then listed below the table:

   ```console
   $ backendstat show-index-status --baseDN dc=example,dc=com
   ```

   > **Collapse: Show output**
   >
   > ```
   >   Index Name                                          ...Over  Entry Limit...
   > ------------------------------------------------------...-----------------...
   >   ...                                                 ...
   >   cn.caseIgnoreSubstringsMatch:6                      ...  14         4000...
   >   ...                                                 ...
   >   givenName.caseIgnoreSubstringsMatch:6               ...   9         4000...
   >   ...                                                 ...
   >   mail.caseIgnoreIA5SubstringsMatch:6                 ...  31         4000...
   >   ...                                                 ...
   >   objectClass.objectIdentifierMatch                   ...   4         4000...
   >   ...                                                 ...
   >   sn.caseIgnoreSubstringsMatch:6                      ...  14         4000...
   >   ...                                                 ...
   >   telephoneNumber.telephoneNumberSubstringsMatch:6    ...  10         4000...
   >   ...
   >
   > Index: mail.caseIgnoreIA5SubstringsMatch:6
   > Over index-entry-limit keys: [.com] [0@exam] ...
   >
   > Index: cn.caseIgnoreSubstringsMatch:6
   > Over index-entry-limit keys: [a] [an] [e] [er] [i] [k] [l] [n] [o] [on] [r] [s] [t] [y]
   >
   > Index: givenName.caseIgnoreSubstringsMatch:6
   > Over index-entry-limit keys: [a] [e] [i] [ie] [l] [n] [na] [ne] [y]
   >
   > Index: telephoneNumber.telephoneNumberSubstringsMatch:6
   > Over index-entry-limit keys: [0] [1] [2] [3] [4] [5] [6] [7] [8] [9]
   >
   > Index: sn.caseIgnoreSubstringsMatch:6
   > Over index-entry-limit keys: [a] [an] [e] [er] [i] [k] [l] [n] [o] [on] [r] [s] [t] [y]
   >
   > Index: objectClass.objectIdentifierMatch
   > Over index-entry-limit keys: [inetorgperson] [organizationalperson] [person] [top]
   > ```

   For example, every user entry has the object classes listed, and every user entry has an email address ending in `.com`, so those values are not specific enough to be used in search filters.

   A non-zero value in the **Over** column represents a tradeoff. As described above, this is usually a good tradeoff, not a problem to be solved.

   Find a detailed explanation of each column of the output in [backendstat show-index-status](../tools-reference/backendstat.html#backendstat_show_index_status).

3. If you stopped the server, start it again:

   ```console
   $ start-ds
   ```

### On over index-entry-limit keys

The settings for this directory server are a good tradeoff. Unless you are observing many unindexed searches targeting keys in the `Over index-entry-limit keys` lists, there's no reason to change the `index-entry-limit` settings.

*A search might be indexed even though some keys are over the limit.*

For example, as shown above, the `objectClass` value `inetorgperson` is over the limit. Yet, a search with a filter like `(&(cn=Babs Jensen)(objectclass=inetOrgPerson))` is indexed:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=user.1,ou=people,dc=example,dc=com \
 --bindPassword password \
 --baseDN dc=example,dc=com \
 "(&(cn=Babs Jensen)(objectclass=inetOrgPerson))" cn
```

> **Collapse: Show output**
>
> ```
> dn: uid=bjensen,ou=People,dc=example,dc=com
> cn: Barbara Jensen
> cn: Babs Jensen
> ```

The search is indexed because the equality index for `cn` is not over the limit, so the search term `(cn=Babs Jensen)` is enough for DS to find a match using that index.

If you look at the `debugsearchindex` output, you observe how DS uses the `cn` index, and skips the `objectclass` index. The overall search is clearly indexed:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=admin \
 --bindPassword password \
 --baseDN dc=example,dc=com \
 "(&(cn=Babs Jensen)(objectclass=inetOrgPerson))" \
 debugsearchindex | sed -n -e "s/^debugsearchindex: //p"
```

> **Collapse: Show debugsearchindex output**
>
> ```
> {
>     "baseDn": "dc=example,dc=com",
>     "scope": "sub",
>     "filter": "(&(cn=Babs Jensen)(objectclass=inetOrgPerson))",
>     "maxCandidateSize": 100000,
>     "lookThroughLimit": 0,
>     "strategies": [
>         {
>             "name": "BaseObjectSearchStrategy",
>             "diagnostic": "not applicable",
>             "lookedThrough": 0
>         },
>         {
>             "name": "VlvSearchStrategy",
>             "diagnostic": "not applicable",
>             "lookedThrough": 0
>         },
>         {
>             "name": "AttributeIndexSearchStrategy",
>             "filter": {
>                 "query": "INTERSECTION",
>                 "rank": "EXACT_MATCH",
>                 "filter": "(&(cn=Babs Jensen)(objectclass=inetOrgPerson))",
>                 "subQueries": [
>                     {
>                         "query": "FIRST_OF",
>                         "rank": "EXACT_MATCH",
>                         "filter": "(cn=Babs Jensen)",
>                         "subQueries": [
>                             {
>                                 "query": "EXACT_MATCH",
>                                 "rank": "EXACT_MATCH",
>                                 "filter": "(cn=Babs Jensen)",
>                                 "index": "cn.caseIgnoreMatch",
>                                 "key": "babs jensen",
>                                 "diagnostic": "indexed",
>                                 "candidates": 1
>                             },
>                             {
>                                 "query": "MATCH_ALL",
>                                 "rank": "MATCH_ALL",
>                                 "filter": "(cn=Babs Jensen)",
>                                 "index": "cn.presence",
>                                 "diagnostic": "skipped"
>                             }
>                         ],
>                         "diagnostic": "indexed",
>                         "candidates": 1,
>                         "retained": 1
>                     },
>                     {
>                         "query": "FIRST_OF",
>                         "rank": "OBJECT_CLASS_EQUALITY_MATCH",
>                         "filter": "(objectclass=inetOrgPerson)",
>                         "subQueries": [
>                             {
>                                 "query": "OBJECT_CLASS_EQUALITY_MATCH",
>                                 "rank": "OBJECT_CLASS_EQUALITY_MATCH",
>                                 "filter": "(objectclass=inetOrgPerson)",
>                                 "subQueries": [
>                                     {
>                                         "query": "EXACT_MATCH",
>                                         "rank": "EXACT_MATCH",
>                                         "index": "objectClass.objectIdentifierMatch",
>                                         "key": "inetorgperson",
>                                         "diagnostic": "skipped"
>                                     },
>                                     {
>                                         "query": "EXACT_MATCH",
>                                         "rank": "EXACT_MATCH",
>                                         "index": "objectClass.objectIdentifierMatch",
>                                         "key": "2.16.840.1.113730.3.2.2",
>                                         "diagnostic": "skipped"
>                                     }
>                                 ],
>                                 "diagnostic": "skipped"
>                             },
>                             {
>                                 "query": "MATCH_ALL",
>                                 "rank": "MATCH_ALL",
>                                 "filter": "(objectclass=inetOrgPerson)",
>                                 "index": "objectClass.presence",
>                                 "diagnostic": "skipped"
>                             }
>                         ],
>                         "diagnostic": "skipped"
>                     }
>                 ],
>                 "diagnostic": "indexed",
>                 "candidates": 1
>             },
>             "diagnostic": "indexed",
>             "candidates": 1,
>             "lookedThrough": 1
>         },
>         {
>             "name": "BigIndexSearchStrategy",
>             "diagnostic": "skipped"
>         },
>         {
>             "name": "UnindexedSearchStrategy",
>             "diagnostic": "skipped"
>         }
>     ],
>     "lookedThrough": 1,
>     "final": 1
> }
> ```

### Index entry limit changes

In rare cases, the index entry limit might be too low for a certain key. This could manifest itself as a frequent, useful search becoming unindexed with no reasonable way to narrow the search.

You can change the index entry limit on a per-index basis. Do not do this in production unless you can explain and show why the benefits outweigh the costs.

|   |                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Changing the index entry limit significantly can result in serious performance degradation. Be prepared to test performance thoroughly before you roll out an index entry limit change in production. |

To configure the `index-entry-limit` for an index or a backend:

* Use the `dsconfig set-backend-index-prop` command to change the setting for a specific backend index.

* (Not recommended) Use the `dsconfig set-backend-prop` command to change the setting for all indexes in the backend.

---

---
title: Data storage
description: Manage PingDS data storage backends, including creating and deleting backends, importing and exporting LDIF, and entry expiration.
component: pingds
version: 8.1
page_id: pingds:config-guide:import-export
canonical_url: https://docs.pingidentity.com/pingds/8.1/config-guide/import-export.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Backup &amp; Restore", "Features", "LDAP", "Setup &amp; Configuration", "Storage"]
section_ids:
  create-database-backend: Create a backend
  importing-exporting-ldif: Import and export
  import-ldif: Import LDIF
  export-ldif: Export LDIF
  split-data: Subordinate backends
  set-database-backend-disk-thresholds: Disk space thresholds
  backend-ttl: Entry expiration
  update-database-backend: Add a base DN to a backend
  delete-database-backend: Delete a backend
---

# Data storage

DS directory servers store data in backends *(tooltip: \<div class="paragraph">
\<p>A repository to store directory data. Different implementations with different capabilities exist.\</p>
\</div>)*. A backend is a private server repository implemented in memory, as an LDAP Data Interchange Format (LDIF) *(tooltip: \<div class="paragraph">
\<p>An IETF standard file format for representing LDAP directory content and modifications to directory content. Typically used to import and export LDAP-based directory information.\</p>
\</div>)* file, or as an embedded database.

Embedded database backends have these characteristics:

* Suitable for large numbers of entries

  When creating a database backend, you choose the backend type. DS directory servers use JE backends for local data.

  The JE backend type is implemented using B-tree data structures. It stores data as key-value pairs, which is different from the model used by relational databases.

  JE backends are designed to hold hundreds of millions, or even billions of LDAP entries.

* Fully managed by DS servers

  Let the server manage its backends and their database files.

  By default, backend database files are located under the `opendj/db` directory.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | Do not compress, tamper with, or otherwise alter backend database files directly, unless specifically instructed to do so by a qualified technical support engineer. External changes to backend database files can render them unusable by the server.If you use snapshot technology for backup, read [Back up using snapshots](../maintenance-guide/backup-restore.html#backup-snapshot) and [Restore from a snapshot](../maintenance-guide/backup-restore.html#restore-snapshot). |

  DS servers provide the `dsbackup` command for backing up and restoring database backends. For details, refer to [Backup and restore](../maintenance-guide/backup-restore.html).

* Self-cleaning

  A JE backend stores data on disk using append-only log files with names like `number.jdb`. The JE backend writes updates to the highest-numbered log file. The log files grow until they reach a specified size (default: 1 GB). When the current log file reaches the specified size, the JE backend creates a new log file.

  To avoid an endless increase in database size on disk, JE backends clean their log files in the background. A cleaner thread copies active records to new log files. Log files that no longer contain active records are deleted.

  Due to the cleanup processes, JE backends can actively write to disk, even when there are no pending client or replication operations.

* Configurable I/O behavior

  By default, JE backends let the operating system potentially cache data for a period of time before flushing the data to disk. This setting trades full durability with higher disk I/O for good performance with lower disk I/O.

  With this setting, it is possible to lose the most recent updates that were not yet written to disk, in the event of an underlying OS or hardware failure.

  You can modify this behavior by changing the advanced configuration settings for the JE backend. If necessary, you can change the advanced setting, [db-durability](../configref/objects-je-backend.html#db-durability), using the `dsconfig set-backend-prop` command.

* Automatic recovery

  When a JE backend is opened, it recovers by recreating its B-tree structure from its log files.

  This is a normal process. It lets the backend recover after an orderly shutdown or after a crash.

* Automatic verification

  JE backends run checksum verification periodically on the database log files.

  If the verification process detects backend database corruption, then the server logs an error message and takes the backend offline. If this happens, restore the corrupted backend from backup so that it can be used again.

  By default, the verification runs every night at midnight local time. If necessary, you can change this behavior by adjusting the advanced settings, [db-run-log-verifier](../configref/objects-je-backend.html#db-run-log-verifier) and [db-log-verifier-schedule](../configref/objects-je-backend.html#db-log-verifier-schedule), using the `dsconfig set-backend-prop` command.

* Encryption support

  JE backends support encryption for data confidentiality.

  For details, refer to [Data encryption](../security-guide/data.html).

Depending on the setup profiles used at installation time, DS servers have backends with the following default settings:

| Backend         | Type      | Optional?(1) | Replicated? | Part of Backup? | Details                                                                                                                                                                                                          |
| --------------- | --------- | ------------ | ----------- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| adminRoot       | LDIF      | No           | If enabled  | If enabled      | Symmetric keys for (deprecated) reversible password storage schemes.Base DN: `cn=admin data`Base directory: `db/adminRoot`                                                                                       |
| amCts           | JE        | Yes          | Yes         | Yes             | AM core token store (CTS) data.More information: [Install DS for AM CTS](../install-guide/profile-am-cts.html).Base DN: `ou=tokens`Base directory: `db/amCts`                                                    |
| amIdentityStore | JE        | Yes          | Yes         | Yes             | AM identities.More information: [Install DS for platform identities](../install-guide/profile-am-idrepo.html).Base DN: `ou=identities`Base directory: `db/amIdentityStore`                                       |
| cfgStore        | JE        | Yes          | Yes         | Yes             | AM configuration, policy, and other data.More information: [Install DS for AM configuration](../install-guide/profile-am-config.html).Base DN: `ou=am-config`Base directory: `db/cfgStore`                       |
| changelogDb     | Changelog | Yes(2)       | N/A         | No              | Change data for replication and change notifications.More information: [Changelog for notifications](changelog.html).Base DN: `cn=changelog`Base directory: `changelogDb`                                        |
| config          | Config    | No           | N/A         | No              | File-based representation of this server's configuration.Do not edit `config/config.ldif` directly. Use the `dsconfig` command instead.Base DN: `cn=config`Base directory: `config`                              |
| dsEvaluation    | JE        | Yes          | Yes         | Yes             | Example.com sample data.More information: [Install DS for evaluation](../install-guide/setup-ds.html).Base DN: `dc=example,dc=com`Base directory: `db/dsEvaluation`                                              |
| idmRepo         | JE        | Yes          | Yes         | Yes             | IDM repository data.More information: [Install DS as an IDM repository](../install-guide/profile-idm-repo.html).Base DN: `dc=openidm,dc=example,dc=com`Base directory: `db/idmRepo`                              |
| monitor         | Monitor   | No           | N/A         | N/A             | Single entry; volatile monitoring metrics maintained in memory since server startup.More information: [LDAP-based monitoring](../monitoring-guide/ldap-monitoring.html).Base DN: `cn=monitor`Base directory: N/A |
| monitorUser     | LDIF      | Yes          | Yes         | Yes             | Single entry; default monitor user account.Base DN: `uid=Monitor`Base directory: `db/monitorUser`                                                                                                                |
| rootUser        | LDIF      | No(3)        | No          | Yes             | Single entry; default directory superuser account.Base DN: `uid=admin`Base directory: `db/rootUser`                                                                                                              |
| root DSE        | Root DSE  | No           | N/A         | N/A             | Single entry describing server capabilities.Use `ldapsearch --baseDn "" --searchScope base "(&)" +` to read all the (operational) attributes of this entry.Base DN: `""` (empty string)Base directory: N/A       |
| schema          | Schema    | No           | Yes         | Yes             | Single entry listing LDAP schema definitions.More information: [LDAP schema](schema.html).Base DN: `cn=schema`Base directory: `db/schema`                                                                        |
| tasks           | Task      | No           | N/A         | Yes             | Scheduled tasks for this server.Use the `manage-tasks` command.Base DN: `cn=tasks`Base directory: `db/tasks`                                                                                                     |
| userData        | JE        | Yes          | Yes         | Yes             | User entries imported from the LDIF you provide.More information: [Install DS for user data](../install-guide/profile-user-data.html).Base directory: `db/userData`                                              |

(1) Optional backends depend on the setup choices.

(2) The changelog backend is mandatory for servers with a replication server role.

(3) You must create a superuser account at setup time. You may choose to replace it later. For details, refer to [Use a non-default superuser account](../security-guide/admin.html#non-default-root-dn-account).

## Create a backend

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Separate backends let you use different configuration settings for different data with different access patterns. While doing this allows you more flexibility, it also comes at the price of more administrative and maintenance tasks to manage. Because of this, don't create more backends than you need.Each new backend implies new administrative tasks. When you create a backend:- Add [backup tasks](../maintenance-guide/backup-restore.html#backup) for the new backend.

- Define [restore procedures](../maintenance-guide/backup-restore.html#restore) for the new backend.

- Include the backend in your [disaster recovery](../use-cases/disaster-recovery.html) plans.

- Consider whether [shared cache for all JE database backends](tuning.html#perf-db-cache) still makes sense for your deployment.Before creating a backend *whose base DN is a child of an existing backend*, also read [Subordinate backends](#split-data) carefully. Subordinate backends include important requirements and limitations. |

When you create a new backend on a replicated directory server, let the server replicate the new data:

1. Configure the new backend.

   The following example creates a database backend for Example.org data. The backend relies on a JE database for data storage and indexing:

   ```console
   $ dsconfig \
    create-backend \
    --hostname localhost \
    --port 4444 \
    --bindDn uid=admin \
    --bindPassword password \
    --backend-name exampleOrgBackend \
    --type je \
    --set enabled:true \
    --set base-dn:dc=example,dc=org \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

   When you create a new backend using the `dsconfig` command, DS directory servers create the following indexes automatically:

   | Index              | Approx.                         | Equality | Ordering | Presence | Substring | Entry Limit |
   | ------------------ | ------------------------------- | -------- | -------- | -------- | --------- | ----------- |
   | `aci`              | -                               | -        | -        | Yes      | -         | 4000        |
   | `dn2id`            | Non-configurable internal index |          |          |          |           |             |
   | `ds-sync-conflict` | -                               | Yes      | -        | -        | -         | 4000        |
   | `ds-sync-hist`     | -                               | -        | Yes      | -        | -         | 4000        |
   | `entryUUID`        | -                               | Yes      | -        | -        | -         | 4000        |
   | `id2children`      | Non-configurable internal index |          |          |          |           |             |
   | `id2subtree`       | Non-configurable internal index |          |          |          |           |             |
   | `objectClass`      | -                               | Yes      | -        | -        | -         | 4000        |

2. Verify that replication is enabled:

   ```console
   $ dsconfig \
    get-synchronization-provider-prop \
    --provider-name "Multimaster Synchronization" \
    --property enabled \
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
   > Property : Value(s)
   > ---------:---------
   > enabled  : true
   > ```

   If replication should be enabled but is not, use `dsconfig set-synchronization-provider-prop --set enabled:true` to enable it.

3. Let the server replicate the base DN of the new backend:

   ```console
   $ dsconfig \
    create-replication-domain \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --provider-name "Multimaster Synchronization" \
    --domain-name dc=example,dc=org \
    --type generic \
    --set enabled:true \
    --set base-dn:dc=example,dc=org \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

4. If you have existing data for the backend, follow the appropriate procedure to initialize replication.

   For details, refer to [Manual initialization](repl-init.html).

If you must temporarily disable replication for the backend, take care to avoid losing changes. For details, refer to [Disable replication](repl-stop.html).

## Import and export

The following procedures demonstrate how to import and export LDIF data.

For details on creating custom sample LDIF to import, refer to [Generate test data](../ldap-guide/ldif-tools.html#generating-ldif).

### Import LDIF

If you are initializing replicas by importing LDIF, refer to [Initialize all replicas from LDIF](repl-init.html#init-repl-ldif) for context.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | * Importing from LDIF overwrites the data in the target backend with entries from the LDIF data.

  For a backend with multiple base DNs, importing the data for one of the base DNs doesn't affect the data for the other base DNs.

* If the LDIF was exported from another server, it may contain pre-encoded passwords. As long as DS supports the password storage schemes used to encode the passwords, you can enable the storage schemes in the configuration to migrate existing passwords into DS. For details, refer to [Password storage](../security-guide/pwp-strong-safe.html#configure-pwd-storage).

  By default, password policies do not allow you to use pre-encoded passwords. You can change this behavior by changing the default password policy configuration property, `allow-pre-encoded-passwords`.

  The DS import process does not warn you about passwords that use disabled password storage schemes. Instead, search the LDIF to find all the password storage schemes in use, and make sure all the schemes are enabled in the server configuration. Users whose passwords are stored with a disabled scheme cannot bind successfully.

* LDIF from another server can include passwords encrypted with a reversible storage scheme, such as AES. To decrypt the passwords, the server must use the same deployment ID as the server that encrypted the passwords. |

Perform either of the following steps to import `dc=example,dc=com` data into the `dsEvaluation` backend:

* To import offline, shut down the server before you run the `import-ldif` command:

  ```console
  $ stop-ds
  $ import-ldif \
   --offline \
   --backendId dsEvaluation \
   --includeBranch dc=example,dc=com \
   --ldifFile example.ldif
  ```

* To import online, schedule a task:

  ```console
  $ start-ds
  $ import-ldif \
   --hostname localhost \
   --port 4444 \
   --bindDn uid=admin \
   --bindPassword password \
   --backendId dsEvaluation \
   --includeBranch dc=example,dc=com \
   --ldifFile example.ldif \
   --trustStorePath /path/to/opendj/config/keystore \
   --trustStoreType PKCS12 \
   --trustStorePassword:file /path/to/opendj/config/keystore.pin
  ```

  You can schedule the import task to start at a particular time using the `--start` option.

  Use the [manage-tasks](../tools-reference/manage-tasks.html) command to manage scheduled tasks. For background, read [Server tasks](../maintenance-guide/server-process.html#server-tasks). For an example command, refer to [Status and tasks](../monitoring-guide/monitoring-status-and-tasks.html).

### Export LDIF

Perform either of the following steps to export `dc=example,dc=com` data from the `dsEvaluation` backend:

* To export offline, shut down the server before you run the `export-ldif` command:

  ```console
  $ stop-ds
  $ export-ldif \
   --offline \
   --backendId dsEvaluation \
   --includeBranch dc=example,dc=com \
   --ldifFile backup.ldif
  ```

* To export online, schedule a task:

  ```console
  $ export-ldif \
   --hostname localhost \
   --port 4444 \
   --bindDn uid=admin \
   --bindPassword password \
   --backendId dsEvaluation \
   --includeBranch dc=example,dc=com \
   --ldifFile backup.ldif \
   --start 0 \
   --trustStorePath /path/to/opendj/config/keystore \
   --trustStoreType PKCS12 \
   --trustStorePassword:file /path/to/opendj/config/keystore.pin
  ```

  The `--start 0` option tells the directory server to start the export task immediately.

  You can specify a time for the task to start using the format yyyymmddHHMMSS. For example, `20250101043000` specifies a start time of 4:30 AM on January 1, 2025.

  If the server is not running at the time specified, it attempts to perform the task after it restarts.

  Use the [manage-tasks](../tools-reference/manage-tasks.html) command to manage scheduled tasks. For background, read [Server tasks](../maintenance-guide/server-process.html#server-tasks). For an example command, refer to [Status and tasks](../monitoring-guide/monitoring-status-and-tasks.html).

## Subordinate backends

A subordinate backend has a base DN making it a child of an existing backend. For example, a DS server has an `exampleCom` backend for `dc=example,dc=com`, a subordinate `peopleExampleCom` backend for `ou=People,dc=example,dc=com`, and an `exampleOrg` backend:

![Depiction of a subordinate backend](../_images/backends.png)

(Technically, all DS backends are subordinate to the root DSE backend whose base DN is the empty string. You don't manage the root DSE, however.)

Subordinate backends include **important requirements and limitations**:

* DS supports paging, sorting, and VLV search results for searches in a single backend. DS doesn't support paging, sorting, and VLV searches traversing backends.

  Client applications know base DNs, however, not backends. Use of subordinate backends can lead to unexpected, logically wrong search results when the scope extends from the parent to the child backend.

* Like other backends, you must add backup tasks and restore procedures, and include subordinate backends in disaster recovery plans.

  Unlike other backends, you must perform all tasks and procedures for subordinate backends *at the same time you perform them for parent backends*. This ensures the replicated data remains aligned.

* Subordinate backends don't reduce network traffic between replication servers, and the replication changelog doesn't use less disk space. Instead, the servers use slightly more system resources in file descriptors and threads for each added backend.

|   |                                                                                                                                                                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you migrate to DS from another directory service, don't use subordinate backends simply because you used them in the other directory service.Try concatenating the data and using a single backend instead:1) Exporting existing backends to LDIF.

2) Concatenate the child LDIF after the parent LDIF in a single LDIF file.

3) Import the concatenated LDIF into a single DS backend. |

If you accept the requirements and limitations and the deployment appears to require a subordinate backend, contact [Ping Identity](https://www.pingidentity.com/) to validate your plans before deploying in production.

To set up a subordinate backend, stop the servers and follow this example for each server:

1. Create an `exampleCom` backend with a `dc=example,dc=com` replication domain.

   This backend holds all Example.com data except `ou=People,dc=example,dc=com`. The backend `base-dn` must match the replication domain `base-dn`:

   1. Create a backend for the data not under the subordinate base DN:

      ```console
      $ dsconfig \
       create-backend \
       --backend-name exampleCom \
       --type je \
       --set enabled:true \
       --set base-dn:dc=example,dc=com \
       --offline \
       --no-prompt
      ```

   2. Let the server replicate the base DN of the new backend:

      ```console
      $ dsconfig \
       create-replication-domain \
       --provider-name "Multimaster Synchronization" \
       --domain-name dc=example,dc=com \
       --type generic \
       --set enabled:true \
       --set base-dn:dc=example,dc=com \
       --offline \
       --no-prompt
      ```

   3. Import data not under the subordinate base DN:

      ```console
      $ import-ldif \
       --backendId exampleCom \
       --excludeBranch ou=People,dc=example,dc=com \
       --ldifFile example.ldif \
       --offline
      ```

2. Create a `peopleExampleCom` backend with an `ou=People,dc=example,dc=com` replication domain.

   This backend holds only Example.com data for `ou=People`. The backend `base-dn` must match the replication domain `base-dn`:

   1. Create a backend for the data under the subordinate base DN:

      ```console
      $ dsconfig \
       create-backend \
       --backend-name peopleExampleCom \
       --type je \
       --set enabled:true \
       --set base-dn:ou=People,dc=example,dc=com \
       --offline \
       --no-prompt
      ```

   2. Let the server replicate the base DN of the new backend:

      ```console
      $ dsconfig \
       create-replication-domain \
       --provider-name "Multimaster Synchronization" \
       --domain-name ou=People,dc=example,dc=com \
       --type generic \
       --set enabled:true \
       --set base-dn:ou=People,dc=example,dc=com \
       --offline \
       --no-prompt
      ```

   3. Import data under the subordinate base DN:

      ```console
      $ import-ldif \
       --backendId peopleExampleCom \
       --includeBranch ou=People,dc=example,dc=com \
       --ldifFile example.ldif \
       --offline
      ```

3. Start the server.

## Disk space thresholds

Directory data growth depends on applications that use the directory. When directory applications add more data than they delete, the database backend grows until it fills the available disk space. The system can end up in an unrecoverable state if no disk space is available.

Database backends therefore have advanced properties, `disk-low-threshold` and `disk-full-threshold`. When available disk space falls below `disk-low-threshold`, the directory server only allows updates from users and applications that have the `bypass-lockdown` privilege. When available space falls below `disk-full-threshold`, the directory server stops allowing updates, instead returning an `UNWILLING_TO_PERFORM` error to each update request.

If growth across the directory service tends to happen quickly, set the thresholds higher than the defaults to allow more time to react when growth threatens to fill the disk. The following example sets `disk-low-threshold` to 10 GB `disk-full-threshold` to 5 GB for the `dsEvaluation` backend:

```console
$ dsconfig \
 set-backend-prop \
 --hostname localhost \
 --port 4444 \
 --bindDn uid=admin \
 --bindPassword password \
 --backend-name dsEvaluation \
 --set "disk-low-threshold:10 GB" \
 --set "disk-full-threshold:5 GB" \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
```

The properties [disk-low-threshold](../configref/objects-je-backend.html#disk-low-threshold), and [disk-full-threshold](../configref/objects-je-backend.html#disk-full-threshold) are listed as *advanced* properties.

To examine their values with the `dsconfig` command, use the `--advanced` option:

```console
$ dsconfig \
 get-backend-prop \
 --advanced \
 --hostname localhost \
 --port 4444 \
 --bindDn uid=admin \
 --bindPassword password \
 --backend-name dsEvaluation \
 --property disk-low-threshold \
 --property disk-full-threshold \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
```

> **Collapse: Show output**
>
> ```
> Property            : Value(s)
> --------------------:---------
> disk-full-threshold : 5 gb
> disk-low-threshold  : 10 gb
> ```

## Entry expiration

If the directory service creates many entries that expire and should be deleted, you could find the entries with a time-based search and then delete them individually. That approach uses replication to delete the entries in all replicas. It has the disadvantage of generating potentially large amounts of replication traffic.

Entry expiration lets you configure the backend database to delete the entries as they expire. This approach deletes expired entries at the backend database level, without generating replication traffic. AM uses this approach when relying on DS to delete expired token entries, as demonstrated in [Install DS for AM CTS](../install-guide/profile-am-cts.html).

Backend indexes for generalized time (timestamp) attributes have these properties to configure automated, optimized entry expiration and removal:

* [ttl-enabled](../configref/objects-backend-index.html#ttl-enabled)

* [ttl-age](../configref/objects-backend-index.html#ttl-age)

Configure this capability by performing the following steps:

1. Prepare an ordering index for a generalized time (timestamp) attribute on entries that expire.

   For details, refer to [Configure indexes](idx-config.html) and [Active accounts](../ldap-guide/search-ldap.html#extensible-match-search).

2. Using the `dsconfig set-backend-index-prop` command, set `ttl-enabled` on the index to true, and optionally set `ttl-age` on the index to the desired entry lifetime duration.

3. (Optional) Enable the access log to record messages when the server deletes an expired entry.

   Using the `dsconfig set-log-publisher-prop` command, set `suppress-internal-operations:false` for the access log publisher. Note that this causes the server to log messages for all internal operations.

   When the server deletes an expired entry, it logs a message with `"additionalItems":{"ttl": true}` in the response.

Once you configure and build the index, the backend can delete expired entries. At intervals of 10 seconds, the backend automatically deletes entries whose timestamps on the attribute are older than the specified lifetime. Entries that expire in the interval between deletions are removed on the next round. Client applications should therefore check that entries have not expired, as it is possible for expired entries to remain available until the next round of deletions.

When using this capability, keep the following points in mind:

* Entry expiration is per index. The time to live depends on the value of the indexed attribute plus the `ttl-age` setting, and all matching entries are subject to TTL.

  To expire entries quickly after reaching the time of the indexed attribute, use a low `ttl-age` setting. For example, for entries having an expiration date, like sessions or access tokens, use the default or other low value for `ttl-age`.

  To expire entries having a last login time or last use attribute, use a high `ttl-age` setting to leave a long grace period before deletion. For example, to delete entries a year after they become inactive, configure the index for last login time and use `ttl-age: 52w`.

* If multiple indexes' `ttl-enabled` and `ttl-age` properties are configured, as soon as one of the entry's matching attributes exceeds the TTL, the entry is eligible for deletion.

* The backend deletes the entries directly as an internal operation. The server only records the deletion when `suppress-internal-operations: false` for the access log publisher. Persistent searches do not return the deletion.

  Furthermore, this means that *deletion is not replicated*. To ensure expired entries are deleted on all replicas, use the same indexes with the same settings on all replicas.

* When a backend deletes an expired entry, the effect is a subtree delete. In other words, if a parent entry expires, the parent entry *and all the parent's child entries* are deleted.

  If you do not want parent entries to expire, index a generalized time attribute that is only present on its child entries.

* The backend deletes expired entries atomically.

  If you update the TTL attribute to prevent deletion and the update succeeds, then TTL has effectively been reset.

* Expiration fails when the `index-entry-limit` is exceeded. (For background information, refer to [Index entry limits](idx-config.html#index-entry-limits).)

  This only happens if the timestamp for the indexed attribute matches to the nearest millisecond on more than 4000 entries (for default settings). This corresponds to four million timestamp updates per second, which would be very difficult to reproduce in a real directory service.

  It is possible, however, to construct and import an LDIF file where more than 4000 entries have the same timestamp. Make sure not to reuse the same timestamp for thousands of entries when artificially creating entries that you intend to expire.

## Add a base DN to a backend

The following example adds the base DN `o=example` to the `dsEvaluation` backend, and creates a replication domain configuration to replicate the data under the new base DN:

```console
$ dsconfig \
 set-backend-prop \
 --hostname localhost \
 --port 4444 \
 --bindDn uid=admin \
 --bindPassword password \
 --backend-name dsEvaluation \
 --add base-dn:o=example \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
$ dsconfig \
 get-backend-prop \
 --hostname localhost \
 --port 4444 \
 --bindDn uid=admin \
 --bindPassword password \
 --backend-name dsEvaluation \
 --property base-dn \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
```

> **Collapse: Show output**
>
> ```
> Property : Value(s)
> ---------:-------------------------------
> base-dn  : "dc=example,dc=com", o=example
> ```

```console
$ dsconfig \
 create-replication-domain \
 --provider-name "Multimaster Synchronization" \
 --domain-name o=example \
 --type generic \
 --set enabled:true \
 --set base-dn:o=example \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
```

When you add a base DN to a backend, the base DN must not be subordinate to any other base DNs in the backend. As in the commands shown here, you can add the base DN `o=example` to a backend that already has a base DN `dc=example,dc=com`. You cannot, however, add `o=example,dc=example,dc=com` as a base DN, because that is a child of `dc=example,dc=com`.

## Delete a backend

When you delete a database backend with the `dsconfig delete-backend` command, the directory server does not actually remove the database files for these reasons:

* A mistake could potentially cause lots of data to be lost.

* Deleting a large database backend could cause severe service degradation due to a sudden increase in I/O load.

After you run the `dsconfig delete-backend` command, manually remove the database backend files, and remove replication domain configurations any base DNs you deleted by removing the backend.

If run the `dsconfig delete-backend` command by mistake, but have not yet deleted the actual files, recover the data by creating the backend again, and reconfiguring and rebuilding the indexes.

---

---
title: Debug a missing index
description: Work through an end-to-end example of diagnosing and fixing an unindexed LDAP search failure caused by a missing PingDS attribute index.
component: pingds
version: 8.1
page_id: pingds:config-guide:idx-debug
canonical_url: https://docs.pingidentity.com/pingds/8.1/config-guide/idx-debug.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["LDAP", "Troubleshooting"]
section_ids:
  how_it_looks_to_the_application: How it looks to the application
  how_it_looks_to_the_administrator: How it looks to the administrator
  how_the_fix_looks_to_the_administrator: How the fix looks to the administrator
  how_the_fix_looks_to_the_application: How the fix looks to the application
  more_to_do: More to do?
---

# Debug a missing index

This example explains how you, as directory administrator, investigate an indexing problem.

## How it looks to the application

In this example, an LDAP client application helps people look up names using mobile telephone numbers. The mobile numbers are stored on the `mobile` attribute in the directory.

The LDAP client application has a search for a mobile number failing with error 50:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=user.1,ou=people,dc=example,dc=com \
 --bindPassword password \
 --baseDN dc=example,dc=com \
 "(mobile=14120300042)" cn
```

> **Collapse: Show output**
>
> ```
> # The LDAP search request failed: 50 (Insufficient Access Rights)
> # Additional Information:  You do not have sufficient privileges to perform an unindexed search
> ```

The application owner tells you there's a problem searching on mobile numbers.

## How it looks to the administrator

As administrator, you can observe the failures in the DS access logs. The following example includes only the relevant fields of an access log message with the failure:

```json
{
  "request": {
    "operation": "SEARCH",
    "dn": "dc=example,dc=com",
    "scope": "sub",
    "filter": "(mobile=14120300042)"
  },
  "response": {
    "status": "FAILED",
    "statusCode": "50",
    "detail": "You do not have sufficient privileges to perform an unindexed search",
    "additionalItems": {
      "unindexed": true
    },
    "nentries": 0
  },
  "userId": "uid=user.1,ou=People,dc=example,dc=com"
}
```

For this simple filter, `(mobile=14120300042)`, if the search is unindexed, you can conclude that the attribute must not be indexed. As expected, the `mobile` attribute does not appear in the list of indexes for the backend:

```console
$ dsconfig \
 list-backend-indexes \
 --backend-name dsEvaluation \
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
> Backend Index              : index-type             ...
> ---------------------------:------------------------...
> aci                        : presence               ...
> cn                         : equality, substring    ...
> ds-certificate-fingerprint : equality               ...
> ds-certificate-subject-dn  : equality               ...
> ds-sync-conflict           : equality               ...
> ds-sync-hist               : ordering               ...
> entryUUID                  : equality               ...
> givenName                  : equality, substring    ...
> json                       : equality               ...
> jsonToken                  : equality               ...
> mail                       : equality, substring    ...
> manager                    : equality, extensible   ...
> member                     : equality               ...
> oauth2Token                : equality               ...
> objectClass                : big-equality, equality ...
> sn                         : equality, substring    ...
> telephoneNumber            : equality, substring    ...
> uid                        : equality               ...
> uniqueMember               : equality               ...
> ```

You can determine why a filter is unindexed by:

* Referring to the `response` > `additionalItems` > `debugSearchIndex` object on the access log message for the unindexed search.

* Running the search with the `debugsearchindex` attribute.

If the data and indexes changed significantly since the search ran, the `debugSearchIndex` object and `debugsearchindex` output can be different.

You notice that `telephoneNumber` has equality and substring indexes, and decide to add the same for the `mobile` attribute. Adding a new index means adding the configuration for the index, and then building the index. An index is specific to a given server, so you do this for each DS replica. For example:

```console
$ dsconfig \
 create-backend-index \
 --backend-name dsEvaluation \
 --index-name mobile \
 --type generic \
 --set index-type:equality \
 --set index-type:substring \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
$ rebuild-index \
 --index mobile \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --baseDN dc=example,dc=com \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin
```

## How the fix looks to the administrator

Once the index is built, you check that the search is now indexed by looking at the `debugsearchindex` output:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=admin \
 --bindPassword password \
 --baseDN dc=example,dc=com \
 "(mobile=14120300042)" \
 debugsearchindex | sed -n -e "s/^debugsearchindex: //p"
```

> **Collapse: Show output**
>
> ```
> {
>     "baseDn": "dc=example,dc=com",
>     "scope": "sub",
>     "filter": "(mobile=14120300042)",
>     "maxCandidateSize": 100000,
>     "lookThroughLimit": 0,
>     "strategies": [
>         {
>             "name": "BaseObjectSearchStrategy",
>             "diagnostic": "not applicable",
>             "lookedThrough": 0
>         },
>         {
>             "name": "VlvSearchStrategy",
>             "diagnostic": "not applicable",
>             "lookedThrough": 0
>         },
>         {
>             "name": "AttributeIndexSearchStrategy",
>             "filter": {
>                 "query": "FIRST_OF",
>                 "rank": "EXACT_MATCH",
>                 "filter": "(mobile=14120300042)",
>                 "subQueries": [
>                     {
>                         "query": "EXACT_MATCH",
>                         "rank": "EXACT_MATCH",
>                         "filter": "(mobile=14120300042)",
>                         "index": "mobile.telephoneNumberMatch",
>                         "key": "14120300042",
>                         "diagnostic": "indexed",
>                         "candidates": 1
>                     },
>                     {
>                         "query": "MATCH_ALL",
>                         "rank": "MATCH_ALL",
>                         "filter": "(mobile=14120300042)",
>                         "index": "mobile.presence",
>                         "diagnostic": "skipped"
>                     }
>                 ],
>                 "diagnostic": "indexed",
>                 "candidates": 1
>             },
>             "diagnostic": "indexed",
>             "candidates": 1,
>             "lookedThrough": 1
>         },
>         {
>             "name": "BigIndexSearchStrategy",
>             "diagnostic": "skipped"
>         },
>         {
>             "name": "UnindexedSearchStrategy",
>             "diagnostic": "skipped"
>         }
>     ],
>     "lookedThrough": 1,
>     "final": 1
> }
> ```

You tell the application owner to try searching on mobile numbers now that you have indexed the attribute.

## How the fix looks to the application

The client application now has a working search:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=user.1,ou=people,dc=example,dc=com \
 --bindPassword password \
 --baseDN dc=example,dc=com \
 "(mobile=14120300042)" cn
```

> **Collapse: Show output**
>
> ```
> dn: uid=user.0,ou=People,dc=example,dc=com
> cn: Aaccf Amar
> ```

## More to do?

Must you do anything more? What about `index-entry-limit` settings, for example?

Run the `backendstat show-index-status` command. Optionally, stop the server before running the command:

```console
$ stop-ds --quiet
$ backendstat show-index-status --baseDN dc=example,dc=com
```

> **Collapse: Show output**
>
> ```
> Index Name                                ...  Over  Entry Limit  Mean  ...
> ------------------------------------------...---------------------------...--
> ...
> mobile.telephoneNumberMatch               ...     0         4000     1  ...
> mobile.telephoneNumberSubstringsMatch:6   ...    10         4000     2  ...
> ...
>
> Index: mobile.telephoneNumberSubstringsMatch:6
> Over index-entry-limit keys: [0] [1] [2] [3] [4] [5] [6] [7] [8] [9]
> ...
> ```

Notice that the equality index `mobile.telephoneNumberMatch` has no keys whose entry ID lists are over the limit, and the average number of values is 1. This is what you would expect. Each mobile number belongs to a single user. DS uses this index for exact match search filters like `(mobile=14120300042)`.

Notice also that the substring index `mobile.telephoneNumberSubstringsMatch:6` has 10 keys whose lists are over the (default) limit of 4000 values. These are the keys for substrings that match only a single digit of a mobile number. For example, a search for all users whose mobile telephone number starts with `1` uses the filter `(mobile=1*)`. This search would be unindexed.

Should you raise the `index-entry-limit` for this substring index? Probably not, no.

The filter `(mobile=1*)` matches all mobile numbers for the United States and Canada, for example. Someone running this search is not looking up a user's name by their mobile phone number. They are scanning the directory database, even if it is not intentional. If you raise the `index-entry-limit` setting to prevent any `Over index-entry-limit keys`, the server must update enormous entry ID lists for these keys whenever a `mobile` attribute value changes. The impact on write performance could be a bad tradeoff.

If possible, suggest that the LDAP application refrains from searching until the user has provided enough digits of the mobile number to match, or that it prompts the user for more digits when it encounters an unindexed search.

If you cannot change the application, it might be acceptable that searches for a single mobile telephone digit simply fail. That might be a better tradeoff than impacting write performance due to a very high `index-entry-limit` setting.

---

---
title: Disable replication
description: Temporarily disable PingDS replication on a replica or permanently remove a server from the replication topology.
component: pingds
version: 8.1
page_id: pingds:config-guide:repl-stop
canonical_url: https://docs.pingidentity.com/pingds/8.1/config-guide/repl-stop.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["LDAP", "Replication", "Troubleshooting"]
section_ids:
  stop-repl-temporarily: Disable replication temporarily
  stop-repl-permanently: Stop replicating permanently
---

# Disable replication

## Disable replication temporarily

|   |                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Do not allow modifications on the replica for which replication is temporarily stopped. No record of such changes is kept, and the changes cause replication to diverge. |

Follow these steps to disable replication temporarily for a replica and drop any changes that occur:

1. Prevent changes to the affected data.

   For details, refer to [Read-only replicas](repl-read-only.html).

2. Disable the replication mechanism:

   ```console
   $ dsconfig \
    set-synchronization-provider-prop \
    --provider-name "Multimaster Synchronization" \
    --set enabled:false \
    --hostname replica.example.com \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

3. Perform whatever operations are required.

4. Enable the replication mechanism again:

   ```console
   $ dsconfig \
    set-synchronization-provider-prop \
    --provider-name "Multimaster Synchronization" \
    --set enabled:true \
    --hostname replica.example.com \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

5. Allow changes to the affected data.

   For details, refer to [Read-only replicas](repl-read-only.html).

Before removing a server from a group of replicated servers, disable replication as described. When the server you remove is a bootstrap replication server, also remove it from the configuration on all other servers.

## Stop replicating permanently

You might remove a server from a replication topology because:

* The DS server is no longer needed.

  For example, you are scaling a deployment down, or retiring an old server that you replaced with a newer one.

* Someone configured replication between DS servers that should be independent.

  For example, at setup time, replication was configured to include all six replicas in three data centers, but the expected configuration was three separate directory service deployments with two replicas in each data center.

  In this case, you must permanently change which servers replicate with each other.

|   |                                                                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The steps that follow only apply to deployments of DS 7 and later servers.If you are upgrading from older servers and have a mix of DS 7 and earlier servers, refer to the [Upgrade](../upgrade-guide/preface.html) documentation instead. |

*To remove a server that is no longer needed:*

1. Uninstall the server.

   For details, refer to [Uninstallation](../install-guide/uninstall.html).

2. If the server is referenced in other servers' `bootstrap-replication-server` settings, remove it.

   For details, refer to [Remove a bootstrap replication server](repl-bootstrap.html#remove-bootstrap-replication-server).

3. The automated purge process eventually removes historical data and changelog data for old servers.

   You can optionally trigger a purge task manually, as described in [Manual purge](repl-purge.html).

*To change which servers replicate with each other:*

1. Prevent changes to the affected data.

   For details, refer to [Read-only replicas](repl-read-only.html).

2. Perform these steps in parallel on all affected servers:

   1. Disable the replication mechanism.

      For details, refer to [Disable replication temporarily](#stop-repl-temporarily).

   2. Adjust the `bootstrap-replication-server` settings to limit replication as desired.

   3. Enable the replication mechanism again.

   4. Restart the server for the changes to take effect.

3. Allow changes to the affected data.

4. Delete entries that were erroneously replicated.

   For details, refer to [Delete entries](../ldap-guide/write-ldap.html#delete-ldap).

5. The automated purge process eventually removes historical data and changelog data for old servers.

   You can optionally trigger a purge task manually, as described in [Manual purge](repl-purge.html).

---

---
title: Disk space thresholds
description: Configure disk space thresholds on PingDS replication servers to trigger alerts and disconnect from the topology when changelog storage runs low.
component: pingds
version: 8.1
page_id: pingds:config-guide:repl-disk-space
canonical_url: https://docs.pingidentity.com/pingds/8.1/config-guide/repl-disk-space.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Features", "LDAP", "Replication", "Setup &amp; Configuration", "Troubleshooting"]
---

# Disk space thresholds

Replication servers record changes in changelog database files under the `opendj/changelogDb` directory.

|   |                                                                                                                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Do not compress, tamper with, or otherwise alter changelog database files directly, unless specifically instructed to do so by a qualified technical support engineer.External changes to changelog database files can render them unusable by the server. |

Replication server configuration objects have changelog database properties, `disk-low-threshold`, and `disk-full-threshold`:

* When available disk space falls below `disk-low-threshold`, the replication server triggers a warning alert notification to let you know to free disk space.

* When available disk space falls below `disk-full-threshold`, the replication server triggers another warning alert notification, and *disconnects from the replication topology*.

  Connected directory servers fail over to another replication server until available disk space is above the `disk-full-threshold` again.

Set the thresholds high enough to allow time to react after the initial alert.

The following example sets `disk-low-threshold` to 10 GB and `disk-full-threshold` to 5 GB:

```console
$ dsconfig \
 set-replication-server-prop \
 --provider-name "Multimaster Synchronization" \
 --set "disk-low-threshold:10 GB" \
 --set "disk-full-threshold:5 GB" \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
```

The [disk-low-threshold](../configref/objects-replication-server.html#disk-low-threshold) and [disk-full-threshold](../configref/objects-replication-server.html#disk-full-threshold) properties are *advanced* properties. Examine their values with the `dsconfig --advanced` option.

---

---
title: Fractional replication (advanced)
description: Configure fractional replication in PingDS to include or exclude specific LDAP attributes on a per-replica basis.
component: pingds
version: 8.1
page_id: pingds:config-guide:repl-fractional
canonical_url: https://docs.pingidentity.com/pingds/8.1/config-guide/repl-fractional.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Features", "LDAP", "Replication", "Setup &amp; Configuration"]
---

# Fractional replication (advanced)

|   |                                                     |
| - | --------------------------------------------------- |
|   | This information applies to *advanced* deployments. |

With fractional replication, you specify the attributes to include and to exclude using `fractional-include` and `fractional-exclude` configuration properties. Fractional replicas must respect LDAP schemas. Attributes that are required by the relevant object classes are included whether you specify them or not. Excluded attributes must be optional attributes of the relevant object classes.

Each attribute must remain on at least one replica. When you configure a replica to exclude an attribute, the replica checks that the attribute is never added to the replica as part of any LDAP operation. If you exclude the attribute everywhere, it can never be added anywhere.

When using fractional replication, initialize replication from LDAP Data Interchange Format (LDIF) *(tooltip: \<div class="paragraph">
\<p>An IETF standard file format for representing LDAP directory content and modifications to directory content. Typically used to import and export LDAP-based directory information.\</p>
\</div>)*. The import process imports only the data allowed by fractional replication. Be aware that you cannot create a replica with a full data set from a replica with only a subset of the data.

Replication servers filter objects for fractional replication. If you must prevent data from being replicated across a national boundary, for example, keep standalone replication servers in locations where you can store full entries and their changes. Outside that location, set up standalone replicas that receive the fractional entries.

The following example configures a fractional replica with a subset of `inetOrgPerson` attributes:

```console
$ dsconfig \
 set-replication-domain-prop \
 --provider-name "Multimaster Synchronization" \
 --domain-name "dc=example,dc=com" \
 --set fractional-include:inetorgperson:cn,givenname,mail,mobile,sn,telephonenumber \
 --hostname replica.example.com \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
```

The following example excludes a custom attribute, `sessionToken`, on the replica:

```console
$ dsconfig \
 set-replication-domain-prop \
 --provider-name "Multimaster Synchronization" \
 --domain-name "dc=example,dc=com" \
 --set fractional-exclude:*:sessionToken \
 --hostname replica.example.com \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
```

This example only applies if you have defined a `sessionToken` attribute in the LDAP schema.

---

---
title: Groups
description: Configure dynamic, static, and virtual static groups in PingDS, including nested groups and referential integrity.
component: pingds
version: 8.1
page_id: pingds:config-guide:groups
canonical_url: https://docs.pingidentity.com/pingds/8.1/config-guide/groups.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Features", "Groups", "LDAP", "Setup &amp; Configuration"]
section_ids:
  dynamic-groups: Dynamic groups
  virtual-static-groups: Virtual static groups
  static-groups: Static groups
  nested-groups: Nested groups
  group-membership: Group membership
  referential-integrity: Referential integrity
---

# Groups

DS servers support several methods of grouping entries:

* [Dynamic groups](#dynamic-groups) look up their membership based on an LDAP filter.

* [Static groups](#static-groups) list each member.

  Static groups are easy to start, but can become large and expensive to maintain.

  For static groups, you must have a mechanism to remove members whose entries are deleted, and members whose entries are modified in a way that ends their membership. DS servers use a *referential integrity* plugin for this.

* [Virtual static groups](#virtual-static-groups) use a dynamic group-style definition, but let applications list group members as if the group were static.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The examples that follow assume `ou=Groups,dc=example,dc=com` already exists. The `ds-evaluation` profile includes this entry by default. If you are using another profile, you can create the groups entry:```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=admin \
 --bindPassword password << EOF
dn: ou=Groups,dc=example,dc=com
objectClass: organizationalunit
objectClass: top
ou: Groups
EOF
``` |

## Dynamic groups

A dynamic group *(tooltip: \<div class="paragraph">
\<p>A group specifying members with LDAP URLs.\</p>
\</div>)* references members using LDAP URLs *(tooltip: \<div class="paragraph">
\<p>A standard uniform resource locator for accessing entries in a directory.\</p>
\</div>)*. Dynamic group entries take the `groupOfURLs` object class, with one or more `memberURL` values specifying LDAP URLs to identify group members.

Dynamic groups are a natural fit for directory servers. If you have a choice, choose dynamic groups over static groups for these reasons:

* Dynamic group membership is a property of a member's entry.

  There is no need to maintain a separate entry with the list of members.

* Determining dynamic group membership is as simple as applying the member URL criteria.

* Dynamic groups scale to any size without performance issues.

  Dynamic group entries remain small even when the group has a large number of members.

The following dynamic group includes entries matching the filter `"(l=San Francisco)"` (users whose location is San Francisco):

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery << EOF
dn: cn=My Dynamic Group,ou=Groups,dc=example,dc=com
cn: My Dynamic Group
objectClass: top
objectClass: groupOfURLs
ou: Groups
memberURL: ldap:///ou=People,dc=example,dc=com??sub?l=San Francisco
EOF
```

Group membership changes dynamically as entries change to match the `memberURL` values:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 --baseDN dc=example,dc=com \
 "(&(uid=*jensen)(isMemberOf=cn=My Dynamic Group,ou=Groups,dc=example,dc=com))" \
 1.1
```

> **Collapse: Show output**
>
> ```
> dn: uid=bjensen,ou=People,dc=example,dc=com
>
> dn: uid=rjensen,ou=People,dc=example,dc=com
> ```

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery << EOF
dn: uid=ajensen,ou=People,dc=example,dc=com
changetype: modify
replace: l
l: San Francisco
EOF
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 --baseDN dc=example,dc=com \
 "(&(uid=*jensen)(isMemberOf=cn=My Dynamic Group,ou=Groups,dc=example,dc=com))" \
 1.1
```

> **Collapse: Show output**
>
> ```
> dn: uid=ajensen,ou=People,dc=example,dc=com
>
> dn: uid=bjensen,ou=People,dc=example,dc=com
>
> dn: uid=rjensen,ou=People,dc=example,dc=com
> ```

## Virtual static groups

DS servers let you create virtual static groups *(tooltip: \<div class="paragraph">
\<p>An entry representing dynamic groups as static groups.\</p>
\</div>)*. Virtual static groups allow applications to display dynamic groups as if they had an enumerated list of members like a static group.

The virtual static group takes the auxiliary object class `ds-virtual-static-group`. Virtual static groups use the object class `groupOfNames`, or `groupOfUniqueNames`. Instead of `member` or `uniqueMember` attributes, they have `ds-target-group-dn` attributes pointing to other groups.

Generating the list of members can be resource-intensive for large groups. By default, you cannot retrieve the list of members. If you have an application that must read the list of members, change the configuration of `Virtual Static member` or `Virtual Static uniqueMember` to set `allow-retrieving-membership:true`:

```console
$ dsconfig \
 set-virtual-attribute-prop \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --name "Virtual Static member" \
 --set allow-retrieving-membership:true \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
```

The following example creates a virtual static group, and reads the group entry with all members:

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery << EOF
dn: cn=Virtual Static,ou=Groups,dc=example,dc=com
cn: Virtual Static
objectclass: top
objectclass: groupOfNames
objectclass: ds-virtual-static-group
ds-target-group-dn: cn=My Dynamic Group,ou=Groups,dc=example,dc=com
EOF
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 --baseDN dc=example,dc=com \
 "(cn=Virtual Static)"
```

> **Collapse: Show output**
>
> ```
> dn: cn=Virtual Static,ou=Groups,dc=example,dc=com
> objectClass: top
> objectClass: groupOfNames
> objectClass: ds-virtual-static-group
> cn: Virtual Static
> ds-target-group-dn: cn=My Dynamic Group,ou=Groups,dc=example,dc=com
> member: uid=abergin,ou=People,dc=example,dc=com
> member: uid=ajensen,ou=People,dc=example,dc=com
> member: uid=aknutson,ou=People,dc=example,dc=com
> member: uid=awalker,ou=People,dc=example,dc=com
> member: uid=aworrell,ou=People,dc=example,dc=com
> member: uid=bjensen,ou=People,dc=example,dc=com
> member: uid=bplante,ou=People,dc=example,dc=com
> member: uid=btalbot,ou=People,dc=example,dc=com
> member: uid=cwallace,ou=People,dc=example,dc=com
> member: uid=dakers,ou=People,dc=example,dc=com
> member: uid=dthorud,ou=People,dc=example,dc=com
> member: uid=ewalker,ou=People,dc=example,dc=com
> member: uid=gfarmer,ou=People,dc=example,dc=com
> member: uid=jbourke,ou=People,dc=example,dc=com
> member: uid=jcampaig,ou=People,dc=example,dc=com
> member: uid=jmuffly,ou=People,dc=example,dc=com
> member: uid=jreuter,ou=People,dc=example,dc=com
> member: uid=jwalker,ou=People,dc=example,dc=com
> member: uid=kcarter,ou=People,dc=example,dc=com
> member: uid=kschmith,ou=People,dc=example,dc=com
> member: uid=mjablons,ou=People,dc=example,dc=com
> member: uid=mlangdon,ou=People,dc=example,dc=com
> member: uid=mschneid,ou=People,dc=example,dc=com
> member: uid=mtalbot,ou=People,dc=example,dc=com
> member: uid=mtyler,ou=People,dc=example,dc=com
> member: uid=mwhite,ou=People,dc=example,dc=com
> member: uid=pshelton,ou=People,dc=example,dc=com
> member: uid=rjensen,ou=People,dc=example,dc=com
> member: uid=smason,ou=People,dc=example,dc=com
> member: uid=tlabonte,ou=People,dc=example,dc=com
> member: uid=tschmith,ou=People,dc=example,dc=com
> ```

## Static groups

A LDAP static group (static group) *(tooltip: \<div class="paragraph">
\<p>An entry enumerating member entries.\</p>
\</div>)* entry enumerates the entries in the group. Static group entries grow as their membership increases.

Large static groups are a performance bottleneck. If you have a choice, choose dynamic groups over static groups for these reasons:

* Static group membership is defined in a separate, potentially large LDAP entry.

  Large static group entries are expensive to maintain, cache, and replicate.

* Determining static group membership involves reading the group entry, or using virtual membership attributes.

* Static group performance tends to decrease with size.

  Reading and updating the group entry becomes more expensive as group size grows.

|   |                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------- |
|   | When working with static groups, also read [Group membership](#group-membership) and [Referential integrity](#referential-integrity). |

Static group entries are based on one of the following standard object classes:

* `groupOfNames`

  The `groupOfNames` object class requires at least one `member` attribute.

  Each value is the distinguished name of an entry.

* `groupOfEntries`

  The `groupOfEntries` object class requires zero or more `member` attributes.

* `groupOfUniqueNames`

  The `groupOfUniqueNames` object class has at least one `uniqueMember` attribute.

  Each value follows Name and Optional UID syntax. Name and Optional UID syntax values are a DN, optionally followed by `\#BitString`. The BitString, such as `'0101111101'B`, serves to distinguish the entry from another entry with the same DN, which can occur when the original entry was deleted and a new entry was created with the same DN.

Like other LDAP attributes, each group member attribute value is unique. LDAP does not allow duplicate values for the same attribute on the same entry.

|   |                                                                                     |
| - | ----------------------------------------------------------------------------------- |
|   | When creating a group entry, use `groupOfNames` or `groupOfEntries` where possible. |

To create a static group, add a group entry such as the following to the directory:

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery << EOF
dn: cn=My Static Group,ou=Groups,dc=example,dc=com
cn: My Static Group
objectClass: groupOfNames
objectClass: top
ou: Groups
member: uid=ahunter,ou=People,dc=example,dc=com
member: uid=bjensen,ou=People,dc=example,dc=com
member: uid=tmorris,ou=People,dc=example,dc=com
EOF
```

To change group membership, modify the values of the membership attribute:

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery << EOF
dn: cn=My Static Group,ou=Groups,dc=example,dc=com
changetype: modify
add: member
member: uid=scarter,ou=People,dc=example,dc=com
EOF
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 --baseDN dc=example,dc=com \
 "(cn=My Static Group)"
```

> **Collapse: Show output**
>
> ```
> dn: cn=My Static Group,ou=Groups,dc=example,dc=com
> objectClass: groupOfNames
> objectClass: top
> cn: My Static Group
> member: uid=ahunter,ou=People,dc=example,dc=com
> member: uid=bjensen,ou=People,dc=example,dc=com
> member: uid=tmorris,ou=People,dc=example,dc=com
> member: uid=scarter,ou=People,dc=example,dc=com
> ou: Groups
> ```

RFC 4519 says a `groupOfNames` entry must have at least one member. Although DS servers allow you to create a `groupOfNames` without members, strictly speaking, that behavior is not standard. Alternatively, you can use the `groupOfEntries` object class as shown in the following example:

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery << EOF
dn: cn=Initially Empty Static Group,ou=Groups,dc=example,dc=com
cn: Initially Empty Static Group
objectClass: groupOfEntries
objectClass: top
ou: Groups
EOF
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery << EOF
dn: cn=Initially Empty Static Group,ou=Groups,dc=example,dc=com
changetype: modify
add: member
member: uid=ahunter,ou=People,dc=example,dc=com
member: uid=bjensen,ou=People,dc=example,dc=com
member: uid=tmorris,ou=People,dc=example,dc=com
member: uid=scarter,ou=People,dc=example,dc=com
EOF
```

## Nested groups

DS servers let you nest groups. The following example shows a group of groups of managers and administrators:

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery << EOF
dn: cn=The Big Shots,ou=Groups,dc=example,dc=com
cn: The Big Shots
objectClass: groupOfNames
objectClass: top
ou: Groups
member: cn=Accounting Managers,ou=groups,dc=example,dc=com
member: cn=Directory Administrators,ou=Groups,dc=example,dc=com
member: cn=HR Managers,ou=groups,dc=example,dc=com
member: cn=PD Managers,ou=groups,dc=example,dc=com
member: cn=QA Managers,ou=groups,dc=example,dc=com
EOF
```

Although not shown in the example above, DS servers let you nest groups within nested groups.

DS servers let you create dynamic groups of groups. The following example shows a group of other groups. The members of this group are themselves groups, not users:

```console
$ ldapmodify \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery << EOF
dn: cn=Group of Groups,ou=Groups,dc=example,dc=com
cn: Group of Groups
objectClass: top
objectClass: groupOfURLs
ou: Groups
memberURL: ldap:///ou=Groups,dc=example,dc=com??sub?ou=Groups
EOF
```

Use the `isMemberOf` attribute to determine what groups a member belongs to, as described in [Group membership](#group-membership). The following example requests the groups that Kirsten Vaughan belongs to:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 --baseDN dc=example,dc=com \
 "(uid=kvaughan)" \
 isMemberOf
```

> **Collapse: Show output**
>
> ```
> dn: uid=kvaughan,ou=People,dc=example,dc=com
> isMemberOf: cn=Directory Administrators,ou=Groups,dc=example,dc=com
> isMemberOf: cn=HR Managers,ou=groups,dc=example,dc=com
> isMemberOf: cn=The Big Shots,ou=Groups,dc=example,dc=com
> ```

Notice that Kirsten is a member of The Big Shots group.

Notice also that Kirsten does not belong to the Group of Groups. The members of that group are groups, not users. The following example requests the groups that the directory administrators group belongs to:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 --baseDN dc=example,dc=com \
 "(cn=Directory Administrators)" \
 isMemberOf
```

> **Collapse: Show output**
>
> ```
> dn: cn=Directory Administrators,ou=Groups,dc=example,dc=com
> isMemberOf: cn=Group of Groups,ou=Groups,dc=example,dc=com
> isMemberOf: cn=The Big Shots,ou=Groups,dc=example,dc=com
> ```

The following example shows which groups each group belong to. The search is unindexed, and so is performed here with directory administrator credentials:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=admin \
 --bindPassword password \
 --baseDN dc=example,dc=com \
 "(ou=Groups)" \
 isMemberOf
```

> **Collapse: Show output**
>
> ```
> dn: ou=Groups,dc=example,dc=com
>
> dn: cn=Accounting Managers,ou=groups,dc=example,dc=com
> isMemberOf: cn=The Big Shots,ou=Groups,dc=example,dc=com
> isMemberOf: cn=Group of Groups,ou=Groups,dc=example,dc=com
>
> dn: cn=Directory Administrators,ou=Groups,dc=example,dc=com
> isMemberOf: cn=The Big Shots,ou=Groups,dc=example,dc=com
> isMemberOf: cn=Group of Groups,ou=Groups,dc=example,dc=com
>
> dn: cn=Group of Groups,ou=Groups,dc=example,dc=com
>
> dn: cn=HR Managers,ou=groups,dc=example,dc=com
> isMemberOf: cn=The Big Shots,ou=Groups,dc=example,dc=com
> isMemberOf: cn=Group of Groups,ou=Groups,dc=example,dc=com
>
> dn: cn=Initially Empty Static Group,ou=Groups,dc=example,dc=com
> isMemberOf: cn=Group of Groups,ou=Groups,dc=example,dc=com
>
> dn: cn=My Dynamic Group,ou=Groups,dc=example,dc=com
>
> dn: cn=My Static Group,ou=Groups,dc=example,dc=com
> isMemberOf: cn=Group of Groups,ou=Groups,dc=example,dc=com
>
> dn: cn=PD Managers,ou=groups,dc=example,dc=com
> isMemberOf: cn=The Big Shots,ou=Groups,dc=example,dc=com
> isMemberOf: cn=Group of Groups,ou=Groups,dc=example,dc=com
>
> dn: cn=QA Managers,ou=groups,dc=example,dc=com
> isMemberOf: cn=The Big Shots,ou=Groups,dc=example,dc=com
> isMemberOf: cn=Group of Groups,ou=Groups,dc=example,dc=com
>
> dn: cn=The Big Shots,ou=Groups,dc=example,dc=com
> isMemberOf: cn=Group of Groups,ou=Groups,dc=example,dc=com
> ```

Notice that the group of groups is not a member of itself.

## Group membership

DS servers let you verify which groups a user belongs to by reading their entry. The virtual `isMemberOf` attribute shows which groups a user is in.

Reading the user entry is more efficient than reading large static group entries and checking the lists of members:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 --baseDN dc=example,dc=com \
 "(uid=bjensen)" \
 isMemberOf
```

> **Collapse: Show output**
>
> ```
> dn: uid=bjensen,ou=People,dc=example,dc=com
> isMemberOf: cn=Initially Empty Static Group,ou=Groups,dc=example,dc=com
> isMemberOf: cn=My Static Group,ou=Groups,dc=example,dc=com
> isMemberOf: cn=My Dynamic Group,ou=Groups,dc=example,dc=com
> isMemberOf: cn=Virtual Static,ou=Groups,dc=example,dc=com
> isMemberOf: cn=Carpoolers,ou=Self Service,ou=Groups,dc=example,dc=com
> ```

You must request `isMemberOf` explicitly.

For a dynamic group, you can check the membership directly on the candidate member's entry using the same search criteria as the dynamic group's member URL.

## Referential integrity

When you delete or rename an entry that belongs to static groups, that entry's DN must be removed or changed in each group it belongs to. You can configure the server to resolve membership changes by enabling referential integrity.

Referential integrity functionality is implemented as a plugin. The referential integrity plugin is disabled by default. To enable the plugin, use the `dsconfig` command:

```console
$ dsconfig \
 set-plugin-prop \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --plugin-name "Referential Integrity" \
 --set enabled:true \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
```

With the plugin enabled, referential integrity resolves group membership automatically:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 --baseDN dc=example,dc=com \
 "(cn=My Static Group)"
```

> **Collapse: Show output**
>
> ```
> dn: cn=My Static Group,ou=Groups,dc=example,dc=com
> objectClass: groupOfNames
> objectClass: top
> cn: My Static Group
> member: uid=ahunter,ou=People,dc=example,dc=com
> member: uid=bjensen,ou=People,dc=example,dc=com
> member: uid=tmorris,ou=People,dc=example,dc=com
> member: uid=scarter,ou=People,dc=example,dc=com
> ou: Groups
> ```

```console
$ ldapdelete \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 uid=scarter,ou=People,dc=example,dc=com
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=kvaughan,ou=People,dc=example,dc=com \
 --bindPassword bribery \
 --baseDN dc=example,dc=com \
 "(cn=My Static Group)"
```

> **Collapse: Show output**
>
> ```
> dn: cn=My Static Group,ou=Groups,dc=example,dc=com
> objectClass: groupOfNames
> objectClass: top
> cn: My Static Group
> member: uid=ahunter,ou=People,dc=example,dc=com
> member: uid=bjensen,ou=People,dc=example,dc=com
> member: uid=tmorris,ou=People,dc=example,dc=com
> ou: Groups
> ```

By default, the referential integrity plugin is configured to manage `member` and `uniqueMember` attributes. These attributes take values that are DNs, and are indexed for equality by default for the default backend. Before you add an additional attribute to manage, make sure that it has DN syntax and that it is indexed for equality. DS servers require indexes because an unindexed search can consume too many of the server's resources. For instructions on indexing attributes, refer to [Configure indexes](idx-config.html).

Consider these settings when configuring the referential integrity plugin:

* `check-references:true` checks that members' entries exist when added to a group.

* `check-references-filter-criteria` lets your members' entries match an LDAP filter.

  For example, `check-references-filter-criteria:member:(objectclass=person)` checks that members are person entries.

* `check-references-scope-criteria:naming-context` checks that members' entries are in the same naming context (base DN).

---

---
title: HTTP access
description: Configure HTTP ports, authorization mechanisms, and administrative API endpoints on PingDS servers.
component: pingds
version: 8.1
page_id: pingds:config-guide:http-access
canonical_url: https://docs.pingidentity.com/pingds/8.1/config-guide/http-access.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Features", "REST API", "Setup &amp; Configuration"]
section_ids:
  setup-http-connection-handler: Set the HTTP port
  setup-https-access: Set the HTTPS port
  setup-http-authorization: Configure HTTP authorization
  setup-admin-endpoint: Use administrative APIs
---

# HTTP access

This page describes how to configure HTTP ports for DS servers.

Alternatively, you can configure unified connection handlers to process HTTP and LDAP on the same port. Learn more in [Administrative and unified access](admin-access.html).

## Set the HTTP port

The following steps demonstrate how to set up an HTTP port if none was configured at setup time with the `--httpPort` option:

1. Create an HTTP connection handler:

   ```console
   $ dsconfig \
    create-connection-handler \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --handler-name HTTP \
    --type http \
    --set enabled:true \
    --set listen-port:8080 \
    --no-prompt \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin
   ```

2. Enable an HTTP access log.

   1. The following command enables JSON-based HTTP access logging:

      ```console
      $ dsconfig \
       set-log-publisher-prop \
       --hostname localhost \
       --port 4444 \
       --bindDN uid=admin \
       --bindPassword password \
       --publisher-name "Json File-Based HTTP Access Logger" \
       --set enabled:true \
       --no-prompt \
       --trustStorePath /path/to/opendj/config/keystore \
       --trustStoreType PKCS12 \
       --trustStorePassword:file /path/to/opendj/config/keystore.pin
      ```

   2. The following command enables HTTP access logging:

      ```console
      $ dsconfig \
       set-log-publisher-prop \
       --hostname localhost \
       --port 4444 \
       --bindDN uid=admin \
       --bindPassword password \
       --publisher-name "File-Based HTTP Access Logger" \
       --set enabled:true \
       --no-prompt \
       --trustStorePath /path/to/opendj/config/keystore \
       --trustStoreType PKCS12 \
       --trustStorePassword:file /path/to/opendj/config/keystore.pin
      ```

3. After you set up an HTTP port, enable an HTTP endpoint.

   For details, refer to [Use administrative APIs](#setup-admin-endpoint).

## Set the HTTPS port

At setup time use the `--httpsPort` option.

Later, follow these steps to set up an HTTPS port:

1. Create an HTTPS connection handler.

   The following example sets the port to `8443` and uses the default server certificate:

   ```console
   $ dsconfig \
    create-connection-handler \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --handler-name HTTPS \
    --type http \
    --set enabled:true \
    --set listen-port:8443 \
    --set use-ssl:true \
    --set key-manager-provider:PKCS12 \
    --set trust-manager-provider:"JVM Trust Manager" \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

   If the key manager provider has multiple key pairs that DS could use for TLS, where the secret key was generated with the same key algorithm, such as `EC` or `RSA`, you can specify which key pairs to use with the `--set ssl-cert-nickname:server-cert` option. The *server-cert* is the certificate alias of the key pair. This option is not necessary if there is only one server key pair, or if each secret key was generated with a different key algorithm.

2. Enable the HTTP access log.

   1. The following command enables JSON-based HTTP access logging:

      ```console
      $ dsconfig \
       set-log-publisher-prop \
       --hostname localhost \
       --port 4444 \
       --bindDN uid=admin \
       --bindPassword password \
       --publisher-name "Json File-Based HTTP Access Logger" \
       --set enabled:true \
       --no-prompt \
       --trustStorePath /path/to/opendj/config/keystore \
       --trustStoreType PKCS12 \
       --trustStorePassword:file /path/to/opendj/config/keystore.pin
      ```

   2. The following command enables HTTP access logging:

      ```console
      $ dsconfig \
       set-log-publisher-prop \
       --hostname localhost \
       --port 4444 \
       --bindDN uid=admin \
       --bindPassword password \
       --publisher-name "File-Based HTTP Access Logger" \
       --set enabled:true \
       --no-prompt \
       --trustStorePath /path/to/opendj/config/keystore \
       --trustStoreType PKCS12 \
       --trustStorePassword:file /path/to/opendj/config/keystore.pin
      ```

3. If the deployment requires SSL client authentication, set the properties `ssl-client-auth-policy` and `trust-manager-provider` appropriately.

4. After you set up an HTTPS port, enable an HTTP endpoint.

   For details, refer to [Use administrative APIs](#setup-admin-endpoint).

## Configure HTTP authorization

HTTP authorization mechanisms map HTTP credentials to LDAP credentials.

Multiple HTTP authorization mechanisms can be enabled simultaneously.

These HTTP authorization mechanisms are supported:

* HDAP (enabled by default)

  Process anonymous, basic and bearer authorization requests.

  This mechanism treats anonymous requests like the HTTP Anonymous mechanism.

  For HTTP Basic requests, this mechanism matches an HDAP resource `_id` to the DN. The `_id` matches the suffix of the path to the resource. For example, the default directory superuser `_id` is `uid=admin`. Babs Jensen's `_id` is `dc=com/dc=example/ou=People/uid=bjensen`.

  For HTTP Bearer requests, this mechanism uses a JSON Web Token (JWT). Get the JWT with the HDAP `authenticate` action. Learn more in [Bearer auth](../rest-guide/rest-operations.html#authenticate-rest-bearer).

* HTTP Anonymous (enabled by default)

  Process anonymous HTTP requests, optionally binding with a specified DN.

  If the client does not specify a bind DN (default), it binds as an anonymous LDAP user.

* HTTP Basic (enabled by default)

  Process [HTTP Basic authorization](https://www.rfc-editor.org/info/rfc7235) requests by mapping the HTTP Basic identity to a user's directory account.

  By default, DS uses the exact match identity mapper with its default configuration to map the HTTP Basic username to an LDAP `uid`. DS searches all local public naming contexts to find the user's entry based in the `uid` value. Learn more in [Identity mappers](../ldap-guide/client-auth.html#client-auth-identity-mappers).

## Use administrative APIs

The APIs for configuring and monitoring DS servers are under the following endpoints:

* `/alive`

  Check whether the server is currently *alive*, meaning its internal checks have not found any errors that would require administrative action.

  By default, this endpoint returns a status code to anonymous requests and supports authenticated requests. For details, refer to [Server is alive (HTTP)](../monitoring-guide/http-monitoring.html#monitoring-liveness-http).

* `/healthy`

  Check whether the server is currently *healthy*, meaning it's alive, the replication server is accepting connections on the configured port, and any replication delays are below the configured threshold.

  By default, this endpoint returns a status code to anonymous requests, and supports authenticated requests. For details, refer to [Server health (HTTP)](../monitoring-guide/http-monitoring.html#monitoring-health-http).

* `/metrics/prometheus/0.0.4`

  Access the server monitoring information in [Prometheus monitoring software](https://prometheus.io/) format.

  By default, DS protects this endpoint with the HTTP Basic authorization mechanism. Users reading monitoring information must have the `monitor-read` privilege.

To use these APIs, follow these steps:

1. Grant access to the `/metrics/prometheus/0.0.4` endpoint, if necessary, by assigning the `monitor-read` privilege.

   For details, refer to [Administrative privileges](../security-guide/admin.html#admin-privileges).

   Alternatively, create a monitor user with the `setup` command when installing DS.

2. Adjust the `authorization-mechanism` settings for the Admin endpoint.

   By default, DS uses the HTTP Basic authorization mechanism. The HTTP Basic authorization mechanism default configuration resolves the user identity extracted from the HTTP request to an LDAP user identity as follows:

   * If the request has an `Authorization: Basic` header for HTTP Basic authentication, DS extracts the username and password.

   * If the request has `X-OpenIDM-Username` and `X-OpenIDM-Password` headers, DS extracts the username and password.

   * DS uses the default exact match identity mapper to search for a unique match between the username and the UID attribute value of an entry in the local public naming contexts of the DS server.

     In LDAP terms, it searches all user base DNs for `(uid=<http-username>)`. The username `kvaughan` maps to the example entry with DN `uid=kvaughan,ou=People,dc=example,dc=com`.

     For details, refer to [Identity mappers](../ldap-guide/client-auth.html#client-auth-identity-mappers) and [Configure HTTP authorization](#setup-http-authorization).

3. Test access to the endpoint as an authorized user.

---

---
title: Index types
description: Understand the index types PingDS directory servers support, including equality, substring, ordering, big, and virtual list view indexes.
component: pingds
version: 8.1
page_id: pingds:config-guide:idx-types
canonical_url: https://docs.pingidentity.com/pingds/8.1/config-guide/idx-types.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Features", "LDAP", "Setup &amp; Configuration"]
section_ids:
  indexes-presence: Presence index
  indexes-equality: Equality index
  indexes-approximate: Approximate index
  indexes-substring: Substring index
  indexes-ordering: Ordering index
  big-indexes: Big index
  indexes-vlv: Virtual list view (browsing) index
  indexes-extensible: Extensible matching rule index
---

# Index types

DS directory servers support multiple index types, each corresponding to a different type of search.

View what is indexed by using the `backendstat list-indexes` command. For details about a particular index, you can use the `backendstat dump-index` command.

## Presence index

A presence index matches an attribute that is present on the entry, regardless of the value. By default, the `aci` attribute is indexed for presence:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=admin \
 --bindPassword password \
 --baseDN dc=example,dc=com \
 "(aci=*)" \
 aci
```

A presence index takes up less space than other indexes. In a presence index, there is just one key with a list of IDs.

When the index list length is small, presence indexes are useful for attributes present in a relatively small percentage of directory entries.

The following command examines the ACI presence index for a server configured with the evaluation profile. Optionally, stop the server before running the command:

```console
$ stop-ds
$ backendstat \
 dump-index \
 --baseDn dc=example,dc=com \
 aci.presence
```

> **Collapse: Show output**
>
> ```
> Key (len 1): PRESENCE
> Value (len 3): [COUNT:2] 1 9
>
> Total Records: 1
> Total / Average Key Size: 1 bytes / 1 bytes
> Total / Average Data Size: 3 bytes / 3 bytes
> ```

In this case, entries with ACI attributes have IDs `1` and `9`.

## Equality index

An equality index matches values that correspond exactly (generally ignoring case) to those in search filters. An equality index requires clients to match values without wildcards or misspellings:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=bjensen,ou=People,dc=example,dc=com \
 --bindPassword hifalutin \
 --baseDN dc=example,dc=com \
 "(uid=bjensen)" \
 mail
```

> **Collapse: Show output**
>
> ```
> dn: uid=bjensen,ou=People,dc=example,dc=com
> mail: bjensen@example.com
> ```

An equality index has one list of entry IDs for each attribute value. Depending on the backend implementation, the keys in a case-insensitive index might not be strings. For example, a key of `6A656E73656E` could represent `jensen`.

The following command examines the SN equality index for a server configured with the evaluation profile. Optionally, stop the server before running the command:

```console
$ stop-ds
$ backendstat \
 dump-index \
 --baseDN dc=example,dc=com \
 sn.caseIgnoreMatch | grep -A 1 "jensen$"
```

> **Collapse: Show output**
>
> ```
> Key (len 6): jensen
> Value (len 26): [COUNT:17] 18 31 32 66 79 94 133 134 150 5996 19415 32834 46253 59672 73091 86510 99929
> ```

In this case, there are 17 entries that have an SN of Jensen.

Unless the keys are encrypted, the server can reuse an equality index for ordering and initial substring searches.

## Approximate index

An approximate index matches values that "sound like" those provided in the filter. An approximate index on `sn` lets client applications find people even when they misspell surnames:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=bjensen,ou=People,dc=example,dc=com \
 --bindPassword hifalutin \
 --baseDN dc=example,dc=com \
 "(&(sn~=Jansen)(cn=Babs*))" \
 cn
```

> **Collapse: Show output**
>
> ```
> dn: uid=bjensen,ou=People,dc=example,dc=com
> cn: Barbara Jensen
> cn: Babs Jensen
> ```

An approximate index squashes attribute values into a normalized form.

The following command examines an SN approximate index added to a server configured with the evaluation profile. Optionally, stop the server before running the command:

```console
$ stop-ds
$ backendstat \
 dump-index \
 --baseDN dc=example,dc=com \
 sn.ds-mr-double-metaphone-approx | grep -A 1 "JNSN$"
```

> **Collapse: Show output**
>
> ```
> Key (len 4): JNSN
> Value (len 83): [COUNT:74] 18 31 32 59 66 79 94 133 134 150 5928 5939 5940 5941 5996 5997 6033 6034 19347 19358 19359 19360 19415 19416 19452 19453 32766 32777 32778 32779 32834 32835 32871 32872 46185 46196 46197 46198 46253 46254 46290 46291 59604 59615 59616 59617 59672 59673 59709 59710 73023 73034 73035 73036 73091 73092 73128 73129 86442 86453 86454 86455 86510 86511 86547 86548 99861 99872 99873 99874 99929 99930 99966 99967
> ```

In this case, there are 74 entries that have an SN that sounds like Jensen.

## Substring index

A substring index matches values that are specified with wildcards in the filter. Substring indexes can be expensive to maintain, especially for large attribute values:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=bjensen,ou=People,dc=example,dc=com \
 --bindPassword hifalutin \
 --baseDN dc=example,dc=com \
 "(cn=Barb*)" \
 cn
```

> **Collapse: Show output**
>
> ```
> dn: uid=bfrancis,ou=People,dc=example,dc=com
> cn: Barbara Francis
>
> dn: uid=bhal2,ou=People,dc=example,dc=com
> cn: Barbara Hall
>
> dn: uid=bjablons,ou=People,dc=example,dc=com
> cn: Barbara Jablonski
>
> dn: uid=bjensen,ou=People,dc=example,dc=com
> cn: Barbara Jensen
> cn: Babs Jensen
>
> dn: uid=bmaddox,ou=People,dc=example,dc=com
> cn: Barbara Maddox
> ```

In a substring index, there are enough keys to match any substring in the attribute values. Each key is associated with a list of IDs. The default maximum size of a substring key is six bytes.

The following command examines an SN substring index for a server configured with the evaluation profile. Optionally, stop the server before running the command:

```console
$ stop-ds
$ backendstat \
dump-index \
 --baseDN dc=example,dc=com \
 sn.caseIgnoreSubstringsMatch:6
```

> **Collapse: Show output**
>
> ```
> ...
> Key (len 1): e
> Value (len 25): [COUNT:22] ...
> ...
> Key (len 2): en
> Value (len 15): [COUNT:12] ...
> ...
> Key (len 3): ens
> Value (len 3): [COUNT:1] 147
> Key (len 5): ensen
> Value (len 10): [COUNT:9] 18 31 32 66 79 94 133 134 150
> ...
> Key (len 6): jensen
> Value (len 10): [COUNT:9] 18 31 32 66 79 94 133 134 150
> ...
> Key (len 1): n
> Value (len 35): [COUNT:32] ...
> ...
> Key (len 2): ns
> Value (len 3): [COUNT:1] 147
> Key (len 4): nsen
> Value (len 10): [COUNT:9] 18 31 32 66 79 94 133 134 150
> ...
> Key (len 1): s
> Value (len 13): [COUNT:12] 12 26 47 64 95 98 108 131 135 147 149 154
> ...
> Key (len 2): se
> Value (len 7): [COUNT:6] 52 58 75 117 123 148
> Key (len 3): sen
> Value (len 10): [COUNT:9] 18 31 32 66 79 94 133 134 150
> ...
> ```

In this case, the SN value Jensen shares substrings with many other entries. The size of the lists and number of keys make a substring index much more expensive to maintain than other indexes. This is particularly true for longer attribute values.

## Ordering index

An ordering index is used to match values for a filter that specifies a range. For example, the `ds-sync-hist` attribute used by replication has an ordering index by default. Searches on that attribute often seek entries with changes more recent than the last time a search was performed.

The following example shows a search that specifies a range on the SN attribute value:

```console
$ ldapsearch \
 --hostname localhost \
 --port 1636 \
 --useSsl \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --bindDN uid=bjensen,ou=People,dc=example,dc=com \
 --bindPassword hifalutin \
 --baseDN dc=example,dc=com \
 "(sn>=zyw)" \
 sn
```

> **Collapse: Show output**
>
> ```
> dn: uid=user.13401,ou=People,dc=example,dc=com
> sn: Zywiel
>
> dn: uid=user.26820,ou=People,dc=example,dc=com
> sn: Zywiel
>
> dn: uid=user.40239,ou=People,dc=example,dc=com
> sn: Zywiel
>
> dn: uid=user.53658,ou=People,dc=example,dc=com
> sn: Zywiel
>
> dn: uid=user.67077,ou=People,dc=example,dc=com
> sn: Zywiel
>
> dn: uid=user.80496,ou=People,dc=example,dc=com
> sn: Zywiel
>
> dn: uid=user.93915,ou=People,dc=example,dc=com
> sn: Zywiel
> ```

In this case, the server only requires an ordering index if it cannot reuse the (ordered) equality index instead. For example, if the equality index is encrypted, an ordering index must be maintained separately.

## Big index

A big index is designed for attributes where many, many entries have the same attribute value.

This can happen for attributes whose values all belong to a known enumeration. For example, if you have a directory service with an entry for each person in the United States, the `st` (state) attribute is the same for more than 30 million Californians (`st: CA`). With a regular equality index, a search for `(st=CA)` would be unindexed. With a big index, the search is indexed, and optimized for paging through the results. For an example, refer to [Indexes for attributes with few unique values](idx-config.html#use-big-indexes).

A big index can be easier to configure and to use than a virtual list view index. Consider big indexes when:

* Many1 entries have the same value for a given attribute.

  DS search performance with a big index is equivalent to search performance with a standard index. For attributes with only a few unique values, big indexes support much higher modification rates.

* Modifications outweigh searches for the attribute.

  When attributes have a wide range of possible values, favor standard indexes, except when the attribute is often the target of modifications, and only sometimes part of a search filter.

1 Many, but not all entries. **Do not create a big index for all values of the `objectClass` attribute, for example.** When all entries have the same value for an attribute, as is the case for `objectClass: top`, indexes consume additional system resources and disk space with no benefit. The DS server must still read every entry to return search results. In practice, the upper limit is probably somewhat less than half the total entries. In other words, if half the entries have the same value for an attribute, it will cost more to maintain the big index than to evaluate all entries to find matches for the search. Let such searches remain *unindexed* searches.

## Virtual list view (browsing) index

A virtual list view index (VLV index) *(tooltip: \<div class="paragraph">
\<p>Matches browsing requests for paging through a long list of results.\</p>
\</div>)* is designed to help applications that list results. For example, a GUI application might let users browse through a list of users. VLVs help the server respond to clients that request server-side sorting of the search results.

VLV indexes correspond to particular searches. Configure your VLV indexes using the command line.

## Extensible matching rule index

In some cases, you need an index for a matching rule other than those described above.

For example, a generalized time-based matching index lets applications find entries with a time-based attribute later or earlier than a specified time.

---

---
title: Indexes
description: Overview of PingDS indexing pages covering index types, configuration, verification, and debugging to help searches run efficiently.
component: pingds
version: 8.1
page_id: pingds:config-guide:indexing
canonical_url: https://docs.pingidentity.com/pingds/8.1/config-guide/indexing.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Features", "LDAP"]
---

# Indexes

These pages show you how to configure and debug indexes so DS can respond quickly to searches:

* [About indexes](idx-about.html)

* [What to index](idx-what.html)

* [Index types](idx-types.html)

* [Indexing tools](idx-tools.html)

* [Configure indexes](idx-config.html)

* [Verify indexes](idx-verify.html)

* [Debug a missing index](idx-debug.html)