---
title: Release notes
description: Unless otherwise noted, all of the following enhancements, known issues, and resolved issues apply to the PingDirectory server, the PingDirectoryProxy server, and the PingDataSync server.
component: pingdirectory
version: 11.1
page_id: pingdirectory:release_notes:pd_release_notes
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/release_notes/pd_release_notes.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  pingdirectory-suite-of-products-11-1-0-0-june-2026: PingDirectory suite of products 11.1.0.0 (June 2026)
  added-runtime-support-for-java-25: Added runtime support for Java 25
  added-smtp-bearer-access-token-authentication: Added SMTP bearer access token authentication
  added-scheduled-data-cleanup-tasks: Added scheduled data cleanup tasks
  added-log-mode-for-rate-limiting-operations: Added log mode for rate-limiting operations
  added-a-kafka-sync-source: Added a Kafka sync source
  updated-the-password-sync-agent-to-version-4-9: Updated the Password Sync Agent to version 4.9
  added-certificate-trust-configuration-for-the-psa: Added certificate trust configuration for the PSA
  improved-connection-asymmetry-alarm-visibility: Improved connection-asymmetry alarm visibility
  improved-server-startup-time-on-linux: Improved server startup time on Linux
  improved-composite-index-selection-for-substring-filters: Improved composite index selection for substring filters
  improved-prometheus-metric-family-grouping: Improved Prometheus metric family grouping
  made-allow-upgrading-to-composite-index-editable-on-existing-indexes: Made allow-upgrading-to-composite-index editable on existing indexes
  added-detection-for-deleted-recovered-active-directory-entries: Added detection for deleted recovered Active Directory entries
  improved-deep-json-field-support-in-constructed-attribute-mappings: Improved deep JSON field support in constructed attribute mappings
  improved-schema-element-registration-error-messages: Improved schema element registration error messages
  improved-access-control-rule-parsing-and-validation: Improved access control rule parsing and validation
  improved-verify-index-schema-consistency-detection: Improved verify-index schema consistency detection
  added-alerts-for-ldap-schema-element-changes: Added alerts for LDAP schema element changes
  improved-psa-logging-for-connection-errors: Improved PSA logging for connection errors
  removed-scim-1-1-support: Removed SCIM 1.1 support
  deprecated-support-for-the-implicit-grant-type: Deprecated support for the Implicit grant type
  removed-the-swagger-ui-and-schema-generation-endpoints: Removed the Swagger UI and schema generation endpoints
  updated-the-opencsv-library: Updated the opencsv library
  upgraded-the-embedded-http-server-to-jetty-12: Upgraded the embedded HTTP server to Jetty 12
  removed-the-x86-version-of-the-psa: Removed the x86 version of the PSA
  installing-the-psa-on-windows-server-2016: Installing the PSA on Windows Server 2016
  fixed-a-tls-1-3-connection-termination-issue: Fixed a TLS 1.3 connection termination issue
  fixed-the-nodetach-option-for-start-server: Fixed the --nodetach option for start-server
  fixed-a-manage-profile-replace-profile-error: Fixed a manage-profile replace-profile error
  fixed-manage-profile-generate-profile-omitting-obscured-properties: Fixed manage-profile generate-profile omitting obscured properties
  fixed-a-server-shutdown-delay-issue: Fixed a server shutdown delay issue
  fixed-an-slf4j-startup-warning: Fixed an SLF4J startup warning
  fixed-admin-console-icons-in-closed-environments: Fixed admin console icons in closed environments
  fixed-false-positive-conflicts-for-the-unique-attribute-plugin: Fixed false-positive conflicts for the Unique Attribute plugin
  fixed-an-ldap-changelog-issue-with-subtree-deletions: Fixed an LDAP changelog issue with subtree deletions
  fixed-changelog-ordering-for-subtree-deletes: Fixed changelog ordering for subtree deletes
  fixed-identity-mapper-errors-for-unavailable-base-dns: Fixed identity mapper errors for unavailable base DNs
  fixed-rest-api-errors-for-unknown-schema-elements: Fixed REST API errors for unknown schema elements
  fixed-a-replication-missing-changes-alarm-error-message: Fixed a replication-missing-changes alarm error message
  fixed-schema-file-ordering-for-dependent-schema-elements: Fixed schema file ordering for dependent schema elements
  fixed-a-delegated-admin-sign-on-failure-issue: Fixed a Delegated Admin sign-on failure issue
  fixed-pluggable-pass-through-authentication-plugin-changes-not-taking-effect: Fixed Pluggable Pass-Through Authentication plugin changes not taking effect
  fixed-missing-updates-to-modifiersname-and-modifytimestamp: Fixed missing updates to modifiersName and modifyTimestamp
  fixed-a-password-change-time-issue-during-reencoding: Fixed a password change time issue during reencoding
  fixed-an-authentication-issue-in-the-pluggable-pass-through-authentication-plugin: Fixed an authentication issue in the Pluggable Pass-Through Authentication plugin
  fixed-an-issue-with-encrypted-changelog-recovery: Fixed an issue with encrypted changelog recovery
  fixed-an-issue-with-missing-attribute-updates-after-a-repair: Fixed an issue with missing attribute updates after a repair
  fixed-a-dsreplication-enable-failure: Fixed a dsreplication enable failure
  fixed-sasl-plain-binds-that-use-proxy-transformations: Fixed SASL PLAIN binds that use proxy transformations
  fixed-a-pingdirectoryproxy-startup-failure-with-undefined-external-server-locations: Fixed a PingDirectoryProxy startup failure with undefined external server locations
  fixed-unredacted-dns-in-the-sync-failed-ops-log: Fixed unredacted DNs in the sync-failed-ops log
  fixed-groups-object-class-mapping-omitting-top: Fixed groups object class mapping omitting top
  fixed-missing-description-attribute-mapping-for-active-directory-group-sync: Fixed missing description attribute mapping for Active Directory group sync
  fixed-a-benign-error-with-pingone-password-synchronization: Fixed a benign error with PingOne password synchronization
  fixed-attribute-mappings-filtering-on-absent-attributes: Fixed attribute mappings filtering on absent attributes
  fixed-an-npe-in-unboundidsyncdestination: Fixed an NPE in UnboundIDSyncDestination
  stopped-the-psa-msi-installer-from-showing-dialogs-during-silent-install: Stopped the PSA MSI installer from showing dialogs during silent install
  fixed-an-unnecessary-entry-rename-when-using-non-default-matching-rules: Fixed an unnecessary entry rename when using non-default matching rules
  fixed-the-psa-upgrade-path-from-versions-older-than-4-7: Fixed the PSA upgrade path from versions older than 4.7
  fixed-a-psa-installation-failure-related-to-the-character: "Fixed a PSA installation failure related to the # character"
  fixed-psa-command-line-installation: Fixed PSA command-line installation
  prevrel: Previous Releases
