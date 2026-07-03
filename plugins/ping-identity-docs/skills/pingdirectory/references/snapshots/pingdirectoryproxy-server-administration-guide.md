---
title: About alternate authorization identities
description: Alternate authorization identities allow for the proper evaluation of access control rules for users whose entries aren't present within an entry-balanced dataset.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectoryproxy_server_administration_guide:pd_proxy_about_alt_authn_ids
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectoryproxy_server_administration_guide/pd_proxy_about_alt_authn_ids.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  processing-steps: Processing steps
---

# About alternate authorization identities

Alternate authorization identities allow for the proper evaluation of access control rules for users whose entries aren't present within an entry-balanced dataset.

Whenever the PingDirectoryProxy server forwards a request to the backend set containing the user's entry, it forwards the request with an authorization identity that reflects the user's actual identity because the user is known to servers in that set. However, when forwarding a request to a backend set that doesn't contain the user's entry, the PingDirectoryProxy server uses an alternate authorization identity that reflects the generic user with the same set of rights as the actual user issuing the request.

Alternate authorization identities allow for the proper evaluation of access control rules for users whose entries are not present within an entry-balanced dataset.

There are only a few different generic classes of users from an access control perspective. These can be placed in a portion of the directory information tree (DIT) that isn't below the entry-balancing base distinguished name (DN) and is replicated to all servers in the topology.

Whenever a user authenticates to the PingDirectoryProxy server, the server can keep track of which backend set holds that user's entry and determine whether an alternate authorization identity is required. The server can determine which of these generic accounts best describes the rights that the user should have.

For the following example, assume that you have three classes of users: full administrators, password administrators, and normal users. Assume that you create the following entries in the topology and assign them the appropriate access rights:

* `uid=normal user,dc=example,dc=com`

* `uid=server-admin,dc=example,dc=com`

* `uid=password-admin,dc=example,dc=com`

![An illustrated workflow of an alternate authorization identity solving an access control issue in an entry-balancing deployment. The processing steps section below describes the workflow in detail. The client with uid=5000 is represented by a person at a desktop. The flow moves down from the client sending a bind request to the proxy server 01 which is represented by a box with the global index box sitting beside it. The the flow moves from the Proxy Server 01 in two directions: it sends a search request represented by an orange line to the entry balancing set 02 represented by a box with an orange outline and it sends a bind request represented by a green line to entry balancing set 01 represented by a box with a green outline. The entry balancing set 01 contains the base distinguished name, normal users, full administrators, and password administrator users, entries in the uid=0-10000 range, access control instructions, and an entry balancing point. The flow within is described in the processing steps. The entry balancing set 02 contains the base distinguished name, normal users, full administrators, and password administrator users, entries for uid=10001-20000, access control instructions, and an entry balancing point. The flow within is described in the processing steps.](_images/aqs1564012014720.png)Alternate Authorization Identity Solves Access Control Issues in Entry-Balancing Deployments

## Processing steps

1. The client with `uid=5000` binds to the PingDirectoryProxy server, which sends a `BIND` request to entry-balancing set-01.

2. The client sends a `SEARCH` request for `uid=15000`.

3. The PingDirectoryProxy server determines that `uid=15000` lives on entry-balancing set-02.

4. The PingDirectoryProxy server then determines that the client `uid=5000` doesn't have an entry on entry-balancing set-02.

5. The PingDirectoryProxy server uses an alternate authorization identity that reflects the generic user, `uid=normal user`, which has the same set of rights as the client `uid=5000` issuing the request.

6. The access control is accepted and the `SEARCH` request returns a response for `uid=5000`.

7. When an alternate authorization identity is invoked, `authzID='dn:uid=normal user,dc=example,dc=com` records in the server log, which indicates the use of the alternate authorization identity.

   For example, if the `user.15000` is in a different backend set from `user.5000`, the log shows the following response.

   ```
   % bin/ldapsearch -D "uid=user.5000,ou=people,dc=example,dc=com" -w pasword \
     -b uid=user15000,ou=people,dc=example,dc=com "(objectclass=)"

   [18/Aug/2013:11:54:35 -0500] SEARCH REQUEST conn=153 op=1 msgID=2
   via="app='Directory-Proxy address='127.0.0.1'
   authzID='dn:uid=normal user,dc=example,dcom' sessionID='conn=2'
   requestID='op=1'" base="uid=user.150000,ou=people,dc=example,dc=com"scope=2
   filter="(objectclass=)" attrs="ALL"

   [18/Aug/2013:11:54:35 -0500] SEARCH REQUEST conn=153 op=1 msgID=2 resultCode=0 etime=2.038
   entriesReturned=1 authzDN="uid=normal-user,dc=example,dc=com"
   ```

---

