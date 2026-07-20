---
title: Deprecated
description: Lists functionality deprecated in PingDS releases that is likely to be removed in a future version.
component: pingds
version: release-notes
page_id: pingds::deprecation
canonical_url: https://docs.pingidentity.com/pingds/release-notes/deprecation.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-04-20T12:00:00Z
keywords: ["Compatibility", "LDAP"]
section_ids:
  deprecated-81: Since DS 8.1
  deprecated-80: Since DS 8.0
  deprecated-75: Since DS 7.5.1
  since_ds_7_5: Since DS 7.5
  deprecated-74: Since DS 7.4.2
  since_ds_7_4: Since DS 7.4
  deprecated-73: Since DS 7.3.5
  since_ds_7_3: Since DS 7.3
  deprecated-72: Since DS 7.2.5
  since_ds_7_2: Since DS 7.2
  deprecated-71: Since DS 7.1.8
  since_ds_7_1_3: Since DS 7.1.3
  since_ds_7_1: Since DS 7.1
  deprecated-70: Since DS 7.0
  since_ds_6_5: Since DS 6.5
---

# Deprecated

The functionality listed here is deprecated, and likely to be removed in a future release.

## Since DS 8.1

* Commands using keystores and truststores now indicate the path, type, and provider with separate options:

  | Deprecated option                        | Use this instead                                                           |
  | ---------------------------------------- | -------------------------------------------------------------------------- |
  | `--providerArg {argument}`               | `--keyStoreProviderArg {argument}` or `--trustStoreProviderArg {argument}` |
  | `--providerClass {class}`                | `--keyStoreProviderClass {class}` or `--trustStoreProviderClass {class}`   |
  | `--providerName {name}`                  | `--keyStoreProviderName {name}` or `--trustStoreProviderName {name}`       |
  | `--useJavaKeyStore {keyStorePath}`       | `--keyStorePath {keyStorePath} --keyStoreType JKS`                         |
  | `--useJavaTrustStore {trustStorePath}`   | `--trustStorePath {trustStorePath} --trustStoreType JKS`                   |
  | `--useJceKeyStore {keyStorePath}`        | `--keyStorePath {keyStorePath} --keyStoreType JCEKS`                       |
  | `--useJceTrustStore {trustStorePath}`    | `--trustStorePath {trustStorePath} --trustStoreType JCEKS`                 |
  | `--useJvmTrustStore`                     | `--trustStoreType JVM`                                                     |
  | `--usePkcs11KeyStore`                    | `--keyStoreType PKCS11`                                                    |
  | `--usePkcs12KeyStore {keyStorePath}`     | `--keyStorePath {keyStorePath} --keyStoreType PKCS12`                      |
  | `--usePkcs12TrustStore {trustStorePath}` | `--trustStorePath {trustStorePath} --trustStoreType PKCS12`                |

* The following environment variables names are changing:

  | Deprecated environment variable | Use this instead |
  | ------------------------------- | ---------------- |
  | `OPENDJ_JAVA_ARGS`              | `DS_JAVA_ARGS`   |
  | `OPENDJ_JAVA_BIN`               | `DS_JAVA_BIN`    |
  | `OPENDJ_JAVA_HOME`              | `DS_JAVA_HOME`   |