---

# Release notes

Unless otherwise noted, all of the following enhancements, known issues, and resolved issues apply to the PingDirectory server, the PingDirectoryProxy server, and the PingDataSync server.

Subscribe to get automatic updates: [icon: rss-square, set=fa][PingDirectory Release Notes RSS feed](pd_release_notes.xml)

|   |                                                                                                 |
| - | ----------------------------------------------------------------------------------------------- |
|   | This is a short-term support release. Learn more in [Release statuses](../release_status.html). |

## PingDirectory suite of products 11.1.0.0 (June 2026)

### Added runtime support for Java 25

New DS-50713 PingDirectory, PingDirectoryProxy, PingDataSync

We added JRE support for Oracle JDK 25 and OpenJDK 25.

|   |                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Consult the [upgrade considerations](../installing_the_pingdirectory_suite_of_products/pd_proxy_sync_upgrade_considerations.html) for Java-related actions you must take when upgrading to Java 25. |

### Added SMTP bearer access token authentication

New DS-48730 PingDirectory, PingDirectoryProxy, PingDataSync

The server now supports SMTP authentication by bearer access token. You can obtain a token through the OAuth 2.0 client credentials flow or configure a static token. Learn more in [Working with the SMTP Account Status Notification Handler](../pingdirectory_server_administration_guide/pd_ds_smtp_acct_status_notif_handler.html).