---
title: About client connection policies
description: Client connection policies define the general behavior the server exhibits when communicating with a set of clients.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectoryproxy_server_administration_guide:pd_proxy_client_connection_policies
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectoryproxy_server_administration_guide/pd_proxy_client_connection_policies.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 25, 2024
---

# About client connection policies

Client connection policies define the general behavior the server exhibits when communicating with a set of clients.

Each policy contains the following:

* A set of connection criteria that define which client is associated with the policy based on information the server has about the client, including:

  * Client address

  * Protocol used

  * Secure communication mechanism

  * Location of the client's entry in the PingDirectoryProxy server

  * Contents of the client's entry

  These criteria are the same as those used for filtered logging. For example, different client connection policies could be established for different classes of users, such as root and non-root users.

* A set of constraints on the type of operations a client can request. You can specify whether a particular type of operation is allowed for clients.

  For some operation types, such as extended operations, you can allow only a particular subset of an operation type, such as a particular extended operation.

* A set of subtree views that define information about the parts of the directory information tree (DIT) the client can access.

When a client connection is established, only one client connection policy is applied. If the criteria for several policies match the same client connection, the evaluation order index is used as a tiebreaker. If no policy matches, the client connection is terminated. If the client binds, changing its identity, or uses StartTLS to convert from an insecure connection to a secure connection, then the connection is evaluated again to determine if it matches the same or a different client connection policy. The connection is terminated if it no longer matches any policy.

Learn more about [Client connection policy configuration](../pingdirectory_server_administration_guide/pd_ds_client_connection_policy_config.html).

---

---
title: About creating a custom health check
description: You can create a new health check from scratch or use an existing health check as a template for the configuration of a new health check.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectoryproxy_server_administration_guide:pd_proxy_about_creating_custom_health_check
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectoryproxy_server_administration_guide/pd_proxy_about_creating_custom_health_check.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# About creating a custom health check

You can create a new health check from scratch or use an existing health check as a template for the configuration of a new health check.

If you choose to create a custom health check, you can create one of the following types:

* Admin Alert Health Check

  This health check watches for administrative alerts generated by the LDAP external server to determine whether the server has entered a degraded or unavailable state.

* Groovy Scripted LDAP Health Check

  This health check allows you to create custom LDAP health checks in a dynamically-loaded Groovy script, which implements the `ScriptedLDAPHealthCheck` class defined in the Server SDK.

* Replication Backlog Health Check

  While the Admin Alert Health Check consumes replication backlog alerts emitted from external servers, a finer definition of external server health based on replication backlog can be defined with this health check. If a server falls too far behind in replication, then the PingDirectoryProxy server can stop sending requests to it. A server is classified as degraded or unavailable if the threshold is reached for the number of backlogged changes, the age of the oldest backlogged change, or both.

* Search LDAP Health Check

  This health check performs searches on an LDAP external server and gauges the health of the server depending on the response time in which the expected results were returned. For example, if an error occurs while attempting to communicate with the server, then the server is considered unavailable. You can also apply filters to the results to use values within the monitor entry as indicators of server health.

* Third Party LDAP Health Check

  This health check allows you to define LDAP health check implementations in third-party code using the Server SDK.

* Work Queue Busyness Health Check

  This health check can monitor the percentage of time that worker threads in backend servers devote to processing requests.

---

---
title: About dynamic rebalancing
description: During dynamic rebalancing, entries get moved as they are modified. You configure dynamic rebalancing in the entry counter placement algorithm or a third-party placement algorithm that supports rebalancing.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectoryproxy_server_administration_guide:pd_proxy_dynamic_rebalancing
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectoryproxy_server_administration_guide/pd_proxy_dynamic_rebalancing.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# About dynamic rebalancing

During dynamic rebalancing, entries get moved as they are modified. You configure dynamic rebalancing in the entry counter placement algorithm or a third-party placement algorithm that supports rebalancing.

This algorithm keeps a count of the number of entries or the size of the backend set. Configure dynamic rebalancing using the following parameters:

`rebalancing-enabled`

Determines whether entry rebalancing is enabled. When rebalancing is enabled, the placement algorithm is consulted after `modify` and `add` operations to determine whether the target entry should be moved to a different backend set. `rebalancing-scope`

Indicates which modified entries are candidates for rebalancing. A value of `top-level` indicates that only entries immediately below the entry-balancing base can be rebalanced. A value of any indicates that entries at any level below the entry-balancing base might be rebalanced. `rebalancing-minimum-percentage`

Specifies the minimum threshold for entries to be migrated from one backend set to a preferred backend set with a smaller size. Entries are not migrated unless the percentage difference between the value of the current backend set and the value of the preferred backend set exceeds this threshold. This parameter prevents unnecessarily migrating entries back and forth between backend sets of similar sizes. `rebalancing-subtree-size-limit`