* The DS cloud storage plugin is deprecated.

  Mount your cloud storage as a directory in the local filesystem and back up to it. Learn more in [Cloud Storage](https://docs.pingidentity.com/pingds/8.1/maintenance-guide/backup-restore.html#cloud-storage).

* Support for creating your own setup profiles is deprecated.

  Use `dsconfig` and the other commands located with the DS server to script the configuration instead. You can use the `dsconfig --batch` or `dsconfig --batchFilePath` option to run a set of configuration changes in a single command.

* Support for Graphite is deprecated.

  Use [Prometheus](https://prometheus.io/) and the PromQL query language instead.

## Since DS 8.0

* The HTTP OAuth2 OpenAM authorization scheme is deprecated.

* The `ds-rlim-lookthrough-limit` setting is no longer deprecated.

* The following table lists deprecated metrics and their replacements:

  | Deprecated metric                     | Use this instead                       |
  | ------------------------------------- | -------------------------------------- |
  | `ds-mon-backend-degraded-index`       | `ds-mon-backend-untrusted-index`       |
  | `ds-mon-backend-degraded-index-count` | `ds-mon-backend-untrusted-index-count` |
  | `ds_backend_degraded_index_count`     | `ds_backend_untrusted_index_count`     |

## Since DS 7.5.1

* The `setup-profile --instancePath` is deprecated.

  Run the `setup-profile` command located with the server instance.

## Since DS 7.5

* The Prometheus endpoint configuration property `legacy-format` is deprecated.

  Update your applications to work with the [Prometheus text format](https://prometheus.io/docs/instrumenting/exposition_formats/#text-based-format).

* To prepare for compliance with the OpenMetrics standard, all Prometheus counter metrics end in `_total` going forward.

  The following table lists deprecated metrics with their replacements:

  | Deprecated counter                                             | Use this instead                                                     |
  | -------------------------------------------------------------- | -------------------------------------------------------------------- |
  | `ds_connection_handlers_ldap_abandoned_requests`               | `ds_connection_handlers_ldap_abandoned_requests_total`               |
  | `ds_replication_replica_replayed_internal_updates`             | `ds_replication_replica_replayed_internal_updates_total`             |
  | `ds_replication_replica_replayed_updates_conflicts_resolved`   | `ds_replication_replica_replayed_updates_conflicts_resolved_total`   |
  | `ds_replication_replica_replayed_updates_conflicts_unresolved` | `ds_replication_replica_replayed_updates_conflicts_unresolved_total` |
  | `ds_replication_replica_sent_updates`                          | `ds_replication_replica_sent_updates_total`                          |
  | `ds_replication_replica_updates_already_in_progress`           | `ds_replication_replica_updates_already_in_progress_total`           |

## Since DS 7.4.2

* The `dsrepl start-disaster-recovery` and `dsrepl end-disaster-recovery` commands are deprecated.

  For instructions on what to use, refer to the [disaster recovery](https://docs.pingidentity.com/pingds/7.4/maintenance-guide/disaster-recovery.html) documentation instead.

## Since DS 7.4

* Support for REST to LDAP is deprecated in favor of HDAP for future applications.

  REST to LDAP remains supported [as documented for DS 7.3](https://docs.pingidentity.com/pingds/7.3/rest-guide/preface.html).

  For details about HDAP, refer to [Use HDAP](https://docs.pingidentity.com/pingds/7.4/rest-guide/preface.html).

* Support for `/admin/config` is deprecated.

  Use the `dsconfig` command to change the DS server configuration.

* Support for `/metrics/api` is deprecated.

  Use Prometheus for HTTP monitoring instead. For details, refer to [HTTP-based monitoring](https://docs.pingidentity.com/pingds/7.4/monitoring-guide/http-monitoring.html).

* Support for the backwards-compatible [file-based access log publisher](https://docs.pingidentity.com/pingds/7.4/logging-guide/ldap-access.html#log-ldap-access) is deprecated.

  Use the JSON format log publishers, which new DS servers use by default since the 5.0 release.

* Support for the JMX connection handler is deprecated.

  JMX MBeans remain supported.

## Since DS 7.3.5

* The `dsrepl start-disaster-recovery` and `dsrepl end-disaster-recovery` commands are deprecated.

  For instructions on what to use, refer to the [disaster recovery](https://docs.pingidentity.com/pingds/7.3/maintenance-guide/disaster-recovery.html) documentation instead.

## Since DS 7.3

This release does not deprecate any functionality.

## Since DS 7.2.5

* The `dsrepl start-disaster-recovery` and `dsrepl end-disaster-recovery` commands are deprecated.

  For instructions on what to use, refer to the [disaster recovery](https://docs.pingidentity.com/pingds/7.2/maintenance-guide/disaster-recovery.html) documentation instead.

## Since DS 7.2

* The `ds-pwp-last-login-time` attribute, which has directory string syntax, is deprecated.

  Use the new `ds-last-login-time` attribute instead. For an example, refer to [Active accounts](https://docs.pingidentity.com/pingds/7.2/ldap-guide/search-ldap.html#extensible-match-search).

* Support for CSV, Elasticsearch, JDBC, JMS, Splunk, and Syslog access logs is deprecated.

* The DSML gateway is deprecated.

  For deployments that require HTTP access to directory data, consider HDAP as an alternative.

## Since DS 7.1.8

* The `dsrepl start-disaster-recovery` and `dsrepl end-disaster-recovery` commands are deprecated.

  For instructions on what to use, refer to the disaster recovery documentation instead.

## Since DS 7.1.3

* The following Prometheus counter metrics are deprecated:

  * `ds_connection_handlers_ldap_abandoned_requests{ldap_handler}`

  * `ds_replication_replica_replayed_internal_updates{domain_name,server_id}`

  * `ds_replication_replica_replayed_updates_conflicts_resolved`

  * `ds_replication_replica_replayed_updates_conflicts_unresolved`

  * `ds_replication_replica_sent_updates`

  * `ds_replication_replica_updates_already_in_progress{domain_name,server_id}`

  They are expected to be replaced with metrics whose names end in `_total` in a future release.

## Since DS 7.1

* The previous format for password file options is deprecated. The options remain supported until removal, but are now hidden in online help. This affects the following options:

  | Deprecated form               | Use this form                                                |
  | ----------------------------- | ------------------------------------------------------------ |
  | `--bindPasswordFile`          | `--bindPassword:file`                                        |
  | `--deploymentKeyPasswordFile` | `--deploymentIdPassword:file`                                |
  | `--keyStorePasswordFile`      | `--keyStorePassword:file``--keyStorePasswordFilePath`(1)     |
  | `--monitorUserPasswordFile`   | `--monitorUserPassword:file`                                 |
  | `--rootUserPasswordFile`      | `--rootUserPassword:file`                                    |
  | `--trustStorePasswordFile`    | `--trustStorePassword:file``--trustStorePasswordFilePath`(1) |

  (1) The `--keyStorePasswordFilePath` and `--trustStorePasswordFilePath` options apply only to the `setup`. They retain the path to the file in the configuration. The other options copy the cleartext password at setup time.

* The `dsrepl add-local-server-to-pre-7-0-topology` command `--masterKeyPairCertAlias` and `--rootCaCertAlias` options are deprecated. The command now finds the certificates by introspecting the configuration.

  The options are now hidden in online help.

## Since DS 7.0

* Support for SNMP.

  DS software provides better options for monitoring servers, including support for Prometheus, Graphite, and LDAP. For details, refer to *Monitoring*.

  DS server software also includes a sample monitoring dashboard for Prometheus and Grafana, which is described in `opendj/samples/grafana/README.md`.

* The `pwdValidatorPolicy` object class.

  For subentry password policies, use the object classes derived from `ds-pwp-validator` instead.

* Reversible password storage schemes, and the `cn=admin data` base DN and `adminData` backend used to support them. This includes the following password storage schemes:

  * `3DES`

  * `AES`

  * `Blowfish`

  * `RC4`

  The `3DES`, `Blowfish`, and `RC4` are supported for compatibility purposes only. If you must use reversible encryption, use the `AES` scheme.

* The `ds-rlim-lookthrough-limit` setting is deprecated.

## Since DS 6.5

* Regarding replication monitoring metrics, including those deprecated since 6.0:

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | In mixed topologies, a directory server version 6 or earlier connected to a replication server version 6.5 or later can't consume messages about other servers going offline. The monitoring framework reflects this as a delay on the directory server that could not consume the message.The delay is calculated correctly again once all servers in the topology are upgraded to at least version 6.5, or when the offline server comes back online and has seen a change to directory data. |

  Monitor replication delay instead of using the deprecated metrics. For details, refer to *Replication delay (LDAP)* or *Replication delay (Prometheus)*.

---

---
title: Downloads
description: Download PingDS server software, including packages for deployment as an LDAP directory server, proxy, or replication server.
component: pingds
version: release-notes
page_id: pingds::downloads
canonical_url: https://docs.pingidentity.com/pingds/release-notes/downloads.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-04-20T12:00:00Z
keywords: ["Evaluation", "Install", "LDAP"]
---

# Downloads

The [Ping Identity Download Center](https://product-downloads.pingidentity.com/) provides access to Ping Identity releases.

| Latest release              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DS-8.1.1.zip`              | Cross-platform distribution of the server software.Pure Java, high-performance server that can be configured as:- An LDAPv3 directory server with the additional capability to serve directory data to REST applications over HTTP.

- An LDAPv3 directory proxy server providing a single point of access to underlying directory servers.

- A replication server handling replication traffic with directory servers and with other replication servers, receiving and sending changes to directory data.Server distributions include command-line tools for installing, configuring, and managing servers. The tools make it possible to script all operations.By default, this file unpacks into an `opendj/` directory. |
| `DS-8.1.1.msi`              | Microsoft Windows native installer for the server software.By default, this installs files into a `C:\Program Files (x86)\PingDS Server\` directory.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `DS_8.1.1-1_all.deb`        | Server software native packages for Debian and related Linux distributions.By default, this installs files into an `/opt/opendj/` directory.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `DS-8.1.1-1.noarch.rpm`     | Server software native packages for Red Hat and related Linux distributions.By default, this installs files into an `/opt/opendj/` directory.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `DS-hdap-servlet-8.1.1.war` | Cross-platform HDAP gateway web archive.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

---

---
title: Fixes
description: Index of cumulative fix lists for PingDS major and minor versions, from 6.5.x through 8.1.x.
component: pingds
version: release-notes
page_id: pingds::fixes
canonical_url: https://docs.pingidentity.com/pingds/release-notes/fixes.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-04-20T12:00:00Z
keywords: ["LDAP", "Upgrade"]
---

# Fixes

The following pages list important fixes in DS major or minor versions.

|   |                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Fixes in a version are cumulative.For example, when an issue is fixed in DS 8.0.1, it's fixed in 8.0.2 and any later 8.0.x maintenance releases. |

* [Fixes in 8.1.x](fixes-8.1.html)

* [Fixes in 8.0.x](fixes-8.0.html)

* [Fixes in 7.5.x](fixes-7.5.html)

* [Fixes in 7.4.x](fixes-7.4.html)

* [Fixes in 7.3.x](fixes-7.3.html)

* [Fixes in 7.2.x](fixes-7.2.html)

* [Fixes in 7.1.x](fixes-7.1.html)

* [Fixes in 7.0.x](fixes-7.0.html)

* [Fixes in 6.5.x](fixes-6.5.html)

---

---
title: Fixes in 6.5.x
description: Cumulative list of important fixes in PingDS 6.5.x maintenance releases.
component: pingds
version: release-notes
page_id: pingds::fixes-6.5
canonical_url: https://docs.pingidentity.com/pingds/release-notes/fixes-6.5.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-11-03T13:32:20Z
keywords: ["LDAP", "Upgrade"]
section_ids:
  ds_6_5_6: DS 6.5.6
  ds_6_5_5: DS 6.5.5
  ds_6_5_4: DS 6.5.4
  ds_6_5_3: DS 6.5.3
  ds_6_5_2: DS 6.5.2
  ds_6_5_1: DS 6.5.1
  ds_6_5_0: DS 6.5.0
---

# Fixes in 6.5.x

This page lists the cumulative fixes in DS 6.5.x releases:

## DS 6.5.6

* OPENDJ-8698: DS should write config archive files in a crash consistent way

* OPENDJ-8845: Bad encoding of PersistentSearch's changeType of the EntryChangeNotificationResponseControl

* OPENDJ-7970: Ensure that DS is crash resilient for all runtime file changes

* OPENDJ-7761: DS sporadically hangs while reconnecting to an RS

* OPENDJ-7653: replication issue in the cloud after ldapadd

* OPENDJ-6349: "RuntimeException: Should never happen" in HttpClientConnection

## DS 6.5.5

* OPENDJ-8028: Prometheus monitoring doesn't work with Telegraf

* OPENDJ-7851: Supportextract tool: clobbers the server.out filehandle when kill -3 is used.

* OPENDJ-7818: Package based upgrade does not support instances running as non-root

* OPENDJ-7737: ConfigurationFramework#initialize0 changes the class loader without clearing the map of registered jar files

* OPENDJ-7699: Supportextract throws NoSuchElementException when the server.pid file is empty

* OPENDJ-7655: Replaying multiple MODIFYDN operations is very slow

* OPENDJ-7481: JSON logs do not contain proxy auth DN

* OPENDJ-7450: The startswith (sw) operator on indexed JSON attribute is slow

* OPENDJ-6992: Persistent search from IDM is blocking worker threads.

* OPENDJ-5927: Server stuck on a DS trying to reconnect to an RS

* CMON-109: Prometheus metrics contains more than one HELP metric line for the same metric

## DS 6.5.4

* OPENDJ-7414: AM: Persistent search with changesOnly gets cancelled by a request timeout

* OPENDJ-7286: Changelog searches can start with incorrect cursors

* OPENDJ-7232: StackOverflowError in Tomcat logs when using external DS

* OPENDJ-7176: Filters with malformed attribute descriptions cannot be parsed

* OPENDJ-7115: DS does not start when deployed with ISTIO side car container in the GCP K8s cloud

* OPENDJ-7031: VLVIndex are incorrectly rebuilt by rebuild-index

* OPENDJ-7020: Rebuild-index offline ignores rebuild-index.offline.java-args

* OPENDJ-7016: Status command outputs malformed JSON in script friendly mode

* OPENDJ-7014: Some operational attributes are not replicated when a restore --dry-run is used against an online server

* OPENDJ-6994: Strict-format-country-string does not affect the server

* OPENDJ-6970: Tamil locales cause illegal matchingRules values

* OPENDJ-6910: Supportextract --maxLogFiles gathers logs but not the latest logs

* OPENDJ-6812: Client tools fail in offline mode when Account Status Notification Handlers are used

* OPENDJ-6711: Replication status reports The provided value "5277383431" could not be parsed as an integer.

* OPENDJ-6498: Profile creation stores AM cts and config global aci's in base64 format

* OPENDJ-6377: Replication replay: issues with ReplaySynchronizer

* OPENDJ-6309: Search operation on whole tree skips nodes if there are DNs without backends in the directory information tree (DIT)

* OPENDJ-5851: ACI: getEffectiveRights with authz do not print out acl rights

* OPENDJ-5439: LeastRequestsStrategy should distribute load randomly when idle

* OPENDJ-4058: IDM Account Status notification handler doesn't look for certificates correctly

## DS 6.5.3

* OPENDJ-6930: Increase interoperability with HSMs when protecting and distributing symmetric keys

* OPENDJ-6929: Support storing ads-certificate key-pair and other instance public keys in an HSM

* OPENDJ-6892: Incorrect units for two updates metrics

* OPENDJ-6830: The supportextract tool should capture stack traces in server.out with SIGQUIT

* OPENDJ-6822: Reduce number of expensive seeks in BlockLogReader

* OPENDJ-6820: dsconfig "-w -" option doesn't prompt for password

* OPENDJ-6787: Changelog searches are extremely slow if any cursors are exhausted

* OPENDJ-6781: example-plugin fails to build on 6.5 branch

* OPENDJ-6778: Proxy server mishandles abandon requests

* OPENDJ-6733: SMTP handler sends incorrect email when account status is modified by manually updating ds-pwp-account-disabled attribute

* OPENDJ-6708: The supportextract tool fails with an error parsing json

* OPENDJ-6695: Heap slowly fills with DomainDBCursors

* OPENDJ-6675: The supportextract tool cannot collect gc files when there are dots in the path

* OPENDJ-6557: IDM Password Sync plugin induces 100% CPU in Apache Http Components when used with JDK 11

* OPENDJ-6540: The supportextract tool hangs when loggers are configured to use /dev/stdout

* OPENDJ-6527: server does not return password policy responses with only warnings

* OPENDJ-6521: setup checks admin port despite options --skipPortCheck --doNotStart

* OPENDJ-6512: Problems when work queue fills

* OPENDJ-6474: REST: some requests fails when stressing embedded http endpoint with Gatling

* OPENDJ-6464: IsMemberOfVirtualAttributeProvider does not process subordinate nested groups

* OPENDJ-6422: Make the supportextract tool compliant with JVM unified logging framework

* OPENDJ-6394: Update forgerock-commons for 6.5.3

* OPENDJ-6371: The supportextract tool generates data but returns 1 instead of 0 on Windows

* OPENDJ-6240: DS not honoring per user resource limits when processing RESTful operation requests

* OPENDJ-6163: The supportextract tool needs to gather archived-configs

* OPENDJ-5960: The supportextract tool should gather basic changelogDb information

* OPENDJ-5895: Unable to rebuild indexes when the Error Log Handler is assigned to a password policy

* OPENDJ-5600: The supportextract tool should capture stack traces with jcmd

## DS 6.5.2

* OPENDJ-6248: NPE when running supportextract without monitoring user configured

* OPENDJ-6235: Stale ds-sync-hist attribute values reappear in the entry after replication is unconfigured

* OPENDJ-6222: SMTP messages are sometimes not encoded with the correct charset

* OPENDJ-6217: NPE when running supportextract tool on upgraded instance

* OPENDJ-6196: HTTP connection handler continues to listen to 0.0.0.0 after setting listen-address

* OPENDJ-6173: cn=monitor memory pool stats do not get updated properly over time

* OPENDJ-6170: supportextract tool misses rotated or non-standard GC log files

* OPENDJ-6128: supportextract tool needs to gather Profile and Data Information

* OPENDJ-6125: supportextract tool needs to gather the rootUser and monitorUser ldif files

* OPENDJ-5972: bin/status command fails when using a french locale

## DS 6.5.1

* OPENDJ-6089: TelephoneNumber syntax in DN creates an incorrect entry DN value

* OPENDJ-6039: AM Config Store Profile doesn't have enough access in ProductionMode when upgrading AM

* OPENDJ-5979: Server does not validate sum of memory used by JE backend caches after upgrade

* OPENDJ-5977: Can not use custom base dn with cts profile because organization unit is forced

* OPENDJ-5955: Missing version fallback feature for profiles

* OPENDJ-5843: Rebuild-index failed with ConfigException on db-cache-size

* OPENDJ-5801: ldap operation fails with "49 Invalid Credentials" when bindDN of 'cn=Directory Manager' is supplied in a properties file

* OPENDJ-5794: JE db-cache-size settings conflicts with shared cache

* OPENDJ-5793: Replication on windows: ChangelogException while adding entries

* OPENDJ-5727: Add optional base DN for each profile

* OPENDJ-5726: Proxy distribution has trouble scaling writes to 3 shards

* OPENDJ-5675: JDK11: supportextract tool cannot find jstack command

* OPENDJ-5611: Change number indexing can lag behind replication under extreme load

* OPENDJ-5584: Server does not validate sum of memory used by JE backend caches in all cases

* OPENDJ-5423: Incorrectly reported missing parent entries cause import-ldif and index rebuilds to fail

## DS 6.5.0

* OPENDJ-5606: Upgrade to DS 6.0 fails if multiple filesystems are involved

* OPENDJ-5594: StackOverflowError with groupOfURLs when isMemberOf is requested

* OPENDJ-5582: LdapClientSocket connection leaked when handshake fails

* OPENDJ-5558: SDK: LdapUrl is not IPv6 clean

* OPENDJ-5553: Rest2Ldap cannot connect to TLSv1.2 servers

* OPENDJ-5496: DS fails to reconnect to an RS, disconnecting in handshake phase, after system restart

* OPENDJ-5481: ERR\_OPERATION\_NOT\_FOUND\_IN\_PENDING message used twice in different contexts

* OPENDJ-5406: Duplicate entry DNs if entry is deleted and then added during export-ldif or dsreplication initialize

* OPENDJ-5293: Proxy: Replication Service Discovery Mechanism logs WARNING

* OPENDJ-5272: "idle-time-limit" global configuration property has no effect

* OPENDJ-5210: Possible memory-leak if request received while bind in progress

* OPENDJ-5140: PersistentSearch heap usage grows

* OPENDJ-5137: Reading compressed or encrypted entries fails to close the InflaterInputStream

* OPENDJ-5115: ldappasswordmodify fails, NPE in PasswordPolicyState updatePasswordHistory

* OPENDJ-4967: Rest2ldap UndeliverableException occurs when a referenced entity cannot be fetched

* OPENDJ-4947: SASL DIGEST-MD5: bind request failed with protocol error

* OPENDJ-4881: Updates via Rest2ldap fail if record does not contain the necessary object class

* OPENDJ-4852: Backup with --backupAll misses a few backends

* OPENDJ-4625: Changelog range searches miss entries

* OPENDJ-4589: dsconfig --offline is not case-insensitive

* OPENDJ-4325: Changelog searches requesting changelogCookie are very slow

* OPENDJ-4229: status command with keystore options throws NullPointerException

* OPENDJ-3480: Updating schema backend properties while it is enabled leaves schema backend in broken state

* OPENDJ-3343: Invalid Conflict resolution on Add sequence when Parent & Child are added on different replica

* OPENDJ-3341: REST to LDAP gateway: HTTP response for API description is empty

* OPENDJ-3153: REST to LDAP gateway: changing password fails when using proxied authorization

* OPENDJ-2356: verify-index displays an inappropriate error message when run in online mode

---

---
title: Fixes in 7.0.x
description: Cumulative list of important fixes in PingDS 7.0.x maintenance releases.
component: pingds
version: release-notes
page_id: pingds::fixes-7.0
canonical_url: https://docs.pingidentity.com/pingds/release-notes/fixes-7.0.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-11-03T13:32:20Z
keywords: ["LDAP", "Upgrade"]
section_ids:
  ds_7_0_2: DS 7.0.2
  ds_7_0_1: DS 7.0.1
  ds_7_0_0: DS 7.0.0
  ds_6_5_0: DS 6.5.0
---

# Fixes in 7.0.x

This page lists the cumulative fixes in DS 7.0.x releases:

## DS 7.0.2

* OPENDJ-7810: JMX connections are always considered insecure

## DS 7.0.1

* OPENDJ-7674: Migrating encrypted changelog files during upgrade fails

* OPENDJ-7612: replication divergence on CTS in the cloud

* OPENDJ-7599: Cannot add a pre-encoded password to an entry without an existing password

* OPENDJ-7554: Windows: Secrets not retrieved from :file command-line arguments

* OPENDJ-7523: Example plugin and example pwdscheme pom.xml is missing 7.0.0 as revision

* OPENDJ-7450: The startswith (sw) operator on indexed JSON attribute is slow

* OPENDJ-7443: AM Identity Store 7.0 Setup profile missing "push2faEnabled" attribute

* OPENDJ-7436: Backup to the cloud takes too much time

* OPENDJ-5927: Server stuck on a DS trying to reconnect to an RS

## DS 7.0.0

* OPENDJ-7319: Addrate can run out of memory when --deleteMode off and --noPurge are set

* OPENDJ-7286: Changelog searches can start with incorrect cursors

* OPENDJ-7176: Filters with malformed attribute descriptions cannot be parsed

* OPENDJ-7115: DS does not start when deployed with ISTIO sidecar container in the GCP K8s cloud

* OPENDJ-7016: status command outputs malformed JSON in script friendly mode

* OPENDJ-6994: strict-format-country-string does not affect the server

* OPENDJ-6787: Changelog searches are extremely slow if any cursors are exhausted

* OPENDJ-6778: Proxy server mishandles abandon requests

* OPENDJ-6733: SMTP handler sends incorrect email when account status is modified by manually updating ds-pwp-account-disabled attribute

* OPENDJ-6711: Replication status reports The provided value "5277383431" could not be parsed as an integer.

* OPENDJ-6557: IDM Password Sync plugin induces 100% CPU in Apache Http Components when used with JDK 11

* OPENDJ-6540: The Supportextract hangs when loggers are configured to use /dev/stdout

* OPENDJ-6527: Server does not return password policy responses with only warnings

* OPENDJ-6521: setup checks admin port despite options --skipPortCheck --doNotStart

* OPENDJ-6512: Problems when work queue fills

* OPENDJ-6499: Query on rest2ldap over ssl gets stuck after few curl requests using TLSv1.3 on JDK11

* OPENDJ-6377: Replication replay: issues with ReplaySynchronizer

* OPENDJ-6349: "RuntimeException: Should never happen" in HttpClientConnection

* OPENDJ-6240: DS not honoring per user resource limits when processing RESTful operation requests

* OPENDJ-6235: Stale ds-sync-hist attribute values reappear in the entry after replication is unconfigured

* OPENDJ-6222: SMTP messages are sometimes not encoded with the correct charset

* OPENDJ-6221: Logging for CONNECT operations are not saved in Nanosecond format

* OPENDJ-6196: HTTP connection handler continues to listen to 0.0.0.0 after setting listen-address

* OPENDJ-6188: Backend returns an incorrect error type when disk space hits low threshold

* OPENDJ-6173: cn=monitor memory pool stats do not get updated properly over time

* OPENDJ-6116: Unspecified Communications Error when multiple rest2ldap endpoints share configuration elements

* OPENDJ-5675: JDK11: supportextract tool cannot find jstack command

* OPENDJ-5664: JDK 11: illegal reflective access warning during import-ldif

* OPENDJ-5661: supportextract tool help and version options are different from other tools

* OPENDJ-5660: JDK 11: illegal reflective access warning on setup (with profile)

* OPENDJ-5611: Change number indexing can lag behind replication under extreme load

* OPENDJ-5590: Proxy: server discovery fails silently when proxy base-dn differs from backend's base-dn

* OPENDJ-5584: Server does not validate sum of memory used by JE backend caches in all cases

* OPENDJ-4764: REST2LDAP gateway sasl-plain authorization doesn't handle dn: correctly

* OPENDJ-4714: SSL handshake now sends 16KB list of CA issuer DNs

* OPENDJ-3121: Setup fails to create the lib/extensions directory in the instance.loc path, if a instance.loc file is used.

* OPENDJ-2605: Debian packages should be idempotent

* OPENDJ-1169: Exception/error lost when logging ERR\_LOOP\_REPLAYING\_OPERATION

* OPENDJ-640: Text Query Against indexed telephoneNumber Attribute Very Slow

## DS 6.5.0

* OPENDJ-5606: Upgrade to DS 6.0 fails if multiple filesystems are involved

* OPENDJ-5594: StackOverflowError with groupOfURLs when isMemberOf is requested

* OPENDJ-5582: LdapClientSocket connection leaked when handshake fails

* OPENDJ-5558: SDK: LdapUrl is not IPv6 clean

* OPENDJ-5553: Rest2Ldap cannot connect to TLSv1.2 servers

* OPENDJ-5496: DS fails to reconnect to an RS, disconnecting in handshake phase, after system restart

* OPENDJ-5481: ERR\_OPERATION\_NOT\_FOUND\_IN\_PENDING message used twice in different contexts

* OPENDJ-5406: Duplicate entry DNs if entry is deleted and then added during export-ldif or dsreplication initialize

* OPENDJ-5293: Proxy: Replication Service Discovery Mechanism logs WARNING

* OPENDJ-5272: "idle-time-limit" global configuration property has no effect

* OPENDJ-5210: Possible memory-leak if request received while bind in progress

* OPENDJ-5140: PersistentSearch heap usage grows

* OPENDJ-5137: Reading compressed or encrypted entries fails to close the InflaterInputStream

* OPENDJ-5115: ldappasswordmodify fails, NPE in PasswordPolicyState updatePasswordHistory

* OPENDJ-4967: Rest2ldap UndeliverableException occurs when a referenced entity cannot be fetched

* OPENDJ-4947: SASL DIGEST-MD5: bind request failed with protocol error

* OPENDJ-4881: Updates via Rest2ldap fail if record does not contain the necessary object class

* OPENDJ-4852: Backup with --backupAll misses a few backends

* OPENDJ-4625: Changelog range searches miss entries

* OPENDJ-4589: dsconfig --offline is not case-insensitive

* OPENDJ-4325: Changelog searches requesting changelogCookie are very slow

* OPENDJ-4229: status command with keystore options throws NullPointerException

* OPENDJ-3480: Updating schema backend properties while it is enabled leaves schema backend in broken state

* OPENDJ-3343: Invalid Conflict resolution on Add sequence when Parent & Child are added on different replica

* OPENDJ-3341: REST to LDAP gateway: HTTP response for API description is empty

* OPENDJ-3153: REST to LDAP gateway: changing password fails when using proxied authorization

* OPENDJ-2356: verify-index displays an inappropriate error message when run in online mode

---

---
title: Fixes in 7.1.x
description: Cumulative list of important fixes in PingDS 7.1.x maintenance releases.
component: pingds
version: release-notes
page_id: pingds::fixes-7.1
canonical_url: https://docs.pingidentity.com/pingds/release-notes/fixes-7.1.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-11-03T13:32:20Z
keywords: ["LDAP", "Upgrade"]
section_ids:
  ds_7_1_8: DS 7.1.8
  ds_7_1_7: DS 7.1.7
  ds_7_1_6: DS 7.1.6
  ds_7_1_5: DS 7.1.5
  ds_7_1_4: DS 7.1.4
  ds_7_1_3: DS 7.1.3
  ds_7_1_2: DS 7.1.2
  ds_7_1_1: DS 7.1.1
  ds_7_1_0: DS 7.1.0
  ds_7_0_0: DS 7.0.0
  ds_6_5_0: DS 6.5.0
---

# Fixes in 7.1.x

This page lists the cumulative fixes in DS 7.1.x releases:

## DS 7.1.8

* OPENDJ-10139: Replication status "TOO\_LATE" does not mark DS as unhealthy

* OPENDJ-10131: ds-mon-receive-delay metric is not working

## DS 7.1.7

* OPENDJ-8228: Updates for an entry in a replicated sub-suffix appear also in the changelog for its parent

## DS 7.1.6

* OPENDJ-9587: ChangeNumberIndexer unable to advance even after proper shutdown of the replica

* OPENDJ-9542: References to ds-mon-requests-rejected-queue-full in the docs needs removing

* OPENDJ-9472: Upgrade does not correctly handle previously patched upgrades

* OPENDJ-8992: A replica rejoining the topology after its changelog is purged is not tested for the correct server state

* OPENDJ-8975: Modified file permissions for 99-user.ldif revert to 600 when DS is restarted

## DS 7.1.5

* OPENDJ-9419: Disaster recovery must delete all domain states from the changelog

* OPENDJ-9347: GSSAPISASLMechanismHandler incorrectly formats the login conf file

* OPENDJ-9245: DS backup to an S3 bucket on a new region fails

* OPENDJ-9204: RS ignores DS state and forwards changes DS has already seen

* OPENDJ-9020: Replicas should persist their ReplicaOfflineMsg unless they're being recovered from the replication server

* OPENDJ-8610: RS-RS session thread stuck in Session.send could prevent DS from shutdown

## DS 7.1.4

* OPENDJ-8792: Log SSL exceptions as errors instead of warnings

## DS 7.1.3

* OPENDJ-8874: Full replica purge should write CSN information right away

* OPENDJ-8845: Persistent search entry change notifications cannot be read by JNDI

* OPENDJ-8815: dsrepl status does not take into account a status of Bad generation id

* OPENDJ-8779: Improve replica and changelog logging

* OPENDJ-8727: HTTP embedded listener throws IllegalStateException: Output channel is not set

* OPENDJ-8698: DS should write config archive files in a crash consistent way

* OPENDJ-8532: Error running export-ldif offline: "DatabaseConfig.setReadOnly() must be set to false when creating a Database"

* OPENDJ-8378: dsrepl status shows deleted replication domains

* OPENDJ-8254: dsbackup restore/list slow to complete with cloud storage

## DS 7.1.2

* OPENDJ-8548: Optimize scoping of indexed searches

* OPENDJ-8500: IllegalMonitorStateException after subtree read lock timeout when adding an entry

* OPENDJ-8062: Possible inconsistent state after backup restore

* OPENDJ-7970: Ensure that DS is crash resilient for all runtime file changes

* OPENDJ-7816: dsbackup fails when destination is a symbolic link to a real directory

* OPENDJ-4935: Replication instability and divergence when using high latency disks

## DS 7.1.1

* OPENDJ-8243: Indexes could cause ldapsearch to return multiple copies of the same entry

* OPENDJ-8226: Support Extract tool ignores non-default changelogDb location when collecting domains.state file

* OPENDJ-8205: Log message lists an object's string representation instead of a file name

* OPENDJ-8115: -Djavax.net.ssl.trustStore=\<value> in OPENDJ\_JAVA\_ARGS throws NullPointerException

* OPENDJ-8090: am-identity-store:7.1 setup profile is not functional

* OPENDJ-8079: targattrsfilters expression does not work with 2 filters but permits 1 or more than 2 filters

* OPENDJ-8028: Prometheus monitoring doesn't work with Telegraf

* OPENDJ-7971: dsbackup fails when JDB file cleaned

* OPENDJ-7889: Configuring group-id against DS-only instance requires restart for the change to be reported by monitoring

* OPENDJ-7818: Package based upgrade does not support instances running as non-root

* OPENDJ-7755: DS 7.0 replication with older version, CryptoManager failed to import the symmetric key entry

* OPENDJ-7744: dsrepl initialize in a topology with DS7 and DS 5.5 fails if DS7 serverId starts with 0

## DS 7.1.0

* OPENDJ-7928: JSON normalization cannot handle nested arrays

* OPENDJ-7905: Schema replication error after upgrade

* OPENDJ-7867: NPE if dsbackup bucket name contains underscores

* OPENDJ-7851: Supportextract tool: clobbers the server.out filehandle when kill -3 is used.

* OPENDJ-7847: StaticGroup's objectclass sanity checks are unhelpful

* OPENDJ-7810: JMX connections are always considered insecure

* OPENDJ-7761: DS sporadically hangs while reconnecting to an RS

* OPENDJ-7758: DS 7.0 dsrepl add-local-server-to-pre-7-0-topology: NPE if master-key is in different keystore

* OPENDJ-7747: ldapmodify display full stack exception on LDIF errors if connection is already established

* OPENDJ-7737: ConfigurationFramework#initialize0 changes the class loader without clearing the map of registered jar files

* OPENDJ-7699: Supportextract throws NoSuchElementException when the server.pid file is empty

* OPENDJ-7689: dsrepl add-local-server-to-pre-7-0-topology does not tolerate separate keystore and truststore

* OPENDJ-7687: Global Access Control Policy regarding cn=schema is too restrictive

* OPENDJ-7674: Migrating encrypted changelog files during upgrade fails

* OPENDJ-7655: Replaying multiple MODIFYDN operations is very slow

* OPENDJ-7612: replication divergence on CTS in the cloud

* OPENDJ-7599: Cannot add a pre-encoded password to an entry without an existing password

* OPENDJ-7554: Windows: Secrets not retrieved from :file command-line arguments

* OPENDJ-7523: Example plugin and example pwdscheme pom.xml are missing correct revision

* OPENDJ-7513: Missing subSchemaSubEntry attribute from rootDSE access controls

* OPENDJ-7481: JSON logs do not contain proxy auth DN

* OPENDJ-7474: Docker sample README.md provides wrong instructions for running the container

* OPENDJ-7450: The startswith (sw) operator on indexed JSON attribute is slow

## DS 7.0.0

* OPENDJ-7319: Addrate can run out of memory when --deleteMode off and --noPurge are set

* OPENDJ-7286: Changelog searches can start with incorrect cursors

* OPENDJ-7176: Filters with malformed attribute descriptions cannot be parsed

* OPENDJ-7115: DS does not start when deployed with ISTIO sidecar container in the GCP K8s cloud

* OPENDJ-7016: status command outputs malformed JSON in script friendly mode

* OPENDJ-6994: strict-format-country-string does not affect the server

* OPENDJ-6787: Changelog searches are extremely slow if any cursors are exhausted

* OPENDJ-6778: Proxy server mishandles abandon requests

* OPENDJ-6733: SMTP handler sends incorrect email when account status is modified by manually updating ds-pwp-account-disabled attribute

* OPENDJ-6711: Replication status reports The provided value "5277383431" could not be parsed as an integer.

* OPENDJ-6557: IDM Password Sync plugin induces 100% CPU in Apache Http Components when used with JDK 11

* OPENDJ-6540: The Supportextract hangs when loggers are configured to use /dev/stdout

* OPENDJ-6527: Server does not return password policy responses with only warnings

* OPENDJ-6521: setup checks admin port despite options --skipPortCheck --doNotStart

* OPENDJ-6512: Problems when work queue fills

* OPENDJ-6499: Query on rest2ldap over ssl gets stuck after few curl requests using TLSv1.3 on JDK11

* OPENDJ-6377: Replication replay: issues with ReplaySynchronizer

* OPENDJ-6349: "RuntimeException: Should never happen" in HttpClientConnection

* OPENDJ-6240: DS not honoring per user resource limits when processing RESTful operation requests

* OPENDJ-6235: Stale ds-sync-hist attribute values reappear in the entry after replication is unconfigured

* OPENDJ-6222: SMTP messages are sometimes not encoded with the correct charset

* OPENDJ-6221: Logging for CONNECT operations are not saved in Nanosecond format

* OPENDJ-6196: HTTP connection handler continues to listen to 0.0.0.0 after setting listen-address

* OPENDJ-6188: Backend returns an incorrect error type when disk space hits low threshold

* OPENDJ-6173: cn=monitor memory pool stats do not get updated properly over time

* OPENDJ-6116: Unspecified Communications Error when multiple rest2ldap endpoints share configuration elements

* OPENDJ-5675: JDK11: supportextract tool cannot find jstack command

* OPENDJ-5664: JDK 11: illegal reflective access warning during import-ldif

* OPENDJ-5661: supportextract tool help and version options are different from other tools

* OPENDJ-5660: JDK 11: illegal reflective access warning on setup (with profile)

* OPENDJ-5611: Change number indexing can lag behind replication under extreme load

* OPENDJ-5590: Proxy: server discovery fails silently when proxy base-dn differs from backend's base-dn

* OPENDJ-5584: Server does not validate sum of memory used by JE backend caches in all cases

* OPENDJ-4764: REST2LDAP gateway sasl-plain authorization doesn't handle dn: correctly

* OPENDJ-4714: SSL handshake now sends 16KB list of CA issuer DNs

* OPENDJ-3121: Setup fails to create the lib/extensions directory in the instance.loc path, if a instance.loc file is used.

* OPENDJ-2605: Debian packages should be idempotent

* OPENDJ-1169: Exception/error lost when logging ERR\_LOOP\_REPLAYING\_OPERATION

* OPENDJ-640: Text Query Against indexed telephoneNumber Attribute Very Slow

## DS 6.5.0

* OPENDJ-5606: Upgrade to DS 6.0 fails if multiple filesystems are involved

* OPENDJ-5594: StackOverflowError with groupOfURLs when isMemberOf is requested

* OPENDJ-5582: LdapClientSocket connection leaked when handshake fails

* OPENDJ-5558: SDK: LdapUrl is not IPv6 clean

* OPENDJ-5553: Rest2Ldap cannot connect to TLSv1.2 servers

* OPENDJ-5496: DS fails to reconnect to an RS, disconnecting in handshake phase, after system restart

* OPENDJ-5481: ERR\_OPERATION\_NOT\_FOUND\_IN\_PENDING message used twice in different contexts

* OPENDJ-5406: Duplicate entry DNs if entry is deleted and then added during export-ldif or dsreplication initialize

* OPENDJ-5293: Proxy: Replication Service Discovery Mechanism logs WARNING

* OPENDJ-5272: "idle-time-limit" global configuration property has no effect

* OPENDJ-5210: Possible memory-leak if request received while bind in progress

* OPENDJ-5140: PersistentSearch heap usage grows

* OPENDJ-5137: Reading compressed or encrypted entries fails to close the InflaterInputStream

* OPENDJ-5115: ldappasswordmodify fails, NPE in PasswordPolicyState updatePasswordHistory

* OPENDJ-4967: Rest2ldap UndeliverableException occurs when a referenced entity cannot be fetched

* OPENDJ-4947: SASL DIGEST-MD5: bind request failed with protocol error

* OPENDJ-4881: Updates via Rest2ldap fail if record does not contain the necessary object class

* OPENDJ-4852: Backup with --backupAll misses a few backends

* OPENDJ-4625: Changelog range searches miss entries

* OPENDJ-4589: dsconfig --offline is not case-insensitive

* OPENDJ-4325: Changelog searches requesting changelogCookie are very slow

* OPENDJ-4229: status command with keystore options throws NullPointerException

* OPENDJ-3480: Updating schema backend properties while it is enabled leaves schema backend in broken state

* OPENDJ-3343: Invalid Conflict resolution on Add sequence when Parent & Child are added on different replica

* OPENDJ-3341: REST to LDAP gateway: HTTP response for API description is empty

* OPENDJ-3153: REST to LDAP gateway: changing password fails when using proxied authorization

* OPENDJ-2356: verify-index displays an inappropriate error message when run in online mode

---

---
title: Fixes in 7.2.x
description: Cumulative list of important fixes in PingDS 7.2.x maintenance releases.
component: pingds
version: release-notes
page_id: pingds::fixes-7.2
canonical_url: https://docs.pingidentity.com/pingds/release-notes/fixes-7.2.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-11-03T13:32:20Z
keywords: ["LDAP", "Upgrade"]
section_ids:
  ds_7_2_5: DS 7.2.5
  ds_7_2_4: DS 7.2.4
  ds_7_2_3: DS 7.2.3
  ds_7_2_2: DS 7.2.2
  ds_7_2_1: DS 7.2.1
  ds_7_2_0: DS 7.2.0
  ds_7_1_0: DS 7.1.0
  ds_7_0_0: DS 7.0.0
  ds_6_5_0: DS 6.5.0
---

# Fixes in 7.2.x

This page lists the cumulative fixes in DS 7.2.x releases:

## DS 7.2.5

* OPENDJ-10139: Replication status "TOO\_LATE" does not mark DS as unhealthy

* OPENDJ-10131: ds-mon-receive-delay metric is not working

* OPENDJ-10032: Inconsistent password storage scheme rehash policies can create multiple userPassword values

* OPENDJ-5041: Set resource limits according to proxyAs user instead of the bindDN

## DS 7.2.4

* OPENDJ-9999: DS uses encrypt/decrypt for key wrapping instead of wrap/unwrap

* OPENDJ-8796: Virtual attribute providers ignore critical controls, such as VLV, paging, and sorting

## DS 7.2.3

* OPENDJ-9828: Deadlock in big index

* OPENDJ-9587: ChangeNumberIndexer unable to advance even after proper shutdown of the replica

* OPENDJ-9472: Upgrade does not correctly handle previously patched upgrades

* OPENDJ-9419: Disaster recovery must delete all domain states from the changelog

* OPENDJ-9200: Backup process logs incorrect number of jdb files

* OPENDJ-9158: AM User/CTS affinity failover doesn't happen when DS's disk volume is detached

* OPENDJ-8975: Modified file permissions for 99-user.ldif revert to 600 when DS is restarted

* OPENDJ-7941: Client connections to proxy time out after 10 seconds regardless of activity

## DS 7.2.2

* OPENDJ-9358: ACI: (userdn = "ldap\:///anyone" and not userdn = "ldap\:///all") captures authenticated users and should not

* OPENDJ-9347: GSSAPISASLMechanismHandler incorrectly formats the login conf file

* OPENDJ-9315: Virtual static group does not contain all members of a target dynamic group

* OPENDJ-9295: Search involving BigIndex throws NoSuchElementException

* OPENDJ-9272: Change number indexing state is logged too often

* OPENDJ-9245: DS backup to an S3 bucket on a new region fails

* OPENDJ-9228: DS intermittently fails to stop due to TaskScheduler.writeLockEntry()

* OPENDJ-9042: All worker threads blocked waiting for abandon operations to complete

## DS 7.2.1

* OPENDJ-9204: RS ignores DS state and forwards changes that DS has already seen

* OPENDJ-9183: Replicated request controls serialized in LDIF using V1 encoding

* OPENDJ-9182: NPE in changelogstat on encountering a modify DN request

* OPENDJ-9102: Log rotation stops once the File Count Retention Policy count is met

* OPENDJ-9042: All worker threads blocked waiting for abandon operations to complete

* OPENDJ-9041: Undeliverable unexpected exception while performing an abandon operation during server shutdown

* OPENDJ-9033: DS refuses to start and throws a NullPointerException when a subordinate-base-dn is used.

* OPENDJ-9032: The dsrepl --script-friendly was never implemented and shouldn't appear in the tool

* OPENDJ-9020: Replicas should persist their ReplicaOfflineMsg unless they're being recovered from the replication server

* OPENDJ-9007: LoadBalancer availability check fails if the current bind user state is "bad"

* OPENDJ-9002: Changelogstat outputs verbose CSNs for offline messages, but not other messages

* OPENDJ-8992: Replica rejoining the topology after its changelog is purged is not tested for correct server state

* OPENDJ-8917: ReplicationBroker.java swallowed important debugging info

* OPENDJ-8831: Log when and why the ChangeNumberIndexer cannot move forward

* OPENDJ-8815: dsrepl status does not take into account a status of Bad generation id

* OPENDJ-8808: Potential deadlock between overlapping rename operations

* OPENDJ-8779: Improve replica and changelog logging

* OPENDJ-8378: dsrepl status shows deleted replication domains

* OPENDJ-7688: Spurious DS disconnections because of missing heartbeat

* OPENDJ-7640: Supportextract doesn't collect all security store when several keystores have the same basename

* OPENDJ-7516: External cn=changelog is not updated while replication initialization is in progress

## DS 7.2.0

* OPENDJ-8874: Full replica purge should write CSN information right away

* OPENDJ-8829: Error messages incorrectly mentions cn=System,cn=monitor

* OPENDJ-8805: dsconfig exits when setting the "bootstrap-replication-server" property with a \<null> value in the "Replication Service Discovery Mechanism".

* OPENDJ-8792: SDK: Log SSL exceptions as errors instead of warnings

* OPENDJ-8778: Setup option --trustStorePassword:file behaves differently than --trustStorePasswordFile

* OPENDJ-8727: HTTP embedded listener throws IllegalStateException: Output channel is not set

* OPENDJ-8698: DS should write config archive files in a crash consistent way

* OPENDJ-8610: RS-RS session thread stuck in Session.send could prevent DS from shutdown

* OPENDJ-8548: Optimize scoping of indexed searches

* OPENDJ-8532: Error running export-ldif offline: "DatabaseConfig.setReadOnly() must be set to false when creating a Database"

* OPENDJ-8500: IllegalMonitorStateException after subtree read lock timeout when adding an entry

* OPENDJ-8473: Upgrade does not migrate ds-cfg-je-property values

* OPENDJ-8383: dsrepl status fails when certificates accepted interactively

* OPENDJ-8280: DS will not start when using a non US Locale after changing config

* OPENDJ-8254: dsbackup restore/list slow to complete with cloud storage

* OPENDJ-8243: Indexes could cause ldapsearch to return multiple copies of the same entry

* OPENDJ-8227: Deadlock between Changelog DB purger and Thread for RS session

* OPENDJ-8226: Support Extract tool ignores non-default changelogDb location when collecting domains.state file

* OPENDJ-8205: Log message lists an object's string representation instead of a file name

* OPENDJ-8137: LDIF backend silently rejects entries that fail schema validation

* OPENDJ-8115: -Djavax.net.ssl.trustStore=\<value> in OPENDJ\_JAVA\_ARGS throws NullPointerException

* OPENDJ-8090: am-identity-store:7.1 setup profile is not functional

* OPENDJ-8079: targattrsfilters expression does not work with 2 filters but permits 1 or more than 2 filters

* OPENDJ-8062: Possible inconsistent state after backup restore

* OPENDJ-8046: Changelog files are not closed after searching cn=changelog

* OPENDJ-8028: Prometheus monitoring doesn't work with Telegraf

* OPENDJ-8024: Prevent configuration of VLV indexes with scope base-object

* OPENDJ-8008: OutOfMemoryException in subtree delete

* OPENDJ-7991: makeldif: "invalid number of arguments" using DateTime tag with colons

* OPENDJ-7971: dsbackup fails when JDB file cleaned

* OPENDJ-7970: Ensure that DS is crash resilient for all runtime file changes

* OPENDJ-7889: Configuring group-id against DS-only instance requires restart for the change to be reported by monitoring

* OPENDJ-7818: Package based upgrade does not support instances running as non-root

* OPENDJ-7816: dsbackup fails when destination is a symbolic link to a real directory

* OPENDJ-7755: DS 7.0 replication with older version, CryptoManager failed to import the symmetric key entry

* OPENDJ-7744: dsrepl initialize in a topology with DS7 and DS 5.5 fails if DS7 serverId starts with 0

* OPENDJ-7596: dsbackup has global connection options that do not work with some subcommands

* OPENDJ-4935: Replication instability and divergence when using high latency disks

## DS 7.1.0

* OPENDJ-7928: JSON normalization cannot handle nested arrays

* OPENDJ-7905: Schema replication error after upgrade

* OPENDJ-7867: NPE if dsbackup bucket name contains underscores

* OPENDJ-7851: Supportextract tool: clobbers the server.out filehandle when kill -3 is used.

* OPENDJ-7847: StaticGroup's objectclass sanity checks are unhelpful

* OPENDJ-7810: JMX connections are always considered insecure

* OPENDJ-7761: DS sporadically hangs while reconnecting to an RS

* OPENDJ-7758: DS 7.0 dsrepl add-local-server-to-pre-7-0-topology: NPE if master-key is in different keystore

* OPENDJ-7747: ldapmodify display full stack exception on LDIF errors if connection is already established

* OPENDJ-7737: ConfigurationFramework#initialize0 changes the class loader without clearing the map of registered jar files

* OPENDJ-7699: Supportextract throws NoSuchElementException when the server.pid file is empty

* OPENDJ-7689: dsrepl add-local-server-to-pre-7-0-topology does not tolerate separate keystore and truststore

* OPENDJ-7687: Global Access Control Policy regarding cn=schema is too restrictive

* OPENDJ-7674: Migrating encrypted changelog files during upgrade fails

* OPENDJ-7655: Replaying multiple MODIFYDN operations is very slow

* OPENDJ-7612: replication divergence on CTS in the cloud

* OPENDJ-7599: Cannot add a pre-encoded password to an entry without an existing password

* OPENDJ-7554: Windows: Secrets not retrieved from :file command-line arguments

* OPENDJ-7523: Example plugin and example pwdscheme pom.xml are missing correct revision

* OPENDJ-7513: Missing subSchemaSubEntry attribute from rootDSE access controls

* OPENDJ-7481: JSON logs do not contain proxy auth DN

* OPENDJ-7474: Docker sample README.md provides wrong instructions for running the container

* OPENDJ-7450: The startswith (sw) operator on indexed JSON attribute is slow

## DS 7.0.0

* OPENDJ-7319: Addrate can run out of memory when --deleteMode off and --noPurge are set

* OPENDJ-7286: Changelog searches can start with incorrect cursors

* OPENDJ-7176: Filters with malformed attribute descriptions cannot be parsed

* OPENDJ-7115: DS does not start when deployed with ISTIO sidecar container in the GCP K8s cloud

* OPENDJ-7016: status command outputs malformed JSON in script friendly mode

* OPENDJ-6994: strict-format-country-string does not affect the server

* OPENDJ-6787: Changelog searches are extremely slow if any cursors are exhausted

* OPENDJ-6778: Proxy server mishandles abandon requests

* OPENDJ-6733: SMTP handler sends incorrect email when account status is modified by manually updating ds-pwp-account-disabled attribute

* OPENDJ-6711: Replication status reports The provided value "5277383431" could not be parsed as an integer.

* OPENDJ-6557: IDM Password Sync plugin induces 100% CPU in Apache Http Components when used with JDK 11

* OPENDJ-6540: The Supportextract hangs when loggers are configured to use /dev/stdout

* OPENDJ-6527: Server does not return password policy responses with only warnings

* OPENDJ-6521: setup checks admin port despite options --skipPortCheck --doNotStart

* OPENDJ-6512: Problems when work queue fills

* OPENDJ-6499: Query on rest2ldap over ssl gets stuck after few curl requests using TLSv1.3 on JDK11

* OPENDJ-6377: Replication replay: issues with ReplaySynchronizer

* OPENDJ-6349: "RuntimeException: Should never happen" in HttpClientConnection

* OPENDJ-6240: DS not honoring per user resource limits when processing RESTful operation requests

* OPENDJ-6235: Stale ds-sync-hist attribute values reappear in the entry after replication is unconfigured

* OPENDJ-6222: SMTP messages are sometimes not encoded with the correct charset

* OPENDJ-6221: Logging for CONNECT operations are not saved in Nanosecond format

* OPENDJ-6196: HTTP connection handler continues to listen to 0.0.0.0 after setting listen-address

* OPENDJ-6188: Backend returns an incorrect error type when disk space hits low threshold

* OPENDJ-6173: cn=monitor memory pool stats do not get updated properly over time

* OPENDJ-6116: Unspecified Communications Error when multiple rest2ldap endpoints share configuration elements

* OPENDJ-5675: JDK11: supportextract tool cannot find jstack command

* OPENDJ-5664: JDK 11: illegal reflective access warning during import-ldif

* OPENDJ-5661: supportextract tool help and version options are different from other tools

* OPENDJ-5660: JDK 11: illegal reflective access warning on setup (with profile)

* OPENDJ-5611: Change number indexing can lag behind replication under extreme load

* OPENDJ-5590: Proxy: server discovery fails silently when proxy base-dn differs from backend's base-dn

* OPENDJ-5584: Server does not validate sum of memory used by JE backend caches in all cases

* OPENDJ-4764: REST2LDAP gateway sasl-plain authorization doesn't handle dn: correctly

* OPENDJ-4714: SSL handshake now sends 16KB list of CA issuer DNs

* OPENDJ-3121: Setup fails to create the lib/extensions directory in the instance.loc path, if a instance.loc file is used.

* OPENDJ-2605: Debian packages should be idempotent

* OPENDJ-1169: Exception/error lost when logging ERR\_LOOP\_REPLAYING\_OPERATION

* OPENDJ-640: Text Query Against indexed telephoneNumber Attribute Very Slow

## DS 6.5.0

* OPENDJ-5606: Upgrade to DS 6.0 fails if multiple filesystems are involved

* OPENDJ-5594: StackOverflowError with groupOfURLs when isMemberOf is requested

* OPENDJ-5582: LdapClientSocket connection leaked when handshake fails

* OPENDJ-5558: SDK: LdapUrl is not IPv6 clean

* OPENDJ-5553: Rest2Ldap cannot connect to TLSv1.2 servers

* OPENDJ-5496: DS fails to reconnect to an RS, disconnecting in handshake phase, after system restart

* OPENDJ-5481: ERR\_OPERATION\_NOT\_FOUND\_IN\_PENDING message used twice in different contexts

* OPENDJ-5406: Duplicate entry DNs if entry is deleted and then added during export-ldif or dsreplication initialize

* OPENDJ-5293: Proxy: Replication Service Discovery Mechanism logs WARNING

* OPENDJ-5272: "idle-time-limit" global configuration property has no effect

* OPENDJ-5210: Possible memory-leak if request received while bind in progress

* OPENDJ-5140: PersistentSearch heap usage grows

* OPENDJ-5137: Reading compressed or encrypted entries fails to close the InflaterInputStream

* OPENDJ-5115: ldappasswordmodify fails, NPE in PasswordPolicyState updatePasswordHistory

* OPENDJ-4967: Rest2ldap UndeliverableException occurs when a referenced entity cannot be fetched

* OPENDJ-4947: SASL DIGEST-MD5: bind request failed with protocol error

* OPENDJ-4881: Updates via Rest2ldap fail if record does not contain the necessary object class

* OPENDJ-4852: Backup with --backupAll misses a few backends

* OPENDJ-4625: Changelog range searches miss entries

* OPENDJ-4589: dsconfig --offline is not case-insensitive

* OPENDJ-4325: Changelog searches requesting changelogCookie are very slow

* OPENDJ-4229: status command with keystore options throws NullPointerException

* OPENDJ-3480: Updating schema backend properties while it is enabled leaves schema backend in broken state

* OPENDJ-3343: Invalid Conflict resolution on Add sequence when Parent & Child are added on different replica

* OPENDJ-3341: REST to LDAP gateway: HTTP response for API description is empty

* OPENDJ-3153: REST to LDAP gateway: changing password fails when using proxied authorization

* OPENDJ-2356: verify-index displays an inappropriate error message when run in online mode

---

---
title: Fixes in 7.3.x
description: Cumulative list of important fixes in PingDS 7.3.x maintenance releases.
component: pingds
version: release-notes
page_id: pingds::fixes-7.3
canonical_url: https://docs.pingidentity.com/pingds/release-notes/fixes-7.3.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-11-03T13:32:20Z
keywords: ["LDAP", "Upgrade"]
section_ids:
  ds_7_3_6: DS 7.3.6
  ds_7_3_5: DS 7.3.5
  ds_7_3_4: DS 7.3.4
  ds_7_3_3: DS 7.3.3
  ds_7_3_2: DS 7.3.2
  ds_7_3_1: DS 7.3.1
  ds_7_3_0: DS 7.3.0
  ds_7_2_0: DS 7.2.0
  ds_7_1_0: DS 7.1.0
  ds_7_0_0: DS 7.0.0
  ds_6_5_0: DS 6.5.0
---

# Fixes in 7.3.x

This page lists the cumulative fixes in DS 7.3.x releases:

## DS 7.3.6

* OPENDJ-10557: LDAP PDUs triggering a changelog write bigger than 16MiB may render the changelog files unreadable

* OPENDJ-10082: Upgrade fails in Windows environment

* OPENDJ-10032: Inconsistent password storage scheme rehash policies can create multiple userPassword values

## DS 7.3.5

* OPENDJ-10139: Replication status "TOO\_LATE" does not mark DS as unhealthy

* OPENDJ-10131: ds-mon-receive-delay metric is not working

* OPENDJ-10078: Unable to use dsrepl initialize for cn=schema when 99-user.ldif only contains ds-sync-state entries

* OPENDJ-5041: Set resource limits according to proxyAs user instead of the bindDN

## DS 7.3.4

* OPENDJ-9999: DS uses encrypt/decrypt for key wrapping instead of wrap/unwrap

* OPENDJ-9917: VirtualListView limits returned entries when used with an attr#USERDN ACI

* OPENDJ-8796: Virtual attribute providers ignore critical controls, such as VLV, paging, and sorting

## DS 7.3.3

* OPENDJ-9828: Deadlock in big index

* OPENDJ-9798: Recreated indexes are considered trusted when empty

* OPENDJ-9790: Cannot create GeneralizedTimes with large fractional values

* OPENDJ-9773: Slow startup when using multiple backends with static groups

* OPENDJ-9272: Change number indexing state is logged too often

* OPENDJ-9158: AM User/CTS affinity failover doesn't happen when DS's disk volume is detached

* OPENDJ-6791: RS reconnect delay is too aggressive

## DS 7.3.2

* OPENDJ-9587: ChangeNumberIndexer unable to advance even after proper shutdown of the replica

* OPENDJ-9472: Upgrade does not correctly handle previously patched upgrades

## DS 7.3.1

* OPENDJ-9550: Problem with entryUUIDs and operational attributes of static groups

* OPENDJ-9473: The bindPasswordFile (bindPassword:file) option cannot be used with a tools.properties file

* OPENDJ-9358: ACI: (userdn = "ldap\:///anyone" and not userdn = "ldap\:///all") captures authenticated users and should not

## DS 7.3.0

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | An issue was discovered in the 7.3.0 release that has the potential to corrupt *static groups*. To ensure data integrity, upgrade to 7.3.1 or later. This issue affects the stability and reliability of static groups only. Continuing to use version 7.3.0 may lead to data corruption and other unintended consequences.DS version 7.3.1 and later include the necessary fixes; however if you deployed DS 7.3.0 with static groups, you must contact [support](https://www.pingidentity.com/en/support/support-center.html) for assistance with resolving the data corruption. |

* OPENDJ-9300: DS 7.3 upgrade requires a full index rebuild

* OPENDJ-9295: Search involving BigIndex throws NoSuchElementException

* OPENDJ-9272: Change number indexing state is logged too often

* OPENDJ-9250: The max-allowed-client-connections limit should not apply to the admin connector

* OPENDJ-9245: DS backup to an S3 bucket on a new region fails

* OPENDJ-9213: The dsconfig list-replication-domains output contains redundant columns

* OPENDJ-9204: RS ignores DS state and forwards changes DS has already seen

* OPENDJ-9200: Backup process logs incorrect number of jdb files

* OPENDJ-9183: Replicated request controls serialized in LDIF using V1 encoding

* OPENDJ-9182: NPE in changelogstat on encountering a modify DN request

* OPENDJ-9167: Reading isMemberOf after adding, deleting, or renaming a static group can block for a long time when there are many static groups

* OPENDJ-9102: Log rotation stops once the File Count Retention Policy count is met

* OPENDJ-9042: All worker threads blocked waiting for abandon operations to complete

* OPENDJ-9041: Undeliverable unexpected exception while performing an abandon operation during server shutdown

* OPENDJ-9033: DS refuses to start and throws an NPE when a subordinate-base-dn is used

* OPENDJ-9032: The dsrepl --script-friendly option was never implemented and should not appear in the tool

* OPENDJ-9020: Replicas should persist their ReplicaOfflineMsg unless they're being recovered from the replication server

* OPENDJ-9007: LoadBalancer availability check fails if the current bind user state is "bad"

* OPENDJ-9002: Changelogstat outputs verbose CSNs for offline messages, but not other messages

* OPENDJ-9000: Missing RS - RS heartbeats are not detected

* OPENDJ-8992: A replica rejoining the topology after its changelog is purged is not tested for the correct server state

* OPENDJ-8975: Modified file permissions for 99-user.ldif revert to 600 when DS is restarted

* OPENDJ-8917: ReplicationBroker.java swallowed important debugging info

* OPENDJ-8831: Log when and why the ChangeNumberIndexer cannot move forward

* OPENDJ-8815: dsrepl status does not take bad data status into account

* OPENDJ-8808: Potential deadlock between overlapping rename operations

* OPENDJ-8779: Improve replica and changelog logging

* OPENDJ-8378: dsrepl status shows deleted replication domains

* OPENDJ-8233: RS connection error reason is not logged when hostname is not resolvable

* OPENDJ-7942: The server ignores critical VLV request controls when falling back to an unindexed search

* OPENDJ-7941: Client connections to proxy are timed out after 10 seconds regardless of activity

* OPENDJ-7925: Searchrate does not retrieve data when used simultaneously with modrate on groups

* OPENDJ-7688: Spurious DS disconnections because of missing heartbeat

* OPENDJ-7640: Supportextract does not collect all security stores when several keystores have the same basename

* OPENDJ-7516: External cn=changelog is not updated while replication initialization is in progress

* OPENDJ-3409: Retention and rotation policies do not work with CAUD handlers

* OPENDJ-3057: Replication Server starts listener although ChangeLog DB is unusable

## DS 7.2.0

* OPENDJ-8874: Full replica purge should write CSN information right away

* OPENDJ-8829: Error messages incorrectly mentions cn=System,cn=monitor

* OPENDJ-8805: dsconfig exits when setting the "bootstrap-replication-server" property with a \<null> value in the "Replication Service Discovery Mechanism".

* OPENDJ-8792: SDK: Log SSL exceptions as errors instead of warnings

* OPENDJ-8778: Setup option --trustStorePassword:file behaves differently than --trustStorePasswordFile

* OPENDJ-8727: HTTP embedded listener throws IllegalStateException: Output channel is not set

* OPENDJ-8698: DS should write config archive files in a crash consistent way

* OPENDJ-8610: RS-RS session thread stuck in Session.send could prevent DS from shutdown

* OPENDJ-8548: Optimize scoping of indexed searches

* OPENDJ-8532: Error running export-ldif offline: "DatabaseConfig.setReadOnly() must be set to false when creating a Database"

* OPENDJ-8500: IllegalMonitorStateException after subtree read lock timeout when adding an entry

* OPENDJ-8473: Upgrade does not migrate ds-cfg-je-property values

* OPENDJ-8383: dsrepl status fails when certificates accepted interactively

* OPENDJ-8280: DS will not start when using a non US Locale after changing config

* OPENDJ-8254: dsbackup restore/list slow to complete with cloud storage

* OPENDJ-8243: Indexes could cause ldapsearch to return multiple copies of the same entry

* OPENDJ-8227: Deadlock between Changelog DB purger and Thread for RS session

* OPENDJ-8226: Support Extract tool ignores non-default changelogDb location when collecting domains.state file

* OPENDJ-8205: Log message lists an object's string representation instead of a file name

* OPENDJ-8137: LDIF backend silently rejects entries that fail schema validation

* OPENDJ-8115: -Djavax.net.ssl.trustStore=\<value> in OPENDJ\_JAVA\_ARGS throws NullPointerException

* OPENDJ-8090: am-identity-store:7.1 setup profile is not functional

* OPENDJ-8079: targattrsfilters expression does not work with 2 filters but permits 1 or more than 2 filters

* OPENDJ-8062: Possible inconsistent state after backup restore

* OPENDJ-8046: Changelog files are not closed after searching cn=changelog

* OPENDJ-8028: Prometheus monitoring doesn't work with Telegraf

* OPENDJ-8024: Prevent configuration of VLV indexes with scope base-object

* OPENDJ-8008: OutOfMemoryException in subtree delete

* OPENDJ-7991: makeldif: "invalid number of arguments" using DateTime tag with colons

* OPENDJ-7971: dsbackup fails when JDB file cleaned

* OPENDJ-7970: Ensure that DS is crash resilient for all runtime file changes

* OPENDJ-7889: Configuring group-id against DS-only instance requires restart for the change to be reported by monitoring

* OPENDJ-7818: Package based upgrade does not support instances running as non-root

* OPENDJ-7816: dsbackup fails when destination is a symbolic link to a real directory

* OPENDJ-7755: DS 7.0 replication with older version, CryptoManager failed to import the symmetric key entry

* OPENDJ-7744: dsrepl initialize in a topology with DS7 and DS 5.5 fails if DS7 serverId starts with 0

* OPENDJ-7596: dsbackup has global connection options that do not work with some subcommands

* OPENDJ-4935: Replication instability and divergence when using high latency disks

## DS 7.1.0

* OPENDJ-7928: JSON normalization cannot handle nested arrays

* OPENDJ-7905: Schema replication error after upgrade

* OPENDJ-7867: NPE if dsbackup bucket name contains underscores

* OPENDJ-7851: Supportextract tool: clobbers the server.out filehandle when kill -3 is used.

* OPENDJ-7847: StaticGroup's objectclass sanity checks are unhelpful

* OPENDJ-7810: JMX connections are always considered insecure

* OPENDJ-7761: DS sporadically hangs while reconnecting to an RS

* OPENDJ-7758: DS 7.0 dsrepl add-local-server-to-pre-7-0-topology: NPE if master-key is in different keystore

* OPENDJ-7747: ldapmodify display full stack exception on LDIF errors if connection is already established

* OPENDJ-7737: ConfigurationFramework#initialize0 changes the class loader without clearing the map of registered jar files

* OPENDJ-7699: Supportextract throws NoSuchElementException when the server.pid file is empty

* OPENDJ-7689: dsrepl add-local-server-to-pre-7-0-topology does not tolerate separate keystore and truststore

* OPENDJ-7687: Global Access Control Policy regarding cn=schema is too restrictive

* OPENDJ-7674: Migrating encrypted changelog files during upgrade fails

* OPENDJ-7655: Replaying multiple MODIFYDN operations is very slow

* OPENDJ-7612: replication divergence on CTS in the cloud

* OPENDJ-7599: Cannot add a pre-encoded password to an entry without an existing password

* OPENDJ-7554: Windows: Secrets not retrieved from :file command-line arguments

* OPENDJ-7523: Example plugin and example pwdscheme pom.xml are missing correct revision

* OPENDJ-7513: Missing subSchemaSubEntry attribute from rootDSE access controls

* OPENDJ-7481: JSON logs do not contain proxy auth DN

* OPENDJ-7474: Docker sample README.md provides wrong instructions for running the container

* OPENDJ-7450: The startswith (sw) operator on indexed JSON attribute is slow

## DS 7.0.0

* OPENDJ-7319: Addrate can run out of memory when --deleteMode off and --noPurge are set

* OPENDJ-7286: Changelog searches can start with incorrect cursors

* OPENDJ-7176: Filters with malformed attribute descriptions cannot be parsed

* OPENDJ-7115: DS does not start when deployed with ISTIO sidecar container in the GCP K8s cloud

* OPENDJ-7016: status command outputs malformed JSON in script friendly mode

* OPENDJ-6994: strict-format-country-string does not affect the server

* OPENDJ-6787: Changelog searches are extremely slow if any cursors are exhausted

* OPENDJ-6778: Proxy server mishandles abandon requests

* OPENDJ-6733: SMTP handler sends incorrect email when account status is modified by manually updating ds-pwp-account-disabled attribute

* OPENDJ-6711: Replication status reports The provided value "5277383431" could not be parsed as an integer.

* OPENDJ-6557: IDM Password Sync plugin induces 100% CPU in Apache Http Components when used with JDK 11

* OPENDJ-6540: The Supportextract hangs when loggers are configured to use /dev/stdout

* OPENDJ-6527: Server does not return password policy responses with only warnings

* OPENDJ-6521: setup checks admin port despite options --skipPortCheck --doNotStart

* OPENDJ-6512: Problems when work queue fills

* OPENDJ-6499: Query on rest2ldap over ssl gets stuck after few curl requests using TLSv1.3 on JDK11

* OPENDJ-6377: Replication replay: issues with ReplaySynchronizer

* OPENDJ-6349: "RuntimeException: Should never happen" in HttpClientConnection

* OPENDJ-6240: DS not honoring per user resource limits when processing RESTful operation requests

* OPENDJ-6235: Stale ds-sync-hist attribute values reappear in the entry after replication is unconfigured

* OPENDJ-6222: SMTP messages are sometimes not encoded with the correct charset

* OPENDJ-6221: Logging for CONNECT operations are not saved in Nanosecond format

* OPENDJ-6196: HTTP connection handler continues to listen to 0.0.0.0 after setting listen-address

* OPENDJ-6188: Backend returns an incorrect error type when disk space hits low threshold

* OPENDJ-6173: cn=monitor memory pool stats do not get updated properly over time

* OPENDJ-6116: Unspecified Communications Error when multiple rest2ldap endpoints share configuration elements

* OPENDJ-5675: JDK11: supportextract tool cannot find jstack command

* OPENDJ-5664: JDK 11: illegal reflective access warning during import-ldif

* OPENDJ-5661: supportextract tool help and version options are different from other tools

* OPENDJ-5660: JDK 11: illegal reflective access warning on setup (with profile)

* OPENDJ-5611: Change number indexing can lag behind replication under extreme load

* OPENDJ-5590: Proxy: server discovery fails silently when proxy base-dn differs from backend's base-dn

* OPENDJ-5584: Server does not validate sum of memory used by JE backend caches in all cases

* OPENDJ-4764: REST2LDAP gateway sasl-plain authorization doesn't handle dn: correctly

* OPENDJ-4714: SSL handshake now sends 16KB list of CA issuer DNs

* OPENDJ-3121: Setup fails to create the lib/extensions directory in the instance.loc path, if a instance.loc file is used.

* OPENDJ-2605: Debian packages should be idempotent

* OPENDJ-1169: Exception/error lost when logging ERR\_LOOP\_REPLAYING\_OPERATION

* OPENDJ-640: Text Query Against indexed telephoneNumber Attribute Very Slow

## DS 6.5.0

* OPENDJ-5606: Upgrade to DS 6.0 fails if multiple filesystems are involved

* OPENDJ-5594: StackOverflowError with groupOfURLs when isMemberOf is requested

* OPENDJ-5582: LdapClientSocket connection leaked when handshake fails

* OPENDJ-5558: SDK: LdapUrl is not IPv6 clean

* OPENDJ-5553: Rest2Ldap cannot connect to TLSv1.2 servers

* OPENDJ-5496: DS fails to reconnect to an RS, disconnecting in handshake phase, after system restart

* OPENDJ-5481: ERR\_OPERATION\_NOT\_FOUND\_IN\_PENDING message used twice in different contexts

* OPENDJ-5406: Duplicate entry DNs if entry is deleted and then added during export-ldif or dsreplication initialize

* OPENDJ-5293: Proxy: Replication Service Discovery Mechanism logs WARNING

* OPENDJ-5272: "idle-time-limit" global configuration property has no effect

* OPENDJ-5210: Possible memory-leak if request received while bind in progress

* OPENDJ-5140: PersistentSearch heap usage grows

* OPENDJ-5137: Reading compressed or encrypted entries fails to close the InflaterInputStream

* OPENDJ-5115: ldappasswordmodify fails, NPE in PasswordPolicyState updatePasswordHistory

* OPENDJ-4967: Rest2ldap UndeliverableException occurs when a referenced entity cannot be fetched

* OPENDJ-4947: SASL DIGEST-MD5: bind request failed with protocol error

* OPENDJ-4881: Updates via Rest2ldap fail if record does not contain the necessary object class

* OPENDJ-4852: Backup with --backupAll misses a few backends

* OPENDJ-4625: Changelog range searches miss entries

* OPENDJ-4589: dsconfig --offline is not case-insensitive

* OPENDJ-4325: Changelog searches requesting changelogCookie are very slow

* OPENDJ-4229: status command with keystore options throws NullPointerException

* OPENDJ-3480: Updating schema backend properties while it is enabled leaves schema backend in broken state

* OPENDJ-3343: Invalid Conflict resolution on Add sequence when Parent & Child are added on different replica

* OPENDJ-3341: REST to LDAP gateway: HTTP response for API description is empty

* OPENDJ-3153: REST to LDAP gateway: changing password fails when using proxied authorization

* OPENDJ-2356: verify-index displays an inappropriate error message when run in online mode

---

---
title: Fixes in 7.4.x
description: Cumulative list of important fixes in PingDS 7.4.x maintenance releases.
component: pingds
version: release-notes
page_id: pingds::fixes-7.4
canonical_url: https://docs.pingidentity.com/pingds/release-notes/fixes-7.4.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-11-03T13:32:20Z
section_ids:
  ds_7_4_4: DS 7.4.4
  ds_7_4_3: DS 7.4.3
  ds_7_4_2: DS 7.4.2
  ds_7_4_1: DS 7.4.1
  ds_7_4_0: DS 7.4.0
  ds_7_3_0: DS 7.3.0
  ds_7_2_0: DS 7.2.0
  ds_7_1_0: DS 7.1.0
  ds_7_0_0: DS 7.0.0
  ds_6_5_0: DS 6.5.0
---

# Fixes in 7.4.x

This page lists the cumulative fixes in DS 7.4.x releases:

## DS 7.4.4

* OPENDJ-11243: Searches returning multiple attributes of the same OID use the last alias

## DS 7.4.3

* OPENDJ-10838: Change Number Indexer stops indexing when a Replication Server recovers from disk full errors

* OPENDJ-10314: Change number indexing does not take into account excluded domains

* OPENDJ-10082: Upgrade fails in Windows environment

* OPENDJ-10032: Inconsistent password storage scheme rehash policies can create multiple userPassword values

## DS 7.4.2

* OPENDJ-10139: Replication status "TOO\_LATE" does not mark DS as unhealthy

* OPENDJ-10131: ds-mon-receive-delay metric is not working

* OPENDJ-10078: Unable to use dsrepl initialize for cn=schema when 99-user.ldif only contains ds-sync-state entries

## DS 7.4.1

* OPENDJ-10211: Upgrading to DS 7.4.0 with a backend with confidentiality enabled fails

* OPENDJ-9999: DS uses encrypt/decrypt for key wrapping instead of wrap/unwrap

* OPENDJ-9966: ds-sync-delay and ds-sync-is-available are not correctly specified in schema

* OPENDJ-9917: VirtualListView limits returned entries when used with an attr#USERDN ACI

## DS 7.4.0

* OPENDJ-9692: Unindexed privilege not enforced for unindexed sorted and paged searches

* OPENDJ-9680: Reduce Argon2 memory requirement

* OPENDJ-9544: Searches for attributes that do not exist in schema still take time

* OPENDJ-9524: create-rc-script: systemd service should run start-ds/stop-ds, and not write a wrapper init script

* OPENDJ-9507: Enable GSSAPI/Kerberos to use wildcard principal

* OPENDJ-8849: An isolated DS (no RS) should return UNAVAILABLE instead of UNWILLING\_TO\_PERFORM

* OPENDJ-8796: Virtual attribute providers ignore critical controls, such as VLV, paging, and sorting

* OPENDJ-8228: Updates for an entry in a replicated sub-suffix appear also in the changelog for its parent

## DS 7.3.0

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | An issue was discovered in the 7.3.0 release that has the potential to corrupt *static groups*. To ensure data integrity, upgrade to 7.3.1 or later. This issue affects the stability and reliability of static groups only. Continuing to use version 7.3.0 may lead to data corruption and other unintended consequences.DS version 7.3.1 and later include the necessary fixes; however if you deployed DS 7.3.0 with static groups, you must contact [support](https://www.pingidentity.com/en/support/support-center.html) for assistance with resolving the data corruption. |

* OPENDJ-9300: DS 7.3 upgrade requires a full index rebuild

* OPENDJ-9295: Search involving BigIndex throws NoSuchElementException

* OPENDJ-9272: Change number indexing state is logged too often

* OPENDJ-9250: The max-allowed-client-connections limit should not apply to the admin connector

* OPENDJ-9245: DS backup to an S3 bucket on a new region fails

* OPENDJ-9213: The dsconfig list-replication-domains output contains redundant columns

* OPENDJ-9204: RS ignores DS state and forwards changes DS has already seen

* OPENDJ-9200: Backup process logs incorrect number of jdb files

* OPENDJ-9183: Replicated request controls serialized in LDIF using V1 encoding

* OPENDJ-9182: NPE in changelogstat on encountering a modify DN request

* OPENDJ-9167: Reading isMemberOf after adding, deleting, or renaming a static group can block for a long time when there are many static groups

* OPENDJ-9102: Log rotation stops once the File Count Retention Policy count is met

* OPENDJ-9042: All worker threads blocked waiting for abandon operations to complete

* OPENDJ-9041: Undeliverable unexpected exception while performing an abandon operation during server shutdown

* OPENDJ-9033: DS refuses to start and throws an NPE when a subordinate-base-dn is used

* OPENDJ-9032: The dsrepl --script-friendly option was never implemented and should not appear in the tool

* OPENDJ-9020: Replicas should persist their ReplicaOfflineMsg unless they're being recovered from the replication server

* OPENDJ-9007: LoadBalancer availability check fails if the current bind user state is "bad"

* OPENDJ-9002: Changelogstat outputs verbose CSNs for offline messages, but not other messages

* OPENDJ-9000: Missing RS - RS heartbeats are not detected

* OPENDJ-8992: A replica rejoining the topology after its changelog is purged is not tested for the correct server state

* OPENDJ-8975: Modified file permissions for 99-user.ldif revert to 600 when DS is restarted

* OPENDJ-8917: ReplicationBroker.java swallowed important debugging info

* OPENDJ-8831: Log when and why the ChangeNumberIndexer cannot move forward

* OPENDJ-8815: dsrepl status does not take bad data status into account

* OPENDJ-8808: Potential deadlock between overlapping rename operations

* OPENDJ-8779: Improve replica and changelog logging

* OPENDJ-8378: dsrepl status shows deleted replication domains

* OPENDJ-8233: RS connection error reason is not logged when hostname is not resolvable

* OPENDJ-7942: The server ignores critical VLV request controls when falling back to an unindexed search

* OPENDJ-7941: Client connections to proxy are timed out after 10 seconds regardless of activity

* OPENDJ-7925: Searchrate does not retrieve data when used simultaneously with modrate on groups

* OPENDJ-7688: Spurious DS disconnections because of missing heartbeat

* OPENDJ-7640: Supportextract does not collect all security stores when several keystores have the same basename

* OPENDJ-7516: External cn=changelog is not updated while replication initialization is in progress

* OPENDJ-3409: Retention and rotation policies do not work with CAUD handlers

* OPENDJ-3057: Replication Server starts listener although ChangeLog DB is unusable

## DS 7.2.0

* OPENDJ-8874: Full replica purge should write CSN information right away

* OPENDJ-8829: Error messages incorrectly mentions cn=System,cn=monitor

* OPENDJ-8805: dsconfig exits when setting the "bootstrap-replication-server" property with a \<null> value in the "Replication Service Discovery Mechanism".

* OPENDJ-8792: SDK: Log SSL exceptions as errors instead of warnings

* OPENDJ-8778: Setup option --trustStorePassword:file behaves differently than --trustStorePasswordFile

* OPENDJ-8727: HTTP embedded listener throws IllegalStateException: Output channel is not set

* OPENDJ-8698: DS should write config archive files in a crash consistent way

* OPENDJ-8610: RS-RS session thread stuck in Session.send could prevent DS from shutdown

* OPENDJ-8548: Optimize scoping of indexed searches

* OPENDJ-8532: Error running export-ldif offline: "DatabaseConfig.setReadOnly() must be set to false when creating a Database"

* OPENDJ-8500: IllegalMonitorStateException after subtree read lock timeout when adding an entry

* OPENDJ-8473: Upgrade does not migrate ds-cfg-je-property values

* OPENDJ-8383: dsrepl status fails when certificates accepted interactively

* OPENDJ-8280: DS will not start when using a non US Locale after changing config

* OPENDJ-8254: dsbackup restore/list slow to complete with cloud storage

* OPENDJ-8243: Indexes could cause ldapsearch to return multiple copies of the same entry

* OPENDJ-8227: Deadlock between Changelog DB purger and Thread for RS session

* OPENDJ-8226: Support Extract tool ignores non-default changelogDb location when collecting domains.state file

* OPENDJ-8205: Log message lists an object's string representation instead of a file name

* OPENDJ-8137: LDIF backend silently rejects entries that fail schema validation

* OPENDJ-8115: -Djavax.net.ssl.trustStore=\<value> in OPENDJ\_JAVA\_ARGS throws NullPointerException

* OPENDJ-8090: am-identity-store:7.1 setup profile is not functional

* OPENDJ-8079: targattrsfilters expression does not work with 2 filters but permits 1 or more than 2 filters

* OPENDJ-8062: Possible inconsistent state after backup restore

* OPENDJ-8046: Changelog files are not closed after searching cn=changelog

* OPENDJ-8028: Prometheus monitoring doesn't work with Telegraf

* OPENDJ-8024: Prevent configuration of VLV indexes with scope base-object

* OPENDJ-8008: OutOfMemoryException in subtree delete

* OPENDJ-7991: makeldif: "invalid number of arguments" using DateTime tag with colons

* OPENDJ-7971: dsbackup fails when JDB file cleaned

* OPENDJ-7970: Ensure that DS is crash resilient for all runtime file changes

* OPENDJ-7889: Configuring group-id against DS-only instance requires restart for the change to be reported by monitoring

* OPENDJ-7818: Package based upgrade does not support instances running as non-root

* OPENDJ-7816: dsbackup fails when destination is a symbolic link to a real directory

* OPENDJ-7755: DS 7.0 replication with older version, CryptoManager failed to import the symmetric key entry

* OPENDJ-7744: dsrepl initialize in a topology with DS7 and DS 5.5 fails if DS7 serverId starts with 0

* OPENDJ-7596: dsbackup has global connection options that do not work with some subcommands

* OPENDJ-4935: Replication instability and divergence when using high latency disks

## DS 7.1.0

* OPENDJ-7928: JSON normalization cannot handle nested arrays

* OPENDJ-7905: Schema replication error after upgrade

* OPENDJ-7867: NPE if dsbackup bucket name contains underscores

* OPENDJ-7851: Supportextract tool: clobbers the server.out filehandle when kill -3 is used.

* OPENDJ-7847: StaticGroup's objectclass sanity checks are unhelpful

* OPENDJ-7810: JMX connections are always considered insecure

* OPENDJ-7761: DS sporadically hangs while reconnecting to an RS

* OPENDJ-7758: DS 7.0 dsrepl add-local-server-to-pre-7-0-topology: NPE if master-key is in different keystore

* OPENDJ-7747: ldapmodify display full stack exception on LDIF errors if connection is already established

* OPENDJ-7737: ConfigurationFramework#initialize0 changes the class loader without clearing the map of registered jar files

* OPENDJ-7699: Supportextract throws NoSuchElementException when the server.pid file is empty

* OPENDJ-7689: dsrepl add-local-server-to-pre-7-0-topology does not tolerate separate keystore and truststore

* OPENDJ-7687: Global Access Control Policy regarding cn=schema is too restrictive

* OPENDJ-7674: Migrating encrypted changelog files during upgrade fails

* OPENDJ-7655: Replaying multiple MODIFYDN operations is very slow

* OPENDJ-7612: replication divergence on CTS in the cloud

* OPENDJ-7599: Cannot add a pre-encoded password to an entry without an existing password

* OPENDJ-7554: Windows: Secrets not retrieved from :file command-line arguments

* OPENDJ-7523: Example plugin and example pwdscheme pom.xml are missing correct revision

* OPENDJ-7513: Missing subSchemaSubEntry attribute from rootDSE access controls

* OPENDJ-7481: JSON logs do not contain proxy auth DN

* OPENDJ-7474: Docker sample README.md provides wrong instructions for running the container

* OPENDJ-7450: The startswith (sw) operator on indexed JSON attribute is slow

## DS 7.0.0

* OPENDJ-7319: Addrate can run out of memory when --deleteMode off and --noPurge are set

* OPENDJ-7286: Changelog searches can start with incorrect cursors

* OPENDJ-7176: Filters with malformed attribute descriptions cannot be parsed

* OPENDJ-7115: DS does not start when deployed with ISTIO sidecar container in the GCP K8s cloud

* OPENDJ-7016: status command outputs malformed JSON in script friendly mode

* OPENDJ-6994: strict-format-country-string does not affect the server

* OPENDJ-6787: Changelog searches are extremely slow if any cursors are exhausted

* OPENDJ-6778: Proxy server mishandles abandon requests

* OPENDJ-6733: SMTP handler sends incorrect email when account status is modified by manually updating ds-pwp-account-disabled attribute

* OPENDJ-6711: Replication status reports The provided value "5277383431" could not be parsed as an integer.

* OPENDJ-6557: IDM Password Sync plugin induces 100% CPU in Apache Http Components when used with JDK 11

* OPENDJ-6540: The Supportextract hangs when loggers are configured to use /dev/stdout

* OPENDJ-6527: Server does not return password policy responses with only warnings

* OPENDJ-6521: setup checks admin port despite options --skipPortCheck --doNotStart

* OPENDJ-6512: Problems when work queue fills

* OPENDJ-6499: Query on rest2ldap over ssl gets stuck after few curl requests using TLSv1.3 on JDK11

* OPENDJ-6377: Replication replay: issues with ReplaySynchronizer

* OPENDJ-6349: "RuntimeException: Should never happen" in HttpClientConnection

* OPENDJ-6240: DS not honoring per user resource limits when processing RESTful operation requests

* OPENDJ-6235: Stale ds-sync-hist attribute values reappear in the entry after replication is unconfigured

* OPENDJ-6222: SMTP messages are sometimes not encoded with the correct charset

* OPENDJ-6221: Logging for CONNECT operations are not saved in Nanosecond format

* OPENDJ-6196: HTTP connection handler continues to listen to 0.0.0.0 after setting listen-address

* OPENDJ-6188: Backend returns an incorrect error type when disk space hits low threshold

* OPENDJ-6173: cn=monitor memory pool stats do not get updated properly over time

* OPENDJ-6116: Unspecified Communications Error when multiple rest2ldap endpoints share configuration elements

* OPENDJ-5675: JDK11: supportextract tool cannot find jstack command

* OPENDJ-5664: JDK 11: illegal reflective access warning during import-ldif

* OPENDJ-5661: supportextract tool help and version options are different from other tools

* OPENDJ-5660: JDK 11: illegal reflective access warning on setup (with profile)

* OPENDJ-5611: Change number indexing can lag behind replication under extreme load

* OPENDJ-5590: Proxy: server discovery fails silently when proxy base-dn differs from backend's base-dn

* OPENDJ-5584: Server does not validate sum of memory used by JE backend caches in all cases

* OPENDJ-4764: REST2LDAP gateway sasl-plain authorization doesn't handle dn: correctly

* OPENDJ-4714: SSL handshake now sends 16KB list of CA issuer DNs

* OPENDJ-3121: Setup fails to create the lib/extensions directory in the instance.loc path, if a instance.loc file is used.

* OPENDJ-2605: Debian packages should be idempotent

* OPENDJ-1169: Exception/error lost when logging ERR\_LOOP\_REPLAYING\_OPERATION

* OPENDJ-640: Text Query Against indexed telephoneNumber Attribute Very Slow

## DS 6.5.0

* OPENDJ-5606: Upgrade to DS 6.0 fails if multiple filesystems are involved

* OPENDJ-5594: StackOverflowError with groupOfURLs when isMemberOf is requested

* OPENDJ-5582: LdapClientSocket connection leaked when handshake fails

* OPENDJ-5558: SDK: LdapUrl is not IPv6 clean

* OPENDJ-5553: Rest2Ldap cannot connect to TLSv1.2 servers

* OPENDJ-5496: DS fails to reconnect to an RS, disconnecting in handshake phase, after system restart

* OPENDJ-5481: ERR\_OPERATION\_NOT\_FOUND\_IN\_PENDING message used twice in different contexts

* OPENDJ-5406: Duplicate entry DNs if entry is deleted and then added during export-ldif or dsreplication initialize

* OPENDJ-5293: Proxy: Replication Service Discovery Mechanism logs WARNING

* OPENDJ-5272: "idle-time-limit" global configuration property has no effect

* OPENDJ-5210: Possible memory-leak if request received while bind in progress

* OPENDJ-5140: PersistentSearch heap usage grows

* OPENDJ-5137: Reading compressed or encrypted entries fails to close the InflaterInputStream

* OPENDJ-5115: ldappasswordmodify fails, NPE in PasswordPolicyState updatePasswordHistory

* OPENDJ-4967: Rest2ldap UndeliverableException occurs when a referenced entity cannot be fetched

* OPENDJ-4947: SASL DIGEST-MD5: bind request failed with protocol error

* OPENDJ-4881: Updates via Rest2ldap fail if record does not contain the necessary object class

* OPENDJ-4852: Backup with --backupAll misses a few backends

* OPENDJ-4625: Changelog range searches miss entries

* OPENDJ-4589: dsconfig --offline is not case-insensitive

* OPENDJ-4325: Changelog searches requesting changelogCookie are very slow

* OPENDJ-4229: status command with keystore options throws NullPointerException

* OPENDJ-3480: Updating schema backend properties while it is enabled leaves schema backend in broken state

* OPENDJ-3343: Invalid Conflict resolution on Add sequence when Parent & Child are added on different replica

* OPENDJ-3341: REST to LDAP gateway: HTTP response for API description is empty

* OPENDJ-3153: REST to LDAP gateway: changing password fails when using proxied authorization

* OPENDJ-2356: verify-index displays an inappropriate error message when run in online mode

---

---
title: Fixes in 7.5.x
description: Cumulative list of important fixes in PingDS 7.5.x maintenance releases.
component: pingds
version: release-notes
page_id: pingds::fixes-7.5
canonical_url: https://docs.pingidentity.com/pingds/release-notes/fixes-7.5.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-07-01T12:00:00Z
section_ids:
  ds_7_5_4: DS 7.5.4
  ds_7_5_3: DS 7.5.3
  ds_7_5_2: DS 7.5.2
  ds_7_5_1: DS 7.5.1
  ds_7_5_0: DS 7.5.0
  ds_7_4_0: DS 7.4.0
  ds_7_3_0: DS 7.3.0
  ds_7_2_0: DS 7.2.0
  ds_7_1_0: DS 7.1.0
  ds_7_0_0: DS 7.0.0
  ds_6_5_0: DS 6.5.0
---

# Fixes in 7.5.x

This page lists the cumulative fixes in DS 7.5.x releases:

## DS 7.5.4

* OPENDJ-12168: JE cache monitoring statistics appear to be broken when there are multiple backends

* OPENDJ-12160: stop-ds doesn't work if a telnet connection is present

* OPENDJ-11971: Failed StartTLS connections aren't disconnected

* OPENDJ-11970: Worker threads stuck performing abandon or cancel operations

## DS 7.5.3

* OPENDJ-11763: Potential deadlock when processing bind requests and protocol errors on the RX LDAP connection handler

* OPENDJ-11706: In the middle of paged searches, DS can start returning entries from the first page

* OPENDJ-11667: DS accepts search requests presenting obviously invalid paging cookies

* OPENDJ-11536: NullPointerException in compressed schema

## DS 7.5.2

* OPENDJ-11243: Searches returning multiple attributes of the same OID use the last alias

* OPENDJ-11032: simplePageSize=0 should be allowed in the ldapsearch command

* OPENDJ-10863: Very slow response when using debugsearchindex

* OPENDJ-10674: Dynamic groups not initialized after restart in platform deployment

* OPENDJ-10532: The case of a baseDN can be changed once replicated

## DS 7.5.1

* OPENDJ-10482: Referential integrity plugin cannot be used with a big-extensible index

* OPENDJ-10314: Change number indexing does not take into account excluded domains

* OPENDJ-10082: Upgrade fails in Windows environment

* OPENDJ-10032: Inconsistent password storage scheme rehash policies can create multiple userPassword values

## DS 7.5.0

* OPENDJ-10306: Null pointer exceptions due to unrecognized (UNKNOWN) requests

* OPENDJ-10171: etag in schema config entry leads to schema violation error when attempting to update cn=schema

* OPENDJ-10139: Replication status "TOO\_LATE" does not mark DS as unhealthy

* OPENDJ-10131: ds-mon-receive-delay metric is not working

* OPENDJ-10078: Unable to use dsrepl initialize for cn=schema when 99-user.ldif only contains ds-sync-state entries

* OPENDJ-9913: Bind via REST API ignores force-change-on-add in password policy

## DS 7.4.0

* OPENDJ-9692: Unindexed privilege not enforced for unindexed sorted and paged searches

* OPENDJ-9680: Reduce Argon2 memory requirement

* OPENDJ-9544: Searches for attributes that do not exist in schema still take time

* OPENDJ-9524: create-rc-script: systemd service should run start-ds/stop-ds, and not write a wrapper init script

* OPENDJ-9507: Enable GSSAPI/Kerberos to use wildcard principal

* OPENDJ-8849: An isolated DS (no RS) should return UNAVAILABLE instead of UNWILLING\_TO\_PERFORM

* OPENDJ-8796: Virtual attribute providers ignore critical controls, such as VLV, paging, and sorting

* OPENDJ-8228: Updates for an entry in a replicated sub-suffix appear also in the changelog for its parent

## DS 7.3.0

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | An issue was discovered in the 7.3.0 release that has the potential to corrupt *static groups*. To ensure data integrity, upgrade to 7.3.1 or later. This issue affects the stability and reliability of static groups only. Continuing to use version 7.3.0 may lead to data corruption and other unintended consequences.DS version 7.3.1 and later include the necessary fixes; however if you deployed DS 7.3.0 with static groups, you must contact [support](https://www.pingidentity.com/en/support/support-center.html) for assistance with resolving the data corruption. |

* OPENDJ-9300: DS 7.3 upgrade requires a full index rebuild

* OPENDJ-9295: Search involving BigIndex throws NoSuchElementException

* OPENDJ-9272: Change number indexing state is logged too often

* OPENDJ-9250: The max-allowed-client-connections limit should not apply to the admin connector

* OPENDJ-9245: DS backup to an S3 bucket on a new region fails

* OPENDJ-9213: The dsconfig list-replication-domains output contains redundant columns

* OPENDJ-9204: RS ignores DS state and forwards changes DS has already seen

* OPENDJ-9200: Backup process logs incorrect number of jdb files

* OPENDJ-9183: Replicated request controls serialized in LDIF using V1 encoding

* OPENDJ-9182: NPE in changelogstat on encountering a modify DN request

* OPENDJ-9167: Reading isMemberOf after adding, deleting, or renaming a static group can block for a long time when there are many static groups

* OPENDJ-9102: Log rotation stops once the File Count Retention Policy count is met

* OPENDJ-9042: All worker threads blocked waiting for abandon operations to complete

* OPENDJ-9041: Undeliverable unexpected exception while performing an abandon operation during server shutdown

* OPENDJ-9033: DS refuses to start and throws an NPE when a subordinate-base-dn is used

* OPENDJ-9032: The dsrepl --script-friendly option was never implemented and should not appear in the tool

* OPENDJ-9020: Replicas should persist their ReplicaOfflineMsg unless they're being recovered from the replication server

* OPENDJ-9007: LoadBalancer availability check fails if the current bind user state is "bad"

* OPENDJ-9002: Changelogstat outputs verbose CSNs for offline messages, but not other messages

* OPENDJ-9000: Missing RS - RS heartbeats are not detected

* OPENDJ-8992: A replica rejoining the topology after its changelog is purged is not tested for the correct server state

* OPENDJ-8975: Modified file permissions for 99-user.ldif revert to 600 when DS is restarted

* OPENDJ-8917: ReplicationBroker.java swallowed important debugging info

* OPENDJ-8831: Log when and why the ChangeNumberIndexer cannot move forward

* OPENDJ-8815: dsrepl status does not take bad data status into account

* OPENDJ-8808: Potential deadlock between overlapping rename operations

* OPENDJ-8779: Improve replica and changelog logging

* OPENDJ-8378: dsrepl status shows deleted replication domains

* OPENDJ-8233: RS connection error reason is not logged when hostname is not resolvable

* OPENDJ-7942: The server ignores critical VLV request controls when falling back to an unindexed search

* OPENDJ-7941: Client connections to proxy are timed out after 10 seconds regardless of activity

* OPENDJ-7925: Searchrate does not retrieve data when used simultaneously with modrate on groups

* OPENDJ-7688: Spurious DS disconnections because of missing heartbeat

* OPENDJ-7640: Supportextract does not collect all security stores when several keystores have the same basename

* OPENDJ-7516: External cn=changelog is not updated while replication initialization is in progress

* OPENDJ-3409: Retention and rotation policies do not work with CAUD handlers

* OPENDJ-3057: Replication Server starts listener although ChangeLog DB is unusable

## DS 7.2.0

* OPENDJ-8874: Full replica purge should write CSN information right away

* OPENDJ-8829: Error messages incorrectly mentions cn=System,cn=monitor

* OPENDJ-8805: dsconfig exits when setting the "bootstrap-replication-server" property with a \<null> value in the "Replication Service Discovery Mechanism".

* OPENDJ-8792: SDK: Log SSL exceptions as errors instead of warnings

* OPENDJ-8778: Setup option --trustStorePassword:file behaves differently than --trustStorePasswordFile

* OPENDJ-8727: HTTP embedded listener throws IllegalStateException: Output channel is not set

* OPENDJ-8698: DS should write config archive files in a crash consistent way

* OPENDJ-8610: RS-RS session thread stuck in Session.send could prevent DS from shutdown

* OPENDJ-8548: Optimize scoping of indexed searches

* OPENDJ-8532: Error running export-ldif offline: "DatabaseConfig.setReadOnly() must be set to false when creating a Database"

* OPENDJ-8500: IllegalMonitorStateException after subtree read lock timeout when adding an entry

* OPENDJ-8473: Upgrade does not migrate ds-cfg-je-property values

* OPENDJ-8383: dsrepl status fails when certificates accepted interactively

* OPENDJ-8280: DS will not start when using a non US Locale after changing config

* OPENDJ-8254: dsbackup restore/list slow to complete with cloud storage

* OPENDJ-8243: Indexes could cause ldapsearch to return multiple copies of the same entry

* OPENDJ-8227: Deadlock between Changelog DB purger and Thread for RS session

* OPENDJ-8226: Support Extract tool ignores non-default changelogDb location when collecting domains.state file

* OPENDJ-8205: Log message lists an object's string representation instead of a file name

* OPENDJ-8137: LDIF backend silently rejects entries that fail schema validation

* OPENDJ-8115: -Djavax.net.ssl.trustStore=\<value> in OPENDJ\_JAVA\_ARGS throws NullPointerException

* OPENDJ-8090: am-identity-store:7.1 setup profile is not functional

* OPENDJ-8079: targattrsfilters expression does not work with 2 filters but permits 1 or more than 2 filters

* OPENDJ-8062: Possible inconsistent state after backup restore

* OPENDJ-8046: Changelog files are not closed after searching cn=changelog

* OPENDJ-8028: Prometheus monitoring doesn't work with Telegraf

* OPENDJ-8024: Prevent configuration of VLV indexes with scope base-object

* OPENDJ-8008: OutOfMemoryException in subtree delete

* OPENDJ-7991: makeldif: "invalid number of arguments" using DateTime tag with colons

* OPENDJ-7971: dsbackup fails when JDB file cleaned

* OPENDJ-7970: Ensure that DS is crash resilient for all runtime file changes

* OPENDJ-7889: Configuring group-id against DS-only instance requires restart for the change to be reported by monitoring

* OPENDJ-7818: Package based upgrade does not support instances running as non-root

* OPENDJ-7816: dsbackup fails when destination is a symbolic link to a real directory

* OPENDJ-7755: DS 7.0 replication with older version, CryptoManager failed to import the symmetric key entry

* OPENDJ-7744: dsrepl initialize in a topology with DS7 and DS 5.5 fails if DS7 serverId starts with 0

* OPENDJ-7596: dsbackup has global connection options that do not work with some subcommands

* OPENDJ-4935: Replication instability and divergence when using high latency disks

## DS 7.1.0

* OPENDJ-7928: JSON normalization cannot handle nested arrays

* OPENDJ-7905: Schema replication error after upgrade

* OPENDJ-7867: NPE if dsbackup bucket name contains underscores

* OPENDJ-7851: Supportextract tool: clobbers the server.out filehandle when kill -3 is used.

* OPENDJ-7847: StaticGroup's objectclass sanity checks are unhelpful

* OPENDJ-7810: JMX connections are always considered insecure

* OPENDJ-7761: DS sporadically hangs while reconnecting to an RS

* OPENDJ-7758: DS 7.0 dsrepl add-local-server-to-pre-7-0-topology: NPE if master-key is in different keystore

* OPENDJ-7747: ldapmodify display full stack exception on LDIF errors if connection is already established

* OPENDJ-7737: ConfigurationFramework#initialize0 changes the class loader without clearing the map of registered jar files

* OPENDJ-7699: Supportextract throws NoSuchElementException when the server.pid file is empty

* OPENDJ-7689: dsrepl add-local-server-to-pre-7-0-topology does not tolerate separate keystore and truststore

* OPENDJ-7687: Global Access Control Policy regarding cn=schema is too restrictive

* OPENDJ-7674: Migrating encrypted changelog files during upgrade fails

* OPENDJ-7655: Replaying multiple MODIFYDN operations is very slow

* OPENDJ-7612: replication divergence on CTS in the cloud

* OPENDJ-7599: Cannot add a pre-encoded password to an entry without an existing password

* OPENDJ-7554: Windows: Secrets not retrieved from :file command-line arguments

* OPENDJ-7523: Example plugin and example pwdscheme pom.xml are missing correct revision

* OPENDJ-7513: Missing subSchemaSubEntry attribute from rootDSE access controls

* OPENDJ-7481: JSON logs do not contain proxy auth DN

* OPENDJ-7474: Docker sample README.md provides wrong instructions for running the container

* OPENDJ-7450: The startswith (sw) operator on indexed JSON attribute is slow

## DS 7.0.0

* OPENDJ-7319: Addrate can run out of memory when --deleteMode off and --noPurge are set

* OPENDJ-7286: Changelog searches can start with incorrect cursors

* OPENDJ-7176: Filters with malformed attribute descriptions cannot be parsed

* OPENDJ-7115: DS does not start when deployed with ISTIO sidecar container in the GCP K8s cloud

* OPENDJ-7016: status command outputs malformed JSON in script friendly mode

* OPENDJ-6994: strict-format-country-string does not affect the server

* OPENDJ-6787: Changelog searches are extremely slow if any cursors are exhausted

* OPENDJ-6778: Proxy server mishandles abandon requests

* OPENDJ-6733: SMTP handler sends incorrect email when account status is modified by manually updating ds-pwp-account-disabled attribute

* OPENDJ-6711: Replication status reports The provided value "5277383431" could not be parsed as an integer.

* OPENDJ-6557: IDM Password Sync plugin induces 100% CPU in Apache Http Components when used with JDK 11

* OPENDJ-6540: The Supportextract hangs when loggers are configured to use /dev/stdout

* OPENDJ-6527: Server does not return password policy responses with only warnings

* OPENDJ-6521: setup checks admin port despite options --skipPortCheck --doNotStart

* OPENDJ-6512: Problems when work queue fills

* OPENDJ-6499: Query on rest2ldap over ssl gets stuck after few curl requests using TLSv1.3 on JDK11

* OPENDJ-6377: Replication replay: issues with ReplaySynchronizer

* OPENDJ-6349: "RuntimeException: Should never happen" in HttpClientConnection

* OPENDJ-6240: DS not honoring per user resource limits when processing RESTful operation requests

* OPENDJ-6235: Stale ds-sync-hist attribute values reappear in the entry after replication is unconfigured

* OPENDJ-6222: SMTP messages are sometimes not encoded with the correct charset

* OPENDJ-6221: Logging for CONNECT operations are not saved in Nanosecond format

* OPENDJ-6196: HTTP connection handler continues to listen to 0.0.0.0 after setting listen-address

* OPENDJ-6188: Backend returns an incorrect error type when disk space hits low threshold

* OPENDJ-6173: cn=monitor memory pool stats do not get updated properly over time

* OPENDJ-6116: Unspecified Communications Error when multiple rest2ldap endpoints share configuration elements

* OPENDJ-5675: JDK11: supportextract tool cannot find jstack command

* OPENDJ-5664: JDK 11: illegal reflective access warning during import-ldif

* OPENDJ-5661: supportextract tool help and version options are different from other tools

* OPENDJ-5660: JDK 11: illegal reflective access warning on setup (with profile)

* OPENDJ-5611: Change number indexing can lag behind replication under extreme load

* OPENDJ-5590: Proxy: server discovery fails silently when proxy base-dn differs from backend's base-dn

* OPENDJ-5584: Server does not validate sum of memory used by JE backend caches in all cases

* OPENDJ-4764: REST2LDAP gateway sasl-plain authorization doesn't handle dn: correctly

* OPENDJ-4714: SSL handshake now sends 16KB list of CA issuer DNs

* OPENDJ-3121: Setup fails to create the lib/extensions directory in the instance.loc path, if a instance.loc file is used.

* OPENDJ-2605: Debian packages should be idempotent

* OPENDJ-1169: Exception/error lost when logging ERR\_LOOP\_REPLAYING\_OPERATION

* OPENDJ-640: Text Query Against indexed telephoneNumber Attribute Very Slow

## DS 6.5.0

* OPENDJ-5606: Upgrade to DS 6.0 fails if multiple filesystems are involved

* OPENDJ-5594: StackOverflowError with groupOfURLs when isMemberOf is requested

* OPENDJ-5582: LdapClientSocket connection leaked when handshake fails

* OPENDJ-5558: SDK: LdapUrl is not IPv6 clean

* OPENDJ-5553: Rest2Ldap cannot connect to TLSv1.2 servers

* OPENDJ-5496: DS fails to reconnect to an RS, disconnecting in handshake phase, after system restart

* OPENDJ-5481: ERR\_OPERATION\_NOT\_FOUND\_IN\_PENDING message used twice in different contexts

* OPENDJ-5406: Duplicate entry DNs if entry is deleted and then added during export-ldif or dsreplication initialize

* OPENDJ-5293: Proxy: Replication Service Discovery Mechanism logs WARNING

* OPENDJ-5272: "idle-time-limit" global configuration property has no effect

* OPENDJ-5210: Possible memory-leak if request received while bind in progress

* OPENDJ-5140: PersistentSearch heap usage grows

* OPENDJ-5137: Reading compressed or encrypted entries fails to close the InflaterInputStream

* OPENDJ-5115: ldappasswordmodify fails, NPE in PasswordPolicyState updatePasswordHistory

* OPENDJ-4967: Rest2ldap UndeliverableException occurs when a referenced entity cannot be fetched

* OPENDJ-4947: SASL DIGEST-MD5: bind request failed with protocol error

* OPENDJ-4881: Updates via Rest2ldap fail if record does not contain the necessary object class

* OPENDJ-4852: Backup with --backupAll misses a few backends

* OPENDJ-4625: Changelog range searches miss entries

* OPENDJ-4589: dsconfig --offline is not case-insensitive

* OPENDJ-4325: Changelog searches requesting changelogCookie are very slow

* OPENDJ-4229: status command with keystore options throws NullPointerException

* OPENDJ-3480: Updating schema backend properties while it is enabled leaves schema backend in broken state

* OPENDJ-3343: Invalid Conflict resolution on Add sequence when Parent & Child are added on different replica

* OPENDJ-3341: REST to LDAP gateway: HTTP response for API description is empty

* OPENDJ-3153: REST to LDAP gateway: changing password fails when using proxied authorization

* OPENDJ-2356: verify-index displays an inappropriate error message when run in online mode

---

---
title: Fixes in 8.0.x
description: Cumulative list of important fixes in PingDS 8.0.x maintenance releases.
component: pingds
version: release-notes
page_id: pingds::fixes-8.0
canonical_url: https://docs.pingidentity.com/pingds/release-notes/fixes-8.0.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-07-07T12:00:00Z
section_ids:
  ds_8_0_4: DS 8.0.4
  ds_8_0_3: DS 8.0.3
  ds_8_0_2: DS 8.0.2
  ds_8_0_1: DS 8.0.1
  ds_8_0_0: DS 8.0.0
  ds_7_5_0: DS 7.5.0
  ds_7_4_0: DS 7.4.0
  ds_7_3_0: DS 7.3.0
  ds_7_2_0: DS 7.2.0
  ds_7_1_0: DS 7.1.0
  ds_7_0_0: DS 7.0.0
  ds_6_5_0: DS 6.5.0
---

# Fixes in 8.0.x

This page lists the cumulative fixes in DS 8.0.x releases:

## DS 8.0.4

No new fixes in this release.

## DS 8.0.3

* OPENDJ-12168: JE cache monitoring statistics appear to be broken when there are multiple backends

* OPENDJ-12160: stop-ds doesn't work if a telnet connection is present

* OPENDJ-11971: Failed StartTLS connections aren't disconnected

* OPENDJ-11970: Worker threads stuck performing abandon or cancel operations

## DS 8.0.2

* OPENDJ-11763: Potential deadlock when processing bind requests and protocol errors on the RX LDAP connection handler

* OPENDJ-11706: In the middle of paged searches, DS can start returning entries from the first page

## DS 8.0.1

* OPENDJ-11667: DS accepts search requests presenting obviously invalid paging cookies

* OPENDJ-11576: Empty attribute values match password substrings

* OPENDJ-11536: NullPointerException in compressed schema

* OPENDJ-11486: Index processing failure: IndexOutOfBoundsException in EntryContainer.java when processing complex filters

## DS 8.0.0

* OPENDJ-11280: OAuth2 token auth\_time field recorded in seconds instead of milliseconds causes very high DB contention

* OPENDJ-11243: Searches returning multiple attributes of the same OID use the last alias

* OPENDJ-11191: Upgrade fails in Windows environment if directory path contains spaces

* OPENDJ-11001: manage-tasks stuck after creating backup and backup purge

* OPENDJ-10912: DS rejects MODIFY requests with no modifications

* OPENDJ-10863: Very slow response when using debugsearchindex

* OPENDJ-10532: The case of a baseDN can be changed once replicated

* OPENDJ-10010: HTTP/HTTPS connection handler only creates one listener address when multiple addresses are specified

## DS 7.5.0

* OPENDJ-10306: Null pointer exceptions due to unrecognized (UNKNOWN) requests

* OPENDJ-10171: etag in schema config entry leads to schema violation error when attempting to update cn=schema

* OPENDJ-10139: Replication status "TOO\_LATE" does not mark DS as unhealthy

* OPENDJ-10131: ds-mon-receive-delay metric is not working

* OPENDJ-10078: Unable to use dsrepl initialize for cn=schema when 99-user.ldif only contains ds-sync-state entries

* OPENDJ-9913: Bind via REST API ignores force-change-on-add in password policy

## DS 7.4.0

* OPENDJ-9692: Unindexed privilege not enforced for unindexed sorted and paged searches

* OPENDJ-9680: Reduce Argon2 memory requirement

* OPENDJ-9544: Searches for attributes that do not exist in schema still take time

* OPENDJ-9524: create-rc-script: systemd service should run start-ds/stop-ds, and not write a wrapper init script

* OPENDJ-9507: Enable GSSAPI/Kerberos to use wildcard principal

* OPENDJ-8849: An isolated DS (no RS) should return UNAVAILABLE instead of UNWILLING\_TO\_PERFORM

* OPENDJ-8796: Virtual attribute providers ignore critical controls, such as VLV, paging, and sorting

* OPENDJ-8228: Updates for an entry in a replicated sub-suffix appear also in the changelog for its parent

## DS 7.3.0

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | An issue was discovered in the 7.3.0 release that has the potential to corrupt *static groups*. To ensure data integrity, upgrade to 7.3.1 or later. This issue affects the stability and reliability of static groups only. Continuing to use version 7.3.0 may lead to data corruption and other unintended consequences.DS version 7.3.1 and later include the necessary fixes; however if you deployed DS 7.3.0 with static groups, you must contact [support](https://www.pingidentity.com/en/support/support-center.html) for assistance with resolving the data corruption. |

* OPENDJ-9300: DS 7.3 upgrade requires a full index rebuild

* OPENDJ-9295: Search involving BigIndex throws NoSuchElementException

* OPENDJ-9272: Change number indexing state is logged too often

* OPENDJ-9250: The max-allowed-client-connections limit should not apply to the admin connector

* OPENDJ-9245: DS backup to an S3 bucket on a new region fails

* OPENDJ-9213: The dsconfig list-replication-domains output contains redundant columns

* OPENDJ-9204: RS ignores DS state and forwards changes DS has already seen

* OPENDJ-9200: Backup process logs incorrect number of jdb files

* OPENDJ-9183: Replicated request controls serialized in LDIF using V1 encoding

* OPENDJ-9182: NPE in changelogstat on encountering a modify DN request

* OPENDJ-9167: Reading isMemberOf after adding, deleting, or renaming a static group can block for a long time when there are many static groups

* OPENDJ-9102: Log rotation stops once the File Count Retention Policy count is met

* OPENDJ-9042: All worker threads blocked waiting for abandon operations to complete

* OPENDJ-9041: Undeliverable unexpected exception while performing an abandon operation during server shutdown

* OPENDJ-9033: DS refuses to start and throws an NPE when a subordinate-base-dn is used

* OPENDJ-9032: The dsrepl --script-friendly option was never implemented and should not appear in the tool

* OPENDJ-9020: Replicas should persist their ReplicaOfflineMsg unless they're being recovered from the replication server

* OPENDJ-9007: LoadBalancer availability check fails if the current bind user state is "bad"

* OPENDJ-9002: Changelogstat outputs verbose CSNs for offline messages, but not other messages

* OPENDJ-9000: Missing RS - RS heartbeats are not detected

* OPENDJ-8992: A replica rejoining the topology after its changelog is purged is not tested for the correct server state

* OPENDJ-8975: Modified file permissions for 99-user.ldif revert to 600 when DS is restarted

* OPENDJ-8917: ReplicationBroker.java swallowed important debugging info

* OPENDJ-8831: Log when and why the ChangeNumberIndexer cannot move forward

* OPENDJ-8815: dsrepl status does not take bad data status into account

* OPENDJ-8808: Potential deadlock between overlapping rename operations

* OPENDJ-8779: Improve replica and changelog logging

* OPENDJ-8378: dsrepl status shows deleted replication domains

* OPENDJ-8233: RS connection error reason is not logged when hostname is not resolvable

* OPENDJ-7942: The server ignores critical VLV request controls when falling back to an unindexed search

* OPENDJ-7941: Client connections to proxy are timed out after 10 seconds regardless of activity

* OPENDJ-7925: Searchrate does not retrieve data when used simultaneously with modrate on groups

* OPENDJ-7688: Spurious DS disconnections because of missing heartbeat

* OPENDJ-7640: Supportextract does not collect all security stores when several keystores have the same basename

* OPENDJ-7516: External cn=changelog is not updated while replication initialization is in progress

* OPENDJ-3409: Retention and rotation policies do not work with CAUD handlers

* OPENDJ-3057: Replication Server starts listener although ChangeLog DB is unusable

## DS 7.2.0

* OPENDJ-8874: Full replica purge should write CSN information right away

* OPENDJ-8829: Error messages incorrectly mentions cn=System,cn=monitor

* OPENDJ-8805: dsconfig exits when setting the "bootstrap-replication-server" property with a \<null> value in the "Replication Service Discovery Mechanism".

* OPENDJ-8792: SDK: Log SSL exceptions as errors instead of warnings

* OPENDJ-8778: Setup option --trustStorePassword:file behaves differently than --trustStorePasswordFile

* OPENDJ-8727: HTTP embedded listener throws IllegalStateException: Output channel is not set

* OPENDJ-8698: DS should write config archive files in a crash consistent way

* OPENDJ-8610: RS-RS session thread stuck in Session.send could prevent DS from shutdown

* OPENDJ-8548: Optimize scoping of indexed searches

* OPENDJ-8532: Error running export-ldif offline: "DatabaseConfig.setReadOnly() must be set to false when creating a Database"

* OPENDJ-8500: IllegalMonitorStateException after subtree read lock timeout when adding an entry

* OPENDJ-8473: Upgrade does not migrate ds-cfg-je-property values

* OPENDJ-8383: dsrepl status fails when certificates accepted interactively

* OPENDJ-8280: DS will not start when using a non US Locale after changing config

* OPENDJ-8254: dsbackup restore/list slow to complete with cloud storage

* OPENDJ-8243: Indexes could cause ldapsearch to return multiple copies of the same entry

* OPENDJ-8227: Deadlock between Changelog DB purger and Thread for RS session

* OPENDJ-8226: Support Extract tool ignores non-default changelogDb location when collecting domains.state file

* OPENDJ-8205: Log message lists an object's string representation instead of a file name

* OPENDJ-8137: LDIF backend silently rejects entries that fail schema validation

* OPENDJ-8115: -Djavax.net.ssl.trustStore=\<value> in OPENDJ\_JAVA\_ARGS throws NullPointerException

* OPENDJ-8090: am-identity-store:7.1 setup profile is not functional

* OPENDJ-8079: targattrsfilters expression does not work with 2 filters but permits 1 or more than 2 filters

* OPENDJ-8062: Possible inconsistent state after backup restore

* OPENDJ-8046: Changelog files are not closed after searching cn=changelog

* OPENDJ-8028: Prometheus monitoring doesn't work with Telegraf

* OPENDJ-8024: Prevent configuration of VLV indexes with scope base-object

* OPENDJ-8008: OutOfMemoryException in subtree delete

* OPENDJ-7991: makeldif: "invalid number of arguments" using DateTime tag with colons

* OPENDJ-7971: dsbackup fails when JDB file cleaned

* OPENDJ-7970: Ensure that DS is crash resilient for all runtime file changes

* OPENDJ-7889: Configuring group-id against DS-only instance requires restart for the change to be reported by monitoring

* OPENDJ-7818: Package based upgrade does not support instances running as non-root

* OPENDJ-7816: dsbackup fails when destination is a symbolic link to a real directory

* OPENDJ-7755: DS 7.0 replication with older version, CryptoManager failed to import the symmetric key entry

* OPENDJ-7744: dsrepl initialize in a topology with DS7 and DS 5.5 fails if DS7 serverId starts with 0

* OPENDJ-7596: dsbackup has global connection options that do not work with some subcommands

* OPENDJ-4935: Replication instability and divergence when using high latency disks

## DS 7.1.0

* OPENDJ-7928: JSON normalization cannot handle nested arrays

* OPENDJ-7905: Schema replication error after upgrade

* OPENDJ-7867: NPE if dsbackup bucket name contains underscores

* OPENDJ-7851: Supportextract tool: clobbers the server.out filehandle when kill -3 is used.

* OPENDJ-7847: StaticGroup's objectclass sanity checks are unhelpful

* OPENDJ-7810: JMX connections are always considered insecure

* OPENDJ-7761: DS sporadically hangs while reconnecting to an RS

* OPENDJ-7758: DS 7.0 dsrepl add-local-server-to-pre-7-0-topology: NPE if master-key is in different keystore

* OPENDJ-7747: ldapmodify display full stack exception on LDIF errors if connection is already established

* OPENDJ-7737: ConfigurationFramework#initialize0 changes the class loader without clearing the map of registered jar files

* OPENDJ-7699: Supportextract throws NoSuchElementException when the server.pid file is empty

* OPENDJ-7689: dsrepl add-local-server-to-pre-7-0-topology does not tolerate separate keystore and truststore

* OPENDJ-7687: Global Access Control Policy regarding cn=schema is too restrictive

* OPENDJ-7674: Migrating encrypted changelog files during upgrade fails

* OPENDJ-7655: Replaying multiple MODIFYDN operations is very slow

* OPENDJ-7612: replication divergence on CTS in the cloud

* OPENDJ-7599: Cannot add a pre-encoded password to an entry without an existing password

* OPENDJ-7554: Windows: Secrets not retrieved from :file command-line arguments

* OPENDJ-7523: Example plugin and example pwdscheme pom.xml are missing correct revision

* OPENDJ-7513: Missing subSchemaSubEntry attribute from rootDSE access controls

* OPENDJ-7481: JSON logs do not contain proxy auth DN

* OPENDJ-7474: Docker sample README.md provides wrong instructions for running the container

* OPENDJ-7450: The startswith (sw) operator on indexed JSON attribute is slow

## DS 7.0.0

* OPENDJ-7319: Addrate can run out of memory when --deleteMode off and --noPurge are set

* OPENDJ-7286: Changelog searches can start with incorrect cursors

* OPENDJ-7176: Filters with malformed attribute descriptions cannot be parsed

* OPENDJ-7115: DS does not start when deployed with ISTIO sidecar container in the GCP K8s cloud

* OPENDJ-7016: status command outputs malformed JSON in script friendly mode

* OPENDJ-6994: strict-format-country-string does not affect the server

* OPENDJ-6787: Changelog searches are extremely slow if any cursors are exhausted

* OPENDJ-6778: Proxy server mishandles abandon requests

* OPENDJ-6733: SMTP handler sends incorrect email when account status is modified by manually updating ds-pwp-account-disabled attribute

* OPENDJ-6711: Replication status reports The provided value "5277383431" could not be parsed as an integer.

* OPENDJ-6557: IDM Password Sync plugin induces 100% CPU in Apache Http Components when used with JDK 11

* OPENDJ-6540: The Supportextract hangs when loggers are configured to use /dev/stdout

* OPENDJ-6527: Server does not return password policy responses with only warnings

* OPENDJ-6521: setup checks admin port despite options --skipPortCheck --doNotStart

* OPENDJ-6512: Problems when work queue fills

* OPENDJ-6499: Query on rest2ldap over ssl gets stuck after few curl requests using TLSv1.3 on JDK11

* OPENDJ-6377: Replication replay: issues with ReplaySynchronizer

* OPENDJ-6349: "RuntimeException: Should never happen" in HttpClientConnection

* OPENDJ-6240: DS not honoring per user resource limits when processing RESTful operation requests

* OPENDJ-6235: Stale ds-sync-hist attribute values reappear in the entry after replication is unconfigured

* OPENDJ-6222: SMTP messages are sometimes not encoded with the correct charset

* OPENDJ-6221: Logging for CONNECT operations are not saved in Nanosecond format

* OPENDJ-6196: HTTP connection handler continues to listen to 0.0.0.0 after setting listen-address

* OPENDJ-6188: Backend returns an incorrect error type when disk space hits low threshold

* OPENDJ-6173: cn=monitor memory pool stats do not get updated properly over time

* OPENDJ-6116: Unspecified Communications Error when multiple rest2ldap endpoints share configuration elements

* OPENDJ-5675: JDK11: supportextract tool cannot find jstack command

* OPENDJ-5664: JDK 11: illegal reflective access warning during import-ldif

* OPENDJ-5661: supportextract tool help and version options are different from other tools

* OPENDJ-5660: JDK 11: illegal reflective access warning on setup (with profile)

* OPENDJ-5611: Change number indexing can lag behind replication under extreme load

* OPENDJ-5590: Proxy: server discovery fails silently when proxy base-dn differs from backend's base-dn

* OPENDJ-5584: Server does not validate sum of memory used by JE backend caches in all cases

* OPENDJ-4764: REST2LDAP gateway sasl-plain authorization doesn't handle dn: correctly

* OPENDJ-4714: SSL handshake now sends 16KB list of CA issuer DNs

* OPENDJ-3121: Setup fails to create the lib/extensions directory in the instance.loc path, if a instance.loc file is used.

* OPENDJ-2605: Debian packages should be idempotent

* OPENDJ-1169: Exception/error lost when logging ERR\_LOOP\_REPLAYING\_OPERATION

* OPENDJ-640: Text Query Against indexed telephoneNumber Attribute Very Slow

## DS 6.5.0

* OPENDJ-5606: Upgrade to DS 6.0 fails if multiple filesystems are involved

* OPENDJ-5594: StackOverflowError with groupOfURLs when isMemberOf is requested

* OPENDJ-5582: LdapClientSocket connection leaked when handshake fails

* OPENDJ-5558: SDK: LdapUrl is not IPv6 clean

* OPENDJ-5553: Rest2Ldap cannot connect to TLSv1.2 servers

* OPENDJ-5496: DS fails to reconnect to an RS, disconnecting in handshake phase, after system restart

* OPENDJ-5481: ERR\_OPERATION\_NOT\_FOUND\_IN\_PENDING message used twice in different contexts

* OPENDJ-5406: Duplicate entry DNs if entry is deleted and then added during export-ldif or dsreplication initialize

* OPENDJ-5293: Proxy: Replication Service Discovery Mechanism logs WARNING

* OPENDJ-5272: "idle-time-limit" global configuration property has no effect

* OPENDJ-5210: Possible memory-leak if request received while bind in progress

* OPENDJ-5140: PersistentSearch heap usage grows

* OPENDJ-5137: Reading compressed or encrypted entries fails to close the InflaterInputStream

* OPENDJ-5115: ldappasswordmodify fails, NPE in PasswordPolicyState updatePasswordHistory

* OPENDJ-4967: Rest2ldap UndeliverableException occurs when a referenced entity cannot be fetched

* OPENDJ-4947: SASL DIGEST-MD5: bind request failed with protocol error

* OPENDJ-4881: Updates via Rest2ldap fail if record does not contain the necessary object class

* OPENDJ-4852: Backup with --backupAll misses a few backends

* OPENDJ-4625: Changelog range searches miss entries

* OPENDJ-4589: dsconfig --offline is not case-insensitive

* OPENDJ-4325: Changelog searches requesting changelogCookie are very slow

* OPENDJ-4229: status command with keystore options throws NullPointerException

* OPENDJ-3480: Updating schema backend properties while it is enabled leaves schema backend in broken state

* OPENDJ-3343: Invalid Conflict resolution on Add sequence when Parent & Child are added on different replica

* OPENDJ-3341: REST to LDAP gateway: HTTP response for API description is empty

* OPENDJ-3153: REST to LDAP gateway: changing password fails when using proxied authorization

* OPENDJ-2356: verify-index displays an inappropriate error message when run in online mode

---

---
title: Fixes in 8.1.x
description: Cumulative list of important fixes in PingDS 8.1.x maintenance releases.
component: pingds
version: release-notes
page_id: pingds::fixes-8.1
canonical_url: https://docs.pingidentity.com/pingds/release-notes/fixes-8.1.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-15T00:00:00Z
section_ids:
  ds_8_1_1: DS 8.1.1
  ds_8_1_0: DS 8.1.0
  ds_8_0_0: DS 8.0.0
  ds_7_5_0: DS 7.5.0
  ds_7_4_0: DS 7.4.0
  ds_7_3_0: DS 7.3.0
  ds_7_2_0: DS 7.2.0
  ds_7_1_0: DS 7.1.0
  ds_7_0_0: DS 7.0.0
  ds_6_5_0: DS 6.5.0
---

# Fixes in 8.1.x

This page lists the cumulative fixes in DS 8.1.x releases:

## DS 8.1.1

* OPENDJ-12283: Thread dumps are missing critical "nid" field

## DS 8.1.0

* OPENDJ-12025: Rotated access log filenames should use UTC not local time

* OPENDJ-11970: Worker threads stuck performing abandon or cancel operations

* OPENDJ-11763: Potential deadlock when processing bind requests and protocol errors on the RX LDAP connection handler

* OPENDJ-11706: In the middle of paged searches, DS can start returning entries from the first page

* OPENDJ-11667: DS accepts search requests presenting obviously invalid paging cookies

* OPENDJ-11536: NullPointerException in compressed schema

* OPENDJ-11486: Index processing failure: IndexOutOfBoundsException in EntryContainer.java when processing complex filters

* OPENDJ-11001: manage-tasks stuck after creating backup and backup purge

* OPENDJ-10547: The JSON Audit Access Logger records msgID but not operationID

* OPENDJ-10083: Creation of password validator fails if password-character-set:punct characters not surrounded by single quotes at command line

## DS 8.0.0

* OPENDJ-11280: OAuth2 token auth\_time field recorded in seconds instead of milliseconds causes very high DB contention

* OPENDJ-11243: Searches returning multiple attributes of the same OID use the last alias

* OPENDJ-11191: Upgrade fails in Windows environment if directory path contains spaces

* OPENDJ-11001: manage-tasks stuck after creating backup and backup purge

* OPENDJ-10912: DS rejects MODIFY requests with no modifications

* OPENDJ-10863: Very slow response when using debugsearchindex

* OPENDJ-10532: The case of a baseDN can be changed once replicated

* OPENDJ-10010: HTTP/HTTPS connection handler only creates one listener address when multiple addresses are specified

## DS 7.5.0

* OPENDJ-10306: Null pointer exceptions due to unrecognized (UNKNOWN) requests

* OPENDJ-10171: etag in schema config entry leads to schema violation error when attempting to update cn=schema

* OPENDJ-10139: Replication status "TOO\_LATE" does not mark DS as unhealthy

* OPENDJ-10131: ds-mon-receive-delay metric is not working

* OPENDJ-10078: Unable to use dsrepl initialize for cn=schema when 99-user.ldif only contains ds-sync-state entries

* OPENDJ-9913: Bind via REST API ignores force-change-on-add in password policy

## DS 7.4.0

* OPENDJ-9692: Unindexed privilege not enforced for unindexed sorted and paged searches

* OPENDJ-9680: Reduce Argon2 memory requirement

* OPENDJ-9544: Searches for attributes that do not exist in schema still take time

* OPENDJ-9524: create-rc-script: systemd service should run start-ds/stop-ds, and not write a wrapper init script

* OPENDJ-9507: Enable GSSAPI/Kerberos to use wildcard principal

* OPENDJ-8849: An isolated DS (no RS) should return UNAVAILABLE instead of UNWILLING\_TO\_PERFORM

* OPENDJ-8796: Virtual attribute providers ignore critical controls, such as VLV, paging, and sorting

* OPENDJ-8228: Updates for an entry in a replicated sub-suffix appear also in the changelog for its parent

## DS 7.3.0

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | An issue was discovered in the 7.3.0 release that has the potential to corrupt *static groups*. To ensure data integrity, upgrade to 7.3.1 or later. This issue affects the stability and reliability of static groups only. Continuing to use version 7.3.0 may lead to data corruption and other unintended consequences.DS version 7.3.1 and later include the necessary fixes; however if you deployed DS 7.3.0 with static groups, you must contact [support](https://www.pingidentity.com/en/support/support-center.html) for assistance with resolving the data corruption. |

* OPENDJ-9300: DS 7.3 upgrade requires a full index rebuild

* OPENDJ-9295: Search involving BigIndex throws NoSuchElementException

* OPENDJ-9272: Change number indexing state is logged too often

* OPENDJ-9250: The max-allowed-client-connections limit should not apply to the admin connector

* OPENDJ-9245: DS backup to an S3 bucket on a new region fails

* OPENDJ-9213: The dsconfig list-replication-domains output contains redundant columns

* OPENDJ-9204: RS ignores DS state and forwards changes DS has already seen

* OPENDJ-9200: Backup process logs incorrect number of jdb files

* OPENDJ-9183: Replicated request controls serialized in LDIF using V1 encoding

* OPENDJ-9182: NPE in changelogstat on encountering a modify DN request

* OPENDJ-9167: Reading isMemberOf after adding, deleting, or renaming a static group can block for a long time when there are many static groups

* OPENDJ-9102: Log rotation stops once the File Count Retention Policy count is met

* OPENDJ-9042: All worker threads blocked waiting for abandon operations to complete

* OPENDJ-9041: Undeliverable unexpected exception while performing an abandon operation during server shutdown

* OPENDJ-9033: DS refuses to start and throws an NPE when a subordinate-base-dn is used

* OPENDJ-9032: The dsrepl --script-friendly option was never implemented and should not appear in the tool

* OPENDJ-9020: Replicas should persist their ReplicaOfflineMsg unless they're being recovered from the replication server

* OPENDJ-9007: LoadBalancer availability check fails if the current bind user state is "bad"

* OPENDJ-9002: Changelogstat outputs verbose CSNs for offline messages, but not other messages

* OPENDJ-9000: Missing RS - RS heartbeats are not detected

* OPENDJ-8992: A replica rejoining the topology after its changelog is purged is not tested for the correct server state

* OPENDJ-8975: Modified file permissions for 99-user.ldif revert to 600 when DS is restarted

* OPENDJ-8917: ReplicationBroker.java swallowed important debugging info

* OPENDJ-8831: Log when and why the ChangeNumberIndexer cannot move forward

* OPENDJ-8815: dsrepl status does not take bad data status into account

* OPENDJ-8808: Potential deadlock between overlapping rename operations

* OPENDJ-8779: Improve replica and changelog logging

* OPENDJ-8378: dsrepl status shows deleted replication domains

* OPENDJ-8233: RS connection error reason is not logged when hostname is not resolvable

* OPENDJ-7942: The server ignores critical VLV request controls when falling back to an unindexed search

* OPENDJ-7941: Client connections to proxy are timed out after 10 seconds regardless of activity

* OPENDJ-7925: Searchrate does not retrieve data when used simultaneously with modrate on groups

* OPENDJ-7688: Spurious DS disconnections because of missing heartbeat

* OPENDJ-7640: Supportextract does not collect all security stores when several keystores have the same basename

* OPENDJ-7516: External cn=changelog is not updated while replication initialization is in progress

* OPENDJ-3409: Retention and rotation policies do not work with CAUD handlers

* OPENDJ-3057: Replication Server starts listener although ChangeLog DB is unusable

## DS 7.2.0

* OPENDJ-8874: Full replica purge should write CSN information right away

* OPENDJ-8829: Error messages incorrectly mentions cn=System,cn=monitor

* OPENDJ-8805: dsconfig exits when setting the "bootstrap-replication-server" property with a \<null> value in the "Replication Service Discovery Mechanism".

* OPENDJ-8792: SDK: Log SSL exceptions as errors instead of warnings

* OPENDJ-8778: Setup option --trustStorePassword:file behaves differently than --trustStorePasswordFile

* OPENDJ-8727: HTTP embedded listener throws IllegalStateException: Output channel is not set

* OPENDJ-8698: DS should write config archive files in a crash consistent way

* OPENDJ-8610: RS-RS session thread stuck in Session.send could prevent DS from shutdown

* OPENDJ-8548: Optimize scoping of indexed searches

* OPENDJ-8532: Error running export-ldif offline: "DatabaseConfig.setReadOnly() must be set to false when creating a Database"

* OPENDJ-8500: IllegalMonitorStateException after subtree read lock timeout when adding an entry

* OPENDJ-8473: Upgrade does not migrate ds-cfg-je-property values

* OPENDJ-8383: dsrepl status fails when certificates accepted interactively

* OPENDJ-8280: DS will not start when using a non US Locale after changing config

* OPENDJ-8254: dsbackup restore/list slow to complete with cloud storage

* OPENDJ-8243: Indexes could cause ldapsearch to return multiple copies of the same entry

* OPENDJ-8227: Deadlock between Changelog DB purger and Thread for RS session

* OPENDJ-8226: Support Extract tool ignores non-default changelogDb location when collecting domains.state file

* OPENDJ-8205: Log message lists an object's string representation instead of a file name

* OPENDJ-8137: LDIF backend silently rejects entries that fail schema validation

* OPENDJ-8115: -Djavax.net.ssl.trustStore=\<value> in OPENDJ\_JAVA\_ARGS throws NullPointerException

* OPENDJ-8090: am-identity-store:7.1 setup profile is not functional

* OPENDJ-8079: targattrsfilters expression does not work with 2 filters but permits 1 or more than 2 filters

* OPENDJ-8062: Possible inconsistent state after backup restore

* OPENDJ-8046: Changelog files are not closed after searching cn=changelog

* OPENDJ-8028: Prometheus monitoring doesn't work with Telegraf

* OPENDJ-8024: Prevent configuration of VLV indexes with scope base-object

* OPENDJ-8008: OutOfMemoryException in subtree delete

* OPENDJ-7991: makeldif: "invalid number of arguments" using DateTime tag with colons

* OPENDJ-7971: dsbackup fails when JDB file cleaned

* OPENDJ-7970: Ensure that DS is crash resilient for all runtime file changes

* OPENDJ-7889: Configuring group-id against DS-only instance requires restart for the change to be reported by monitoring

* OPENDJ-7818: Package based upgrade does not support instances running as non-root

* OPENDJ-7816: dsbackup fails when destination is a symbolic link to a real directory

* OPENDJ-7755: DS 7.0 replication with older version, CryptoManager failed to import the symmetric key entry

* OPENDJ-7744: dsrepl initialize in a topology with DS7 and DS 5.5 fails if DS7 serverId starts with 0

* OPENDJ-7596: dsbackup has global connection options that do not work with some subcommands

* OPENDJ-4935: Replication instability and divergence when using high latency disks

## DS 7.1.0

* OPENDJ-7928: JSON normalization cannot handle nested arrays

* OPENDJ-7905: Schema replication error after upgrade

* OPENDJ-7867: NPE if dsbackup bucket name contains underscores

* OPENDJ-7851: Supportextract tool: clobbers the server.out filehandle when kill -3 is used.

* OPENDJ-7847: StaticGroup's objectclass sanity checks are unhelpful

* OPENDJ-7810: JMX connections are always considered insecure

* OPENDJ-7761: DS sporadically hangs while reconnecting to an RS

* OPENDJ-7758: DS 7.0 dsrepl add-local-server-to-pre-7-0-topology: NPE if master-key is in different keystore

* OPENDJ-7747: ldapmodify display full stack exception on LDIF errors if connection is already established

* OPENDJ-7737: ConfigurationFramework#initialize0 changes the class loader without clearing the map of registered jar files

* OPENDJ-7699: Supportextract throws NoSuchElementException when the server.pid file is empty

* OPENDJ-7689: dsrepl add-local-server-to-pre-7-0-topology does not tolerate separate keystore and truststore

* OPENDJ-7687: Global Access Control Policy regarding cn=schema is too restrictive

* OPENDJ-7674: Migrating encrypted changelog files during upgrade fails

* OPENDJ-7655: Replaying multiple MODIFYDN operations is very slow

* OPENDJ-7612: replication divergence on CTS in the cloud

* OPENDJ-7599: Cannot add a pre-encoded password to an entry without an existing password

* OPENDJ-7554: Windows: Secrets not retrieved from :file command-line arguments

* OPENDJ-7523: Example plugin and example pwdscheme pom.xml are missing correct revision

* OPENDJ-7513: Missing subSchemaSubEntry attribute from rootDSE access controls

* OPENDJ-7481: JSON logs do not contain proxy auth DN

* OPENDJ-7474: Docker sample README.md provides wrong instructions for running the container

* OPENDJ-7450: The startswith (sw) operator on indexed JSON attribute is slow

## DS 7.0.0

* OPENDJ-7319: Addrate can run out of memory when --deleteMode off and --noPurge are set

* OPENDJ-7286: Changelog searches can start with incorrect cursors

* OPENDJ-7176: Filters with malformed attribute descriptions cannot be parsed

* OPENDJ-7115: DS does not start when deployed with ISTIO sidecar container in the GCP K8s cloud

* OPENDJ-7016: status command outputs malformed JSON in script friendly mode

* OPENDJ-6994: strict-format-country-string does not affect the server

* OPENDJ-6787: Changelog searches are extremely slow if any cursors are exhausted

* OPENDJ-6778: Proxy server mishandles abandon requests

* OPENDJ-6733: SMTP handler sends incorrect email when account status is modified by manually updating ds-pwp-account-disabled attribute

* OPENDJ-6711: Replication status reports The provided value "5277383431" could not be parsed as an integer.

* OPENDJ-6557: IDM Password Sync plugin induces 100% CPU in Apache Http Components when used with JDK 11

* OPENDJ-6540: The Supportextract hangs when loggers are configured to use /dev/stdout

* OPENDJ-6527: Server does not return password policy responses with only warnings

* OPENDJ-6521: setup checks admin port despite options --skipPortCheck --doNotStart

* OPENDJ-6512: Problems when work queue fills

* OPENDJ-6499: Query on rest2ldap over ssl gets stuck after few curl requests using TLSv1.3 on JDK11

* OPENDJ-6377: Replication replay: issues with ReplaySynchronizer

* OPENDJ-6349: "RuntimeException: Should never happen" in HttpClientConnection

* OPENDJ-6240: DS not honoring per user resource limits when processing RESTful operation requests

* OPENDJ-6235: Stale ds-sync-hist attribute values reappear in the entry after replication is unconfigured

* OPENDJ-6222: SMTP messages are sometimes not encoded with the correct charset

* OPENDJ-6221: Logging for CONNECT operations are not saved in Nanosecond format

* OPENDJ-6196: HTTP connection handler continues to listen to 0.0.0.0 after setting listen-address

* OPENDJ-6188: Backend returns an incorrect error type when disk space hits low threshold

* OPENDJ-6173: cn=monitor memory pool stats do not get updated properly over time

* OPENDJ-6116: Unspecified Communications Error when multiple rest2ldap endpoints share configuration elements

* OPENDJ-5675: JDK11: supportextract tool cannot find jstack command

* OPENDJ-5664: JDK 11: illegal reflective access warning during import-ldif

* OPENDJ-5661: supportextract tool help and version options are different from other tools

* OPENDJ-5660: JDK 11: illegal reflective access warning on setup (with profile)

* OPENDJ-5611: Change number indexing can lag behind replication under extreme load

* OPENDJ-5590: Proxy: server discovery fails silently when proxy base-dn differs from backend's base-dn

* OPENDJ-5584: Server does not validate sum of memory used by JE backend caches in all cases

* OPENDJ-4764: REST2LDAP gateway sasl-plain authorization doesn't handle dn: correctly

* OPENDJ-4714: SSL handshake now sends 16KB list of CA issuer DNs

* OPENDJ-3121: Setup fails to create the lib/extensions directory in the instance.loc path, if a instance.loc file is used.

* OPENDJ-2605: Debian packages should be idempotent

* OPENDJ-1169: Exception/error lost when logging ERR\_LOOP\_REPLAYING\_OPERATION

* OPENDJ-640: Text Query Against indexed telephoneNumber Attribute Very Slow

## DS 6.5.0

* OPENDJ-5606: Upgrade to DS 6.0 fails if multiple filesystems are involved

* OPENDJ-5594: StackOverflowError with groupOfURLs when isMemberOf is requested

* OPENDJ-5582: LdapClientSocket connection leaked when handshake fails

* OPENDJ-5558: SDK: LdapUrl is not IPv6 clean

* OPENDJ-5553: Rest2Ldap cannot connect to TLSv1.2 servers

* OPENDJ-5496: DS fails to reconnect to an RS, disconnecting in handshake phase, after system restart

* OPENDJ-5481: ERR\_OPERATION\_NOT\_FOUND\_IN\_PENDING message used twice in different contexts

* OPENDJ-5406: Duplicate entry DNs if entry is deleted and then added during export-ldif or dsreplication initialize

* OPENDJ-5293: Proxy: Replication Service Discovery Mechanism logs WARNING

* OPENDJ-5272: "idle-time-limit" global configuration property has no effect

* OPENDJ-5210: Possible memory-leak if request received while bind in progress

* OPENDJ-5140: PersistentSearch heap usage grows

* OPENDJ-5137: Reading compressed or encrypted entries fails to close the InflaterInputStream

* OPENDJ-5115: ldappasswordmodify fails, NPE in PasswordPolicyState updatePasswordHistory

* OPENDJ-4967: Rest2ldap UndeliverableException occurs when a referenced entity cannot be fetched

* OPENDJ-4947: SASL DIGEST-MD5: bind request failed with protocol error

* OPENDJ-4881: Updates via Rest2ldap fail if record does not contain the necessary object class

* OPENDJ-4852: Backup with --backupAll misses a few backends

* OPENDJ-4625: Changelog range searches miss entries

* OPENDJ-4589: dsconfig --offline is not case-insensitive

* OPENDJ-4325: Changelog searches requesting changelogCookie are very slow

* OPENDJ-4229: status command with keystore options throws NullPointerException

* OPENDJ-3480: Updating schema backend properties while it is enabled leaves schema backend in broken state

* OPENDJ-3343: Invalid Conflict resolution on Add sequence when Parent & Child are added on different replica

* OPENDJ-3341: REST to LDAP gateway: HTTP response for API description is empty

* OPENDJ-3153: REST to LDAP gateway: changing password fails when using proxied authorization

* OPENDJ-2356: verify-index displays an inappropriate error message when run in online mode

---

---
title: Getting support
description: Overview of Ping Identity support services, professional services, and documentation resources available for PingDS deployments.
component: pingds
version: release-notes
page_id: pingds::support
canonical_url: https://docs.pingidentity.com/pingds/release-notes/support.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-02-26T17:02:16Z
---

# Getting support

Ping Identity provides support services, professional services, training, and partner services to assist you in setting up and maintaining your deployments. Find a general overview of these services at <https://www.pingidentity.com>.

Ping Identity has staff members around the globe who support international customers and partners. Learn about Ping Identity's support offering at <https://www.pingidentity.com/support>.

Ping Identity publishes comprehensive documentation online:

* The Ping Identity [Knowledge Base](https://support.pingidentity.com/s/knowledge-base) offers a large and increasing number of up-to-date, practical articles that help you deploy and manage Ping Identity Platform software.

  While many articles are visible to everyone, Ping Identity customers have access to much more, including advanced information for customers using Ping Identity Platform software in a mission-critical capacity.

* Ping Identity product documentation, such as this document, aims to be technically accurate and complete with respect to the software documented. It is visible to everyone and covers all product features and examples of how to use them.

---

---
title: Incompatible changes
description: Lists incompatible changes in PingDS releases that require action when upgrading, including command syntax, protocol, and behavior differences.
component: pingds
version: release-notes
page_id: pingds::changes
canonical_url: https://docs.pingidentity.com/pingds/release-notes/changes.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-04-20T12:00:00Z
keywords: ["Compatibility", "LDAP"]
section_ids:
  changes-81: DS 8.1
  changes-80: DS 8.0
  changes-75: DS 7.5.2
  ds_7_5: DS 7.5
  changes-74: DS 7.4
  changes-73: DS 7.3
  changes-72: DS 7.2
  changes-71: DS 7.1
  changes-70: DS 7.0
  accounts: Accounts
  backup: Backup
  data: Data
  ldap: LDAP
  logging: Logging
  mail: Mail
  replication: Replication
  rest: REST
  security: Security
  setup: Setup
  tools: Tools
  upgrade: Upgrade
  security-defaults: Default security settings
  ds_6_5: DS 6.5
---

# Incompatible changes

## DS 8.1

* When rotating access log files, DS continues to add a timestamp as the rotation filename suffix.

  Previously, the timestamps reflected local time. The timestamps now reflect Coordinated Universal Time (UTC) instead and have a trailing `Z` as a timezone indicator. This change can cause an offset of several hours in the timestamps depending on your time zone. Newly rotated audit files can temporarily have timestamps earlier than existing files.

* Simplification of the `backendstat` command resulted in these changes:

  | Subcommand      | Change                                                                                                                                                                                           |
  | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  | `dump-index`    | Specify the base DN.The *-n \| --backendId* option was removed.Specify the index name as a trailing argument. The *-i \| --indexName* option was removed.                                        |
  | `dump-raw-db`   | Specify either the base DN or the backend ID.Use the backend ID to dump indexes not linked to base DN.Specify the database name as a trailing argument. The *-d \| --dbName* option was removed. |
  | `list-backends` | Subcommand removed.                                                                                                                                                                              |
  | `list-base-dns` | The output table now lists the base DNs and backends where they're defined.                                                                                                                      |
  | `list-indexes`  | Specify the base DN.The option to specify a backend ID was removed.                                                                                                                              |
  | `list-raw-dbs`  | No changes.                                                                                                                                                                                      |

* The `OPENDJ_JFR_ENABLED` environment variable to enable or disable the Java Flight Recorder for DS is now named `DS_JFR_ENABLED`.

## DS 8.0

* DS replicas using [change number indexing](https://docs.pingidentity.com/pingds/8/config-guide/changelog.html#ecl-configure-changenumber-indexer) to provide [Internet-Draft change numbers](https://docs.pingidentity.com/pingds/8/config-guide/changelog.html#ecl-legacy-format) now order change numbers *locally* on each server. The local change numbers follow the order in which replicated updates arrive.

  DS servers no longer order change numbers globally. The order likely differs from replica to replica.

  This reduces the number of potential problems the change number indexer faces, and so simplifies monitoring.

  Applications that need global consistency in the change log to fail over across replicas can continue to use or switch to [changelog cookies](https://docs.pingidentity.com/pingds/8/ldap-guide/change-notification.html#use-ecl).

* New DS servers now publish Prometheus metrics at `/metrics/prometheus/0.0.4` by default.

  The `0.0.4` path element reflects the content type version for the Prometheus [text-based format](https://prometheus.io/docs/instrumenting/exposition_formats/#text-based-format).

* The global property `max-psearches` sets a default limit of 100 total concurrent persistent searches.

  By default, the global property `max-psearches-policy` is set to `warn`. When it reaches the limit, DS accepts the incoming persistent search request and logs a warning message to the error log.

  If you set `max-psearches-policy: reject`, when it reaches the limit set by `max-psearches`, DS rejects incoming persistent search requests.

* HDAP now returns normalized field names by default.

  To return field names as specified with the `_fields` query parameter or as stored in the LDAP entry, set the HDAP endpoint configuration property `normalize-attribute-names:false` or the HDAP gateway configuration setting `"normalizeAttributeNames": false`.

* The `rebuild-index --rebuildDegraded` option is now `rebuild-index --rebuildUntrusted`.

  The `rebuild-index --clearDegradedState` option now does nothing. Since DS 7.5.0, DS servers no longer require rebuilding indexes for attributes that have never been used before.

  In addition, DS log messages now mention "trusted" and "untrusted" indexes rather than "degraded" indexes. If you scan log files for messages about degraded indexes, you must update them.

* The `setup-profile --instancePath` option is no longer supported.

  Set the instance path when using the `setup` command instead.

* The DS plugin API continues to evolve. This release brings many significant changes.

  Make sure you can build plugins built with earlier releases. Review the [Javadoc](https://docs.pingidentity.com/pingds/8/_attachments/javadoc/index.html) to understand how the API has changed.

* Setup profiles like the [user data profile](https://docs.pingidentity.com/pingds/8/install-guide/profile-user-data.html) have changed how they interpret relative paths to LDIF files.

  Previously, the path was either absolute or relative to the current directory. Now, the path is either absolute or relative to the directory where the profile is defined.

## DS 7.5.2

* DS 7.5.x no longer logs `debugsearchindex` information by default.

  If needed, use the boolean system property `org.forgerock.opendj.logDebugSearchIndex` to enable it:

  ```console
  $ OPENDJ_JAVA_ARGS="-Dorg.forgerock.opendj.logDebugSearchIndex=true" start-ds
  ```

## DS 7.5

The following changes affect the evolving DS plugin API:

| Class or interface                                                                                                                               | Changes                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `PluginOperation`                                                                                                                                | Added:- `getRequest()`

  You can also now use `getRequest().getRequestType()`.

- `hasPrivilege()`Removed:- `getOperationType()`

- `removeAttachment(String name)`                                                                               |
| `PreParseOperation` `PreOperationOperation`                                                                                                      | Added:- `sendResponses(ResponseStream responses)` for sending intermediate responses.

  The APIs were removed from the `ClientConnection` class.                                                                                                  |
| `ClientConnection`                                                                                                                               | This class has a volatile API and will very likely be subject to significant changes in future releases.Many methods were added and removed.                                                                                                       |
| `InProgressSearchOperation` `PostOperationSearchOperation` `PostResponseSearchOperation` `PreOperationSearchOperation` `PreParseSearchOperation` | To access resource limits, change your code from:```java
int sizelimit = getSizeLimit();
int timelimit = getTimeLimit();
```To:```java
int sizelimit = getResourceLimits().getSizeLimit();
int timelimit = getResourceLimits().getTimeLimit();
``` |

## DS 7.4

* You can upgrade DS 6.0 and later servers directly to DS 7.4.

  When starting from 5.5.x and earlier, *first upgrade all servers to DS 6.5* before upgrading further. Direct upgrade from versions earlier than 6.0 is no longer supported.

* For new DS servers, the `setup` command no longer enables support for changelog change numbers or change number indexing by default.

  For new servers, the replication server configuration property is `changelog-enabled: enabled-cookie-mode-only` by default, meaning client applications must use cookies instead of change numbers when searching the changelog. For examples, refer to [Use the external change log](https://docs.pingidentity.com/pingds/7.4/ldap-guide/change-notification.html#use-ecl).

  When you upgrade an existing server in place, the `upgrade` command keeps the existing server behavior.

* The documentation describes the new HDAP APIs for HTTP access.

  For documentation covering REST to LDAP, refer to [Use REST/HTTP](https://docs.pingidentity.com/pingds/7.3/rest-guide/preface.html) for 7.3.

* The log publisher properties `default-severity` and `override-severity` now take single values.

  Set them to the lowest severity level to log.

* The `create-rc-script` option `-f|--outputFile` has been removed.

  Use `-r|--rcScript /etc/init.d/opendj` or `-s|--systemdService /etc/systemd/system/opendj.service` instead.

* The configuration property `big-index-matching-rule` has changed to `big-index-extensible-matching-rule`.

  When creating a `big-extensible` index, you must set at least one `big-index-extensible-matching-rule`.

* The configuration property `log-control-oids` has changed to `log-controls` and is `true` by default for new servers.

* DS servers no longer return replication conflict entries by default.

  Use the manage DSAIT LDAP control to access them.

## DS 7.3

* New DS servers now write replication messages to the server error log (default: `opendj/logs/errors`).

* Metrics formerly under `cn=entry cache,cn=monitor` have moved under `cn=entry caches,cn=monitor`.

## DS 7.2

* The *deployment key* described in earlier DS 7 releases has been renamed *deployment ID*:

  * A deployment ID is not a cryptographic key or digital certificate.

  * A deployment ID does uniquely identify a DS deployment.

  The change affects the commands and the documentation:

  | Old option                | New option               |
  | ------------------------- | ------------------------ |
  | `--deploymentKey`         | `--deploymentId`         |
  | `--deploymentKeyPassword` | `--deploymentIdPassword` |

  The name change does not affect the deployment IDs (formerly keys) themselves. You can continue to use existing IDs (keys) in your deployments.

* The `setup` command now requires a `--deploymentId` option.

  Before running `setup` for the first time, generate a deployment ID as shown throughout the documentation:

  ```bash
  $ /path/to/opendj/bin/dskeymgr create-deployment-id --deploymentIdPassword password
  <deployment-id>
  $ export DEPLOYMENT_ID=<deployment-id>
  ```

* As a side effect of the change to allow `mail` addresses to include UTF-8 characters, DS no longer supports zero-length `mail` addresses.

  If you can't prevent applications from adding zero-length `mail` addresses and no addresses use UTF-8, set the advanced core schema property `allow-zero-length-values-directory-string` to `true`.

* The following changes affect proxy backend configurations:

  | Old Property                       | New Property                        |
  | ---------------------------------- | ----------------------------------- |
  | `heartbeat-interval`               | `keep-alive-interval`               |
  | `heartbeat-search-request-base-dn` | `keep-alive-search-request-base-dn` |

* The `lookthrough-limit` setting has been removed. Use `time-limit` instead.

  DS servers now enforce `time-limit` and `ds-rlimit-time-limit` settings while evaluating the entries to return for a search, rather than enforcing time limits only when sending entries.

  DS servers now ignore the `ds-rlim-lookthrough-limit` setting.

* The global advanced setting, `cursor-entry-limit`, has been replaced by a `max-candidate-set-size` setting, which corresponds to the maximum number of candidate entries that DS servers maintain in memory when querying attribute indexes.

* The `dsbackup` command no longer supports specifying options before the subcommand.

  You must now put all options after the subcommand, as has always been indicated in the documentation.

## DS 7.1

* With the introduction of the global configuration property, `group-id-failover-order`, which takes a comma-separated list of group IDs, commas are no longer permitted in group IDs.

  The `upgrade` command replaces each `,` with a `.` in group IDs.

* The following changes affect proxy backend configurations:

  | Old Property                        | New Property                   | Notes                                                                                                                                   |
  | ----------------------------------- | ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
  | `load-balancing-algorithm`          | None                           | All proxy backends now use affinity load balancing. As a result, they always route requests with the same target DN to the same server. |
  | `bind-connection-pool-idle-timeout` | `connection-pool-idle-timeout` | DS proxy backends no longer use shared connection pools.                                                                                |
  | `bind-connection-pool-max-size`     | `connection-pool-max-size`     |                                                                                                                                         |
  | `bind-connection-pool-min-size`     | `connection-pool-min-size`     |                                                                                                                                         |
  | `request-connection-pool-size`      | None                           |                                                                                                                                         |

* When using the `dskeymgr` command to generate a PEM format certificate, you can no longer use the `--alias` option. The PEM format does not support aliases.

  If you do use the `--alias` and `--outputFile` options together, the command now displays an error message:

  ```
  You may not provide both the --outputFile and the --alias arguments
  ```

## DS 7.0

### Accounts

* The default directory superuser (Directory Manager) DN is now `uid=admin` for new servers.

  The upgrade process does not change the directory superuser DN for existing servers.

  This change makes it easier to manage the server configuration over REST, as the default identity mapper configuration maps the HTTP `admin` username to the LDAP DN `uid=admin`.

* The replication service discovery mechanism now obtains some information by reading the `cn=monitor` LDAP entry. As a result, the `bind-dn` account must now have the `monitor-read` privilege.

  This affects accounts used by DS directory proxy servers to bind to DS replication servers. For an example showing the account with the `monitor-read` privilege, refer to *Try DS directory proxy*.

### Backup

* DS backups taken with this release are not compatible with backups from earlier releases.

* Scheduled backup tasks continue after upgrade.

* Tasks created with the `restore` command in earlier releases are removed during upgrade.

### Data

The default backend ID for application data depends on the setup profiles.

The upgrade process does not change the backend ID for existing servers.

### LDAP

When matching strings in attributes with telephone number syntax, DS servers now behave as follows:

* As in previous versions, a search for `"(telephoneNumber=1555123456)"` matches entries with telephone number values `+1 555 123 456` and `1 555 123456`.

* All `+` characters are ignored.

  In other words, `+` is no longer significant when matching a telephone number syntax attribute.

* A search for `"(telephoneNumber=*Flower*)"` returns only entries with telephone numbers containing `Flower` (case-insensitive match).

* A search for `"(telephoneNumber=15550102)"` no longer matches entries with telephone numbers like `+15550102 - Home`.

### Logging

* The `batch` configuration for the JMS common audit handler for access logs has changed to support reconnection if the broker becomes unavailable.

  This change adds a `batch.writeInterval` setting. It removes the following settings:

  * `batch.batchEnabled`

  * `batch.insertTimeoutSec`

  * `batch.pollTimeoutSec`

  * `batch.shutdownTimeoutSec`

  * `batch.threadCount`

* The example JDBC audit handler configuration for logging to MySQL has changed.

  The old configuration is not compatible with MySQL 8, supported in DS 7.

### Mail

The global property `smtp-server` has been replaced with a configuration object, *mail server*.

### Replication

* The `group-id` and `server-id` identifiers are now global settings, and only take a single value per server.

  Replication domain and replication server configurations no longer have mutable `server-id` and `group-id` properties.

* The external changelog domain configuration has moved to the replication domain and replication server configurations.

  This affects the following properties:

  * `ecl-include`

  * `ecl-include-for-deletes`

  * `changelog-enabled-excluded-domains`

* The following replication domain configuration properties have moved to the replication synchronization provider:

  * `changetime-heartbeat-interval`

  * `isolation-policy`

  * `heartbeat-interval`

  * `initialization-window-size`

  * `log-changenumber`

  * `referrals-url`

  * `solve-conflicts`

  * `source-address`

* The following replication server properties have moved to the replication synchronization provider:

  * `replication-purge-delay`

  * `source-address`

* In addition to the property changes, the replication synchronization provider has changed:

  * A new property, `bootstrap-replication-server`, takes the addresses of one or more replication servers this server should contact to discover the rest of the topology.

  * The `replication-purge-delay` property has replaced the replication domain property, `conflicts-historical-purge-delay`.

    In this release, the `replication-purge-delay` setting alone governs how long the replica retains data in the changelog and historical metadata necessary to solve conflicts in directory entries.

### REST

* The `resourceTypeProperty` field is no longer used in REST to LDAP configurations. The resource type is now inferred from the property with `"type": "resourceType"`.

### Security

* Default security settings have been hardened.

  For details, refer to [Default security settings](#security-defaults).

* The following configuration changes impact TLS-related settings:

  The Crypto Manager no longer has the following properties:

  * `ssl-cert-nickname`

  * `ssl-cipher-suite`

  * `ssl-encryption`

  * `ssl-protocol`

  The replication synchronization provider configuration object now has the following properties:

  * `key-manager-provider`

  * `ssl-cert-nickname`

  * `ssl-cipher-suite`

  * `ssl-encryption`

  * `ssl-protocol`

  * `trust-manager-provider`

  The following configuration objects now have `ssl-cipher-suite` and `ssl-protocol` properties:

  * HTTP OAuth2 OpenAM authorization mechanism

  * HTTP OAuth2 token introspection (RFC 7662) authorization mechanism

  * Replication service discovery mechanism

  * Static service discovery mechanism

* The default fingerprint algorithm for the fingerprint certificate mapper is now SHA-256.

### Setup

The `setup` command has changed:

* The `--productionMode` option has been removed.

  Default settings are now secure. For details, refer to [Default security settings](#security-defaults).

  The evaluation setup profile is compatible with other setup profiles. However, if you apply the evaluation setup profile last, it sets `unauthenticated-requests-policy:allow`, granting global permission to perform operations over insecure connections.

* Subcommands have been replaced by setup profiles.

* The `setup` command no longer starts the server by default.

  Before starting your new DS server, finish configuration.

  If no further configuration is required, use the `setup --start` option.

* For new servers, key pairs with self-signed certificates are no longer used. Instead, the setup process generates keys used for secure connections, and derives a shared master key to protect secret keys for data encryption. These keys depend on a deployment ID and deployment ID password.

  The deployment ID and deployment ID password are required as part of the setup process:

  * If you don't provide your own keys, the generated keys and the signing CA certificate are stored in a PKCS#12 keystore file, `config/keystore`.

    The password is stored in a PIN file, `config/keystore.pin`.

    You can use the CA certificate as the root of trust for an entire deployment.

  * By default, replication now relies on the same key pairs as all other connection handlers to secure network communications.

    The `Replication Key Manager` and `Replication Trust Manager` providers now point to the providers chosen during the setup process.

  * The `Default Key Manager` is now named after its keystore format, such as `PKCS12`.

* The following `setup` command options have been removed:

  * `-a, --addBaseEntry`

  * `-b, --baseDn`

  * `--useJvmTrustStore`

  * `-l, --ldifFile`

  * `-O, --doNotStart`

  * `--productionMode`

  * `-R, --rejectFile`

  * `--skipFile`

  Add your initial data before starting the server by creating a backend database, configuring indexes, and importing from LDIF.

* The `-d, --sampleData` option has moved. It is now provided as the `generatedUsers` parameter of the `ds-evaluation` setup profile.

### Tools

* DS command line tools no longer support the `-w -` and `--bindPassword -` options to prompt interactively for a password.

  Instead, provide the bind DN and omit the `-w -` or `--bindPassword -` option. The tools then prompt for a password unless you specify the `--no-prompt` option.

### Upgrade

You can upgrade DS 3.0 and later servers directly to DS 7.

When starting from 2.6, *first upgrade all servers to DS 6.5* before upgrading further. Direct upgrade from 2.6 is no longer supported.

### Default security settings

When you set up new DS servers, they are now configured with tighter security settings by default. These changes don't affect DS servers that you upgrade from earlier versions. If you require more lenient settings for compatibility, you must configure them after setting up the server:

* All operations except bind requests and StartTLS requests, and base object searches on the root DSE, require secure connections.

  This behavior is governed by the global configuration property, `unauthenticated-requests-policy`, which is now set to `allow-discovery`, instead of `allow`, unless the last setup profile applied is the `ds-evaluation` profile.

* The password storage scheme for the Default Password Policy and Root Password Policy is now `PBKDF2-HMAC-SHA256` with 10 iterations. For stronger security, raise the number of iterations, and require users to change their passwords.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | `PBKDF2-HMAC-SHA256` is a computationally intensive one-way hashing scheme. When used with a high number of iterations, *it is intentionally orders of magnitude slower* than the previous default for user passwords, which was `Salted SHA-512`.`PBKDF2-HMAC-SHA256` and similar computationally intensive password storage schemes lower throughput and raise response times for some operations, including the following:- Importing plaintext passwords from LDIF; for example, during evaluation and testing with generated data.

  - Updating passwords.

  - Authenticating with passwords. |

  To migrate user passwords to a new storage scheme, refer to *Password storage*.

* SASL mechanism handler configurations for `CRAM-MD5` and `DIGEST-MD5` are no longer present in the default configuration.

* Password storage scheme configurations for `MD5`, `RC4`, and `Salted MD5` are no longer present in the default configuration.

  Less secure and reversible password storage schemes have been disabled in the default configuration. You must therefore enable these password storage schemes if you intend to use them.

  | Setting                                 | New Default                             |
  | --------------------------------------- | --------------------------------------- |
  | Crypto Manager                          | `SHA-256`                               |
  | Crypto Manager                          | `RSA/ECB/OAEPWITHSHA-256ANDMGF1PADDING` |
  | Crypto Manager                          | `HmacSHA256`                            |
  | Global setting                          | `allow-discovery`                       |
  | Password storage scheme: 3DES           | `false`                                 |
  | Password storage scheme: AES            | `false`                                 |
  | Password storage scheme: Base64         | `false`                                 |
  | Password storage scheme: Blowfish       | `false`                                 |
  | Password storage scheme: Clear          | `false`                                 |
  | Password storage scheme: CRYPT          | `false`                                 |
  | Password storage scheme: PBKDF2         | `false`                                 |
  | Password storage scheme: PKCS5S2        | `false`                                 |
  | Password storage scheme: Salted SHA-1   | `false`                                 |
  | Password storage scheme: Salted SHA-256 | `false`                                 |
  | Password storage scheme: Salted SHA-384 | `false`                                 |
  | Password storage scheme: Salted SHA-512 | `false`                                 |
  | Password storage scheme: SHA-1          | `false`                                 |
  | Pluggable (JE) backend                  | `AES/GCM/NoPadding`                     |
  | Replication server                      | `AES/GCM/NoPadding`                     |

## DS 6.5

* There is an issue when running an upgrade from DS 6.5.0 to 6.5.1. If you did not set the `je-backend-shared-cache-enabled` property and accepted the default value of `true` before the upgrade, the value changes *AFTER* upgrade to `false`. You may have to reset this value to `true` for your deployments.

  If you set the `je-backend-shared-cache-enabled` property before upgrade to either `true` or `false`, the value does not change after upgrade.

* The `status` command has been rewritten, with the following notable changes:

  * The command is no longer interactive.

  * You must supply the required options when invoking the status command.

  * The command now has an `--offline` option.

  * When you run status `--offline` on a running server, the command only displays a portion of the available information.

  * You can now run the command against a remote DS server version 6 or later.

  * The output shows more information than before.

* The `dsreplication status` command no longer shows metrics for `M.C.` (missing changes) and `A.O.M.C.` (age of oldest missing change). Instead, it shows the replication delay.

  For DS 6 and later servers that expose a replication delay metric, the command shows the delay value. For DS 5.5 and earlier servers, the command shows `N/A`.

* The `db/admin` backend has been renamed `db/adminRoot`.

* The global server configuration property, `reject-unauthenticated-requests`, a boolean, has been removed and replaced with the property, `unauthenticated-requests-policy`. The new property can be set to the following values:

  * `reject`

    Same behavior as `reject-unauthenticated-requests:true`

  * `allow`

    Same behavior as `reject-unauthenticated-requests:false`

  * `allow-discovery`

    Like `reject`, but allows unauthenticated base object searches of the root DSE

* The proxy backend configuration property `service-discovery-mechanism` has been renamed `shard`.

* The `encode-password` command now displays the encoded password without additional characters.

  In other words, the output is now `{scheme}encoded-password` rather than `Encoded Password: "{scheme}encoded-password"`.

---

---
title: Interface stability
description: Describes PingDS interface stability classifications, including which APIs, commands, log messages, and configuration are Evolving or Internal.
component: pingds
version: release-notes
page_id: pingds::stability
canonical_url: https://docs.pingidentity.com/pingds/release-notes/stability.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-11-03T13:32:20Z
keywords: ["Compatibility", "LDAP"]
section_ids:
  release-levels: Product release levels
  interface-stability: Product stability labels
---

# Interface stability

Interfaces labeled as *Evolving* and *Technology Preview* in the documentation may change without warning. In addition, the following rules apply:

* All Java APIs are Evolving, except `com.*` packages, which are *Internal/Undocumented*.

* The class `org.forgerock.opendj.ldap.CoreMessages` is *Internal*.

* Text in log messages is *Internal*. Log message IDs are *Evolving*.

* The default content of `cn=schema` (LDAP schema) is *Evolving*.

* The interfaces of the `backendstat` and `changelogstat` commands are *Evolving*.

* Interfaces that aren't described in released product documentation are *Internal/Undocumented*.

  For example, the LDIF representation of the server configuration, `config.ldif`, is *Internal*.

* Learn more in [Deprecated](deprecation.html) and [Removed](removed.html).

## Product release levels

Ping Identity defines Major, Minor, Maintenance, and Patch product release levels. The version number reflects release level. The release level tells you what sort of compatibility changes to expect.

**Release level definitions**

| Release Label      | Version Numbers                                               | Characteristics                                                                                                                                                                                                                                                                                                                  |
| ------------------ | ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Major              | Version: x\[.0.0] (trailing 0s are optional)                  | * Bring major new features, minor features, and bug fixes.

* Can include changes even to Stable interfaces.

* Can remove previously Deprecated functionality, and in rare cases, remove Evolving functionality that has not been explicitly Deprecated.

* Include changes present in previous Minor and Maintenance releases. |
| Minor              | Version: x.y\[.0] (trailing 0s are optional)                  | - Bring minor features, and bug fixes.

- Can include backwards-compatible changes to Stable interfaces in the same Major release, and incompatible changes to Evolving interfaces.

- Can remove previously Deprecated functionality.

- Include changes present in previous Minor and Maintenance releases.                    |
| Maintenance, Patch | Version: x.y.z\[.p]The optional *p* reflects a Patch version. | * Bring bug fixes

* Are intended to be fully compatible with previous versions from the same Minor release.                                                                                                                                                                                                                     |

## Product stability labels

Ping Identity Platform software supports many features, protocols, APIs, GUIs, and command-line interfaces. Some of these are standard and have long been stable. Others offer new functionality that is continuing to evolve.

Ping Identity acknowledges you invest in these features and interfaces and so need to understand when they are expected to change. For that reason, Ping Identity Platform products use the following stability labels.

**Stability label definitions**

| Stability Label       | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Stable                | This documented feature or interface is expected to undergo backwards-compatible changes only for major releases.Changes may be announced at least one minor release before they take effect.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Evolving              | This documented feature or interface is continuing to evolve and so is expected to change, potentially in backwards-incompatible ways even in a minor release. Changes are documented at the time of product release.While new protocols and APIs are still in the process of standardization, they are Evolving. This applies, for example, to recent Internet-Draft implementations and to newly developed functionality.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Legacy                | This feature or interface has been replaced with an improved version, and is no longer receiving development effort from Ping Identity.You should migrate to the newer version, however the existing functionality will remain.Legacy features or interfaces will be marked as *Deprecated* if they are scheduled to be removed from the product.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Deprecated            | This feature or interface is deprecated, and likely to be removed in a future release.For previously stable features or interfaces, the change was likely announced in a previous release.Deprecated features or interfaces will be removed from Ping Identity products.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Removed               | This feature or interface was deprecated in a previous release, and has now been removed from the product.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Technology Preview    | Technology previews provide access to new features that are considered as new technology that is not yet supported. Technology preview features may be functionally incomplete, and the function as implemented is subject to change without notice.*DON'T DEPLOY A TECHNOLOGY PREVIEW INTO A PRODUCTION ENVIRONMENT.*Customers are encouraged to test drive the technology preview features in a non-production environment, and are welcome to make comments and suggestions about the features in the associated forums.Ping Identity does not guarantee that a technology preview feature will be present in future releases, the final complete version of the feature is liable to change between preview and the final version. Once a technology preview moves into the completed version, said feature will become part of Ping Identity Platform.Technology previews are provided on an "AS-IS" basis for evaluation purposes only, and Ping Identity accepts no liability or obligations for the use thereof. |
| Internal/Undocumented | Internal and undocumented features or interfaces can change without notice.If you depend on one of these features or interfaces, contact support to discuss your needs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

---

---
title: Known issues
description: Lists known issues open at the time of each PingDS release, including Java version incompatibilities and other unresolved defects.
component: pingds
version: release-notes
page_id: pingds::known-issues
canonical_url: https://docs.pingidentity.com/pingds/release-notes/known-issues.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-07-07T12:00:00Z
keywords: ["LDAP", "Upgrade"]
section_ids:
  known-issues-81: DS 8.1.1
  known-issues-80: DS 8.0.4
  known-issues-75: DS 7.5.4
  known-issues-74: DS 7.4.4
  known-issues-73: DS 7.3.6
  known-issues-72: DS 7.2.5
  known-issues-71: DS 7.1.8
  known-issues-70: DS 7.0.2
  ds_6_5_6: DS 6.5.6
---

# Known issues

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Due to a change to the Java platform between versions 11 and 17, the keys you generate with the `dskeymgr` and `setup` commands using Java 11 are incompatible with keys generated using Java 17 and later.Using different Java versions is a problem if you use deployment ID-based CA certificates. Replication breaks, for example, when you use the `setup` command for a new server with a more recent version of Java than was used to set up existing servers.Learn how to resolve the issue in [Incompatible Java versions](https://docs.pingidentity.com/pingds/8.1/maintenance-guide/troubleshooting.html#troubleshoot-incompatible-java-versions). |

The following important issues remained open at the time of the latest release for each version.

## DS 8.1.1

| Issue ID     | Summary                                                                                | Status |
| ------------ | -------------------------------------------------------------------------------------- | ------ |
| OPENDJ-12427 | Scrypt password storage rehash-policy:always causes user binds to fail                 | Open   |
| OPENDJ-12257 | dsconfig --batch and --batchfile don't strip whitespace after backslash before newline | Open   |
| OPENDJ-11821 | JE exceptions under high modification load with Java 25.0.2                            | Open   |

## DS 8.0.4

No known issues at the time of release.

## DS 7.5.4

| Issue ID     | Summary                                                                                                    | Status1               |
| ------------ | ---------------------------------------------------------------------------------------------------------- | --------------------- |
| OPENDJ-11486 | Index processing failure: IndexOutOfBoundsException in EntryContainer.java when processing complex filters | Fixed in 8.0.1, 8.1.0 |
| OPENDJ-11191 | Upgrade fails in Windows environment if directory path contains spaces                                     | Fixed in 8.0.0        |
| OPENDJ-11001 | manage-tasks stuck after creating backup and backup purge                                                  | Fixed in 8.0.0, 8.1.0 |

1 Upgrade to the listed version or later to get the fix.

## DS 7.4.4

| Issue ID     | Summary                                                                                                                         | Status1               |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| OPENDJ-10674 | Dynamic groups not initialized after restart in platform deployment                                                             | Fixed in 7.5.2, 8.0.0 |
| OPENDJ-10083 | Creation of password validator fails if password-character-set:punct characters not surrounded by single quotes at command line | Open                  |
| OPENDJ-10010 | HTTP/HTTPS connection handler only creates one listener address when multiple addresses are specified                           | Fixed in 8.0.0        |
| OPENDJ-9812  | Schema updates are not crash resilient                                                                                          | Open                  |
| OPENDJ-8093  | Stale replica information returned from cn=monitor                                                                              | Open                  |

1 Upgrade to the listed version or later to get the fix.

## DS 7.3.6

| Issue ID     | Summary                                                                                            | Status1        |
| ------------ | -------------------------------------------------------------------------------------------------- | -------------- |
| OPENDJ-10532 | The case of a baseDN can be changed once replicated                                                | Fixed in 7.5.2 |
| OPENDJ-10171 | etag in schema config entry leads to schema violation error when attempting to update cn=schema    | Fixed in 7.5.0 |
| OPENDJ-9913  | Bind via REST API ignores force-change-on-add in password policy                                   | Fixed in 7.5.0 |
| OPENDJ-9812  | Schema updates are not crash resilient                                                             | Open           |
| OPENDJ-9544  | Searches for attributes that do not exist in schema still take time                                | Fixed in 7.4.0 |
| OPENDJ-9524  | create-rc-script: systemd service should run start-ds/stop-ds, and not write a wrapper init script | Fixed in 7.4.0 |
| OPENDJ-9268  | Cannot store zero-length mail attribute values                                                     | Open           |
| OPENDJ-8093  | Stale replica information returned from cn=monitor                                                 | Open           |

1 Upgrade to the listed version or later to get the fix.

## DS 7.2.5

| Issue ID     | Summary                                                                                                                           | Status1               |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| OPENDJ-10010 | HTTP/HTTPS connection handler only creates one listener address when multiple addresses are specified                             | Fixed in 8.0.0        |
| OPENDJ-9790  | Cannot create GeneralizedTimes with large fractional values                                                                       | Fixed in 7.3.3, 7.4.0 |
| OPENDJ-9379  | Restoring a backup fails if the 02-config.ldif schema file is missing                                                             | Open                  |
| OPENDJ-9369  | RxCachedThreadScheduler threads increase over time                                                                                | Open                  |
| OPENDJ-9300  | DS 7.3 upgrade requires a full index rebuild                                                                                      | Fixed in 7.3.0        |
| OPENDJ-9268  | Cannot store zero-length mail attribute values                                                                                    | Open                  |
| OPENDJ-9250  | The max-allowed-client-connections limit should not apply to the admin connector                                                  | Fixed in 7.3.0        |
| OPENDJ-9213  | The dsconfig list-replication-domains output contains redundant columns                                                           | Fixed in 7.3.0        |
| OPENDJ-9167  | Reading isMemberOf after adding, deleting, or renaming a static group can block for a long time when there are many static groups | Fixed in 7.3.0        |
| OPENDJ-9128  | Entry cache and group manager use too much memory                                                                                 | Fixed in 7.3.0        |
| OPENDJ-9000  | Missing RS - RS heartbeats are not detected                                                                                       | Fixed in 7.3.0        |
| OPENDJ-8849  | An isolated DS (no RS) should return UNAVAILABLE instead of UNWILLING\_TO\_PERFORM                                                | Fixed in 7.4.0        |
| OPENDJ-8233  | RS connection error reason is not logged when hostname is not resolvable                                                          | Fixed in 7.3.0        |
| OPENDJ-8093  | Stale replica information returned from cn=monitor                                                                                | Open                  |
| OPENDJ-7925  | The searchrate tool does not retrieve data when used simultaneously with the modrate tool on groups                               | Fixed in 7.3.0        |
| OPENDJ-7844  | Difficult to override standard LDAP schema defined in 00-core.ldif                                                                | Open                  |
| OPENDJ-7763  | Proxy service discovery with RS-only and DS-only seems not to route search                                                        | Open                  |
| OPENDJ-7743  | Setting DN-valued properties to a config expression causes startup to fail                                                        | Open                  |
| OPENDJ-7741  | dsrepl add-local-server-to-pre-7-0-topology requires a base DN for an RS                                                          | Open                  |
| OPENDJ-7219  | PreParseAddOperation cannot remove attributes                                                                                     | Open                  |
| OPENDJ-6579  | Schema is not populated to remote instances if added before enabling replication                                                  | Open                  |
| OPENDJ-6468  | ds-mon-\* Prometheus metrics are labeled as gauge but seem to be counters                                                         | Open                  |
| OPENDJ-6022  | PTA to Active Directory returns more than one entry when only one exists                                                          | Open                  |
| OPENDJ-3409  | Retention and rotation policies do not work with CAUD handlers                                                                    | Fixed in 7.3.0        |

1 Upgrade to the listed version or later to get the fix.

## DS 7.1.8

| Issue ID     | Summary                                                                                                                                        | Status1                      |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| OPENDJ-10553 | DN syntax does not perform strict enforcement of country codes in RDNs if enabled                                                              | Open                         |
| OPENDJ-10532 | The case of a baseDN can be changed once replicated                                                                                            | Fixed in 8.0.0               |
| OPENDJ-9790  | Cannot create GeneralizedTimes with large fractional values                                                                                    | Fixed in 7.3.3, 7.4.0        |
| OPENDJ-9250  | The max-allowed-client-connections limit should not apply to the admin connector                                                               | Fixed in 7.3.0               |
| OPENDJ-9213  | The dsconfig list-replication-domains output contains redundant columns                                                                        | Fixed in 7.3.0               |
| OPENDJ-9200  | Backup process logs incorrect number of jdb files                                                                                              | Fixed in 7.2.3, 7.3.0        |
| OPENDJ-9158  | AM User/CTS affinity failover doesn't happen when DS's disk volume is detached                                                                 | Fixed in 7.2.3, 7.3.3, 7.4.0 |
| OPENDJ-9033  | DS refuses to start and throws an NPE when a subordinate-base-dn is used                                                                       | Fixed in 7.2.1, 7.3.0        |
| OPENDJ-8917  | ReplicationBroker.java swallowed important debugging info                                                                                      | Fixed in 7.2.1, 7.3.0        |
| OPENDJ-8870  | RFC2307bis schema is different from the internet-draft                                                                                         | Fixed in 7.2.0               |
| OPENDJ-8831  | Log when and why the ChangeNumberIndexer cannot move forward                                                                                   | Fixed in 7.2.1, 7.3.0        |
| OPENDJ-8829  | Error messages incorrectly mentions cn=System,cn=monitor                                                                                       | Fixed in 7.2.0               |
| OPENDJ-8808  | Potential deadlock between overlapping rename operations                                                                                       | Fixed in 7.2.1, 7.3.0        |
| OPENDJ-8805  | dsconfig exits when setting the "bootstrap-replication-server" property with a \<null> value in the "Replication Service Discovery Mechanism". | Fixed in 7.2.0               |
| OPENDJ-8778  | Setup option --trustStorePassword:file behaves differently than --trustStorePasswordFile                                                       | Fixed in 7.2.0               |
| OPENDJ-8473  | Upgrade does not migrate ds-cfg-je-property values                                                                                             | Fixed in 7.2.0               |
| OPENDJ-8280  | DS will not start when using a non-US locale after changing config                                                                             | Fixed in 7.2.0               |
| OPENDJ-8233  | RS connection error reason is not logged when hostname is not resolvable                                                                       | Fixed in 7.3.0               |
| OPENDJ-8093  | Stale replica information returned from cn=monitor                                                                                             | Open                         |
| OPENDJ-8008  | OutOfMemoryException in subtree delete                                                                                                         | Fixed in 7.2.0               |
| OPENDJ-7942  | The server ignores critical VLV request controls when falling back to an unindexed search                                                      | Fixed in 7.3.0               |
| OPENDJ-7941  | Client connections to proxy time out after 10 seconds regardless of activity                                                                   | Fixed in 7.2.3, 7.3.0        |
| OPENDJ-7925  | The searchrate tool does not retrieve data when used simultaneously with the modrate tool on groups                                            | Fixed in 7.3.0               |
| OPENDJ-7844  | Difficult to override standard LDAP schema defined in 00-core.ldif                                                                             | Open                         |
| OPENDJ-7837  | Schema replication issues when adding a new server with conflicting schema to an existing topology                                             | Open                         |
| OPENDJ-7788  | dsrepl initialize from 5.5 causes the ReplicationDomain listener to die with an NPE                                                            | Open                         |
| OPENDJ-7763  | Proxy replication service discovery with RS-only and DS-only seems not to route search                                                         | Open                         |
| OPENDJ-7743  | Setting DN-valued properties to a config expression causes startup to fail                                                                     | Open                         |
| OPENDJ-7741  | dsrepl add-local-server-to-pre-7-0-topology requires a base DN for an RS                                                                       | Open                         |
| OPENDJ-7640  | Supportextract does not collect all security stores when several keystores have the same basename                                              | Fixed in 7.2.1, 7.3.0        |
| OPENDJ-7596  | dsbackup has global connection options that do not work with some subcommands                                                                  | Fixed in 7.2.0               |
| OPENDJ-7544  | dsconfig online sometimes triggers a duplicate server IDs error                                                                                | Open                         |
| OPENDJ-7516  | External cn=changelog is not updated while replication initialization is in progress                                                           | Fixed in 7.2.1, 7.3.0        |
| OPENDJ-7219  | PreParseAddOperation cannot remove attributes                                                                                                  | Open                         |
| OPENDJ-6579  | Schema is not populated to remote instances if added before enabling replication                                                               | Open                         |
| OPENDJ-6468  | ds-mon-\* Prometheus metrics are labeled as gauge but seem to be counters                                                                      | Open                         |
| OPENDJ-6022  | PTA to Active Directory returns more than one entry when only one exists                                                                       | Open                         |
| OPENDJ-3409  | Retention and rotation policies do not work with CAUD handlers                                                                                 | Fixed in 7.3.0               |

1 Upgrade to the listed version or later to get the fix.

## DS 7.0.2

| Issue ID    | Summary                                                                                                      | Status1                             |
| ----------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------------- |
| OPENDJ-9790 | Cannot create GeneralizedTimes with large fractional values                                                  | Fixed in 7.3.3, 7.4.0               |
| OPENDJ-9472 | Upgrade does not correctly handle previously patched upgrades                                                | Fixed in 7.1.6, 7.2.3, 7.3.2, 7.4.0 |
| OPENDJ-9347 | GSSAPISASLMechanismHandler incorrectly formats the login conf file                                           | Fixed in 7.1.5, 7.2.2, 7.3.0        |
| OPENDJ-9250 | The max-allowed-client-connections limit should not apply to the admin connector                             | Fixed in 7.3.0                      |
| OPENDJ-9213 | The dsconfig list-replication-domains output contains redundant columns                                      | Fixed in 7.3.0                      |
| OPENDJ-9033 | DS refuses to start and throws an NPE when a subordinate-base-dn is used                                     | Fixed in 7.2.1, 7.3.0               |
| OPENDJ-8874 | Full replica purge should write CSN information right away                                                   | Fixed in 7.1.3, 7.2.0               |
| OPENDJ-8870 | RFC2307bis schema is different from the internet-draft                                                       | Fixed in 7.2.0                      |
| OPENDJ-8829 | Error messages incorrectly mentions cn=System,cn=monitor                                                     | Fixed in 7.2.0                      |
| OPENDJ-8815 | dsrepl status does not take bad data status into account                                                     | Fixed in 7.1.3, 7.2.1, 7.3.0        |
| OPENDJ-8778 | Setup option --trustStorePassword:file behaves differently than --trustStorePasswordFile                     | Fixed in 7.2.0                      |
| OPENDJ-8698 | DS should write config archive files in a crash consistent way                                               | Fixed in 7.1.3, 7.2.0               |
| OPENDJ-8613 | No error is logged when sending of task completion notification email fails                                  | Fixed in 7.1.3, 7.2.0               |
| OPENDJ-8473 | Upgrade does not migrate ds-cfg-je-property values                                                           | Fixed in 7.2.0                      |
| OPENDJ-8383 | dsrepl status fails when certificates accepted interactively                                                 | Fixed in 7.2.0                      |
| OPENDJ-8378 | dsrepl status shows deleted replication domains                                                              | Fixed in 7.1.3, 7.2.1, 7.3.0        |
| OPENDJ-8280 | DS will not start when using a non-US locale after changing config                                           | Fixed in 7.2.0                      |
| OPENDJ-8243 | Indexes could cause ldapsearch to return multiple copies of the same entry                                   | Fixed in 7.1.1, 7.2.0               |
| OPENDJ-8227 | Deadlock between Changelog DB purger and Thread for RS session                                               | Fixed in 7.2.0                      |
| OPENDJ-8093 | Stale replica information returned from cn=monitor                                                           | Open                                |
| OPENDJ-8072 | dsrepl initialize hangs after re-enabling replication                                                        | Open                                |
| OPENDJ-8046 | Changelog files are not closed after searching cn=changelog                                                  | Fixed in 7.1.1, 7.2.0               |
| OPENDJ-8028 | Prometheus monitoring doesn't work with Telegraf                                                             | Fixed in 7.1.1, 7.2.0               |
| OPENDJ-8024 | Prevent configuration of VLV indexes with scope base-object                                                  | Fixed in 7.2.0                      |
| OPENDJ-7991 | makeldif: "invalid number of arguments" using DateTime tag with colons                                       | Fixed in 7.2.0                      |
| OPENDJ-7971 | dsbackup fails when JDB file cleaned                                                                         | Fixed in 7.1.1, 7.2.0               |
| OPENDJ-7970 | Ensure that DS is crash resilient for all runtime file changes                                               | Fixed in 7.1.2, 7.2.0               |
| OPENDJ-7942 | The server ignores critical VLV request controls when falling back to an unindexed search                    | Fixed in 7.3.0                      |
| OPENDJ-7941 | Client connections to proxy time out after 10 seconds regardless of activity                                 | Fixed in 7.2.3, 7.3.0               |
| OPENDJ-7928 | JSON normalization cannot handle nested arrays                                                               | Fixed in 7.1.0                      |
| OPENDJ-7905 | Schema replication error after upgrade                                                                       | Fixed in 7.1.0                      |
| OPENDJ-7889 | Configuring group-id against DS-only instance requires restart for the change to be reported by monitoring   | Fixed in 7.1.1, 7.2.0               |
| OPENDJ-7867 | NPE if dsbackup bucket name contains underscores                                                             | Fixed in 7.1.0                      |
| OPENDJ-7851 | Supportextract tool: clobbers the server.out filehandle when kill -3 is used.                                | Fixed in 7.1.0                      |
| OPENDJ-7847 | StaticGroup's objectclass sanity checks are unhelpful                                                        | Fixed in 7.1.0                      |
| OPENDJ-7844 | Difficult to override standard LDAP schema defined in 00-core.ldif                                           | Open                                |
| OPENDJ-7837 | Schema replication issues when adding a new server with conflicting schema to an existing topology           | Open                                |
| OPENDJ-7818 | Package based upgrade does not support instances running as non-root                                         | Fixed in 7.1.1, 7.2.0               |
| OPENDJ-7816 | dsbackup fails when destination is a symbolic link to a real directory                                       | Fixed in 7.1.2, 7.2.0               |
| OPENDJ-7788 | dsrepl initialize from 5.5 causes the ReplicationDomain listener to die with an NPE                          | Open                                |
| OPENDJ-7761 | DS sporadically hangs while reconnecting to an RS                                                            | Fixed in 7.1.0                      |
| OPENDJ-7758 | DS 7.0 dsrepl add-local-server-to-pre-7-0-topology: NPE if master-key is in different keystore               | Fixed in 7.1.0                      |
| OPENDJ-7755 | DS 7.0 replication with older version, CryptoManager failed to import the symmetric key entry                | Fixed in 7.1.1, 7.2.0               |
| OPENDJ-7744 | dsrepl initialize in a topology with DS7 and DS 5.5 fails if DS7 serverId starts with 0                      | Fixed in 7.1.1, 7.2.0               |
| OPENDJ-7743 | Setting DN-valued properties to a config expression causes startup to fail                                   | Open                                |
| OPENDJ-7737 | ConfigurationFramework#initialize0 changes the class loader without clearing the map of registered jar files | Fixed in 7.1.0                      |
| OPENDJ-7706 | Unable to set up replication between standalone DS and RS servers and older versions of DS or OpenDJ         | Open                                |
| OPENDJ-7699 | Supportextract throws NoSuchElementException when the server.pid file is empty                               | Fixed in 7.1.0                      |
| OPENDJ-7689 | dsrepl add-local-server-to-pre-7-0-topology does not tolerate separate keystore and truststore               | Fixed in 7.1.0                      |
| OPENDJ-7688 | Spurious DS disconnections because of missing heartbeat                                                      | Fixed in 7.2.1, 7.3.0               |
| OPENDJ-7687 | Global Access Control Policy regarding cn=schema is too restrictive                                          | Fixed in 7.1.0                      |
| OPENDJ-7655 | Replaying multiple MODIFYDN operations is very slow                                                          | Fixed in 7.1.0                      |
| OPENDJ-7653 | replication issue in the cloud after ldapadd                                                                 | Fixed in 7.1.0                      |
| OPENDJ-7596 | dsbackup has global connection options that do not work with some subcommands                                | Fixed in 7.2.0                      |
| OPENDJ-7516 | External cn=changelog is not updated while replication initialization is in progress                         | Fixed in 7.2.1, 7.3.0               |
| OPENDJ-7513 | Missing subSchemaSubEntry attribute from rootDSE access controls                                             | Fixed in 7.1.0                      |
| OPENDJ-7481 | JSON logs do not contain proxy auth DN                                                                       | Fixed in 7.1.0                      |
| OPENDJ-7474 | Docker sample README.md provides wrong instructions for running the container                                | Fixed in 7.1.0                      |
| OPENDJ-7322 | IndexOutOfBoundsException while configuring max-replication-delay-health-check                               | Fixed in 7.1.0                      |
| OPENDJ-7219 | PreParseAddOperation cannot remove attributes                                                                | Open                                |
| OPENDJ-7014 | Some operational attributes are not replicated when a restore --dry-run is used against an online server     | Open                                |
| OPENDJ-7011 | RFC 2252 Binary syntax doesn't use ";binary" transfer encoding                                               | Open                                |
| OPENDJ-6791 | RS reconnect delay is too aggressive                                                                         | Fixed in 7.3.3, 7.4.0               |
| OPENDJ-6774 | Searches no longer return attributes in the order requested                                                  | Open                                |
| OPENDJ-6579 | Schema is not populated to remote instances if added before enabling replication                             | Open                                |
| OPENDJ-6468 | ds-mon-\* Prometheus metrics are labeled as gauge but seem to be counters                                    | Open                                |
| OPENDJ-6022 | PTA to Active Directory returns more than one entry when only one exists                                     | Open                                |
| OPENDJ-5602 | JDK11: unexpected return code 81 using SASL External                                                         | Open                                |
| OPENDJ-4935 | Replication instability and divergence when using high latency disks                                         | Fixed in 7.1.2, 7.2.0               |
| OPENDJ-3409 | Retention and rotation policies do not work with CAUD handlers                                               | Fixed in 7.3.0                      |

1 Upgrade to the listed version or later to get the fix.

## DS 6.5.6

| Issue ID    | Summary                                                                                                         | Status1               |
| ----------- | --------------------------------------------------------------------------------------------------------------- | --------------------- |
| OPENDJ-9544 | Searches for attributes that do not exist in schema still take time                                             | Fixed in 7.4.0        |
| OPENDJ-8842 | Proxy DS does not cancel psearch to Backend DS if psearch is cancelled                                          | Fixed in 7.0.0        |
| OPENDJ-8838 | Backslashes in files read via a config expression are mishandled                                                | Open                  |
| OPENDJ-8829 | Error messages incorrectly mentions cn=System,cn=monitor                                                        | Fixed in 7.2.0        |
| OPENDJ-8613 | No error is logged when sending of task completion notification email fails                                     | Fixed in 7.1.3, 7.2.0 |
| OPENDJ-8473 | Upgrade does not migrate ds-cfg-je-property values                                                              | Fixed in 7.2.0        |
| OPENDJ-8460 | Deploying DS6.5.5+JDK11 causes continuous hostname resolution errors in pods with DS6.5.5+JDK8                  | Open                  |
| OPENDJ-8234 | ADD of large entry is not replicated                                                                            | Open                  |
| OPENDJ-8226 | Support Extract tool ignores non-default changelogDb location when collecting domains.state file                | Fixed in 7.1.1, 7.2.0 |
| OPENDJ-8205 | Log message lists an object's string representation instead of a file name                                      | Fixed in 7.1.1, 7.2.0 |
| OPENDJ-8137 | LDIF backend silently rejects entries that fail schema validation                                               | Fixed in 7.2.0        |
| OPENDJ-8089 | rest2ldap gateway returns string instead of boolean                                                             | Fixed in 7.1.0        |
| OPENDJ-8046 | Changelog files are not closed after searching cn=changelog                                                     | Fixed in 7.1.1, 7.2.0 |
| OPENDJ-8024 | Prevent configuration of VLV indexes with scope base-object                                                     | Fixed in 7.2.0        |
| OPENDJ-8018 | Older servers cannot create a new symmetric key in mixed version topologies                                     | Open                  |
| OPENDJ-7942 | The server ignores critical VLV request controls when falling back to an unindexed search                       | Fixed in 7.3.0        |
| OPENDJ-7919 | A search for modifyTimestamp>=00000101000000Z results in a YEAR error and disconnect                            | Fixed in 7.0.0        |
| OPENDJ-7810 | JMX connections are always considered insecure                                                                  | Fixed in 7.0.2, 7.1.0 |
| OPENDJ-7687 | Global Access Control Policy regarding cn=schema is too restrictive                                             | Fixed in 7.1.0        |
| OPENDJ-7654 | DS is sometimes unable to connect to RS after full gc                                                           | Fixed in 7.2.0        |
| OPENDJ-7643 | Log that is supposedly generated from dsreplication operation is empty or does not exist                        | Open                  |
| OPENDJ-7640 | Supportextract does not collect all security stores when several keystores have the same basename               | Fixed in 7.2.1, 7.3.0 |
| OPENDJ-7516 | External cn=changelog is not updated while replication initialization is in progress                            | Fixed in 7.2.1, 7.3.0 |
| OPENDJ-7288 | LDAPS Handlers "SelectorRunner" thread hangs up in Grizzly SSLUtils.sslEngineUnwrap                             | Fixed in 7.1.0        |
| OPENDJ-7219 | PreParseAddOperation cannot remove attributes                                                                   | Open                  |
| OPENDJ-7099 | Query for AclRightsInfos can throw an exception due to invalid attribute description                            | Fixed in 7.0.0        |
| OPENDJ-7011 | RFC 2252 Binary syntax doesn't use ";binary" transfer encoding                                                  | Open                  |
| OPENDJ-6977 | DS expects root user password instead of admin user password in standalone DS , RS deployments                  | Open                  |
| OPENDJ-6931 | DS to RS failover mechanism does not account for non responsive established connections                         | Fixed in 7.0.0        |
| OPENDJ-6774 | Searches no longer return attributes in the order requested                                                     | Open                  |
| OPENDJ-6579 | Schema is not populated to remote instances if added before enabling replication                                | Open                  |
| OPENDJ-6499 | Query on rest2ldap over ssl gets stuck after few curl requests using TLSv1.3 on JDK11                           | Fixed in 7.0.0        |
| OPENDJ-6468 | ds-mon-\* Prometheus metrics are labeled as gauge but seem to be counters                                       | Open                  |
| OPENDJ-6380 | Warning message for duplicate objectclass schema definition is misleading                                       | Open                  |
| OPENDJ-6378 | Entries are returned with attribute names using inconsistent case                                               | Fixed in 7.0.0        |
| OPENDJ-6358 | backUpAll doesn't backup ads-truststore.pin                                                                     | Open                  |
| OPENDJ-6223 | Searching telephoneNumber field with a non-numeric value returns all the records                                | Fixed in 7.0.0        |
| OPENDJ-6221 | Logging for CONNECT operations are not saved in Nanosecond format                                               | Fixed in 7.0.0        |
| OPENDJ-6198 | Server won't start if I try to configure a ConnectionHandler to listen on 2 IP addresses                        | Fixed in 7.0.0        |
| OPENDJ-6149 | The Global Access Control Policy option within the dsconfig tool is misleading as is the error message returned | Open                  |
| OPENDJ-6116 | Unspecified Communications Error when multiple rest2ldap endpoints share configuration elements                 | Fixed in 7.0.0        |
| OPENDJ-6022 | PTA to Active Directory returns more than one entry when only one exists                                        | Open                  |
| OPENDJ-5985 | Divergence of "cn=admin data" after setting up secure replication and encrypted backends                        | Open                  |
| OPENDJ-5956 | Data discrepancy between servers if the same attribute has extra spaces in RDN                                  | Open                  |
| OPENDJ-5745 | Azure AD Connector Uses Deprecated Untrusted/Unsigned MSOnline Powershell Module                                | Open                  |
| OPENDJ-5664 | JDK 11: illegal reflective access warning during import-ldif                                                    | Fixed in 7.0.0        |
| OPENDJ-5663 | JDK 11: illegal reflective access warning on setup (without profile)                                            | Open                  |
| OPENDJ-5661 | supportextract tool help and version options are different from other tools                                     | Fixed in 7.0.0        |
| OPENDJ-5660 | JDK 11: illegal reflective access warning on setup (with profile)                                               | Fixed in 7.0.0        |
| OPENDJ-5590 | Proxy: server discovery fails silently when proxy base-dn differs from backend's base-dn                        | Fixed in 7.0.0        |
| OPENDJ-5201 | Tools may prompt to trust certificate multiple times for different reasons                                      | Open                  |
| OPENDJ-5174 | dsreplication initialize-all task sometimes fails with STOPPED\_BY\_ERROR                                       | Open                  |
| OPENDJ-4943 | NullPointerException in BackupManager.java when backup --hash is used offline                                   | Open                  |
| OPENDJ-4475 | Attribute value password validator does not check substrings in reversed password                               | Fixed in 7.0.0        |
| OPENDJ-4008 | dsconfig exits with error when listing global access control policy                                             | Open                  |

1 Upgrade to the listed version or later to get the fix.

---

---
title: Limitations
description: Describes inherent PingDS design limitations, including account lockout replication behavior and HDAP JSON attribute patching restrictions.
component: pingds
version: release-notes
page_id: pingds::limitations
canonical_url: https://docs.pingidentity.com/pingds/release-notes/limitations.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-06-10T12:00:00Z
keywords: ["Evaluation", "LDAP"]
section_ids:
  account_lockout: Account lockout
  hdap: HDAP
  language_dependent_matching: Language-dependent matching
  ldap: LDAP
  passwords: Passwords
  proxy_services: Proxy services
  replication: Replication
  rest_to_ldap: REST to LDAP
  windows: Windows
---

# Limitations

The following limitations are inherent to the design, not bugs to be fixed.

## Account lockout

When you configure account lockout as part of password policy, DS servers lock an account after the specified number of consecutive authentication failures.

*Account lockout is not transactional across all replicas in a deployment.* Global account lockout occurs as soon as the authentication failure times have been replicated.

## HDAP

* When patching a `json` syntax attribute, you can't patch individual fields of the JSON object. You must change the entire JSON object instead.

  As a workaround, perform an update of the entire object, changing only the desired fields in your copy.

- For referrals, HDAP returns HTTP 404 `Not Found`. HDAP does not return the equivalent of LDAP continuation references.

* HDAP does not support query filters for equality matching (`eq`) with address fields like `postalAddress`.

## Language-dependent matching

Between Java 17 and Java 21, the string collation rules implementation changed.

DS depends on Java string collation rules to compare and sort strings for many languages and locales. When you change Java versions, DS can therefore return different results for the same language-specific search.

As an example, suppose you have entries with attributes containing `passe`, `passé`, `PASSE`, and `PASSÉ`. With Java 21, the French-specific search filter `(cn:fr.eq:=passe)` matches all the entries. With Java 17, the same filter matches only the entries whose values don't include the accents, `passe` and `PASSE`.

## LDAP

* DS servers provide full LDAP v3 support, except for alias dereferencing, and limited support for LDAPv2.

* When the global server property `invalid-attribute-syntax-behavior` is set to `accept` or `warn`, a search on group membership using a value with invalid syntax returns nothing.

## Passwords

* Directory servers store passwords prefixed with the storage scheme in braces, as in `{scheme}`.

  To prevent users from effectively attempting to choose their own password storage scheme, directory servers don't support passwords that strictly match this format.

  Specifically, directory servers don't support passwords that match `{string.*`.

  Requests to update `userPassword` values with such passwords fail with result code 19 (Constraint Violation), and an additional message that passwords may not be provided in pre-encoded form.

* The Password Policy control (OID: `1.3.6.1.4.1.42.2.27.8.5.1`) is supported for add, bind, and modify operations.

  It is not supported for compare, delete, search, and modify DN operations.

## Proxy services

* Configuring a server with both local backends and proxy backends is not supported.

  Access control models for directory servers and proxy servers don't function at the same time in the same server.

* The policy-based access control handler used in proxy servers:

  * Does not support the Get Effective Rights control.

  * Does not check the `modify-acl` privilege when global access control policies are changed.

    The `config-write` privilege is sufficient to change global access control policies.

  * Does not send alert notifications when global access control policies change.

* When using ACIs or collective attributes with the proxy server data distribution feature, the ACI and entries having collective attribute values must be located at or above the `partition-base-dn`. When changing this data, make the change behind the proxy to one directory server replica in each shard. Your changes are not replicated outside the shard.

  The proxy server data distribution feature does not currently support the following:

  * Importing distributed data with the `import-ldif` command.

  * Changes to the number of partitions after data has been deployed.

  * Modify DN operations to distributed entries.

  * Updates to entries at or above the `partition-base-dn`.

  * Virtual static groups.

  * Data distribution does not support these virtual attributes:

    `member`\
    `uniqueMember`

    The `isMemberOf` virtual attribute works as expected as long as you replicate the group entries on every shard.

  * Data distribution does not support these LDAP controls:

    * Server-Side Sort controls

      `1.2.840.113556.1.4.473`\
      `1.2.840.113556.1.4.474`

    * Simple Paged Results control

      `1.2.840.113556.1.4.319`

    * Virtual List View controls

      `2.16.840.1.113730.3.4.9`\
      `2.16.840.1.113730.3.4.10`

## Replication

* The `dsrepl status` command can't read status information from DS 6.5 and earlier servers.

  During upgrade, use the `dsreplication status` command for 6.5 and earlier servers, and the `dsrepl status` command for 7.0 and later servers.

* Pre-7.0 DS servers can't create a new symmetric key in mixed version topologies.

  When a DS 6.5 or earlier server generates a new symmetric key, it displays an error, such as the following:

  ```
  Cannot encode entry for writing on storage:
   CryptoManager failed to encode symmetric key attribute value:
    InvalidKeyException(Wrong key usage) base dn : dc=com
  ```

  To work around this limitation, upgrade the pre-7.0 DS servers and use the new security model.

## REST to LDAP

* REST to LDAP on a DS proxy server does not support authentication as a remote user.

  Access REST to LDAP through the gateway or directly on a DS directory server.

* REST to LDAP does not support modify RDN operations.

* REST to LDAP query filters don't work with properties of subtypes.

  For example, the default example configuration describes a user type, and a POSIX user type. If your query filter is based on a POSIX user type property that is not a property of the user type, such as `loginShell` or `gidNumber`, the filter always evaluates to false, and the query returns nothing.

* When applying a Common REST patch operation to a `Json` syntax attribute, you can't patch individual fields of the JSON object. You must change the entire JSON object instead.

  As a workaround, perform an update of the entire object, changing only the desired fields in your copy.

## Windows

Due to a Java issue on Windows systems ([JDK-8057894](https://bugs.openjdk.java.net/browse/JDK-8057894)), when configuring DS servers with data confidentiality enabled, DS might display an error message containing the following text:

```
Unexpected CryptoAPI failure generating seed
```

If this happens, try running the command again.

---

---
title: PingDS release notes
description: PingDS release notes covering multiple versions with quick links to downloads, requirements, fixes, and upgrade guidance.
component: pingds
version: release-notes
page_id: pingds::preface
canonical_url: https://docs.pingidentity.com/pingds/release-notes/preface.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-07-07T12:00:00Z
keywords: ["Evaluation", "LDAP"]
section_ids:
  quick_links: Quick links
  ds_8_1_1_latest: DS 8.1.1 (latest)
  ds_8_0_4: DS 8.0.4
  ds_7_5_4: DS 7.5.4
  ds_7_4_4: DS 7.4.4
  ds_7_3_6: DS 7.3.6
  ds_7_2_5: DS 7.2.5
  about_pingds: About PingDS
---

# PingDS release notes

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | These release notes cover multiple versions of PingDS software. They're designed to make it easier to upgrade, especially when you're skipping releases.Some older DS versions have reached the end of support (EOS) or end of life (EOL). Learn more in [Ping Identity End of Life (EOL) Software Tracker](https://support.pingidentity.com/s/article/Ping-Identity-EOL-Tracker#pds). If you're still running an EOS or EOL version, upgrade as soon as possible to an actively maintained version. |

## Quick links

### DS 8.1.1 (latest)

* [Downloads](downloads.html)

* [Requirements](requirements.html)

* [What's new](whats-new.html#whats-new-81)

* [Fixes in 8.1.x](fixes-8.1.html)

* [Removed features](removed.html#removed-81)

* [Incompatible changes](changes.html#changes-81)

* [Deprecated features](deprecation.html#deprecated-81)

* [Known issues](known-issues.html#known-issues-81)

* [Limitations](limitations.html)

### DS 8.0.4

* [Downloads](https://product-downloads.pingidentity.com/browse/ds/all/productId:ds/minorVersion:8.0)

* [Requirements](requirements.html)

* [What's new](whats-new.html#whats-new-80)

* [Fixes in 8.0.x](fixes-8.0.html)

* [Removed features](removed.html#removed-80)

* [Incompatible changes](changes.html#changes-80)

* [Deprecated features](deprecation.html#deprecated-80)

* [Known issues](known-issues.html#known-issues-80)

* [Limitations](limitations.html)

### DS 7.5.4

* [Downloads](https://product-downloads.pingidentity.com/browse/ds/all/productId:ds/minorVersion:7.5)

* [Requirements](requirements.html)

* [What's new](whats-new.html#whats-new-75)

* [Fixes in 7.5.x](fixes-7.5.html)

* [Removed features](removed.html#removed-75)

* [Incompatible changes](changes.html#changes-75)

* [Deprecated features](deprecation.html#deprecated-75)

* [Known issues](known-issues.html#known-issues-75)

* [Limitations](limitations.html)

### DS 7.4.4

* [Downloads](https://product-downloads.pingidentity.com/browse/ds/all/productId:ds/minorVersion:7.4)

* [Requirements](requirements.html)

* [What's new](whats-new.html#whats-new-74)

* [Fixes in 7.4.x](fixes-7.4.html)

* [Removed features](removed.html#removed-74)

* [Incompatible changes](changes.html#changes-74)

* [Deprecated features](deprecation.html#deprecated-74)

* [Known issues](known-issues.html#known-issues-74)

* [Limitations](limitations.html)

### DS 7.3.6

* [Downloads](https://product-downloads.pingidentity.com/browse/ds/all/productId:ds/minorVersion:7.3)

* [Requirements](requirements.html)

* [What's new](whats-new.html#whats-new-73)

* [Fixes in 7.3.x](fixes-7.3.html)

* [Removed features](removed.html#removed-73)

* [Incompatible changes](changes.html#changes-73)

* [Deprecated features](deprecation.html#deprecated-73)

* [Known issues](known-issues.html#known-issues-73)

* [Limitations](limitations.html)

### DS 7.2.5

* [Downloads](https://product-downloads.pingidentity.com/browse/ds/all/productId:ds/minorVersion:7.2)

* [Requirements](requirements.html)

* [What's new](whats-new.html#whats-new-72)

* [Fixes in 7.2.x](fixes-7.2.html)

* [Removed features](removed.html#removed-72)

* [Incompatible changes](changes.html#changes-72)

* [Deprecated features](deprecation.html#deprecated-72)

* [Known issues](known-issues.html#known-issues-72)

* [Limitations](limitations.html)

## About PingDS

PingDS software provides an LDAPv3-compliant directory service, developed for the Java platform, delivering a high-performance, highly available, and secure store for the identities managed by your organization. *Read these notes before you install or upgrade PingDS software.*

The easy installation process, combined with the power of the Java platform, makes this the simplest and fastest directory service to deploy and manage. PingDS software comes with plenty of tools. PingDS software also offers REST access to directory data over HTTP.

Ping Identity offers training and support subscriptions to help you get the most out of your deployment.

---

---
title: Release timeline
description: PingDS release timeline listing all major, minor, and maintenance releases with release dates and version numbers.
component: pingds
version: release-notes
page_id: pingds::timeline
canonical_url: https://docs.pingidentity.com/pingds/release-notes/timeline.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-07-07T12:00:00Z
keywords: ["LDAP", "Upgrade"]
---

# Release timeline

| Release date | DS version    | Release type(1) |
| ------------ | ------------- | --------------- |
| 2025-07-16   | 8.0.4         | Maintenance     |
| 2025-07-16   | 7.5.4         | Maintenance     |
| 2026-06-30   | 8.1.1         | Maintenance     |
| 2026-06-04   | 8.0.3         | Maintenance     |
| 2026-03-31   | 8.1.0         | Minor           |
| 2025-11-19   | 8.0.2         | Maintenance     |
| 2025-11-19   | 7.5.3         | Maintenance     |
| 2025-09-30   | 8.0.1         | Maintenance     |
| 2025-07-16   | 7.4.4         | Maintenance     |
| 2025-05-15   | 7.5.2         | Maintenance     |
| 2025-04-07   | 8.0.0         | Major           |
| 2025-01-15   | 7.3.6         | Maintenance     |
| 2024-10-16   | 7.4.3         | Maintenance     |
| 2024-08-14   | 7.5.1         | Maintenance     |
| 2024-06-26   | 7.1.8         | Maintenance     |
| 2024-05-29   | 7.2.5         | Maintenance     |
| 2024-05-15   | 7.3.5         | Maintenance     |
| 2024-04-30   | 7.4.2         | Maintenance     |
| 2024-04-02   | 7.5.0         | Minor           |
| 2024-01-18   | 7.4.1         | Maintenance     |
| 2024-01-17   | 7.3.4         | Maintenance     |
| 2023-12-14   | 7.2.4         | Maintenance     |
| 2023-11-15   | 7.1.7         | Maintenance     |
| 2023-10-09   | 7.4.0         | Minor           |
| 2023-09-11   | 7.3.3         | Maintenance     |
| 2023-08-28   | 7.2.3         | Maintenance     |
| 2023-07-27   | 7.1.6         | Maintenance     |
| 2023-06-29   | 7.3.2         | Maintenance     |
| 2023-06-09   | 7.3.1         | Maintenance     |
| 2023-05-25   | 7.1.5         | Maintenance     |
| 2023-04-27   | 7.2.2         | Maintenance     |
| 2023-04-04   | 7.3.0         | Minor           |
| 2023-01-26   | 7.2.1         | Maintenance     |
| 2022-10-11   | 7.1.4         | Maintenance     |
| 2022-09-09   | 7.1.3         | Maintenance     |
| 2022-08-03   | 6.5.6         | Maintenance     |
| 2022-06-30   | 7.2.0         | Minor           |
| 2022-02-28   | 7.1.2         | Maintenance     |
| 2021-09-28   | 7.1.1         | Maintenance     |
| 2021-08-16   | 6.5.5         | Maintenance     |
| 2021-05-12   | 7.1.0         | Minor           |
| 2021-03-29   | 7.0.2         | Maintenance     |
| 2020-12-10   | 7.0.1         | Maintenance     |
| 2020-09-23   | 6.5.4         | Maintenance     |
| 2020-08-10   | 7.0.0         | Major           |
| 2020-04-03   | 5.5.3         | Maintenance     |
| 2020-02-27   | 6.5.3         | Maintenance     |
| 2019-06-20   | 6.5.2         | Maintenance     |
| 2019-04-10   | 6.5.1         | Maintenance     |
| 2018-11-28   | 6.5.0         | Minor           |
| 2018-10-01   | 5.5.2         | Maintenance     |
| 2018-07-19   | 5.5.1         | Maintenance     |
| 2018-05-04   | 6.0.0         | Major           |
| 2017-10-18   | 5.5.0         | Minor           |
| 2017-04-03   | 5             | Major           |
| 2016-01-27   | 3             | Major           |
| 2013-07-04   | 2.6           | Minor           |
| 2010-12-23   | 2.4           | Minor           |
| 2010-07-23   | 2.5.0-Xpress1 | Minor           |

(1) Find details about the scope of expected changes for different release types in [Interface stability](stability.html).

---

---
title: Removed
description: Lists functionality removed in PingDS releases, including commands, APIs, and configuration options no longer available.
component: pingds
version: release-notes
page_id: pingds::removed
canonical_url: https://docs.pingidentity.com/pingds/release-notes/removed.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-04-20T12:00:00Z
keywords: ["Compatibility", "LDAP", "Upgrade"]
section_ids:
  removed-81: DS 8.1
  removed-80: DS 8.0
  removed-75: DS 7.5
  removed-74: DS 7.4
  removed-73: DS 7.3
  removed-72: DS 7.2
  removed-71: DS 7.1
  removed-70: DS 7.0
  ds_6_5: DS 6.5
---

# Removed

The functionality listed here has been removed.

## DS 8.1

* Support for Java 21 has been removed.

* Support for the following HTTP authorization mechanisms has been removed:

  * HTTP OAuth2 CTS

  * HTTP OAuth2 File

  * HTTP OAuth2 OpenAM

  * HTTP OAuth2 Token Introspection (RFC7662)

## DS 8.0

* Support for Java versions before 21 has been removed.

* The DS REST to LDAP endpoints, configuration, and gateway have been removed.

  The DSML gateway has also been removed.

  For HTTP access to directory data, use [HDAP](https://docs.pingidentity.com/pingds/8/rest-guide/preface.html) instead.

* The JMX connection handler has been removed.

* The `rehash-policy: always` setting for Bcrypt and PBKDF2-based password policies has been removed.

  The `rehash-policy` can now be set to `never` (default), `only-decrease`, or `only-increase`.

* Support has been removed for CSV, Elasticsearch, JDBC, JMS, Splunk, and Syslog access logs.

  As a result, the following log publishers have been removed:

  * `CsvFileAccessLogPublisher`

  * `CsvFileHttpAccessLogPublisher`

  Elasticsearch and Splunk have native or third-party tools to collect, transform, and route logs. Learn more in [Third-party software](requirements.html#commons-third-party).

* Support has been removed for the `/admin` and `/metrics/api` endpoints.

* With the updates to change number indexing, the `dsrepl reset-change-number` command has been removed.

  The following metrics have also been removed:

  LDAP:

  * `ds-mon-indexing-state`

  * `ds-mon-purge-waiting-for-change-number-indexing`

  * `ds-mon-replicas-preventing-indexing`

  * `ds-mon-time-since-last-indexing`

  Prometheus:

  * `ds_change_number_indexing_state`

  * `ds_change_number_time_since_last_indexing_seconds`

  * `ds_replication_changelog_purge_waiting_for_change_number_indexing`

- The `dsconfig` global configuration variable `use-virtual-threads-if-available` has been removed.

* The following JE Backend configuration properties have been removed:

  * `db-checkpointer-wakeup-interval`

  * `db-evictor-core-threads`

  * `db-evictor-keep-alive`

  * `db-evictor-max-threads`

  * `db-num-cleaner-threads`

  * `db-num-lock-tables`

  * `db-run-cleaner`

## DS 7.5

* Support for Java 11 has been removed.

  When upgrading to this version, follow the instructions in [Before you upgrade](https://docs.pingidentity.com/pingds/7.5/upgrade-guide/before-you-upgrade.html).

* The `dsrepl start-disaster-recovery` and `dsrepl end-disaster-recovery` commands have been removed.

  For instructions on what to use instead, refer to the [disaster recovery](https://docs.pingidentity.com/pingds/7.5/use-cases/disaster-recovery.html) documentation instead.

* Support for SNMP monitoring has been removed.

* The deprecated `/admin` and `/api` (REST to LDAP) endpoints have been removed from the configuration for new servers.

  If you must create them temporarily for compatibility, refer to [When adding new servers](https://docs.pingidentity.com/pingds/7.5/upgrade-guide/add-new-servers.html).

## DS 7.4

* The file-based debug log publisher has been removed.

  An error log publisher now writes debug-level messages. For details, refer to [Debug-level logging](https://docs.pingidentity.com/pingds/7.4/maintenance-guide/troubleshooting.html#troubleshoot-enable-debug-logging).

* The Argon2 password storage configuration property `argon2-migration-memory` has been removed.

  If necessary, set `argon2-memory-pool-size` instead.

## DS 7.3

* The following deprecated command-line options have been removed:

  `--bindPasswordFile`\
  `--deploymentKeyPasswordFile`\
  `--keyStorePasswordFile`\
  `--monitorUserPasswordFile`\
  `--rootUserPasswordFile`\
  `--trustStorePasswordFile`

  Use the `--*:file` alternatives suggested in [Deprecated since DS 7.1](deprecation.html#deprecated-71) instead. With the `setup` command, use the `--keyStorePasswordFilePath` and `--trustStorePasswordFilePath` options to retain the paths to the files in the configuration instead of copying the cleartext passwords.

* The `Degraded` replica status and `degraded-status-threshold` configuration property have been removed.

  When the replication delay is more than five seconds, the `dsrepl status` command reports the replica is `SLOW`.

* The advanced LDAP connection handler property `send-rejection-notice` has been removed.

  The LDAP connection handler no longer sends an extended response message with a notice of disconnection when rejecting a new client connection.

## DS 7.2

* The `lookthrough-limit` setting has been removed. Use `time-limit` instead.

## DS 7.1

* You can no longer add new DS servers to a deployment with OpenDJ 2.6 or earlier servers.

  Instead, upgrade older servers before adding new servers.

* DS server configuration support for extending group implementations, including group implementation configuration objects, their properties, and the related `dsconfig` subcommands.

  In previous releases, an administrator could disable and enable group implementations, and could change the Java class of a group implementation as part of the server configuration.

  The default group implementations continue to work as documented in *Groups*.

## DS 7.0

* Support for Java 8 has been removed.

  Support for 32-bit JVMs has also been removed.

  When upgrading to this version, follow the instructions in *Before you upgrade*.

* The `backup` and `restore` commands have been removed. Use the `dsbackup` command instead.

* The `dsreplication` command has been removed.

  You now configure replication as part of the setup process using the `setup --replicationPort` and `setup --bootstrapReplicationServer` options. For details and examples, refer to *Installation*.

  For most operations, use the `dsrepl` command. Since replication configuration is part of the setup process, the `dsrepl` command does not include a command for configuring replication. Learn about the new command in *Replication*, and *Changelog for notifications*.

  To temporarily suspend and resume replication, use the `dsconfig` command. For details, refer to *Disable replication*.

* The `ads-truststore` and `ads-truststore.pin` files have been removed.

  For new deployments, DS servers protect secret keys with a shared master key. The setup process derives the shared master key from the deployment ID and password.

* The JVM profiler plugin has been removed.

* The following monitoring metrics have been removed:

  * LDAP metrics:

    * `ds-mon-approx-oldest-change-not-synchronized`

    * `ds-mon-approximate-delay`

    * `ds-mon-missing-changes`

  * Prometheus metrics:

    * `ds_replication_changelog_connected_replicas_approx_oldest_change_not_synchronized_seconds`

    * `ds_replication_changelog_connected_replicas_approximate_delay_seconds`

    * `ds_replication_changelog_connected_replicas_missing_changes`

* The following monitoring metrics depending on the JVM implementation are not stable interfaces. They have been removed from the documentation:

  * Garbage collection statistics

    Affected metrics have names like `ds-mon-jvm-garbage-collector-*` under `cn=monitor`, and `ds_jvm_garbage_collector_*` in Prometheus output.

  * Memory pool use

    Affected metrics have names like `ds-mon-jvm-memory-pools-*` under `cn=monitor`, and `ds_jvm_memory_pools_*` in Prometheus output.

* The `No-Op` alias for the LDAP no-op control (OID: 1.3.6.1.4.1.4203.1.10.2) has been removed.

  Use the `NoOp` alias or the OID instead.

## DS 6.5

* The `manage-account get-password-history` subcommand has been removed due to security concerns.