### Added scheduled data cleanup tasks

New DS-51377 PingDirectory

We added new single-run and recurring tasks that enable you to schedule server data cleanup, including PingFederate sessions and access grants.

The existing purge expired data plugin runs on a fixed 24-hour schedule from server startup, making it difficult to guarantee that large purge jobs run during a planned maintenance window. These new tasks allow you to reliably schedule purge operations so they don't run during peak business hours after an unexpected server restart or deployment.

### Added log mode for rate-limiting operations

New DS-50863 PingDirectory, PingDirectoryProxy, PingDataSync

To help tune rate-limiting operations and identify unusual client activity, you can now allow operations to exceed the configured per-connection and per-policy operation rates in a log mode. The server adds information about the client connections that exceed those rates to the error log.

Learn more in the configuration documentation included with the server for the Client Connection Policy properties `connection-operation-rate-exceeded-behavior` and `policy-operation-rate-exceeded-behavior`.

### Added a Kafka sync source

New DS-51133, DS-51297, DS-51301 PingDataSync Preview

We added a Kafka sync source, which you can use to apply changes published in a Kafka topic to a sync destination. Learn more in [Synchronize with Apache Kafka](../pingdatasync_server_administration_guide/pd_sync_with_apache_kafka.html).

As part of this implementation:

* We added the `consumer-property` and `sensitive-consumer-property` configuration parameters to Kafka cluster external servers. These parameters enable passing standard and sensitive configuration properties to the Kafka consumer on the PingDataSync server.

* We added the JSON sync operation mapping configuration, which allows a Kafka sync source to map arbitrary JSON messages to a sync operation.

|   |                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This feature is provided as a **Preview**, which means that it isn't supported and should not be used in production environments. Learn more in [Feature statuses](../feature_status.html). |

### Updated the Password Sync Agent to version 4.9

New DS-44517 PingDataSync

We updated the Password Sync Agent (PSA) to version 4.9.

### Added certificate trust configuration for the PSA

New DS-44517 PingDataSync

You can now configure the PSA to either trust all certificates presented by the PingDataSync server or to use the Windows Certificate Authority for validation.

### Improved connection-asymmetry alarm visibility

Improved DS-49225 PingDirectory, PingDirectoryProxy, PingDataSync

You can now quickly identify peers causing topology connection-asymmetry alarms. The mirrored subtree manager monitor entry automatically includes the `peer-inbound-only` and `peer-outbound-only` attributes if any servers appear in only the inbound or outbound connection set. Connection-asymmetry alarm messages include the names of the peers involved.

### Improved server startup time on Linux

Improved DS-50645 PingDirectory, PingDirectoryProxy, PingDataSync

To reduce server startup time when you run `start-server`, we reduced the number of Java processes that get created before starting the server. This change applies to Linux only and is enabled by default.

|   |                                                                                                                                                                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In deployments that run multiple server instances per node, parallel server startups can increase short-term CPU load, because JVM initialization occurs at the same time across instances. This effect might be more pronounced with this improvement enabled.To revert to the prior behavior, set the environment variable `UNBOUNDID_FAST_START` to `false`. |

### Improved composite index selection for substring filters

Improved DS-50820, DS-51183 PingDirectory

We improved the logic the server uses to prioritize composite index usage when evaluating substring filters.

### Improved Prometheus metric family grouping

Improved DS-51115 PingDirectory, PingDirectoryProxy, PingDataSync

The Prometheus Monitoring HTTP Servlet Extension now groups metrics with the same name under common `HELP` and `TYPE` headers, more closely following the standard for annotating metric families in Prometheus.

### Made `allow-upgrading-to-composite-index` editable on existing indexes

Improved DS-51180 PingDirectory

You can use the `allow-upgrading-to-composite-index` property, in the attribute index configuration, to specify whether the server should store an attribute index in its legacy form or update it to use a composite index behind the scenes.