Specifies the maximum size of a subtree that can be rebalanced. `poll-interval`

Specifies how long to wait between polling the size of the backends to determine how to rebalance and works in conjunction with the `rebalancing-minimum-percentage` property. `placement-criteria`

Determines which approach to use to select a destination backend for rebalancing. Possible values are:

* `entry-count`

* `backend-size`

* `custom`

The following figure illustrates an entry-balancing base DN and three subtrees, A, B, and C. If the rebalancing scope is set to `any`, any child entries under the base DN can be rebalanced. For example, if a change is made to entry A1, the entire subtree A might be rebalanced, depending upon how you have configured rebalancing. If the rebalancing scope is set to `top-level`, rebalancing is only triggered when entries at the top level, such as A, are modified. Changes made to subentries, such as A1 or A2, do not trigger rebalancing. Rebalancing is also triggered upon the addition of entries such as `A1,A2`, provided the scope is `any`.

![Diagram showing rebalancing at the top level.](_images/jeq1564012002622.png)

If you are writing your own third-party algorithm, you program dynamic rebalancing using the `SelectRebalancingBackendSet` method on the placement algorithm. Learn more in the [Server SDK documentation](https://developer.pingidentity.com/reference/server-sdk/latest/).

---

---
title: About encrypting log files
description: The server lets you encrypt log files as they are written.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectoryproxy_server_administration_guide:pd_proxy_encrypt_log_files
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectoryproxy_server_administration_guide/pd_proxy_encrypt_log_files.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
page_aliases: ["pd_proxy_config_log_signing.adoc", "pd_proxy_validate_signed_file.adoc", "pd_proxy_config_log_file_encryption.adoc"]
section_ids:
  configuring-log-signing: Configuring log signing
  steps: Steps
  example: Example:
  example-2: Example:
  validating-a-signed-file: Validating a signed file
  steps-2: Steps
  example-3: Example:
  result: Result:
  configuring-log-file-encryption: Configuring log file encryption
  steps-3: Steps
  example-4: Example:
  example-5: Example:
---

# About encrypting log files

The server lets you encrypt log files as they are written.

The `encrypt-log` configuration property controls whether encryption is enabled for the logger. Enabling encryption causes the log file to have an `.encrypted` extension. If both encryption and compression are enabled, the extension is `.gz.encrypted`. Any change that affects the name used for the log file could prevent older files from getting properly cleaned up.

Like compression, encryption can only be enabled when the logger is created. Encryption can't be turned on or off after the logger is configured. For any log file that is encrypted, enabling compression is also recommended to reduce the amount of data that needs to be encrypted. This reduces the overall size of the log file. The `encrypt-file` tool or custom code, using the LDAP SDK's `com.unboundid.util.PassphraseEncryptedInputStream`, is used to access the encrypted data.

To enable encryption, at least one encryption settings definition must be defined in the server. Use the one created during setup, or create a new one with the `encryption-settings create` command. By default, the encryption is performed with the server's preferred encryption settings definition.

To explicitly specify which definition should be used for the encryption, set the `encryption-settings-definition-id` property with the ID of that definition. You should set the encryption settings definition to be created from a passphrase so that the file can be decrypted by providing that passphrase even if the original encryption settings definition is no longer available. You can also create a randomly generated encryption settings definition, but the log file can only be decrypted using a server instance that has that encryption settings definition.

When using encrypted logging, a small amount of data might remain in an in-memory buffer until the log file is closed. The encryption is performed using a block cipher, and it can't write an incomplete block of data until the file is closed. This is not an issue for any log file that isn't being actively written.

To examine the contents of a log file that is being actively written, use the `rotate-log` tool to force the file to be rotated before attempting to examine it.

## Configuring log signing

Configure log signing for a log publisher.

### Steps

1. To enable log signing for a log publisher, use `dsconfig`.

   #### Example:

   In this example, the `sign-log` property is set on the File-based Audit Log Publisher.

   ```shell
   $ bin/dsconfig set-log-publisher-prop --publisher-name "File-Based Audit Logger" \
     --set sign-log:true
   ```

2. Disable and then re-enable the log publisher for the change to take effect.

   #### Example:

   ```shell
   $ bin/dsconfig set-log-publisher-prop --publisher-name "File-Based Audit Logger" \
     --set enabled:false
   $ bin/dsconfig set-log-publisher-prop --publisher-name "File-Based Audit Logger" \
     --set enabled:true
   ```

## Validating a signed file

The server provides a tool, `validate-file-signature`, that checks if a file hasn't been tampered with in any way.

### Steps

* Run the `validate-file-signature` tool to check if a signed file has been tampered with.

  #### Example:

  For this example, assume that the `sign-log` property was enabled for the File-Based Audit Log Publisher.

  ```shell
  $ bin/validate-file-signature --file logs/audit
  ```

  #### Result:

  ```
  All signature information in file 'logs/audit' is valid
  ```

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                  |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If any validation errors occur, you will see a message similar to the following:```
  One or more signature validation errors were encountered
  while validating the contents of file 'logs/audit':
  * The end of the input stream was encountered without
    encountering the end of an active signature block.
    The contents of this signed block cannot be trusted
    because the signature cannot be verified
  ``` |

## Configuring log file encryption

Configure log file encryption for a log publisher.

### Steps

1. To enable encryption for a log publisher, use `dsconfig`.

   #### Example:

   In this example, the File-based Access Log Publisher `"Encrypted Access"` is created, compression is set, and rotation and retention policies are set.

   ```shell
   $ bin/dsconfig create-log-publisher-prop --publisher-name "Encrypted Access" \
     --type file-based-access \
     --set enabled:true \
     --set compression-mechanism:gzip \
     --set encryption-settings-definition-id:332C846EF0DCD1D5187C1592E4C74CAD33FC1E5FC20B726CD301CDD2B3FFBC2B \
     --set encrypt-log:true \
     --set log-file:logs/encrypted-access \
     --set "rotation-policy:24 Hours Time Limit Rotation Policy" \
     --set "rotation-policy:Size Limit Rotation Policy" \
     --set "retention-policy:File Count Retention Policy" \
     --set "retention-policy:Free Disk Space Retention Policy" \
     --set "retention-policy:Size Limit Retention Policy"
   ```

2. Decrypt and decompress the file.

   #### Example:

   ```shell
   $ bin/encrypt-file --decrypt \
     --decompress-input \
     --input-file logs/encrypted-access.20180216040332Z.gz.encrypted \
     --output-file decrypted-access
   Initializing the server's encryption framework...Done
   Writing decrypted data to file '/ds/Data-Sync/decrypted-access' using a
   key generated from encryption settings definition '332c846ef0dcd1d5187c1592e4c74cad33fc1e5fc20b726cd301cdd2b3ffbc2b'
   Successfully wrote 123,456,789 bytes of decrypted data
   ```

---

---
title: About entry balancing
description: Entry balancing allows you to automatically spread entries below a common parent among multiple sets of directory servers for improved scalability and performance.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectoryproxy_server_administration_guide:pd_proxy_entry_balancing
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectoryproxy_server_administration_guide/pd_proxy_entry_balancing.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# About entry balancing

Entry balancing allows you to automatically spread entries below a common parent among multiple sets of directory servers for improved scalability and performance.

Entry balancing can take advantage of a global index. A global index is an in-memory cache used for quickly determining which set or sets of servers to use to process a request based on the entry distinguished names (DNs) and attribute values.

For information about configuring entry balancing, see [Deploying an entry-balancing proxy configuration](pd_proxy_deploy_entry_balancing_proxy_config.html).

---

---
title: About LDAP external servers
description: PingDirectoryProxy allows you to configure different types of LDAP external servers.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectoryproxy_server_administration_guide:pd_proxy_ldap_ext_servers
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectoryproxy_server_administration_guide/pd_proxy_ldap_ext_servers.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# About LDAP external servers

PingDirectoryProxy allows you to configure different types of LDAP external servers.

You can configure information about the directory server instances accessed by PingDirectoryProxy. The default configuration for each type is tuned to be the best possible configuration for each.

The configuration information includes the following:

* Server connection information, such as IP address, port, and security layer

* Location

* Authentication information

* Methods for authenticating and authorizing clients

* Server-specific health checks

* Types of operations allowed

  For example, some LDAP external servers might allow only reads and others allow reads and writes so that the PingDirectoryProxy server can recognize this and accommodate it.

For more information about configuring LDAP external servers, see [Configuring LDAP external servers](pd_proxy_config_ldap_ext_servers.html).

---

---
title: About LDAP health checks
description: LDAP health checks provide information about the status and availability of LDAP external servers. Configure the PingDirectoryProxy server health checks that work best for your environment.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectoryproxy_server_administration_guide:pd_proxy_ldap_health_checks
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectoryproxy_server_administration_guide/pd_proxy_ldap_health_checks.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  results: Results
  frequency: Frequency
  server-states-and-search-response-times: Server states and search response times
---

# About LDAP health checks

LDAP health checks provide information about the status and availability of LDAP external servers. Configure the PingDirectoryProxy server health checks that work best for your environment.

PingDirectoryProxy provides the following health checks:

* Measure the response time for searches and examine the entry contents

  The health check might retrieve a monitoring entry from a server and base the health check result on whether the entry was returned, how long it took to be returned, and whether the value of the returned entry matches what was expected.

* Monitor the replication backlog

  If a server falls too far behind in replication, then the PingDirectoryProxy server can stop sending requests to it. A server is classified as `degraded` or `unavailable` if the threshold is reached for the number of missing changes, the age of the oldest missing change, or both.

* Consume Directory Server administrative alerts

  If the PingDirectory server indicates there is a problem, such as an index that must be rebuilt, then it flags itself as `degraded` or `unavailable`. When the PingDirectoryProxy server detects this, it stops sending requests to the server. The PingDirectoryProxy server detects administrative alerts as soon as they are issued by maintaining an LDAP persistent search for changes within the `cn=alerts` branch of the PingDirectory server.

  When the PingDirectoryProxy server is notified by the PingDirectory server of a new alert, it immediately retrieves the base `cn=monitor` entry of the PingDirectory server. If this entry has a value for the `unavailable-alert-type` attribute, then the PingDirectoryProxy server considers it unavailable. If this entry has a value for the `degraded-alert-type` attribute, then the PingDirectoryProxy server considers it `degraded`. Clients of the PingDirectoryProxy server can use a similar mechanism to detect and react when server flags itself as `degraded` or `unavailable`.

* Monitor the busyness of the server

  If a server becomes too busy, you can mark it as `degraded` or `unavailable` so that less heavily-loaded servers are preferred.

## Results

The health check results contain the following server states:

* `Available`

  Completely accessible for use.

* `Degraded`

  The server can be used if necessary but has a condition which can make it less desirable than other servers. For example, it is slow to respond or has fallen behind in replication.

* `Unavailable`

  Completely unsuitable for use. For example, the server is offline or is missing critical data.

Health check results include a numeric score that has a value between 1 and 10. This score helps rank servers with the same state. For example, two servers are available and one has a score of 8 and the other a score of 7, you can configure the PingDirectoryProxy server to prefer the server with the higher score.

The results of health checks are made available to the load-balancing algorithms to help determine where to send requests. The PingDirectoryProxy server attempts to use servers with a state of `available` before trying servers with a state of `degraded`. It never attempts to use servers with a state of `unavailable`.

Some load-balancing algorithms also take the health check score into account, such as the health-weighted load-balancing algorithm that prefers servers with higher scores over those with lower scores. You should configure the algorithms that work best for you environment.

## Frequency

The PingDirectoryProxy server periodically invokes health checks to monitor each LDAP external server and initiates health checks in response to failed operations. It checks the health of the LDAP external servers at intervals configured in the LDAP server's `health-check-frequency` property. The PingDirectoryProxy server contains safeguards to ensure that only one health check is in progress at any time against a backend server to avoid affecting its ability to process other requests.

To associate a health check with an LDAP external server and set the health check frequency, you must configure the `health-check` and `health-check-frequency` properties of the LDAP external server.

You can find more information about configuring the properties of the external server in [Configuring an external server using `dsconfig`](pd_proxy_config_ldap_ext_servers.html#config_ext_server_dsconfig).

## Server states and search response times

In some cases, an LDAP health check defines different sets of criteria for promoting and demoting the state of a server. A `degraded` server might need to meet more stringent requirements to be reclassified as `available` than originally for it to be considered `degraded`.

If response time is used in the process of determining the health of a server, then the PingDirectoryProxy server might have a faster response time threshold for transitioning a server from `degraded` back to `available` than the threshold used to consider it `degraded` in the first place. This threshold difference helps avoid cases in which a server repeatedly transitions between the two states because it's operating near the threshold.

For example, the health check used to measure search response time is configured to mark any server as `degraded` when the search response time is greater than 1 second. You can configure that the response time must be less than 500 ms before the server is made available again so that the PingDirectoryProxy server doesn't flip back and forth between `available` and `degraded`.

You can find more information about configuring health checks in [Configuring server health checks](pd_proxy_config_server_health_checks.html).

---

---
title: About load-balancing algorithms
description: Load-balancing algorithms determine which server in a set of similar servers to use to process a client request.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectoryproxy_server_administration_guide:pd_proxy_load_balancing_algorithms
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectoryproxy_server_administration_guide/pd_proxy_load_balancing_algorithms.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 25, 2024
section_ids:
  algorithm-criteria: Algorithm criteria
---

# About load-balancing algorithms

Load-balancing algorithms determine which server in a set of similar servers to use to process a client request.

The PingDirectoryProxy server provides the following load-balancing algorithms:

* Fewest operations

  Forwards request to the backend server with the fewest operations currently in progress.

* Single server

  Sends requests to the same server and doesn't attempt to fail over to another server if the target server is unavailable.

* Weighted

  Administrators explicitly assign numeric weights to individual servers or sets of servers to control how likely they are to be selected for processing requests relative to other servers.

* Health-based weighting

  Uses the health check score to assign weights to each of the servers so that a server with a higher score gets a higher percentage of the traffic than a server with a lower score. The proportion of traffic received is the difference between their health check scores.

* Failover

  Sends requests to a given server first. If that server fails, then the request sends to another specified server as specified in the ordered failover server list.

Learn more about [Configuring load balancing](pd_proxy_config_load_balancing.html).

## Algorithm criteria

The algorithm takes the following criteria into account:

* Location of the server

  Servers in the same location as the PingDirectoryProxy server are preferred over those in alternate locations.

* Health of the server

  Servers that are `available` are preferred over those that are `degraded`. In some cases, the health check score can be used to further differentiate between servers with the same health check state.

* Route requests consistency

  Requests from a single client can be consistently routed to the same PingDirectoryProxy server instance to avoid problems such as propagation delay from replication.

* Operation retries

  Retries the operation in an alternate server if the request fails or the operation times out. You can control if the retry is allowed and, if so, how many times to retry and the time out interval.

---

---
title: About locations
description: You can assign a location to the PingDirectoryProxy server and each of the backend LDAP external servers for routing requests and failover response preferences.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectoryproxy_server_administration_guide:pd_proxy_locations
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectoryproxy_server_administration_guide/pd_proxy_locations.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 25, 2024
---

# About locations

You can assign a location to the PingDirectoryProxy server and each of the backend LDAP external servers for routing requests and failover response preferences.

Locations define a group of servers with similar response time characteristics. Each location consists of a name and an ordered list of preferred failover locations. These locations can determine how to route requests so that the server forwards requests to the PingDirectoryProxy server in the same data center over those in remote locations.

For example, a deployment consists of three data centers, one in New York, one in Chicago, and one in Los Angeles. In the New York data center, applications that reside in this data center prefer communicating with directories in this data center. If none of the servers are available, it prefers to failover to the data center in Chicago rather than the data center in Los Angeles, so the New York location contains an ordered list in which the Chicago location is preferred over the Los Angeles data center for failover.

Follow these guidelines for assigning locations in the PingDirectoryProxy server:

* If you have multiple data centers, assign a separate location for each one.

* In most environments, all PingDirectoryProxy server instances should have the same configuration except for the attribute that specifies the location of the server itself.

Learn more about [Configuring locations](pd_proxy_config_locations.html).

---

---
title: About log compression
description: The server supports the ability to compress log files as they are written.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectoryproxy_server_administration_guide:pd_proxy_log_compression
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectoryproxy_server_administration_guide/pd_proxy_log_compression.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
---

# About log compression

The server supports the ability to compress log files as they are written.

This feature can significantly increase the amount of data that can be stored in a given amount of space so that log information can be kept for a longer period of time.

Because of the inherent problems with mixing compressed and uncompressed data, compression can only be enabled at the time the logger is created. Compression cannot be turned on or off when the logger is configured. Because of problems in trying to append to an existing compressed file, if the server encounters an existing log file at startup, it rotates that file and begin a new one rather than attempting to append to the previous file.

Compression is performed using the standard gzip algorithm, so compressed log files can be accessed using readily available tools. The `summarize-access-log` tool can also work directly on compressed log files rather than requiring them to be uncompressed first.

However, because it can be useful to have a small amount of uncompressed log data available for troubleshooting purposes, administrators using compressed logging might want to have a second logger defined that does not use compression and has rotation and retention policies that minimizes the amount of space consumed by those logs while still making them useful for diagnostic purposes without the need to uncompress the files before examining them.

Configure compression by setting the `compression-mechanism` property to have the value of `gzip` when creating a new logger.

---

---
title: About log signing
description: The server supports the ability to cryptographically sign a log to ensure that it has not been modified in any way.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectoryproxy_server_administration_guide:pd_proxy_log_signing
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectoryproxy_server_administration_guide/pd_proxy_log_signing.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
---

# About log signing

The server supports the ability to cryptographically sign a log to ensure that it has not been modified in any way.

For example, financial institutions require audit logs for all transactions to check for correctness. Tamper-proof files are needed to ensure that these transactions can be properly validated and ensure that they have not been modified by any third-party entity or internally by unscrupulous employees.

Use the `dsconfig` tool to enable the `sign-log` property on a log publisher to turn on cryptographic signing.

When enabling signing for a logger that already exists and was enabled without signing, the first log file is not completely verifiable because it still contains unsigned content from before signing was enabled. Only log files whose entire content was written with signing enabled are considered completely valid. For the same reason, if a log file is still open for writing, then signature validation does not indicate that the log is completely valid because the log doesn't include the necessary end signed content indicator at the end of the file.

To validate log file signatures, use the `validate-file-signature` tool provided in the `bin` directory of the server or the `bat` directory for Windows systems.

After you have enabled this property, you must disable and then re-enable the log publisher for the changes to take effect.

---

---
title: About mapping multiple source DNs to the same target DN
description: Some complications exist when defining multiple distinguished names (DN) mappings that are used for the same request processor and the same source or target DN or that have source or target DNs that are hierarchically related.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectoryproxy_server_administration_guide:pd_proxy_map_multiple_source_dns_target_dn
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectoryproxy_server_administration_guide/pd_proxy_map_multiple_source_dns_target_dn.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# About mapping multiple source DNs to the same target DN

Some complications exist when defining multiple distinguished names (DN) mappings that are used for the same request processor and the same source or target DN or that have source or target DNs that are hierarchically related.

The client request might not include enough information to disambiguate and determine the proper rule to follow.

Several solutions exist to avoid problems of disambiguation. If the client does not need to be able to see all mappings at the same time, then a new client connection policy can be created to use connection criteria that select the set of mappings applied to the client based on information such as the IP address or bind DN. Each client connection policy would have separated subtree views with separate proxying request processors that reference the appropriate transformation for that client.

Alternatively, if it is unnecessary to search under the `o=sample` base DN, then you can create separate subtree views in the same client connection policy. For example, you would create one subtree view for `ou=east,o=sample` and one for `ou=west,o=sample`. Each subtree view is then associated with its own proxying request processor, one for `ou=east` requests and one for `ou=west` requests.

---

---
title: About request processors
description: A request processor encapsulates the logic for handling an operation, ensuring that a given operation is handled appropriately.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectoryproxy_server_administration_guide:pd_proxy_request_processors
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectoryproxy_server_administration_guide/pd_proxy_request_processors.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 25, 2024
---

# About request processors

A request processor encapsulates the logic for handling an operation, ensuring that a given operation is handled appropriately.

The request processor can:

* Process the operation directly

* Forward the request to another server

* Hand off the request to another request processor

PingDirectoryProxy server request processors can be used to forward certain controls, including the batch transaction control and the LDAP join control. The batch transaction control must target a single Berkeley DB backend. For more information about the controls, see [LDAP SDK for Java documentation](https://docs.ldap.com/ldap-sdk/docs/index.html).

PingDirectoryProxy provides the following types of request processors:

* Proxying request processors

  Forwards operations received by the PingDirectoryProxy server to other LDAP external servers.

* Entry-balancing request processors

  Splits data across multiple servers. They determine which set of servers are used to process a given operation. They then hand off operations to proxying request processors so that requests can be forwarded to one of the servers in the set.

* Failover request processors

  Perform ordered failover between other types of request processors, sometimes with different behavior for different types of operations.

Learn more about [Configuring request processors](pd_proxy_config_request_processors.html).

---

---
title: About server affinity providers
description: The PingDirectoryProxy server supports the ability to forward a sequence of requests to the same external server if specific conditions are met, called server affinity.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectoryproxy_server_administration_guide:pd_proxy_server_affinity_providers
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectoryproxy_server_administration_guide/pd_proxy_server_affinity_providers.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# About server affinity providers

The PingDirectoryProxy server supports the ability to forward a sequence of requests to the same external server if specific conditions are met, called server affinity.

Use the server affinity provider to establish an affinity to a particular backend server for certain operations.

The following provider configurations and server affinity methods are available in the PingDirectoryProxy server:

* Client connection Server Affinity

  Requests from the same client connection consistently route to the same backend server.

* Client IP address Server Affinity

  All requests coming from the same client system consistently route to the same backend server.

* Bind DN Server Affinity

  All requests from the same user consistently route to the same backend server.

For information about configuring server affinity, see [Configuring server affinity](pd_proxy_config_server_affinity.html).

---

---
title: About subtree views
description: A subtree view can be used to make a portion of the directory information tree (DIT) available to a client by associating a request processor with a base distinguished name (DN).
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectoryproxy_server_administration_guide:pd_proxy_subtree_views
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectoryproxy_server_administration_guide/pd_proxy_subtree_views.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# About subtree views

A subtree view can be used to make a portion of the directory information tree (DIT) available to a client by associating a request processor with a base distinguished name (DN).

A subtree views allow you to route operations concerning one set of data to a particular set of data sources and operations concerning another set of data to another set of data sources. Multiple subtree views are involved in processing a request, such as searches that have a scope that is larger than the subtree view.

The subtree view includes using a single base DN to identify the portion of the DIT. They might have hierarchical relationships: for example, one subtree view is configured for `dc=example,dc=com` and another for `ou=People,dc=example,dc=com`.

For information about configuring a subtree view, see [Configuring subtree views](pd_proxy_config_subtree_views.html).

---

---
title: About the --restricted argument of the dsreplication command-line Tool
description: The dsreplication tool with the --restricted argument specifies a base distinguished name (DN) when multiple domains are enabled in an entry balanced environment.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectoryproxy_server_administration_guide:pd_proxy_about_restricted_arg_dsreplication_tool
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectoryproxy_server_administration_guide/pd_proxy_about_restricted_arg_dsreplication_tool.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# About the --restricted argument of the dsreplication command-line Tool

The `dsreplication` tool with the `--restricted` argument specifies a base distinguished name (DN) when multiple domains are enabled in an entry balanced environment.

When enabling replication for a server that takes part in an entry-balanced environment, the multiple domains involved are enabled at the same time. There is a global domain and a restricted domain. The restricted domain represents the entry-balancing point. Each base DN is defined in a separate local database (DB) backend. Use the `dsreplication` command-line interface (CLI) tool with the `--restricted` argument to specify which base DN is considered an entry-balancing point.

---

---
title: About the client connection policy
description: Client connection policies are based on two factors.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectoryproxy_server_administration_guide:pd_proxy_client_connection_policy
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectoryproxy_server_administration_guide/pd_proxy_client_connection_policy.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
---

# About the client connection policy

Client connection policies are based on two factors.

* Connection criteria

  The connection criteria are used in many areas within the server. They are used by the client connection policies, but they can be used in other instances when the server needs to perform matching based on connection-level properties, such as filtered logging. A single connection can match multiple connection criteria definitions.

* Evaluation order index

  If multiple client connection policies are defined in the server, then each of them must have a unique value for the `evaluation-order-index` property. The client connection policies are evaluated in order of ascending evaluation order index. If a client connection does not match the criteria for any defined client connection policy, then that connection will be terminated.

  If the connection policy matches a connection, then the connection is assigned to that policy and no further evaluation occurs. If, after evaluating all of the defined client connection policies, no match is found, the connection is terminated.

---

---
title: About the configuration tools
description: You can access and modify the server configuration in two ways.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectoryproxy_server_administration_guide:pd_proxy_config_tools
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectoryproxy_server_administration_guide/pd_proxy_config_tools.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
---

# About the configuration tools

You can access and modify the server configuration in two ways.

* Admin console

  The server provides an admin console for graphical server management and monitoring. The console functions are equivalent to the `dsconfig` tool for viewing or editing configurations.

  All configuration changes using the admin console are recorded in `logs/config-audit.log`, which also has the equivalent reversion commands if you need to undo a configuration.

* `dsconfig` Command-line tool

  The `dsconfig` tool is a text-based menu-driven interface to the underlying configuration. The tool runs the configuration using three operational modes:

  * Interactive command-line mode

  * Non-interactive command-line mode

  * Batch mode

  All configuration changes made using this tool are recorded in `logs/config-audit.log`.

|   |                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can [generate a summary of your server's configuration](../pingdirectory_server_administration_guide/pd_ds_generate_summary_config_components.html) to help you plan any modifications. |

---

---
title: About the connection pools
description: PingDirectoryProxy maintains either one or two connection pools to the backend server, depending on the type of backend server you use.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectoryproxy_server_administration_guide:pd_proxy_connection_pools
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectoryproxy_server_administration_guide/pd_proxy_connection_pools.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# About the connection pools

PingDirectoryProxy maintains either one or two connection pools to the backend server, depending on the type of backend server you use.

PingDirectoryProxy maintains either one pool for all types of operations or two separate pools for processing bind and non-bind operations from clients. When PingDirectoryProxy establishes connections, it authenticates them using the authentication mechanism defined in the configuration of the external server.

These connections are re-used for all types of operations forwarded to the backend server. You can configure the bind distinguished name (DN) and password in the PingDirectoryProxy server.

When a client sends a bind request to the PingDirectoryProxy server, the server looks at the type of bind request that was sent:

* If the bind request is a SASL bind request, authentication is processed by the PingDirectoryProxy server itself and does not forward to the backend server, however, the PingDirectoryProxy server can use information contained in the backend server as needed.

* If the bind request is a simple bind request, and the bind DN is within the scope of data supplied by the backend server, the PingDirectoryProxy server forwards the client request to the backend server so that it uses the credentials provided by the client.

Regardless of the authentication method the client uses, the PingDirectoryProxy server remembers the identity of the client after the authentication completes. For any subsequent requests sent by that client, the server uses the configured authorization method to identify the client to the backend server.

Even though the operation is forwarded over a connection that is authenticated as a user defined in the PingDirectoryProxy server configuration, the request processes through the backend server under the authority of the end client.