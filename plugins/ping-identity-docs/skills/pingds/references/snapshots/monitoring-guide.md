---
title: Alerts
description: Configure PingDS alert notifications over JMX or email, and review the full list of server alert types.
component: pingds
version: 8.1
page_id: pingds:monitoring-guide:alert-notifications
canonical_url: https://docs.pingidentity.com/pingds/8.1/monitoring-guide/alert-notifications.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Monitoring", "Troubleshooting"]
section_ids:
  jmx_alerts: JMX alerts
  mail_alerts: Mail alerts
  alert-types: Alert types
---

# Alerts

DS servers can send alerts for significant server events.

## JMX alerts

The following example enables JMX alert notifications:

```console
$ dsconfig \
 set-alert-handler-prop \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --handler-name "JMX Alert Handler" \
 --set enabled:true \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
```

## Mail alerts

The following example sets up an SMTP server, and configures email alerts:

```console
$ dsconfig \
 create-mail-server \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --server-name "SMTP server" \
 --set enabled:true \
 --set auth-username:mail.user \
 --set auth-password:password \
 --set smtp-server:smtp.example.com:587 \
 --set trust-manager-provider:"JVM Trust Manager" \
 --set use-start-tls:true \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
$ dsconfig \
 create-alert-handler \
 --hostname localhost \
 --port 4444 \
 --bindDN uid=admin \
 --bindPassword password \
 --handler-name "SMTP Alert Handler" \
 --type smtp \
 --set enabled:true \
 --set message-subject:"DS Alert, Type: %%alert-type%%, ID: %%alert-id%%" \
 --set message-body:"%%alert-message%%" \
 --set recipient-address:kvaughan@example.com \
 --set sender-address:ds@example.com \
 --trustStorePath /path/to/opendj/config/keystore \
 --trustStoreType PKCS12 \
 --trustStorePassword:file /path/to/opendj/config/keystore.pin \
 --no-prompt
```

## Alert types

DS servers use the following alert types. For alert types that indicate server problems, check `logs/errors` for details:

* `org.opends.server.AccessControlDisabled`

  The access control handler has been disabled.

* `org.opends.server.AccessControlEnabled`

  The access control handler has been enabled.

* `org.opends.server.authentiation.dseecompat.ACIParseFailed`

  The dseecompat access control subsystem failed to correctly parse one or more access control instruction (ACI) *(tooltip: \<div class="paragraph">
  \<p>An instruction or rule that can be used to grant or deny access to users to perform operations on a server.\</p>
  \</div>)* rules when the server first started.

* `org.opends.server.BackupFailure`

  A backup has failed.

* `org.opends.server.BackupSuccess`

  A backup has completed successfully.

* `org.opends.server.CannotCopySchemaFiles`

  A problem has occurred while attempting to create copies of the existing schema configuration files before making a schema update, and the schema configuration has been left in a potentially inconsistent state.

* `org.opends.server.CannotRenameCurrentTaskFile`

  The server is unable to rename the current tasks backing file in the process of trying to write an updated version.

* `org.opends.server.CannotRenameNewTaskFile`

  The server is unable to rename the new tasks backing file into place.

* `org.opends.server.CannotScheduleRecurringIteration`

  The server is unable to schedule an iteration of a recurring task.

* `org.opends.server.CannotWriteConfig`

  The server is unable to write its updated configuration for some reason and therefore the server may not exhibit the new configuration if it is restarted.

* `org.opends.server.CannotWriteNewSchemaFiles`

  A problem has occurred while attempting to write new versions of the server schema configuration files, and the schema configuration has been left in a potentially inconsistent state.

* `org.opends.server.CannotWriteTaskFile`

  The server is unable to write an updated tasks backing file for some reason.

* `org.opends.server.DirectoryServerShutdown`

  The server has begun the process of shutting down.

* `org.opends.server.DirectoryServerStarted`

  The server has completed its startup process.

* `org.opends.server.DiskFull`

  Free disk space has reached the full threshold.

  Default is 6% of the size of the file system.

* `org.opends.server.DiskSpaceLow`

  Free disk space has reached the low threshold.

  Default is 10% of the size of the file system.

* `org.opends.server.EnteringLockdownMode`

  The server is entering lockdown mode, wherein only root users are allowed to perform operations and only over the loopback address.

* `org.opends.server.LDAPHandlerDisabledByConsecutiveFailures`

  Consecutive failures have occurred in the LDAP connection handler and have caused it to become disabled.

* `org.opends.server.LDAPHandlerUncaughtError`

  Uncaught errors in the LDAP connection handler have caused it to become disabled.

* `org.opends.server.LDIFBackendCannotWriteUpdate`

  An LDIF backend was unable to store an updated copy of the LDIF file after processing a write operation.

* `org.opends.server.LDIFConnectionHandlerIOError`

  The LDIF connection handler encountered an I/O error that prevented it from completing its processing.

* `org.opends.server.LDIFConnectionHandlerParseError`

  The LDIF connection handler encountered an unrecoverable error while attempting to parse an LDIF file.

* `org.opends.server.LeavingLockdownMode`

  The server is leaving lockdown mode.

* `org.opends.server.ManualConfigEditHandled`

  The server detects that its configuration has been manually edited with the server online, and those changes were overwritten by another change made through the server. The manually edited configuration will be copied to another location.

* `org.opends.server.ManualConfigEditLost`

  The server detects that its configuration has been manually edited with the server online, and those changes were overwritten by another change made through the server. The manually edited configuration could not be preserved due to an unexpected error.

* `org.opends.server.replication.UnresolvedConflict`

  Multimaster replication cannot resolve a conflict automatically.

* `org.opends.server.UncaughtException`

  A server thread has encountered an uncaught exception that caused that thread to terminate abnormally. The impact that this problem has on the server depends on which thread was impacted and the nature of the exception.

* `org.opends.server.UniqueAttributeSynchronizationConflict`

  A unique attribute conflict has been detected during synchronization processing.

* `org.opends.server.UniqueAttributeSynchronizationError`

  An error occurred while attempting to perform unique attribute conflict detection during synchronization processing.