Previously, this property was declared as read-only, and you could only specify its value when creating a new attribute index. Now, you can edit the property for existing indexes, although the server continues to maintain the index in its current form until you export the data to LDIF and re-import it.

Composite indexes are more scalable and versatile than legacy attribute indexes, although there could be cases where the server exhibits better performance for attribute indexes stored in the legacy format.

### Added detection for deleted recovered Active Directory entries

Improved DS-50203 PingDataSync

PingDataSync now detects when recovered Active Directory entries get deleted.

### Improved deep JSON field support in constructed attribute mappings

Improved DS-51186 PingDataSync

You can now reference JSON fields that are multiple levels deep when building constructed attribute mappings.

For example, suppose an organization stores all user contact information in a JSON object in the `contact` attribute. This might result in a deeply nested path to the user's email address. With this change, you can extract that email value by referencing something like `{contact.ubidEmailJSON.value}` in the `value-pattern` parameter.

This change also adds support for automatically expanding intermediate JSON arrays in the path. Intermediate JSON arrays produce multiple values in the expected way.

|   |                                                                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This enhancement doesn't change the constructed attribute mapping behavior for JSON attribute field keys that contain a dot. When there's ambiguity as to whether a dot is part of a field name or a separator between field names, the parser interprets the dot as part of the field name. |

### Improved schema element registration error messages

Improved DS-51300 PingDirectory, PingDirectoryProxy

We clarified and enhanced the error messages displayed when schema elements can't be registered with the schema.

### Improved access control rule parsing and validation

Improved DS-51399 PingDirectory, PingDirectoryProxy, PingDataSync

We added a new mechanism for parsing and validating access control rules. The new parser runs alongside the existing one and might help identify problematic ACIs and provide more useful error messages for malformed rules.

All currently valid ACIs continue to be accepted and operate as before. The server raises an administrative alert upon encountering any ACIs not supported by the new parser.

|   |                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------- |
|   | We plan to remove the existing parser in a future release. At that time, ACIs flagged by the new parser won't be permitted. |

### Improved `verify-index` schema consistency detection

Improved DS-51409 PingDirectory

The `verify-index` tool now checks for entries whose DN2ID index key can't be found because an attribute syntax or matching rule was altered after the entry was created.

|   |                                                                                                                                                                                                                 |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Altering the schema definition of an attribute syntax or matching rule might cause existing entries to become inaccessible through LDAP search until the backend contents are exported to LDIF and re-imported. |

### Added alerts for LDAP schema element changes

Improved DS-51360 PingDirectory

The server now raises an `existing-schema-element-changed` alert and logs a `SEVERE_WARNING` if existing schema elements are modified or deleted using LDAP. Adding new schema elements logs a `NOTICE` but doesn't raise an alert.

### Improved PSA logging for connection errors

Improved DS-44665, DS-44686, DS-49012, DS-51082 PingDataSync

We improved logging in the PSA for connection errors and DNS resolution failures.

### Removed SCIM 1.1 support

Info DS-49199 PingDirectory, PingDirectoryProxy, PingDataSync

We removed SCIM 1.1 and related functionality from the server. Migrate any functionality to SCIM 2.0.

|   |                                                                                                                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If the server uses SCIM 1.1, you must remove the servlet extensions from all HTTP connection handlers before upgrading. For example:```
$ bin/dsconfig set-connection-handler-prop \
    --handler-name "HTTPS Connection Handler" \
    --remove http-servlet-extension:SCIM
``` |

### Deprecated support for the Implicit grant type

Info DS-51671 Delegated Admin

We deprecated support for the Implicit grant type and will remove it in a future release. Use the Authorization Code with PKCE grant type instead. Learn more in [Changing the default OIDC grant type](../delegated_admin_application_guide/pd_da_change_oidc_grant_type.html).

### Removed the Swagger UI and schema generation endpoints

Info DS-50931 PingDirectory, PingDirectoryProxy, PingDataSync

We removed the Swagger UI and API endpoints for generating Swagger schema from the Consent and SCIM 2.0 APIs. Learn more about using these APIs in the [developer documentation](https://developer.pingidentity.com/pingdirectory/directory/introduction.html).

### Updated the opencsv library

Info DS-51436 PingDirectory, PingDirectoryProxy, PingDataSync

We updated the opencsv library from the abandoned `net.sf.opencsv 2.3` to `com.opencsv 5.10`.

### Upgraded the embedded HTTP server to Jetty 12

Info DS-51450 PingDirectory, PingDirectoryProxy, PingDataSync

We upgraded the embedded HTTP server from Jetty 11 to Jetty 12. Most behavior is preserved, with the following exceptions:

* HTTP requests with unencoded reserved characters in path segments (for example, a literal forward slash in a distinguished name such as `/directory/v1/sn=Sch/m*i^d`) now receive a `400 Bad Request` response instead of being silently truncated at the reserved character. Clients using the Directory REST API, SCIM API, or any other HTTP servlet extension must percent-encode reserved characters in URL path segments. For example, encode a forward slash as `%2F`, a caret as `%5E`, and a question mark as `%3F`. This requirement is specified in RFC 3986 and is now enforced.

* The `Location` header in HTTP redirect responses now always contains an absolute URI as required by RFC 7231. Update any clients that relied on a relative URI in this header.

### Removed the x86 version of the PSA

Info DS-51333, DS-51351 PingDataSync

We removed the x86 version of the PSA.

### Installing the PSA on Windows Server 2016

Info DS-51525 PingDataSync

You can now install the PSA, version 4.8 and later, on Windows Server 2016. This is an unsupported Windows version and could result in erroneous PSA behavior. The installer displays a warning advising that Windows Server 2016 isn't supported.

### Fixed a TLS 1.3 connection termination issue

Fixed DS-51445 PingDirectory, PingDirectoryProxy, PingDataSync

We fixed an issue that could cause a small percentage of LDAP connections secured with TLS 1.3 to be prematurely terminated.

### Fixed the `--nodetach` option for `start-server`

Fixed DS-51565 PingDirectory, PingDirectoryProxy, PingDataSync

We fixed the `--nodetach` option for `start-server` so that it correctly prevents the server from starting in a detached manner.

### Fixed a `manage-profile replace-profile` error

Fixed DS-51396 PingDirectory, PingDirectoryProxy, PingDataSync

We fixed an issue where the `manage-profile replace-profile` tool could fail with a `DirectoryNotEmptyException` error during upgrades in environments where the `logs` directory was mounted as a separate volume. This failure was caused by the tool holding an internal lock on a background optimization file during the upgrade process. Now, the tool correctly releases these locks and skips the migration of non-essential cache files.

Additionally, we fixed a defect where the `setup` tool didn't always correctly apply the `--optionCacheDirectory` argument.

### Fixed `manage-profile generate-profile` omitting obscured properties

Fixed DS-51245 PingDirectory, PingDirectoryProxy, PingDataSync

We fixed an issue where, after an upgrade, `manage-profile generate-profile` excluded `dsconfig` commands from the profile that set obscured properties.

### Fixed a server shutdown delay issue

Fixed DS-51291 PingDirectory, PingDirectoryProxy, PingDataSync

We fixed an issue where a large number of peer connections or unresponsive peers could cause excessively long server shutdown times.

### Fixed an SLF4J startup warning

Fixed DS-50990 PingDirectory, PingDirectoryProxy, PingDataSync

We resolved the following server startup warning:

`SLF4J(E): A service provider failed to instantiate: org.slf4j.spi.SLF4JServiceProvider: Provider org.slf4j.impl.PingSLF4JServiceProvider not found.`

### Fixed admin console icons in closed environments

Fixed DS-50165 PingDirectory, PingDirectoryProxy, PingDataSync

We fixed an issue where the admin console didn't properly display icons when running in an environment without internet access, such as a closed environment.

### Fixed false-positive conflicts for the Unique Attribute plugin

Fixed DS-51327 PingDirectory

We fixed an issue where the Unique Attribute plugin could report a false-positive conflict. This could happen when a single LDAP operation modified multiple subtypes of the same unique attribute on the same entry.

### Fixed an LDAP changelog issue with subtree deletions

Fixed DS-51456 PingDirectory, PingDataSync

We fixed an issue where the server didn't correctly generate LDAP changelog records for subtree deletions. Records could be written out of order on the target server, preventing reliable replay on other destinations. Servers replicating the request could include only the base subtree delete without records for subordinate entry deletions.

### Fixed changelog ordering for subtree deletes

Fixed DS-50986 PingDirectory, PingDataSync

We fixed an issue where subtree delete operations were recorded out of order in the changelog for servers in a replication topology.

### Fixed identity mapper errors for unavailable base DNs

Fixed DS-51149 PingDirectory, PingDirectoryProxy

We fixed an issue where an identity mapper would throw an error when one or more configured match base DNs were unavailable. We also added a `tolerate-unavailable-base-dn` configuration property to identity mapper objects to control the behavior of the mapper in this scenario.

### Fixed REST API errors for unknown schema elements

Fixed DS-51230 PingDirectory, PingDirectoryProxy

We fixed internal server errors that could occur when using the REST API with attribute types or object classes not present in the schema.

### Fixed a `replication-missing-changes` alarm error message

Fixed DS-48998 PingDirectory

We fixed a benign `null generator` error message that could appear when the server cleared `replication-missing-changes` alarms.

### Fixed schema file ordering for dependent schema elements

Fixed DS-51524 PingDirectory

We fixed an issue where a running server would allow dependent schema elements to be registered in a file that would be loaded later than the elements they depended on. This wouldn't cause immediate issues but would prevent the server from restarting until the schema files were modified to correct the misordering.

### Fixed a Delegated Admin sign-on failure issue

Fixed DS-51475 PingDirectory

We fixed an issue where signing on to Delegated Admin would fail because of how some access token validators handled client secrets containing URL special characters.

### Fixed Pluggable Pass-Through Authentication plugin changes not taking effect

Fixed DS-51459 PingDirectory

We fixed an issue where changes to the `pass-through-authentication-handler` property on a Pluggable Pass Through Authentication plugin made using `dsconfig` wouldn't take effect until the plugin was disabled and reenabled.

### Fixed missing updates to `modifiersName` and `modifyTimestamp`

Fixed DS-51353 PingDirectory

We fixed an issue where several tools, plugins, and extended operations that rely on internal operations to modify entries wouldn't update the `modifiersName` and `modifyTimestamp` values on those entries.

### Fixed a password change time issue during reencoding

Fixed DS-51349 PingDirectory

We fixed an issue where reencoding an entry's password also updated its `pwdChangedTime` attribute.

### Fixed an authentication issue in the Pluggable Pass-Through Authentication plugin

Fixed DS-51137 PingDirectory

We fixed an issue in the Pluggable Pass-Through Authentication plugin where successful sign-ons were recorded as authentication failures when `try-local-bind` was enabled. Now, users won't be incorrectly locked out due to valid pass-through authentications.

### Fixed an issue with encrypted changelog recovery

Fixed DS-51147 PingDirectory

We fixed an issue where the server didn't initialize the changelog backend's encryption tokenizer when data encryption was enabled, preventing encrypted changelog recovery after unscheduled shutdowns.

### Fixed an issue with missing attribute updates after a repair

Fixed DS-51487 PingDirectory

We fixed an issue where a replica could silently miss attribute updates after the Replication Repair control was used to delete an entry on that replica, and then the entry was later re-added. Other replicas would have the updated attribute, while the affected replica didn't.

### Fixed a `dsreplication enable` failure

Fixed DS-51095 PingDirectory

We fixed an issue where `dsreplication enable` wouldn't execute successfully on PingDirectory servers with `Sensitive Password Attributes` enabled.

### Fixed SASL PLAIN binds that use proxy transformations

Fixed DS-51350 PingDirectoryProxy

We fixed an issue where SASL PLAIN bind requests failed when passing through DN-mapping or attribute-mapping proxy transformations.

### Fixed a PingDirectoryProxy startup failure with undefined external server locations

Fixed DS-51125 PingDirectoryProxy

We fixed an issue where PingDirectoryProxy would fail to start when using automatic backend discovery against external server instances with a location not defined in PingDirectoryProxy's configuration.

### Fixed unredacted DNs in the `sync-failed-ops` log

Fixed DS-51558 PingDataSync

We fixed an issue where the server could write unredacted entry DNs to the `sync-failed-ops` log, even when `log-redaction-regex` was configured. Now, the server applies the configured redaction patterns to the DN field in `sync-failed-ops` log entries, consistent with how they are applied to message text.

### Fixed groups object class mapping omitting `top`

Fixed DS-47327 PingDataSync

We fixed an issue where the `create-sync-pipe-config` wizard generated a groups object class mapping that omitted `top`. This caused the server to detect groups as out-of-sync on every change and incorrectly apply a modify operation to the sync destination, even when no mapped attribute had changed. This issue didn't affect user entries.

### Fixed missing `description` attribute mapping for Active Directory group sync

Fixed DS-47329 PingDataSync

We fixed an issue where the `create-sync-pipe-config` wizard didn't include a `description` attribute mapping when generating the groups attribute map for synchronization from PingDirectory to Active Directory. This caused group `description` changes to be silently dropped by the sync pipe.

The wizard now also prompts for a separate source base DN for groups, allowing you to specify a different OU than the one for users.

### Fixed a benign error with PingOne password synchronization

Fixed DS-45978 PingDataSync

We fixed an issue where password synchronizations to PingOne would log a benign error about schema failures.

### Fixed attribute mappings filtering on absent attributes

Fixed DS-44411 PingDataSync

We fixed an issue where attribute mappings with conditional value patterns that filtered on the absence of an attribute wouldn't properly map any values.

### Fixed an NPE in `UnboundIDSyncDestination`

Fixed DS-47105 PingDataSync

We fixed an issue where `UnboundIDSyncDestination` would throw a `NullPointerException` when a `LDAPSyncDestinationPlugin` returned `PreStepResult.ABORT_OPERATION` for a `preCreate` or `preModify` call and the entry or modification set contained password-policy-state attributes, such as `pwdAccountLockedTime`.

### Stopped the PSA MSI installer from showing dialogs during silent install

Fixed DS-51464 PingDataSync

We fixed an issue where the PSA MSI installer would display dialog boxes during silent installations (`/qn` or `/passive`), blocking automated deployment scripts. The installer now honors quiet mode flags and logs messages instead of showing popups.

### Fixed an unnecessary entry rename when using non-default matching rules

Fixed DS-51458 PingDataSync

We fixed an issue where the server could attempt to rename an entry to its existing DN in the following scenario:

* The RDN attribute used a non-default matching rule (such as `telephoneNumberMatch`).

* The sync class was configured for byte-for-byte attribute comparison.

* `creates-as-modifies` was enabled.

Now, the server normalizes both DNs using the destination schema before comparison.

### Fixed the PSA upgrade path from versions older than 4.7

Fixed DS-49011, DS-51319 PingDataSync

We fixed the upgrade process for the PSA:

* We blocked direct upgrades from versions older than 4.7:

  * Previously, an upgrade from those versions wouldn't complete properly because of significant changes in version 4.7.

  * Now, the installer prompts you to uninstall the old PSA before installing version 4.7 or later.

* We updated messaging around restarts to clarify that a reboot is only required when prompted by the Windows operating system.

### Fixed a PSA installation failure related to the `#` character

Fixed DS-50788, DS-51233 PingDataSync

We fixed an issue where installing the PSA failed when passwords contained the `#` character.

### Fixed PSA command-line installation

Fixed DS-13850 PingDataSync

We fixed an issue where the PSA overrode or deleted values during command-line installation.

## Previous Releases

Learn more about enhancements and issues resolved in previous major and minor releases of PingDirectory products using the following links:

* [11.0](https://docs.pingidentity.com/pingdirectory/11.0/release_notes/pd_release_notes.html)

* [10.3](https://docs.pingidentity.com/pingdirectory/10.3/release_notes/pd_release_notes.html)

* [10.2](https://docs.pingidentity.com/pingdirectory/10.2/release_notes/pd_release_notes.html)